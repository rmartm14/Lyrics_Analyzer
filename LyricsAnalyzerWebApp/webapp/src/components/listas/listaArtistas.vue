<template>
  <div class="ma-5">
    <v-card max-width="450" class="mx-auto">
      <v-toolbar color="indigo darken-1" dark>
        <v-app-bar-nav-icon></v-app-bar-nav-icon>

        <v-toolbar-title>Lista de Artistas</v-toolbar-title>

        <v-spacer></v-spacer>

        <v-btn icon>
          <v-icon>mdi-guitar</v-icon>
        </v-btn>
      </v-toolbar>

      <v-list three-line>
        <template v-for="(item, index) in items">
          <v-subheader
            v-if="item.header"
            :key="item.header"
            v-text="item.header"
          ></v-subheader>

          <v-divider
            v-else-if="item.divider"
            :key="index"
            :inset="item.inset"
          ></v-divider>

          <v-list-item v-else :key="item.title">
            <v-list-item-avatar>
              <v-img :src="item.avatar"></v-img>
            </v-list-item-avatar>
            <v-list-item-content>
              <v-list-item-title v-html="item.title"></v-list-item-title>
              <v-list-item-subtitle
                v-html="item.subtitle"
              ></v-list-item-subtitle>
            </v-list-item-content>
          </v-list-item>
        </template>
      </v-list>
    </v-card>
  </div>
</template>
<script>
export default {
  name: "listaArtistas",
  data: () => ({
    items: [
      { header: "Artistas" },
      {
        avatar:
          "https://interactivo.eluniversal.com.mx/2016/rolling-stones/img/curiosidades/logo.png",
        title: "The Rolling Stones",
        subtitle: "Grupo de Música de la década de los 70 con estilo Rock",
      },
      { divider: true, inset: true },
      {
        avatar: "https://logos-marcas.com/wp-content/uploads/2020/07/Beatles-Simbolo.png",
        title: 'The Beatles',
        subtitle: "Grupo de Música de la década de los 60 con estilo Rock"
      },
      { divider: true, inset: true },
      {
        avatar: "https://indiehoy.com/wp-content/uploads/2020/05/radiohead-logo.jpg",
        title: "Radiohead",
        subtitle: "Grupo de Música de la década de los 90 con estilo Rock" 
        },
      { divider: true, inset: true },
      {
        avatar: "https://img.huffingtonpost.com/asset/60a980f0260000858bb43a34.jpg?cache=WKAVDXrtgX&ops=scalefit_720_noupscale&format=webp",
        title: "Bob Dylan",
        subtitle: "Cantautor de los 70"
        },
      { divider: true, inset: true },
      {
        avatar: "https://ichef.bbci.co.uk/news/800/cpsprodpb/10BEB/production/_104378586_gettyimages-74292099.jpg",
        title: "Queen",
        subtitle: "Grupo de musica de la decada de los 70 -80"
      },
    ],
  }),
};
</script>