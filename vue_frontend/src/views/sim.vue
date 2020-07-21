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
    <router-view/>
    <h1>Send Information Mail</h1>
    <button id="goback" v-show="iscsvtrue" type="button" name="button" @click="gobacktoform">!form</button>
  <div id="col1inner" >
    <div v-show="isNight3" >
    <strong><p id="fd">Fill details:</p></strong>
    <button id="refresh" @click="clear">Clear</button>
    <form @submit="formSubmit">
    <strong id="rid" >Recipient Email ID:</strong>
    <input id="ridi" type="email" v-model="remail" @change="$store.commit('remail', remail)" multiple><br>
    <strong id="cc">CC:</strong>
    <input id="cci" type="email" v-model="cc" @change="$store.commit('cc', cc)" multiple><br>
    <strong id="bcc">BCC:</strong>
    <input id="bcci" type="email" v-model="bcc" @change="$store.commit('bcc', bcc)" multiple><br>
    <strong id="name">Name:*</strong>
    <input id="namei" type="text" v-model="name" @change="$store.commit('name', name)" required><br>
    <strong id="desig">Designation:*</strong>
    <input id="desigi" type="text" v-model="designation" @change="$store.commit('designation', designation)" required><br>
    <strong id="depart">Department:*</strong>
    <input id="departi" type="text" v-model="department" @change="$store.commit('department', department)" required><br>
    <strong id="cname">College Name:</strong>
    <input id="cnamei" type="text" v-model="cname" @change="$store.commit('cname', cname)"><br>
    <div id="recipientstatei">
        <b-dropdown  v-bind:text="state" class="dropsize">
          <div v-for="(p,i) in statedisdata" v-bind:key='i' >
            <div v-for="(sta,index) in p" v-bind:key='index' >
              <b-dropdown-item @click='selectedstate(sta.state,index)' v-model="state">{{sta.state}}</b-dropdown-item>
            </div>
          </div>
        </b-dropdown>
    </div>
    <div id="recipientdisi">
        <b-dropdown  v-bind:text="d" class="dropsize">
          <div v-for="(dis,i) in districts" v-bind:key='i'>
            <div v-for="(diss,i) in dis" v-bind:key='i' >
              <b-dropdown-item  @click='selecteddistrict(diss)'>{{diss}}</b-dropdown-item>
            </div>
            </div>
        </b-dropdown>
        </div>
    <strong id="cno">Contact No.:</strong>
    <input id="cnoi" type="tel" v-model="cno" @change="$store.commit('cno', cno)" @input="acceptNumber"><br>
    <button id="msub" v-on:click="loader = true">Submit</button>
    </form>
    <p id="or">-----------------------or------------------------</p>
    <p id="up">Upload csv file</p>
    <label id="file">File:
    <input type="file" accept=".xlsx,.csv" id="file" ref="file" v-on:change="handleFileUpload()"/>
  </label>
    <button id="csub" v-on:click="loader = true;submitFile()">Submit</button>
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
<input type="checkbox" :value="pk" v-model="selected" @change="$store.commit('selected', selected)">
</label>
</td>
<td v-on:click="clickList(pk,i)">{{i}}</td>
<td>{{pk}}</td>
</tr>
</tbody>
</table>
  </div>
  <form>
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
          <b-button id="bsure" @click="sender = true;approveselect()" size="sm" variant="primary">Sure</b-button>
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
          <b-button id="bstd" @click="sender = true;gsaveselected()" size="sm" variant="primary">Save to draft</b-button>
          <b-button id="bdiscard" @click="discardselected" size="sm" variant="danger">Discard</b-button>
        </div>
      </b-popover>
      <p id="csvresult" v-show="csvapp">Result: [Success {{approvecsv.success}} / {{approvecsv.total}}] - [failure {{approvecsv.failure}} / {{approvecsv.total}}]</p>
      <p id="csvresult" v-show="csvgsave">Result: [success{{gsavecsv.success}} / {{gsavecsv.total}}] - [failure{{gsavecsv.failure}} / {{gsavecsv.total}}]</p>
  </div>
</div>
<div id="col2inner">
  <img id="img1" v-show="isNight" alt="no-thumbnail" src="../assets/no-thumbnail.jpg">
