
// Leaderboard types aligned with Django LeaderBoard serializer
// PSCApp/src/api/user_stats/serializers.py

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
