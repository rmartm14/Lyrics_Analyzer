<template>
  <div>
    <v-app-bar color="#0a043c">
      <v-app-bar-nav-icon large color="white" v-on:click="goToInit()">
        <v-icon>mdi-music</v-icon>
      </v-app-bar-nav-icon>

      <v-app-bar-title class="white--text ">
        LyAnalyzer
      </v-app-bar-title>

      <v-spacer></v-spacer>
      <v-btn color="#a3ddcb" outlined v-on:click="goToDetect()"> Detect Song </v-btn>
      <v-btn color="#a3ddcb" class="ml-2" outlined v-on:click="goToArtist()"> Artist</v-btn>
      <v-btn color="#a3ddcb" class="ml-2" outlined v-on:click="goToAbout()"> About</v-btn>
    </v-app-bar>
  </div>
</template>

<script>
export default {
  name: "top_bar",
  methods: {
    goToInit(){
     this.$router.push({ path: '/' })
    },
    goToAbout() {
      this.$router.push("about")
    },
    goToDetect(){
      this.$router.push("detect")
    },
    goToArtist() {
      this.$router.push("artist")
    }
  }
};
</script>

<style scoped></style>
