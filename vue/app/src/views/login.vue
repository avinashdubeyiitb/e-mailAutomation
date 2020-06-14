<template>

  <div id="login">

      <button id="butt" type="button" name="button" v-if="authenticated"><router-link to="/home">Home</router-link></button>

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
</template>

<script>
import AuthService from '../auth/AuthService.js'
import axios from 'axios'

const API_URL = 'http://127.0.0.1:8081'

const auth = new AuthService()
export default {
  name: 'login',
  data () {
    this.handleAuthentication()
    this.authenticated = false

    auth.authNotifier.on('authChange', authState => {
      this.authenticated = authState.authenticated
    })

    return {
      authenticated: false,
      message: ''
    }
  },
  methods: {
    // this method calls the AuthService login() method
    login () {
      auth.login()
    },
    handleAuthentication () {
      auth.handleAuthentication()
    },
    logout () {
      auth.logout()
    },
    privateMessage () {
      const url = `${API_URL}/api/private/`
      return axios.get(url, { headers: { Authorization: `Bearer ${auth.getAuthToken()}` } }).then((response) => {
        console.log(response.data)
        this.message = response.data || ''
      })
    }
  }
}
</script>

<!--
background: linear-gradient(0deg, rgba(37, 48, 51, 0.95), rgba(37, 48, 51, 0.95)), linear-gradient(0deg, rgba(37, 48, 51, 0.95), rgba(37, 48, 51, 0.95)), rgba(37, 48, 51, 0.95);
-->
<style>
#login {
  margin: 10px;
  padding: 10px;
}

#butt{
  background: linear-gradient(0deg, rgba(37, 48, 51, 0.95), rgba(37, 48, 51, 0.95)), linear-gradient(0deg, rgba(37, 48, 51, 0.95), rgba(37, 48, 51, 0.95)), rgba(37, 48, 51, 0.95);
  border: 1px solid rgba(145, 146, 165, 0.71);
  width:150px;
}
a.router-link-exact-active {
  color: #42b983;
}
</style>
