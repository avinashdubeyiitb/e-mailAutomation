<template>

  <div id="app">
    <h1 class="uuid">Send Mail To Team</h1>
    <button id="butt" type="button" name="button"><router-link to="/">Home</router-link></button>
  <div id="col1inner" >
    <div>
      <button id="sub" @click="submit">Submit</button>
    </div>
  <div>
    <button id="sub" @click="send">Send</button>
  </div>
  </div>
  <div id="col2inner">
  <div>

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
      data: '',
      issub: false,
      issnd: false
    }
  },
  methods: {
    submit (e) {
      e.preventDefault()
      const currentObj = this
      this.axios.post('http://localhost:8081/api/main/sendmail', {
      })
        .then(function (response) {
          this.data = response.data
        })
        .catch(function (error) {
          currentObj.output = error
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
#sub{
position: absolute;
right:10%;
top: 60%;
}
</style>
