<template>
  <div>
    <h1>Send Information Mail</h1>
    <b-container class="bv-example-row">
      <b-row><b-col cols="8">

    <div class="container">
        <div class="row justify-content-center">
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
     <p class="my-4">Key: {{output.key}}</p>
     <p class="my-4">Recipient ID:{{output.recipientId}}</p>
     <p class="my-4">Subject: {{output.subject}}</p>
     <p class="my-4">Body: {{output.body}}</p>
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
      file: ''
    }
  },
  watch: {
  },
  methods: {
    handleFileUpload () {
      this.file = this.$refs.file.files[0]
    },
    submitFile () {
      const formData = new FormData()
      // const currentObj = this
      formData.append('file', this.file)
      this.axios.post('http://localhost:8081/api/teg',
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
      // Some references may be a component, functional component, or plain element
      // This handles that check before focusing, assuming a `focus()` method exists
      // We do this in a double `$nextTick()` to ensure components have
      // updated & popover positioned first
      // this.$nextTick(() => {
      //   this.$nextTick(() => {
      //     ;(ref.$el || ref).focus()
      //   })
      // })
    },
    formSubmit (e) {
      e.preventDefault()
      const currentObj = this
      this.isNight = false
      this.axios.post('http://localhost:8081/api/teg', {
        captureid: 'sim',
        remail: this.remail,
        ccbcc: this.ccbcc,
        name: this.name,
        designation: this.designation,
        department: this.department,
        cname: this.cname,
        cno: this.cno
      })
        .then(function (response) {
          currentObj.output = response.data
          // this.$store.commit('change', response.data)
          if (currentObj.output.key === 'success') {
            console.log(currentObj.output.key)

            // isVisible: False
          //   visibleHandler(isVisible) {
          //   if (isVisible) {
          //     // Do something
          //
          //   } else {
          //     // Do something else
          //     this.isVisible: False
          //   }
          // }
          }
        })
        .catch(function (error) {
          currentObj.output = error
        })
      // this.$store.dispatch('createEvent', this.output)
      this.$store.commit({
        type: 'change',
        key: currentObj.output.key,
        recipientId: currentObj.output.recipientId,
        subject: currentObj.output.subject,
        body: currentObj.output.body
      })
    },
    approve (e) {
      e.preventDefault()
      const currentObj = this
      this.axios.post('http://localhost:8081/api/teg', {
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
      this.axios.post('http://localhost:8081/api/teg', {
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
      this.axios.post('http://localhost:8081/api/teg', {
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
      this.axios.post('http://localhost:8081/api/teg', {
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
