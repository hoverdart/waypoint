import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { LinkButton } from "@/components/shared/LinkButton";
import { DailyPlan } from "@/lib/api";

export function TodaysPlanSummaryCard({ plan }: { plan: DailyPlan | null }) {
  const pending = plan?.items.filter((i) => i.status === "pending") ?? [];

  return (
    <Card>
      <CardHeader>
        <CardTitle>Today&apos;s plan</CardTitle>
      </CardHeader>
      <CardContent className="space-y-3">
        {plan ? (
          <p className="text-sm text-muted-foreground">
            {pending.length > 0
              ? `${pending.length} item(s) left · ${plan.point_budget} point budget`
              : "You've cleared today's plan. Nice work."}
          </p>
        ) : (
          <p className="text-sm text-muted-foreground">
            No plan generated yet for today - head to Daily Plan to get one.
          </p>
        )}
        <LinkButton href="/daily-plan">Go to daily plan</LinkButton>
      </CardContent>
    </Card>
  );
}
