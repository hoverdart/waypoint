import { render, screen } from "@testing-library/react";
import userEvent from "@testing-library/user-event";
import { describe, expect, it, vi } from "vitest";
import { SubjectPreferences } from "./SubjectPreferences";

const { save } = vi.hoisted(() => ({ save: vi.fn() }));
vi.mock("@/lib/api", () => ({ saveMySubjects: save }));
vi.mock("@/lib/hooks/useApiToken", () => ({ useApiToken: () => "token" }));
vi.mock("next/navigation", () => ({ useRouter: () => ({ refresh: vi.fn() }) }));
const subjects = [{ id: 1, name: "AP Biology", ap_exam_code: "bio", description: null, is_active: true, display_order: 1 }];

describe("SubjectPreferences", () => {
  it("adds a course with edited study time", async () => {
    save.mockResolvedValueOnce([]);
    render(<SubjectPreferences subjects={subjects} enrolled={[]} />);
    await userEvent.click(screen.getByRole("checkbox", { name: "AP Biology" }));
    const minutes = screen.getByLabelText("Daily minutes for AP Biology");
    await userEvent.clear(minutes);
    await userEvent.type(minutes, "35");
    await userEvent.click(screen.getByRole("button", { name: "Save course preferences" }));
    expect(save).toHaveBeenCalledWith([{ subject_id: 1, target_score: 4, exam_date: null, study_minutes_per_day: 35 }], "token");
    expect(await screen.findByRole("status")).toHaveTextContent("saved");
  });
  it("removes a course and retains unsaved changes after failure", async () => {
    save.mockRejectedValueOnce(new Error("offline")).mockResolvedValueOnce([]);
    render(<SubjectPreferences subjects={subjects} enrolled={[{ id: 1, subject_id: 1, target_score: 5, exam_date: null, study_minutes_per_day: 20, is_active: true }]} />);
    await userEvent.click(screen.getByRole("checkbox", { name: "AP Biology" }));
    await userEvent.click(screen.getByRole("button", { name: "Save course preferences" }));
    expect(await screen.findByRole("alert")).toHaveTextContent("try again");
    expect(screen.getByRole("checkbox")).not.toBeChecked();
    await userEvent.click(screen.getByRole("button", { name: "Save course preferences" }));
    expect(save).toHaveBeenLastCalledWith([], "token");
    expect(await screen.findByRole("status")).toHaveTextContent("saved");
  });
});
