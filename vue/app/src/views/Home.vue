<template>
    <div id="app">
  <div id="leftbar">
    <div id="baritem0" class="baritems">
      <router-link to="/" style="text-decoration: none; color: inherit;position:absolute" >Home</router-link>
      </div>
    <div id="baritem1" class="baritems">
      <router-link style="text-decoration: none; color: inherit; position:absolute" to="/sim">Send info. mail</router-link>
    </div>
    <div id="baritem2" class="baritems">
      <router-link style="text-decoration: none; color: inherit;" to="/aws">Announce Workshop</router-link>
    </div>
    <div id="baritem3" class="baritems">
      <router-link style="text-decoration: none; color: inherit;" to="/cws">Create Workshop</router-link>
    </div>
    <div id="baritem4" class="baritems">
      <router-link style="text-decoration: none; color: inherit;" to="/algo">Run Algorithm</router-link>
    </div>
    <div id="baritem5" class="baritems">
      <router-link style="text-decoration: none; color: inherit;" to="/tsa">Coming soon :(</router-link>
    </div>
  <router-view/>
  </div>
  <!-- <div id="logout">
  <button class="btn btn-primary" v-if="authenticated" @click="logout()" >Log Out</button>
</div> -->
<div id="login">

    <!-- <button id="butt" type="button" name="button" v-if="authenticated"><router-link to="/home">Home</router-link></button> -->

        <button
    class="btn btn-primary btn-margin"
    v-if="!authenticated"
    @click="login()">
    Log In
  </button>

  <button
    class="btn btn-primary btn-margin"
    v-if="authenticated"
    @click="privateMessage()">
    Call Private
  </button>

  <button
    class="btn btn-primary btn-margin"
    v-if="authenticated"
    @click="logout()">
    Log Out
  </button>
  {{ message }}
  <br>

  <!--  <router-link to="/about">About</router-link> -->
  <router-view/>
</div>
</div>
</template>
<script>
import AuthService from '../auth/AuthService.js'
import axios from 'axios'

const API_URL = 'http://127.0.0.1:8081'

const auth = new AuthService()
// this.$store.commit('changeAuth', auth)
export default {
  data () {
    this.$store.commit('changeAuth', auth)
    this.handleAuthentication()
    this.authenticated = false

    auth.authNotifier.on('authChange', authState => {
      this.authenticated = authState.authenticated
      this.$store.commit('changeState', this.authenticated)
    })
    return {
      message: '',
      authenticated: this.$store.getters.getAuthenticated,
      auth: this.$store.getters.getAuth
    }
  },
  mounted () {
    console.log(this.auth)
    console.log(this.authenticated)
  },
  methods: {
    // this method calls the AuthService login() method
    login () {
      auth.login()
      this.$store.commit('changeAuth', auth)
      console.log('login')
      console.log(this.$store.getters.getAuthenticated)
      console.log(this.$store.getters.getAuth)
    },
    handleAuthentication () {
      auth.handleAuthentication()
      this.$store.commit('changeAuth', auth)
    },
    logout () {
      auth.logout()
      this.$store.commit('changeAuth', auth)
    },
    privateMessage () {
      const url = `${API_URL}/api/private/`
      return axios.get(url, { headers: { Authorization: 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImMzM3UyMjIwOU5YZTk0U2NOX2RFUCJ9.eyJpc3MiOiJodHRwczovL2Rldi16eTItc3dzaC51cy5hdXRoMC5jb20vIiwic3ViIjoiZ29vZ2xlLW9hdXRoMnwxMDc3MTY0MjMzODgwOTMyNTI3NjciLCJhdWQiOlsiaHR0cHM6Ly9kamFuZ28tdnVlanMtYXBpIiwiaHR0cHM6Ly9kZXYtenkyLXN3c2gudXMuYXV0aDAuY29tL3VzZXJpbmZvIl0sImlhdCI6MTU5MjMwMTM5MSwiZXhwIjoxNTkyMzA4NTkxLCJhenAiOiI2ZFFUcEVJSFMyOWRoREdMeHNNVExoa29vZUF0dEJ4OCIsInNjb3BlIjoib3BlbmlkIHByb2ZpbGUifQ.ZyedVFng_e7wDzbWXWf2mmCbfvgu37pz4t7kuI2vFGXcpFruj8aIkXIwXo3B0cgqlmBMX1a-2VyrODmpm0X7LUJ_Jt2EKeV8sX5Sh5aOeFnVV7ZYvU__ym6sNzCwYnnwBlOH91VH6GU7Q404I7yN51HuW2-gjcIOZQ4848QbHWGlkRkBXjyolDaeUboVd-yzPcrdGuag9aH07LDawMF8XX2se_0W8Dt7CQ2EvQq27-8wG_Yq2f12KM2-_OhOZCaNlEqonrA8cSrbCQiKGfd5c-anz5F42ouIajsLkilu-NKNdyGfRE9Hv2GRfSCNpUK76IgGEl-hJs0pUPBha7lHzg' } }).then((response) => {
        console.log(response.data)
        this.message = response.data || ''
      })
    }
  }
}
</script>
<style scoped>
#but1{
  position: absolute;
  width: 200px;
  height: 40px;
  left: 15%;
  top: 45%;
}
#logout{
  left:90%;
  width:7em;
  top:3px;
  position:absolute;
}
</style>
