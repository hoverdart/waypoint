"use client";

import { useRouter } from "next/navigation";
import { DailyPlanItem, updatePlanItem } from "@/lib/api";
import { useApiToken } from "@/lib/hooks/useApiToken";
import { PlanItemCard } from "./PlanItemCard";

export function PlanItemList({
  items,
  topicNames,
  gamified = false,
}: {
  items: DailyPlanItem[];
  topicNames: Record<number, string>;
  gamified?: boolean;
}) {
  const router = useRouter();
  const getToken = useApiToken();

  async function handleSkip(itemId: number) {
    await updatePlanItem(itemId, "skipped", getToken);
    router.refresh();
  }

  if (items.length === 0) {
    return <p className="text-sm text-muted-foreground">Nothing scheduled for this subject today.</p>;
  }

  return (
    <div className="space-y-2">
      {items.map((item) => (
        <PlanItemCard
          key={item.id}
          item={item}
          topicName={topicNames[item.topic_id] ?? "Topic"}
          onSkip={handleSkip}
          gamified={gamified}
        />
      ))}
    </div>
  );
}
