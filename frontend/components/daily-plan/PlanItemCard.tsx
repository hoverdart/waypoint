"use client";

import { useState } from "react";
import { useRouter } from "next/navigation";
import { Card, CardContent } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { Badge } from "@/components/ui/badge";
import { ReasonBadge } from "@/components/shared/ReasonBadge";
import { DailyPlanItem, startPractice } from "@/lib/api";
import { useApiToken } from "@/lib/hooks/useApiToken";

const ITEM_TYPE_LABEL: Record<DailyPlanItem["item_type"], string> = {
  weakness: "Weak spot",
  review: "Review",
  calibration: "Calibration",
  frq: "Free response",
  challenge: "Challenge",
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
    <Card className={isDone ? "opacity-60" : undefined}>
      <CardContent className="flex items-center justify-between gap-4 py-4">
        <div className="space-y-1.5">
          <div className="flex items-center gap-2">
            <Badge variant="outline">{ITEM_TYPE_LABEL[item.item_type]}</Badge>
            <span className="text-sm font-medium">{topicName}</span>
            <span className="text-xs text-muted-foreground">
              {gamified ? `+${item.point_cost} XP` : `${item.point_cost} pts`}
            </span>
          </div>
          <ReasonBadge reason={item.reason} />
        </div>

        {!isDone && (
          <div className="flex shrink-0 gap-2">
            <Button variant="ghost" size="sm" disabled={busy} onClick={() => onSkip(item.id)}>
              Skip
            </Button>
            <Button size="sm" disabled={busy} onClick={handleStart}>
              Start
            </Button>
          </div>
        )}
        {isDone && (
          <span className="shrink-0 text-xs capitalize text-muted-foreground">{item.status}</span>
        )}
      </CardContent>
    </Card>
  );
}
