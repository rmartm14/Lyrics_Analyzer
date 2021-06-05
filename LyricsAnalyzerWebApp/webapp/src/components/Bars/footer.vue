<template>
<div>
<v-footer
    color
    padless
  >
    <v-card
      class="flex"
      flat
      tile

    >
      <v-card-title class="colorback">
        <strong class="subheading">Conecta conmigo en las siguientes redes sociales</strong>

        <v-spacer></v-spacer>

        <v-btn
          v-for="icon in icons"
          :key="icon"
          class="mx-4"
          dark
          icon
        >
          <v-icon size="24px">
            {{ icon }}
          </v-icon>
        </v-btn>
      </v-card-title>

      <v-card-text class="py-2 text-center secon-color">
        {{ new Date().getFullYear() }} — <strong>Vuetify</strong>
      </v-card-text>
    </v-card>
  </v-footer>
</div>
</template>
<script>
export default {
    name: "top_bar",
    data: () => ({
      icons: [
        'mdi-github',
        'mdi-twitter',
        'mdi-linkedin',
      ],
    }),
}
</script>
<style scoped>
.colorback{
    background-color: #0a043c;
    color:white;
}
.secon-color{
  background: #b0afac;

}
</style>