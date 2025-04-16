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
      authStore.setAuthentication({ isAuthenticated: true, token: data.Token });
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
  <v-app class="#181818">
    <v-app-bar :elevation="0"  color="#181818" class="nav-text navShadow">
      <nav>
        <div class="nav-left">
          <RouterLink
          
          to="/">Home</RouterLink>
          <RouterLink to="/dashboard">Dashboard</RouterLink>
          <RouterLink to="/log">Log Meal</RouterLink>
        </div>
        <div class="nav-right">
          <RouterLink v-if="!authStore.isAuth" to="/login">Login</RouterLink>
          <div v-if="authStore.isAuth">
            <span>
              Hello
            </span>
            <a @click="logout">Logout</a>
          </div>
        </div>
      </nav>
    </v-app-bar>

    <RouterView />
  </v-app>
</template>
<style> 
#app {
  margin:0;
  padding: 0;
  background-color: #181818;
}

.v-toolbar {
  box-shadow: rgba(100, 100, 111, 0.2) 0px 7px 29px 0px;
}

.navShadow {
  box-shadow: rgba(100, 100, 111, 0.2) 0px 7px 29px 0px;
}
</style>

<style scoped>


#app> {
  padding: 0;
  margin: 0;
  background-color: #181818;
}

.nav-text {
  color: white;
}

header {
  line-height: 1.5;
  max-height: 100vh;
}

.logo {
  display: block;

}

nav {
  display: flex;
  justify-content: space-between;
  width: 100%;
  font-size: 12px;
  text-align: center;
  color: white;
}

nav a.router-link-exact-active {
  color: var(--color-text);
}

nav a.router-link-exact-active:hover {
  background-color: transparent;
}

nav a {
  display: inline-block;
  padding: 0 1rem;
  border-left: 1px solid var(--color-border);
  cursor: pointer
}

nav a:first-of-type {
  border: 0;
}

@media (min-width: 1024px) {
  header {
    display: flex;
    place-items: center;
    padding-right: calc(var(--section-gap) / 2);
  }

  .logo {
    margin: 0 2rem 0 0;
  }

  header .wrapper {
    display: flex;
    place-items: flex-start;
    flex-wrap: wrap;
  }

  nav {
    text-align: left;

    font-size: 1rem;
    padding: 1rem 0;

  }
}
</style>