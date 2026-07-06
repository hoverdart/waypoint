import { describe, expect, it } from "vitest";
import { render, screen } from "@testing-library/react";
import { AchievementBadgeGrid } from "./AchievementBadgeGrid";

describe("AchievementBadgeGrid", () => {
  it("shows an empty-state message when no badges have been earned", () => {
    render(<AchievementBadgeGrid badges={[]} />);
    expect(screen.getByText(/No badges yet/)).toBeInTheDocument();
  });

  it("renders one AchievementBadge per earned badge", () => {
    render(
      <AchievementBadgeGrid
        badges={[
          { id: 1, name: "First Steps", description: null, icon: "🎯" },
          { id: 2, name: "On Fire", description: null, icon: "🔥" },
        ]}
      />
    );
    expect(screen.getByText("First Steps")).toBeInTheDocument();
    expect(screen.getByText("On Fire")).toBeInTheDocument();
  });
});
