// Mock test, attempts and time configuration types
// PSCApp/src/api/mocktest/serializers.py
// PSCApp/src/api/attempt_answer/serializers.py
// PSCApp/src/api/time_config/serializers.py

import type { Question } from "./question.types";

export type TestType =
  | "OFFICIAL"
  | "COMMUNITY"
  | "CUSTOM"
  | string;

export interface MockTestQuestion {
  id: number;
  question: Question;
  question_order: number;
  marks_allocated: number;
}

export interface MockTest {
  id: number;
  title_en: string;
  title_np: string;
  slug: string;
  description_en: string | null;
  description_np: string | null;
  test_type: TestType;
  branch: number | null;
  branch_name: string;
  sub_branch: number | null;
  total_questions: number;
  total_marks?: number; // Optional: total marks for the test
  duration_minutes: number;
  use_standard_duration: boolean;
  pass_percentage: number;
  created_by: number | null;
  created_by_name: string;
  is_public: boolean;
  is_active: boolean;
  attempt_count: number;
  test_questions: MockTestQuestion[];
  created_at: string; // ISO timestamp
}

export interface UserAnswer {
  id: number;
  user_attempt: number;
  question: number;
  question_text?: string;
  selected_answer: number | null;
  selected_answer_text?: string;
  correct_answer_text?: string;
  is_correct: boolean;
  time_taken_seconds: number;
  is_skipped: boolean;
  is_marked_for_review: boolean;
  created_at: string; // ISO timestamp
}

export interface UserAnswerCreatePayload {
  user_attempt: number;
  question: number;
  selected_answer: number | null;
  time_taken_seconds: number;
  is_skipped: boolean;
  is_marked_for_review: boolean;
}

export type AttemptStatus = string; // e.g. "IN_PROGRESS" | "COMPLETED" | ...
export type AttemptMode = string; // e.g. "MOCK_TEST" | "PRACTICE" | ...

// Mock test summary for use in attempt results
export interface MockTestSummary {
  id: number;
  title_en: string;
  title_np?: string;
  pass_percentage: number;
  duration_minutes: number;
  total_questions: number;
}

export interface UserAttempt {
  id: number;
  user: number;
  mock_test: number | MockTestSummary; // Can be ID or full object depending on endpoint
  mock_test_title: string;
  start_time: string | null; // ISO timestamp
  end_time: string | null; // ISO timestamp
  total_time_taken: number | null;
  score_obtained: number | null;
  total_score: number | null;
  percentage: number | null;
  status: AttemptStatus;
  mode: AttemptMode;
  user_answers: UserAnswer[];
  created_at: string; // ISO timestamp
}

export interface StartAttemptRequest {
  mock_test_id?: number;
  mode?: AttemptMode;
}

export interface TimeConfiguration {
  id: number;
  branch: number | null;
  sub_branch: number | null;
  category: number | null;
  standard_duration_minutes: number;
  questions_count: number;
  description: string | null;
}
