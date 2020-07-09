<template>
    <div id="app">
      <div>
        <b-dropdown id="dropdown-form" text="Settings" ref="dropdown" class="m-2 settings">
          <b-dropdown-form>
            <b-form-group label="Url" label-for="dropdown-form" @submit.stop.prevent>
              <b-form-input
                id="dropdown-form"
                size="sm"
                placeholder="http://localhost:8081/"
                v-model="url"
              ></b-form-input>
            </b-form-group>
            <b-button variant="primary" size="sm" @click="onClick(url)">Save</b-button>
            <div>
              <b-form-checkbox v-model="checked" @change="themechange()" name="check-button" switch>
                <b>Change Theme </b>
              </b-form-checkbox>
            </div>
          </b-dropdown-form>
        </b-dropdown>
      </div>
      <div v-show="success">
      <button class="btn" @click="logout" id="logout">Log Out!</button>
    </div>
  <div id="leftbar" v-show="success">
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
      <router-link style="text-decoration: none; color: inherit;" to="/ema">Email Analytics</router-link>
    </div>
  <router-view/>
  </div>
  <div v-show="!success">
    <div class="container">
            <br/>
            <form>
            <div class="form-group">
                <label for="usr">User Name:</label>
                <input type="text" class="form-control" id="txtUsr" v-model="user_name">
            </div>
            <div class="form-group">
                <label for="pwd">Password:</label>
                <input type="password" class="form-control" id="txtPwd" v-model="user_pass">
            </div>
            <button class="btn" @click="login">Login</button>
            <label  id="lbl">{{stat}}</label>
          </form>
          <!-- <div class="content-blk">
          <button id="loadnewwindow" @click="say">Google Login</button>
                 <div id='message'></div>
          </div>
          <div>
            <button @click="conti">continue</button>
          </div> -->
    </div>
  </div>
</div>
</template>
<script>
const ipcRenderer = require('electron').ipcRenderer

export default {
  mounted () {
    console.log('Component mounted.')
  },
  computed: {

  },
  data () {
    return {
      checked: true,
      stat: '',
      user_name: this.$store.getters.user_name,
      user_pass: '',
      success: this.$store.getters.success,
      token: this.$store.getters.token,
      url: this.$store.getters.url
    }
  },
  watch: {
  },
  methods: {
    themechange () {
      const t = document.getElementById('theme')
      if (this.checked === true) {
        t.setAttribute('href', '/theme/light.css')
      } else {
        t.setAttribute('href', '/theme/dark.css')
      }
    },
    conti (e) {
      e.preventDefault()
      console.log('here')
      console.log(this.token)
      // const currentObj = this
      this.axios.post(this.url + '/api/main/glogin', {
        token: this.token
      })
        .then(status => {
          this.stat = status.data.status
          console.log(this.stat)
          if (this.stat === 'success') {
            this.success = true
            this.$store.commit('success', this.success)
          }
          // if (this.output.status === 'Created Successfully') {
          //   this.success = true
          // }
        })
        .catch(function (error) {
          this.status = error
        })
    },
    say () {
      var arg = 'secondparam'
      // send the info to main process . we can pass any arguments as second param.
      ipcRenderer.send('btnclick', arg) // ipcRender.send will pass the information to main process
      ipcRenderer.on('btnclick-task-finished', (event, param) => {
        this.token = param
        this.$store.commit('token', this.token.access_token)
      })
    },
    login (e) {
      e.preventDefault()
      console.log('request')
      this.axios.post(this.url + '/api/main/login', {
        username: this.user_name,
        password: this.user_pass
      })
        .then(status => {
          this.stat = status.data.status
          console.log(this.stat)
          if (this.stat === 'success') {
            this.success = true
            this.$store.commit('success', this.success)
            this.$store.commit('user_name', this.user_name)
          }
          // if (this.output.status === 'Created Successfully') {
          //   this.success = true
          // }
        })
        .catch(function (error) {
          this.status = error
        })
    },
    onClick (i) {
      // Close the menu and (by passing true) return focus to the toggle button
      this.url = i
      this.$store.commit('url', this.url)
      this.$refs.dropdown.hide(true)
    },
    logout (e) {
      e.preventDefault()
      console.log('request')
      this.axios.post(this.url + '/api/main/logout', {
        username: this.user_name
      })
        .then(status => {
          this.stat = status.data.status
          console.log(this.stat)
          if (this.stat === 'logged out') {
            this.success = false
            this.$store.commit('success', this.success)
            this.$store.commit('user_name', '')
          }
          // if (this.output.status === 'Created Successfully') {
          //   this.success = true
          // }
        })
        .catch(function (error) {
          this.status = error
        })
    }
  }
}
</script>
<style scoped>
#th{
  position:absolute;
  top: 30%;
  left:33%;
}
.container{
  background: #FFFFFF;
  position:absolute;
  top: 30%;
  left:33%;
  height:37%;
  width:37%;
}

.btn{
  background: #008CBA;
}
#logout{
  position:absolute;
  top: 5%;
  right:13%;
}
.settings{
  position:absolute;
  top: 4%;
  right:4%;
}
</style>
