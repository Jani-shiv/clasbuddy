import apiClient from './client';

export interface LoginResponse {
  access_token: string;
  token_type: string;
}

export interface User {
  id: number;
  email: string;
  username: string;
  full_name?: string;
  is_active: boolean;
  is_verified: boolean;
  student_id?: string;
  year?: string;
  major?: string;
}

export interface RegisterRequest {
  email: string;
  username: string;
  password: string;
  full_name?: string;
  student_id?: string;
  year?: string;
  major?: string;
}

class AuthAPI {
  async login(email: string, password: string): Promise<LoginResponse> {
    const formData = new FormData();
    formData.append('username', email);
    formData.append('password', password);
    
    return apiClient.post<LoginResponse>('/auth/token', formData, {
      headers: {
        'Content-Type': 'application/x-www-form-urlencoded',
      },
    });
  }

  async register(userData: RegisterRequest): Promise<User> {
    return apiClient.post<User>('/auth/register', userData);
  }

  async getCurrentUser(): Promise<User> {
    return apiClient.get<User>('/auth/me');
  }

  async updateProfile(userData: Partial<User>): Promise<User> {
    return apiClient.put<User>('/auth/me', userData);
  }
}

export const authAPI = new AuthAPI();
