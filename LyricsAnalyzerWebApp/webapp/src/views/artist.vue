<template>
    <div>
        <top-bar> </top-bar>
        
        <listaArtistas> </listaArtistas>
        <my_footer> </my_footer>
    </div>
</template>

<script>
import topBar from "../components/Bars/topBar.vue";
import my_footer from "../components/Bars/footer.vue";
import listaArtistas from "../components/listas/listaArtistas.vue";
export default {
    name: "artist",
    components: {
        topBar,
        my_footer,
        listaArtistas
    }
}
</script>