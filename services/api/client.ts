import { API_BASE_URL } from "../../config/api.config";

export class ApiError extends Error {
  status: number;
  data: unknown;

  constructor(message: string, status: number, data: unknown) {
    super(message);
    this.name = "ApiError";
    this.status = status;
    this.data = data;
  }
}

export type HttpMethod = "GET" | "POST" | "PUT" | "PATCH" | "DELETE";

export interface RequestOptions {
  method?: HttpMethod;
  body?: unknown;
  token?: string | null;
  headers?: Record<string, string>;
}

export async function apiRequest<T>(
  endpoint: string,
  { method = "GET", body, token, headers }: RequestOptions = {},
): Promise<T> {
  const url = endpoint.startsWith("http")
    ? endpoint
    : `${API_BASE_URL}${endpoint}`;

  const finalHeaders: Record<string, string> = {
    Accept: "application/json",
    ...(body ? { "Content-Type": "application/json" } : {}),
    ...(headers ?? {}),
  };

  if (token) {
    finalHeaders.Authorization = `Bearer ${token}`;
  }

  const response = await fetch(url, {
    method,
    headers: finalHeaders,
    body: body ? JSON.stringify(body) : undefined,
    // Allow cookie-based auth when backend is configured for it
    credentials: "include",
  });

  const text = await response.text();
  const data = text ? JSON.parse(text) : null;

  if (!response.ok) {
    const message =
      (data && (data as any).detail) ||
      (data && (data as any).message) ||
      `Request failed with status ${response.status}`;

    throw new ApiError(message, response.status, data);
  }

  return data as T;
}
 
// Helper to build query strings for GET requests from a plain object of params
export function buildQuery<T extends object>(params: T): string {
	const searchParams = new URLSearchParams();

	Object.entries(params as Record<string, unknown>).forEach(
		([key, value]) => {
			if (value === undefined || value === null) {
				return;
			}
			searchParams.append(key, String(value));
		},
	);

	const queryString = searchParams.toString();
	return queryString ? `?${queryString}` : "";
}
