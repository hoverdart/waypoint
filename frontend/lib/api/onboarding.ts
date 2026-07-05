import { apiFetch, TokenSource } from "./client";
import { User, UserMode, UserSubject } from "./types";

export interface OnboardingSubjectInput {
  subject_id: number;
  target_score?: number | null;
  exam_date?: string | null;
  study_minutes_per_day: number;
}

export interface OnboardingRequest {
  mode: UserMode;
  subjects: OnboardingSubjectInput[];
}

export interface OnboardingResponse {
  user: User;
  user_subjects: UserSubject[];
}

export function submitOnboarding(payload: OnboardingRequest, token: TokenSource): Promise<OnboardingResponse> {
  return apiFetch<OnboardingResponse>("/onboarding", { method: "POST", body: payload, token });
}
