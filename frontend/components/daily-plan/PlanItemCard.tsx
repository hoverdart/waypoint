"use client";

import { useState } from "react";
import { Card, CardContent } from "@/components/ui/card";
import { WayPointButton } from "@/components/shared/WayPointButton";
import { WeakSpotBadge } from "@/components/shared/MasteryPills";
import { AnimatedCheckpoint } from "@/components/shared/AnimatedCheckpoint";
import { ReasonBadge } from "@/components/shared/ReasonBadge";
import { ITEM_TYPE_LABEL } from "@/lib/planItemLabels";
import { useStartPlanItem } from "@/lib/hooks/useStartPlanItem";
import { DailyPlanItem } from "@/lib/api";
import { cn } from "@/lib/utils";

export function PlanItemCard({
  item,
  topicName,
  onSkip,
  gamified = false,
}: {
  item: DailyPlanItem;
  topicName: string;
  onSkip: (itemId: number) => Promise<void>;
  gamified?: boolean;
}) {
  const startPlanItem = useStartPlanItem();
  const [busy, setBusy] = useState(false);
  const isDone = item.status !== "pending";

  async function handleStart() {
    setBusy(true);
    try {
      await startPlanItem(item, { planItemId: item.id });
    } finally {
      setBusy(false);
    }
  }

  async function handleSkip() {
    setBusy(true);
    try {
      await onSkip(item.id);
    } finally {
      setBusy(false);
    }
  }

  return (
    <Card className={cn("transition-opacity", isDone && "opacity-60")}>
      <CardContent className="flex items-center gap-4 py-4">
        <AnimatedCheckpoint done={item.status === "completed"} />

        <div className="min-w-0 flex-1 space-y-1.5">
          <div className="flex flex-wrap items-center gap-2">
            {item.item_type === "weakness" ? (
              <WeakSpotBadge label={ITEM_TYPE_LABEL[item.item_type]} />
            ) : (
              <span className="inline-flex items-center rounded-full bg-blue-soft px-2.5 py-0.5 text-xs font-medium text-navy">
                {ITEM_TYPE_LABEL[item.item_type]}
              </span>
            )}
            <span className="text-sm font-medium text-navy">{topicName}</span>
            <span className="text-xs text-muted-foreground">
              {gamified ? `+${item.point_cost} XP` : `${item.point_cost} pts`}
            </span>
          </div>
          <ReasonBadge reason={item.reason} />
        </div>

        {!isDone && (
          <div className="flex shrink-0 gap-2">
            <WayPointButton variant="ghost" size="sm" showArrow={false} disabled={busy} onClick={handleSkip}>
              Skip
            </WayPointButton>
            <WayPointButton variant="secondary" size="sm" showArrow={false} disabled={busy} onClick={handleStart}>
              Start
            </WayPointButton>
          </div>
        )}
        {isDone && <span className="shrink-0 text-xs capitalize text-muted-foreground">{item.status}</span>}
      </CardContent>
    </Card>
  );
}
