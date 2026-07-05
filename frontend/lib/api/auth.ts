import { apiFetch, TokenSource } from "./client";
import { User } from "./types";

export function syncUser(token: TokenSource): Promise<User> {
  return apiFetch<User>("/auth/sync-user", { method: "POST", token });
}
