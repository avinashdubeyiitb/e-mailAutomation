<template>
  <div id="app">
    <h1>Send Information Mail</h1>
    <button id="butt" type="button" name="button"><router-link to="/">Home</router-link></button>
    <button id="goback" v-show="iscsvtrue" type="button" name="button" @click="gobacktoform">!form</button>
  <div id="col1inner" >
    <div v-show="isNight3" >
    <strong><p id="fd">Fill details:</p></strong>
    <form @submit="formSubmit">
    <strong id="rid" >Recipient Email ID:</strong>
    <input id="ridi" type="email" v-model="remail"><br>
    <strong id="ccbcc">CC/BCC:</strong>
    <input id="ccbcci" type="email" v-model="ccbcc"><br>
    <strong id="name">Name:</strong>
    <input id="namei" type="text" v-model="name"><br>
    <strong id="desig">Designation:</strong>
    <input id="desigi" type="text" v-model="designation"><br>
    <strong id="depart">Department:</strong>
    <input id="departi" type="text" v-model="department"><br>
    <strong id="cname">College Name:</strong>
    <input id="cnamei" type="text" v-model="cname"><br>
    <strong id="cno">Contact No.:</strong>
    <input id="cnoi" type="tel" v-model="cno"><br>
    <button id="msub">Submit</button>
    </form>
    <!-- <strong>Response:</strong> -->
    <!-- <pre>
    </pre> -->
    <!-- <p id="rmsg">{{output}}</p> -->
    <!-- <div  v-if="{{output.key}} === 'success'"> -->
    <p id="or">-----------------------or------------------------</p>
    <p id="up">Upload csv file</p>
    <label id="file">File:
    <input type="file" accept=".xlsx,.csv" id="file" ref="file" v-on:change="handleFileUpload()"/>
  </label>
    <button id="csub" v-on:click="submitFile()">Submit</button>
  </div>
  <div v-show="!isNight2">
    <p v-show="!isNight2">"comming soon"</p>
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
<th>Receipient Id</th>
</tr>
</thead>
<tbody>
<tr v-bind:key="i" v-for="(pk,i) in items" :class="getClass(pk)">
<td>
<label class="form-checkbox">
<input type="checkbox" :value="pk" v-model="selected">
</label>
</td>
<td v-on:click="clickList(pk,i)">{{i}}</td>
<td>{{pk}}</td>
</tr>
</tbody>
</table>
  </div>
  <form>
    <!--<p id="rmsg">{{approvecsv}}</p>-->
  <b-button id="popover-reactive-3" ref="button3">Approve Selected</b-button>
</form>
  <b-popover
        target="popover-reactive-3"
        triggers="click"
        :show.sync="popoverShow3"
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
          <b-button id="bsure" @click="approveselect" size="sm" variant="primary">Sure</b-button>
        </div>
      </b-popover>
    <form>
  <b-button id="popover-reactive-4" ref="button4" >Reject Selected</b-button>
</form>
  <b-popover
        target="popover-reactive-4"
        triggers="click"
        :show.sync="popoverShow4"
        placement="auto"
        container="my-container"
        ref="popover"
        @hidden="onHidden"
      >
        <template v-slot:title>
          Are you want to save it in gmail draft or discard it ?
        </template>
        <div>
          <b-button id="bstd" @click="gsaveselected" size="sm" variant="primary">Save to draft</b-button>
          <b-button id="bdiscard" @click="discardselected" size="sm" variant="danger">Discard</b-button>
        </div>
      </b-popover>
  </div>
</div>
<div id="col2inner">
  <p id="para1" v-show="isNight">" nothing to show right now" </p>
  <img id="img1" v-show="isNight" alt="no-thumbnail" src="../assets/no-thumbnail.jpg">
