<template>
  <v-main class="pt-5" style="background-color:#ffe3de">
    <fondo-initial></fondo-initial>
  </v-main>
</template>

<script>
import fondoInitial from "../components/fondos/fondoInitial.vue";

export default {
  name: "App",

  components: {
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
