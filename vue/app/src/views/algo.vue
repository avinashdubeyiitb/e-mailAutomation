<template>
  <div id="app">
    <h1>Algorithm for Team Selection </h1>
    <button id="butt" type="button" name="button"><router-link to="/home">Home</router-link></button>
    <button class="btn btn-primary btn-margin" v-if="authenticated" @click="logout()">Log Out</button>
  <div id="col1inner" >
    <strong id="wrk" >Select Workshop:</strong>
    <div class="dropdown" id="wrki">
  <input v-model="selectedworkshop" class="dropdown-input" type="text" placeholder="Select"  />
    <div  v-show="selectedworkshop" class="dropdown-list" style="z-index:100; position: fixed;background: #FFFFFF">
      <div v-for="(p,i) in wrklist" v-bind:key='i' v-show="showing">
        <div  v-for="(host,index) in p" v-bind:key='index' v-show="itemVisible(host)" @click="savehcn(host,index)" class="dropdown-item">
          {{host}}
        </div>
      </div>
      </div>
  </div>
  <strong id="lang">Preferred Language:</strong>
  <input id="langi" type="text" v-model="lang" @change="$store.commit('lang', lang)"><br>
  <strong id="lwilldrag" >Selection of workshop team from willing members : (Ascending order)</strong><br>

  <label id="id1"><strong>&#187; Demo is clear for atleast </strong>
    <label>
  <input v-if = "key1" v-model = "demo"
  @blur= "key1 = false; $emit('update')"
  @keyup.enter = "key1=false; $emit('update')" id="inp"
  @change="$store.commit('demo', demo)">
    <label v-else @click = "key1 = true;"> {{demo}}</label>
    <strong> modules .</strong>
  </label>
  </label><br>

    <div id ="willdrag">
      <strong >&#187; Solve conflicts in order :</strong>
      <draggable v-model="willcriteria" v-on:change="willupdate(willcriteria)" v-bind="dragOptions">
          <transition-group>
              <div v-for="element in willcriteria" :key="element" id="dragele">
                  {{element}}
              </div>
          </transition-group>
      </draggable>
    </div>

    <label id="id2"><strong>&#187; Eliminate all the persons with total count of workshops &#62; </strong>
      <label>
    <input v-if = "key2" v-model = "tcnt"
    @blur= "key2 = false; $emit('update')"
    @keyup.enter = "key2=false; $emit('update')" id="inp"
    @change="$store.commit('tcnt', tcnt)">
      <label v-else @click = "key2 = true;"> {{tcnt}}</label>
      <strong> .</strong>
    </label>
    </label><br>

    <strong id="lavaildrag" > Selection of workshow team from available members : (Descending order)</strong>
    <div id ="availdrag">
      <strong >&#187; Solve conflicts in order :</strong>
      <draggable v-model="availcriteria" v-on:change="availupdate(availcriteria)" v-bind="dragOptions">
          <transition-group>
              <div v-for="element in availcriteria" :key="element" id="dragele">
                  {{element}}
              </div>
          </transition-group>
      </draggable>
    </div>
    <label id="id3"><strong>&#187; Eliminate all the persons with total count of workshops &#60; </strong>
      <label>
    <input v-if = "key3" v-model = "tcntt"
    @blur= "key3 = false; $emit('update')"
    @keyup.enter = "key3=false; $emit('update')" id="inp"
    @change="$store.commit('tcntt', tcntt)">
      <label v-else @click = "key3 = true;"> {{tcntt}}</label>
      <strong> .</strong>
    </label>
    </label><br>
  </div>
  <button id="msub" @click="formSubmit">Submit</button>
<!-- <p id="rmsg">Output:</p> -->
<p id="rep"> {{output.msg}}</p>
<table id="rmsg">
  <thead>
    <th >Workshop Team:</th>
  </thead>
  <tbody>
    <tr v-for="(it,j) in output.workshop_team" :key="j">
      <td>
        {{it}}
      </td>
    </tr>
  </tbody>
</table>
  </div>
