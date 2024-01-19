import { createRouter, createWebHistory } from 'vue-router';
import { routes } from './routes';
import { getCookie } from '@/utils/cookies';

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: routes,
});

router.beforeEach((to, from, next) => {
  const token = getCookie('token');

  if (!token && to.meta.auth) {
    next({ name: 'login', params: { nextUrl: to.fullPath } });
  } else if (token && to.meta.guest) {
    next(from.path);
  } else {
    next();
  }
});

export default router;
