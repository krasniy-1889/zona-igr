import type { IUser } from '@/stores/types/user.types';
import { getCookie } from '@/utils/cookies';

export const getUser = () => {
  const user = getCookie('user');
  if (!user) return null;
  return JSON.parse(user) as IUser;
};

export const getToken = () => {
  const token = getCookie('token');
  if (!token) return null;
  return token;
};
