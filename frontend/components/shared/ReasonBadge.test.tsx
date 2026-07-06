import { describe, expect, it } from "vitest";
import { render, screen } from "@testing-library/react";
import { ReasonBadge } from "./ReasonBadge";

describe("ReasonBadge", () => {
  it("renders the given reason text verbatim", () => {
    render(<ReasonBadge reason="Your mastery dropped" />);
    expect(screen.getByText("Your mastery dropped")).toBeInTheDocument();
  });
});
