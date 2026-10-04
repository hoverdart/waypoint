import { apiFetch, TokenSource } from "./client";

export interface GuidedLesson {
  slug: string;
  title: string;
  skill: string;
  objective: string;
  explanation: string[];
  example: string;
  example_kind?: "fictional" | "historical";
  walkthrough: string;
  prompt: string;
  options: string[];
  revision: number;
  completed: boolean;
  practice_topic_ids: { mcq: number | null; frq: number | null };
}

export function getLessons(unitId: number, token: TokenSource) {
  return apiFetch<GuidedLesson[]>(`/units/${unitId}/lessons`, { token });
}

export function checkLesson(unitId: number, lesson: GuidedLesson, option: number, token: TokenSource) {
  return apiFetch<{ correct: boolean; feedback: string }>(`/units/${unitId}/lessons/${encodeURIComponent(lesson.slug)}/check`, {
    method: "POST", token, body: { option, revision: lesson.revision },
  });
}
