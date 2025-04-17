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
    <v-snackbar v-model="err" color="red">
        Invalid username or password
    </v-snackbar>
    <v-snackbar v-model="success" color="green">
        Login successful
    </v-snackbar>
    <v-card class="mx-auto pa-12 pb-8" elevation="8" max-width="448" rounded="lg">
        <div class="text-subtitle-1 text-medium-emphasis">Account</div>
        <v-text-field v-model="username" placeholder="Username" density="compact" prepend-inner-icon="mdi-email-outline"
            variant="outlined"></v-text-field>
        <v-text-field v-model="password" type="password" placeholder="Password" density="compact"
            prepend-inner-icon="mdi-lock-outline" variant="outlined" loading>
            <template v-slot:loader>
                <v-progress-linear :active="isAttemptingAuth" height="7" indeterminate></v-progress-linear>
            </template></v-text-field>


        <v-btn block class="mb-8" color="blue" size="large" variant="tonal" @click.prevent="login"
            :disabled="isAttemptingAuth">Login</v-btn>
        <v-btn color="primary" size="large" variant="tonal"
            ><RouterLink to="/register">Register</RouterLink></v-btn>

    </v-card>
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