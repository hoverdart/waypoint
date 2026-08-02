import { describe, expect, it, vi } from "vitest";
import { render, screen } from "@testing-library/react";
import userEvent from "@testing-library/user-event";
import { McqQuestionForm } from "./McqQuestionForm";
import { Question } from "@/lib/api";

const question: Question = {
  id: 1,
  subject_id: 1,
  unit_id: 1,
  topic_id: 1,
  type: "mcq",
  difficulty: 2,
  prompt: "Find lim(x->2) (x^2 - 4)/(x - 2).",
  options: [
    { id: 10, label: "A", text: "0" },
    { id: 11, label: "B", text: "4" },
    { id: 12, label: "C", text: "the limit does not exist" },
    { id: 13, label: "D", text: "2" },
  ],
};

describe("McqQuestionForm", () => {
  it("renders every option's label and text", () => {
    render(<McqQuestionForm question={question} selectedOptionId={null} onSelect={() => {}} />);
    for (const option of question.options) {
      expect(screen.getByText(option.text)).toBeInTheDocument();
    }
  });

  it("calls onSelect with the clicked option's id", async () => {
    const onSelect = vi.fn();
    const user = userEvent.setup();
    render(<McqQuestionForm question={question} selectedOptionId={null} onSelect={onSelect} />);

    await user.click(screen.getByText("4"));
    expect(onSelect).toHaveBeenCalledWith(11);
  });

  // Asserted through aria-pressed rather than a class name: that's the part
  // of "marked as selected" that's actually contractual, and it survives a
  // restyle of the selected-state colours.
  it("marks the currently selected option as pressed", () => {
    render(<McqQuestionForm question={question} selectedOptionId={12} onSelect={() => {}} />);
    expect(screen.getByText("the limit does not exist").closest("button")).toHaveAttribute("aria-pressed", "true");
    expect(screen.getByText("0").closest("button")).toHaveAttribute("aria-pressed", "false");
  });
});
