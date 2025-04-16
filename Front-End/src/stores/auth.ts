import { defineStore } from "pinia";

export interface AuthState {
  user_id: number
  isAuthenticated: boolean;
  token: string | null;
}

export const useAuthStore = defineStore("auth", {
  state: (): AuthState => ({
    user_id: 0,
    isAuthenticated: false,
    token: null,
  }),
  getters: {
    isAuth: (state) => state.isAuthenticated,
  },
  actions: {
    setAuthentication({ isAuthenticated, token, user_id }: AuthState) {
      if (isAuthenticated !== undefined) {
        this.$state.isAuthenticated = isAuthenticated;
      }
      this.$state.user_id = user_id;
      this.$state.token = token;
    },
  },
});