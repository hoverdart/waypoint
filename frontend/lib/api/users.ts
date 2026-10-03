import { apiFetch, TokenSource } from "./client";
import { User, UserMode, UserSubject } from "./types";
import { OnboardingSubjectInput } from "./onboarding";

export interface UserUpdateRequest {
  mode?: UserMode;
  display_name?: string | null;
}

export function getCurrentUser(token: TokenSource): Promise<User> {
  return apiFetch<User>("/users/me", { token });
}

export function updateMe(payload: UserUpdateRequest, token: TokenSource): Promise<User> {
  return apiFetch<User>("/users/me", { method: "PATCH", body: payload, token });
}

export function getMySubjects(token: TokenSource): Promise<UserSubject[]> {
  return apiFetch("/users/me/subjects", { token });
}

export function saveMySubjects(subjects: OnboardingSubjectInput[], token: TokenSource): Promise<UserSubject[]> {
  return apiFetch("/users/me/subjects", { method: "PATCH", body: { subjects }, token });
}
