import { apiFetch, TokenSource } from "./client";
import { AnswerInput, Question } from "./types";

export interface ExamSectionSummary {
  title: string;
  duration_seconds: number;
  question_count: number;
  score_weight: number;
  instructions: string;
}
export interface ExamForm {
  form_id: string;
  title: string;
  source_url: string;
  available: boolean;
  sections: ExamSectionSummary[];
}
export interface ExamSession {
  session_id: number;
  subject_id: number;
  form_id: string;
  title: string;
  time_multiplier: number;
  server_time: string;
  current_section: number;
  completed: boolean;
  sections: (ExamSectionSummary & { index: number; status: "ready" | "active" | "expired" | "finished"; started_at: string | null; deadline: string | null; finished_at: string | null })[];
  questions: Question[];
  answers: AnswerInput[];
  current_index: number;
  revision: number;
  break_policy: string;
}
export function getExamForms(subjectId: number, token: TokenSource) {
  return apiFetch<ExamForm[]>(`/exams/subjects/${subjectId}`, { token });
}
export function startExam(subjectId: number, formId: string, timeMultiplier: number, token: TokenSource) {
  return apiFetch<ExamSession>("/exams/start", { method: "POST", token, body: { subject_id: subjectId, form_id: formId, time_multiplier: timeMultiplier } });
}
export function getExam(sessionId: number, token: TokenSource) {
  return apiFetch<ExamSession>(`/exams/${sessionId}`, { token });
}
export function saveExamDraft(sessionId: number, section: number, answers: AnswerInput[], index: number, revision: number, token: TokenSource) {
  return apiFetch<ExamSession>(`/exams/${sessionId}/sections/${section}/draft`, { method: "PUT", token, body: { answers, current_index: index, expected_revision: revision } });
}
export function beginExamSection(sessionId: number, section: number, token: TokenSource) {
  return apiFetch<ExamSession>(`/exams/${sessionId}/sections/${section}/start`, { method: "POST", token });
}
export function finishExamSection(sessionId: number, section: number, token: TokenSource) {
  return apiFetch<ExamSession>(`/exams/${sessionId}/sections/${section}/finish`, { method: "POST", token });
}
