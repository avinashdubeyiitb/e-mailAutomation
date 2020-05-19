<template>
  <b-jumbotron id="jumb">
  <div id="app">
    <div id="nav">
      <h1 >Welcome~.~</h1>
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
#jumb{
margin:0px;
padding:0px;
position: absolute;
width: 100%;
height: 100%;

background: linear-gradient(180deg, rgba(129, 153, 241, 0.6) 24.48%, #000000 99.99%, rgba(255, 255, 255, 0) 100%), #FFFFFF;}
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
