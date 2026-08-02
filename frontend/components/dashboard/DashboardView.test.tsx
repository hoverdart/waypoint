import { describe, expect, it, vi } from "vitest";
import { render, screen } from "@testing-library/react";
import { DashboardView } from "./DashboardView";
import { Dashboard } from "@/lib/api";

vi.mock("@/lib/hooks/useStartPlanItem", () => ({
  useStartPlanItem: () => vi.fn(),
}));

function makeDashboard(overrides: Partial<Dashboard> = {}): Dashboard {
  return {
    user: {
      id: 1,
      auth_provider_id: "user_1",
      email: "student@example.com",
      display_name: "Ada",
      mode: "professional",
    },
    subjects: [],
    today_plan: null,
    latest_weekly_report: null,
    total_xp: 0,
    streak_days: 0,
    earned_badges: [],
    ...overrides,
  };
}

describe("DashboardView", () => {
  it("renders the professional dashboard when the user's mode is professional", () => {
    render(<DashboardView data={makeDashboard({ user: { ...makeDashboard().user, mode: "professional" } })} />);
    expect(screen.getByText("Welcome back, Ada")).toBeInTheDocument();
    expect(screen.queryByText(/Level \d/)).not.toBeInTheDocument();
  });

  it("renders the gamified dashboard with an XP bar and streak badge when the user's mode is gamified", () => {
    render(
      <DashboardView
        data={makeDashboard({
          user: { ...makeDashboard().user, mode: "gamified" },
          total_xp: 34,
          streak_days: 2,
        })}
      />
    );
    expect(screen.getByText("Let's keep the streak alive.")).toBeInTheDocument();
    expect(screen.getByText(/Level 1/)).toBeInTheDocument();
    expect(screen.getByText(/2-day streak/)).toBeInTheDocument();
  });
});
