<template>
  <div id="app">
    <div id="leftbar">
      <div id="baritem0" class="baritems">
          <router-link to="/" style="text-decoration: none; color: inherit;" >Home</router-link>
        </div>
      <div id="baritem1" class="baritems">
        <router-link style="text-decoration: none; color: inherit;" to="/sim">Send info. mail</router-link>
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
    </div>
    <h1>Email Analytics</h1>
  <div id="col1inner" >
    Sent
<table class="table">
<thead>
<tr>
<th>User</th>
<th>Label</th>
<th>Count</th>
<th>Failed</th>
</tr>
</thead>
<tbody v-for='value in output.Sent' v-bind:key='value.user'>
  <tr v-for='data in value.Data' v-bind:key='data.label'>
    <td>{{value.user}}</td>
    <td>{{data.label}}</td>
    <td>{{data.count}}
      <b-dropdown class="dropsize">
              <div v-for="(id,idx) in data.clist" v-bind:key='idx' >
                <b-dropdown-item>{{id}}</b-dropdown-item>
              </div>
      </b-dropdown>
      </td>
    <td>{{data.failed}}
      <b-dropdown class="dropsize">
              <div v-for="(id,idx) in data.flist" v-bind:key='idx' >
                <b-dropdown-item>{{id}}</b-dropdown-item>
              </div>
      </b-dropdown>
      </td>
  </tr>
</tbody>
</table>
Draft
<table class="table">
  <thead>
<tr>
<th>User</th>
<th>Count</th>
<th>Failed</th>
</tr>
</thead>
  <tbody >
  <tr v-for='data in output.Draft' v-bind:key='data.user'>
    <td>{{data.user}}</td>
    <td>
      {{data.Data.count}}
      <b-dropdown class="dropsize">
              <div v-for="(id,idx) in data.Data.clist" v-bind:key='idx' >
                <b-dropdown-item>{{id}}</b-dropdown-item>
              </div>
      </b-dropdown>
      </td>
    <td>{{data.Data.failed}}
      <b-dropdown class="dropsize">
              <div v-for="(id,idx) in data.Data.flist" v-bind:key='idx' >
                <b-dropdown-item>{{id}}</b-dropdown-item>
              </div>
      </b-dropdown>
      </td>
  </tr>
</tbody>
</table>
Inbox
<table class="table">
  <thead>
<tr>
<th>User</th>
<th>Label</th>
<th>Count</th>
</tr>
</thead>
  <tbody v-for='value in output.Inbox' v-bind:key='value.user'>
  <tr v-for='data in value.Data' v-bind:key='data.label'>
    <td>{{value.user}}</td>
    <td>{{data.label}}</td>
    <td>{{data.count}}
      <b-dropdown class="dropsize">
              <div v-for="(id,idx) in data.clist" v-bind:key='idx' >
                <b-dropdown-item>{{id}}</b-dropdown-item>
              </div>
      </b-dropdown>
      </td>
  </tr>
</tbody>
</table>
<div id="loader" v-show="loader">
<b-button variant="danger" disabled>
  <b-spinner small ></b-spinner>
  Loading...
</b-button>
</div>
  </div>
  </div>
</template>

<script>
export default {
  mounted () {
    console.log('Component mounted.')
    this.stats()
  },
  computed: {
  },
  data () {
    return {
      output: '',
      url: this.$store.getters.url,
      // isget: false,
      // issend: false,
      // selected: [],
      // result: '',
      // sent: []
      loader: true
    }
  },
  methods: {
    stats () {
      this.axios.post(this.url + '/api/main/stats', {
      })
        .then(output => {
          this.output = output.data
          console.log('SUCCESS')
          this.loader = false
        })
        .catch(function (error) {
          console.log(error)
        })
    }
  }
}
</script>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1{
position: absolute;
left: 40%;
top: 2%;
margin:0px;
font-style: normal;
font-weight: normal;
font-size: 2em;
text-align: center;
color: #FFFFFF;
}

#col1inner{
position: absolute;
width: 90%;
height: 90%;
left: 7%;
right:1%;
top: 10%;
z-index: -1;
background: #4ABDAC;
border: 1px solid #000000;
box-sizing: border-box;
border-radius: 10px;
}
/*
#col2inner{
position: absolute;
width: 48%;
height: 90%;
right: 1%;
top: 15%;
background: #4ABDAC;
border: 1px solid #000000;
box-sizing: border-box;
border-radius: 10px;
}
#sub1{
position: absolute;
right:40%;
top: 60%;
}
#sub2{
position: absolute;
right:80%;
top: 60%;
}
#result{
position: absolute;
right:50%;
top: 70%;
}
#content{
  position: absolute;
  height:300px;
  width:500px;
  top:7%;
  left:4%;
  background-color: #f1f1c1;

  margin:4px, 4px;
   overflow-x: hidden;
   overflow-x: auto;
   text-align:justify;
}*/
tr ,td,thead,table,th{
  padding:0px;
  padding-left:6px;
}
#loader{
  position: absolute;
  top:45%;
  left:45%;
}
</style>