<p id="para1" v-show="!isNight1"></p>
<div v-show="!isNight1">
   <form>
   <label  id="sremail"><strong >Recipient Id:</strong>
   <input v-if = "key1" v-model = "output.remail"
   @blur= "key1 = false; $emit('update')"
   @keyup.enter = "key1=false; $emit('update')"
   @change="$store.commit('output', output)">
   <div v-else>
     <label @click = "key1 = true;"> {{output.remail}} </label>
   </div>
 </label><br>
   <label id="srcc"><strong>CC:</strong>
   <input v-if = "key2" v-model = "output.cc"
   @blur= "key2 = false; $emit('update')"
   @keyup.enter = "key2=false; $emit('update')"
   @change="$store.commit('output', output)" >
         <div v-else>
     <label @click = "key2 = true;">{{output.cc}} </label>
   </div>
    </label><br>
    <label id="srbcc"><strong>Bcc:</strong>
    <input v-if = "key5" v-model = "output.bcc"
    @blur= "key5 = false; $emit('update')"
    @keyup.enter = "key5=false; $emit('update')"
    @change="$store.commit('output', output)">
          <div v-else>
      <label @click = "key5 = true;">{{output.bcc}} </label>
    </div>
     </label><br>
   <label id="srsubject"><strong>subject:</strong>
   <input v-if = "key3" v-model = "output.subject"
   @blur= "key3 = false; $emit('update')"
   @keyup.enter = "key3=false; $emit('update')" id="isrsubject"
   @change="$store.commit('output', output)">
         <div v-else>
     <label @click = "key3 = true;"> {{output.subject}}</label>
   </div>
   </label><br>
  <div v-if="output.subdiv !== 'A'">
    {{output.subdiv}}
    <b-dropdown  v-bind:text="detailprop" class="dropsize">
          <div v-for="(dtl,i) in output.tchdtl" v-bind:key='i'>
              <b-dropdown-item @click="chooseDetails(dtl,i)">{{dtl}}</b-dropdown-item>
            </div>
    </b-dropdown>
  <b-button @click="refresh">Refresh</b-button>
  </div>
    <b-button v-b-modal.modal-2 id="srbody">body</b-button>
    <b-modal id="modal-2" size="lg" title="Body" hide-footer >
    <b-container class="px-2" id="container1">
    <span v-html="output.body"></span>
    </b-container>
    <b-button @click="onDivInput1($event);$bvModal.hide('modal-2')">OK</b-button>
    </b-modal><br>
  <label id="srattach"><strong>Attachment:</strong>
      <div v-for="(value,key) in output.attachments" v-bind:key="key">
      <b-button >
      <b-button size="sm" @click='getfile(value)' >{{value}}</b-button>
      <b-button @click="disc1(value,key)" class="close" aria-label="Close"><span class="d-inline-block" aria-hidden="true">&times;</span></b-button></b-button>
       </div>

       <input type="file" id="upfile1" ref="upfile1" v-on:change="handleattachUpload1()" multiple>
        {{upfile1.name}}
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
          <b-button id="bsure" @click="sender = true;approve($event)" size="sm" variant="primary">Sure</b-button>
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
          <b-button id="bstd" @click="sender = true;gsave($event)" size="sm" variant="primary">Save to draft</b-button>
          <b-button id="bdiscard" @click="discard" size="sm" variant="danger">Discard</b-button>
        </div>
      </b-popover>
      <b-button id="save" @click="loader = true;saveDetail($event)" v-if="output.subdiv !== 'A'">Store Changes</b-button>
