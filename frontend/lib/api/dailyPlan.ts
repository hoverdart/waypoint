import { apiFetch, TokenSource } from "./client";
import { DailyPlan, PlanItemStatus } from "./types";

export function generateDailyPlan(subjectId: number, token: TokenSource): Promise<DailyPlan> {
  return apiFetch<DailyPlan>("/daily-plan/generate", {
    method: "POST",
    body: { subject_id: subjectId },
    token,
  });
}

export function getTodayPlan(token: TokenSource): Promise<DailyPlan[]> {
  return apiFetch<DailyPlan[]>("/daily-plan/today", { token });
}

export function updatePlanItem(itemId: number, status: PlanItemStatus, token: TokenSource): Promise<DailyPlan> {
  return apiFetch<DailyPlan>(`/daily-plan/items/${itemId}`, {
    method: "PATCH",
    body: { status },
    token,
  });
}
