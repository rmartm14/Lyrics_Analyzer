import Vue from "vue";
import Router from "vue-router";
import Ping from "../components/Ping.vue";
import hello from "../components/HelloWorld.vue";

Vue.use(Router);

export default new Router({
  mode: "history",
  base: process.env.BASE_URL,
  routes: [
    {
      path: "/hello",
      name: "Ping",
      component: hello
    },
    {
      path: "/ping",
      name: "Ping",
      component: Ping
    }
  ]
});
