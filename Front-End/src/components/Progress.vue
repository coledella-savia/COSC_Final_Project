<script setup lang="ts">
import { ref, onMounted } from 'vue';
import { useAuthStore } from '@/stores/auth';
import { buildGetRequest } from '@/requests/requests.factory';

const authStore = useAuthStore();
const mealData = ref([]);

onMounted(async () => {
  await loadMeals();
});

async function loadMeals() {
  try {
    const response = await fetch(`http://localhost:8000/meals/${authStore.user_id}`, buildGetRequest());
    if (response.status !== 200) throw new Error("Error retrieving meals from server");
    mealData.value = await response.json();
  } catch (error) {
    console.error("Failed to load meals:", error);
  }
}
</script>

<template>
  <v-container>
    <v-row>
      <v-col cols="12">
        <v-card
          class="pa-6 mb-6"
          color="surface"
          elevation="4"
          rounded="lg"
        >
          <v-card-title class="text-h4 font-weight-bold mb-4">
            Your Progress
          </v-card-title>
          <v-card-subtitle class="text-body-1">
            Track your nutrition journey
          </v-card-subtitle>
        </v-card>
      </v-col>
    </v-row>

    <v-row>
      <v-col cols="12" md="6">
        <v-card
          class="pa-6"
          color="surface"
          elevation="4"
          rounded="lg"
        >
          <v-card-title class="text-h5 font-weight-bold mb-4">
            Weekly Calorie Intake
          </v-card-title>
          <v-card-text>
            <!-- Placeholder for chart -->
            <div class="text-center pa-4">
              <v-icon
                icon="mdi-chart-line"
                size="64"
                color="primary"
              ></v-icon>
              <div class="text-body-1 mt-4">
                Chart will be implemented here
              </div>
            </div>
          </v-card-text>
        </v-card>
      </v-col>

      <v-col cols="12" md="6">
        <v-card
          class="pa-6"
          color="surface"
          elevation="4"
          rounded="lg"
        >
          <v-card-title class="text-h5 font-weight-bold mb-4">
            Nutrition Breakdown
          </v-card-title>
          <v-card-text>
            <!-- Placeholder for nutrition breakdown -->
            <div class="text-center pa-4">
              <v-icon
                icon="mdi-pie-chart"
                size="64"
                color="secondary"
              ></v-icon>
              <div class="text-body-1 mt-4">
                Nutrition breakdown will be implemented here
              </div>
            </div>
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<style scoped>
.v-card {
  transition: transform 0.2s;
}

.v-card:hover {
  transform: translateY(-2px);
}
</style> 