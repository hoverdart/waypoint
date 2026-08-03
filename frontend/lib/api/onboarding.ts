import { apiFetch, TokenSource } from "./client";
import { DiagnosticStatus, OnboardingStep, User, UserMode, UserSubject } from "./types";

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

/**
 * Contract owned by the backend onboarding workstream. The state endpoint
 * allows the frontend to resume a partially completed onboarding flow without
 * retaining student profile or course choices in browser storage.
 */
export interface OnboardingState {
  user: User;
  user_subjects: UserSubject[];
  onboarding_step: OnboardingStep;
  diagnostic_status: DiagnosticStatus;
}

export interface SaveOnboardingDraftRequest {
  display_name?: string;
  grade_level?: number;
  subjects?: OnboardingSubjectInput[];
  onboarding_step: Exclude<OnboardingStep, "complete">;
  diagnostic_status?: DiagnosticStatus;
}

export interface CompleteOnboardingRequest {
  mode: UserMode;
  diagnostic_status: DiagnosticStatus;
}

export function submitOnboarding(payload: OnboardingRequest, token: TokenSource): Promise<OnboardingResponse> {
  return apiFetch<OnboardingResponse>("/onboarding", { method: "POST", body: payload, token });
}

export function getOnboardingState(token: TokenSource): Promise<OnboardingState> {
  return apiFetch<OnboardingState>("/onboarding", { token });
}

export function saveOnboardingDraft(
  payload: SaveOnboardingDraftRequest,
  token: TokenSource
): Promise<OnboardingState> {
  return apiFetch<OnboardingState>("/onboarding", { method: "PATCH", body: payload, token });
}

export function completeOnboarding(
  payload: CompleteOnboardingRequest,
  token: TokenSource
): Promise<OnboardingState> {
  return apiFetch<OnboardingState>("/onboarding/complete", { method: "POST", body: payload, token });
}
