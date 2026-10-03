import { fireEvent, render, screen, waitFor } from "@testing-library/react";
import { beforeEach, describe, expect, it, vi } from "vitest";
import { RegenerateTimeBudgetControl } from "./RegenerateTimeBudgetControl";
const { generate, refresh } = vi.hoisted(() => ({ generate: vi.fn(), refresh: vi.fn() }));
vi.mock("next/navigation", () => ({ useRouter: () => ({ refresh }) }));
vi.mock("@/lib/api", () => ({ generateDailyPlan: generate }));
vi.mock("@/lib/hooks/useApiToken", () => ({ useApiToken: () => "token" }));
const subjects = [{ subject_id: 4, subject_name: "AP Biology", mastery_score: 0, predicted_ap_score: 1, exam_date: null, target_score: 5 }];
describe("Adjust daily study time", () => {
  beforeEach(() => vi.resetAllMocks());
  it("updates the chosen course budget and reports preserved work", async () => {
    generate.mockResolvedValue({});
    render(<RegenerateTimeBudgetControl subjects={subjects} />);
    fireEvent.click(screen.getByRole("button", { name: "Adjust today's time" }));
    fireEvent.change(screen.getByLabelText("Time today"), { target: { value: "5" } });
    fireEvent.click(screen.getByRole("button", { name: "Update this course" }));
    await waitFor(() => expect(generate).toHaveBeenCalledWith(4, "token", 5));
    expect(await screen.findByRole("status")).toHaveTextContent("completed work is preserved");
    expect(refresh).toHaveBeenCalled();
  });
  it("keeps controls available after an API failure", async () => {
    generate.mockRejectedValue(new Error("offline"));
    render(<RegenerateTimeBudgetControl subjects={subjects} />);
    fireEvent.click(screen.getByRole("button", { name: "Adjust today's time" }));
    fireEvent.click(screen.getByRole("button", { name: "Update this course" }));
    expect(await screen.findByRole("alert")).toHaveTextContent("Couldn't update");
    expect(screen.getByRole("button", { name: "Update this course" })).toBeEnabled();
  });
});
