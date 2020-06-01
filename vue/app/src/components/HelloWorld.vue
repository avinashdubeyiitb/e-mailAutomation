<template>
  <div class="hello">
    <h1>{{ msg }}</h1>
    <div class="container">
        <div class="row justify-content-center">
            <div class="col-md-8">
                <div class="card">
                    <div class="card-header">Vue Axios Post - ItSolutionStuff.com</div>
                    <div class="card-body">
                        <form @submit="formSubmit">
                        <strong>Name:</strong>
                        <input type="text" class="form-control" v-model="name">
                        <strong>Description:</strong>
                        <input type="email" class="form-control" v-model="email">
                        <button class="btn btn-success">Submit</button>
                        </form>
                        <strong>Output:</strong>
                        <pre>
                        {{output}}
                        </pre>
                    </div>
                </div>
            </div>
        </div>
    </div>

  </div>
</template>

<script>
export default {
  name: 'HelloWorld',
  props: {
    msg: String
  },
  mounted () {
    console.log('Component mounted.')
  },
  data () {
    return {
      name: '',
      email: '',
      output: ''
    }
  },
  methods: {
    formSubmit (e) {
      e.preventDefault()
      const currentObj = this
      this.axios.post('http://localhost:8081/api/teg', {
        name: this.name,
        email: this.email
      })
        .then(function (response) {
          currentObj.output = response.data
        })
        .catch(function (error) {
          currentObj.output = error
        })
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
</style>
