import { describe, expect, it, vi } from "vitest";
import { render, screen } from "@testing-library/react";
import userEvent from "@testing-library/user-event";
import { PlanItemCard } from "./PlanItemCard";
import { DailyPlanItem } from "@/lib/api";

const push = vi.fn();

vi.mock("@clerk/nextjs", () => ({
  useAuth: () => ({ getToken: async () => "test-token" }),
}));

vi.mock("next/navigation", () => ({
  useRouter: () => ({ push, refresh: vi.fn() }),
}));

vi.mock("@/lib/api", () => ({
  startPractice: vi.fn().mockResolvedValue({ session_id: 42, session_type: "mcq", questions: [] }),
}));

function makeItem(overrides: Partial<DailyPlanItem> = {}): DailyPlanItem {
  return {
    id: 1,
    subject_id: 1,
    unit_id: 1,
    topic_id: 1,
    item_type: "weakness",
    point_cost: 25,
    priority_score: 1,
    reason: "Your mastery dropped",
    status: "pending",
    ...overrides,
  };
}

describe("PlanItemCard", () => {
  it("shows plain point cost by default", () => {
    render(<PlanItemCard item={makeItem()} topicName="Evidence of Evolution" onSkip={async () => {}} />);
    expect(screen.getByText("25 pts")).toBeInTheDocument();
  });

  it("shows an XP-styled point cost when gamified", () => {
    render(<PlanItemCard item={makeItem()} topicName="Evidence of Evolution" onSkip={async () => {}} gamified />);
    expect(screen.getByText("+25 XP")).toBeInTheDocument();
  });

  it("shows the topic name and reason", () => {
    render(<PlanItemCard item={makeItem()} topicName="Evidence of Evolution" onSkip={async () => {}} />);
    expect(screen.getByText("Evidence of Evolution")).toBeInTheDocument();
    expect(screen.getByText("Your mastery dropped")).toBeInTheDocument();
  });

  it("calls onSkip with the item id when Skip is clicked", async () => {
    const onSkip = vi.fn().mockResolvedValue(undefined);
    const user = userEvent.setup();
    render(<PlanItemCard item={makeItem({ id: 7 })} topicName="Evidence of Evolution" onSkip={onSkip} />);

    await user.click(screen.getByRole("button", { name: "Skip" }));
    expect(onSkip).toHaveBeenCalledWith(7);
  });

  it("navigates to the practice session after starting", async () => {
    const user = userEvent.setup();
    render(<PlanItemCard item={makeItem({ id: 3 })} topicName="Evidence of Evolution" onSkip={async () => {}} />);

    await user.click(screen.getByRole("button", { name: "Start" }));
    expect(push).toHaveBeenCalledWith("/practice/session/42?planItemId=3");
  });

  it("hides Skip/Start and shows the completed status once the item is done", () => {
    render(<PlanItemCard item={makeItem({ status: "completed" })} topicName="Evidence of Evolution" onSkip={async () => {}} />);
    expect(screen.queryByRole("button", { name: "Skip" })).not.toBeInTheDocument();
    expect(screen.queryByRole("button", { name: "Start" })).not.toBeInTheDocument();
    expect(screen.getByText("completed")).toBeInTheDocument();
  });
});
