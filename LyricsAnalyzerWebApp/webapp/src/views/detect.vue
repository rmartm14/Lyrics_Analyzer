<template>
    <div>
        <top-bar> </top-bar>
        <form>
            <v-card class="mt-6" >
            <v-container>
                <v-row>
                    <h2 class="color-font"> Detect your own artist </h2>
                </v-row>
                <v-row class="col-6">
                    <v-col> 
                            <v-textarea
                            color="#0a043c"
                            v-model="letra" 
                            prepend-icon="mdi-music"
                            counter
                            placeholder="Letra de la canción"
                            id="nombre"
                            clearable
                            clear-icon="mdi-close-circle"
                            label="Letra de la canción"> 
                            </v-textarea> 
                    </v-col>   
                </v-row>
                <v-row class="ml-2">
                    <dialog-info-class/>
                </v-row>
                
                <v-row class="col-6 mt-2">
                    <h3 class="color-font"> Clasificadores </h3>
                </v-row>
                <v-row class="ml-3" >
                    <v-radio-group v-model="clasif" mandatory >
                        <v-radio label="redes neuronales" value="Redes" color="#0a043c"/>
                        <v-radio label="SVM" value="SVM" color="#0a043c"/>
                        <v-radio label="Naive Bayes" value="Naive" color="#0a043c"/>
                        <v-radio label="KNN" value="KNN" color="#0a043c"/>
                    </v-radio-group>
                    
                </v-row>
                
                <v-row class="ml-3 mt-2 mb-3">
                    
                    <v-btn color="#a3ddcb" class="ml-2 back-color" outlined> Detectar Artista </v-btn>
                </v-row>
            </v-container>
            </v-card>
        </form>
    </div>
</template>

<script>
import topBar from "../components/Bars/topBar.vue"
import dialogInfoClass from "../components/dialogs/masInfoClasificadores.vue"
export default {
    name: "detect",
    components: {
        topBar,
        dialogInfoClass
    },
    data () {
      return {
        clasif: "",
        letra:"",
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