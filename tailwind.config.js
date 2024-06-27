module.exports = {
  content: [
      "./templates/**/*.html",
      "./static/src/**/*.js",
      "./node_modules/flowbite/**/*.js"
  ],
  theme: {
    extend: {
      colors: {
        'jasper': '#DB504A',
        'bittersweet': '#FF6F59',
        'dark-state-grey': '#254441',
        'jasper': '#DB504A',
      },
      margin: {
        '25%': '25%',
      }
    },
    container: {
      center: true,
    },
  },
  
  plugins: [
    require("flowbite/plugin")
  ],

}