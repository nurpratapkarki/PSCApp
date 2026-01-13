// Contribution, analytics, leaderboard, statistics and notification types
// Derived from serializers in PSCApp/src/api/{analytics,user_stats,platform_stats,notification,app_settings}

export type ContributionStatus =
  | "PENDING"
  | "APPROVED"
  | "REJECTED"
  | "MADE_PUBLIC"
  | string;

export interface Contribution {
  id: number;
  user: number;
  user_name: string;
  question: number;
  question_text: string;
  contribution_month: number;
  contribution_year: number;
  status: ContributionStatus;
  is_featured: boolean;
  approval_date: string | null; // ISO timestamp
  public_date: string | null; // ISO timestamp
  rejection_reason: string | null;
  created_at: string; // ISO timestamp
}

export interface DailyActivity {
  date: string; // YYYY-MM-DD
  new_users: number;
  questions_added: number;
  questions_approved: number;
  mock_tests_taken: number;
  total_answers_submitted: number;
  active_users: number;
  created_at: string; // ISO timestamp
}

export type LeaderboardTimePeriod = "WEEKLY" | "MONTHLY" | "ALL_TIME";

export interface LeaderboardEntry {
  rank: number;
  previous_rank: number | null;
  user_name: string;
  profile_picture: string | null;
  total_score: number;
  tests_completed: number;
  accuracy_percentage: number;
  time_period: LeaderboardTimePeriod;
  branch: number | null;
  sub_branch: number | null;
}

export interface UserProgress {
  id: number;
  category: number;
  category_name: string;
  questions_attempted: number;
  correct_answers: number;
  accuracy_percentage: number;
  average_time_seconds: number;
  last_attempted_date: string | null; // ISO date
  weak_topics: string[] | null;
}

export type BadgesEarned = Record<string, unknown>;

export interface UserStatistics {
  questions_contributed: number;
  questions_made_public: number;
  questions_answered: number;
  correct_answers: number;
  total_correct_answers: number;
  questions_correct?: number; // Alias for compatibility
  accuracy_percentage: number;
  mock_tests_completed: number;
  tests_attempted?: number;
  tests_passed?: number;
  study_streak_days: number;
  longest_streak: number;
  total_study_time?: number; // in seconds
  featured_contributions?: number;
  last_activity_date: string | null; // ISO date
  badges_earned: BadgesEarned;
  contribution_rank: number | null;
  accuracy_rank: number | null;
  last_updated: string; // ISO timestamp
}

export interface StudyCollection {
  id: number;
  name: string;
  description: string | null;
  is_private: boolean;
  icon: string | null;
  color_code: string | null;
  question_count: number;
  created_at: string; // ISO timestamp
}

export interface PlatformStats {
  total_questions_public: number;
  total_questions_pending: number;
  total_contributions_this_month: number;
  total_users_active: number;
  total_mock_tests_taken: number;
  total_answers_submitted: number;
  questions_added_today: number;
  top_contributor_this_month: number | null;
  top_contributor_name: string | null;
  most_attempted_category: number | null;
  most_attempted_category_name: string | null;
  last_updated: string; // ISO timestamp
}

// Alias for compatibility with community stats screen
export interface PlatformStatistics {
  total_users: number;
  total_questions: number;
  total_mock_tests: number;
  total_categories: number;
  total_branches: number;
  active_users_today: number;
  questions_added_today: number;
  tests_taken_today: number;
}

export interface AppSetting {
  setting_key: string;
  setting_value: string;
  description: string | null;
  updated_at: string; // ISO timestamp
}

export type NotificationType = string;

export interface Notification {
  id: number;
  notification_type: NotificationType;
  title_en: string;
  title_np: string;
  message_en: string;
  message_np: string;
  related_question: number | null;
  related_mock_test: number | null;
  is_read: boolean;
  action_url: string | null;
  created_at: string; // ISO timestamp
}
