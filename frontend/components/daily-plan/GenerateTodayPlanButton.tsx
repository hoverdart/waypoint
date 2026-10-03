"use client";

import { toast } from "sonner";
import { useState } from "react";
import { useRouter } from "next/navigation";
import { PillButton } from "@/components/kit/PillButton";
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
    } catch {
      toast.error("Could not generate every course plan. Please try again; existing plans are preserved.");
      router.refresh();
    } finally {
      setBusy(false);
    }
  }

  return (
    <PillButton disabled={busy || subjects.length === 0} onClick={handleGenerate}>
      {busy ? "Building your plan..." : "Generate today's plan"}
    </PillButton>
  );
}
