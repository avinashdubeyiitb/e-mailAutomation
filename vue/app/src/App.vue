<template>
  <div id="app">
      <!-- <button id="butt" type="button" name="button"><router-link to="/">Home</router-link></button> -->
    <!--  <router-link to="/about">About</router-link> -->
    <div id="particles">
    <vue-particles
   color="#dedede"
   :particleOpacity="0.7"
   :particlesNumber="80"
   shapeType="circle"
   :particleSize="4"
   linesColor="#dedede"
   :linesWidth="1"
   :lineLinked="true"
   :lineOpacity="0.4"
   :linesDistance="150"
   :moveSpeed="3"
   :hoverEffect="true"
   hoverMode="grab"
   :clickEffect="true"
   clickMode="push"
 >
 </vue-particles>
</div>
    <router-view/>
  </div>
</template>
<style>
/* #app {
  margin: 0px;
  padding:0px;
  background: linear-gradient(0deg, rgba(37, 48, 51, 0.95), rgba(37, 48, 51, 0.95)), linear-gradient(0deg, rgba(37, 48, 51, 0.95), rgba(37, 48, 51, 0.95)), rgba(37, 48, 51, 0.95);
} */
#particles {
    position: absolute;
    width: 100%;
    height: 100%;
    z-index: -1;
    background-color: #255;
}
#app{
  background: #000000;
  /* background-image: url(./assets/cool-background.png); */
  /* position:absolute; */
  /* z-index: -1; */
width: 100%;
height: 100%;
left: 0px;
top: 0px;
background-repeat: no-repeat;
background-position: center;
background-size: contain;
}
#leftbar{
  width: 65px;
  background: #FC4A1A;
  position: absolute;
top: 0px;
bottom: 0;
left: 0;
z-index: 0;
display: inline-block;
padding: 20px;
border-right: 1px solid #000000;
box-shadow: 4px 6px 4px rgba(0, 0, 0, 0.4);
border-radius: 0px 12px 12px 0px;
opacity: .9;
}
.baritems{
  height: 46px;
  width: 65px;
  background: #F7B733;
  position: absolute;
top: 30px;
bottom: 0;
left: -10px;
z-index: 2;
display: block;
padding-top: 12px;
padding-left: 13px;
padding-right: 8px;
overflow: hidden;
border: 1px solid #000000;
box-shadow: 4px 6px 4px rgba(0, 0, 0, 0.25);
border-radius: 0px 15px 15px 0px;
transition:0.7s;
}
#baritem1{
top: 80px;
white-space:nowrap;
}
.baritems:hover {
  width: 180px;
}
#baritem2{
top: 150px;
white-space:nowrap
}
#baritem3{
top: 220px;
white-space:nowrap
}
#baritem0{
top: 5px;
white-space:nowrap
}
#baritem4{
top: 290px;
white-space:nowrap
}
#baritem5{
top: 360px;
white-space:nowrap
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
