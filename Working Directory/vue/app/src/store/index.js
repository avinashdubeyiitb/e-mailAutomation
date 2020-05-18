import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    key: 'failed',
    recipientId: '',
    subject: '',
    body: ''
    // events: []
  },
  mutations: {
    change (state, payload) {
      state.key = payload.key
      state.recipientId = payload.recipientId
      state.subject = payload.subject
      state.body = payload.body
    }
    // ADD_EVENT (state, event) {
    //   state.events.push(event)
    // }
  },
  actions: {
    // createEvent ({ commit }, event) {
    //   commit('ADD_EVENT', event)
    // }
  },
  modules: {
  }
})
