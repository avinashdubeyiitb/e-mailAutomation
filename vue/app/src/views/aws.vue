<template>
  <div id="app">
    <h1>Announce Workshop </h1>
    <button id="butt" type="button" name="button"><router-link to="/home">Home</router-link></button>
    <button class="btn btn-primary btn-margin" v-if="authenticated" @click="logout()">Log Out</button>
  <div id="col1inner" >
    <div v-show="isNight3" >
    <strong><p id="fd">Fill details:</p></strong>
    <form @submit="formSubmit">
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
    <strong id="filldate">Last date to Fill:</strong>
    <input id="filldatei" type="date" v-model="filldate" @change="$store.commit('filldate', filldate)"><br>
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
    <button id="sub1" @click="sendmail">Send Mail to Team</button>
    <button id="sub2" @click="headmail">Send Approval Mails</button>
        <div id="result">{{result}}</div>

    </form>
    <button id="sub3" @click="edtalw">Edit</button>
    <!-- <strong>Response:</strong> -->
    <!-- <pre>
    </pre> -->
    <!-- <p id="rmsg">{{output}}</p> -->
  </div>
  <div v-show="!isNight2">
    <form @submit="sndchngs">
    <label id="hcn" ><strong>Host College Name:</strong>
    <input v-if = "key4" v-model = "reqdata.hcn"
   @blur= "key4 = false; $emit('update')"
   @keyup.enter = "key4=false; $emit('update')" id="hcni"
   @change="$store.commit('awsreqdata',reqdata)">
         <div v-else>
     <label @click = "key4 = true;"> {{reqdata.hcn}} </label>
   </div>
   </label><br>
    <label id="startdate"><strong >Start Date:</strong>
    <input type="date" v-if = "key5" v-model = "reqdata.startdate"
   @blur= "key5 = false; $emit('update')"
   @keyup.enter = "key5=false; $emit('update')" id="startdatei"
   @change="$store.commit('awsreqdata',reqdata)">
         <div v-else>
     <label @click = "key5 = true;"> {{reqdata.startdate}} </label>
   </div>
    </label><br>
    <label id="enddate"><strong>End Date:</strong>
    <input type="date" v-if = "key6" v-model = "reqdata.enddate"
   @blur= "key6 = false; $emit('update')"
   @keyup.enter = "key6=false; $emit('update')" id="enddatei"
   @change="$store.commit('awsreqdata',reqdata)">
         <div v-else>
     <label @click = "key6 = true;"> {{reqdata.enddate}} </label>
   </div>
    </label><br>
    <label  id="venueadd"><strong>Venue Address:</strong>
    <input type="text" v-if = "key7" v-model = "reqdata.venueadd"
   @blur= "key7 = false; $emit('update')"
   @keyup.enter = "key7=false; $emit('update')" id="venueaddi"
   @change="$store.commit('awsreqdata',reqdata)">
         <div v-else>
     <label @click = "key7 = true;"> {{reqdata.venueadd}} </label>
   </div>
    </label><br>
    <label id="cooname"><strong>Coordinator Name:</strong>
    <input type="text" v-if = "key8" v-model = "reqdata.cooname"
   @blur= "key8 = false; $emit('update')"
   @keyup.enter = "key8=false; $emit('update')" id="coonamei"
   @change="$store.commit('awsreqdata',reqdata)">
         <div v-else>
     <label @click = "key8 = true;"> {{reqdata.cooname}} </label>
   </div>
    </label><br>
    <label id="cooemail"><strong>Coordinator Email:</strong>
    <input type="email" v-if = "key9" v-model = "reqdata.cooemail"
   @blur= "key9 = false; $emit('update')"
   @keyup.enter = "key9=false; $emit('update')" id="cooemaili"
   @change="$store.commit('awsreqdata',reqdata)">
         <div v-else>
     <label @click = "key9 = true;"> {{reqdata.cooemail}} </label>
   </div>
    </label><br>
    <label id="coono"><strong>Coordinator Cont.:</strong>
    <input type="tel" v-if = "key1" v-model = "reqdata.coono"
   @blur= "key1 = false; $emit('update')"
   @keyup.enter = "key1=false; $emit('update')" id="coono"
   @change="$store.commit('awsreqdata',reqdata)">
         <div v-else>
     <label @click = "key1 = true;"> {{reqdata.coono}} </label>
   </div>
    </label><br>

    <button id="sub1">Feed</button>
    </form>
  </div>
