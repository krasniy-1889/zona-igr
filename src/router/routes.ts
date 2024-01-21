import type { RouteRecordRaw } from 'vue-router';
import HomeView from '@/views/HomeView.vue';

export const routes: Readonly<RouteRecordRaw[]> = [
  {
    path: '/',
    name: 'home',
    component: HomeView,
    meta: {
      title: 'Zona Igr',
    },
  },
  {
    path: '/posts',
    name: 'posts',
    component: () => import('@/views/post/PostsListView.vue'),
    meta: {
      auth: true,
      title: 'Posts',
    },
  },
  {
    path: '/posts/:slug',
    name: 'post-detail',
    component: () => import('@/views/post/PostDetailView.vue'),
    meta: {
      auth: true,
      title: 'Post',
    },
  },
  {
    path: '/login',
    name: 'login',
    component: () => import('@/views/auth/LoginView.vue'),
    meta: {
      guest: true,
      title: 'Login',
    },
  },
  {
    path: '/register',
    name: 'register',
    component: () => import('@/views/auth/RegisterView.vue'),
    meta: {
      guest: true,
      title: 'Register',
    },
  },
];
