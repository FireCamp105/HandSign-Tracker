<template>
  <v-app >
    <v-layout>
      <v-main>
          <div  class="position-relative">
            <v-card-text>
              <img src="./fatyoshi.png"  class="position-absolute" style="top:0; right: 0; margin-right: 48px ; margin-top: 24px; " alt="IT IS OUR APP WLH">
              <div class="text-h2">Hand Tracker</div>
              <v-icon>mdi-heart-cog-outline</v-icon>
              <div class="text-amber text-h6">by Hamza Hanbli, Mohamed Sedki bannour & Amel Bahloul!</div>
              
            </v-card-text>
            
              <v-container
                class="px-0"
                fluid
              > 
                <div class=" d-flex justify-space-evenly" >
                  <v-col class="rounded-xl position-relative" style="min-width:50%; max-width: 75%; min-height: 22ch;">
                    <v-radio-group v-model="camChoice" inline>
                      <v-radio label="WebCam" :value="0" v-on:click="camref = '0'" ></v-radio>
                      <v-radio label="IP Cam" :value="'IP Cam'"></v-radio>
                    </v-radio-group>
                    <v-text-field style="min-width:20ch; max-width: 40ch;" v-if="camChoice == 'IP Cam'"
                          density="compact"
                          name="cam address"
                          v-model="camref"
                          > 
                    </v-text-field>
                    <div class=" position-absolute" style="bottom: 0; right: 0;margin-right: 24px ; margin-bottom: 24px;" >
                      <v-btn 
                       color="info" class="mr-5" style="min-width:20ch ;" @click="SaveC()">SAVE</v-btn> 
                    </div>
                  </v-col>
                  <div class="d-flex align-start flex-column mb-6  position-relative" style="min-width:10%; max-width: 25%; justify-content: space-evenly;">
                    
                      <v-btn color="amber"   style="min-width:20ch ;"@click="saveF()" class="">
                        Save to File</v-btn>
                      <v-btn color="success" style="min-width:20ch ;" @click="deploy()">DEPLOY</v-btn>
                      <!-- <v-btn color="error"   style="min-width:20ch ;"@click="CloseScript()">CLOSE</v-btn> -->
                    
                  </div>
                </div>
                
              </v-container>
          <v-expansion-panels style="max-width:100%; padding:10px;" variant="popout">
            <v-expansion-panel 
            v-for=",jsonSign in HandJson" 
              :title="jsonSign +' :  '+   handMacros[jsonSign] "
            >
              <v-expansion-panel-text>  
                  <v-list>
                    <v-list-item v-for=",Choice in ChoicesJson " class="rounded-e-lg mx-auto" base-color="light-green" v-on:click="save(Choice,jsonSign)" color="light-green">
                        
                        <v-icon icon="mdi-ray-start-arrow" start></v-icon>{{Choice}} <span v-if="Choice == 'open website'">: {{ customURL }} </span> 
                        <v-text-field v-if="Choice == 'open website'"
                        density="compact"
                        name="name"
                        v-model="customURL"
                        placeholder="www.example.com"
                        :label="jsonSign"
                        id="id"
                        >
                        </v-text-field> 
                        <v-text-field v-if="Choice == 'call process'"
                        density="compact"
                        name="name"
                        v-model="processURL"
                        placeholder="C:/example/location/example.exe"
                        :label="jsonSign"
                        id="id"
                        >
                        </v-text-field>
                        <v-slider v-if="Choice == 'angle PWM'"
                          v-model="angleSlider"
                          max=180
                          min=0
                          step=1
                          style="margin-left: 5%;"
                          hide-details
                        >
                          <template v-slot:append>
                            <v-text-field
                              v-model="angleSlider"
                              density="compact"
                              style="width: 5rem;"
                              type="number"
                              hide-details
                              single-line
                              Readonly
                            ></v-text-field>
                          </template>
                        </v-slider>

                    </v-list-item>
                  </v-list>
                  </v-expansion-panel-text>
            </v-expansion-panel>
                
          </v-expansion-panels>
        </div>
      </v-main >
    </v-layout>
  </v-app>

</template>

<script setup>
import HandJson from './IMPORTANT/HandMacros.json';
import ChoicesJson from './IMPORTANT/Choices.json';
import cam from './IMPORTANT/CAM.json';
import { ref } from 'vue';

const filepath = './resources/app/src/IMPORTANT/HandMacros.json';
const campath = './resources/app/src/IMPORTANT/CAM.json';


const handMacros = ref(HandJson);
const camref = ref(cam['cam']);
const customURL= ref("");
const processURL= ref("");
const angleSlider = ref(0);
const camChoice = ref(1);
function save(Choice,jsonSign) { 
  switch(Choice){
    case "angle PWM":
        handMacros.value[jsonSign] = "PWM: " + angleSlider.value;
      break;
    case "open website":
      handMacros.value[jsonSign] ="URL: " + customURL.value;
      customURL.value = "";
      break;
    case "youtube":
      handMacros.value[jsonSign] ="URL: " + "https://www.youtube.com/";
      break;
    case "facebook":
      handMacros.value[jsonSign] ="URL: " + "https://www.facebook.com/";
      break;
    case "spotify":
      handMacros.value[jsonSign] ="URL: " + "https://open.spotify.com/";
      break;
    case "call process":
      handMacros.value[jsonSign] ="SHORTCUT: " + processURL.value;
      processURL.value = "";
      break;
    case "shutdown pc in 5 minutes shutdown":
      handMacros.value[jsonSign] ="SHORTCUT: SHUTDOWNPC.BAT";
      break;
    case "abort shutdown before timer expires":
      handMacros.value[jsonSign] ="SHORTCUT: ABORTSHUTDOWN.BAT";
      break;
    default:
      handMacros.value[jsonSign] = Choice;
  }
}

//import console.log
const saveF = () => {
  window.electron.SaveFile(filepath, JSON.stringify( handMacros.value, null, 2));
}
const SaveC = () => {
  window.electron.SaveFile(campath, JSON.stringify( camref.value, null, 2));
}
const deploy = () =>{
  console.log("deploying");
  //window.electron.Children();
  window.electron.PythonFunction();
}

const CloseScript = () =>{
  console.log("closing");
  window.electron.KillPython();
}
</script>