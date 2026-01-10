// Question, answer and report types aligned with Django Question/Answer serializers
// PSCApp/src/api/question_answer/serializers.py

export interface AnswerOption {
  id: number;
  answer_text_en: string;
  answer_text_np: string;
  is_correct: boolean;
  display_order: number;
}

export type QuestionDifficulty = string; // e.g. "EASY" | "MEDIUM" | "HARD"
export type QuestionType = string; // e.g. "MCQ_SINGLE" | "MCQ_MULTI" | ...
export type QuestionStatus = string; // e.g. "DRAFT" | "PENDING" | "PUBLIC" | ...

export interface Question {
  id: number;
  question_text_en: string;
  question_text_np: string;
  category: number;
  category_name: string;
  difficulty_level: QuestionDifficulty;
  question_type: QuestionType;
  explanation_en: string | null;
  explanation_np: string | null;
  image: string | null;
  status: QuestionStatus;
  created_by: number | null;
  created_by_name: string;
  is_public: boolean;
  consent_given: boolean;
  scheduled_public_date: string | null; // ISO timestamp
  source_reference: string | null;
  times_attempted: number;
  times_correct: number;
  answers: AnswerOption[];
  created_at: string; // ISO timestamp
}

export interface QuestionReport {
  id: number;
  question: number;
  reported_by: number;
  reason: string;
  description: string;
  status: string;
  created_at: string; // ISO timestamp
}

// Payloads for creating questions and reports

export interface AnswerCreatePayload {
  answer_text_en: string;
  answer_text_np?: string;
  is_correct: boolean;
  display_order?: number;
}

export interface QuestionCreatePayload {
  question_text_en: string;
  question_text_np?: string;
  category: number;
  difficulty_level: QuestionDifficulty;
  question_type: QuestionType;
  explanation_en?: string | null;
  explanation_np?: string | null;
  image?: string | null;
  consent_given?: boolean;
  source_reference?: string | null;
  answers?: AnswerCreatePayload[];
}

export interface QuestionReportCreatePayload {
  question: number;
  reason: string;
  description?: string;
}
