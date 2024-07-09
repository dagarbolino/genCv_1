/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "../**/src/**/*.{js,css,scss,html}",
    "../**/templates/**/*.{js,css,scss,html}",
    "../.venv/**/*.{js,css,scss,html}"
  ],
  theme: {
    fontFamily: {
      sans: ['Graphik', 'sans-serif'],
      serif: ['Merriweather', 'serif'],
    },
    extend: {},
  },
  plugins: [
    require('daisyui'),
  ],
}

