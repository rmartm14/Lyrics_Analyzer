<template>
  <div>
    
    <topBar></topBar>
    <v-main class="pt-5 text-center" style="background-color: #ffe3de">
      <fondo-initial></fondo-initial>
    </v-main>
    <my_footer> </my_footer>
  </div>
</template>

<script>
import topBar from "./components/Bars/topBar.vue";
import fondoInitial from "./components/fondos/fondoInitial.vue";
import my_footer from "./components/Bars/footer.vue";
export default {
  name: "App",

  components: {
    topBar,
    fondoInitial,
    my_footer,
  },

  data: () => ({
    //
  }),
};
</script>