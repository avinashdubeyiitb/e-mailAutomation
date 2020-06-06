<template>

  <div id="app">
    <h1 class="uuid">Send Mail To Team</h1>
    <button id="butt" type="button" name="button"><router-link to="/">Home</router-link></button>
  <div id="col1inner" >
    <div>
      <button id="sub1" @click="getmailids">Get Mail ids</button>
    </div>
  <div>
    <button id="sub2" @click="send" v-if="isget">Send</button>
  </div>
  </div>
  <div id="col2inner">
  <div v-if="isget">
    <div v-for="id in output.mailids" v-bind:key="id">
      {{id}}
    </div>
  </div>
  <div v-else>
    {{output}}
  </div>
  </div>
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
      isget: false
    }
  },
  methods: {
    getmailids (e) {
      e.preventDefault()
      const currentObj = this
      this.isget = true
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
      this.isget = false
      this.output = "sending mails"
      this.axios.post('http://localhost:8081/api/main/sendmail', {
      })
        .then(function (response) {
          currentObj.output = response.data
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
top: 0%;
margin:0px;
font-style: normal;
font-weight: normal;
font-size: 2em;
text-align: center;
color: #000000;
}
#app{
background: #FFFFFF;
position: absolute;
width: 100%;
height: 100%;
left: 0px;
top: 0px;
}
#col1inner{
position: absolute;
width: 48%;
height: 90%;
left: 1%;
top: 15%;
background: #6EA5F7;
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
background: #6EA5F7;
border: 1px solid #000000;
box-sizing: border-box;
border-radius: 10px;
}
#sub1{
position: absolute;
right:10%;
top: 60%;
}
#sub2{
position: absolute;
right:40%;
top: 60%;
}
</style>