</div>
<div v-show="!isNight2">
     <form>
     <label  id="sremail"><strong >Recipient Id:</strong>
     <input v-if = "key1" v-model = "reqdata.to"
     @blur= "key1 = false; $emit('update')"
     @keyup.enter = "key1=false; $emit('update')"
     @change="$store.commit('reqdata', reqdata)">
     <div v-else>
       <label @click = "key1 = true;"> {{reqdata.to}} </label>
     </div>
   </label><br>
     <label id="srccbcc"><strong>Cc:</strong>
     <input v-if = "key2" v-model = "reqdata.cc"
     @blur= "key2 = false; $emit('update')"
     @keyup.enter = "key2=false; $emit('update')"
     @change="$store.commit('reqdata', reqdata)">
           <div v-else>
       <label @click = "key2 = true;">{{reqdata.cc}} </label>
     </div>
     </label><br>
     <label id="srccbcc"><strong>Bcc:</strong>
     <input v-if = "key5" v-model = "reqdata.bcc"
     @blur= "key5 = false; $emit('update')"
     @keyup.enter = "key5=false; $emit('update')"
     @change="$store.commit('reqdata', reqdata)">
           <div v-else>
       <label @click = "key5 = true;">{{reqdata.bcc}} </label>
     </div>
      </label><br>
     <label id="srsubject"><strong>subject:</strong>
     <input v-if = "key3" v-model = "reqdata.subject"
     @blur= "key3 = false; $emit('update')"
     @keyup.enter = "key3=false; $emit('update')" id="isrsubject"
     @change="$store.commit('reqdata', reqdata)">
           <div v-else>
       <label @click = "key3 = true;"> {{reqdata.subject}} </label>
     </div>
     </label><br>
    <b-button v-b-modal.modal-1 id="srbody">body</b-button>
    <b-modal id="modal-1" size="lg" title="Body" hide-footer>
    <b-container class="px-2" id="container2">
    <span v-html="reqdata.body"></span>
    </b-container>
    <b-button block @click="onDivInput2($event);$bvModal.hide('modal-1')">OK</b-button>
    </b-modal><br>

    <label id="srattach"><strong>Attachment:</strong>
      <div v-for="(value,key) in reqdata.attachments" v-bind:key="key">
      <b-button>
      <b-button size="sm" @click='getfile(value)'>{{value}}</b-button>
      <b-button @click="disc2(value,key)" class="close" aria-label="Close"><span class="d-inline-block" aria-hidden="true">&times;</span></b-button>
      </b-button>
    </div>

    <input type="file" id="upfile2" ref="upfile2" v-on:change="handleattachUpload2()" multiple>

   </label><br>
 </form>
</div>
</div>
<div id="loader" v-show="loader">
<b-button variant="danger" disabled>
  <b-spinner small ></b-spinner>
  Loading...
</b-button>
</div>
<div id="loader" v-show="sender">
<b-button variant="danger" disabled>
  <b-spinner small ></b-spinner>
  Sending...
</b-button>
</div>
  </div>
