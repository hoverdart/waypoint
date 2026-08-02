import { describe, expect, it, vi } from "vitest";
import { render, screen } from "@testing-library/react";
import userEvent from "@testing-library/user-event";
import { ConfidenceRatingInput } from "./ConfidenceRatingInput";

describe("ConfidenceRatingInput", () => {
  it("renders all four confidence levels", () => {
    render(<ConfidenceRatingInput value={null} onChange={() => {}} />);
    expect(screen.getByRole("button", { name: "Guessed" })).toBeInTheDocument();
    expect(screen.getByRole("button", { name: "Unsure" })).toBeInTheDocument();
    expect(screen.getByRole("button", { name: "Fairly sure" })).toBeInTheDocument();
    expect(screen.getByRole("button", { name: "Confident" })).toBeInTheDocument();
  });

  it("calls onChange with the selected level's numeric value", async () => {
    const onChange = vi.fn();
    const user = userEvent.setup();
    render(<ConfidenceRatingInput value={null} onChange={onChange} />);

    await user.click(screen.getByRole("button", { name: "Confident" }));
    expect(onChange).toHaveBeenCalledWith(4);

    await user.click(screen.getByRole("button", { name: "Guessed" }));
    expect(onChange).toHaveBeenCalledWith(1);
  });

  // Asserted through aria-pressed rather than a class name: that's the part
  // of "marked as selected" that's actually contractual, and it survives a
  // restyle of the selected-state colours.
  it("marks the currently selected level as pressed", () => {
    render(<ConfidenceRatingInput value={3} onChange={() => {}} />);
    expect(screen.getByRole("button", { name: "Fairly sure" })).toHaveAttribute("aria-pressed", "true");
    expect(screen.getByRole("button", { name: "Guessed" })).toHaveAttribute("aria-pressed", "false");
  });
});
