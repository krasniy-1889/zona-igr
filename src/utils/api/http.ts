import axios from 'axios';
import { getCookie } from '../cookies';
import { useAuthStore } from '@/stores';

axios.interceptors.request.use((request) => {
  const store = useAuthStore();
  request.baseURL = 'http://127.0.0.1:8000/api/';
  if (store.token) {
    request.headers.Authorization = store.token;
    console.log('Adding token to header', store.token);
  }
});
