import { render, screen } from "@testing-library/react";
import { describe, expect, it } from "vitest";
import { Hero } from "./Hero";
describe("Landing introduction", () => {
  it("provides a real signup link and labels the illustrative plan", () => {
    render(<Hero />);
    expect(screen.getByRole("heading", { level: 1 })).toHaveTextContent("Big ambitions.");
    expect(screen.getByRole("link", { name: "Find your starting point" })).toHaveAttribute("href", "/signup");
    expect(screen.getByText("An example day")).toBeInTheDocument();
    expect(screen.getByRole("link", { name: "Explore the courses ↓" })).toHaveAttribute("href", "#courses");
  });
});
