"use client";

import { useState } from "react";
import { AnswerBreakdownItem, saveSelfReview } from "@/lib/api";
import { useApiToken } from "@/lib/hooks/useApiToken";
import { PillButton } from "@/components/kit/PillButton";

export function RubricSelfReview({ item, sessionId }: { item: AnswerBreakdownItem; sessionId: number }) {
  const token = useApiToken();
  const [points, setPoints] = useState<(number | null)[]>(item.self_review?.points ?? (item.rubric ?? []).map(() => null));
  const [saved, setSaved] = useState(item.self_review?.total ?? null);
  const [busy, setBusy] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [dirty, setDirty] = useState(false);
  async function save() {
    if (points.some(p => p === null)) return;
    setBusy(true);
    setError(null);
    try {
      const review = await saveSelfReview(sessionId, item.question_id, points as number[], token);
      setSaved(review.total);
      setDirty(false);
    } catch { setError("Couldn't save your rubric review. Your selections are still here; please retry."); }
    finally { setBusy(false); }
  }
  return <div className="space-y-5 rounded-2xl border border-border p-4">
    <div><h3 className="font-semibold">Your rubric review</h3><p className="mt-2 text-sm leading-relaxed text-muted-foreground">Compare your response with the model and select a level for each row. This is your assessment, not an automated or official AP grade. It does not change mastery or award accuracy points.</p></div>
    {item.rubric?.map((row, index) => <fieldset key={index} disabled={busy} className="space-y-2">
      <legend className="mb-2 text-sm font-medium">{row.point} · up to {row.points} points</legend>
      {row.levels?.map((description, score) => <label key={score} className="flex cursor-pointer items-start gap-3 rounded-xl border border-border p-3 text-sm leading-relaxed has-[:checked]:border-blue has-[:checked]:bg-blue-soft/40">
        <input type="radio" className="mt-1 shrink-0 accent-blue" name={`rubric-${item.question_id}-${index}`} checked={points[index] === score} onChange={() => { setPoints(previous => previous.map((p, i) => i === index ? score : p)); setDirty(true); }} />
        <span><strong>{score} {score === 1 ? "point" : "points"}.</strong> {description}</span>
      </label>)}
    </fieldset>)}
    {error && <p role="alert" className="text-sm text-destructive">{error}</p>}
    {saved !== null && !dirty && <p role="status" className="text-sm font-medium">Saved self-assessment: {saved}/{item.max_score} points.</p>}
    <PillButton size="sm" disabled={busy || points.some(p => p === null)} onClick={() => void save()}>{busy ? "Saving…" : "Save rubric review"}</PillButton>
  </div>;
}
