import type { IUser } from '@/stores';
import { getCookie } from '@/utils/cookies';

export const getUser = () => {
  const user = getCookie('user');
  if (!user) return null;
  return JSON.parse(user) as IUser;
};