</template>
<script>
const { shell } = require('electron')
export default {
  mounted () {
    console.log('Component mounted.')
  },
  computed: {
  },
  data () {
    return {
      loader: false,
      sender: false,
      url: this.$store.getters.url,
      csvapp: this.$store.getters.csvapp,
      csvgsave: this.$store.getters.csvgsave,
      isNight: this.$store.getters.simisNight,
      isNight1: this.$store.getters.simisNight1,
      isNight2: this.$store.getters.simisNight2,
      isNight3: this.$store.getters.simisNight3,
      iscsvtrue: this.$store.getters.iscsvtrue,
      statedisdata: this.$store.getters.statedisdata,
      state: this.$store.getters.state,
      index: this.$store.getters.index,
      in: this.$store.getters.in,
      value: this.$store.getters.value,
      districts: this.$store.getters.districts,
      d: this.$store.getters.d,
      district: this.$store.getters.district,
      popoverShow1: false,
      popoverShow2: false,
      popoverShow3: false,
      popoverShow4: false,
      remail: this.$store.getters.remail,
      cc: this.$store.getters.cc,
      bcc: this.$store.getters.bcc,
      name: this.$store.getters.name,
      designation: this.$store.getters.designation,
      department: this.$store.getters.department,
      cname: this.$store.getters.cname,
      cno: this.$store.getters.cno,
      scno: '',
      output: this.$store.getters.output,
      items: this.$store.getters.items,
      selected: this.$store.getters.selected,
      selectAll: this.$store.getters.selectAll,
      file: this.$store.getters.file,
      upfile1: this.$store.getters.upfile1,
      upfile2: this.$store.getters.upfile2,
      mulupfile1: this.$store.getters.mulupfile1,
      mulupfile2: this.$store.getters.mulupfile2,
      key1: '',
      key2: '',
      key3: '',
      key5: '',
      reqdata: this.$store.getters.reqdata,
      approvecsv: this.$store.getters.approvecsv,
      gsavecsv: this.$store.getters.gsavecsv,
      aprovselected: this.$store.getters.aprovselected,
      gsvselected: this.$store.getters.gsvselected,
      dscrdselected: this.$store.getters.dscrdselected,
      detailprop: 'Teacher Details',
      detail: this.$store.getters.detail
    }
  },
  watch: {
  },
  methods: {
    /*
      Function name: getfile()
      Input: value
      Logic: opens the file(value) in an external window
    */
    clear () {
      this.popoverShow1 = false
      this.popoverShow2 = false
      this.isNight = true
      this.$store.commit('simisNight', this.isNight)
      this.isNight1 = true
      this.$store.commit('simisNight1', this.isNight1)
      this.isNight2 = true
      this.$store.commit('simisNight2', this.isNight2)
      this.iscsvtrue = false
      this.$store.commit('iscsvtrue', this.iscsvtrue)
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
      this.$store.commit('output', this.output)
      this.upfile1 = ''
      this.$store.commit('upfile1', this.upfile1)
      this.upfile2 = ''
      this.$store.commit('upfile2', this.upfile2)
      this.detail = ''
      this.$store.commit('detail', this.detail)
      this.remail = ''
      this.$store.commit('remail', this.remail)
      this.cc = ''
      this.$store.commit('cc', this.cc)
      this.bcc = ''
      this.$store.commit('bcc', this.bcc)
      this.name = ''
      this.$store.commit('name', this.name)
      this.designation = ''
      this.$store.commit('designation', this.designation)
      this.department = ''
      this.$store.commit('department', this.department)
      this.cname = ''
      this.$store.commit('cname', this.cname)
      this.state = 'State'
      this.$store.commit('state', this.state)
      this.d = 'District'
      this.$store.commit('d', this.d)
    },
    onDivInput1 (e) {
      this.output.body = document.getElementById('container1').innerHTML
    },
    onDivInput2 (e) {
      this.reqdata.body = document.getElementById('container2').innerHTML
    },
    getfile (value) {
      console.log(value)
      if (value === 'Pamphlet2020.pdf') {
        shell.openExternal(this.output.attachmentlinks.pamp)
      } else {
        shell.openExternal(this.output.attachmentlinks.LoI)
      }
    },
    /*
      Function name: getClass()
      Input: pk
      Output: class to implement(first for approved & second for drafted & third for discarded)
      Logic: sets the background color of the row(addressed on the basis of pk) accordingly whether it has been
             approved or drafted or discarded
    */
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
    /*
      Function name: select()
      Logic: This function is called when all the csv data is selected and thus pushes all the mail ids to
             selected variable
    */
    select () {
      this.selected = []
      if (!this.selectAll) {
        for (const pk in this.items) {
          this.selected.push(this.items[pk])
        }
      }
      this.$store.commit('selected', this.selected)
    },
    /*
      Function name: discard()
      Logic: discards the mail that was to be sent and therefore resets the variables
    */
    discard () {
      this.popoverShow1 = false
      this.popoverShow2 = false
      this.isNight = true
      this.$store.commit('simisNight', this.isNight)
      this.isNight1 = true
      this.$store.commit('simisNight1', this.isNight1)
      this.isNight2 = true
      this.$store.commit('simisNight2', this.isNight2)
      this.iscsvtrue = false
      this.$store.commit('iscsvtrue', this.iscsvtrue)
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
      this.$store.commit('output', this.output)
      this.upfile1 = ''
      this.$store.commit('upfile1', this.upfile1)
      this.upfile2 = ''
      this.$store.commit('upfile2', this.upfile2)
      this.detail = ''
      this.$store.commit('detail', this.detail)
    },
    /*
      Function name: handleFileUpload()
      Logic: stores the .csv or .xlsx file uploaded which will be needed for further operations to be performed
    */
    handleFileUpload () {
      this.file = this.$refs.file.files[0]
      this.$store.commit('file', this.file)
    },
    /*
      Function name: handleFileUpload1()
      Logic: stores the multiple file uploads while sending the mail to college individually
    */
    handleattachUpload1 () {
      for (var i = 0; i < this.$refs.upfile1.files.length; i++) {
        this.mulupfile1.push(this.$refs.upfile1.files[i])
      }
      this.$store.commit('upfile1', this.upfile1)
      this.$store.commit('mulupfile1', this.mulupfile1)
    },
    /*
      Function name: handleFileUpload2()
      Logic: stores the multiple file uploads while data to send the mail to college was uploaded thorough .csv or
             .xlsx file
    */
    handleattachUpload2 () {
      for (var i = 0; i < this.$refs.upfile2.files.length; i++) {
        this.mulupfile2.push(this.$refs.upfile2.files[i])
      }
      this.$store.commit('upfile2', this.upfile2)
      this.$store.commit('mulupfile2', this.mulupfile2)
    },
    /*
      Function name: gobacktoform()
      Logic: This function is called when user wants to switch to sending information mail to college individually
    */
    gobacktoform () {
      this.isNight = true
      this.$store.commit('simisNight', this.isNight)
      this.isNight1 = true
      this.$store.commit('simisNight1', this.isNight1)
      this.isNight2 = true
      this.$store.commit('simisNight2', this.isNight2)
      this.isNight3 = true
      this.$store.commit('simisNight3', this.isNight3)
      this.iscsvtrue = false
      this.$store.commit('iscsvtrue', this.iscsvtrue)
    },
    /*
      Function name: submitFile()
      Logic:
    */
    submitFile () {
      const frmData = new FormData()
      frmData.append('file', this.file)
      this.isNight = false
      this.$store.commit('simisNight', this.isNight)
      this.upfile1 = ''
      this.$store.commit('upfile1', this.upfile1)
      this.upfile2 = ''
      this.$store.commit('upfile2', this.upfile2)
      this.isNight1 = true
      this.$store.commit('simisNight1', this.isNight1)
      this.isNight2 = false
      this.$store.commit('simisNight2', this.isNight2)
      this.isNight3 = false
      this.$store.commit('simisNight3', this.isNight3)
      this.iscsvtrue = true
      this.$store.commit('iscsvtrue', this.iscsvtrue)
      this.axios.post(this.url + '/api/main/csv/submit',
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
          this.$store.commit('items', this.items)
          console.log(this.items)
          this.loader = false
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
      this.$store.commit('csvapp', this.csvapp)
      const formData = new FormData()
      for (var i = 0; i < this.mulupfile2.length; i++) {
        formData.append('file2[' + i + ']', this.mulupfile2[i])
      }
      if (this.reqdata !== '') {
        formData.append('file2send2', Object.values(this.reqdata.attachments))
      } else {
        formData.append('file2send2', Object.values({ pamp: 'Pamphlet2020.pdf', LoI: 'letter-of-intent.docx' }))
      }
      formData.append('list', this.selected)
      formData.append('label', 'information-mail')
      formData.append('user', this.$store.getters.user_name)
      const currentObj = this
      this.axios.post(this.url + '/api/main/csv/approve', formData,
        {
          headers: {
            'Content-Type': 'multipart/form-data'
          }
        })
        .then(function (response) {
          currentObj.approvecsv = response.data
          console.log(currentObj.approvecsv)
          currentObj.$store.commit('approvecsv', currentObj.approvecsv)
          currentObj.reqdata = ''
          currentObj.$store.commit('reqdata', currentObj.reqdata)
          currentObj.popoverShow3 = false
          for (i = 0; i < currentObj.selected.length; i++) {
            if (currentObj.aprovselected.indexOf(currentObj.selected[i]) === -1) {
              currentObj.aprovselected.push(currentObj.selected[i])
            }
          }
          currentObj.$store.commit('aprovselected', currentObj.aprovselected)
          currentObj.csvgsave = false
          currentObj.$store.commit('csvgsave', currentObj.csvgsave)
          currentObj.selected = []
          currentObj.$store.commit('selected', currentObj.selected)
          currentObj.sender = false
        })
        .catch(function (error) {
          console.log(error)
        })
    },
    selectedstate (state, index) {
      console.log(state, index)
      this.state = state
      this.$store.commit('state', this.state)
      this.index = index
      this.$store.commit('index', this.index)
      this.districts = []
      this.districts.push(this.statedisdata.states[index].districts)
      this.$store.commit('districts', this.districts)
    },
    selecteddistrict (diss) {
      this.district = diss
      this.$store.commit('district', this.district)
      this.d = diss
      this.$store.commit('d', this.d)
      console.log(diss)
      console.log(this.district)
    },
    chooseDetails (dtl, i) {
      if (this.detail.indexOf('default') !== -1 && (dtl === 'id' || dtl === 'name' || dtl === 'department')) {
        this.detail.splice(this.detail.indexOf('default'), 1)
      }
      this.detail.push(dtl)
      this.$store.commit('detail', this.detail)
    },
    refresh () {
      this.detail = ['default']
      this.$store.commit('detail', this.detail)
    },
    discardselected () {
      this.popoverShow3 = false
      this.popoverShow4 = false
      if (this.reqdata !== '') {
        this.reqdata.to = ''
        this.reqdata.cc = ''
        this.reqdata.bcc = ''
        this.reqdata.subject = ''
        this.reqdata.body = ''
        this.reqdata.state = ''
        this.reqdata.district = ''
        this.reqdata.attachments = ''
      }
      this.$store.commit('reqdata', this.reqdata)
      for (var i = 0; i < this.selected.length; i++) {
        if (this.dscrdselected.indexOf(this.selected[i]) === -1) {
          this.dscrdselected.push(this.selected[i])
        }
      }
      this.$store.commit('dscrdselected', this.dscrdselected)
      this.selected = []
      this.$store.commit('selected', this.selected)
    },
    gsaveselected () {
      this.csvgsave = true
      this.$store.commit('csvgsave', this.csvgsave)
      const formData = new FormData()
      for (var i = 0; i < this.mulupfile2.length; i++) {
        formData.append('file2[' + i + ']', this.mulupfile2[i])
      }
      if (this.reqdata !== '') {
        formData.append('file2send2', Object.values(this.reqdata.attachments))
      } else {
        formData.append('file2send2', Object.values({ pamp: 'Pamphlet2020.pdf', LoI: 'letter-of-intent.docx' }))
      }
      formData.append('list', this.selected)
      formData.append('user', this.$store.getters.user_name)
      const currentObj = this
      this.axios.post(this.url + '/api/main/csv/gsave', formData,
        {
          headers: {
            'Content-Type': 'multipart/form-data'
          }
        })
        .then(function (response) {
          currentObj.gsavecsv = response.data
          currentObj.$store.commit('gsavecsv', currentObj.gsavecsv)
          console.log(currentObj.gsavecsv)
          currentObj.reqdata = ''
          currentObj.$store.commit('reqdata', currentObj.reqdata)
          currentObj.popoverShow4 = false
          for (i = 0; i < currentObj.selected.length; i++) {
            if (currentObj.gsvselected.indexOf(currentObj.selected[i]) === -1) {
              currentObj.gsvselected.push(currentObj.selected[i])
            }
          }
          currentObj.$store.commit('gsvselected', currentObj.gsvselected)
          currentObj.csvapp = false
          currentObj.$store.commit('csvapp', currentObj.csvapp)
          currentObj.selected = []
          currentObj.$store.commit('selected', currentObj.selected)
          currentObj.sender = false
        })
        .catch(function (error) {
          console.log(error)
        })
    },
    saveDetail (e) {
      e.preventDefault()
      const currentObj = this
      this.axios.post(this.url + '/api/main/store', {
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
          this.$store.commit('output', this.output)
          console.log(output)
          this.loader = false
        })
        .catch(function (error) {
          currentObj.output = error
          console.log(error)
        })
    },
    clickList: function (pk, i) {
      console.log('clickList fired with ' + pk)
      const currentObj = this
      this.axios.post(this.url + '/api/main/idrequest', {
        remail: pk,
        cname: i
      })
        .then(reqdata => {
          this.reqdata = reqdata.data
          this.$store.commit('reqdata', this.reqdata)
        })
        .catch(function (error) {
          currentObj.reqdata = error
        })
    },
    formSubmit (e) {
      e.preventDefault()
      const currentObj = this
      this.isNight = false
      this.$store.commit('simisNight', this.isNight)
      this.isNight1 = false
      this.$store.commit('simisNight1', this.isNight1)
      this.isNight2 = true
      this.$store.commit('simisNight2', this.isNight2)
      this.isNight3 = true
      this.$store.commit('simisNight3', this.isNight3)
      this.axios.post(this.url + '/api/main/submit', {
        remail: this.remail,
        cc: this.cc,
        bcc: this.bcc,
        name: this.name,
        designation: this.designation,
        department: this.department,
        cname: this.cname,
        state: this.state,
        district: this.district,
        cno: this.scno
      })
        .then(output => {
          this.output = output.data
          this.$store.commit('output', this.output)
          this.loader = false
        })
        .catch(function (error) {
          currentObj.output = error
        })
    },
    approve (e) {
      const formData = new FormData()
      for (var i = 0; i < this.mulupfile1.length; i++) {
        formData.append('file1[' + i + ']', this.mulupfile1[i])
      }
      formData.append('file1', this.upfile1)
      formData.append('files2send1', Object.values(this.output.attachments))
      formData.append('remail', this.output.remail)
      formData.append('cc', this.output.cc)
      formData.append('bcc', this.output.bcc)
      formData.append('body', this.output.body)
      formData.append('subject', this.output.subject)
      formData.append('label', 'information-mail')
      formData.append('user', this.$store.getters.user_name)
      e.preventDefault()
      const currentObj = this
      this.detail = ''
      this.$store.commit('detail', this.detail)
      this.axios.post(this.url + '/api/main/approve', formData,
        {
          headers: {
            'Content-Type': 'multipart/form-data'
          }
        })
        .then(function (response) {
          currentObj.output = response.data
          currentObj.$store.commit('output', currentObj.output)
          console.log(currentObj.output)
          currentObj.sender = false
          currentObj.clear()
        })
        .catch(function (error) {
          currentObj.output = error
          console.log(currentObj.output)
        })
      this.popoverShow1 = false
    },
    disc1 (value, key) {
      console.log(value, key)
      this.$delete(this.output.attachments, key)
      console.log(Object.values(this.output.attachments))
      this.$store.commit('output', this.output)
    },
    disc2 (value, key) {
      console.log(value, key)
      this.$delete(this.output.attachments, key)
      console.log(Object.values(this.output.attachments))
      this.$store.commit('output', this.output)
    },
    gsave (e) {
      const formData = new FormData()
      for (var i = 0; i < this.mulupfile1.length; i++) {
        formData.append('file1[' + i + ']', this.mulupfile1[i])
      }
      formData.append('files2send1', Object.values(this.output.attachments))
      formData.append('remail', this.output.remail)
      formData.append('cc', this.output.cc)
      formData.append('bcc', this.output.bcc)
      formData.append('body', this.output.body)
      formData.append('subject', this.output.subject)
      formData.append('user', this.$store.getters.user_name)
      e.preventDefault()
      const currentObj = this
      this.detail = ''
      this.$store.commit('detail', this.detail)
      this.axios.post(this.url + '/api/main/gsave', formData,
        {
          headers: {
            'Content-Type': 'multipart/form-data'
          }
        })
        .then(function (response) {
          currentObj.output = response.data
          currentObj.$store.commit('output', currentObj.output)
          console.log(currentObj.output)
          currentObj.sender = false
          currentObj.clear()
        })
        .catch(function (error) {
          currentObj.output = error
          console.log(currentObj.output)
        })
      this.popoverShow2 = false
    },
    acceptNumber () {
      const x = this.cno.replace(/\D/g, '').match(/(\d{0,2})(\d{0,3})(\d{0,3})(\d{0,4})/)
      this.cno = !x[3] ? (!x[2] ? x[1] : '(' + '+' + x[1] + ')' + ' ' + x[2]) : '(' + '+' + x[1] + ')' + ' ' + x[2] + '-' + x[3] + (x[4] ? '-' + x[4] : '')
      this.scno = x[1] + x[2] + x[3] + x[4]
    }
  }
}
</script>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
#loader{
  position: absolute;
  top:45%;
  left:45%;
}
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
/*
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

a {
  color: #42b983;
}

.form-control{
  margin:10px
}*/
img{
  height:200px;
  width:200px;
}
h1{
position: absolute;
left: 40%;
top: 2%;
margin:0px;
font-style: normal;
font-weight: normal;
font-size: 2em;
text-align: center;
color: #FFFFFF
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
#refresh{
position: absolute;
right:10%;
top: 1%;
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
/*
#rmsg{
  position: absolute;
  left:35%;
  top: 55%;
}*/
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
#goback{
  float:right;
}
</style>
