<template>
  <v-container class="fondo">
    <v-row>
      <v-col>
        <h1 id="initTitle">Lyrics Analyzer</h1>

        <h5 id="subInit" class="mb-4 mt-4">A place where we love to analyze music</h5>
        <p class="ml-8" >
          This is the TFG web app result that will give you several classifiers
          in order to collect the data that you insert in some TextBoxes and
          forms.
        </p>
      </v-col>
    </v-row>
    <v-row class="col-10 ml-4" align-center>
      <v-spacer/>
      <v-spacer/>

      <v-img
        height="400px"
        width="300px"
        class="photo"
        src="https://interactivo.eluniversal.com.mx/2016/rolling-stones/img/curiosidades/logo.png"
        
      ></v-img>
      <v-spacer/>
    </v-row>
  </v-container>
</template>

<script>
export default {
  data: () => ({
    isActive: false,
    photoIndex: 0,
    images: [
      {
        id: 1,
        src: require("./../../assets/beatlesAR.jpg"),
      },
      {
        id: 2,
        src: require("./../../assets/RollingStones.jpg"),
      },
    ],
    image: require("./../../assets/beatlesAR.jpg"),
  }),
  mounted() {
    setInterval(this.switchImage(), 3000);
  },
  methods: {
    switchImage() {
      if (this.photoIndex < this.images.length) {
        this.photoIndex = this.photoIndex + 1;
        console.log("aqui");
      } else {
        this.photoIndex = 0;
        console.log("alli");
      }
      this.image = this.images[this.photoIndex].src;
    },
  },
};
</script>

<style scoped>
#initTitle {
  color: #0a043c;
  font-family: "Open Sans", sans-serif;
  font-size: 60px;
  font-weight: 600;
  line-height: 32px;
  margin: 30px 30px 4px 30px;

}
#subInit {
  color: #03506f;
  font-family: "Open Sans", sans-serif;
  font-size: 30px;
  font-weight: 600;
  line-height: 40px;
  margin: 10px 30px 0px 30px;

}
.fondo {
  background-color: "#ffe3de";
  text-align: center;
}
.photo {
  background: #b0afac;
  padding: 14px;
  border: 12px solid #0a043c;
  
}
</style>
