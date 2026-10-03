import { fireEvent, render, screen, waitFor } from "@testing-library/react";
import { beforeEach, describe, expect, it, vi } from "vitest";
import { PracticeSessionRoot } from "./PracticeSessionRoot";
import type { Question } from "@/lib/api";
const { save, submit, diagnostic, push } = vi.hoisted(() => ({ save: vi.fn(), submit: vi.fn(), diagnostic: vi.fn(), push: vi.fn() }));
vi.mock("next/navigation", () => ({ useRouter: () => ({ push }) }));
vi.mock("@/lib/hooks/useApiToken", () => ({ useApiToken: () => "token" }));
vi.mock("@/components/shared/ReportQuestionDialog", () => ({ ReportQuestionDialog: () => null }));
vi.mock("@/lib/api", async importOriginal => ({ ...await importOriginal<object>(), savePracticeDraft: save, submitPractice: submit, submitDiagnostic: diagnostic }));
const questions: Question[] = [1, 2].map(id => ({ id, subject_id: 1, unit_id: 1, topic_id: 1, type: "mcq", difficulty: 2, prompt: `Question ${id}`, options: [{ id: id * 10, label: "A", text: `Answer ${id}` }] }));
describe("Saved practice", () => {
  beforeEach(() => { vi.resetAllMocks(); save.mockResolvedValue(undefined); submit.mockResolvedValue({}); });
  it("saves on next and allows returning to the selected answer", async () => {
    render(<PracticeSessionRoot sessionId={7} sessionType="mcq" questions={questions} />);
    fireEvent.click(screen.getByRole("button", { name: /Answer 1/ }));
    fireEvent.click(screen.getByRole("button", { name: "Next" }));
    expect(await screen.findByText("Question 2")).toBeInTheDocument();
    expect(save).toHaveBeenCalledWith(7, expect.arrayContaining([expect.objectContaining({ question_id: 1, selected_option_id: 10 })]), 1, "token", undefined);
    fireEvent.click(screen.getByRole("button", { name: "Back" }));
    await waitFor(() => expect(screen.getByRole("button", { name: /Answer 1/ })).toHaveAttribute("aria-pressed", "true"));
  });
  it("restores server drafts and saves before exit", async () => {
    render(<PracticeSessionRoot sessionId={7} sessionType="mcq" questions={questions} initialIndex={1} initialAnswers={[{ question_id: 2, selected_option_id: 20, time_seconds: 8 }]} />);
    expect(screen.getByRole("button", { name: /Answer 2/ })).toHaveAttribute("aria-pressed", "true");
    fireEvent.click(screen.getByRole("button", { name: "Save & exit" }));
    await waitFor(() => expect(push).toHaveBeenCalledWith("/practice"));
    expect(save).toHaveBeenCalled();
  });
  it("keeps answers and current position after a failed save", async () => {
    save.mockRejectedValue(new Error("offline"));
    render(<PracticeSessionRoot sessionId={7} sessionType="mcq" questions={questions} />);
    fireEvent.click(screen.getByRole("button", { name: /Answer 1/ }));
    fireEvent.click(screen.getByRole("button", { name: "Next" }));
    expect(await screen.findByRole("alert")).toHaveTextContent("couldn't save");
    expect(screen.getByRole("button", { name: /Answer 1/ })).toHaveAttribute("aria-pressed", "true");
    expect(push).not.toHaveBeenCalled();
  });
  it("allows retrying a failed submission without losing answers", async () => {
    submit.mockRejectedValueOnce(new Error("offline")).mockResolvedValueOnce({});
    render(<PracticeSessionRoot sessionId={7} sessionType="mcq" questions={[questions[0]]} />);
    fireEvent.click(screen.getByRole("button", { name: /Answer 1/ }));
    fireEvent.click(screen.getByRole("button", { name: "Finish" }));
    expect(await screen.findByRole("alert")).toHaveTextContent("could not submit");
    fireEvent.click(screen.getByRole("button", { name: "Finish" }));
    await waitFor(() => expect(push).toHaveBeenCalledWith("/practice/results/7"));
  });
});
