"use client";

import { useState } from "react";
import { useRouter } from "next/navigation";
import { WayPointButton } from "@/components/shared/WayPointButton";
import { DashboardSubjectSummary, generateDailyPlan } from "@/lib/api";
import { useApiToken } from "@/lib/hooks/useApiToken";

export function GenerateTodayPlanButton({ subjects }: { subjects: DashboardSubjectSummary[] }) {
  const router = useRouter();
  const getToken = useApiToken();
  const [busy, setBusy] = useState(false);

  async function handleGenerate() {
    setBusy(true);
    try {
      await Promise.all(subjects.map((s) => generateDailyPlan(s.subject_id, getToken)));
      router.refresh();
    } finally {
      setBusy(false);
    }
  }

  return (
    <WayPointButton showArrow={false} disabled={busy || subjects.length === 0} onClick={handleGenerate}>
      {busy ? "Building your plan..." : "Generate today's plan"}
    </WayPointButton>
  );
}
