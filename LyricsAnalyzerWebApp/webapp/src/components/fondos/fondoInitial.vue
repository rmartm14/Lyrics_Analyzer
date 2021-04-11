<template>
  <v-container class="fondo">
    <v-row class="mb-12">
      <v-col cols="6">
        <h1 id="initTitle">
          Lyrics Analyzer
        </h1>

        <h5 id="subInit">
          A place where we love to analyze music
        </h5>
        <p class="letras">
          Do you want to analyze what you're singing? This is the place where
          you can know it. We have a variety of artist to compare with and also,
          you can add the song by text or with voice recognition.
        </p>
      </v-col>

      <v-img
        v-for="image in this.images"
        :src="image.src"
        :alt="image.alt"
        :key="image.id"
        class="imgRight"
      />
    </v-row>
    <v-spacer></v-spacer>
    <v-divider></v-divider>
    <v-row class="mt-6">
      <v-spacer></v-spacer>
      <p class="letras_centered">
        Do you want to start?
      </p>
      <v-spacer></v-spacer>
    </v-row>
    <v-row class="mt-6">
      <v-spacer></v-spacer>
      <v-btn outlined elevation="6" x-large>Start</v-btn>
      <v-spacer></v-spacer>
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
        alt: "The Beatles",
      },
      {
        id: 2,
        src: require("./../../assets/RollingStones.jpg"),
        alt: "Rolling Stones",
      },
    ],
  }),
};
</script>

<style scoped>
#initTitle {
  color: #0a043c;
  font-family: "Open Sans", sans-serif;
  font-size: 60px;
  font-weight: 600;
  line-height: 50px;
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
.letras {
  color: black;
  font-family: "Open Sans", sans-serif;
  font-size: 25px;
  font-weight: 600;
  line-height: 40px;
  margin: 10px 30px 0px 30px;
  text-align: justify;
}
.letras_centered {
  color: #0a043c;
  font-family: "Open Sans", sans-serif;
  font-size: 25px;
  font-weight: 600;
  line-height: 40px;
  margin: 10px 30px 0px 30px;
  text-align: center;
}
.fondo {
  background-color: "#ffe3de";
}
.imgRight {
  height: 300px;
  width: 300px;
  margin-top: 70px;
  border-radius: 25%;
}
</style>
