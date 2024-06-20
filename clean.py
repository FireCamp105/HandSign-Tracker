# %%
import cv2
import mediapipe as mp
import tensorflow as tf
import numpy as np
from ordre import get_value_from_json, execute_command
# Load your trained model
model = tf.keras.models.load_model('./mnadhem.h5')
classes=['Open Hand',"Peace Sign", "Thumb's up", "point up",'OK!','call Sign',"devil horns"]
# Initialize MediaPipe hand landmark model
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()

import os


# %%
len(classes)

# %%
import json
# Open the JSON file in read mode
with open('./resources/app/src/IMPORTANT/HandMacros.json', 'r') as file:
    # Load the JSON data into a Python dictionary
    handMacros = json.load(file)

# Now you can work with the 'data' dictionary
# For example, print it
print(handMacros)

# %%
with open('./resources/app/src/IMPORTANT/CAM.json', 'r') as file:
    # Load the JSON data into a Python dictionary
    camadress = json.load(file)
# %% 'http://192.168.1.100:8080/video'
# Launch an IP camera instance
cap = cv2.VideoCapture(camadress)
cap.set(cv2.CAP_PROP_FPS, 1)
cv2.namedWindow('Sign Prediction', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Sign Prediction', 640, 480)
while cap.isOpened():
    
    success, image = cap.read()
    if not success:
        break

    # Convert the image to RGB and pass it to the MediaPipe hand landmark model
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    rgb_image= cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = hands.process(image)
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            # Assuming hand_landmarks is the array of landmarks obtained from MediaPipe
            # Preprocess the hand landmarks for prediction
            x_coordinates = [landmark.x for landmark in hand_landmarks.landmark]
            y_coordinates = [landmark.y for landmark in hand_landmarks.landmark]
            z_coordinates = [landmark.z for landmark in hand_landmarks.landmark]

            # Combine the x, y, and z coordinates into a single input array
            input_data = np.array([x_coordinates, y_coordinates, z_coordinates])             
            input_data = input_data.reshape(1, -1)  # Assuming the model takes a single sample as input # Reshape the input to match the model's expected input shape
            # # Make a prediction using the preprocessed input
            prediction = model.predict(input_data, verbose=0) #verbose = anything besides 0 causes a crush because AGHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH
            # Assuming you have the prediction result in a variable named 'prediction'
            # Assuming 'image' is the captured frame
            predicted_class = np.argmax(prediction)   # Adding 1 to convert 0-based index to 1-based class

            execute_command(handMacros[classes[predicted_class]]) # <------------------------------------------ IMPORTANT
            confidence = prediction[0][predicted_class]  # Confidence for the predicted class

            # Draw the predicted sign on the image
            
            
            cv2.putText(rgb_image, f"Predicted Class {classes[np.argmax(prediction)]} with {((confidence)*100):.2f}% confidence sum = {prediction.sum():.2f}, command found: =  {handMacros[classes[predicted_class]]}", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            for i in range(0,7):
                cv2.putText(rgb_image, f" Class {classes[i]} with {prediction[0][i]*100:.2f}% confidence ", (50, 100+ 50*i), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    # Display the image with the predicted sign
    cv2.imshow('Sign Prediction', rgb_image)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

