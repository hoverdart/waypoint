"use client";

import { useState } from "react";
import { useRouter } from "next/navigation";
import { DashboardSubjectSummary, generateDailyPlan } from "@/lib/api";
import { useApiToken } from "@/lib/hooks/useApiToken";
import { PillButton } from "@/components/kit/PillButton";

export function RegenerateTimeBudgetControl({ subjects }: { subjects: DashboardSubjectSummary[] }) {
  const router = useRouter();
  const token = useApiToken();
  const [subjectId, setSubjectId] = useState(subjects[0]?.subject_id ?? 0);
  const [minutes, setMinutes] = useState(10);
  const [open, setOpen] = useState(false);
  const [busy, setBusy] = useState(false);
  const [message, setMessage] = useState<string | null>(null);
  const [error, setError] = useState<string | null>(null);

  async function regenerate() {
    setBusy(true);
    setError(null);
    setMessage(null);
    try {
      await generateDailyPlan(subjectId, token, minutes);
      setMessage("Plan updated. Your completed work is preserved.");
      router.refresh();
    } catch {
      setError("Couldn't update your plan. Please try again.");
    } finally { setBusy(false); }
  }

  return <div className="relative">
    <PillButton variant="secondary" size="sm" aria-expanded={open} disabled={!subjects.length} onClick={() => setOpen(!open)}>Adjust today&apos;s time</PillButton>
    {open && <div className="absolute left-0 z-20 sm:right-0 sm:left-auto mt-3 w-72 space-y-4 rounded-md border border-border bg-card p-5 shadow-lift">
      <p className="text-sm leading-relaxed text-muted-foreground">Set today’s total time for one course. Finished work stays; extra pending tasks are marked skipped.</p>
      <label className="block text-sm">Course<select value={subjectId} onChange={e => setSubjectId(Number(e.target.value))} disabled={busy} className="mt-1 w-full rounded border border-input bg-background p-2">{subjects.map(subject => <option key={subject.subject_id} value={subject.subject_id}>{subject.subject_name}</option>)}</select></label>
      <label className="block text-sm">Time today<select value={minutes} onChange={e => setMinutes(Number(e.target.value))} disabled={busy} className="mt-1 w-full rounded border border-input bg-background p-2">{[5, 10, 20, 30, 45, 60].map(value => <option key={value} value={value}>{value} minutes</option>)}</select></label>
      <PillButton disabled={busy} onClick={() => void regenerate()}>{busy ? "Updating…" : "Update this course"}</PillButton>
      {error && <p role="alert" className="text-sm text-destructive">{error}</p>}
      {message && <p role="status" className="text-sm text-blue">{message}</p>}
    </div>}
  </div>;
}
