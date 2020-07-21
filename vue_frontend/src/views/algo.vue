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
    <b-button v-b-modal.stats size="sm" id="stats" @click="getallinfo">Members Stats</b-button>
            <b-modal size="xl" id="stats" title="Stats" hide-footer scrollable>
              <table>
                <thead>
                  <th><button @click="show1 = !show1;show2 = false;show3 = false">Count of Workshop taken</button></th>
                  <th><button @click="show2 = !show2;show1 = false;show3 = false">Willingness/Unavailability</button></th>
                  <th><button @click="show3 = !show3;show2 = false;show1 = false">Demo details</button></th>
                </thead>
                <tbody>
                </tbody>
              </table>
            <b-container class="px-2" v-show="show1">
              <table>
                <thead >
                  <th v-for="(x,y) in response1.head_wtc " :key="y">{{x}}</th>
                </thead>
                <tbody>
              <tr v-for="(x2,j2) in response1.WorkshopsTakenCount" :key="j2">
                <td v-for="(value2,key2) in x2" :key="key2">{{value2}}</td>
              </tr>
                </tbody>
              </table>
            </b-container>
            <b-container class="px-2" v-show="show2">
              <div id="content">
                <div class="text-uppercase text-bold">id selected: {{selected}}</div>
          <table class="table table-hover">
          <thead>
          <tr>
          <th>
          <label class="form-checkbox">
          <input type="checkbox" v-model="selectAll" @click="select">
          </label>
          </th>
          <th>College Name</th>
          </tr>
          </thead>
          <tbody>
          <tr v-bind:key="name" v-for="name in response1.WorkshopTeamStatus">
          <td>
          <label class="form-checkbox">
          <input type="checkbox" :value="name" v-model="selected" @change="$store.commit('selected', selected);clginfo()">
          </label>
          </td>
          <td>{{name}}</td>
          </tr>
          </tbody>
          </table>
            </div>
              <table v-show="avail">
                <thead >
                  <th v-for="(x,y) in response2.head_wts " :key="y">{{x}}</th>
                </thead>
                <tbody v-for="(x,y) in response2.dtl" :key="y">
              <tr v-for="(value4,key4) in x" :key="key4">
                <td v-for="(val,key) in value4" :key="key">{{val}}</td>
              </tr>
                </tbody>
              </table>
            </b-container>
            <b-container class="px-2" v-show="show3">
              <table>
                <thead >
                  <th v-for="(x,y) in response1.head_dd " :key="y">{{x}}</th>
                </thead>
                <tbody>
              <tr v-for="(x6,j6) in response1.DemoDtls" :key="j6">
                <td v-for="(value6,key6) in x6" :key="key6">{{value6}}</td>
              </tr>
                </tbody>
              </table>
            </b-container>
            </b-modal>
    <h1>Algorithm for Team Selection </h1>
  <div id="col1inner" >
    <strong id="wrk" >Select Workshop:</strong>
    <div class="dropdown" id="wrki">
  <input v-model="selectedworkshop" class="dropdown-input" type="text" placeholder="Select"  @click="chngclg()"/>
    <div  v-show="selectedworkshop" class="dropdown-list" style="z-index:100; position: fixed;background: #FFFFFF">
      <div v-for="(p,i) in wrklist" v-bind:key='i' v-show="showing1">
        <div  v-for="(host,index) in p" v-bind:key='index' v-show="itemVisible1(host[0])" @click="savehcn(host[0],index)" class="dropdown-item">
          {{host[0]}}
        </div>
      </div>
      </div>
  </div>
  <strong id="lang">Preferred Language:</strong>
  <div class="dropdown" id="langi">
    <input  type="text" v-model="selectedlang" class="dropdown-input" @click="chnglang()" placeholder="Select"><br>
  <div  v-show="selectedlang" class="dropdown-list" style="z-index:100; position: fixed;background: #FFFFFF">
    <div v-show="showing2" v-for="(p,i) in lang" v-bind:key='i'>
      <div  v-for="(host,index) in p" v-bind:key='index' v-show="itemVisible2(host)" @click="savelang(host,index)" class="dropdown-item">
        {{host}}
      </div>
    </div>
    </div>
</div>
  <strong id="lwilldrag" >Selection of workshop team from willing members : (Ascending order)</strong><br>
  <label id="id1"><strong>&#187; Demo is clear for atleast </strong>
    <label>
  <input v-if = "key1" v-model = "demo"
  @blur= "key1 = false; $emit('update')"
  @keyup.enter = "key1=false; $emit('update')" id="inp">
    <label v-else @click = "key1 = true;"> {{demo}}</label>
    <strong> modules .</strong>
  </label>
  </label><br>

    <div id ="willdrag">
      <strong >&#187; Solve conflicts in order :</strong>
      <draggable v-model="willcriteria" v-on:change="willupdate(willcriteria)" v-bind="dragOptions1">
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
    @keyup.enter = "key2=false; $emit('update')" id="inp">
      <label v-else @click = "key2 = true;"> {{tcnt}}</label>
      <strong> .</strong>
    </label>
    </label><br>

    <strong id="lavaildrag" > Selection of workshow team from available members : (Descending order)</strong>
    <div id ="availdrag">
      <strong >&#187; Solve conflicts in order :</strong>
      <draggable v-model="availcriteria" v-on:change="availupdate(availcriteria)" v-bind="dragOptions2">
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
    @keyup.enter = "key3=false; $emit('update')" id="inp">
      <label v-else @click = "key3 = true;"> {{tcntt}}</label>
      <strong> .</strong>
    </label>
    </label><br>
  <button id="msub" @click="formSubmit">Submit</button>
  <button id="nsub" @click="savealgo">Confirm changes!</button>

