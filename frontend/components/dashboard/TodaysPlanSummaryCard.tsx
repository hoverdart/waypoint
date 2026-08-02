"use client";

import { useState } from "react";
import { Surface } from "@/components/kit/Surface";
import { PillButton, PillLink } from "@/components/kit/PillButton";
import { DailyPlan } from "@/lib/api";
import { useStartPlanItem } from "@/lib/hooks/useStartPlanItem";
import { ITEM_TYPE_LABEL } from "@/lib/planItemLabels";

export function TodaysPlanSummaryCard({
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
  const pending = plan?.items.filter((i) => i.status === "pending") ?? [];
  const nextItem = pending[0];

  async function handleStart() {
    if (!nextItem) return;
    setStarting(true);
    try {
      await startPlanItem(nextItem, { planItemId: nextItem.id });
    } finally {
      setStarting(false);
    }
  }

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
      {pending.length > 0 && (
        <ul className="space-y-2">
          {pending.slice(0, 3).map((item) => (
            <li key={item.id} className="rounded-xl bg-blue-soft/35 px-3 py-2.5">
              <p className="truncate text-sm font-medium text-ink">{topicNames[item.topic_id] ?? "Topic"}</p>
              <p className="truncate text-xs text-muted-foreground">
                {ITEM_TYPE_LABEL[item.item_type]} · {item.reason}
              </p>
            </li>
          ))}
          {pending.length > 3 && <li className="text-xs text-muted-foreground">+{pending.length - 3} more items</li>}
        </ul>
      )}
      <div className="mt-auto">
        {nextItem ? (
          <div className="flex flex-wrap gap-2">
            <PillButton size="sm" disabled={starting} onClick={handleStart}>
              {starting ? "Starting..." : gamified ? "Start today’s quest" : "Start today’s plan"}
            </PillButton>
            <PillLink href="/daily-plan" variant="secondary" size="sm" arrow>
              View full plan
            </PillLink>
          </div>
        ) : (
          <PillLink href="/daily-plan" variant="secondary" size="sm" arrow>
            Go to daily plan
          </PillLink>
        )}
      </div>
    </Surface>
  );
}
