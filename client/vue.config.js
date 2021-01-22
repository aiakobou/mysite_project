const path = require("path");

module.exports = {
  lintOnSave: false,
  devServer: {
    host: "localhost",
    port: 8080,
    progress: false,
    proxy: {
      "/api": {
        target: "http://127.0.0.1:5555/",
        ws: false,
        changeOrigin: true
      },
      "/socket.io": {
        target: "http://127.0.0.1:5555/",
        ws: true,
        changeOrigin: true
      }
    },
    hot: false,
    inline: false
  },
  configureWebpack: {
    devtool: "source-map"
  },
  outputDir: path.resolve(__dirname, "../client/dist"),
  assetsDir: "static"
};