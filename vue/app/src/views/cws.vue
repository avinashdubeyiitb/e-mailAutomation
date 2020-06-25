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
    <h1>Create Workshop </h1>
  <div id="col1inner" >
    <div >
    <strong><p id="fd">Fill details:</p></strong>
    <form @submit="formSubmit">
      <strong id="hcnstatel">Hcn State:</strong>
      <div id="hcnstate">
          <b-dropdown  v-bind:text="state" >
            <div v-for="(p,i) in statedisdata" v-bind:key='i' >
              <div v-for="(sta,index) in p" v-bind:key='index' >
                <b-dropdown-item @click='selectedstate(sta.state,index)' v-model="state">{{sta.state}}</b-dropdown-item>
              </div>
            </div>
          </b-dropdown>
      </div>

    <strong id="hcn" >Host College Name: </strong>

    <div class="dropdown" id="hcni">
  <input v-model="selectedhcn" class="dropdown-input" type="text" placeholder="Find college" @click="chngclg()"/>
    <div  v-show="selectedhcn" class="dropdown-list" style="z-index:100; position: fixed;background: #FFFFFF">
      <div v-for="(p,i) in hcn" v-bind:key='i' v-show="showing" >
        <div  v-for="(host,index) in p" v-bind:key='index' v-show="itemVisible(host)" @click="savehcn(host,index)" class="dropdown-item">
          {{host}}
        </div>
      </div>
      </div>
  </div>

    <strong id="startdate">Start Date:</strong>
    <input id="startdatei" type="date" v-model="startdate"><br>
    <strong id="enddate">End Date:</strong>
    <input id="enddatei" type="date" v-model="enddate"><br>
    <strong id="venueadd">Venue Address:</strong>
    <input id="venueaddi" type="text" v-model="venueadd"><br>
    <strong id="cooname">Coordinator Name:</strong>
    <input id="coonamei" type="text" v-model="cooname"><br>
    <strong id="cooemail">Coordinator Email:</strong>
    <input id="cooemaili" type="email" v-model="cooemail"><br>
    <strong id="coono">Coordinator Cont.:</strong>
    <input id="coonoi" type="tel" v-model="coono"><br>

    <button id="msub">Submit</button>
    </form>
  </div>

<button id="nsub" @click="discard">New</button>

<div v-show="success" id="rmsg">
  <p>{{output.status}}</p>
  <label>Workshop Created:
  <table>
    <thead>
      <th>Host College</th>
      <th>Start date</th>
      <th>End date</th>
      <th>Venue Address</th>
      <th>Coordinator name</th>
      <th>Coordinator email</th>
      <th>Coordinator contact</th>
    </thead>
    <tr>
      <td>{{selectedhcn}}</td>
      <td>{{startdate}}</td>
      <td>{{enddate}}</td>
      <td>{{venueadd}}</td>
      <td>{{cooname}}</td>
      <td>{{cooemail}}</td>
      <td>{{coono}}</td>
    </tr>
  </table>
</label>
</div>
</div>
  </div>
