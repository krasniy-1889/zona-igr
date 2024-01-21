import axios from 'axios';
import { useAuthStore } from '@/stores';

axios.interceptors.request.use(
  (request) => {
    const store = useAuthStore();
    request.baseURL = 'http://127.0.0.1:8000/api/';
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
