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
      <button class="btn btn-primary btn-margin" v-if="authenticated" @click="logout()" >Log Out</button>
  <router-view/>
  </div>
</div>
</template>
<script>
export default {
  data () {
    return {
      authenticated: this.$store.getters.getAuthenticated,
      auth: this.$store.getters.getAuth
    }
  },
  mounted () {
    console.log(this.auth)
    console.log(this.authenticated)
  },
  methods: {
    logout () {
      this.auth.logout()
      this.$store.commit('changeAuth', this.auth)
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
</style>
