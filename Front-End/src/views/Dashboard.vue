<script setup lang="ts">
import Dashboard from "../components/Dashboard.vue"
import { useAuthStore } from '@/stores/auth';

const authStore = useAuthStore()
console.log(authStore.isAuthenticated)
</script>

<template>
  <v-main>
    <Dashboard />
  </v-main>
</template>