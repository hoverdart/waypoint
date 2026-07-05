import { apiFetch, TokenSource } from "./client";
import { QuestionReport } from "./types";

export interface QuestionReportRequest {
  reason: string;
  details?: string | null;
}

export function reportQuestion(
  questionId: number,
  payload: QuestionReportRequest,
  token: TokenSource
): Promise<QuestionReport> {
  return apiFetch<QuestionReport>(`/questions/${questionId}/report`, { method: "POST", body: payload, token });
}
