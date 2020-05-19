<template>
  <!-- <div class="home"> -->
    <!-- <img alt="Vue logo" src="../assets/logo.png"> -->
    <!-- <HelloWorld msg="This is my first Vue.js App"/> -->
    <!-- <b-jumbotron> -->
    <div>
    <b-container class="bv-example-row">
      <b-row>
        <b-col cols="8">  <div>
          <!-- <img alt="Vue logo" src="../assets/logo.png" > -->
          <b-jumbotron header="Home" lead="Prototyping the final product">
            <p>For more information visit the link</p>
            <b-button variant="primary" href="#">More Info</b-button>
          </b-jumbotron>
        </div></b-col>
        <div>
         <b-button v-b-toggle.sidebar-right>Available features</b-button>
         <b-sidebar id="sidebar-right" title="features" right shadow>
           <b-col cols="8">  <table id="table" >
               <tr>
             <td><router-link to="/sim">Send information mail</router-link></td>
               </tr>
               <tr>
             <td><router-link to="/aws">Announce Workshop</router-link></td>
               </tr>
               <tr>
             <td>  <router-link to="/tsa">ALGO</router-link></td>
               </tr>
             </table></b-col>

         </b-sidebar>
       </div>
    <!--  <router-link to="/about">About</router-link> -->
    <router-view/>
    </b-row>
    </b-container>
  </div>
  <!-- </b-jumbotron> -->
</template>

<script>
// @ is an alias to /src
// import HelloWorld from '@/components/HelloWorld.vue'
//
// export default {
//   name: 'Home',
//   components: {
//     HelloWorld
//   }
// }
// </script>
