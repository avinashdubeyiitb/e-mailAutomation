import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import axios from 'axios'
import VueAxios from 'vue-axios'
import BootstrapVue from 'bootstrap-vue'
import 'bootstrap/dist/css/bootstrap.min.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import GSignInButton from 'vue-google-signin-button'
import XLSX from 'xlsx'
import UUID from 'vue-uuid'
import VueParticles from 'vue-particles'

Vue.use(GSignInButton)
Vue.use(UUID)
Vue.use(XLSX)
Vue.use(VueAxios, axios)
Vue.use(BootstrapVue)
Vue.use(VueParticles)
Vue.use(GSignInButton)
Vue.config.productionTip = false
new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
