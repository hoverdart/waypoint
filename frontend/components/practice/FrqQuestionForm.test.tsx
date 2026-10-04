import { describe, expect, it, vi } from "vitest";
import { render, screen } from "@testing-library/react";
import userEvent from "@testing-library/user-event";
import { FrqQuestionForm } from "./FrqQuestionForm";

describe("FrqQuestionForm", () => {
  it("provides an accessible response field and accurate word/character counts", () => {
    render(<FrqQuestionForm value={"A clear\nargument"} onChange={vi.fn()} />);
    const field = screen.getByRole("textbox", { name: "Your response" });
    expect(field).toHaveAttribute("maxlength", "20000");
    expect(field).toHaveAccessibleDescription("3 words · 16 / 20,000 characters");
  });
  it("reports edits and treats whitespace as zero words", async () => {
    const changed = vi.fn();
    render(<FrqQuestionForm value=" " onChange={changed} />);
    expect(screen.getByText("0 words · 1 / 20,000 characters")).toBeVisible();
    await userEvent.type(screen.getByRole("textbox"), "x");
    expect(changed).toHaveBeenCalledWith(" x");
  });
});
