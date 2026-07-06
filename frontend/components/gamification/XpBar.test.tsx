import { describe, expect, it } from "vitest";
import { render, screen } from "@testing-library/react";
import { XpBar } from "./XpBar";

describe("XpBar", () => {
  it("shows level 1 and full XP-into-level count for a brand new user", () => {
    render(<XpBar totalXp={0} />);
    expect(screen.getByText("Level 1")).toBeInTheDocument();
    expect(screen.getByText(/0\/100 XP · 0 total/)).toBeInTheDocument();
  });

  it("computes the level from total XP using a 100-XP-per-level curve", () => {
    render(<XpBar totalXp={250} />);
    expect(screen.getByText("Level 3")).toBeInTheDocument();
    expect(screen.getByText(/50\/100 XP · 250 total/)).toBeInTheDocument();
  });

  it("rolls over to the next level exactly at a multiple of 100 XP", () => {
    render(<XpBar totalXp={100} />);
    expect(screen.getByText("Level 2")).toBeInTheDocument();
    expect(screen.getByText(/0\/100 XP · 100 total/)).toBeInTheDocument();
  });
});
