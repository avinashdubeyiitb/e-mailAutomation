<template>
  <div>
    <h1>Send Information Mail</h1>
    <b-container >
      <b-row><b-col cols="8">

    <div >
        <div>
            <div class="col-md-8">
                <div class="card">
                    <div class="card-header">Please input fields</div>
                    <div class="card-body">
                        <form @submit="formSubmit">
                        <strong>Recipient Email ID:</strong>
                        <input type="email" class="form-control" v-model="remail"><br>
                        <strong>CC/BCC:</strong>
                        <input type="email" class="form-control" v-model="ccbcc"><br>
                        <strong>Name:</strong>
                        <input type="text" class="form-control" v-model="name"><br>
                        <strong>Designation:</strong>
                        <input type="text" class="form-control" v-model="designation"><br>
                        <strong>Department:</strong>
                        <input type="text" class="form-control" v-model="department"><br>
                        <strong>College Name:</strong>
                        <input type="text" class="form-control" v-model="cname"><br>
                        <strong>Contact No.:</strong>
                        <input type="tel" class="form-control" v-model="cno"><br>
                        <button class="btn btn-success" v-b-modal.modal-1>Submit</button>
                        </form>
                        <!-- <strong>Response:</strong> -->
                        <!-- <pre>
                        </pre> -->
                        <p id="rmsg">{{output}}</p>
                        <!-- <div  v-if="{{output.key}} === 'success'"> -->
                        <p>{{key}}</p>
                        <p>-----------------------or------------------------</p>
                        <p>Upload csv file</p>
                        <label>File:
                        <input type="file" accept=".csv" id="file" ref="file" v-on:change="handleFileUpload()"/>
                      </label>
                        <button v-on:click="submitFile()" class="btn btn-success">Submit</button>
                    </div>
                </div>
            </div>
        </div>
    </div>
  </b-col>

  <b-col cols="2" v-show="!isNight">"show right now"
  <b-container title="Response" v-show="!isNight">
     <!-- <p class="my-4">Key: {{output.key}}</p> -->
     <form>
     <p>Key:</p>
     <input v-if = "key1" v-model = "output.key"
     @blur= "key1 = false; $emit('update')"
     @keyup.enter = "key1=false; $emit('update')">
           <div v-else>
       <label @click = "key1 = true;">{{output.key}} </label>
     </div>
     <!-- <p class="my-4">Recipient ID:{{output.recipientId}}</p> -->
     <p>recipientId:</p>
     <input v-if = "key2" v-model = "output.recipientId"
     @blur= "key2 = false; $emit('update')"
     @keyup.enter = "key2=false; $emit('update')">
           <div v-else>
       <label @click = "key2 = true;"> {{output.recipientId}} </label>
     </div>
     <!-- <p class="my-4">Subject: {{output.subject}}</p> -->
     <!-- <p class="my-4">Body: {{output.body}}</p> -->
     <p>subject:</p>
     <input v-if = "key3" v-model = "output.subject"
     @blur= "key3 = false; $emit('update')"
     @keyup.enter = "key3=false; $emit('update')">
           <div v-else>
       <label @click = "key3 = true;"> {{output.subject}} </label>
     </div>
     <p>body:</p>
     <input v-if = "key4" v-model = "output.body"
     @blur= "key4 = false; $emit('update')"
     @keyup.enter = "output.body=false; $emit('update')">
           <div v-else>
       <label @click = "key4 = true;"> {{output.body}} </label>
     </div>
   </form>
   </b-container></b-col>
  <b-col cols="2" v-show="isNight">" nothing to show right now"<img alt="no-thumbnail" src="../assets/no-thumbnail.jpg"> </b-col>
  <div v-show="!isNight">
    <form >
    <b-button class="btn btn-success" id="popover-reactive-1" ref="button1">Approve</b-button>
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
          <div>
            <b-button @click="onClose" size="sm" variant="danger">Cancel</b-button>
            <b-button @click="approve" size="sm" variant="primary">Sure</b-button>
          </div>
        </b-popover>
    <form @submit="edit">
    <button class="btn btn-success" >Edit</button>
    </form>
    <b-button id="popover-reactive-2" ref="button2" class="btn btn-success" >Reject</b-button>
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
            <b-button @click="gsave" size="sm" variant="primary">Save to draft</b-button>
            <b-button @click="reject" size="sm" variant="danger">Discard</b-button>
          </div>
        </b-popover>
    <!-- </div> -->
    <!-- Output from the popover interaction -->
  </div>
</b-row>
</b-container>
  </div>
</template>

<script>
import { mapState } from 'vuex'
export default {
  mounted () {
    console.log('Component mounted.')
  },
  computed: {
    ...mapState([
      'key'
    ])
  },
  data () {
    return {
      isNight: true,
      popoverShow1: false,
      popoverShow2: false,
      captureid: '',
      remail: '',
      ccbcc: '',
      name: '',
      designation: '',
      department: '',
      cname: '',
      cno: '',
      output: '',
      file: '',
      key1: '',
      key2: '',
      key3: '',
      key4: '',
      editedTodo: null
    }
  },
  watch: {
  },
  methods: {
    editTodo: function (output) {
      this.editedTodo = output
    },
    handleFileUpload () {
      this.file = this.$refs.file.files[0]
    },
    submitFile () {
      const formData = new FormData()
      // const currentObj = this
      formData.append('file', this.file)
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
    formSubmit (e) {
      e.preventDefault()
      const currentObj = this
      this.isNight = false
      this.axios.post('http://localhost:8081/api/main/submit', {
        captureid: 'sim',
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
        captureid: 'approvesim'
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
    edit (e) {
      e.preventDefault()
      const currentObj = this
      this.axios.post('http://localhost:8081/api/main/edit', {
        captureid: 'editsim'
      })
        .then(function (response) {
          currentObj.output = response.data
          console.log(currentObj.output)
        })
        .catch(function (error) {
          currentObj.output = error
          console.log(currentObj.output)
        })
    },
    reject (e) {
      e.preventDefault()
      const currentObj = this
      this.axios.post('http://localhost:8081/api/main/reject', {
        captureid: 'rejectsim'
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
    },
    gsave (e) {
      e.preventDefault()
      const currentObj = this
      this.axios.post('http://localhost:8081/api/main/gsave', {
        captureid: 'gsavesim'
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
</style>
