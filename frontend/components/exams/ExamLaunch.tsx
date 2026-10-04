"use client";
import { useEffect, useState } from "react";
import { useRouter } from "next/navigation";
import { ExamForm, getExamForms, startExam } from "@/lib/api/exams";
import { useApiToken } from "@/lib/hooks/useApiToken";
import { PillButton } from "@/components/kit/PillButton";

export function ExamLaunch({ subjectId }: { subjectId: number }) {
  const token = useApiToken();
  const router = useRouter();
  const [forms, setForms] = useState<ExamForm[]>([]);
  const [retry, setRetry] = useState(0);
  const [error, setError] = useState<string | null>(null);
  const [busy, setBusy] = useState(false);
  const [multiplier, setMultiplier] = useState(1);
  useEffect(() => {
    let current = true;
    getExamForms(subjectId, token).then(data => { if (current) { setForms(data); setError(null); } })
      .catch(() => { if (current) setError("Couldn't load exam forms. Please retry."); });
    return () => { current = false; };
  }, [subjectId, token, retry]);
  async function begin(formId: string) {
    setBusy(true); setError(null);
    try { const exam = await startExam(subjectId, formId, multiplier, token); router.push(`/exams/${exam.session_id}`); }
    catch (cause) { setError(cause instanceof Error ? cause.message : "Couldn't start this form. Please retry."); }
    finally { setBusy(false); }
  }
  if (!forms.length && !error) return null;
  return <section aria-label="Timed exam practice" className="mb-12 border-y border-border py-8">
    <div className="flex flex-wrap items-end justify-between gap-6">
      <div><p className="font-mono text-xs uppercase tracking-widest text-blue">The rehearsal</p><h2 className="mt-2 font-display text-3xl">Practice the whole exam.</h2><p className="mt-3 max-w-xl text-sm leading-relaxed text-muted-foreground">Original forms with separate section clocks. Closing a section locks its answers. Essays use rubric self-review; this is not an official AP score.</p></div>
      {!!forms.length && <label className="text-sm">Practice time allowance<select value={multiplier} disabled={busy} onChange={e => setMultiplier(Number(e.target.value))} className="mt-2 block w-full rounded-md border border-input bg-background p-2"><option value={1}>Standard timing</option><option value={1.5}>1.5× practice time</option><option value={2}>2× practice time</option></select></label>}
    </div>
    {error && <div className="mt-5 flex flex-wrap items-center gap-3"><p role="alert" className="text-sm text-destructive">{error}</p><PillButton size="sm" variant="secondary" onClick={() => setRetry(n => n + 1)}>Reload forms</PillButton></div>}
    <div className="mt-6 grid gap-4 sm:grid-cols-2">{forms.map(form => <article key={form.form_id} className="border border-border bg-card p-5">
      <h3 className="font-semibold">{form.title}</h3><ul className="my-4 space-y-2 text-sm text-muted-foreground">{form.sections.map(section => <li key={section.title}>{section.title}: {section.question_count} questions · {section.duration_seconds * multiplier / 60} minutes</li>)}</ul>
      <PillButton size="sm" disabled={busy || !form.available} onClick={() => void begin(form.form_id)}>{form.available ? busy ? "Preparing…" : `Start ${form.title.split(" · ").at(-1)}` : "Content being updated"}</PillButton>
    </article>)}</div>
    <p className="mt-4 text-xs text-muted-foreground">Practice permits an untimed break between sections. Once a section starts, its clock continues if you leave the page. Extended practice time is a study preference, not an official accommodation.</p>
  </section>;
}
