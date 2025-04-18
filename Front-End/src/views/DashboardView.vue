<script setup lang="ts">
import { ref, onMounted } from 'vue';
import { useAuthStore } from '@/stores/auth';
import { buildPostRequest } from "@/requests/requests.factory";
import { buildGetRequest } from'@/requests/requests.factory';
import { postMeal } from "@/requests/foodlog"
import router from '@/router';
import Dashboard from '@/components/Dashboard.vue';
const authStore = useAuthStore();

const meal_data = ref()

onMounted(async () => {
    await loadMeals(); // optional 'await' since loadMeals is async
});
async function loadMeals() {
    try {
        const response = await fetch("http://localhost:8000/meals/" + authStore.user_id, buildGetRequest());
        if (response.status !== 200) throw new Error("Error retrieving meals from server");

        const data = await response.json();
        meal_data.value = data;
        console.log(meal_data.value);
    } catch (error) {
        console.error("Failed to load meals:", error);
    }
}

console.log(authStore.isAuthenticated)

</script>

<template>
  <v-main>
    <Dashboard />
  </v-main>
</template>