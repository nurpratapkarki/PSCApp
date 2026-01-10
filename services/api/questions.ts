import { API_ENDPOINTS } from "../../config/api.config";
import { apiRequest, buildQuery } from "./client";

import type { PaginatedResponse } from "../../types/api.types";
import type { Branch, SubBranch, Category } from "../../types/category.types";
import type {
	Question,
	QuestionReport,
	QuestionCreatePayload,
	QuestionReportCreatePayload,
} from "../../types/question.types";

// ---- Branches & Categories ----

export interface BranchListParams {
	page?: number;
}

export interface SubBranchListParams {
	branch?: number;
	page?: number;
}

export interface CategoryListParams {
	scope_type?: string;
	target_branch?: number;
	target_sub_branch?: number;
	search?: string;
	page?: number;
}

export async function listBranches(
	params: BranchListParams = {},
): Promise<PaginatedResponse<Branch>> {
	const query = buildQuery(params);
	return apiRequest<PaginatedResponse<Branch>>(
		`${API_ENDPOINTS.branches.list}${query}`,
	);
}

export async function listSubBranches(
	params: SubBranchListParams = {},
): Promise<PaginatedResponse<SubBranch>> {
	const query = buildQuery(params);
	return apiRequest<PaginatedResponse<SubBranch>>(
		`${API_ENDPOINTS.branches.subBranches}${query}`,
	);
}

export async function listCategories(
	params: CategoryListParams = {},
): Promise<PaginatedResponse<Category>> {
	const query = buildQuery(params);
	return apiRequest<PaginatedResponse<Category>>(
		`${API_ENDPOINTS.branches.categories}${query}`,
	);
}

// ---- Questions ----

export interface QuestionListParams {
	page?: number;
	category?: number;
	difficulty_level?: string;
	question_type?: string;
	search?: string;
	ordering?: string;
}

export async function listQuestions(
	params: QuestionListParams = {},
	token?: string | null,
): Promise<PaginatedResponse<Question>> {
	const query = buildQuery(params);
	return apiRequest<PaginatedResponse<Question>>(
		`${API_ENDPOINTS.questions.list}${query}`,
		{ token: token ?? undefined },
	);
}

export async function getQuestion(
	id: number,
	token?: string | null,
): Promise<Question> {
	return apiRequest<Question>(`${API_ENDPOINTS.questions.list}${id}/`, {
		token: token ?? undefined,
	});
}

export async function createQuestion(
	payload: QuestionCreatePayload,
	token?: string | null,
): Promise<Question> {
	return apiRequest<Question>(API_ENDPOINTS.questions.list, {
		method: "POST",
		body: payload,
		token: token ?? undefined,
	});
}

export async function updateQuestion(
	id: number,
	payload: Partial<QuestionCreatePayload>,
	token?: string | null,
): Promise<Question> {
	return apiRequest<Question>(`${API_ENDPOINTS.questions.list}${id}/`, {
		method: "PATCH",
		body: payload,
		token: token ?? undefined,
	});
}

export async function deleteQuestion(
	id: number,
	token?: string | null,
): Promise<void> {
	await apiRequest<void>(`${API_ENDPOINTS.questions.list}${id}/`, {
		method: "DELETE",
		token: token ?? undefined,
	});
}

// ---- Question Reports ----

export async function reportQuestion(
	payload: QuestionReportCreatePayload,
	token?: string | null,
): Promise<QuestionReport> {
	return apiRequest<QuestionReport>(API_ENDPOINTS.questions.reports, {
		method: "POST",
		body: payload,
		token: token ?? undefined,
	});
}
