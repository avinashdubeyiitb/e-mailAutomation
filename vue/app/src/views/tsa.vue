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
        <router-link style="text-decoration: none; color: inherit;" to="/tsa">Coming soon :(</router-link>
      </div>
    </div>
    <h1>Send Mail To Team</h1>
    <!-- <button id="butt" type="button" name="button"><router-link to="/home">Home</router-link></button> -->
    <button @click="makecall">login</button>
    <!--
  <div id="col1inner" >
      <button id="sub1" @click="getmailids">Get Mail ids</button>
    <button id="sub2" @click="send" v-if="isget">Send</button>
    <div id="content" v-if="isget">
  <table class="table table-hover" >
<thead>
<tr>
<th>
<label class="form-checkbox">
<input type="checkbox" @click="select">
</label>
</th>
<th>Mail Ids</th>
<th>Name</th>
</tr>
</thead>
<tbody>
<tr v-for="dta in output.data" v-bind:key="dta.mailid">
<td>
<label class="form-checkbox">
<input type="checkbox" :value="dta.mailid" v-model="selected" :disabled="getstate(dta.mailid)">
</label>
</td>
<td>{{dta.mailid}}</td>
<td>{{dta.name}}</td>
</tr>
</tbody>
</table>
    </div>
  <div v-if="issend" id ="result">
    {{result}}
  </div>
  </div>
  <div id="col2inner">
  </div-->
  </div>
</template>

<script>
export default {
  mounted () {
    console.log('Component mounted.')
  },
  computed: {
  },
  data () {
    return {
      output: '',
      isget: false,
      issend: false,
      selected: [],
      result: '',
      sent: []
    }
  },
  methods: {
    makecall () {
      require('electron').shell.openExternal('http://127.0.0.1:8081/login')
    },
    getstate (mailid) {
      if (this.issend === true && this.selected.indexOf(mailid) !== -1) {
        if (this.result.success > 0 && this.sent.indexOf(mailid) !== -1) {
          return true
        }
      }
      return false
    },
    getmailids (e) {
      e.preventDefault()
      const currentObj = this
      this.isget = true
      this.issend = false
      this.axios.post('http://localhost:8081/api/main/mailids', {
      })
        .then(function (response) {
          currentObj.output = response.data
          console.log(response)
        })
        .catch(function (error) {
          console.log(error)
        })
    },
    send (e) {
      e.preventDefault()
      const currentObj = this
      this.result = 'sending mails'
      this.issend = true
      this.axios.post('http://localhost:8081/api/main/sendmail', {
        selected: this.selected
      })
        .then(function (response) {
          currentObj.result = response.data
          for (var val in response.data.sent) {
            currentObj.sent.push(response.data.sent[val])
          }
        })
        .catch(function (error) {
          console.log(error)
        })
    },
    select () {
      this.selected = []
      for (var val in this.output.data) {
        this.selected.push(this.output.data[val].mailid)
      }
    }
  }
}
</script>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1{
position: absolute;
left: 40%;
top: 0%;
margin:0px;
font-style: normal;
font-weight: normal;
font-size: 2em;
text-align: center;
color: #000000;
}

#col1inner{
position: absolute;
width: 43%;
height: 90%;
left: 7%;
top: 15%;
z-index:-1;
background: #4ABDAC;
border: 1px solid #000000;
box-sizing: border-box;
border-radius: 10px;
}
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
}
tr ,td,thead,table,th{
  padding:0px;
  padding-left:6px;
}
</style>
