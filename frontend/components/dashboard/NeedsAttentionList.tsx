import { DailyPlanItem } from "@/lib/api";
import { WeakSpotBadge } from "@/components/shared/MasteryPills";

/** Surfaces today's weakness-flagged plan items as a scannable strip -
 * zero extra backend calls, filtered straight from the already-fetched
 * daily plan. */
export function NeedsAttentionList({
  items,
  topicNames,
}: {
  items: DailyPlanItem[];
  topicNames: Record<number, string>;
}) {
  const weakItems = items.filter((item) => item.item_type === "weakness");
  if (weakItems.length === 0) return null;

  return (
    <div className="space-y-2">
      <p className="font-heading text-sm font-semibold text-navy">Needs attention</p>
      <ul className="flex flex-wrap gap-2">
        {weakItems.map((item) => (
          <li key={item.id}>
            <WeakSpotBadge label={topicNames[item.topic_id] ?? "Topic"} />
          </li>
        ))}
      </ul>
    </div>
  );
}
