import { apiFetch, TokenSource } from "./client";
import { Dashboard } from "./types";

export function getDashboard(token: TokenSource): Promise<Dashboard> {
  return apiFetch<Dashboard>("/dashboard", { token });
}
