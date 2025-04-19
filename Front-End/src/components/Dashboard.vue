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
            Welcome to Your Dashboard
          </v-card-title>
          <v-card-subtitle class="text-body-1">
            Track your nutrition and stay on top of your goals
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
            Recent Meals
          </v-card-title>
          
          <v-list v-if="meal_data && meal_data.length > 0">
            <v-list-item
              v-for="meal in meal_data"
              :key="meal.id"
              class="mb-4"
            >
              <v-card
                class="w-100"
                variant="outlined"
              >
                <v-card-text>
                  <div class="d-flex justify-space-between align-center">
                    <div>
                      <div class="text-h6">{{ meal.mealName }}</div>
                      <div class="text-body-2 text-medium-emphasis">{{ meal.description }}</div>
                    </div>
                    <div class="text-h6 text-primary">
                      {{ meal.calories }} cal
                    </div>
                  </div>
                  <div class="text-caption text-medium-emphasis mt-2">
                    {{ new Date(meal.mealDate).toLocaleDateString() }}
                  </div>
                </v-card-text>
              </v-card>
            </v-list-item>
          </v-list>

          <v-alert
            v-else
            type="info"
            variant="tonal"
            class="mt-4"
          >
            No meals logged yet. Start tracking your nutrition!
          </v-alert>
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
            Quick Actions
          </v-card-title>
          
          <v-list>
            <v-list-item
              to="/log"
              class="mb-4"
            >
              <v-card
                class="w-100"
                color="primary"
                variant="tonal"
              >
                <v-card-text class="d-flex align-center">
                  <v-icon
                    icon="mdi-food"
                    size="large"
                    class="mr-4"
                  ></v-icon>
                  <div>
                    <div class="text-h6">Log a Meal</div>
                    <div class="text-body-2">Track your nutrition intake</div>
                  </div>
                </v-card-text>
              </v-card>
            </v-list-item>

            <v-list-item
              to="/progress"
              class="mb-4"
            >
              <v-card
                class="w-100"
                color="secondary"
                variant="tonal"
              >
                <v-card-text class="d-flex align-center">
                  <v-icon
                    icon="mdi-chart-line"
                    size="large"
                    class="mr-4"
                  ></v-icon>
                  <div>
                    <div class="text-h6">View Progress</div>
                    <div class="text-body-2">Track your nutrition goals</div>
                  </div>
                </v-card-text>
              </v-card>
            </v-list-item>
          </v-list>
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