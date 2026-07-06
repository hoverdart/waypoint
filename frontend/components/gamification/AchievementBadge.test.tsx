import { describe, expect, it } from "vitest";
import { render, screen } from "@testing-library/react";
import { AchievementBadge } from "./AchievementBadge";

describe("AchievementBadge", () => {
  it("renders the badge's icon, name, and description", () => {
    render(<AchievementBadge badge={{ id: 1, name: "First Steps", description: "Complete your first session.", icon: "🎯" }} />);
    expect(screen.getByText("🎯")).toBeInTheDocument();
    expect(screen.getByText("First Steps")).toBeInTheDocument();
    expect(screen.getByText("Complete your first session.")).toBeInTheDocument();
  });

  it("falls back to a generic medal icon when the badge has none", () => {
    render(<AchievementBadge badge={{ id: 2, name: "Mystery Badge", description: null, icon: null }} />);
    expect(screen.getByText("🏅")).toBeInTheDocument();
  });

  it("omits the description paragraph when the badge has none", () => {
    render(<AchievementBadge badge={{ id: 3, name: "No Description", description: null, icon: "⭐" }} />);
    expect(screen.getByText("No Description")).toBeInTheDocument();
    expect(screen.queryByText("null")).not.toBeInTheDocument();
  });
});
