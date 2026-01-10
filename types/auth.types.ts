import type { UserProfile } from "./user.types";

// Authentication and session-related types

export interface AuthTokens {
  access: string;
  refresh?: string;
}

export interface AuthUser {
  user: UserProfile;
  tokens: AuthTokens;
}

// User object returned from /api/auth/user/ endpoint
export interface User {
  id: number;
  username: string;
  email: string;
  first_name: string;
  last_name: string;
  profile: UserProfile;
}

export interface LoginRequest {
  email?: string;
  password?: string;
  // For Google or other social providers
  idToken?: string;
}

export interface LoginResponse extends AuthUser {}

export interface RefreshTokenRequest {
  refresh: string;
}

export interface RefreshTokenResponse {
  access: string;
  refresh?: string;
}

// Dev login response mirrors src.api.auth.DevLoginView
export interface DevLoginUser {
  pk: number;
  username: string;
  email: string;
  first_name: string;
  last_name: string;
}

export interface DevLoginResponse {
  user: DevLoginUser;
  access: string;
  refresh: string;
}
