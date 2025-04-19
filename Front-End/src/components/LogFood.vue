<script setup lang="ts">
import { ref } from 'vue';
import { useAuthStore } from '@/stores/auth';
import { buildPostRequest } from "@/requests/requests.factory";
import { postMeal } from "@/requests/foodlog"
import router from '@/router';

const authStore = useAuthStore();
const errorMessages = ref()
const name = ref()
const calories = ref()
const desc = ref()
const meal_date = ref()
const formHasErrors = ref()

let loading = ref(false)
let err = ref(false)
let errMsg = ref("")
let suc = ref(false)

function submit() {
    postMeal("http://localhost:8000", authStore.user_id, name.value, calories.value, desc.value, meal_date.value)
    .then((response: Response) => {
        if (response.status != 200)
            throw new Error()
            loading.value = false
            suc.value = true
            router.push('/dashboard');
    }).catch(() => {
        err.value = true
        errMsg.value = "Error inserting meal"
        loading.value = false
    })
    loading.value = false
}

</script>

<template>
  <v-container class="d-flex justify-center align-center" style="min-height: 80vh">
    <v-card
      class="mx-auto pa-8"
      elevation="8"
      max-width="600"
      rounded="lg"
      color="surface"
    >
      <v-card-title class="text-h4 font-weight-bold text-center mb-6">
        Log Your Meal
      </v-card-title>

      <v-card-subtitle class="text-center mb-8">
        Track your nutrition and stay on top of your goals
      </v-card-subtitle>

      <v-form @submit.prevent="submit">
        <v-text-field
          v-model="name"
          label="Meal/Snack Name"
          variant="outlined"
          density="comfortable"
          :rules="[v => !!v || 'Meal name is required']"
          class="mb-4"
        ></v-text-field>

        <v-textarea
          v-model="desc"
          label="Description"
          variant="outlined"
          density="comfortable"
          :rules="[v => !!v || 'Description is required']"
          class="mb-4"
          rows="3"
        ></v-textarea>

        <v-row>
          <v-col cols="12" md="6">
            <v-text-field
              v-model="calories"
              label="Calories"
              type="number"
              variant="outlined"
              density="comfortable"
              :rules="[
                v => !!v || 'Calories is required',
                v => v >= 0 || 'Calories must be positive'
              ]"
              class="mb-4"
            ></v-text-field>
          </v-col>

          <v-col cols="12" md="6">
            <v-text-field
              v-model="meal_date"
              label="Date"
              type="date"
              variant="outlined"
              density="comfortable"
              :rules="[v => !!v || 'Date is required']"
              class="mb-4"
            ></v-text-field>
          </v-col>
        </v-row>

        <v-btn
          block
          size="large"
          color="primary"
          type="submit"
          :loading="loading"
          class="mb-4"
        >
          Log Meal
        </v-btn>
      </v-form>
    </v-card>

    <v-snackbar
      v-model="err"
      color="error"
      location="top"
      timeout="3000"
    >
      {{ errMsg }}
    </v-snackbar>

    <v-snackbar
      v-model="suc"
      color="success"
      location="top"
      timeout="3000"
    >
      Successfully Added Meal
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