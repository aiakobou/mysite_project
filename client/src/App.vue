<template>
  <img alt="Vue logo" src="./assets/logo.png" />
  <HelloWorld msg="Welcome to Your Vue.js App" />
</template>

<script>
var socket = io();
import HelloWorld from "./components/HelloWorld.vue";

export default {
  name: "App",
  data() {
    return{
        messages: [],
        socket: null}
    },

  components: {
    HelloWorld
  },

  beforeMount(){
    this.setSocketConnection();
    },

  mounted() {
    this.socket.on('MESSAGE', (socket) => {
        this.messages = socket;
        console.log(this.messages);
    });
    this.socket.emit('message', 'VUE CONNECTED MESSAGE')
  },

  methods: {

    setSocketConnection: function () {
    let wsPort = window.location.port;
    this.socket = io.connect();
    // Verify our websocket connection is established
    this.socket.on("connect", function () {
        console.log("Websocket connected!");
        });
    }

  }
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
