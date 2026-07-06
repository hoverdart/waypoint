import { describe, expect, it } from "vitest";
import { render, screen } from "@testing-library/react";
import { MasteryBar } from "./MasteryBar";

describe("MasteryBar", () => {
  it("renders a rounded percentage from a 0-1 mastery score", () => {
    render(<MasteryBar score={0.42} />);
    expect(screen.getByText("42% mastery")).toBeInTheDocument();
  });

  it("rounds to the nearest whole percent", () => {
    render(<MasteryBar score={0.995} />);
    expect(screen.getByText("100% mastery")).toBeInTheDocument();
  });

  it("handles zero mastery", () => {
    render(<MasteryBar score={0} />);
    expect(screen.getByText("0% mastery")).toBeInTheDocument();
  });
});
