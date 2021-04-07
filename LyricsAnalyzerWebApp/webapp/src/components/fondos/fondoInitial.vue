<template>
  <v-container class="fondo">
    <v-row>
      <v-col>
        <h1 id="initTitle">
          Lyrics Analyzer
        </h1>

        <h5 id="subInit">
          A place where we love to analyze music
        </h5>
      </v-col>
      <v-col>
        <v-img class="imgRight" :src="this.image" />
      </v-col>
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
  margin: 100px 30px 4px 30px;
  text-align: left;
}
#subInit {
  color: #03506f;
  font-family: "Open Sans", sans-serif;
  font-size: 30px;
  font-weight: 600;
  line-height: 40px;
  margin: 10px 30px 0px 30px;
  text-align: left;
}
.fondo {
  background-color: "#ffe3de";
}
.imgRight {
  height: 600px;
  width: 600px;
  margin-top: 70px;
}
</style>
