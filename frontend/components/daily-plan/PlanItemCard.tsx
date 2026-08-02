"use client";

import { useState } from "react";
import { useRouter } from "next/navigation";
import { Surface } from "@/components/kit/Surface";
import { PillButton } from "@/components/kit/PillButton";
import { Chip } from "@/components/kit/Pills";
import { ReasonBadge } from "@/components/shared/ReasonBadge";
import { DailyPlanItem, startPractice } from "@/lib/api";
import { useApiToken } from "@/lib/hooks/useApiToken";
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
  const router = useRouter();
  const getToken = useApiToken();
  const [busy, setBusy] = useState(false);
  const isDone = item.status !== "pending";

  async function handleStart() {
    setBusy(true);
    try {
      const session = await startPractice(
        {
          subject_id: item.subject_id,
          topic_id: item.topic_id,
          session_type: item.item_type === "frq" ? "frq" : "mcq",
          question_count: item.item_type === "frq" ? 3 : 8,
        },
        getToken
      );
      router.push(`/practice/session/${session.session_id}?planItemId=${item.id}`);
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
          <PillButton variant="ghost" size="sm" disabled={busy} onClick={() => onSkip(item.id)}>
            Skip
          </PillButton>
          <PillButton size="sm" disabled={busy} onClick={handleStart}>
            Start
          </PillButton>
        </div>
      )}
      {isDone && (
        <Chip tone={item.status === "completed" ? "green" : "neutral"} dot className="shrink-0 capitalize">
          {item.status}
        </Chip>
      )}
    </Surface>
  );
}
