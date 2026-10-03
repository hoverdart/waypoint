import { describe, expect, it, vi } from "vitest";
import { render, screen } from "@testing-library/react";
import userEvent from "@testing-library/user-event";
import { RubricSelfReview } from "./RubricSelfReview";
import { AnswerBreakdownItem } from "@/lib/api";

const { save } = vi.hoisted(() => ({ save: vi.fn() }));
vi.mock("@/lib/api", () => ({ saveSelfReview: save }));
vi.mock("@/lib/hooks/useApiToken", () => ({ useApiToken: () => "token" }));
const item: AnswerBreakdownItem = {
  question_id: 9, topic_id: 1, prompt: "Argument", type: "frq", is_correct: false,
  score: 0, max_score: 1, correct_answer: "Example", selected_option_id: null,
  free_response_text: "My response", explanations: [], scoring_method: "self_review",
  rubric: [{ point: "Thesis", points: 1, levels: ["No position", "Defensible position"] }],
};

describe("RubricSelfReview", () => {
  it("requires a deliberate choice and preserves it on a failed save", async () => {
    save.mockRejectedValueOnce(new Error("offline")).mockResolvedValueOnce({ points: [1], total: 1 });
    render(<RubricSelfReview item={item} sessionId={3} />);
    const button = screen.getByRole("button", { name: "Save rubric review" });
    expect(button).toBeDisabled();
    await userEvent.click(screen.getByRole("radio", { name: /Defensible position/ }));
    await userEvent.click(button);
    expect(await screen.findByRole("alert")).toHaveTextContent("please retry");
    expect(screen.getByRole("radio", { name: /Defensible position/ })).toBeChecked();
    await userEvent.click(button);
    expect(await screen.findByRole("status")).toHaveTextContent("1/1 points");
    expect(save).toHaveBeenLastCalledWith(3, 9, [1], "token");
  });
  it("restores a saved review and lets the student revise it", async () => {
    render(<RubricSelfReview item={{ ...item, self_review: { points: [1], total: 1, reviewed_at: "2026-10-03" } }} sessionId={3} />);
    expect(screen.getByRole("radio", { name: /Defensible position/ })).toBeChecked();
    await userEvent.click(screen.getByRole("radio", { name: /No position/ }));
    expect(screen.queryByRole("status")).not.toBeInTheDocument();
    expect(screen.getByText(/does not change mastery/)).toBeVisible();
  });
});
