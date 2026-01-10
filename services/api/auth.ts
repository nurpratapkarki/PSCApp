import { API_ENDPOINTS } from "../../config/api.config";
import { apiRequest } from "./client";

import type {
	DevLoginResponse,
	RefreshTokenRequest,
	RefreshTokenResponse,
} from "../../types/auth.types";

// Authentication-related API helpers

export async function devLogin(email: string): Promise<DevLoginResponse> {
	return apiRequest<DevLoginResponse>(API_ENDPOINTS.auth.devLogin, {
		method: "POST",
		body: { email },
	});
}

// Direct JWT token obtain using SimpleJWT's TokenObtainPairView
export async function obtainTokenPair(
	credentials: { username?: string; email?: string; password: string },
): Promise<RefreshTokenResponse> {
	return apiRequest<RefreshTokenResponse>(
		API_ENDPOINTS.auth.tokenObtainPair,
		{
			method: "POST",
			body: credentials,
		},
	);
}

export async function refreshToken(
	payload: RefreshTokenRequest,
): Promise<RefreshTokenResponse> {
	return apiRequest<RefreshTokenResponse>(API_ENDPOINTS.auth.tokenRefresh, {
		method: "POST",
		body: payload,
	});
}

export async function blacklistToken(refresh: string): Promise<void> {
	await apiRequest<void>(API_ENDPOINTS.auth.tokenBlacklist, {
		method: "POST",
		body: { refresh },
	});
}

// dj-rest-auth logout endpoint. Works for both session and JWT setups
export async function logout(): Promise<void> {
	await apiRequest<void>(API_ENDPOINTS.auth.logout, {
		method: "POST",
	});
}