</template>
<script>
import draggable from 'vuedraggable'
export default {
  components: {
    draggable
  },
  mounted () {
    console.log('Component mounted.')
    this.workshoplist()
  },
  computed: {
    dragOptions () {
      return {
        animation: 500,
        group: 'description',
        disabled: false,
        ghostClass: 'ghost'
      }
    }
  },
  data () {
    return {
      key1: '',
      demo: this.$store.getters.demo,
      key2: '',
      tcnt: this.$store.getters.tcnt,
      key3: '',
      tcntt: this.$store.getters.tcntt,
      selectedworkshop: this.$store.getters.selectedworkshop,
      wrklist: this.$store.getters.wrklist,
      showing: this.$store.getters.algoshowing,
      willcriteria: this.$store.getters.willcriteria,
      availcriteria: this.$store.getters.availcriteria,
      lang: this.$store.getters.lang,
      output: this.$store.getters.algooutput,
      authenticated: this.$store.getters.getAuthenticated,
      auth: this.$store.getters.getAuth
    }
  },
  watch: {
  },
  methods: {
    logout () {
      this.auth.logout()
      this.$store.commit('changeAuth', this.auth)
    },
    willupdate (event) {
      this.willcriteria.splice(event.newIndex, 0, this.willcriteria.splice(event.oldIndex, 1)[0])
      this.$store.commit('willcriteria', this.willcriteria)
      console.log(this.willcriteria)
    },
    availupdate (event) {
      this.availcriteria.splice(event.newIndex, 0, this.availcriteria.splice(event.oldIndex, 1)[0])
      this.$store.commit('availcriteria', this.availcriteria)
      console.log(this.availcriteria)
    },
    savehcn (host, index) {
      console.log(host, index)
      this.selectedworkshop = host
      this.$store.commit('selectedworkshop', this.selectedworkshop)
      this.showing = !this.showing
      this.$store.commit('algoshowing', this.showing)
    },
    itemVisible (item) {
      const currentName = item.toLowerCase()
      const currentInput = this.selectedworkshop.toLowerCase()
      return currentName.includes(currentInput)
    },
    workshoplist () {
      this.axios.post('http://localhost:8081/api/main/getwrklist', {
      })
        .then(wrklist => {
          this.wrklist = wrklist.data
          console.log(this.wrklist)
          this.$store.commit('wrklist', this.wrklist)
        })
        .catch(function (error) {
          this.wrklist = error
        })
    },
    formSubmit (e) {
      e.preventDefault()
      this.output = []
      this.$store.commit('algooutput', this.output)
      console.log(this.selectedworkshop)
      this.axios.post('http://localhost:8081/api/main/algo', {
        selectedworkshop: this.selectedworkshop,
        willcriteria: this.willcriteria,
        availcriteria: this.availcriteria,
        lang: this.lang,
        tcnt: this.tcnt,
        tcntt: this.tcntt,
        demo: this.demo
      })
        .then(output => {
          this.output = output.data
          console.log(this.output)
          this.$store.commit('algooutput', this.output)
          // if (this.output.status === 'Created Successfully') {
          //   this.success = true
          // }
        })
        .catch(function (error) {
          this.output = error
        })
    }
  }
}
</script>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
.form-control{
  margin:10px
}
h1{
position: absolute;
left: 35%;
top: 2%;
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
width: 96%;
height: 90%;
left: 1%;
right:1%;
top: 9%;
background: #6EA5F7;
border: 1px solid #000000;
box-sizing: border-box;
border-radius: 10px;
}
#wrk{
  position: absolute;
width: 154px;
height: 25px;
left: 4%;
top: 9%;

font-family: Radley;
font-size: 17px;
line-height: 30px;
display: flex;
align-items: center;
text-align: center;
color: #000000;
}
#id1{
  position: absolute;
left: 8%;
top: 30%;
}
#id2{
  position: absolute;
left: 8%;
top: 58%;
}
#id3{
  position: absolute;
left: 8%;
top: 89%;
}
#wrki{
  position: absolute;
left: 25%;
top: 8.5%;
}
#lwilldrag{
  position: absolute;
left: 4%;
top: 25%;
}
#lavaildrag{
  position: absolute;
left: 4%;
top: 65%;
}
#willdrag{
  position: absolute;
left: 8%;
top: 35%;
}
#availdrag{
  position: absolute;
left: 8%;
top: 70%;
}
#lang{
position: absolute;
width: 154px;
height: 25px;
left: 4%;
top: 15.5%;

font-family: Radley;
font-size: 17px;
line-height: 30px;
display: flex;
align-items: center;
text-align: center;

color: #000000;

}
#dragele{
  background :#FFFFFF;
  margin: 3px;
  padding-left: 5px;
  padding-right: 5px;
  box-shadow: 6px 7px 2px rgba(0, 0, 0, 0.3);
  border-radius: 0px;
}
#msub{
position: absolute;
left:47%;
top: 25%;
}
#langi{
position: absolute;
left: 25%;
top: 15%;
}
#rmsg{
  position: absolute;
  right:24%;
  top: 25%;
}
#rep{
  position: absolute;
  left:62%;
  top: 60%;
}
#inp{
  width:25px;
  height:22px;
}
table, th, td {
  border: 1px solid black;
  border-collapse: collapse;
  padding:3px;
  padding-left:6px;
}
</style>
