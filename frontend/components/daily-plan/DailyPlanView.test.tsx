import { describe, expect, it, vi } from "vitest";
import { render, screen } from "@testing-library/react";
import { DailyPlanView } from "./DailyPlanView";
import { DailyPlan, DashboardSubjectSummary, SubjectDetail } from "@/lib/api";

vi.mock("@clerk/nextjs", () => ({
  useAuth: () => ({ getToken: async () => "test-token" }),
}));

vi.mock("next/navigation", () => ({
  useRouter: () => ({ push: vi.fn(), refresh: vi.fn() }),
}));

const subjectDetail: SubjectDetail = {
  id: 1,
  name: "AP Biology",
  ap_exam_code: "biology",
  description: null,
  is_active: true,
  display_order: 0,
  units: [
    {
      id: 1,
      subject_id: 1,
      name: "Unit 1",
      description: null,
      ap_weight_min: 10,
      ap_weight_max: 15,
      display_order: 0,
      topics: [{ id: 1, unit_id: 1, name: "Evidence of Evolution", description: null, skill_tags: [], display_order: 0 }],
    },
  ],
};

const enrolledSubjects: DashboardSubjectSummary[] = [
  { subject_id: 1, subject_name: "AP Biology", mastery_score: 0.4, predicted_ap_score: 3, exam_date: null, target_score: null },
];

function makePlan(overrides: Partial<DailyPlan> = {}): DailyPlan {
  return {
    id: 1,
    plan_date: "2026-07-05",
    point_budget: 50,
    status: "pending",
    items: [
      {
        id: 1,
        subject_id: 1,
        unit_id: 1,
        topic_id: 1,
        item_type: "weakness",
        point_cost: 25,
        priority_score: 1,
        reason: "Your mastery dropped",
        status: "pending",
      },
    ],
    ...overrides,
  };
}

describe("DailyPlanView", () => {
  it("shows plain point costs with no streak badge in professional mode", () => {
    render(
      <DailyPlanView
        plans={[makePlan()]}
        subjectDetails={[subjectDetail]}
        enrolledSubjects={enrolledSubjects}
        mode="professional"
        streakDays={0}
      />
    );
    expect(screen.getByText("Today's plan")).toBeInTheDocument();
    expect(screen.getByText("25 pts")).toBeInTheDocument();
    expect(screen.queryByText(/streak/)).not.toBeInTheDocument();
  });

  it("shows XP-styled point costs and a streak badge in gamified mode", () => {
    render(
      <DailyPlanView
        plans={[makePlan()]}
        subjectDetails={[subjectDetail]}
        enrolledSubjects={enrolledSubjects}
        mode="gamified"
        streakDays={3}
      />
    );
    expect(screen.getByText("Today's quest")).toBeInTheDocument();
    expect(screen.getByText("+25 XP")).toBeInTheDocument();
    expect(screen.getByText(/3-day streak/)).toBeInTheDocument();
    expect(screen.getByText("+25 XP available today")).toBeInTheDocument();
  });

  it("shows an empty state with a generate-plan button when there is no plan yet", () => {
    render(
      <DailyPlanView
        plans={[]}
        subjectDetails={[subjectDetail]}
        enrolledSubjects={enrolledSubjects}
        mode="professional"
        streakDays={0}
      />
    );
    expect(screen.getByText("No plan generated yet for today.")).toBeInTheDocument();
    expect(screen.getByRole("button", { name: /Generate today's plan/i })).toBeInTheDocument();
  });
});
