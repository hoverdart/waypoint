import { describe, expect, it } from "vitest";
import { render, screen } from "@testing-library/react";
import { ResultsView } from "./ResultsView";
import { PracticeResultsResponse } from "@/lib/api";

function makeResults(overrides: Partial<PracticeResultsResponse> = {}): PracticeResultsResponse {
  return {
    session_id: 1,
    session_type: "mcq",
    correct_count: 1,
    total_questions: 1,
    score: 1,
    breakdown: [],
    xp_earned: 12,
    newly_earned_badges: [],
    ...overrides,
  };
}

describe("ResultsView", () => {
  it.each(["professional", "gamified"] as const)("does not present ungraded essays as failed answers in %s mode", mode => {
    render(<ResultsView mode={mode} results={makeResults({ session_type: "frq", total_questions: 3, correct_count: 0, graded_count: 0, self_review_count: 3, score: 0 })} />);
    expect(screen.getByText("Time to reflect")).toBeVisible();
    expect(screen.queryByText(/0% correct/)).not.toBeInTheDocument();
    expect(screen.getByText(/excluded from automatic accuracy/)).toBeVisible();
  });

  it("shows the plain score summary with no XP or badges in professional mode", () => {
    render(<ResultsView results={makeResults()} mode="professional" />);
    expect(screen.getByText("Session complete")).toBeInTheDocument();
    expect(screen.queryByText(/XP earned/)).not.toBeInTheDocument();
  });

  it("shows XP earned in gamified mode", () => {
    render(<ResultsView results={makeResults({ xp_earned: 12 })} mode="gamified" />);
    expect(screen.getByText(/\+12 XP earned/)).toBeInTheDocument();
  });

  it("surfaces newly earned badges in gamified mode", () => {
    render(
      <ResultsView
        results={makeResults({
          newly_earned_badges: [{ id: 1, name: "First Steps", description: "Complete your first session.", icon: "🎯" }],
        })}
        mode="gamified"
      />
    );
    expect(screen.getByText("New badge unlocked!")).toBeInTheDocument();
    expect(screen.getByText("First Steps")).toBeInTheDocument();
  });

  it("pluralizes the badge-unlock heading when multiple badges are earned", () => {
    render(
      <ResultsView
        results={makeResults({
          newly_earned_badges: [
            { id: 1, name: "First Steps", description: null, icon: "🎯" },
            { id: 2, name: "On Fire", description: null, icon: "🔥" },
          ],
        })}
        mode="gamified"
      />
    );
    expect(screen.getByText("New badges unlocked!")).toBeInTheDocument();
  });

  it("labels a diagnostic session as baseline established instead of session complete", () => {
    render(<ResultsView results={makeResults({ session_type: "diagnostic" })} mode="professional" />);
    expect(screen.getByText("Baseline established")).toBeInTheDocument();
  });
});
