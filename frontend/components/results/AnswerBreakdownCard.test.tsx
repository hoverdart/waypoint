import { describe, expect, it, vi } from "vitest";
import { render, screen } from "@testing-library/react";
import userEvent from "@testing-library/user-event";
import { AnswerBreakdownCard } from "./AnswerBreakdownCard";
import { AnswerBreakdownItem } from "@/lib/api";

const { start } = vi.hoisted(() => ({ start: vi.fn() }));
vi.mock("@/lib/hooks/useStartPlanItem", () => ({ useStartPlanItem: () => start }));
vi.mock("@/components/shared/ExplainButton", () => ({ ExplainButton: () => null }));

const item: AnswerBreakdownItem = {
  question_id: 1, topic_id: 1, prompt: "What happens next?", type: "mcq",
  is_correct: false, score: 0, max_score: 1, correct_answer: "B",
  selected_option_id: 1, free_response_text: null, explanations: [],
  options: [{ id: 1, label: "A", text: "Energy disappears" }, { id: 2, label: "B", text: "Energy transfers" }],
};

describe("AnswerBreakdownCard", () => {
  it("shows the student's choice and complete correct answer", () => {
    render(<AnswerBreakdownCard item={item} />);
    expect(screen.getByText("A. Energy disappears")).toBeVisible();
    expect(screen.getByText("B. Energy transfers")).toBeVisible();
  });
  it("does not attribute another option's misconception to the student", () => {
    render(<AnswerBreakdownCard item={{ ...item, explanations: [{ option_id: 2, explanation: "Other choice", misconception_tag: "unrelated misconception" }] }} />);
    expect(screen.queryByText(/unrelated misconception/)).not.toBeInTheDocument();
  });
  it("shows the FRQ response, model, rubric, and scoring limitation", () => {
    render(<AnswerBreakdownCard item={{ ...item, type: "frq", free_response_text: "My reasoning", correct_answer: "Model reasoning", rubric: [{ point: "Explain the mechanism", points: 2 }] }} />);
    expect(screen.getByText("My reasoning")).toBeVisible();
    expect(screen.getByText("Model reasoning")).toBeVisible();
    expect(screen.getByText("Explain the mechanism")).toBeVisible();
    expect(screen.getByText(/automated score checks keywords/)).toBeVisible();
    expect(screen.queryByText("Incorrect")).not.toBeInTheDocument();
  });
  it("allows retry after a similar-question launch fails", async () => {
    start.mockRejectedValueOnce(new Error("offline")).mockResolvedValueOnce(undefined);
    render(<AnswerBreakdownCard item={item} subjectId={1} />);
    const button = screen.getByRole("button", { name: "Try another similar question" });
    await userEvent.click(button);
    expect(await screen.findByRole("alert")).toHaveTextContent("Please try again");
    await userEvent.click(button);
    expect(screen.queryByRole("alert")).not.toBeInTheDocument();
  });
});
