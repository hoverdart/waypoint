import { render, screen } from "@testing-library/react";
import { describe, expect, it, vi } from "vitest";
import { PracticeHistory } from "./PracticeHistory";
vi.mock("@/lib/hooks/useApiToken", () => ({ useApiToken: () => "token" }));
const session = { session_id: 9, subject_id: 1, subject_name: "AP Biology", session_type: "mcq", started_at: "2026-10-03T12:00:00", completed_at: null, total_questions: 10, correct_count: 0, score: 0, answered_count: 3 };
describe("Practice notebook", () => {
  it("links newcomers to courses", () => {
    render(<PracticeHistory initialSessions={[]} />);
    expect(screen.getByRole("link", { name: "Choose a course" })).toHaveAttribute("href", "/subjects");
  });
  it("links unfinished sessions to resume and completed sessions to review", () => {
    render(<PracticeHistory initialSessions={[session, { ...session, session_id: 10, completed_at: "2026-10-03T12:30:00", correct_count: 8, score: 0.8 }]} />);
    expect(screen.getByRole("link", { name: "Resume session" })).toHaveAttribute("href", "/practice/session/9");
    expect(screen.getByRole("link", { name: "Review answers" })).toHaveAttribute("href", "/practice/results/10");
    expect(screen.getByText("3 of 10 questions saved")).toBeInTheDocument();
  });
});
