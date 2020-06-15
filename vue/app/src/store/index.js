import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    user: {
      authenticated: false,
      auth: null
    }
  },
  getters: {
    getAuthenticated: state => {
      return state.user.authenticated
    },
    getAuth: state => {
      return state.user.auth
    }
  },
  mutations: {
    changeState (state, payload) {
      state.user.authenticated = payload
    },
    changeAuth (state, payload) {
      state.user.auth = payload
    }
  },
  actions: {
  },
  modules: {
  }
})
