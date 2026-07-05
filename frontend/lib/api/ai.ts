import { apiFetch, TokenSource } from "./client";
import { AIExplainResponse, AIUsage, ExplainAction } from "./types";

export interface AIExplainRequest {
  question_id: number;
  action: ExplainAction;
  selected_option_id?: number | null;
  free_response_text?: string | null;
  compare_topic?: string | null;
}

export function explainQuestion(payload: AIExplainRequest, token: TokenSource): Promise<AIExplainResponse> {
  return apiFetch<AIExplainResponse>("/ai/explain", { method: "POST", body: payload, token });
}

export function getAiUsage(token: TokenSource): Promise<AIUsage> {
  return apiFetch<AIUsage>("/ai/usage", { token });
}
