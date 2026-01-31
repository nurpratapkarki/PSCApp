import type { UserProfile, UserProfileUpdate, ReactNativeImageAsset } from "../../types/user.types";
import { API_ENDPOINTS } from "../../config/api.config";
import { apiRequest, uploadFile } from "./client";

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

/**
 * Check if a value is a React Native image asset
 */
function isReactNativeImageAsset(value: unknown): value is ReactNativeImageAsset {
  return (
    typeof value === "object" &&
    value !== null &&
    "uri" in value &&
    "name" in value &&
    "type" in value
  );
}

/**
 * Update the current user's profile.
 * Supports both web File objects and React Native image assets for profile_picture.
 */
export async function updateUserProfile(
  updates: UserProfileUpdate,
  token?: string | null,
): Promise<UserProfile> {
  const profilePicture = updates.profile_picture;
  
  // If there's a profile picture, we need to use FormData
  if (profilePicture instanceof File || isReactNativeImageAsset(profilePicture)) {
    const formData = new FormData();
    
    // Add all non-file fields
    Object.entries(updates).forEach(([key, value]) => {
      if (key !== "profile_picture" && value !== undefined && value !== null) {
        formData.append(key, String(value));
      }
    });
    
    // Add the file - handle both File and React Native image asset
    if (profilePicture instanceof File) {
      formData.append("profile_picture", profilePicture);
    } else {
      // React Native format: { uri, name, type }
      // @ts-ignore - FormData accepts this format in React Native
      formData.append("profile_picture", profilePicture);
    }
    
    return uploadFile<UserProfile>(API_ENDPOINTS.auth.user, formData, token, "PATCH");
  }
  
  // Regular JSON update (no file)
  return apiRequest<UserProfile>(API_ENDPOINTS.auth.user, {
    method: "PATCH",
    body: updates,
    token: token ?? undefined,
  });
}
