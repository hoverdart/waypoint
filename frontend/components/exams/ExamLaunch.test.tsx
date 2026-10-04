import { fireEvent, render, screen, waitFor } from "@testing-library/react";
import { beforeEach, describe, expect, it, vi } from "vitest";
import { ExamLaunch } from "./ExamLaunch";

const { forms, start, push } = vi.hoisted(() => ({ forms: vi.fn(), start: vi.fn(), push: vi.fn() }));
vi.mock("next/navigation", () => ({ useRouter: () => ({ push }) }));
vi.mock("@/lib/hooks/useApiToken", () => ({ useApiToken: () => "token" }));
vi.mock("@/lib/api/exams", () => ({ getExamForms: forms, startExam: start }));
const available = [{ form_id: "form-a", title: "English Language · Form A", source_url: "https://apcentral.collegeboard.org", available: true,
  sections: [{ title: "Multiple choice", duration_seconds: 3600, question_count: 45, score_weight: .45, instructions: "" }] }];

describe("ExamLaunch", () => {
  beforeEach(() => vi.resetAllMocks());
  it("starts the chosen form with the selected practice time allowance", async () => {
    forms.mockResolvedValue(available); start.mockResolvedValue({ session_id: 9 });
    render(<ExamLaunch subjectId={1} />);
    const button = await screen.findByRole("button", { name: "Start Form A" });
    fireEvent.change(screen.getByRole("combobox"), { target: { value: "1.5" } });
    fireEvent.click(button);
    await waitFor(() => expect(push).toHaveBeenCalledWith("/exams/9"));
    expect(start).toHaveBeenCalledWith(1, "form-a", 1.5, "token");
  });
  it("offers recovery when catalog loading fails", async () => {
    forms.mockRejectedValueOnce(new Error("offline")).mockResolvedValue(available);
    render(<ExamLaunch subjectId={1} />);
    expect(await screen.findByRole("alert")).toHaveTextContent("Couldn't load exam forms");
    fireEvent.click(screen.getByRole("button", { name: "Reload forms" }));
    expect(await screen.findByRole("button", { name: "Start Form A" })).toBeEnabled();
  });
  it("does not offer an incomplete form as a shortened exam", async () => {
    forms.mockResolvedValue([{ ...available[0], available: false }]);
    render(<ExamLaunch subjectId={1} />);
    expect(await screen.findByRole("button", { name: "Content being updated" })).toBeDisabled();
  });
});