<p id="rep"> {{output.msg}}</p>
<table id="rmsg">
  <thead>
    <th >Workshop Team:</th>
  </thead>
  <tbody>
    <tr v-for="(it,j) in output.workshop_team" :key="j">
      <td>
        {{it}}<b-button size="sm" v-b-modal="'box'+j" @click="getinfo(it)">Stats</b-button>
            <b-modal :id="'box'+j" size="xl" title="Stats" hide-footer scrollable>
              <table>
                <thead>
                  <th><button @click="show1 = !show1;show2 = false;show3 = false">Count of Workshop taken</button></th>
                  <th><button @click="show2 = !show2;show1 = false;show3 = false">Willingness/Unavailability</button></th>
                  <th><button @click="show3 = !show3;show2 = false;show1 = false">Demo details</button></th>
                </thead>
                <tbody>
                </tbody>
              </table>
            <b-container class="px-2" v-show="show1">
              <table>
                <thead v-for="(x1,j1) in response.WorkshopsTakenCount" :key="j1">
                  <th v-for="(value1,key1) in x1" :key="key1">{{key1}}</th>
                </thead>
                <tbody>
              <tr v-for="(x2,j2) in response.WorkshopsTakenCount" :key="j2">
                <td v-for="(value2,key2) in x2" :key="key2">{{value2}}</td>
              </tr>
                </tbody>
              </table>
            </b-container>
            <b-container class="px-2" v-show="show2">
              <table>
                <thead v-for="(x3,j3) in response.WorkshopTeamStatus" :key="j3">
                  <th v-for="(value3,key3) in x3" :key="key3">{{key3}}</th>
                </thead>
                <tbody>
              <tr v-for="(x4,j4) in response.WorkshopTeamStatus" :key="j4">
                <td v-for="(value4,key4) in x4" :key="key4">{{value4}}</td>
              </tr>
                </tbody>
              </table>
            </b-container>
            <b-container class="px-2" v-show="show3">
              <table>
                <thead v-for="(x5,j5) in response.DemoDtls" :key="j5">
                  <th v-for="(value5,key5) in x5" :key="key5">{{key5}}</th>
                </thead>
                <tbody>
              <tr v-for="(x6,j6) in response.DemoDtls" :key="j6">
                <td v-for="(value6,key6) in x6" :key="key6">{{value6}}</td>
              </tr>
                </tbody>
              </table>
            </b-container>
            </b-modal>
      </td>
    </tr>
  </tbody>
</table>

<button id="sub1" @click="loader = true;kavi_sir_mail()">Send Mail to Kavi sir</button>
<div id="result">{{result}}</div>
</div>
<div id="loader" v-show="loader">
<b-button variant="danger" disabled>
  <b-spinner small ></b-spinner>
  Sending...
