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
    <button id="msub" v-b-modal.modal-1>Submit</button>
    </form>
    <!-- <strong>Response:</strong> -->
    <!-- <pre>
    </pre> -->
    <p id="rmsg">{{output}}</p>
    <!-- <div  v-if="{{output.key}} === 'success'"> -->
    <p id="or">-----------------------or------------------------</p>
    <p id="up">Upload csv file</p>
    <label id="file">File:
    <input type="file" accept=".csv" id="file" ref="file" v-on:change="handleFileUpload()"/>
  </label>
    <button id="csub" v-on:click="submitFile()">Submit</button>
  </div>
  <div v-show="!isNight2">
    <p v-show="!isNight2">"comming soon"</p>
    <div id="content">
      <div class="text-uppercase text-bold">id selected: {{selected}}</div>
<table class="table table-striped table-hover">
<thead>
<tr>
<th>
<label class="form-checkbox">
<input type="checkbox" v-model="selectAll" @click="select">
</label>
</th>
<th>id</th>
<th>name</th>
<th>email</th>
</tr>
</thead>
<tbody>
<tr v-bind:key="i" v-for="(pk,i) in items" v-on:click="clickList(pk)">
<td>
<label class="form-checkbox">
<input type="checkbox" :value="pk.age" v-model="selected">
</label>
</td>
<td>{{pk.age}}</td>
<td>{{pk.first_name}}</td>
<td>{{pk.last_name}}</td>
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
      <b-button id="save"> Save </b-button>
    <!-- </div> -->
   </label><br>
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
      items: [
        { age: 1, first_name: 'Dickerson', last_name: 'Mzxacdonald' },
        { age: 2, first_name: 'Larsen', last_name: 'Shzxaw' },
        { age: 3, first_name: 'Geneva', last_name: 'Wilson' },
        { age: 4, first_name: 'Jami', last_name: 'Carney' },
        { age: 5, first_name: 'Dicxzkerson', last_name: 'Macdonald' },
        { age: 6, first_name: 'Larszxen', last_name: 'Shaw' },
        { age: 7, first_name: 'Genevzxa', last_name: 'Wilzxson' },
        { age: 8, first_name: 'Jamzxi', last_name: 'Carnezxy' },
        { age: 9, first_name: 'Diczxkerson', last_name: 'Maxzcdonald' },
        { age: 10, first_name: 'Lazxrsen', last_name: 'Shxzaw' },
        { age: 11, first_name: 'Genzxeva', last_name: 'Wilsoadsn' },
        { age: 12, first_name: 'Jamzxi', last_name: 'Carnezy' }
      ],
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
      editedTodo: null
    }
  },
  watch: {
  },
  methods: {
    select () {
      this.selected = []
      if (!this.selectAll) {
        for (const pk in this.items) {
          this.selected.push(this.items[pk].age)
        }
      }
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
      this.axios.post('http://localhost:8081/api/main/csvsubmit',
        formData,
        {
          headers: {
            'Content-Type': 'multipart/form-data'
          }
        }
      )
        .then(function () {
          console.log('SUCCESS!!')
        })
        .catch(function () {
          console.log('FAILURE!!')
        })
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
    approveselect () {

    },
    discardselected () {

    },
    gsaveselected () {

    },
    clickList: function (pk) {
      console.log('clickList fired with ' + pk.age)
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
