<template>
  <div id="app">
    <h1>Send Workshop Mail</h1>
    <button id="butt" type="button" name="button"><router-link to="/">Home</router-link></button>
  <div id="col1inner" >
    <div v-show="isNight3" >
    <strong><p id="fd">Fill details:</p></strong>
    <form @submit="formSubmit">
    <strong id="hcn" >Host College Name:</strong>
    <input id="hcni" type="text" v-model="hcn"><br>
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
    <strong id="recipientstate">Recipient State:</strong>
    <div id="recipientstatei">
        <b-dropdown  v-bind:text="state" >
          <div v-for="(p,i) in statedisdata" v-bind:key='i' >
            <div v-for="(sta,index) in p" v-bind:key='index' >
              <b-dropdown-item @click='selectedstate(sta.state,index)' v-model="state">{{sta.state}}</b-dropdown-item>
            </div>
          </div>
        </b-dropdown>
    </div>
    <strong id="recipientdis">Recipient District:</strong>
    <div id="recipientdisi">
      <p>{{district}}
        <b-dropdown  v-bind:text="d" >
          <div v-for="(dis,i) in districts" v-bind:key='i'>
            <div v-for="(diss,i) in dis" v-bind:key='i' >
              <b-dropdown-item  @click='selecteddistrict(diss)'>{{diss}}</b-dropdown-item>
            </div>
            </div>
        </b-dropdown></p>
    </div>
    <button id="msub" v-b-modal.modal-1>Submit</button>
    </form>
    <!-- <strong>Response:</strong> -->
    <!-- <pre>
    </pre> -->
    <p id="rmsg">{{output}}</p>
  </div>
</div>
<div id="col2inner">
  <p id="para1" v-show="isNight">" nothing to show right now" </p>
  <img id="img1" v-show="isNight" alt="no-thumbnail" src="../assets/no-thumbnail.jpg">
<p id="para1" v-show="!isNight1">"show right now"</p>
<div v-show="!isNight1">
   <form>
   <label id="srccbcc"><strong>cc/bcc:</strong>
   <b-button v-for='(p,inn) in output.remail' v-bind:key='inn' v-model = "output.remail" >{{p}}<b-button @click="disc(p,inn)" class="close" aria-label="Close"><span class="d-inline-block" aria-hidden="true">&times;</span></b-button></b-button>
    </label><br>
   <label id="srsubject"><strong>subject:</strong>
   <input v-if = "key3" v-model = "output.subject"
   @blur= "key3 = false; $emit('update')"
   @keyup.enter = "key3=false; $emit('update')" id="isrsubject">
         <div v-else>
     <label @click = "key3 = true;"> {{output.subject}} </label>
   </div>
   </label><br>
   <label id="srbody"><strong>body:</strong>
   <input v-if = "key4" v-model = "output.body"
   @blur= "key4 = false; $emit('update')"
   @keyup.enter = "key4=false; $emit('update')" id="isrbody">
    <div v-else>
     <label @click = "key4 = true;"> {{output.body}} </label>
   </div>
  </label><br>
  <label id="srattach"><strong>Attachment:</strong>
  <!-- <input v-if = "key5" v-model = "output.body" -->
  <!-- @blur= "key5 = false; $emit('update')" -->
  <!-- @keyup.enter = "key5=false; $emit('update')" id="isrbody"> -->
  <!-- <div v-else> -->
    <!-- <label @click = "key4 = true;"> {{output.body}} </label> -->
    <label > not Available </label>

  <!-- </div> -->
 </label><br>
 </form>
 </div>
<div v-show="!isNight1">
  <form>
  <b-button id="popover-reactive-1" ref="button1">Approve</b-button>
</form>
  <b-popover
        target="popover-reactive-1"
        triggers="click"
        :show.sync="popoverShow1"
        placement="auto"
        container="my-container"
        ref="popover"
        @hidden="onHidden"
      >
        <template v-slot:title>
          Are you sure you want to continue?
        </template>
        <div >
          <b-button id="bcancel" @click="onClose" size="sm" variant="danger">Cancel</b-button>
          <b-button id="bsure" @click="approve" size="sm" variant="primary">Sure</b-button>
        </div>
      </b-popover>
    <form>
  <b-button id="popover-reactive-2" ref="button2" >Reject</b-button>
