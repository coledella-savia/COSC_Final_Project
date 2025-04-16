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
        errMsg.value = "Error inserting player"
        loading.value = false
    })
    loading.value = false
}

</script>

<template>
 <v-row justify="center">
    <v-col cols="12" lg="6" md="8" sm="10">
      <v-card ref="form">
        <v-card-text>
          <v-text-field
            ref="Name"
            v-model="name"
            :error-messages="errorMessages"
            :rules="[() => !!name || 'This field is required']"
            label="Meal/Snack Name"
            required
          ></v-text-field>
          <v-text-field
            ref="Description"
            :error-messages="errorMessages"
            v-model="desc"
            label="Desription of meal/snack"
            required
          ></v-text-field>
          <v-number-input
            ref="Calories"
            v-model="calories"
            :error-messages="errorMessages"
            :rules="[() => !!calories || 'This field is required', calories >= 0 || 'Cannot have negative calories']"
            label="Calories"
            required
          ></v-number-input>
          <v-date-picker
            width="350"
            :error-messages="errorMessages"
            :rules="[() => !!meal_date || 'This field is required']"
            label="Date Input"
            v-model="meal_date"
            required
          ></v-date-picker>
        
        </v-card-text>
        <v-divider class="mt-12"></v-divider>
        <v-card-actions>
            <v-tooltip v-if="formHasErrors" location="left">
              <template v-slot:activator="{ props }">
              </template>
            </v-tooltip>
          <v-btn 
            size="large"
          color="primary" variant="text" @click="submit" block> Submit </v-btn>
        </v-card-actions>
      </v-card>
    </v-col>
    <v-snackbar v-model="err" color="red">
                {{ errMsg }}
            </v-snackbar>
            <v-snackbar v-model="suc" color="green">
                Successfully Added Meal
            </v-snackbar>
  </v-row>
</template>