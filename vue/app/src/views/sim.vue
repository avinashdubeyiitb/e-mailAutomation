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
    <strong id="cc">CC:</strong>
    <input id="cci" type="email" v-model="cc"><br>
    <strong id="bcc">BCC:</strong>
    <input id="bcci" type="email" v-model="bcc"><br>
    <strong id="name">Name:</strong>
    <input id="namei" type="text" v-model="name"><br>
    <strong id="desig">Designation:</strong>
    <input id="desigi" type="text" v-model="designation"><br>
    <strong id="depart">Department:</strong>
    <input id="departi" type="text" v-model="department"><br>
    <strong id="cname">College Name:</strong>
    <input id="cnamei" type="text" v-model="cname"><br>
    <div id="recipientstatei">
        <b-dropdown  v-bind:text="state" >
          <div v-for="(p,i) in statedisdata" v-bind:key='i' >
            <div v-for="(sta,index) in p" v-bind:key='index' >
              <b-dropdown-item @click='selectedstate(sta.state,index)' v-model="state">{{sta.state}}</b-dropdown-item>
            </div>
          </div>
        </b-dropdown>
    </div>
    <div id="recipientdisi">
        <b-dropdown  v-bind:text="d" >
          <div v-for="(dis,i) in districts" v-bind:key='i'>
            <div v-for="(diss,i) in dis" v-bind:key='i' >
              <b-dropdown-item  @click='selecteddistrict(diss)'>{{diss}}</b-dropdown-item>
            </div>
            </div>
        </b-dropdown>
        </div>
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
      <p id="csvresult" v-show="csvapp">Result: [Success {{approvecsv.success}} / {{approvecsv.total}}] - [failure {{approvecsv.failure}} / {{approvecsv.total}}]</p>
      <p id="csvresult" v-show="csvgsave">Result: [success{{gsavecsv.success}} / {{gsavecsv.total}}] - [failure{{gsavecsv.failure}} / {{gsavecsv.total}}]</p>
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
   <label id="srcc"><strong>CC:</strong>
   <input v-if = "key2" v-model = "output.cc"
   @blur= "key2 = false; $emit('update')"
   @keyup.enter = "key2=false; $emit('update')" >
         <div v-else>
     <label @click = "key2 = true;">{{output.cc}} </label>
   </div>
    </label><br>
    <label id="srbcc"><strong>Bcc:</strong>
    <input v-if = "key5" v-model = "output.bcc"
    @blur= "key5 = false; $emit('update')"
    @keyup.enter = "key5=false; $emit('update')" >
          <div v-else>
      <label @click = "key5 = true;">{{output.bcc}} </label>
    </div>
     </label><br>
   <label id="srsubject"><strong>subject:</strong>
   <input v-if = "key3" v-model = "output.subject"
   @blur= "key3 = false; $emit('update')"
   @keyup.enter = "key3=false; $emit('update')" id="isrsubject">
         <div v-else>
     <label @click = "key3 = true;"> {{output.subject}}</label>
   </div>
   </label><br>
  <div v-if="output.subdiv !== 'A'">
    {{output.subdiv}}
    <b-dropdown  v-bind:text="detailprop" >
          <div v-for="(dtl,i) in output.tchdtl" v-bind:key='i'>
              <b-dropdown-item @click="chooseDetails(dtl,i)">{{dtl}}</b-dropdown-item>
            </div>
    </b-dropdown>
  <b-button @click="refresh">Refresh</b-button>
  </div>
    <b-button v-b-modal.modal-2 id="srbody">body</b-button>
    <b-modal id="modal-2" size="lg" title="Body" hide-footer v-on:keyup.enter = "NoEnter" >
    <b-container class="px-2" >
    <span v-html="output.body"></span>
    </b-container>
    <b-button @click="$bvModal.hide('modal-2')">OK</b-button>
    </b-modal><br>
  <label id="srattach"><strong>Attachment:</strong>
      <div v-for="(value,key) in output.attachments" v-bind:key="key">
      <b-button size="sm" @click='getfile(value)' >{{value}}</b-button>
       </div>
       <input type="file" id="upfile1" ref="upfile1" v-on:change="handleattachUpload()"/>
       <input type="file" id="upfile2" ref="upfile2" v-on:change="handleattachUpload()"/>
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
      <b-button id="save" @click="saveDetail" v-if="output.subdiv !== 'A'">Store Changes</b-button>
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
     <label id="srccbcc"><strong>Cc:</strong>
     <input v-if = "key2" v-model = "reqdata.cc"
     @blur= "key2 = false; $emit('update')"
     @keyup.enter = "key2=false; $emit('update')" >
           <div v-else>
       <label @click = "key2 = true;">{{reqdata.cc}} </label>
     </div>
     </label><br>
     <label id="srccbcc"><strong>Bcc:</strong>
     <input v-if = "key5" v-model = "reqdata.bcc"
     @blur= "key5 = false; $emit('update')"
     @keyup.enter = "key5=false; $emit('update')" >
           <div v-else>
       <label @click = "key5 = true;">{{reqdata.bcc}} </label>
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
    </div>
    <!-- <input type="file" id="upfile1" ref="upfile1" v-on:change="handleattachUpload"/> -->
    <!-- <input type="file" id="upfile2" ref="upfile2" v-on:change="handleattachUpload"/> -->
   </label><br>
      <b-button id="save" @click="save"> Save </b-button>
 </form>
