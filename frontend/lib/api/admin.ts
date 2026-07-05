import { apiFetch, TokenSource } from "./client";
import { AdminQuestion, AdminQuestionDetail, AdminQuestionOption, Topic, Unit } from "./types";

export interface AdminQuestionFilters {
  subject_id?: number;
  validation_status?: string;
  limit?: number;
  offset?: number;
  [key: string]: string | number | boolean | undefined;
}

export function listAdminQuestions(filters: AdminQuestionFilters, token: TokenSource): Promise<AdminQuestion[]> {
  return apiFetch<AdminQuestion[]>("/admin/questions", { token, searchParams: filters });
}

export function getAdminQuestion(id: number, token: TokenSource): Promise<AdminQuestionDetail> {
  return apiFetch<AdminQuestionDetail>(`/admin/questions/${id}`, { token });
}

export interface AdminQuestionUpdateRequest {
  prompt?: string;
  correct_answer?: string;
  difficulty?: number;
  rubric_json?: Record<string, unknown> | null;
  skill_tags?: string[];
  misconception_tags?: string[];
  options?: AdminQuestionOption[];
  explanations?: Array<{ option_label: string | null; explanation: string; misconception_tag?: string | null }>;
}

export function updateAdminQuestion(
  id: number,
  payload: AdminQuestionUpdateRequest,
  token: TokenSource
): Promise<AdminQuestion> {
  return apiFetch<AdminQuestion>(`/admin/questions/${id}`, { method: "PATCH", body: payload, token });
}

export function updateQuestionStatus(
  id: number,
  status: "draft" | "approved" | "rejected" | "needs_review",
  token: TokenSource
): Promise<AdminQuestion> {
  return apiFetch<AdminQuestion>(`/admin/questions/${id}/status`, { method: "POST", body: { status }, token });
}

export function deactivateQuestion(id: number, token: TokenSource): Promise<AdminQuestion> {
  return apiFetch<AdminQuestion>(`/admin/questions/${id}`, { method: "DELETE", token });
}

export function listAdminUnits(subjectId: number, token: TokenSource): Promise<Unit[]> {
  return apiFetch<Unit[]>("/admin/units", { token, searchParams: { subject_id: subjectId } });
}

export function listAdminTopics(unitId: number, token: TokenSource): Promise<Topic[]> {
  return apiFetch<Topic[]>("/admin/topics", { token, searchParams: { unit_id: unitId } });
}
