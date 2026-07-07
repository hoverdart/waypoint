"use client";

import { useRouter } from "next/navigation";
import { PlanItemType, startPractice } from "@/lib/api";
import { useApiToken } from "@/lib/hooks/useApiToken";

interface StartableItem {
  subject_id: number;
  topic_id: number;
  item_type?: PlanItemType;
}

/** Shared "start a practice session for this topic" flow - builds the
 * MCQ/FRQ question-count payload and navigates to the session, optionally
 * tagging it with a daily-plan item id. Used by PlanItemCard's "Start",
 * TodaysRouteCard's "Start today's route", and the results page's "Try
 * another similar question". */
export function useStartPlanItem() {
  const router = useRouter();
  const getToken = useApiToken();

  return async function startPlanItem(item: StartableItem, opts?: { planItemId?: number }) {
    const isFrq = item.item_type === "frq";
    const session = await startPractice(
      {
        subject_id: item.subject_id,
        topic_id: item.topic_id,
        session_type: isFrq ? "frq" : "mcq",
        question_count: isFrq ? 3 : 8,
      },
      getToken
    );
    const suffix = opts?.planItemId ? `?planItemId=${opts.planItemId}` : "";
    router.push(`/practice/session/${session.session_id}${suffix}`);
    return session;
  };
}