</b-button>
</div>
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
    this.getlang()
    this.getalgodetail()
  },
  computed: {
    dragOptions1 () {
      return {
        animation: 500,
        group: 'willcriteria',
        disabled: false,
        ghostClass: 'ghost'
      }
    },
    dragOptions2 () {
      return {
        animation: 500,
        group: 'availcriteria',
        disabled: false,
        ghostClass: 'ghost'
      }
    }
  },
  data () {
    return {
      url: this.$store.getters.url,
      key1: '',
      demo: '',
      key2: '',
      tcnt: '',
      key3: '',
      tcntt: '',
      show1: true,
      show2: false,
      show3: false,
      selectedworkshop: this.$store.getters.selectedworkshop,
      selectedlang: this.$store.getters.selectedlang,
      wrklist: this.$store.getters.wrklist,
      lang: this.$store.getters.lang,
      showing1: false,
      showing2: false,
      willcriteria: [],
      availcriteria: [],
      output: this.$store.getters.algooutput,
      out: '',
      algodetail: '',
      result: '',
      response: '',
      loader: false,
      response1: '',
      response2: '',
      selected: [],
      avail: false,
      selectAll: false
    }
  },
  watch: {
  },
  methods: {
    clginfo () {
      this.avail = false
      if (this.selected.length) {
        this.axios.post(this.url + '/api/main/clginfo', {
          selectedlist: this.selected
        })
          .then(response2 => {
            this.response2 = response2.data
            // console.log(response2)
            this.avail = true
          })
          .catch(function (error) {
            console.log(error)
          })
      }
    },
    select () {
      this.selected = []
      if (!this.selectAll) {
        for (const pk in this.response1.WorkshopTeamStatus) {
          console.log(pk)
          this.selected.push(this.response1.WorkshopTeamStatus[pk])
        }
        this.avail = false
        this.axios.post(this.url + '/api/main/clginfo', {
          selectedlist: this.selected
        })
          .then(response2 => {
            this.response2 = response2.data
            // console.log(response2)
            this.avail = true
          })
          .catch(function (error) {
            console.log(error)
          })
      } else {
        this.selected = []
        this.avail = false
      }
    },
    getinfo (name) {
      console.log(name)
      this.axios.post(this.url + '/api/main/meminfo', {
        selectedworkshop: this.selectedworkshop,
        user: this.$store.getters.user_name,
        name: name
      })
        .then(response => {
          this.response = response.data
          // console.log(response)
        })
        .catch(function (error) {
          console.log(error)
        })
    },
    getallinfo () {
      this.axios.post(this.url + '/api/main/getallinfo', {
        selectedworkshop: this.selectedworkshop
      })
        .then(response1 => {
          this.response1 = response1.data
          // console.log(response1)
        })
        .catch(function (error) {
          console.log(error)
        })
    },
    kavi_sir_mail () {
      this.result = 'sending mails'
      this.axios.post(this.url + '/api/main/kavi_sir_mail', {
        selectedworkshop: this.selectedworkshop,
        label: 'willingness-unavailability',
        user: this.$store.getters.user_name,
        team: this.output.workshop_team,
        url: this.$store.getters.url
      })
        .then(response => {
          this.result = response.data
          this.loader = false
        })
        .catch(function (error) {
          console.log(error)
        })
    },
    getalgodetail () {
      this.axios.post(this.url + '/api/main/getalgodetail', {
      })
        .then(algodetail => {
          this.algodetail = algodetail.data
          console.log(this.algodetail)
          this.demo = this.algodetail.demo
          this.tcnt = this.algodetail.tcnt
          this.tcntt = this.algodetail.tcntt
          this.willcriteria = this.algodetail.willcriteria
          this.availcriteria = this.algodetail.availcriteria
        })
        .catch(function (error) {
          this.algodetail = error
        })
    },
    getlang () {
      this.axios.post(this.url + '/api/main/getlang', {
      })
        .then(lang => {
          this.lang = lang.data
          console.log(this.lang)
          this.$store.commit('lang', this.lang)
        })
        .catch(function (error) {
          this.lang = error
        })
    },
    chngclg () {
      this.showing1 = true
    },
    chnglang () {
      this.showing2 = true
    },
    willupdate (event) {
      this.willcriteria.splice(event.newIndex, 0, this.willcriteria.splice(event.oldIndex, 1)[0])
      console.log(this.willcriteria)
    },
    availupdate (event) {
      this.availcriteria.splice(event.newIndex, 0, this.availcriteria.splice(event.oldIndex, 1)[0])
      console.log(this.availcriteria)
    },
    savehcn (host, index) {
      console.log(host, index)
      this.selectedworkshop = host
      this.$store.commit('selectedworkshop', this.selectedworkshop)
      this.showing1 = !this.showing1
      this.$store.commit('algoshowing', this.showing1)
    },
    itemVisible1 (item) {
      const currentName = item.toLowerCase()
      const currentInput = this.selectedworkshop.toLowerCase()
      return currentName.includes(currentInput)
    },
    savelang (host, index) {
      console.log(host, index)
      this.selectedlang = host
      this.$store.commit('selectedlang', this.selectedlang)
      this.showing2 = !this.showing2
    },
    itemVisible2 (item) {
      const currentName = item.toLowerCase()
      const currentInput = this.selectedlang.toLowerCase()
      return currentName.includes(currentInput)
    },
    workshoplist () {
      this.axios.post(this.url + '/api/main/getwrklist', {
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
    savealgo () {
      this.axios.post(this.url + '/api/main/savealgo', {
        willcriteria: this.willcriteria,
        availcriteria: this.availcriteria,
        lang: this.lang,
        tcnt: this.tcnt,
        tcntt: this.tcntt,
        demo: this.demo
      })
        .then(out => {
          this.out = out.data
          console.log(this.out)
        })
        .catch(function (error) {
          this.out = error
        })
    },
    formSubmit (e) {
      e.preventDefault()
      this.output = []
      this.$store.commit('algooutput', this.output)
      console.log(this.tcnt)
      this.axios.post(this.url + '/api/main/algo', {
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
/*
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
}*/
#stats{
  position: absolute;
  top:15%;
  left:70%;
}
#loader{
  position: absolute;
  top:45%;
  left:45%;
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
color: #FFFFFF;
}

#col1inner{
position: absolute;
width: 92%;
height: 90%;
left: 6.5%;
right:1%;
top: 9%;
z-index: -1;
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
left:49%;
top: 93%;
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
#sub1{
  position: absolute;
  right:17%;
  top: 80%;
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
#nsub{
  position: absolute;
  left:37%;
  top: 93%;
}
table, th, td {
  border: 1px solid black;
  border-collapse: collapse;
  padding:3px;
  padding-left:6px;
}
.dropdown-list{
  max-height: 160px;
  overflow-y: auto;
  z-index:10000;
}
#result{
position: absolute;
right:20%;
top: 83%;
}
</style>
