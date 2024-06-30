/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{vue,js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {},
    fontFamily: {
      sans: ["Noto Sans Lao Looped", "sans-serif"]
    },
  },
  plugins: [require('daisyui'),],
}