<p id="para1" v-show="!isNight1">"show right now"</p>
<div v-show="!isNight1">
   <form>
   <label  id="sremail"><strong >Recipient Id:</strong>
   <input v-if = "key1" v-model = "output.remail"
   @blur= "key1 = false; $emit('update')"
   @keyup.enter = "key1=false; $emit('update')">
   <div v-else>
     <label @click = "key1 = true;"> {{output.remail}} </label>
   </div>
 </label><br>
   <label id="srccbcc"><strong>cc/bcc:</strong>
   <input v-if = "key2" v-model = "output.ccbcc"
   @blur= "key2 = false; $emit('update')"
   @keyup.enter = "key2=false; $emit('update')" >
         <div v-else>
     <label @click = "key2 = true;">{{output.ccbcc}} </label>
   </div>
    </label><br>
   <label id="srsubject"><strong>subject:</strong>
   <input v-if = "key3" v-model = "output.subject"
   @blur= "key3 = false; $emit('update')"
   @keyup.enter = "key3=false; $emit('update')" id="isrsubject">
         <div v-else>
     <label @click = "key3 = true;"> {{output.subject}} </label>
   </div>
   </label><br>
  <!--
   <label id="srbody"><strong>body:</strong>
   <input v-if = "key4" v-model = "output.body"
   @blur= "key4 = false; $emit('update')"
   @keyup.enter = "key4=false; $emit('update')" id="isrbody">
    <div v-else>
     <label @click = "key4 = true;"> {{output.body}} </label>
   </div>
  </label><br>
  -->
      <b-button v-b-modal.modal-2 id="srbody">body</b-button>

    <b-modal id="modal-2" size="lg" title="Body" hide-footer v-on:keyup.enter = "NoEnter" >
    <b-container class="px-2" >
    <span v-html="output.body"></span>
    </b-container>
    <b-button @click="$bvModal.hide('modal-2')">OK</b-button>
    </b-modal><br>

  <label id="srattach"><strong>Attachment:</strong>
      <div v-for="(value,key) in output.attachments" v-bind:key="key">
      <b-button v-b-modal.modal-3 size="sm" @click='getfile(value)'>{{value}}</b-button>
    <b-modal  id="modal-3" size="lg" hide-footer >
    <b-container class="px-2" >
    {{sfile}}
    </b-container>
    </b-modal><br>
       </div>
 </label><br>
    <!-- <h2>Extra details:</h2>
   <p>name:</p>
   <input v-if = "key5" v-model = "output.name"
   @blur= "key5 = false; $emit('update')"
   @keyup.enter = "key5=false; $emit('update')">
         <div v-else>
     <label @click = "key5 = true;">{{output.name}} </label>
   </div>
   <p>Designation:</p>
   <input v-if = "key6" v-model = "output.designation"
   @blur= "key6 = false; $emit('update')"
   @keyup.enter = "key6=false; $emit('update')">
         <div v-else>
     <label @click = "key6 = true;">{{output.designation}} </label>
   </div>
 <p>Department:</p>
 <input v-if = "key7" v-model = "output.department"
 @blur= "key7 = false; $emit('update')"
 @keyup.enter = "key7=false; $emit('update')">
       <div v-else>
   <label @click = "key7 = true;">{{output.department}} </label>
 </div>
 <p>College name:</p>
 <input v-if = "key8" v-model = "output.cname"
 @blur= "key8 = false; $emit('update')"
 @keyup.enter = "key8=false; $emit('update')">
       <div v-else>
   <label @click = "key8 = true;">{{output.cname}} </label>
 </div>
 <p>Contact number:</p>
 <input v-if = "key9" v-model = "output.cno"
 @blur= "key9 = false; $emit('update')"
 @keyup.enter = "key9=false; $emit('update')">
