<script setup lang="ts">
import { ref } from 'vue';
import type { LoginResponse } from '@/models/LoginResponse';
import router from '@/router';
import { useAuthStore } from '@/stores/auth';
import { buildPostRequest } from '@/requests/requests.factory';
import { postregister } from '@/requests/register';


const authStore = useAuthStore();

let err = ref(false)
let success = ref(false)
let isAttemptingAuth = ref(false)
let valid = {}

const errorMessages = ref()
const name = ref()
const user_pass = ref()
const height = ref()
const age = ref()
const gender = ref()
const weightgoal = ref()
const formHasErrors = ref()

function register() {
    err.value = false
    isAttemptingAuth.value = true
    let dailyCalories = 0
    if (gender.value == "Male") {
        dailyCalories = (10 * weightgoal.value) + (6.25 * height.value) - (5 * age.value) + 5
    }
    if (gender.value == "Female") {
        dailyCalories = (10 * weightgoal.value) + (6.25 * height.value) - (5 * age.value) - 161
    }
    let url = "http://localhost:8000"
    console.log(gender.value)
    postregister(url, name.value, user_pass.value, height.value, age.value, gender.value, weightgoal.value, dailyCalories)
    .then((response) => {
        if (response.status === 400) {
            throw new Error('Error Occured')
        }
        console.log(response)
        return response.json();
    }).then((data: LoginResponse) => {
        console.log("Success")
        success.value = true
        router.push('/login');
    }).catch(error => {
        err.value = true
        errorMessages.value = error
        
    });
}
</script>

<template>
    <v-row justify="center">
    <v-col cols="12" lg="6" md="8" sm="10">
      <v-card ref="form">
        <v-card-text>
          <v-text-field
            ref="username"
            v-model="name"
            :error-messages="errorMessages"
            :rules="[() => !!name || 'This field is required']"
            label="Username"
            required
          ></v-text-field>
          <v-text-field
            ref="password"
            :error-messages="errorMessages"
            v-model="user_pass"
            label="password"
            required
          ></v-text-field>
          <v-number-input
            ref="Height"
            v-model="height"
            :error-messages="errorMessages"
            :rules="[() => !!height || 'This field is required', height >= 0 || 'Cannot have negative height']"
            label="Height in CM"
            required
          ></v-number-input>
          <v-number-input
            ref="Age"
            v-model="age"
            :error-messages="errorMessages"
            :rules="[() => !!age || 'This field is required', age >= 0 || 'Cannot have negative age']"
            label="Age"
            required
          ></v-number-input>
          <v-autocomplete
            :items="['Male', 'Female']"
            v-model="gender"
            label="Gender"
            required
          ></v-autocomplete>
          <v-number-input
            ref="Weight Goal"
            v-model="weightgoal"
            :error-messages="errorMessages"
            :rules="[() => !!weightgoal || 'This field is required', weightgoal >= 0 || 'Cannot have negative weight']"
            label="Weight Goal in Kg"
            required
          ></v-number-input>
        
        
        </v-card-text>
        <v-divider class="mt-12"></v-divider>
        <v-card-actions>
            <v-tooltip v-if="formHasErrors" location="left">
              <template v-slot:activator="{ props }">
              </template>
            </v-tooltip>
          <v-btn 
            size="large"
          color="primary" variant="text" @click="register" block> Register </v-btn>
        </v-card-actions>
      </v-card>
    </v-col>
    <v-snackbar v-model="err" color="red">
                {{ errorMessages }}
            </v-snackbar>
            <v-snackbar v-model="success" color="green">
                Successfully Added Meal
            </v-snackbar>
  </v-row>
</template>

<style scoped>
.login-panel {
    display: flex;
    flex-direction: column;
    margin: 2rem;
    width: 24rem;
    border-style: solid;
    border-width: thick;
    border-color: hsla(160, 100%, 37%, 1);
    padding-top: 1rem;
}

.row {
    display: flex;
    align-items: center;
    justify-content: flex-end;
}


.error-message {
    color: red;
}

.success-message {
    color: greenyellow;
}

.input-boxes {
    padding-top: 1rem;
}

span {
    width: 8rem
}

.error-message {
    width: 100%;
    padding-left: 1rem;
    padding-top: 0.5rem;
}

.login-but {
    margin-top: 2rem;
    margin-bottom: 2rem;
    margin-right: 2rem;
}

.box-title {
    margin-left: 1rem;
    font-size: 20px;
    color: hsla(160, 100%, 37%, 1);
}

.input-with-span {
    display: flex;
    justify-content: space-evenly;
    padding: 0.2rem;
}

input,
textarea {
    padding: 9px;
    border: solid 2px rgb(109, 109, 109);
    outline: 0;
    font: normal 13px/100% Verdana, Tahoma, sans-serif;
    width: 10rem;
    background: #cccccc;
    box-shadow: hsla(160, 100%, 37%, 0.2) 0px 0px 8px;
}

input:hover,
textarea:hover,
input:focus,
textarea:focus {
    border-color: hsla(160, 100%, 37%, 1);

}
</style>@/models/LoginResponse