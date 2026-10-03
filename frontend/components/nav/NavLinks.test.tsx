import { render, screen } from "@testing-library/react";
import { describe, expect, it, vi } from "vitest";
import { NavLinks } from "./NavLinks";
vi.mock("next/navigation", () => ({ usePathname: () => "/subjects/1" }));
describe("Navigation", () => {
  it("marks nested course pages active", () => {
    render(<NavLinks />);
    expect(screen.getByRole("link", { name: "Courses" })).toHaveAttribute("aria-current", "page");
    expect(screen.getByRole("link", { name: "Dashboard" })).not.toHaveAttribute("aria-current");
  });
  it("makes every primary destination and settings available on mobile", () => {
    render(<NavLinks mobile />);
    expect(screen.getByRole("navigation", { name: "Mobile navigation" })).toBeInTheDocument();
    expect(screen.getAllByRole("link")).toHaveLength(6);
    expect(screen.getByRole("link", { name: "Settings" })).toHaveAttribute("href", "/settings");
  });
});
