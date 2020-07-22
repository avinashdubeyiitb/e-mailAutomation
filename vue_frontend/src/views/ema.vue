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
    <h1>Email Analytics</h1>
    <button id="refresh" @click="stats()">Refresh</button>
  <div id="col1inner" >
    Sent
<table class="table">
<thead>
<tr>
<th style="width: 17%">User</th>
<th style="width: 50%">Label</th>
<th style="width: 19%">Count</th>
<th>Failed</th>
</tr>
</thead>
<tbody v-for='value in output.Sent' v-bind:key='value.user'>
  <tr v-for='data in value.Data' v-bind:key='data.label'>
    <td>{{value.user}}</td>
    <td>{{data.label}}</td>
    <td>{{data.count}}
      <b-dropdown class="dropsize">
              <div v-for="(id,idx) in data.clist" v-bind:key='idx' >
                <b-dropdown-item v-b-modal="'msent'+idx" @click="getmdtl('sent',id[1])">{{id[0]}}</b-dropdown-item>
                <b-modal :id="'msent'+idx" size="lg" title="Mail Details" hide-footer >
                <b-container class="px-2" >
                  <b>Subject : </b> <br>
                  {{reqdata.subject}}<br>
                  <b>Body : </b> <br>
                <span v-html="reqdata.body"></span><br>
                  <b>Attachments : </b> <br>
                  <div v-for='(data,idx) in reqdata.attachments' v-bind:key='idx' v-show="reqdata.attachments !== 'loading'">
                    <button>{{data}}</button>
                  </div>
                  <div v-show="reqdata.attachments === 'loading'">{{reqdata.attachments}}</div>
                </b-container>
                <b-button @click="$bvModal.hide('msent'+idx)">OK</b-button>
                <b-button @click="download('sent',id[1])" class="float-right">Download</b-button>
                </b-modal>
              </div>
      </b-dropdown>
      </td>
    <td>{{data.failed}}
      <b-dropdown class="dropsize">
              <div v-for="(id,idx) in data.flist" v-bind:key='idx' >
                <b-dropdown-item>{{id[0]}}</b-dropdown-item>
              </div>
      </b-dropdown>
      </td>
  </tr>
</tbody>
</table>
Draft
<table class="table">
  <thead>
<tr>
<th style="width: 67%">User</th>
<th style="width: 19%">Count</th>
<th>Failed</th>
</tr>
</thead>
  <tbody >
  <tr v-for='data in output.Draft' v-bind:key='data.user'>
    <td>{{data.user}}</td>
    <td>
      {{data.Data.count}}
      <b-dropdown class="dropsize">
              <div v-for="(id,idx) in data.Data.clist" v-bind:key='idx' >
                <b-dropdown-item v-b-modal="'mdraft'+idx" @click="getmdtl('draft',id[1])">{{id[0]}}</b-dropdown-item>
                <b-modal :id="'mdraft'+idx" size="lg" title="Mail Details" hide-footer >
                <b-container class="px-2" >
                  <b>Subject : </b> <br>
                  {{reqdata.subject}}<br>
                  <b>Body : </b> <br>
                <span v-html="reqdata.body"></span><br>
                  <b>Attachments : </b> <br>
                  <div v-for='(data,idx) in reqdata.attachments' v-bind:key='idx' v-show="reqdata.attachments !== 'loading'">
                    <button>{{data}}</button>
                  </div>
                  <div v-show="reqdata.attachments === 'loading'">{{reqdata.attachments}}</div>
                </b-container>
                <b-button @click="$bvModal.hide('mdraft'+idx)">OK</b-button>
                <b-button @click="download('draft',id[1])" class="float-right">Download</b-button>
                </b-modal>
              </div>
      </b-dropdown>
      </td>
    <td>{{data.Data.failed}}
      <b-dropdown class="dropsize">
              <div v-for="(id,idx) in data.Data.flist" v-bind:key='idx' >
                <b-dropdown-item >{{id[0]}}</b-dropdown-item>
              </div>
      </b-dropdown>
      </td>
  </tr>
</tbody>
</table>
Inbox
<table class="table">
  <thead>
