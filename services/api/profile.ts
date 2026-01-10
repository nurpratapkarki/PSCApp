import type { UserProfile } from "../../types/user.types";
import { API_ENDPOINTS } from "../../config/api.config";
import { apiRequest } from "./client";

/**
 * Fetch the currently authenticated user's profile.
 *
 * Supply a JWT access token if you're using header-based auth.
 * If your app relies on cookies, omit the token and ensure
 * the backend is configured for cookie-based authentication.
 */
export async function getCurrentUserProfile(
  token?: string | null,
): Promise<UserProfile> {
  return apiRequest<UserProfile>(API_ENDPOINTS.auth.user, {
    method: "GET",
    token: token ?? undefined,
  });
}

