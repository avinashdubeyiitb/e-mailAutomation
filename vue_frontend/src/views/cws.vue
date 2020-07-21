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
    <div id="col2inner" >
      <strong id="hcnactivestatus">Select Workshop:</strong>
      <div id="hcnactivestatusi" >
      <b-dropdown  v-bind:text="selectedworkshop1" class="dropsize">
        <b-dropdown-item v-for="host in wrklist.list" v-bind:key='host[0]' @click="selectedworkshop1 = host[0];savestt(host[1])">
          {{host[0]}}
        </b-dropdown-item>
      </b-dropdown>
      </div>
      <!--
      <div class="dropdown" id="hcnactivestatusi" >
      <input v-model="selectedworkshop1" class="dropdown-input" type="text" placeholder="Select"  @click="chngclg1()"/>
        <div  v-show="selectedworkshop1" class="dropdown-list" style="z-index:100; position: fixed;background: #FFFFFF">
          <div v-show="showing1">
            <div  v-for="host in wrklist.list" v-show="itemVisible1(host[0])" v-bind:key='host[0]' class="dropdown-item" @click="showing1 = !showing1;selectedworkshop1 = host[0];savestt(host[1])">
              {{host[0]}}
            </div>
          </div>
          </div>
          </div>-->
          <strong id="isactv">Is Active:</strong>
            <div class="form-check" id="isactvi1">
                <label class="form-check-label">
                  <input type="radio" :checked="isactive === 'True'" class="form-check-input" name="optradio" @click="isactive = 'True'">
                  True
                </label>
            </div>
            <div class="form-check" id="isactvi2">
                <label class="form-check-label">
                  <input type="radio" :checked="isactive === 'False'" class="form-check-input" name="optradio" @click="isactive = 'False'">
                  False
                </label>
            </div>
            <button id="sub4" @click="savewrkactv">Save</button>
    </div>
    <div id="col1inner">
    <strong><p id="fd">Fill details:</p></strong>
    <form @submit="formSubmit">
      <strong id="hcnstatel">Host State:</strong>
      <div id="hcnstate">
          <b-dropdown  v-bind:text="state" class="dropsize">
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
    <input id="enddatei" type="date" v-model="enddate" :min=startdate><br>
    <strong id="venueadd">Venue Address:</strong>
    <input id="venueaddi" type="text" v-model="venueadd"><br>
    <strong id="cooname">Coordinator Name:</strong>
    <input id="coonamei" type="text" v-model="cooname"><br>
    <strong id="cooemail">Coordinator Email:</strong>
    <input id="cooemaili" type="email" v-model="cooemail"><br>
    <strong id="coono">Coordinator Cont.:</strong>
    <input id="coonoi" type="tel" v-model="coono" @input="acceptNumber" required><br>

    <button id="msub">Submit</button>
    </form>
    <button id="nsub" @click="discard">Clear</button>
  </div>

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
</template>
<script>
export default {
  mounted () {
    console.log('Component mounted.')
    this.workshoplist()
  },
  computed: {
  },
  data () {
    return {
      url: this.$store.getters.url,
      statedisdata: this.$store.getters.statedisdata,
      state: 'State',
      index: '',
      showing1: true,
      startdate: '',
      enddate: '',
      venueadd: '',
      cooname: '',
      cooemail: '',
      coono: '',
      scoono: '',
      output: '',
      selectedhcn: this.$store.getters.selectedhcn,
      hcn: [],
      success: false,
      showing: true,
      wrklist: [],
      selectedworkshop1: 'Host College Name',
      selectedworkshop: '',
      isactive: ''
    }
  },
  watch: {
  },
  methods: {
    savestt (isactv) {
      this.isactive = isactv
    },
    chngclg1 () {
      this.showing1 = true
    },
    chngclg () {
      this.showing = true
    },
    savewrkactv () {
      const currentObj = this
      this.selectedworkshop = this.$store.getters.awsselectedworkshop
      this.axios.post(this.url + '/api/main/savewrkactv', {
        isactive: this.isactive,
        workshop: this.selectedworkshop1
      })
        .then(function (request) {
          console.log(request)
          currentObj.workshoplist()
          if (currentObj.selectedworkshop === currentObj.selectedworkshop1 && currentObj.isactive === 'False') {
            currentObj.selectedworkshop = ''
            currentObj.$store.commit('awsselectedworkshop', '')
          }
          currentObj.isactive = ''
          currentObj.selectedworkshop1 = 'Host College Name'
        })
        .catch(function (error) {
          console.log(error)
        })
    },
    workshoplist () {
      this.axios.post(this.url + '/api/main/getwrklist', {
      })
        .then(wrklist => {
          this.wrklist = wrklist.data
          console.log(this.wrklist)
        })
        .catch(function (error) {
          this.wrklist = error
        })
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
      this.axios.post(this.url + '/api/main/gethcn', {
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
    itemVisible1 (item) {
      console.log(item)
      const currentName = item.toLowerCase()
      const currentInput = this.selectedworkshop1.toLowerCase()
      return currentName.includes(currentInput)
    },
    itemVisible (item) {
      const currentName = item.toLowerCase()
      const currentInput = this.selectedhcn.toLowerCase()
      return currentName.includes(currentInput)
    },
    formSubmit (e) {
      e.preventDefault()
      const currentObj = this
      console.log(this.scoono)
      this.axios.post('http://localhost:8081/api/main/cwssubmit', {
        hcn: this.selectedhcn,
        startdate: this.startdate,
        enddate: this.enddate,
        venueadd: this.venueadd,
        cooname: this.cooname,
        cooemail: this.cooemail,
        coono: this.scoono
      })
        .then(output => {
          this.output = output.data
          console.log(this.output)
          if (this.output.status === 'Created Successfully') {
            this.success = true
          }
          this.workshoplist()
        })
        .catch(function (error) {
          currentObj.output = error
        })
    },
    acceptNumber () {
      const x = this.coono.replace(/\D/g, '').match(/(\d{0,2})(\d{0,3})(\d{0,3})(\d{0,4})/)
      this.coono = !x[3] ? (!x[2] ? x[1] : '(' + '+' + x[1] + ')' + ' ' + x[2]) : '(' + '+' + x[1] + ')' + ' ' + x[2] + '-' + x[3] + (x[4] ? '-' + x[4] : '')
      this.scoono = x[1] + x[2] + x[3] + x[4]
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
width: 43%;
height: 90%;
left: 7%;
top: 10%;
z-index: -1;
border: 1px solid #000000;
box-sizing: border-box;
border-radius: 10px;
}
#col2inner{
position: absolute;
width: 48%;
height: 90%;
right: 1%;
top: 10%;
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
left:45%;
top: 58%;
}
#nsub{
position: absolute;
left:60%;
top: 58%;
}
#rmsg{
  position: absolute;
  left:5%;
  top: 65%;
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
#hcnactivestatus{
position: absolute;
width: 154px;
height: 25px;
left: 10%;
top: 11%;

font-family: Radley;
font-size: 17px;
line-height: 30px;
display: flex;
align-items: center;
text-align: center;

color: #000000;

}
#hcnactivestatusi{
position: absolute;
left: 40%;
top: 10%;
}
#isactv{
position: absolute;
width: 154px;
height: 25px;
left: 10%;
top: 19%;

font-family: Radley;
font-size: 17px;
line-height: 30px;
display: flex;
align-items: center;
text-align: center;

color: #000000;

}
#isactvi1{
position: absolute;
left: 45%;
top: 19%;
}
#isactvi2{
position: absolute;
left: 45%;
top: 23%;
}

#sub4{
position: absolute;
right:10%;
top: 27%;
}
.dropdown-list{
  max-height: 160px;
  overflow-y: auto;
  z-index:5;
}
</style>
