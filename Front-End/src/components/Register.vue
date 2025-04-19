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
  <v-container class="d-flex justify-center align-center" style="min-height: 80vh">
    <v-card
      class="mx-auto pa-8"
      elevation="8"
      max-width="600"
      rounded="lg"
      color="surface"
    >
      <v-card-title class="text-h4 font-weight-bold text-center mb-6">
        Create Your Account
      </v-card-title>

      <v-card-subtitle class="text-center mb-8">
        Join NutriTrack and start your health journey
      </v-card-subtitle>

      <v-form @submit.prevent="register">
        <v-row>
          <v-col cols="12" md="6">
            <v-text-field
              v-model="name"
              label="Username"
              variant="outlined"
              density="comfortable"
              :rules="[v => !!v || 'Username is required']"
              class="mb-4"
            ></v-text-field>
          </v-col>

          <v-col cols="12" md="6">
            <v-text-field
              v-model="user_pass"
              label="Password"
              type="password"
              variant="outlined"
              density="comfortable"
              :rules="[v => !!v || 'Password is required']"
              class="mb-4"
            ></v-text-field>
          </v-col>
        </v-row>

        <v-row>
          <v-col cols="12" md="6">
            <v-text-field
              v-model="height"
              label="Height (cm)"
              type="number"
              variant="outlined"
              density="comfortable"
              :rules="[
                v => !!v || 'Height is required',
                v => v > 0 || 'Height must be positive'
              ]"
              class="mb-4"
            ></v-text-field>
          </v-col>

          <v-col cols="12" md="6">
            <v-text-field
              v-model="age"
              label="Age"
              type="number"
              variant="outlined"
              density="comfortable"
              :rules="[
                v => !!v || 'Age is required',
                v => v > 0 || 'Age must be positive'
              ]"
              class="mb-4"
            ></v-text-field>
          </v-col>
        </v-row>

        <v-row>
          <v-col cols="12" md="6">
            <v-select
              v-model="gender"
              :items="['Male', 'Female']"
              label="Gender"
              variant="outlined"
              density="comfortable"
              :rules="[v => !!v || 'Gender is required']"
              class="mb-4"
            ></v-select>
          </v-col>

          <v-col cols="12" md="6">
            <v-text-field
              v-model="weightgoal"
              label="Weight Goal (kg)"
              type="number"
              variant="outlined"
              density="comfortable"
              :rules="[
                v => !!v || 'Weight goal is required',
                v => v > 0 || 'Weight goal must be positive'
              ]"
              class="mb-4"
            ></v-text-field>
          </v-col>
        </v-row>

        <v-btn
          block
          size="large"
          color="primary"
          type="submit"
          :loading="isAttemptingAuth"
          class="mb-4"
        >
          Create Account
        </v-btn>

        <div class="text-center">
          <span class="text-body-2 text-medium-emphasis">Already have an account?</span>
          <v-btn
            to="/login"
            variant="text"
            color="primary"
            class="text-none"
          >
            Sign In
          </v-btn>
        </div>
      </v-form>
    </v-card>

    <v-snackbar
      v-model="err"
      color="error"
      location="top"
      timeout="3000"
    >
      {{ errorMessages }}
    </v-snackbar>

    <v-snackbar
      v-model="success"
      color="success"
      location="top"
      timeout="3000"
    >
      Registration successful
    </v-snackbar>
  </v-container>
</template>

<style scoped>
.v-card {
  transition: transform 0.2s;
}

.v-card:hover {
  transform: translateY(-2px);
}

.v-btn {
  letter-spacing: 0.5px;
}
</style>