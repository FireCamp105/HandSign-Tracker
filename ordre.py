import json
import sys
import time
import webbrowser
import subprocess

import firebase_admin
from firebase_admin import db
cred_obj = firebase_admin.credentials.Certificate('esp32firebasekey.json')

default_app = firebase_admin.initialize_app(cred_obj, {
	'databaseURL':"https://esp32bs-default-rtdb.europe-west1.firebasedatabase.app"
	})
refPWM = firebase_admin.db.reference("/ESPPWM")
refSwitch = firebase_admin.db.reference("/ESPSWITCH")
def get_value_from_json(json_file, key):
    with open(json_file, 'r') as file:
        data = json.load(file)
        return data.get(key)

last_execution_time = 0
def execute_command(value):

    global last_execution_time, refPWM, refSwitch

    current_time = time.time()
    if current_time - last_execution_time >= 5:
        print(value)
        if value.startswith("URL: "):
            url = value.replace("URL: ", "")
            webbrowser.open(url)

        elif value.startswith("switch"):
            if(refSwitch.get()):
                refSwitch.set(False)
            else:
                refSwitch.set(True)
            

        elif value.startswith("PWM:"):
            refPWM.set(int(value.replace("PWM: ", "")))

        elif value.startswith("SHORTCUT: "):
            shortcut= value.replace("SHORTCUT: ", "")
            subprocess.Popen([shortcut], shell=True)


        elif value.startswith("CLOSEAPP"):
            sys.exit()
        elif value.startswith("SHUTDOWNPC"):
            shortcut= value.replace("SHORTCUT: ", "")
            subprocess.Popen(["SHUTDOWNPC.BAT"], shell=True)
        elif value.startswith("ABORTSHUTDOWN"):
            subprocess.Popen(["ABORTSHUTDOWN.BAT"], shell=True)
        else:
            print("No action defined for this value.")

        last_execution_time = current_time