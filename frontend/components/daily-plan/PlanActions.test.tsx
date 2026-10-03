import { render, screen } from "@testing-library/react";
import userEvent from "@testing-library/user-event";
import { expect, it, vi } from "vitest";
import { PlanItemCard } from "./PlanItemCard";
import { TodaysPlanSummaryCard } from "../dashboard/TodaysPlanSummaryCard";
import { TodaysRouteCard } from "../dashboard/TodaysRouteCard";
import { DailyPlanItem } from "@/lib/api";
const { start } = vi.hoisted(() => ({ start: vi.fn() }));
vi.mock("@/lib/hooks/useStartPlanItem", () => ({ useStartPlanItem: () => start }));
const item: DailyPlanItem = { id: 1, subject_id: 1, unit_id: 1, topic_id: 1, item_type: "review", point_cost: 10, priority_score: 1, reason: "Time to review", status: "pending" };
it("retains a task after skip failure and allows retry", async () => {
  const skip = vi.fn().mockRejectedValueOnce(new Error("offline")).mockResolvedValueOnce(undefined);
  render(<PlanItemCard item={item} topicName="Cells" onSkip={skip} />);
  await userEvent.click(screen.getByRole("button", { name: "Skip" }));
  expect(await screen.findByRole("alert")).toHaveTextContent("try again");
  await userEvent.click(screen.getByRole("button", { name: "Skip" }));
  expect(screen.queryByRole("alert")).not.toBeInTheDocument();
});
it("handles a failed practice launch on the plan page", async () => {
  start.mockRejectedValueOnce(new Error("offline"));
  render(<PlanItemCard item={item} topicName="Cells" onSkip={vi.fn()} />);
  await userEvent.click(screen.getByRole("button", { name: "Start" }));
  expect(await screen.findByRole("alert")).toHaveTextContent("try again");
});
it.each([TodaysPlanSummaryCard, TodaysRouteCard])("handles a failed dashboard launch", async Component => {
  start.mockRejectedValueOnce(new Error("offline"));
  render(<Component plan={{ id: 1, plan_date: "2026-10-03", point_budget: 10, status: "pending", items: [item] }} topicNames={{ 1: "Cells" }} />);
  await userEvent.click(screen.getByRole("button", { name: /Start/ }));
  expect(await screen.findByRole("alert")).toHaveTextContent("try again");
  expect(screen.getByRole("button", { name: /Start/ })).toBeEnabled();
});
