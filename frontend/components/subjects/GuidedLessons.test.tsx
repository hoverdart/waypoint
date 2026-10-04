import { fireEvent, render, screen, waitFor } from "@testing-library/react";
import { beforeEach, describe, expect, it, vi } from "vitest";
import { GuidedLessons } from "./GuidedLessons";
const { get, check } = vi.hoisted(() => ({ get: vi.fn(), check: vi.fn() }));
vi.mock("@/lib/api/lessons", () => ({ getLessons: get, checkLesson: check }));
vi.mock("@/lib/hooks/useApiToken", () => ({ useApiToken: () => "token" }));
const lesson = { slug: "context", title: "Read the situation", skill: "1.A", objective: "Connect audience and purpose", explanation: ["Look for context."], example: "An original example.", walkthrough: "Here is why it matters.", prompt: "Which purpose?", options: ["Inform", "Request"], revision: 1, completed: false, practice_topic_ids: { mcq: 23, frq: null } };

describe("GuidedLessons", () => {
  beforeEach(() => { vi.clearAllMocks(); get.mockResolvedValue([lesson, { ...lesson, slug: "evidence", title: "Choose evidence" }]); });
  it("teaches, checks, saves completion, and launches practice", async () => {
    const practice = vi.fn();
    check.mockResolvedValueOnce({ correct: false, feedback: "Consider the request." }).mockResolvedValueOnce({ correct: true, feedback: "The audience can act." });
    render(<GuidedLessons unitId={7} onPractice={practice} practiceBusy={false} />);
    fireEvent.click(screen.getByRole("button", { name: "Open guided lessons" }));
    expect(await screen.findByText("Look for context.")).toBeVisible();
    expect(get).toHaveBeenCalledWith(7, "token");
    expect(screen.getByRole("button", { name: "Check understanding" })).toBeDisabled();
    fireEvent.click(screen.getByLabelText("Inform"));
    fireEvent.click(screen.getByRole("button", { name: "Check understanding" }));
    expect(await screen.findByRole("status")).toHaveTextContent("Take another look");
    expect(screen.getByText(/0 of 2 lessons completed/)).toBeVisible();
    fireEvent.click(screen.getByLabelText("Request"));
    fireEvent.click(screen.getByRole("button", { name: "Check understanding" }));
    await waitFor(() => expect(screen.getByRole("status")).toHaveTextContent("Lesson complete"));
    expect(check).toHaveBeenLastCalledWith(7, lesson, 1, "token");
    expect(screen.getByText(/1 of 2 lessons completed/)).toBeVisible();
    fireEvent.click(screen.getByRole("button", { name: "Next lesson" }));
    expect(screen.getByRole("heading", { name: "Choose evidence" })).toBeVisible();
    expect(screen.queryByRole("status")).not.toBeInTheDocument();
    expect(screen.getByRole("button", { name: "Check understanding" })).toBeDisabled();
    fireEvent.click(screen.getByRole("button", { name: "Apply it in practice" }));
    expect(practice).toHaveBeenCalledExactlyOnceWith(23);
  });

  it("does not launch unrelated practice when the chosen format is unavailable", async () => {
    const practice = vi.fn();
    const { rerender } = render(<GuidedLessons unitId={7} onPractice={practice} practiceBusy={false} practiceMode="frq" />);
    fireEvent.click(screen.getByRole("button", { name: "Open guided lessons" }));
    expect(await screen.findByText(/No free-response practice is available/)).toBeVisible();
    expect(screen.getByRole("button", { name: "Apply it in practice" })).toBeDisabled();
    expect(practice).not.toHaveBeenCalled();
    rerender(<GuidedLessons unitId={7} onPractice={practice} practiceBusy={false} practiceMode="mcq" />);
    fireEvent.click(screen.getByRole("button", { name: "Apply it in practice" }));
    expect(practice).toHaveBeenCalledWith(23);
  });
  it("resumes at the first unfinished lesson", async () => {
    get.mockResolvedValue([{ ...lesson, completed: true }, { ...lesson, slug: "next", title: "Next skill" }]);
    render(<GuidedLessons unitId={7} onPractice={vi.fn()} practiceBusy={false} />);
    fireEvent.click(screen.getByRole("button", { name: "Open guided lessons" }));
    expect(await screen.findByRole("heading", { name: "Next skill" })).toBeVisible();
    expect(screen.getByText(/1 of 2 lessons completed/)).toBeVisible();
  });
  it("allows loading retries and retains selection after a failed save", async () => {
    get.mockRejectedValueOnce(new Error("offline"));
    check.mockRejectedValueOnce(new Error("offline"));
    render(<GuidedLessons unitId={7} onPractice={vi.fn()} practiceBusy={false} />);
    fireEvent.click(screen.getByRole("button", { name: "Open guided lessons" }));
    expect(await screen.findByRole("alert")).toHaveTextContent("Couldn't load");
    fireEvent.click(screen.getByRole("button", { name: "Open guided lessons" }));
    fireEvent.click(await screen.findByLabelText("Request"));
    fireEvent.click(screen.getByRole("button", { name: "Check understanding" }));
    expect(await screen.findByRole("alert")).toHaveTextContent("Couldn't save");
    expect(screen.getByLabelText("Request")).toBeChecked();
    expect(screen.getByText(/0 of 2 lessons completed/)).toBeVisible();
  });
});
