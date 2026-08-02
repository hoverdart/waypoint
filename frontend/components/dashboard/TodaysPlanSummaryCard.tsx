import { Surface } from "@/components/kit/Surface";
import { PillLink } from "@/components/kit/PillButton";
import { DailyPlan } from "@/lib/api";

export function TodaysPlanSummaryCard({ plan }: { plan: DailyPlan | null }) {
  const pending = plan?.items.filter((i) => i.status === "pending") ?? [];

  return (
    <Surface className="flex h-full flex-col gap-5 p-6 sm:p-7">
      <div>
        <h2 className="font-display text-lg text-ink">Today&apos;s plan</h2>
        <p className="mt-2 text-sm leading-relaxed text-muted-foreground">
          {plan
            ? pending.length > 0
              ? `${pending.length} item(s) left · ${plan.point_budget} point budget`
              : "You've cleared today's plan. Nice work."
            : "No plan generated yet for today - head to Daily Plan to get one."}
        </p>
      </div>
      <div className="mt-auto">
        <PillLink href="/daily-plan" variant="secondary" size="sm" arrow>
          Go to daily plan
        </PillLink>
      </div>
    </Surface>
  );
}
