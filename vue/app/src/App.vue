<template>
  <div id="app">
      <button id="butt" type="button" name="button" ><router-link to="/home">Home</router-link></button>

    <!--  <router-link to="/about">About</router-link> -->
    <router-view/>
  </div>
</template>

<style>
#app {
  margin: 10px;
  padding: 10px;
  background: linear-gradient(0deg, rgba(37, 48, 51, 0.95), rgba(37, 48, 51, 0.95)), linear-gradient(0deg, rgba(37, 48, 51, 0.95), rgba(37, 48, 51, 0.95)), rgba(37, 48, 51, 0.95);
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
