import axios from 'axios';
import { useAuthStore } from '@/stores';

export const $api = axios.create({
  withCredentials: false,
  baseURL: 'http://127.0.0.1:8000/api/',
});

$api.interceptors.request.use(
  (request) => {
    const store = useAuthStore();
    if (store.token) {
      request.headers.Authorization = `Bearer ${store.token}`;
      return request;
    }
    return request;
  },
  (err) => {
    Promise.reject(err);
  }
);
