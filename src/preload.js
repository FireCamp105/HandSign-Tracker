// See the Electron documentation for details on how to use preload scripts:
// https://www.electronjs.org/docs/latest/tutorial/process-model#preload-scripts

const { contextBridge, ipcRenderer } = require('electron');
const fs = require('fs');
const path = require('path');


// Define the fswrite function
// const fsSaveConfig = (filepath, selectedSign, selectedMacroOption) => {
//   console.log(path.resolve(filepath));
//   const configData = require(path.resolve(filepath));
//   console.log(configData);
//    // Read the existing config data
//   configData[selectedSign] = selectedMacroOption; // Update the value for the selectedSign key

//   const newData = JSON.stringify(configData, null, 2); // Convert the updated data back to JSON format

//   // Write the updated data back to the file
//   fs.writeFile(filepath, newData, (err) => {
//     if (err) {
//       console.error(err);
//       return;
//     }
//     console.log('File updated successfully');
//   });
// };
const SaveFile = (filepath,muhdata) => {
    fs.writeFile(filepath, muhdata, (err) => {
    if (err) {
      console.error(err);
      return;
    }
    console.log('File updated successfully');
  });
};


//const spawn = require("child_process").spawn;
//var Child = null;
// const PythonFunction = () => {
//     Child = spawn('python',["./clean.py"], { cwd: 'c:/dev-is-hard/vueapp', detached: true });
//     console.log(`running in child process with PID ${process.pid}`);
//     console.log('Please e5dem');
// };
const { exec } = require('child_process');
const { cwd } = require('process');
console.log(`Current directory: ${cwd()}`);
function PythonFunction() {
    exec(`python "clean.py"`, (error, stdout, stderr) => {
        if (error) {
            console.error(`exec error: ${error}`);
            return;
        }
        console.log(`stdout: ${stdout}`);
        console.error(`stderr: ${stderr}`);
    });
    console.log(`CurrentA AAAAA directory: ${cwd()}`);
 }
const spawn = require("child_process").spawn;
var Child = null;

function Children() {
    Child = spawn('python',["clean.py"], );
    console.log(`running in child process with PID ${process.pid}`);
    console.log('Please e5dem');
}
const KillPython = () => {
  if (Child != null) {
    
    Child.kill();
    console.log(Child);
    Child = null;
  }
  else {
    console.log("Child Not Found");
    console.log(Child);
  }
}
// const SaveCam = (filepath,muhdata) => {
//   fs.writeFile(filepath, muhdata, (err) => {
//     if (err) {
//       console.error(err);
//       return;
//     }
//     console.log('File updated successfully');
//   });
  
// }
// Expose the fsSaveConfig function
contextBridge.exposeInMainWorld('electron', {
  SaveFile: SaveFile,
  PythonFunction: PythonFunction,
  KillPython: KillPython,
  Children: Children
});


// const fsSaveConfig = (filepath, selectedSign,selectedMacroOption ) => {
//   if ((selectedSign != "" )&& (selectedMacroOption != "")) {


//     const data = selectedSign + "," + selectedMacroOption; // data 

//     fs.writeFile(filepath, data, (err) => {
//       if (err) {
//         console.error(err);
//         return;
//       }
//       console.log('File written successfully');
//     });
//   }
  
// };
