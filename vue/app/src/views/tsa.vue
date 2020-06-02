<template>
  <div id="app">
    <h1>Get College Updates</h1>
    <button id="butt" type="button" name="button"><router-link to="/">Home</router-link></button>
  <div id="col1inner" >
    <form @submit="formSubmit">
      <strong id="ccd" >Enter College Code:</strong>
      <input id="ccdi" type="text" v-model="clgcode"><br>
      <button id="sub">Submit</button>
    </form>
  </div>
  <div id="col2inner">
    <div v-if = 'output.status'>
      <label id="cname"><strong >Status :</strong></label>
      <label id="cnamev">{{output.status}}</label>
    </div>
    <div v-else >
    <label id="cname"><strong >College Name :</strong></label>
    <label id="cnamev">{{output.college_name}}</label>
    <label id="ea"><strong >eLSI Status :</strong></label>
    <label id="eav">{{output.elsi_allowed}}</label>
    <label id="tbt"><strong >TBT Status :</strong></label>
    <label id="tbtv">{{output.tbt_allowed}}</label>
    <label id="loi"><strong >LOI Status :</strong></label>
    <label id="loiv">{{output.loi_status}}</label>
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
      clgcode: '',
      output: ''
    }
  },
  methods: {
    formSubmit (e) {
      e.preventDefault()
      const currentObj = this
      this.axios.post('http://localhost:8081/api/main/clgdtl', {
        clgcode: this.clgcode
      })
        .then(function (response) {
          currentObj.output = response.data
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
#ccd{
position: absolute;
right:50%;
top: 53%;
}
#ccdi{
position: absolute;
right:10%;
top: 53%;
}
#sub{
position: absolute;
right:10%;
top: 60%;
}
#cname{
position: absolute;
right:75%;
top: 30%;
}
#cnamev{
position: absolute;
right: 5%;
top: 30%;
}
#ea{
position: absolute;
right: 75%;
top: 40%;
}
#eav{
position: absolute;
right: 50%;
top: 40%;
}
#tbt{
position: absolute;
right: 75%;
top: 50%;
}
#tbtv{
position: absolute;
right: 50%;
top: 50%;
}
#loi{
position: absolute;
right: 75%;
top: 60%;
}
#loiv{
position: absolute;
right: 50%;
top: 60%;
}
</style>