<div v-else>
   <label @click = "key9 = true;">{{output.cno}} </label>
 </div> -->
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
     </label><br><!--
     <label id="srbody"><strong>body:</strong>
     <input v-if = "key4" v-model = "reqdata.body"
     @blur= "key4 = false; $emit('update')"
     @keyup.enter = "key4=false; $emit('update')" id="isrbody">
      <div v-else>
       <label @click = "key4 = true;"> {{reqdata.body}} </label>
     </div>
    </label><br>-->
    <b-button v-b-modal.modal-1 id="srbody">body</b-button>
    <b-modal id="modal-1" size="lg" title="Body" hide-footer v-on:keyup.enter = "NoEnter" >
    <b-container class="px-2" >
    <span v-html="reqdata.body"></span>
    </b-container>
    <b-button block @click="$bvModal.hide('modal-1')">OK</b-button>
    </b-modal><br>

    <label id="srattach"><strong>Attachment:</strong>
      <div v-for="(value,key) in reqdata.attachments" v-bind:key="key">
      <b-button v-b-modal.modal-4 size="sm" @click='getfile(value)'>{{value}}</b-button>
    <b-modal  id="modal-4" size="lg" hide-footer >
    <b-container class="px-2" >
    {{sfile}}
    </b-container>
    </b-modal><br>
    </div>
   </label><br>
      <b-button id="save" @click="save"> Save </b-button>
 </form>
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
      isNight: true,
      isNight1: true,
      isNight2: true,
      isNight3: true,
      iscsvtrue: false,
      popoverShow1: false,
      popoverShow2: false,
      popoverShow3: false,
      popoverShow4: false,
      captureid: '',
      remail: '',
      ccbcc: '',
      name: '',
      designation: '',
      department: '',
      cname: '',
      cno: '',
      output: '',
      items: [],
      selected: [],
      selectAll: false,
      file: '',
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
      editedTodo: null,
      saveoutput: '',
      approvecsv: '',
      aprovselected: [],
      gsvselected: [],
      dscrdselected: [],
      sfile: ''
    }
  },
  watch: {
  },
  methods: {
    func (href) {
      const { shell } = require('electron')
      shell.openExternal(href)
    },
    getfile (value) {
      console.log(value)
      this.axios.post('http://localhost:8081/api/main/getfile', {
        value: this.value
      })
        .then(sfile => {
          this.sfile = sfile.data
        })
        .catch(function (error) {
          this.sfile = error
        })
    },
    getClass (pk) {
      if (this.aprovselected.indexOf(pk) !== -1) {
        return 'first'
      }
      if (this.gsvselected.indexOf(pk) !== -1) {
        return 'second'
      }
      if (this.dscrdselected.indexOf(pk) !== -1) {
        return 'third'
      }
    },
    select () {
      this.selected = []
      if (!this.selectAll) {
        for (const pk in this.items) {
          this.selected.push(this.items[pk])
        }
      }
    },
    NoEnter (e) {
      e.preventDefault()
      console.log(e)
    },
    editTodo: output => {
      this.editedTodo = output
    },
    discard () {
      this.popoverShow1 = false
      this.popoverShow2 = false
      this.isNight = true
      this.isNight1 = true
      this.isNight2 = true
      this.iscsvtrue = false
      this.output.remail = ''
      this.output.ccbcc = ''
      this.output.name = ''
      this.output.designation = ''
      this.output.department = ''
      this.output.cname = ''
      this.output.cno = ''
      this.output.body = ''
      this.output.subject = ''
    },
    handleFileUpload () {
      this.file = this.$refs.file.files[0]
    },
    gobacktoform () {
      this.isNight = true
      this.isNight1 = true
      this.isNight2 = true
      this.isNight3 = true
      this.iscsvtrue = false
    },
    submitFile () {
      const formData = new FormData()
      // const currentObj = this
      formData.append('file', this.file)
      this.isNight = false
      this.isNight1 = true
      this.isNight2 = false
      this.isNight3 = false
      this.iscsvtrue = true
      this.axios.post('http://localhost:8081/api/main/csv/submit',
        formData,
        {
          headers: {
            'Content-Type': 'multipart/form-data'
          }
        }
      )
        .then(items => {
          console.log('SUCCESS!!')
          this.items = items.data
          console.log(this.items)
        })
        .catch(function () {
          console.log('FAILURE!!')
        })
    },
    onClose () {
      this.popoverShow1 = false
      this.popoverShow2 = false
      this.popoverShow3 = false
      this.popoverShow4 = false
    },
    onHidden () {
      // Called just after the popover has finished hiding
      // Bring focus back to the button
      this.focusRef(this.$refs.button)
    },
    focusRef (ref) {
    },
    approveselect () {
      const currentObj = this
      this.axios.post('http://localhost:8081/api/main/csv/approve', {
        list: this.selected
      })
        .then(function (response) {
          currentObj.approvecsv = response.data
        })
        .catch(function (error) {
          currentObj.approvecsv = error
        })
      this.popoverShow3 = false
      for (var i = 0; i < this.selected.length; i++) {
        if (this.aprovselected.indexOf(this.selected[i]) === -1) {
          this.aprovselected.push(this.selected[i])
        }
      }
    },
    discardselected () {
      this.popoverShow3 = false
      this.popoverShow4 = false
      this.approvecsv = ''
      this.saveoutput = ''
      if (this.reqdata !== '') {
        this.reqdata.to = ''
        this.reqdata.ccbcc = ''
        this.reqdata.subject = ''
        this.reqdata.body = ''
      }
      for (var i = 0; i < this.selected.length; i++) {
        if (this.dscrdselected.indexOf(this.selected[i]) === -1) {
          this.dscrdselected.push(this.selected[i])
        }
      }
    },
    gsaveselected () {
      const currentObj = this
      this.axios.post('http://localhost:8081/api/main/csv/gsave', {
        list: this.selected
      })
        .then(function (response) {
          currentObj.approvecsv = response.data
        })
        .catch(function (error) {
          currentObj.approvecsv = error
        })
      this.popoverShow4 = false
      for (var i = 0; i < this.selected.length; i++) {
        if (this.gsvselected.indexOf(this.selected[i]) === -1) {
          this.gsvselected.push(this.selected[i])
        }
      }
    },
    save (e) {
      e.preventDefault()
      const currentObj = this
      this.axios.post('http://localhost:8081/api/main/save', {
        remail: this.reqdata.to,
        ccbcc: this.reqdata.ccbcc,
        body: this.reqdata.body,
        subject: this.reqdata.subject
      })
        .then(function (response) {
          currentObj.saveoutput = response.data
        })
        .catch(function (error) {
          currentObj.saveoutput = error
        })
    },
    clickList: function (pk, i) {
      console.log('clickList fired with ' + pk)
      const currentObj = this
      this.axios.post('http://localhost:8081/api/main/idrequest', {
        remail: pk,
        cname: i
      })
        .then(reqdata => {
          this.reqdata = reqdata.data
        })
        .catch(function (error) {
          currentObj.reqdata = error
        })
    },
    formSubmit (e) {
      e.preventDefault()
      const currentObj = this
      this.isNight = false
      this.isNight1 = false
      this.isNight2 = true
      this.isNight3 = true
      this.axios.post('http://localhost:8081/api/main/submit', {
        remail: this.remail,
        ccbcc: this.ccbcc,
        name: this.name,
        designation: this.designation,
        department: this.department,
        cname: this.cname,
        cno: this.cno
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
        remail: this.output.remail,
        ccbcc: this.output.ccbcc,
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
        remail: this.output.remail,
        ccbcc: this.output.ccbcc,
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
.first {
  background-color: lightgreen;
}
.first:hover {
  background-color: green;
}
.second {
  background-color: lightblue;
}
.second:hover {
  background-color: rgb(0, 204, 255);
}
.third {
  background-color: lightcoral;
}
.third:hover {
  background-color: rgba(255, 38, 0, 0.925);
}
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
#rid{
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
#ridi{
  position: absolute;
left: 36%;
top: 8.5%;

}
#ccbcc{
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
#ccbcci{
position: absolute;
left: 36%;
top: 15%;
}
#name{
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
#namei{
position: absolute;
left: 36%;
top: 21%;
}
#desig{
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
#desigi{
position: absolute;
left: 36%;
top: 27%;

}
#depart{
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
#departi{
position: absolute;
left: 36%;
top: 33%;
}
#cname{
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
#cnamei{
position: absolute;
left: 36%;
top: 39%;
}
#cno{
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
#cnoi{
position: absolute;
left: 36%;
top: 45%;
}
#msub{
position: absolute;
right:10%;
top: 53%;
}
#rmsg{
  position: absolute;
  left:35%;
  top: 55%;
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
