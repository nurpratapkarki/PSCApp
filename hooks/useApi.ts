
import { useState, useEffect, useCallback } from 'react';
import { apiRequest, ApiError, getAccessToken } from '../services/api/client';

type Status = 'idle' | 'loading' | 'success' | 'error';

interface State<T> {
  data: T | null;
  error: string | null;
  status: Status;
}

export const useApi = <T>(endpoint: string, lazy = false) => {
  const [state, setState] = useState<State<T>>({
    data: null,
    error: null,
    status: 'idle',
  });

  const execute = useCallback(
    async (body?: unknown) => {
      if (!endpoint) {
        const errorMsg = 'No endpoint provided to useApi hook.';
        setState({ data: null, error: errorMsg, status: 'error' });
        return Promise.reject(errorMsg);
      }
      
      setState({ data: null, error: null, status: 'loading' });
      try {
        const token = getAccessToken();
        const response = await apiRequest<T>(endpoint, { 
          body,
          token,
          method: body ? 'POST' : 'GET',
        });
        setState({ data: response, error: null, status: 'success' });
        return response;
      } catch (err) {
        const errorMessage = err instanceof ApiError ? err.message : 'An unexpected error occurred.';
        setState({ data: null, error: errorMessage, status: 'error' });
        return Promise.reject(errorMessage);
      }
    },
    [endpoint],
  );

  useEffect(() => {
    if (!lazy && endpoint) {
      execute();
    }
  }, [execute, lazy, endpoint]);

  return { ...state, execute, refetch: execute };
};
