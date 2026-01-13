import { useState, useCallback, useEffect } from 'react';
import { 
  setTokens, 
  clearTokens, 
  getAccessToken,
  getRefreshToken 
} from '../services/api/client';
import { 
  login as apiLogin, 
  googleLogin as apiGoogleLogin, 
  logout as apiLogout,
  devLogin as apiDevLogin,
} from '../services/api/auth';
import { getCurrentUserProfile } from '../services/api/profile';
import type { UserProfile } from '../types/user.types';
import type { 
  LoginRequest, 
  GoogleLoginRequest, 
  TokenResponse 
} from '../types/auth.types';

interface AuthState {
  user: UserProfile | null;
  isAuthenticated: boolean;
  isLoading: boolean;
  error: string | null;
}

export function useAuth() {
  const [state, setState] = useState<AuthState>({
    user: null,
    isAuthenticated: false,
    isLoading: true,
    error: null,
  });

  // Check authentication status on mount
  const checkAuth = useCallback(async () => {
    const token = getAccessToken();
    if (!token) {
      setState({
        user: null,
        isAuthenticated: false,
        isLoading: false,
        error: null,
      });
      return;
    }

    try {
      const profile = await getCurrentUserProfile(token);
      setState({
        user: profile,
        isAuthenticated: true,
        isLoading: false,
        error: null,
      });
    } catch {
      clearTokens();
      setState({
        user: null,
        isAuthenticated: false,
        isLoading: false,
        error: null,
      });
    }
  }, []);

  useEffect(() => {
    checkAuth();
  }, [checkAuth]);

  // Login with email and password
  const login = useCallback(async (credentials: LoginRequest): Promise<TokenResponse> => {
    setState(prev => ({ ...prev, isLoading: true, error: null }));
    try {
      const response = await apiLogin(credentials);
      const profile = await getCurrentUserProfile(response.access);
      setState({
        user: profile,
        isAuthenticated: true,
        isLoading: false,
        error: null,
      });
      return response;
    } catch (err) {
      const errorMessage = err instanceof Error ? err.message : 'Login failed';
      setState(prev => ({
        ...prev,
        isLoading: false,
        error: errorMessage,
      }));
      throw err;
    }
  }, []);

  // Login with Google OAuth
  const googleLogin = useCallback(async (token: GoogleLoginRequest): Promise<TokenResponse> => {
    setState(prev => ({ ...prev, isLoading: true, error: null }));
    try {
      const response = await apiGoogleLogin(token);
      const profile = await getCurrentUserProfile(response.access);
      setState({
        user: profile,
        isAuthenticated: true,
        isLoading: false,
        error: null,
      });
      return response;
    } catch (err) {
      const errorMessage = err instanceof Error ? err.message : 'Google login failed';
      setState(prev => ({
        ...prev,
        isLoading: false,
        error: errorMessage,
      }));
      throw err;
    }
  }, []);

  // Dev login (for development only)
  const devLogin = useCallback(async (email: string, password?: string) => {
    setState(prev => ({ ...prev, isLoading: true, error: null }));
    try {
      const response = await apiDevLogin(email, password);
      const profile = await getCurrentUserProfile(response.access);
      setState({
        user: profile,
        isAuthenticated: true,
        isLoading: false,
        error: null,
      });
      return response;
    } catch (err) {
      const errorMessage = err instanceof Error ? err.message : 'Dev login failed';
      setState(prev => ({
        ...prev,
        isLoading: false,
        error: errorMessage,
      }));
      throw err;
    }
  }, []);

  // Logout
  const logout = useCallback(async () => {
    setState(prev => ({ ...prev, isLoading: true }));
    try {
      await apiLogout();
    } catch {
      // Ignore logout errors, just clear local state
    }
    clearTokens();
    setState({
      user: null,
      isAuthenticated: false,
      isLoading: false,
      error: null,
    });
  }, []);

  // Refresh user profile
  const refreshUser = useCallback(async () => {
    const token = getAccessToken();
    if (!token) return;

    try {
      const profile = await getCurrentUserProfile(token);
      setState(prev => ({
        ...prev,
        user: profile,
      }));
    } catch {
      // Ignore refresh errors
    }
  }, []);

  return {
    ...state,
    login,
    googleLogin,
    devLogin,
    logout,
    refreshUser,
    checkAuth,
  };
}
