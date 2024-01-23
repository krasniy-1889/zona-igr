import type { IUser } from '@/stores/types/user.types';
import { getCookie } from '@/utils/cookies';

export class UserService {
  public static getToken(): string | null {
    const token = getCookie('token');
    if (!token) return null;
    return token;
  }
  public static getUser() {
    const user = getCookie('user');
    if (!user) return null;
    return JSON.parse(user) as IUser;
  }
}
