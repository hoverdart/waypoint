"use client";

import { useRouter } from "next/navigation";
import { DailyPlanItem, updatePlanItem } from "@/lib/api";
import { useApiToken } from "@/lib/hooks/useApiToken";
import { Reveal } from "@/components/motion/Reveal";
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
    return <p className="text-sm text-ink-soft">Nothing scheduled for this subject today.</p>;
  }

  return (
    <div className="space-y-3">
      {items.map((item, i) => (
        <Reveal key={item.id} index={i}>
          <PlanItemCard
            item={item}
            topicName={topicNames[item.topic_id] ?? "Topic"}
            onSkip={handleSkip}
            gamified={gamified}
          />
        </Reveal>
      ))}
    </div>
  );
}
