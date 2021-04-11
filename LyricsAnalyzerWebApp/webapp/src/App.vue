<template>
  <v-app id="application" style="background-color: antiquewhite">
    <topBar></topBar>
    <router-view />
    <v-footer absolute padless>
      <customfooter> </customfooter>
    </v-footer>
  </v-app>
</template>
<script>
import topBar from "./components/Bars/topBar.vue";
import Customfooter from "./components/footer/footer.vue";

export default {
  name: "App",

  components: {
    topBar,
    Customfooter,
  },

  data: () => ({
    //
  }),
};
</script>
