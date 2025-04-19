<script setup lang="ts">
import { ref, onMounted, computed } from 'vue';
import { useAuthStore } from '@/stores/auth';
import { buildGetRequest } from '@/requests/requests.factory';
import { Line } from 'vue-chartjs';
import { Chart as ChartJS, CategoryScale, LinearScale, PointElement, LineElement, Title, Tooltip, Legend } from 'chart.js';

ChartJS.register(CategoryScale, LinearScale, PointElement, LineElement, Title, Tooltip, Legend);

const authStore = useAuthStore();
const mealData = ref([]);

const chartData = computed(() => {
  // Get the last 7 days
  const dates = Array.from({ length: 7 }, (_, i) => {
    const date = new Date();
    date.setDate(date.getDate() - i);
    return date.toISOString().split('T')[0];
  }).reverse();

  // Calculate total calories for each day
  const calories = dates.map(date => {
    const dayMeals = mealData.value.filter(meal => meal.mealDate.startsWith(date));
    return dayMeals.reduce((total, meal) => total + meal.calories, 0);
  });

  return {
    labels: dates.map(date => new Date(date).toLocaleDateString('en-US', { weekday: 'short' })),
    datasets: [
      {
        label: 'Calories',
        data: calories,
        borderColor: '#4CAF50',
        backgroundColor: 'rgba(76, 175, 80, 0.1)',
        tension: 0.4,
        fill: true
      }
    ]
  };
});

const chartOptions = {
  responsive: true,
  maintainAspectRatio: false,
  plugins: {
    legend: {
      display: false
    },
    tooltip: {
      callbacks: {
        label: function(context) {
          return `Calories: ${context.raw}`;
        }
      }
    }
  },
  scales: {
    y: {
      beginAtZero: true,
      title: {
        display: true,
        text: 'Calories'
      }
    }
  }
};

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
      <v-col cols="12">
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
            <div style="height: 400px">
              <Line
                :data="chartData"
                :options="chartOptions"
              />
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