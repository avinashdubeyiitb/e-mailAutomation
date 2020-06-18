<template>
    <div id="app">
  <div id="leftbar">
    <div id="baritem0" class="baritems">
      <router-link to="/home" style="text-decoration: none; color: inherit;position:absolute" >Home</router-link>
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
  <div class="container">
    <div class="columns" style="margin-top: 100px;">
      <div class="column col-2 centered">
        <button v-if="isEmpty(user)" v-google-signin-button="clientId" class="google-signin-button"> Continue with Google</button>
        <user-panel v-else :user="user"></user-panel>
      </div>
    </div>
  </div>
</div>
</template>
<style scoped>
</style>
<script>
// import axios from 'axios'
// import UserPanel from '@/components/UserPanel'
// export default {
//   name: 'App',
//   components: {
//     UserPanel
//   },
//   data () {
//     return {
//       user: {},
//       googleSignInParams: {
//         client_id: '257717644642-ssdbt8958dphipjbd9f97u0norked40s.apps.googleusercontent.com'
//       }
//     }
//   },
//   methods: {
//     onGoogleSignInSuccess (googleUser) {
//       const token = googleUser.Zi.access_token
//       console.log('triggered')
//       console.log(token)
//       axios.post('http://localhost:8081/api/main/google/', {
//         access_token: token
//       })
//         .then(resp => {
//           this.user = resp.data.user
//         })
//         .catch(err => {
//           console.log(err.response)
//         })
//     },
//     onGoogleSignInError (error) {
//       console.log('OH NOES', error)
//     },
//     isEmpty (obj) {
//       return Object.keys(obj).length === 0
//     }
//   }
// }
import GoogleSignInButton from 'vue-google-signin-button-directive'
import axios from 'axios'
import UserPanel from '@/components/UserPanel'
export default {
  name: 'App',
  components: {
    UserPanel
  },
  directives: {
    GoogleSignInButton
  },
  data: () => ({
    user: {},
    clientId: '257717644642-ssdbt8958dphipjbd9f97u0norked40s.apps.googleusercontent.com'
  }),
  methods: {
    OnGoogleAuthSuccess (idToken) {
      console.log(idToken)
      axios.post('http://127.0.0.1:8081/api/main/google', {
        access_token: idToken,
        header: {
          Accept: 'application/json'
        }
      })
        .then(resp => {
          this.user = resp.data.user
        })
        .catch(err => {
          console.log(err.response)
        })
      // Receive the idToken and make your magic with the backend
    },
    OnGoogleAuthFail (error) {
      console.log(error)
    },
    isEmpty (obj) {
      return Object.keys(obj).length === 0
    }
  }
}
</script>
