import { render, screen } from "@testing-library/react";
import userEvent from "@testing-library/user-event";
import { expect, it, vi } from "vitest";
import { AdminQuestionEditor } from "./AdminQuestionEditor";
import { AdminQuestionDetail } from "@/lib/api";
const { save, replace, status } = vi.hoisted(() => ({ save: vi.fn(), replace: vi.fn(), status: vi.fn() }));
vi.mock("@/lib/api", async original => ({ ...await original<typeof import("@/lib/api")>(), updateAdminQuestion: save, updateQuestionStatus: status }));
vi.mock("@/lib/hooks/useApiToken", () => ({ useApiToken: () => "token" }));
vi.mock("next/navigation", () => ({ useRouter: () => ({ replace, refresh: vi.fn() }) }));
const question: AdminQuestionDetail = { id: 1, subject_id: 1, unit_id: 1, topic_id: 1, type: "mcq", difficulty: 2, prompt: "Question?", correct_answer: "A", rubric_json: null, skill_tags: [], misconception_tags: [], source: "generated", validation_status: "approved", version: 1, is_active: true, created_at: "", updated_at: "", reports: [], options: [{ label: "A", text: "First", is_correct: true }, { label: "B", text: "Second", is_correct: false }] };
it("saves a consistent answer key and navigates to the new version", async () => {
  save.mockResolvedValueOnce({ id: 2 });
  render(<AdminQuestionEditor question={question} />);
  await userEvent.selectOptions(screen.getByLabelText("Correct answer"), "B");
  await userEvent.click(screen.getByRole("button", { name: "Save changes" }));
  expect(save).toHaveBeenCalledWith(1, expect.objectContaining({ correct_answer: "B", options: [{ label: "A", text: "First", is_correct: false }, { label: "B", text: "Second", is_correct: true }] }), "token");
  expect(replace).toHaveBeenCalledWith("/admin/questions/2");
});
it("keeps edits available when saving fails", async () => {
  save.mockRejectedValueOnce(new Error("offline"));
  render(<AdminQuestionEditor question={question} />);
  await userEvent.click(screen.getByRole("button", { name: "Save changes" }));
  expect(await screen.findByRole("alert")).toHaveTextContent("try again");
  expect(screen.getByRole("button", { name: "Save changes" })).toBeEnabled();
});
it("makes archived versions read-only", () => {
  render(<AdminQuestionEditor question={{ ...question, is_active: false }} />);
  expect(screen.getByRole("button", { name: "Save changes" })).toBeDisabled();
});
