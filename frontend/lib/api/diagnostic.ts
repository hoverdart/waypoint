import { apiFetch, TokenSource } from "./client";
import { AnswerInput, DiagnosticStartResponse, DiagnosticSubmitResponse } from "./types";

export function startDiagnostic(subjectId: number, token: TokenSource): Promise<DiagnosticStartResponse> {
  return apiFetch<DiagnosticStartResponse>("/diagnostic/start", {
    method: "POST",
    body: { subject_id: subjectId },
    token,
  });
}

export function submitDiagnostic(
  sessionId: number,
  answers: AnswerInput[],
  token: TokenSource
): Promise<DiagnosticSubmitResponse> {
  return apiFetch<DiagnosticSubmitResponse>(`/diagnostic/${sessionId}/submit`, {
    method: "POST",
    body: { answers },
    token,
  });
}
