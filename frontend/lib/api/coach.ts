import { apiFetch, TokenSource } from "./client";
import { WeeklyCoachReport } from "./types";

export function getLatestWeeklyReport(token: TokenSource): Promise<WeeklyCoachReport> {
  return apiFetch<WeeklyCoachReport>("/coach-report/weekly/latest", { token });
}
