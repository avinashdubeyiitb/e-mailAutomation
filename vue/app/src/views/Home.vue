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
</div>
</template>
<style scoped>
</style>
