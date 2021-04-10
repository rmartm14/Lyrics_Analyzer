<template>
  <v-app class="app">
    <topBar></topBar>
    <v-main class="pt-5" style="background-color:#ffe3de">
      <fondo-initial></fondo-initial>
    </v-main>
    <v-footer absolute padless>
      <customfooter> </customfooter>
    </v-footer>
  </v-app>
</template>

<script>
import topBar from "./components/Bars/topBar.vue";
import fondoInitial from "./components/fondos/fondoInitial.vue";
import Customfooter from "./components/footer/footer.vue";

export default {
  name: "App",

  components: {
    topBar,
    fondoInitial,
    Customfooter,
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
