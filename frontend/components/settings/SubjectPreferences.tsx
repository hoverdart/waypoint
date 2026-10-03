"use client";

import { useState } from "react";
import { useRouter } from "next/navigation";
import { Subject, UserSubject, OnboardingSubjectInput, saveMySubjects } from "@/lib/api";
import { useApiToken } from "@/lib/hooks/useApiToken";
import { Surface } from "@/components/kit/Surface";
import { PillButton } from "@/components/kit/PillButton";

export function SubjectPreferences({ subjects, enrolled }: { subjects: Subject[]; enrolled: UserSubject[] }) {
  const [selected, setSelected] = useState<Record<number, OnboardingSubjectInput>>(() => Object.fromEntries(enrolled.map(s => [s.subject_id, { subject_id: s.subject_id, target_score: s.target_score, exam_date: s.exam_date, study_minutes_per_day: s.study_minutes_per_day }])));
  const [saving, setSaving] = useState(false);
  const [message, setMessage] = useState<string | null>(null);
  const [error, setError] = useState<string | null>(null);
  const token = useApiToken();
  const router = useRouter();

  function update(id: number, patch: Partial<OnboardingSubjectInput>) {
    setSelected(previous => ({ ...previous, [id]: { ...previous[id], ...patch } }));
    setMessage(null);
  }

  async function save(event: React.FormEvent) {
    event.preventDefault();
    setSaving(true);
    setError(null);
    setMessage(null);
    try {
      await saveMySubjects(Object.values(selected), token);
      setMessage("Course preferences saved. New plans will use your study time.");
      router.refresh();
    } catch {
      setError("Could not save your preferences. Your changes are still here—please try again.");
    } finally {
      setSaving(false);
    }
  }

  return <Surface className="p-6">
    <form onSubmit={save} className="space-y-6">
      <div><h2 className="font-display text-xl text-ink">Your courses</h2><p className="mt-2 text-sm leading-relaxed text-muted-foreground">Choose what you’re studying and how much time you have. Removing a course keeps your practice history and progress.</p></div>
      <fieldset disabled={saving} className="divide-y divide-border">
        {subjects.map(subject => {
          const value = selected[subject.id];
          return <div key={subject.id} className="py-5 first:pt-0">
            <label className="flex items-center gap-3 font-medium"><input type="checkbox" className="size-4 accent-primary" checked={!!value} onChange={event => {
              setSelected(previous => {
                const next = { ...previous };
                if (event.target.checked) next[subject.id] = { subject_id: subject.id, target_score: 4, exam_date: null, study_minutes_per_day: 20 };
                else delete next[subject.id];
                return next;
              });
              setMessage(null);
            }} />{subject.name}</label>
            {value && <div className="mt-4 grid gap-4 sm:grid-cols-3">
              <label className="text-xs text-muted-foreground">Target score for {subject.name}<select className="mt-2 w-full rounded-md border border-input bg-background p-2 text-sm text-ink" value={value.target_score ?? ""} onChange={e => update(subject.id, { target_score: e.target.value ? Number(e.target.value) : null })}><option value="">No target</option>{[1, 2, 3, 4, 5].map(score => <option key={score}>{score}</option>)}</select></label>
              <label className="min-w-0 text-xs text-muted-foreground">Exam date for {subject.name}<input type="date" className="mt-2 block w-full min-w-0 rounded-md border border-input bg-background p-2 text-sm text-ink" value={value.exam_date ?? ""} onChange={e => update(subject.id, { exam_date: e.target.value || null })} /></label>
              <label className="text-xs text-muted-foreground">Daily minutes for {subject.name}<input type="number" min={5} max={180} required className="mt-2 w-full rounded-md border border-input bg-background p-2 text-sm text-ink" value={value.study_minutes_per_day} onChange={e => update(subject.id, { study_minutes_per_day: Number(e.target.value) })} /></label>
            </div>}
          </div>;
        })}
      </fieldset>
      {error && <p role="alert" className="text-sm text-destructive">{error}</p>}
      {message && <p role="status" className="text-sm text-blue">{message}</p>}
      <PillButton type="submit" disabled={saving}>{saving ? "Saving…" : "Save course preferences"}</PillButton>
    </form>
  </Surface>;
}
