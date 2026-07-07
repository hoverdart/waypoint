"use client";

import { useState } from "react";
import { Compass } from "lucide-react";
import { CardContent } from "@/components/ui/card";
import { WayPointCard } from "@/components/shared/WayPointCard";
import { WayPointButton } from "@/components/shared/WayPointButton";
import { LinkButton } from "@/components/shared/LinkButton";
import { EmptyState } from "@/components/shared/EmptyState";
import { AnimatedCheckpoint } from "@/components/shared/AnimatedCheckpoint";
import { ITEM_TYPE_LABEL } from "@/lib/planItemLabels";
import { useStartPlanItem } from "@/lib/hooks/useStartPlanItem";
import { DailyPlan } from "@/lib/api";

/** Dashboard hero card - named TodaysRouteCard (not "DailyTaskCard") to
 * avoid colliding with the per-item PlanItemCard on /daily-plan, which the
 * brief separately called "DailyTaskCard". Replaces TodaysPlanSummaryCard. */
export function TodaysRouteCard({
  plan,
  topicNames,
  gamified = false,
}: {
  plan: DailyPlan | null;
  topicNames: Record<number, string>;
  gamified?: boolean;
}) {
  const startPlanItem = useStartPlanItem();
  const [starting, setStarting] = useState(false);

  if (!plan) {
    return (
      <WayPointCard elevated>
        <CardContent className="p-6">
          <EmptyState
            icon={<Compass className="size-5" aria-hidden="true" />}
            title="No route generated yet"
            description="Head to Daily Plan to generate today's route."
            action={<LinkButton href="/daily-plan">Go to daily plan</LinkButton>}
          />
        </CardContent>
      </WayPointCard>
    );
  }

  const pending = plan.items.filter((item) => item.status === "pending");
  const nextItem = pending[0];

  async function handleStartRoute() {
    if (!nextItem) return;
    setStarting(true);
    try {
      await startPlanItem(nextItem, { planItemId: nextItem.id });
    } finally {
      setStarting(false);
    }
  }

  return (
    <WayPointCard elevated>
      <CardContent className="space-y-5 p-6">
        <div>
          <p className="text-xs font-medium tracking-wide text-blue uppercase">Today&apos;s route</p>
          <p className="font-heading text-xl font-semibold text-navy">
            {pending.length > 0
              ? `${pending.length} stop${pending.length === 1 ? "" : "s"} left · ${plan.point_budget} ${gamified ? "XP" : "pts"} budget`
              : "Route cleared for today"}
          </p>
        </div>

        {pending.length > 0 ? (
          <>
            <ul className="space-y-2">
              {pending.slice(0, 3).map((item) => (
                <li
                  key={item.id}
                  className="flex items-center gap-3 rounded-xl border border-border/70 bg-muted/40 px-3 py-2.5"
                >
                  <AnimatedCheckpoint done={false} />
                  <div className="min-w-0">
                    <p className="truncate text-sm font-medium text-navy">
                      {topicNames[item.topic_id] ?? "Topic"}
                    </p>
                    <p className="truncate text-xs text-muted-foreground">
                      {ITEM_TYPE_LABEL[item.item_type]} · {item.reason}
                    </p>
                  </div>
                </li>
              ))}
            </ul>
            {pending.length > 3 && (
              <p className="text-xs text-muted-foreground">+{pending.length - 3} more on your daily plan</p>
            )}
            <div className="flex items-center gap-3">
              <WayPointButton onClick={handleStartRoute} disabled={starting}>
                {starting ? "Starting..." : "Start today's route"}
              </WayPointButton>
              <LinkButton variant="ghost" href="/daily-plan">
                View full plan
              </LinkButton>
            </div>
          </>
        ) : (
          <p className="text-sm text-muted-foreground">You&apos;ve cleared today&apos;s plan. Nice work.</p>
        )}
      </CardContent>
    </WayPointCard>
  );
}
