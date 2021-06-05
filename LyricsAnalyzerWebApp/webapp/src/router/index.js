import Vue from "vue";
import VueRouter from "vue-router";

Vue.use(VueRouter);

const routes = [
    {
        path: "/",
        name: "home",
        component: () => import("../init.vue"),
    },
    {
        path: "/about",
        name: "about",
        component: () => import("../views/about.vue")
    },
    {
        path: "/detect",
        name: "detect",
        component: () => import("../views/detect.vue")
    },
    {
        path: "/artist",
        name: "artist",
        component: () => import("../views/artist.vue")
    }

];

const router = new VueRouter({
    mode: "history",
    base: process.env.BASE_URL,
    routes,
});

export default router;