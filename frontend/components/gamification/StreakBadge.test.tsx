import { describe, expect, it } from "vitest";
import { render, screen } from "@testing-library/react";
import { StreakBadge } from "./StreakBadge";

describe("StreakBadge", () => {
  it("prompts the user to start a streak when days is zero", () => {
    render(<StreakBadge days={0} />);
    expect(screen.getByText(/Start a streak today/)).toBeInTheDocument();
  });

  it("shows the current streak count when days is positive", () => {
    render(<StreakBadge days={5} />);
    expect(screen.getByText(/5-day streak/)).toBeInTheDocument();
  });

  it("handles a 1-day streak without a plural mismatch reading oddly", () => {
    render(<StreakBadge days={1} />);
    expect(screen.getByText(/1-day streak/)).toBeInTheDocument();
  });
});
