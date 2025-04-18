import { createRouter, createWebHistory } from "vue-router";
import Home from "../views/HomeView.vue"
import { useAuthStore } from "@/stores/auth";
import { buildPostRequest } from "@/requests/requests.factory";
import type { LoginResponse } from "@/models/LoginResponse";

async function checkRefresh() {
  const authStore = useAuthStore();
  let url = "http://localhost:8000" + "/refresh";
  return fetch(url, buildPostRequest(""))
    .then((response) => {
      if (response.status === 200) {
        return response.json();
      }
      throw new Error("No session token detected");
    })
    .then((data: LoginResponse) => {
      console.log("SessionToken detected, logging in");
      authStore.setAuthentication({ isAuthenticated: true, token: data.Token, user_id: data.id });
      return data;
    })
    .catch((error) => {
      console.log(error);
    });
}

const router = createRouter({
  history: createWebHistory("/"),
  routes: [
    {
      path: "/",
      name: "Home",
      component: Home,
      meta: { requiresAuth: true },
    },
    {
      path: "/dashboard",
      name: "Dashboard",
      component: () => import("../views/DashboardView.vue"),
      meta: { requiresAuth: true },
    },
    {
      path: "/login",
      name: "login",
      component: () => import("../views/Login.vue")
    },
    {
      path: "/log",
      name: "log",
      component: () => import("../views/LogView.vue"),
      meta: { requiresAuth: true },
    },
    {
      path: "/register",
      name: "register",
      component: () => import("../views/RegisterView.vue")
    },
  ],
});

router.beforeEach((to, from, next) => {
  const authStore = useAuthStore();
  console.log("Route-Guard: is auth:");
  console.log(authStore.isAuthenticated);
  if (to.matched.some((record) => record.meta.requiresAuth)) {
    // if the route requires auth
    if (authStore.isAuthenticated) {
      // and the user is authenticated
      next();
    } else {
      // the user is not authenticated, check for session token
      checkRefresh().then((data) => {
        console.log(data);
        // the user is authenticated after the check
        if (authStore.isAuthenticated) {
          next();
        }
        // the user is not authenticated after the check
        else {
          next("/login");
        }
      });
    }
  } else {
    next();
  }
});

export default router;