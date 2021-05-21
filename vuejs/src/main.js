import Vue from "vue";
import App from "@/App.vue";

import store from "@/store";
import router from "@/router";

Vue.config.productionTip = false;

const vue = new Vue({
  router,
  store,
  render: (h) => h(App),
});

vue.$mount("#app");
