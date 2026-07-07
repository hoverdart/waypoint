import { PlanItemType, SubjectDetail } from "@/lib/api/types";

/** A bare DailyPlanItem only carries topic_id/item_type - these two lookups
 * turn that into the labels TodaysRouteCard (dashboard) and PlanItemCard
 * (daily-plan) both need to render, so neither duplicates the mapping. */
export const ITEM_TYPE_LABEL: Record<PlanItemType, string> = {
  weakness: "Weak spot",
  review: "Review",
  calibration: "Calibration",
  frq: "Free response",
  challenge: "Challenge",
};

export function buildTopicNameMap(subjectDetails: SubjectDetail[]): Record<number, string> {
  const map: Record<number, string> = {};
  for (const subject of subjectDetails) {
    for (const unit of subject.units) {
      for (const topic of unit.topics) {
        map[topic.id] = topic.name;
      }
    }
  }
  return map;
}
