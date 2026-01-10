
import { useState, useEffect, useCallback } from 'react';
import { apiRequest, ApiError } from '../services/api/client';

type Status = 'idle' | 'loading' | 'success' | 'error';

interface PaginatedResponse<T> {
    count: number;
    next: string | null;
    previous: string | null;
    results: T[];
}

interface State<T> {
  data: T[] | null;
  count: number;
  error: string | null;
  status: Status;
}

export const usePaginatedApi = <T>(endpoint: string, lazy = false) => {
  const [state, setState] = useState<State<T>>({
    data: null,
    count: 0,
    error: null,
    status: 'idle',
  });

  const execute = useCallback(
    async (queryParams = '') => {
      setState({ data: null, count: 0, error: null, status: 'loading' });
      try {
        const url = `${endpoint}${queryParams}`;
        const response = await apiRequest<PaginatedResponse<T>>(url);
        setState({ data: response.results, count: response.count, error: null, status: 'success' });
        return response;
      } catch (err) {
        const errorMessage = err instanceof ApiError ? err.message : 'An unexpected error occurred.';
        setState({ data: null, count: 0, error: errorMessage, status: 'error' });
        return Promise.reject(errorMessage);
      }
    },
    [endpoint],
  );

  useEffect(() => {
    if (!lazy) {
      execute();
    }
  }, [execute, lazy]);

  return { ...state, execute, refetch: execute };
};