</div>
<div id="col2inner">
  <p id="para1" v-show="isNight">" nothing to show right now" </p>
  <img id="img1" v-show="isNight" alt="no-thumbnail" src="../assets/no-thumbnail.jpg">
<p id="para1" v-show="!isNight1">"show right now"</p>
<div v-show="!isNight1">
   <form>
   <label id="srbcc"><strong>Bcc:</strong>
     <b-button v-b-modal.modal-3 >Bcc</b-button>
     <b-modal id="modal-3" size="lg" title="Bcc" hide-footer v-on:keyup.enter = "NoEnter" >
     <b-container class="px-2" >
        <b-button v-for='(p,inn) in output.bcc' v-bind:key='inn' v-model = "output.bcc" >{{p}}<b-button @click="disc(p,inn)" class="close" aria-label="Close"><span class="d-inline-block" aria-hidden="true">&times;</span></b-button></b-button>
     </b-container>
     <b-button @click="$bvModal.hide('modal-3')">OK</b-button>
     </b-modal><br>
    </label><br>
   <label id="srsubject"><strong>subject:</strong>
   <input v-if = "key3" v-model = "output.subject"
   @blur= "key3 = false; $emit('update')"
   @keyup.enter = "key3=false; $emit('update')" id="isrsubject"
   @change="$store.commit('awsoutput',output)">
         <div v-else>
     <label @click = "key3 = true;"> {{output.subject}} </label>
   </div>
   </label><br>
   <strong>Body</strong>
   <b-button v-b-modal.modal-2 id="srbody">body</b-button>
 <b-modal id="modal-2" size="lg" title="Body" hide-footer v-on:keyup.enter = "NoEnter" >
 <b-container class="px-2" id="container">
 <span v-html="output.body"></span>
 </b-container>
 <b-button @click="onDivInput($event);$bvModal.hide('modal-2');">OK</b-button>
 </b-modal><br>

   <label id="srattach"><strong>Attachment:</strong>
        <div v-for="(value,key) in output.attachments" v-bind:key="key">
        <b-button >
        <b-button size="sm" @click='getfile(value)' >{{value}}</b-button>
        <b-button @click="disc1(value,key)" class="close" aria-label="Close"><span class="d-inline-block" aria-hidden="true">&times;</span></b-button></b-button>
         </div>
        <input type="file" id="upfile1" ref="upfile1" multiple v-on:change="handleattachUpload"/>
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
</div>
  </div>
