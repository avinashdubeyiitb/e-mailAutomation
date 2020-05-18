<template>
  <b-jumbotron>
  <div id="app">
    <div id="nav">
      <h1>Welcome~.~</h1>
       <router-link to="/">home</router-link>
      </div>
    <!--  <router-link to="/about">About</router-link> -->
    <router-view/>
  </div>
  </b-jumbotron>
</template>

<style>

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
#nav {
  padding: 5px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
</style>
