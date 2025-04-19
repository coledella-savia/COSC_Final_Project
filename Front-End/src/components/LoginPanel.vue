<script setup lang="ts">
import { ref } from 'vue';
import type { LoginResponse } from '@/models/LoginResponse';
import router from '@/router';
import { useAuthStore } from '@/stores/auth';
import { buildLoginRequest } from '@/requests/login';

const authStore = useAuthStore();

let err = ref(false)
let success = ref(false)
let isAttemptingAuth = ref(false)
let username = ref("");
let password = ref("");
let valid = {}

function login() {
    err.value = false
    isAttemptingAuth.value = true
    let url = "http://localhost:8000" + "/users/login"
    console.log(username)
    fetch(url, buildLoginRequest(username.value, password.value)).then((response) => {
        if (response.status === 400 || response.status === 401) {
            throw new Error('Invalid username or password')
        }
        console.log(response)
        return response.json();
    }).then((data: LoginResponse) => {
        console.log("Success")
        success.value = true
        isAttemptingAuth.value = false
        authStore.setAuthentication({ user_id: Number(data.User), isAuthenticated: true, token: data.Token })
        router.push('/home');
    }).catch(error => {
        err.value = true
        isAttemptingAuth.value = false
    });
}
</script>

<template>
  <v-container class="d-flex justify-center align-center" style="min-height: 80vh">
    <v-card
      class="mx-auto pa-8"
      elevation="8"
      max-width="448"
      rounded="lg"
      color="surface"
    >
      <v-card-title class="text-h4 font-weight-bold text-center mb-6">
        NutriTrack
      </v-card-title>

      <v-card-subtitle class="text-center mb-8">
        Sign in to continue to NutriTrack and start tracking!
      </v-card-subtitle>

      <v-form @submit.prevent="login">
        <v-text-field
          v-model="username"
          label="Username"
          density="comfortable"
          variant="outlined"
          prepend-inner-icon="mdi-account-outline"
          :rules="[v => !!v || 'Username is required']"
          class="mb-4"
        ></v-text-field>

        <v-text-field
          v-model="password"
          label="Password"
          type="password"
          density="comfortable"
          variant="outlined"
          prepend-inner-icon="mdi-lock-outline"
          :rules="[v => !!v || 'Password is required']"
          class="mb-6"
        >
          <template v-slot:loader>
            <v-progress-linear
              :active="isAttemptingAuth"
              height="4"
              indeterminate
              color="primary"
            ></v-progress-linear>
          </template>
        </v-text-field>

        <v-btn
          block
          size="large"
          color="primary"
          type="submit"
          :loading="isAttemptingAuth"
          class="mb-4"
        >
          Sign In
        </v-btn>

        <div class="text-center">
          <span class="text-body-2 text-medium-emphasis">Don't have an account?</span>
          <v-btn
            to="/register"
            variant="text"
            color="primary"
            class="text-none"
          >
            Sign Up
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
      Invalid username or password
    </v-snackbar>

    <v-snackbar
      v-model="success"
      color="success"
      location="top"
      timeout="3000"
    >
      Login successful
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