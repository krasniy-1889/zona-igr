import type { RouteRecordRaw } from 'vue-router';
import HomeView from '@/views/HomeView.vue';

export const routes: Readonly<RouteRecordRaw[]> = [
  {
    path: '/',
    name: 'home',
    component: HomeView,
  },
  {
    path: '/posts',
    name: 'posts',
    component: () => import('@/views/PostsView.vue'),
    meta: {
      auth: true,
    },
  },
  {
    path: '/login',
    name: 'login',
    component: () => import('@/views/auth/LoginView.vue'),
    meta: {
      guest: true,
    },
  },
];
