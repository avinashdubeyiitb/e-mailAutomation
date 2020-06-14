import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import axios from 'axios'
import VueAxios from 'vue-axios'
import BootstrapVue from 'bootstrap-vue'
import 'bootstrap/dist/css/bootstrap.min.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import XLSX from 'xlsx'
import UUID from 'vue-uuid'
<<<<<<< HEAD

=======
>>>>>>> e1f3f47e92808fa6dd0ccdc05e4dd7c2de0a8921
Vue.use(UUID)
Vue.use(XLSX)
Vue.use(VueAxios, axios)
Vue.use(BootstrapVue)
Vue.config.productionTip = false
new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
