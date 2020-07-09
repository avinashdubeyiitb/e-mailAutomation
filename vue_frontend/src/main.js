import App from './App.vue'
import router from './router'
import store from './store'
import Vue from 'vue'
import axios from 'axios'
import VueAxios from 'vue-axios'
import BootstrapVue from 'bootstrap-vue'
import 'bootstrap/dist/css/bootstrap.min.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import VueParticles from 'vue-particles'

Vue.use(VueAxios, axios)
Vue.use(BootstrapVue)
Vue.use(VueParticles)
Vue.config.productionTip = false
new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')

// import GSignInButton from 'vue-google-signin-button' uninstalled
// import VueHead from 'vue-head' uninstalled
// import UUID from 'vue-uuid' uninstalled

// Vue.use(VueHead) uninstalled
// Vue.use(GSignInButton) uninstalled
// Vue.use(UUID) uninstalled
