import { getToken, getUser } from '@/utils/auth';
import { removeCookie, setCookie } from '@/utils/cookies';
import axios from 'axios';

import { defineStore } from 'pinia';

export const useAuthStore = defineStore('auth', {
  state: () => ({
    authenticationUser: getUser(),
    error: null as string | null,
    jwtToken: getToken(),
  }),

  actions: {
    async login(username: string, password: string) {
      this.logout();

      const { data: tokens, status: loginStatus } = await axios.post('/auth/token/', {
        username,
        password,
      });

      if (loginStatus === 401) {
        this.error = 'Неверное имя пользователя или пароль';
        return;
      }

      setCookie('token', tokens.access, { expires: 60 * 60 * 24 * 7 });
      setCookie('refresh', tokens.refresh, { expires: 60 * 60 * 24 * 30 });
      this.jwtToken = tokens.access;

      const { data: user, status: getMeStatus } = await axios.get('/auth/me/');

      if (getMeStatus !== 200) {
        this.logout();
        return;
      }

      setCookie('user', JSON.stringify(user), { expires: 30 });
      this.authenticationUser = user;
    },
    async register(username: string, email: string, password: string) {
      const { data, status } = await axios.post('/auth/register/', { username, email, password });
      console.log(status);
    },
    logout() {
      removeCookie('token');
      removeCookie('refresh');
      removeCookie('user');
      this.jwtToken = null;
      this.authenticationUser = null;
    },
  },
  getters: {
    isAuth: (state) => !!state.authenticationUser,
    authUser: (state) => state.authenticationUser,
    token: (state) => state.jwtToken,
  },
});