</div>
</div>
  </div>
</template>
<script>
import statedisdata from '../assets/states-and-districts.json'
const { shell } = require('electron')
export default {
  mounted () {
    console.log('Component mounted.')
  },
  computed: {
  },
  data () {
    return {
      csvapp: false,
      csvgsave: false,
      isNight: true,
      isNight1: true,
      isNight2: true,
      isNight3: true,
      iscsvtrue: false,
      statedisdata: statedisdata,
      state: 'State',
      index: '',
      in: '',
      value: '',
      districts: [],
      d: 'District',
      district: [],
      popoverShow1: false,
      popoverShow2: false,
      popoverShow3: false,
      popoverShow4: false,
      captureid: '',
      remail: '',
      cc: '',
      bcc: '',
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
      upfile: '',
      upfile1: '',
      upfile2: '',
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
      gsavecsv: '',
      aprovselected: [],
      gsvselected: [],
      dscrdselected: [],
      sfile: '',
      detailprop: 'Teacher Details',
      detail: [],
      issaved: false
    }
  },
  watch: {
  },
  methods: {
    getfile (value) {
      console.log(value)
      if (value === 'Pamphlet2020.pdf') {
        shell.openExternal(this.output.attachmentlinks.pamp)
      } else {
        shell.openExternal(this.output.attachmentlinks.LoI)
      }
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
      this.output.cc = ''
      this.output.bcc = ''
      this.output.name = ''
      this.output.designation = ''
      this.output.department = ''
      this.output.cname = ''
      this.output.cno = ''
      this.output.body = ''
      this.output.subject = ''
      this.output.state = ''
      this.output.district = ''
      this.upfile1 = ''
      this.upfile2 = ''
      this.detail = ''
    },
    handleFileUpload () {
      this.file = this.$refs.file.files[0]
    },
    handleattachUpload () {
      this.upfile1 = this.$refs.upfile1.files[0]
      this.upfile2 = this.$refs.upfile2.files[0]
    },
    gobacktoform () {
      this.isNight = true
      this.isNight1 = true
      this.isNight2 = true
      this.isNight3 = true
      this.iscsvtrue = false
    },
    submitFile () {
      const frmData = new FormData()
      // const currentObj = this
      frmData.append('file', this.file)
      this.isNight = false
      this.upfile1 = ''
      this.upfile2 = ''
      this.isNight1 = true
      this.isNight2 = false
      this.isNight3 = false
      this.iscsvtrue = true
      this.axios.post('http://localhost:8081/api/main/csv/submit',
        frmData,
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
      this.csvapp = true
      const formData = new FormData()
      formData.append('file1', this.upfile1)
      formData.append('file2', this.upfile2)
      formData.append('list', this.selected)
      const currentObj = this
      this.axios.post('http://localhost:8081/api/main/csv/approve', formData,
        {
          headers: {
            'Content-Type': 'multipart/form-data'
          }
        })
        .then(function (response) {
          currentObj.approvecsv = response.data
          console.log(currentObj.approvecsv)
        })
        .catch(function (error) {
          currentObj.approvecsv = error
          console.log(error)
        })
      this.popoverShow3 = false
      for (var i = 0; i < this.selected.length; i++) {
        if (this.aprovselected.indexOf(this.selected[i]) === -1) {
          this.aprovselected.push(this.selected[i])
        }
      }
      this.csvgsave = false
      this.selected = []
    },
    selectedstate (state, index) {
      console.log(state, index)
      this.state = state
      this.index = index
      this.districts = []
      this.districts.push(this.statedisdata.states[index].districts)
    },
    selecteddistrict (diss) {
      this.district = diss
      this.d = diss
      console.log(diss)
      console.log(this.district)
    },
    chooseDetails (dtl, i) {
      if (this.detail.indexOf('default') !== -1 && (dtl === 'id' || dtl === 'name' || dtl === 'department')) {
        this.detail.splice(this.detail.indexOf('default'), 1)
      }
      this.detail.push(dtl)
    },
    refresh () {
      this.detail = ['default']
    },
    discardselected () {
      this.popoverShow3 = false
      this.popoverShow4 = false
      this.saveoutput = ''
      if (this.reqdata !== '') {
        this.reqdata.to = ''
        this.reqdata.cc = ''
        this.reqdata.bcc = ''
        this.reqdata.subject = ''
        this.reqdata.body = ''
        this.reqdata.state = ''
        this.reqdata.district = ''
      }
      for (var i = 0; i < this.selected.length; i++) {
        if (this.dscrdselected.indexOf(this.selected[i]) === -1) {
          this.dscrdselected.push(this.selected[i])
        }
      }
      this.selected = []
    },
    gsaveselected () {
      this.csvgsave = true
      const formData = new FormData()
      formData.append('file1', this.upfile1)
      formData.append('file2', this.upfile2)
      formData.append('list', this.selected)
      const currentObj = this
      this.axios.post('http://localhost:8081/api/main/csv/gsave', formData,
        {
          headers: {
            'Content-Type': 'multipart/form-data'
          }
        })
        .then(function (response) {
          currentObj.gsavecsv = response.data
          console.log(currentObj.gsavecsv)
        })
        .catch(function (error) {
          currentObj.gsavecsv = error
          console.log(error)
        })
      this.popoverShow4 = false
      for (var i = 0; i < this.selected.length; i++) {
        if (this.gsvselected.indexOf(this.selected[i]) === -1) {
          this.gsvselected.push(this.selected[i])
        }
      }
      this.csvapp = false
      this.selected = []
    },
    save (e) {
      e.preventDefault()
      const currentObj = this
      this.axios.post('http://localhost:8081/api/main/save', {
        remail: this.reqdata.to,
        cc: this.reqdata.cc,
        bcc: this.reqdata.bcc,
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
    saveDetail (e) {
      e.preventDefault()
      const currentObj = this
      this.axios.post('http://localhost:8081/api/main/store', {
        tchdtl: this.detail,
        remail: this.output.remail,
        cc: this.output.cc,
        bcc: this.output.bcc,
        cname: this.output.cname,
        state: this.output.state,
        district: this.output.district,
        subdiv: this.output.subdiv
      })
        .then(output => {
          this.output = output.data
          console.log(output)
        })
        .catch(function (error) {
          currentObj.output = error
          console.log(error)
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
        cc: this.cc,
        bcc: this.bcc,
        name: this.name,
        designation: this.designation,
        department: this.department,
        cname: this.cname,
        state: this.state,
        district: this.district,
        cno: this.cno
      })
        .then(output => {
          this.output = output.data
        })
        .catch(function (error) {
          currentObj.output = error
        })
    },
    approve () {
      const formData = new FormData()
      formData.append('file1', this.upfile1)
      formData.append('file2', this.upfile2)
      formData.append('remail', this.output.remail)
      formData.append('cc', this.output.cc)
      formData.append('bcc', this.output.bcc)
      formData.append('body', this.output.body)
      formData.append('subject', this.output.subject)
      this.detail = ''
      this.axios.post('http://localhost:8081/api/main/approve', formData,
        {
          headers: {
            'Content-Type': 'multipart/form-data'
          }
        })
        .then(function (response) {
          this.output = response.data
          console.log(this.output)
        })
        .catch(function (error) {
          this.output = error
          console.log(this.output)
        })
      this.popoverShow1 = false
    },
    gsave (e) {
      const formData = new FormData()
      formData.append('file1', this.upfile1)
      formData.append('file2', this.upfile2)
      formData.append('remail', this.output.remail)
      formData.append('cc', this.output.cc)
      formData.append('bcc', this.output.bcc)
      formData.append('body', this.output.body)
      formData.append('subject', this.output.subject)
      e.preventDefault()
      const currentObj = this
      this.detail = ''
      this.axios.post('http://localhost:8081/api/main/gsave', formData,
        {
          headers: {
            'Content-Type': 'multipart/form-data'
          }
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
#cc{
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

#cci{
position: absolute;
left: 36%;
top: 15%;
}
#bcc{
position: absolute;
width: 154px;
height: 25px;
left: 4%;
top: 21%;

font-family: Radley;
font-size: 17px;
line-height: 30px;
display: flex;
align-items: center;
text-align: center;

color: #000000;

}
#bcci{
position: absolute;
left: 36%;
top: 21%;
}
#name{
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
#namei{
position: absolute;
left: 36%;
top: 27%;
}
#desig{
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
#desigi{
position: absolute;
left: 36%;
top: 33.5%;

}
#depart{
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
#departi{
position: absolute;
left: 36%;
top: 39.5%;
}
#cname{
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
#cnamei{
position: absolute;
left: 36%;
top: 45.5%;
}

#cno{
position: absolute;
width: 154px;
height: 25px;
left: 4%;
top: 59%;

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
top: 59%;
}
#msub{
position: absolute;
right:10%;
top: 61%;
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
top:90%;
left:20%;
}
#popover-reactive-2{
position: absolute;
top:90%;
left:40%;
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

#recipientstatei{
position: absolute;
left: 36%;
top: 52%;
}

#recipientdisi{
position: absolute;
left: 66%;
top: 52%;
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

#csvresult{
  position: absolute;
  top:80%;
  left:30%;
}
tr ,td,thead,table,th{
  padding:0px;
  padding-left:6px;

}
</style>
