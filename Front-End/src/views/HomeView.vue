<script setup lang="ts">
import Home from "../components/Home.vue"
import { useAuthStore } from '@/stores/auth';

const authStore = useAuthStore()
console.log(authStore.isAuthenticated)
</script>

<template>
  <v-main>
    <Home />
  </v-main>
</template>