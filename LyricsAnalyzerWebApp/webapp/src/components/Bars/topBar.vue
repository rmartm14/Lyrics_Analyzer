<template>
  <div>
    <v-app-bar color="#0a043c">
      <v-app-bar-nav-icon large color="white">
        <v-icon>mdi-music</v-icon>
      </v-app-bar-nav-icon>

      <v-app-bar-title class="white--text">
        Lyrics Analyzer
      </v-app-bar-title>

      <v-spacer></v-spacer>
      <v-btn color="#a3ddcb" outlined> Detect Song</v-btn>
      <v-btn color="#a3ddcb" class="ml-2" outlined> Artist</v-btn>
      <v-btn color="#a3ddcb" class="ml-2" outlined> About</v-btn>
    </v-app-bar>
  </div>
</template>

<script>
export default {
  name: "top_bar",
};
</script>

<style scoped></style>
