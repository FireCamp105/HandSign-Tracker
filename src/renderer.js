/**
 * This file will automatically be loaded by vite and run in the "renderer" context.
 * To learn more about the differences between the "main" and the "renderer" context in
 * Electron, visit:
 *
 * https://electronjs.org/docs/tutorial/application-architecture#main-and-renderer-processes
 *
 * By default, Node.js integration in this file is disabled. When enabling Node.js integration
 * in a renderer process, please be aware of potential security implications. You can read
 * more about security risks here:
 *
 * https://electronjs.org/docs/tutorial/security
 *
 * To enable Node.js integration in this file, open up `main.js` and enable the `nodeIntegration`
 * flag:
 *
 * ```
 *  // Create the browser window.
 *  mainWindow = new BrowserWindow({
 *    width: 800,
 *    height: 600,
 *    webPreferences: {
 *      nodeIntegration: true
 *    }
 *  });
 * ```
 */

import './index.css';
import './tailwind.css';
import { createApp } from 'vue';
import App from './App.vue'; 

// Vuetify
import 'vuetify/styles'
import { createVuetify } from 'vuetify'
import * as components from 'vuetify/components'
import * as directives from 'vuetify/directives'
import '@mdi/font/css/materialdesignicons.css' 
const vuetify = createVuetify({
  components,
  directives,
  theme: { 
    defaultTheme: 'dark',
  },
  icons:{  defaultSet: 'mdi',}
})

createApp(App).use(vuetify).mount('#app')

//generate a random int between 1 and 100
//createApp(App).mount('#app');// #hmez is the id of the div in index.html
console.log('👋 This message is being logged by "renderer.js", included via Vite');
