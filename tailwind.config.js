/** @type {import('tailwindcss').Config} */
module.exports = {
  prefix: 'tw-',
  content: [
    "./index.html",
  "./src/**/*.{vue,js,ts,jsx,tsx}",
],
  theme: {
    extend: {
      colors: {
        "blue-black": "#000b18",
        "turquoise": "#40e0d0",
      }
    },
  },
  plugins: [],
}

