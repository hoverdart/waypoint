import { apiFetch, TokenSource } from "./client";
import {
  AnswerInput,
  PracticeResultsResponse,
  PracticeSessionDetail,
  PracticeStartResponse,
  PracticeSubmitResponse,
  QuestionType,
} from "./types";

export interface PracticeStartRequest {
  subject_id: number;
  unit_id?: number | null;
  topic_id?: number | null;
  session_type?: QuestionType | "timed";
  question_count?: number;
}

export function startPractice(payload: PracticeStartRequest, token: TokenSource): Promise<PracticeStartResponse> {
  return apiFetch<PracticeStartResponse>("/practice/start", { method: "POST", body: payload, token });
}

export function submitPractice(
  sessionId: number,
  answers: AnswerInput[],
  token: TokenSource,
  dailyPlanItemId?: number
): Promise<PracticeSubmitResponse> {
  return apiFetch<PracticeSubmitResponse>(`/practice/${sessionId}/submit`, {
    method: "POST",
    body: { answers, daily_plan_item_id: dailyPlanItemId ?? null },
    token,
  });
}

export function getPracticeResults(sessionId: number, token: TokenSource): Promise<PracticeResultsResponse> {
  return apiFetch<PracticeResultsResponse>(`/practice/${sessionId}/results`, { token });
}

export function getPracticeSession(sessionId: number, token: TokenSource): Promise<PracticeSessionDetail> {
  return apiFetch<PracticeSessionDetail>(`/practice/${sessionId}`, { token });
}
