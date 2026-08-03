import { apiFetch, TokenSource } from "./client";
import { User, UserMode } from "./types";

export interface UserUpdateRequest {
  mode?: UserMode;
  display_name?: string | null;
  grade_level?: number | null;
}

export function getCurrentUser(token: TokenSource): Promise<User> {
  return apiFetch<User>("/users/me", { token });
}

export function updateMe(payload: UserUpdateRequest, token: TokenSource): Promise<User> {
  return apiFetch<User>("/users/me", { method: "PATCH", body: payload, token });
}
