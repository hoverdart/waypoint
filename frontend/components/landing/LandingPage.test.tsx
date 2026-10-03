import { render, screen } from "@testing-library/react";
import { describe, expect, it } from "vitest";
import Home from "@/app/page";
describe("Public course introduction", () => {
  it("renders the study process and all six linked courses without waiting for scroll", () => {
    render(<Home />);
    expect(screen.getByRole("region", { name: "How WayPoint works" })).toBeVisible();
    for (const name of ["AP Calculus AB", "AP Biology", "AP Psychology", "AP US History", "AP Chemistry", "AP Computer Science A"]) {
      expect(screen.getByRole("heading", { name })).toBeVisible();
    }
    expect(screen.getByRole("link", { name: "Create your study plan" })).toHaveAttribute("href", "/signup");
  });
});