<tr>
<th style="width: 17%">User</th>
<th style="width: 50%">Label</th>
<th>Count</th>
</tr>
</thead>
  <tbody v-for='value in output.Inbox' v-bind:key='value.user'>
  <tr v-for='data in value.Data' v-bind:key='data.label'>
    <td>{{value.user}}</td>
    <td>{{data.label}}</td>
    <td>{{data.count}}
      <b-dropdown class="dropsize">
              <div v-for="(id,idx) in data.clist" v-bind:key='idx' >
                <b-dropdown-item v-b-modal="'minbox'+idx" @click="getmdtl('inbox',id[1])">{{id[0]}}</b-dropdown-item>
                <b-modal :id="'minbox'+idx" size="lg" title="Mail Details" hide-footer >
                <b-container class="px-2" >
                  <b>Subject : </b> <br>
                  {{reqdata.subject}}<br>
                  <b>Body : </b> <br>
                <span v-html="reqdata.body"></span><br>
                  <b>Attachments : </b> <br>
                  <div v-for='(data,idx) in reqdata.attachments' v-bind:key='idx' v-show="reqdata.attachments !== 'loading'">
                    <button>{{data}}</button>
                  </div>
                  <div v-show="reqdata.attachments === 'loading'">{{reqdata.attachments}}</div>
                </b-container>
                <b-button @click="$bvModal.hide('minbox'+idx)">OK</b-button>
                <b-button @click="downloaded = true;download('inbox',id[1])" class="float-right">Download</b-button>
                <div id="loader" v-show="downloaded">
                <b-button variant="danger" disabled>
                  <b-spinner small ></b-spinner>
                  Downloading...
                </b-button>
                </div>
                </b-modal>
              </div>
      </b-dropdown>
      </td>
  </tr>
</tbody>
</table>
<div id="loader" v-show="loader">
<b-button variant="danger" disabled>
  <b-spinner small ></b-spinner>
  Loading...
</b-button>
</div>
<!--
<div id="loader" v-show="downloaded">
<b-button variant="danger" disabled>
  <b-spinner small ></b-spinner>
  Downloading...
</b-button>
</div>-->
  </div>
  </div>
</template>

<script>
export default {
  mounted () {
    console.log('Component mounted.')
    this.stats()
  },
  computed: {
  },
  data () {
    return {
      output: '',
      url: this.$store.getters.url,
      reqdata: { subject: 'loading', body: 'loading', attachments: 'loading' },
      // isget: false,
      // issend: false,
      // selected: [],
      // result: '',
      // sent: []
      loader: true,
      downloaded: false
    }
  },
  methods: {
    download (label, mid) {
      this.axios.post(this.url + '/api/main/download', {
        messageid: mid,
        type: label
      })
        .then(response => {
          console.log('Downloaded')
          this.downloaded = false
        })
        .catch(function (error) {
          console.log(error)
        })
    },
    getmdtl (label, mid) {
      if (this.reqdata !== '') {
        this.reqdata.subject = 'loading'
        this.reqdata.body = 'loading'
        this.reqdata.attachments = 'loading'
      }
      this.axios.post(this.url + '/api/main/getmdtl', {
        messageid: mid,
        type: label
      })
        .then(reqdata => {
          this.reqdata = reqdata.data
          console.log('SUCCESS')
        })
        .catch(function (error) {
          console.log(error)
        })
    },
    stats () {
      this.loader = true
      this.axios.post(this.url + '/api/main/stats', {
      })
        .then(output => {
          this.output = output.data
          console.log('SUCCESS')
          this.loader = false
        })
        .catch(function (error) {
          console.log(error)
        })
    }
  }
}
</script>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
#refresh{
position: absolute;
top: 5%;
right: 10%;
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
border: 1px solid #000000;
box-sizing: border-box;
border-radius: 10px;
}
/*
#col2inner{
position: absolute;
width: 48%;
height: 90%;
right: 1%;
top: 15%;
background: #4ABDAC;
border: 1px solid #000000;
box-sizing: border-box;
border-radius: 10px;
}
#sub1{
position: absolute;
right:40%;
top: 60%;
}
#sub2{
position: absolute;
right:80%;
top: 60%;
}
#result{
position: absolute;
right:50%;
top: 70%;
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
tr ,td,thead,table,th{
  padding:0px;
  padding-left:6px;
}
#loader{
  position: absolute;
  top:45%;
  left:45%;
}
</style>
