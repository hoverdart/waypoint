"use client";

import { useState } from "react";
import { Surface } from "@/components/kit/Surface";
import { PillButton } from "@/components/kit/PillButton";
import { Chip } from "@/components/kit/Pills";
import { ReasonBadge } from "@/components/shared/ReasonBadge";
import { DailyPlanItem } from "@/lib/api";
import { useStartPlanItem } from "@/lib/hooks/useStartPlanItem";
import { cn } from "@/lib/utils";

const ITEM_TYPE_LABEL: Record<DailyPlanItem["item_type"], string> = {
  weakness: "Weak spot",
  review: "Review",
  calibration: "Calibration",
  frq: "Free response",
  challenge: "Challenge",
};

/** Tone-codes the item type so a plan reads at a glance: red-ish for the
 * things that need work, cooler tones for upkeep. */
const ITEM_TYPE_TONE: Record<DailyPlanItem["item_type"], "coral" | "blue" | "violet" | "amber" | "green"> = {
  weakness: "coral",
  review: "blue",
  calibration: "violet",
  frq: "amber",
  challenge: "green",
};

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
  const [error, setError] = useState<string | null>(null);
  const isDone = item.status !== "pending";

  async function runAction(action: () => Promise<unknown>) {
    setBusy(true);
    setError(null);
    try {
      await action();
    } catch {
      setError("Could not update this task. Please try again.");
    } finally {
      setBusy(false);
    }
  }

  return (
    <Surface
      tone={isDone ? "quiet" : "default"}
      className={cn(
        "flex flex-wrap items-center justify-between gap-4 p-5 sm:px-6",
        isDone && "opacity-70"
      )}
    >
      <div className="min-w-0 space-y-2.5">
        <div className="flex flex-wrap items-center gap-2.5">
          <Chip tone={ITEM_TYPE_TONE[item.item_type]}>{ITEM_TYPE_LABEL[item.item_type]}</Chip>
          <span className="text-sm font-medium text-ink">{topicName}</span>
          <span className="text-xs text-muted-foreground tabular-nums">
            {gamified ? `+${item.point_cost} XP` : `${item.point_cost} pts`}
          </span>
        </div>
        <ReasonBadge reason={item.reason} />
      </div>

      {!isDone && (
        <div className="flex shrink-0 items-center gap-2">
          <PillButton variant="ghost" size="sm" disabled={busy} onClick={() => void runAction(() => onSkip(item.id))}>
            Skip
          </PillButton>
          <PillButton size="sm" disabled={busy} onClick={() => void runAction(() => startPlanItem(item, { planItemId: item.id }))}>
            Start
          </PillButton>
        </div>
      )}
      {error && <p role="alert" className="w-full text-sm text-destructive">{error}</p>}
      {isDone && (
        <Chip tone={item.status === "completed" ? "green" : "neutral"} dot className="shrink-0 capitalize">
          {item.status}
        </Chip>
      )}
    </Surface>
  );
}
