<template>
  <v-card flat tile width="100%" class=" text-center" color="#0a043c">
    <v-card-text>
      <v-btn v-for="icon in icons" :key="icon" class="mx-4" icon>
        <v-icon size="24px" color="white">
          {{ icon }}
        </v-icon>
      </v-btn>
    </v-card-text>

    <v-divider></v-divider>

    <v-card-text class="white--text">
      {{ new Date().getFullYear() }} — <strong>Rafael Martínez Matías</strong>
    </v-card-text>
  </v-card>
</template>

<script>
export default {
  name: "Customfooter",
  data: () => ({
    icons: ["mdi-home", "mdi-email", "mdi-calendar", "mdi-delete"],
    items: ["default", "absolute", "fixed"],
  }),
};
</script>

<style></style>
