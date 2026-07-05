import { apiFetch, TokenSource } from "./client";
import { SubjectMastery } from "./types";

export function getSubjectMastery(subjectId: number, token: TokenSource): Promise<SubjectMastery> {
  return apiFetch<SubjectMastery>(`/mastery/subject/${subjectId}`, { token });
}
