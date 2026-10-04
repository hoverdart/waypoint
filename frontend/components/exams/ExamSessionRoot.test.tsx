import { act, fireEvent, render, screen, waitFor } from "@testing-library/react";
import { beforeEach, describe, expect, it, vi } from "vitest";
import { ExamSessionRoot } from "./ExamSessionRoot";
import { ExamSession } from "@/lib/api/exams";

const { save, begin, finish, reload, push } = vi.hoisted(() => ({ save: vi.fn(), begin: vi.fn(), finish: vi.fn(), reload: vi.fn(), push: vi.fn() }));
vi.mock("next/navigation", () => ({ useRouter: () => ({ push }) }));
vi.mock("@/lib/hooks/useApiToken", () => ({ useApiToken: () => "token" }));
vi.mock("@/lib/api/exams", () => ({ saveExamDraft: save, beginExamSection: begin, finishExamSection: finish, getExam: reload }));

function exam(overrides: Partial<ExamSession> = {}): ExamSession {
  return { session_id: 5, subject_id: 1, form_id: "form-a", title: "Practice form", time_multiplier: 1,
    server_time: "2026-10-03T12:00:00Z", current_section: 0, completed: false,
    sections: [{ index: 0, title: "Multiple choice", duration_seconds: 3600, question_count: 2,
      score_weight: .45, instructions: "Work through this section.", status: "active",
      started_at: "2026-10-03T12:00:00Z", deadline: "2026-10-03T13:00:00Z", finished_at: null }],
    questions: [1, 2].map(id => ({ id, subject_id: 1, unit_id: 1, topic_id: 1, type: "mcq", difficulty: 3,
      prompt: `Prompt ${id}`, options: [{ id: id * 10, label: "A", text: `Choice ${id}` }] })),
    answers: [], current_index: 0, revision: 0, break_policy: "The clock continues if you leave.", ...overrides };
}

describe("ExamSessionRoot", () => {
  beforeEach(() => vi.resetAllMocks());
  it("restores answers and saves navigation without requiring every answer", async () => {
    const initial = exam({ answers: [{ question_id: 1, selected_option_id: 10 }] });
    save.mockResolvedValue({ ...initial, revision: 1, current_index: 1 });
    render(<ExamSessionRoot initialExam={initial} />);
    expect(screen.getByRole("button", { name: /Choice 1/ })).toHaveAttribute("aria-pressed", "true");
    fireEvent.click(screen.getByRole("button", { name: "Next question" }));
    expect(await screen.findByText("Prompt 2")).toBeVisible();
    expect(save).toHaveBeenCalledWith(5, 0, initial.answers, 1, 0, "token");
  });
  it("keeps a local answer when saving fails and allows retry", async () => {
    save.mockRejectedValueOnce(new Error("offline")).mockResolvedValue(exam({ revision: 1 }));
    render(<ExamSessionRoot initialExam={exam()} />);
    fireEvent.click(screen.getByRole("button", { name: /Choice 1/ }));
    fireEvent.click(screen.getByRole("button", { name: "Save now" }));
    expect(await screen.findByRole("alert")).toHaveTextContent("local answers are still here");
    expect(screen.getByRole("button", { name: /Choice 1/ })).toHaveAttribute("aria-pressed", "true");
    fireEvent.click(screen.getByRole("button", { name: "Save now" }));
    await waitFor(() => expect(screen.queryByRole("alert")).not.toBeInTheDocument());
  });
  it("requires explicit confirmation to close a section and saves dirty answers first", async () => {
    save.mockResolvedValue(exam({ revision: 1 }));
    finish.mockResolvedValue(exam({ completed: true, questions: [] }));
    render(<ExamSessionRoot initialExam={exam()} />);
    fireEvent.click(screen.getByRole("button", { name: /Choice 1/ }));
    fireEvent.click(screen.getByRole("button", { name: "Finish section" }));
    expect(finish).not.toHaveBeenCalled();
    expect(screen.getByText(/1 unanswered. Closing/)).toBeVisible();
    fireEvent.click(screen.getByRole("button", { name: "Save and close section" }));
    await waitFor(() => expect(push).toHaveBeenCalledWith("/practice/results/5"));
    expect(save.mock.invocationCallOrder[0]).toBeLessThan(finish.mock.invocationCallOrder[0]);
  });
  it("locks an expired section and closes only previously saved work", async () => {
    const initial = exam({ server_time: "2026-10-03T13:00:00Z" });
    finish.mockResolvedValue({ ...initial, completed: true, questions: [] });
    render(<ExamSessionRoot initialExam={initial} />);
    expect(screen.getByText("Time is up.")).toBeVisible();
    expect(screen.queryByText("Prompt 1")).not.toBeInTheDocument();
    fireEvent.click(screen.getByRole("button", { name: "Close expired section" }));
    await waitFor(() => expect(finish).toHaveBeenCalledWith(5, 0, "token"));
    expect(save).not.toHaveBeenCalled();
  });
  it("keeps a break untimed until the student starts the next section", async () => {
    const ready = exam();
    ready.sections[0] = { ...ready.sections[0], status: "ready", title: "Free response", deadline: null, started_at: null };
    ready.questions = [];
    begin.mockResolvedValue(exam());
    render(<ExamSessionRoot initialExam={ready} />);
    expect(screen.queryByRole("timer")).not.toBeInTheDocument();
    fireEvent.click(screen.getByRole("button", { name: "Begin Free response" }));
    expect(await screen.findByText("Prompt 1")).toBeVisible();
  });
  it("does not replace edits made while an autosave is in flight", async () => {
    const initial = exam();
    initial.questions = [{ ...initial.questions[0], type: "frq", options: [], scoring_method: "self_review" }];
    let resolve!: (value: ExamSession) => void;
    save.mockReturnValueOnce(new Promise<ExamSession>(done => { resolve = done; }));
    const { unmount } = render(<ExamSessionRoot initialExam={initial} />);
    const field = screen.getByRole("textbox", { name: "Your response" });
    fireEvent.change(field, { target: { value: "First draft" } });
    await waitFor(() => expect(save).toHaveBeenCalledTimes(1), { timeout: 2500 });
    fireEvent.change(field, { target: { value: "Revised while saving" } });
    await act(async () => resolve({ ...initial, revision: 1, answers: [{ question_id: 1, free_response_text: "First draft" }] }));
    expect(field).toHaveValue("Revised while saving");
    expect(screen.getByRole("status")).toHaveTextContent("Unsaved edits");
    unmount();
  });
});
