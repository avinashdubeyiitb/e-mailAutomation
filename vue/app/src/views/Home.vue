<template>
    <div id="app">
      <div id="app2">
        <h1>Welcome to our App :)</h1>
          <h3>Available features:</h3>
        <div id="a">
          <button id="but1" type="button" name="button"><router-link to="/sim">Send information mail</router-link></button>
       </div>
       <div id="b">
       <button id="but2" type="button" name="button"><router-link to="/aws">Announce Workshop</router-link></button>
       </div>
       <div id="c">
       <button id="but3" type="button" name="button"><router-link to="/cws">Create Workshop</router-link></button>
       </div>
       <div>
       <button id="but4" type="button" name="button"><router-link to="/tsa">Coming soon :(</router-link></button>
       </div>
    <router-view/>
  </div>
  </div>
</template>

<style>
#but1{
  position: absolute;
  width: 200px;
  height: 40px;
  left: 15%;
  top: 45%;

  box-shadow: 4px 6px 4px rgba(0, 0, 0, 0.25);
  background: #F5C8C8;
  border-radius: 19px;
}
#but2{
  position: absolute;
  width: 200px;
  height: 40px;
  left: 15%;
  top: 57%;

  background: #F5C8C8;
box-shadow: 4px 6px 4px rgba(0, 0, 0, 0.25);
  border-radius: 19px;
}
#but3{
  position: absolute;
  width: 200px;
  height: 40px;
  left: 15%;
  top: 69%;

  background: #F5C8C8;
  box-shadow: 4px 6px 4px rgba(0, 0, 0, 0.25);
  border-radius: 19px;
}
#but4{
  position: absolute;
  width: 200px;
  height: 40px;
  left: 15%;
  top: 81%;

  background: #F5C8C8;
  box-shadow: 4px 6px 4px rgba(0, 0, 0, 0.25);
  border-radius: 19px;
}
#app{
  background: #8B7980;
position: absolute;
width: 100%;
height: 100%;
left: 0px;
top: 0px;
}
h1{
  position: absolute;
width: 796px;
height: 148px;
left: 25%;
top: 0%;

font-family: Radley;
font-style: normal;
font-weight: normal;
font-size: 48px;
line-height: 61px;
display: flex;
align-items: center;
text-align: center;

color: #000000;

}
#app2{
  position: absolute;
width: 70%;
height: 70%;
left: 165px;
top: 113px;

background: linear-gradient(180deg, #D9B3B3 99.99%, rgba(239, 191, 191, 0) 100%);
border: 1px solid #544242;
box-sizing: border-box;
box-shadow: 0px 8px 4px rgba(13, 12, 12, 0.3);
border-radius: 10px;
}
h3{
  position: absolute;
width: 283px;
height: 55px;
left: 5%;
top: 32%;

font-family: Radley;
font-style: normal;
font-weight: normal;
font-size: 30px;
line-height: 38px;
display: flex;
align-items: center;
text-align: center;

color: #000000;
}
</style>
