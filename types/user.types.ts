// User & profile types aligned with Django's UserProfileSerializer
// PSCApp/src/api/user/serializers.py

export type LanguageCode = "EN" | "NP";

export interface UserProfile {
  id: number;
  full_name: string;
  email: string;
  phone_number: string | null;
  preferred_language: LanguageCode;
  target_branch: number | null;
  target_sub_branch: number | null;
  branch_name?: string;
  sub_branch_name?: string;
  experience_points: number;
  level: number;
  total_contributions: number;
  profile_picture: string | null;
  is_active: boolean;
  date_joined: string; // ISO timestamp
}