<template>
    <div class="container">
        <div class="row justify-content-center">
            <div class="col-md-8">
                <div class="card">
                    <div class="card-header">Manual Input Fields</div>
    
                    <div class="card-body">
                        <form>
                        <strong>MailId:</strong>
                        <input type="email" class="form-control" v-model="mail_id">
                        <strong>CC:</strong>
                        <input type="email" class="form-control" v-model="cc">
                        <strong>BCC:</strong>
                        <input type="email" class="form-control" v-model="bcc">
                        <strong>Name:</strong>
                        <input type="text" class="form-control" v-model="name">
                        <strong>Designation:</strong>
                        <input type="text" class="form-control" v-model="designation">
                        <strong>Department:</strong>
                        <input type="text" class="form-control" v-model="department">
                        <strong>College Name:</strong>
                        <input type="text" class="form-control" v-model="college">
                        <strong>Contact No.:</strong>
                        <input type="number" class="form-control" v-model="contact">
                          <button @click="formSubmit" class="btn btn-success">Accept</button><br><br>
                          <button class="btn btn-success">Reject</button><br><br>
                          <button class="btn btn-success">Edit</button><br><br>
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
</template>
     
<script>
    export default {
        mounted() {
            console.log('Component mounted.')
        },
        data() {
            return {
              mail_id : '',
              cc : '',
              bcc : '',
              name : '',
              designation : '',
              department : '',
              college : '',
              contact : '',
              output: ''
            };
        },
        methods: {
            formSubmit(e) {
                e.preventDefault();
                let currentObj = this;
                let axiosConfig = {
                headers: {
                  'Content-Type': 'application/json;charset=UTF-8'
                 }
                }
                this.axios.post('http://127.0.0.1:8081/', {
                    mail_id : this.mail_id,
                    cc : this.cc,
                    bcc : this.bcc,
                    name : this.name,
                    designation : this.designation,
                    department : this.department,
                    college : this.college,
                    contact : this.contact,
                },axiosConfig)
                .then(function (response) {
                    currentObj.output = response.data;
                })
                .catch(function (error) {
                    currentObj.output = error;
                });
            }
        }
    }
</script>