</template>
<script>
const { shell } = require('electron')
export default {
  mounted () {
    console.log('Component mounted.')
    this.workshoplist()
  },
  computed: {
  },
  data () {
    return {
      statedisdata: this.$store.getters.statedisdata,
      state: this.$store.getters.awsstate,
      index: this.$store.getters.awsindex,
      in: this.$store.getters.awsin,
      wrklist: this.$store.getters.awswrklist,
      showing: this.$store.getters.awsshowing,
      districts: this.$store.getters.awsdistricts,
      d: this.$store.getters.awsd,
      district: this.$store.getters.awsdistrict,
      isNight: this.$store.getters.awsisNight,
      isNight1: this.$store.getters.awsisNight1,
      isNight2: this.$store.getters.awsisNight2,
      isNight3: this.$store.getters.awsisNight3,
      selectedworkshop: this.$store.getters.awsselectedworkshop,
      popoverShow1: false,
      popoverShow2: false,
      popoverShow3: false,
      popoverShow4: false,
      hcn: this.$store.getters.awshcn,
      filldate: this.$store.getters.filldate,
      output: this.$store.getters.awsoutput,
      items: this.$store.getters.awsitems,
      selected: this.$store.getters.awsselected,
      selectAll: this.$store.getters.awsselectAll,
      key1: '',
      key2: '',
      key3: '',
      key4: '',
      key5: '',
      key6: '',
      key7: '',
      key8: '',
      key9: '',
      reqdata: this.$store.getters.awsreqdata,
      editedTodo: this.$store.getters.awseditedTodo,
      upfile1: this.$store.getters.awsupfile1,
      upfile2: this.$store.getters.awsupfile2,
      result: this.$store.getters.result,
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
    onDivInput (e) {
      this.output.body = document.getElementById('container').innerHTML
      this.$store.commit('awsoutput', this.output)
    },
    edtalw (e) {
      this.isNight2 = false
      this.$store.commit('awsisNight2', this.isNight2)
      this.isNight3 = false
      this.$store.commit('awsisNight3', this.isNight3)
      e.preventDefault()
      const currentObj = this
      this.axios.post('http://localhost:8081/api/main/awsedit', {
        selectedworkshop: this.selectedworkshop
      })
        .then(function (response) {
          currentObj.reqdata = response.data
          this.$store.commit('awsreqdata', this.reqdata)
        })
        .catch(function (error) {
          console.log(error)
        })
    },
    sndchngs (e) {
      this.isNight2 = true
      this.$store.commit('awsisNight2', this.isNight2)
      this.isNight3 = true
      this.$store.commit('awsisNight3', this.isNight3)
      e.preventDefault()
      const currentObj = this
      this.axios.post('http://localhost:8081/api/main/awssave', {
        wid: this.reqdata.wid,
        hcn: this.reqdata.hcn,
        startdate: this.reqdata.startdate,
        enddate: this.reqdata.enddate,
        venueadd: this.reqdata.venueadd,
        cooname: this.reqdata.cooname,
        cooemail: this.reqdata.cooemail,
        coono: this.reqdata.coono
      })
        .then(function (response) {
          currentObj.result = response.data
          this.$store.commit('awsreqdata', this.reqdata)
        })
        .catch(function (error) {
          console.log(error)
        })
    },
    headmail (e) {
      e.preventDefault()
      const currentObj = this
      this.result = 'sending mails'
      this.$store.commit('result', this.result)
      this.axios.post('http://localhost:8081/api/main/headmail', {
        selectedworkshop: this.selectedworkshop
      })
        .then(function (response) {
          currentObj.result = response.data
          this.$store.commit('result', this.result)
        })
        .catch(function (error) {
          console.log(error)
        })
    },
    sendmail (e) {
      e.preventDefault()
      const currentObj = this
      this.result = 'sending mails'
      this.$store.commit('result', this.result)
      this.axios.post('http://localhost:8081/api/main/sendmail', {
        selectedworkshop: this.selectedworkshop
      })
        .then(function (response) {
          currentObj.result = response.data
          this.$store.commit('result', this.result)
        })
        .catch(function (error) {
          console.log(error)
        })
    },
    savehcn (host, index) {
      console.log(host, index)
      this.selectedworkshop = host
      this.$store.commit('awsselectedworkshop', this.selectedworkshop)
      this.showing = !this.showing
      this.$store.commit('awsshowing', this.showing)
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
          this.$store.commit('awswrklist', this.wrklist)
        })
        .catch(function (error) {
          this.wrklist = error
        })
    },
    discard () {
      this.popoverShow1 = false
      this.popoverShow2 = false
      this.isNight = true
      this.$store.commit('awsisNight', this.isNight)
      this.isNight1 = true
      this.$store.commit('awsisNight1', this.isNight1)
      this.isNight2 = true
      this.$store.commit('awsisNight2', this.isNight2)
      this.output.hcn = ''
      this.output.bcc = ''
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
      this.$store.commit('awsoutput', this.output)
      this.reqdata.wid = ''
      this.reqdata.hcn = ''
      this.reqdata.startdate = ''
      this.reqdata.enddate = ''
      this.reqdata.venueadd = ''
      this.reqdata.cooname = ''
      this.reqdata.cooemail = ''
      this.reqdata.coono = ''
      this.$store.commit('awsreqdata', this.reqdata)
    },
    getfile (value) {
      console.log(value)
      if (value === 'Pamphlet2020.pdf') {
        shell.openExternal(this.output.attachmentlinks.pamp)
      } else {
        shell.openExternal(this.output.attachmentlinks.LoI)
      }
    },
    handleattachUpload () {
      this.upfile1 = this.$refs.upfile1.files[0]
      this.$store.commit('awsupfile1', this.upfile1)
    },
    selectedstate (state, index) {
      console.log(state, index)
      this.state = state
      this.$store.commit('awsstate', this.state)
      this.index = index
      this.$store.commit('awsindex', this.index)
      this.districts = []
      this.districts.push(this.statedisdata.states[index].districts)
      this.$store.commit('awsdistricts', this.districts)
    },
    disc (p, inn) {
      console.log(p, inn)
      this.$delete(this.output.bcc, inn)
      this.$store.commit('awsoutput', this.output)
    },
    disc1 (value, key) {
      console.log(value, key)
      this.$delete(this.output.attachments, key)
      console.log(Object.values(this.output.attachments))
      this.$store.commit('awsoutput', this.output)
    },
    selecteddistrict (diss) {
      this.district.push(diss)
      this.$store.commit('awsdistrict', this.district)
      this.d = diss
      this.$store.commit('awsd', this.d)
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
      this.$store.commit('awsisNight', this.isNight)
      this.isNight1 = false
      this.$store.commit('awsisNight1', this.isNight1)
      this.isNight2 = true
      this.$store.commit('awsisNight2', this.isNight2)
      this.isNight3 = true
      this.$store.commit('awsisNight3', this.isNight3)
      this.result = ''
      this.$store.commit('result', this.result)
      this.axios.post('http://localhost:8081/api/main/awssubmit', {
        selectedworkshop: this.selectedworkshop,
        filldate: this.filldate,
        enddate: this.enddate,
        state: this.state,
        district: this.district
      })
        .then(output => {
          this.output = output.data
          this.$store.commit('awsoutput', this.output)
        })
        .catch(function (error) {
          currentObj.output = error
        })
    },
    approve (e) {
      const formData = new FormData()
      formData.append('file1', this.upfile1)
      // formData.append('file2', this.$refs.upfile1.files[1])
      formData.append('files2send1', Object.values(this.output.attachments))
      formData.append('bcc', this.output.bcc)
      formData.append('body', this.output.body)
      formData.append('subject', this.output.subject)
      const currentObj = this
      e.preventDefault()
      this.axios.post('http://localhost:8081/api/main/approve', formData,
        {
          headers: {
            'Content-Type': 'multipart/form-data'
          }
        })
        .then(function (response) {
          currentObj.output = response.data
          console.log(currentObj.output)
          this.$store.commit('awsoutput', currentObj.output)
        })
        .catch(function (error) {
          currentObj.output = error
          console.log(currentObj.output)
        })
      this.popoverShow1 = false
    },
    gsave (e) {
      const formData = new FormData()
      formData.append('file1', this.upfile1)
      formData.append('files2send1', Object.values(this.output.attachments))
      formData.append('bcc', this.output.bcc)
      formData.append('body', this.output.body)
      formData.append('subject', this.output.subject)
      e.preventDefault()
      const currentObj = this
      this.axios.post('http://localhost:8081/api/main/gsave', formData,
        {
          headers: {
            'Content-Type': 'multipart/form-data'
          }
        })
        .then(function (response) {
          currentObj.output = response.data
          console.log(currentObj.output)
          this.$store.commit('awsoutput', currentObj.output)
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
top: 5%;
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
#wrki{
  position: absolute;
left: 36%;
top: 8.5%;

}
#filldate{
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
#filldatei{
position: absolute;
left: 36%;
top: 15%;
}
#recipientstate{
position: absolute;
width: 154px;
height: 25px;
left: 4%;
top: 20%;

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
top: 20%;
}
#recipientdis{
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
#recipientdisi{
position: absolute;
left: 36%;
top: 27%;
}
#msub{
position: absolute;
right:10%;
top: 53%;
}
#sub3{
position: absolute;
right:40%;
top: 53%;
}
#sub1{
position: absolute;
right:10%;
top: 63%;
}
#sub2{
position: absolute;
right:10%;
top: 73%;
}
#result{
position: absolute;
right:20%;
top: 83%;
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
#upfile1{
  position: absolute;
  top:75%;
  left:30%;
}
#upfile2{
  position: absolute;
  top:80%;
  left:30%;
}

tr ,td,thead,table,th{
  padding:0px;
  padding-left:6px;

}
</style>
<!--
#hcnstatel{
position: absolute;
width: 154px;
height: 25px;
left: 4%;
top: 9%;

font-family: Radley;
font-size: 14px;
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
#hcn{
  position: absolute;
width: 154px;
height: 25px;
left: 4%;
top: 15.5%;

font-family: Radley;
font-size: 14px;
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
font-size: 14px;
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
font-size: 14px;
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
font-size: 14px;
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
font-size: 14px;
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
font-size: 14px;
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
font-size: 14px;
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
-->