</form>
  <b-popover
        target="popover-reactive-2"
        triggers="click"
        :show.sync="popoverShow2"
        placement="auto"
        container="my-container"
        ref="popover"
        @hidden="onHidden"
      >
        <template v-slot:title>
          Are you want to save it in gmail draft or discard it ?
        </template>
        <div>
          <b-button id="bstd" @click="gsave" size="sm" variant="primary">Save to draft</b-button>
          <b-button id="bdiscard" @click="discard" size="sm" variant="danger">Discard</b-button>
        </div>
      </b-popover>
  <!-- </div> -->
  <!-- Output from the popover interaction -->
</div>
<p id="para1" v-show="!isNight2">"show right now"</p>
<div v-show="!isNight2">
     <form>
     <label  id="sremail"><strong >Recipient Id:</strong>
     <input v-if = "key1" v-model = "reqdata.to"
     @blur= "key1 = false; $emit('update')"
     @keyup.enter = "key1=false; $emit('update')">
     <div v-else>
       <label @click = "key1 = true;"> {{reqdata.to}} </label>
     </div>
   </label><br>
     <label id="srccbcc"><strong>cc/bcc:</strong>
     <input v-if = "key2" v-model = "reqdata.ccbcc"
     @blur= "key2 = false; $emit('update')"
     @keyup.enter = "key2=false; $emit('update')" >
           <div v-else>
       <label @click = "key2 = true;">{{reqdata.ccbcc}} </label>
     </div>
      </label><br>
     <label id="srsubject"><strong>subject:</strong>
     <input v-if = "key3" v-model = "reqdata.subject"
     @blur= "key3 = false; $emit('update')"
     @keyup.enter = "key3=false; $emit('update')" id="isrsubject">
           <div v-else>
       <label @click = "key3 = true;"> {{reqdata.subject}} </label>
     </div>
     </label><br>
     <label id="srbody"><strong>body:</strong>
     <input v-if = "key4" v-model = "reqdata.body"
     @blur= "key4 = false; $emit('update')"
     @keyup.enter = "key4=false; $emit('update')" id="isrbody">
      <div v-else>
       <label @click = "key4 = true;"> {{reqdata.body}} </label>
     </div>
    </label><br>
    <label id="srattach"><strong>Attachment:</strong>
    <!-- <input v-if = "key5" v-model = "output.body" -->
    <!-- @blur= "key5 = false; $emit('update')" -->
    <!-- @keyup.enter = "key5=false; $emit('update')" id="isrbody"> -->
    <!-- <div v-else> -->
      <!-- <label @click = "key4 = true;"> {{output.body}} </label> -->
      <label > not Available </label>
      <b-button id="save"> Save </b-button>
    <!-- </div> -->
   </label><br>
 </form>
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
      statedisdata: statedisdata,
      state: 'State',
      index: '',
      in: '',
      districts: [],
      d: 'District',
      district: [],
      isNight: true,
      isNight1: true,
      isNight2: true,
      isNight3: true,
      popoverShow1: false,
      popoverShow2: false,
      popoverShow3: false,
      popoverShow4: false,
      hcn: '',
      startdate: '',
      enddate: '',
      venueadd: '',
      cooname: '',
      cooemail: '',
      coono: '',
      output: '',
      items: [],
      selected: [],
      selectAll: false,
      key1: '',
      key2: '',
      key3: '',
      key4: '',
      key5: '',
      key6: '',
      key7: '',
      key8: '',
      key9: '',
      reqdata: '',
      editedTodo: null
    }
  },
  watch: {
  },
  methods: {
    discard () {
      this.popoverShow1 = false
      this.popoverShow2 = false
      this.isNight = true
      this.isNight1 = true
      this.isNight2 = true
      this.output.hcn = ''
      this.output.remail = ''
      this.output.startdate = ''
      this.output.enddate = ''
      this.output.venueadd = ''
      this.output.cooname = ''
      this.output.cooemail = ''
      this.output.coono = ''
      this.output.state = ''
      this.output.district = ''
      this.output.body = ''
      this.output.subject = ''
    },
    selectedstate (state, index) {
      console.log(state, index)
      this.state = state
      this.index = index
      this.districts = []
      this.districts.push(this.statedisdata.states[index].districts)
    },
    disc (p, inn) {
      console.log(p, inn)
      this.$delete(this.output.remail, inn)
    },
    selecteddistrict (diss) {
      this.district.push(diss)
      this.d = diss
      console.log(diss)
      console.log(this.district)
    },
    onClose () {
      this.popoverShow1 = false
      this.popoverShow2 = false
    },
    onHidden () {
      // Called just after the popover has finished hiding
      // Bring focus back to the button
      this.focusRef(this.$refs.button)
    },
    focusRef (ref) {
    },
    formSubmit (e) {
      e.preventDefault()
      const currentObj = this
      this.isNight = false
      this.isNight1 = false
      this.isNight2 = true
      this.isNight3 = true
      this.axios.post('http://localhost:8081/api/main/awssubmit', {
        hcn: this.hcn,
        startdate: this.startdate,
        enddate: this.enddate,
        venueadd: this.venueadd,
        cooname: this.cooname,
        cooemail: this.cooemail,
        coono: this.coono,
        state: this.state,
        district: this.district
      })
        .then(output => {
          this.output = output.data
        })
        .catch(function (error) {
          currentObj.output = error
        })
    },
    approve (e) {
      e.preventDefault()
      const currentObj = this
      this.axios.post('http://localhost:8081/api/main/approve', {
        ccbcc: this.output.remail,
        body: this.output.body,
        subject: this.output.subject
      })
        .then(function (response) {
          currentObj.output = response.data
          console.log(currentObj.output)
        })
        .catch(function (error) {
          currentObj.output = error
          console.log(currentObj.output)
        })
      this.popoverShow1 = false
    },
    gsave (e) {
      e.preventDefault()
      const currentObj = this
      this.axios.post('http://localhost:8081/api/main/gsave', {
        ccbcc: this.output.remail,
        body: this.output.body,
        subject: this.output.subject
      })
        .then(function (response) {
          currentObj.output = response.data
          console.log(currentObj.output)
        })
        .catch(function (error) {
          currentObj.output = error
          console.log(currentObj.output)
        })
      this.popoverShow2 = false
    }
  }
}
</script>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
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
img{
  height:200px;
  width:200px;
}
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
}
#img1{
position: absolute;
width: 31em;
height: 31em;
left: 3%;
top: 15%;
border-radius: 15px;
}
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
top: 9%;

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
top: 8.5%;

}
#startdate{
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
#startdatei{
position: absolute;
left: 36%;
top: 15%;
}
#enddate{
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
#enddatei{
position: absolute;
left: 36%;
top: 21%;
}
#venueadd{
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
#venueaddi{
position: absolute;
left: 36%;
top: 27%;

}
#cooname{
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
#coonamei{
position: absolute;
left: 36%;
top: 33%;
}
#cooemail{
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
#cooemaili{
position: absolute;
left: 36%;
top: 39%;
}
#coono{
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
#coonoi{
position: absolute;
left: 36%;
top: 45%;
}
#recipientstate{
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
#recipientstatei{
position: absolute;
left: 36%;
top: 51%;
}
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
}
#msub{
position: absolute;
right:10%;
top: 53%;
}
#rmsg{
  position: absolute;
  left:35%;
  top: 70%;
}
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
left:30%;
}
#popover-reactive-3{
position: absolute;
top:70%;
left:4%;
}
#popover-reactive-4{
position: absolute;
top:70%;
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
}
tr ,td,thead,table,th{
  padding:0px;
  padding-left:6px;

}
</style>