</template>
<script>
import statedisdata from '../assets/states-and-districts.json'
export default {
  mounted () {
    console.log('Component mounted.')
  },
  computed: {
  },
  data () {
    return {
      port: this.$store.getters.port,
      statedisdata: statedisdata,
      state: 'State',
      index: '',
      startdate: '',
      enddate: '',
      venueadd: '',
      cooname: '',
      cooemail: '',
      coono: '',
      output: '',
      selectedhcn: this.$store.getters.selectedhcn,
      hcn: [],
      success: false,
      showing: true
    }
  },
  watch: {
  },
  methods: {
    chngclg () {
      this.showing = true
    },
    discard () {
      this.state = 'State'
      this.selectedhcn = ''
      this.$store.commit('selectedhcn', this.selectedhcn)
      this.startdate = ''
      this.enddate = ''
      this.venueadd = ''
      this.cooname = ''
      this.cooemail = ''
      this.coono = ''
      this.success = false
    },
    selectedstate (state, index) {
      console.log(state, index)
      this.state = state
      this.index = index
      this.axios.post('http://localhost:' + this.port + '/api/main/gethcn', {
        state: this.state
      })
        .then(hcn => {
          this.hcn = hcn.data
          console.log(this.hcn)
        })
        .catch(function (error) {
          this.hcn = error
        })
    },
    savehcn (host, index) {
      console.log(host, index)
      this.selectedhcn = host
      this.$store.commit('selectedhcn', this.selectedhcn)
      this.$store.commit('awsselectedworkshop', this.selectedhcn)
      this.$store.commit('selectedworkshop', this.selectedhcn)
      this.showing = !this.showing
    },
    itemVisible (item) {
      const currentName = item.toLowerCase()
      const currentInput = this.selectedhcn.toLowerCase()
      return currentName.includes(currentInput)
    },
    formSubmit (e) {
      e.preventDefault()
      const currentObj = this
<<<<<<< HEAD
      this.axios.post('http://localhost:8081/api/main/cwssubmit', {
=======
      this.isNight = false
      this.isNight1 = false
      this.isNight2 = true
      this.isNight3 = true
      this.axios.post('http://localhost:' + this.port + '/api/main/cwssubmit', {
>>>>>>> e6bc0ef8aa4c3fe571eae7c2045065e261764e93
        hcn: this.selectedhcn,
        startdate: this.startdate,
        enddate: this.enddate,
        venueadd: this.venueadd,
        cooname: this.cooname,
        cooemail: this.cooemail,
        coono: this.coono
      })
        .then(output => {
          this.output = output.data
          if (this.output.status === 'Created Successfully') {
            this.success = true
          }
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
/*
a {
  color: #42b983;
}
.form-control{
  margin:10px
}

img{
  height:200px;
  width:200px;
}*/
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
#para1{
position: relative;
width: 12em;
height: 4em;
left: 22%;
top: 4%;
font-style: normal;
font-weight: normal;
font-size: 24px;
line-height: 30px;
text-align: center;
color: #000000;
}*/
#fd{
position: absolute;
width: 154px;
height: 25px;
left: 4%;
top: 1%;
font-size: 20px;
line-height: 30px;
text-align: center;
color: #000000;
}

#hcn{
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
#hcni{
  position: absolute;
left: 36%;
top: 15.5%;

}
#startdate{
position: absolute;
width: 154px;
height: 25px;
left: 4%;
top: 20.5%;

font-family: Radley;
font-size: 17px;
line-height: 30px;
display: flex;
align-items: center;
text-align: center;

color: #000000;

}
#startdatei{
position: absolute;
left: 36%;
top: 20.5%;
}
#enddate{
position: absolute;
width: 154px;
height: 25px;
left: 4%;
top: 27%;

font-family: Radley;
font-size: 17px;
line-height: 30px;
display: flex;
align-items: center;
text-align: center;

color: #000000;

}
#enddatei{
position: absolute;
left: 36%;
top: 27%;
}
#venueadd{
position: absolute;
width: 154px;
height: 25px;
left: 4%;
top: 33.5%;

font-family: Radley;
font-size: 17px;
line-height: 30px;
display: flex;
align-items: center;
text-align: center;

color: #000000;

}
#venueaddi{
position: absolute;
left: 36%;
top: 33.5%;

}
#cooname{
position: absolute;
width: 154px;
height: 25px;
left: 4%;
top: 39.5%;

font-family: Radley;
font-size: 17px;
line-height: 30px;
display: flex;
align-items: center;
text-align: center;

color: #000000;

}
#coonamei{
position: absolute;
left: 36%;
top: 39.5%;
}
#cooemail{
position: absolute;
width: 154px;
height: 25px;
left: 4%;
top: 45.5%;

font-family: Radley;
font-size: 17px;
line-height: 30px;
display: flex;
align-items: center;
text-align: center;

color: #000000;

}
#cooemaili{
position: absolute;
left: 36%;
top: 45.5%;
}
#coono{
position: absolute;
width: 154px;
height: 25px;
left: 4%;
top: 51%;

font-family: Radley;
font-size: 17px;
line-height: 30px;
display: flex;
align-items: center;
text-align: center;

color: #000000;

}
#coonoi{
position: absolute;
left: 36%;
top: 51%;
}
#hcnstatel{
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
#hcnstate{
position: absolute;
left: 36%;
top: 9%;
}
/*
#recipientdis{
position: absolute;
width: 154px;
height: 25px;
left: 4%;
top: 57%;

font-family: Radley;
font-size: 17px;
line-height: 30px;
display: flex;
align-items: center;
text-align: center;

color: #000000;

}
#recipientdisi{
position: absolute;
left: 36%;
top: 57%;
}*/
#msub{
position: absolute;
right:10%;
top: 53%;
}
#nsub{
position: absolute;
right:5%;
top: 53%;
}
#rmsg{
  position: absolute;
  left:10%;
  top: 60%;
}
/*
#or{
  position: absolute;
  left:20%;
  top: 66%;
}
#up{
  position: absolute;
  left:40%;
  top: 71%;
}
#file{
  position: absolute;
  left:20%;
  top: 76%;
}
#csub{
  position: absolute;
  right:10%;
  top: 82%;
}

#popover-reactive-1{
position: absolute;
top:80%;
left:4%;
}
#popover-reactive-2{
position: absolute;
top:80%;
left:40%;
}

#bcancel {
  position: absolute;
  top:80%;
  left:0%;
  margin:30px;
}
#bsure{
  position: absolute;
  top:80%;
  left:90px;
  margin:30px;
}
#bstd {
  position: absolute;
  width:110px;
  top:100%;
  left:0%;
  margin:30px;
}
#bdiscard{
  position: absolute;
  top:100%;
  left:130px;
  margin:30px;
}
#save{
  position: absolute;
  top:80%;
  right:10%;
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
table, th, td {
  border: 1px solid black;
  border-collapse: collapse;
  padding:0px;
  padding-left:6px;

}
</style>
