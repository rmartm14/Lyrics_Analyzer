<template>
  <v-app class="app">
    <topBar></topBar>
    <v-main class="pt-5" style="background-color:#ffe3de">
      <fondo-initial></fondo-initial>
    </v-main>
  </v-app>
</template>

<script>
import topBar from "./components/Bars/topBar.vue";
import fondoInitial from "./components/fondos/fondoInitial.vue";

export default {
  name: "App",

  components: {
    topBar,
    fondoInitial,
  },

  data: () => ({
    //
  }),
};
</script>

<style scoped>
.app {
  color: antiquewhite;
}
</style>
