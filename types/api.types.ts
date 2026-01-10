// Generic API response helpers

export interface ApiError {
  message: string;
  statusCode?: number;
  // Optional raw error payload from backend
  details?: unknown;
}

// Default DRF-style paginated response
export interface PaginatedResponse<T> {
  count: number;
  next: string | null;
  previous: string | null;
  results: T[];
}

export type ListResponse<T> = T[];
