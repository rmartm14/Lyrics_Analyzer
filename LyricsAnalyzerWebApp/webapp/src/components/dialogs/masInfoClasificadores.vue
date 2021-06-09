<template>
    <v-dialog
      v-model="dialog"
      width="500"
    >
      <template v-slot:activator="{ on, attrs }">
        <a v-bind="attrs"
          v-on="on" class="color-font">
          Más info
        </a>
      </template>

      <v-card>
        <v-card-title class="text-h5 color-font mb-2">
          Información Sobre los clasificadores
        </v-card-title>

        <v-card-text>
          En el caso de escoger entre los diferentes clasificadores que puedes escoger aqui, has de saber que el clasificador SVM es el que mejor resultado nos ha dado,
          siguiendo con el Naive Bayes, KNN y redes neuronales. Al ser la precisión cercana a un 60%, no esperes que la actuación sea perfecta
        </v-card-text>

        <v-divider></v-divider>

        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn
            class="color-font"
            text
            @click="dialog = false"
          >
            De acuerdo
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
</template>
<script>
  export default {
    data () {
      return {
        dialog: false,
      }
    },
  }
</script>
<style scoped>
.back-color{
    background: #0a043c;
}
.color-font{
    color: #0a043c;
}
</style>