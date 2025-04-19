<script setup lang="ts">
import { RouterLink, RouterView } from 'vue-router'
import type { MutationType } from 'pinia';
import { useAuthStore } from './stores/auth';
import { buildLogoutRequest } from './requests/login';
import type { LoginResponse } from './models/LoginResponse';
import { buildPostRequest } from './requests/requests.factory';

console.log("App.vue triggered")

async function checkRefresh() {
  const authStore = useAuthStore();
  let url = "http://localhost:8000" + "/refresh";
  return fetch(url, buildPostRequest(""))
    .then((response) => {
      if (response.status === 200) {
        return response.json();
      }
      return Promise.reject("No session token detected")
    })
    .then((data: LoginResponse) => {
      console.log("SessionToken detected, logging in");
      authStore.setAuthentication({ user_id: Number(data.User), isAuthenticated: true, token: data.Token });
      return data;
    })
    .catch((error) => {
      console.warn(error);
    });
}

// since the session token is a secure cookie, the browser cannot check to see if it exists
// only the server can check for the cookie, so make a call to it
checkRefresh()

const authStore = useAuthStore();
authStore.$subscribe((x: any, y: any) => {
  console.log('App.vue: Auth state modified:')
  console.log(x, y);
})

function logout() {
  let url = import.meta.env.VITE_BASEURL + "/logout"
  fetch(url, buildLogoutRequest()).then((response) => {
    if (response.status === 400) {
      throw new Error('Logout failed')
    }
    authStore.$reset()
  })
}

</script>

<template>
  <v-app theme="dark">
    <v-app-bar
      :elevation="0"
      color="surface"
      class="nav-bar"
    >
      <v-container class="d-flex align-center">
        <v-toolbar-title class="text-h5 font-weight-bold">
          <RouterLink to="/" class="text-decoration-none text-primary">NutriTrack</RouterLink>
        </v-toolbar-title>
        
        <v-spacer></v-spacer>
        
        <nav class="d-flex align-center">
          <v-btn
            v-for="link in [

              { title: 'Dashboard', to: '/dashboard' },
              { title: 'Log Meal', to: '/log' }
            ]"
            :key="link.to"
            :to="link.to"
            variant="text"
            class="mx-2 text-none"
          >
            {{ link.title }}
          </v-btn>
          
          <v-divider vertical class="mx-4"></v-divider>
          
          <template v-if="!authStore.isAuth">
            <v-btn
              to="/login"
              variant="outlined"
              color="primary"
              class="text-none"
            >
              Login
            </v-btn>
          </template>
          <template v-else>
            <v-menu>
              <template v-slot:activator="{ props }">
                <v-btn
                  v-bind="props"
                  variant="text"
                  class="text-none"
                >
                  <v-avatar size="32" class="mr-2">
                    <v-icon>mdi-account</v-icon>
                  </v-avatar>
                  Account
                </v-btn>
              </template>
              <v-list>
                <v-list-item>
                  <v-list-item-title>Hello, User</v-list-item-title>
                </v-list-item>
                <v-divider></v-divider>
                <v-list-item @click="logout">
                  <v-list-item-title>Logout</v-list-item-title>
                </v-list-item>
              </v-list>
            </v-menu>
          </template>
        </nav>
      </v-container>
    </v-app-bar>

    <v-main>
      <v-container fluid>
        <RouterView />
      </v-container>
    </v-main>
  </v-app>
</template>

<style>
:root {
  --primary-color: #4CAF50;
  --secondary-color: #2196F3;
  --background-color: #121212;
  --surface-color: #1E1E1E;
  --text-color: #FFFFFF;
}

.v-application {
  background-color: var(--background-color) !important;
}

.nav-bar {
  border-bottom: 1px solid rgba(255, 255, 255, 0.12);
}

.v-btn {
  text-transform: none !important;
  letter-spacing: 0.5px;
}

.v-container {
  max-width: 1280px;
}

.v-main {
  background-color: var(--background-color);
  min-height: calc(100vh - 64px);
}
</style>