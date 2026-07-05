import { apiFetch } from "./client";
import { Subject, SubjectDetail } from "./types";

export function getSubjects(): Promise<Subject[]> {
  return apiFetch<Subject[]>("/subjects");
}

export function getSubject(id: number): Promise<SubjectDetail> {
  return apiFetch<SubjectDetail>(`/subjects/${id}`);
}
