import { $api } from '@/api';
import type { IToken } from '@/stores/types/auth.types';
import { getCookie } from '@/utils/cookies';

export class AuthService {
  public static getToken(): string | null {
    const token = getCookie('token');
    if (!token) return null;
    return token;
  }
  public static async login(username: string, password: string) {
    const { data: tokens, status: loginStatus } = await $api.post<IToken>('/auth/token/', {
      username,
      password,
    });
  }
}
