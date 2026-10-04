"use client";

import { useState } from "react";
import { useRouter } from "next/navigation";
import { ArrowUpRight, BookOpen, Search } from "lucide-react";
import { SubjectDetail, startPractice } from "@/lib/api";
import { useApiToken } from "@/lib/hooks/useApiToken";
import { PillButton } from "@/components/kit/PillButton";
import { GuidedLessons } from "./GuidedLessons";
import { DiagnosticStartButton } from "./DiagnosticStartButton";

export function CourseStudy({ subject }: { subject: SubjectDetail }) {
  const router = useRouter();
  const token = useApiToken();
  const [query, setQuery] = useState("");
  const [mode, setMode] = useState<"mcq" | "frq">("mcq");
  const [count, setCount] = useState(10);
  const [busy, setBusy] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const units = subject.units.filter(unit => `${unit.name} ${unit.topics.map(t => t.name).join(" ")}`.toLowerCase().includes(query.toLowerCase()));

  async function practice(unitId?: number, topicId?: number) {
    setBusy(true);
    setError(null);
    try {
      const session = await startPractice({ subject_id: subject.id, unit_id: unitId, topic_id: topicId, session_type: mode, question_count: count }, token);
      if (!session.questions.length) {
        setError("There are no questions in this format for that selection yet. Try the whole unit or multiple choice.");
        return;
      }
      router.push(`/practice/session/${session.session_id}`);
    } catch (cause) {
      setError(cause instanceof Error ? cause.message : "Couldn't start practice. Please try again.");
    } finally {
      setBusy(false);
    }
  }

  return (
    <div className="grid items-start gap-10 lg:grid-cols-[1fr_280px]">
      <section aria-label="Course curriculum" className="space-y-6">
        <label className="flex items-center gap-3 border-b border-border pb-3">
          <Search className="size-4 text-muted-foreground" aria-hidden="true" />
          <input aria-label="Search units and topics" value={query} onChange={e => setQuery(e.target.value)} placeholder="Find a unit or topic…" className="w-full bg-transparent py-2 outline-none focus-visible:ring-2 focus-visible:ring-ring" />
        </label>
        {!units.length && <p className="py-10 text-muted-foreground">No topics match “{query}”. Try another search.</p>}
        {units.map(unit => (
          <details key={unit.id} open={query.length > 0 || undefined} className="group border-b border-border pb-6">
            <summary className="flex cursor-pointer list-none items-start gap-5 py-3 focus-visible:outline-2 focus-visible:outline-ring">
              <span className="font-mono text-sm text-blue">{String(unit.display_order).padStart(2, "0")}</span>
              <div className="flex-1"><h2 className="text-xl font-semibold tracking-tight">{unit.name}</h2><p className="mt-1 text-xs text-muted-foreground">{unit.topics.length} topics · {unit.ap_weight_max > 0 ? `${unit.ap_weight_min}–${unit.ap_weight_max}% exam weighting` : "No official unit weighting"}</p></div>
              <span className="text-xl group-open:rotate-45" aria-hidden="true">+</span>
            </summary>
            <div className="space-y-4 pt-4 sm:pl-10">
              <p className="text-sm leading-relaxed text-muted-foreground">{unit.description}</p>
              {!!unit.lesson_count && <GuidedLessons unitId={unit.id} onPractice={() => void practice(unit.id)} practiceBusy={busy} />}
              <PillButton size="sm" disabled={busy} onClick={() => void practice(unit.id)}>Practice this unit</PillButton>
              <ul className="divide-y divide-border">
                {unit.topics.map(topic => <li key={topic.id} className="flex items-center justify-between gap-4 py-4"><div><h3 className="text-sm font-medium">{topic.name}</h3><p className="mt-1 max-w-lg text-xs leading-relaxed text-muted-foreground">{topic.description}</p></div><button aria-label={`Practice ${topic.name}`} disabled={busy} onClick={() => void practice(unit.id, topic.id)} className="rounded-full border border-border p-2 text-blue hover:bg-blue-soft focus-visible:ring-2 focus-visible:ring-ring disabled:opacity-40"><ArrowUpRight className="size-4" /></button></li>)}
              </ul>
            </div>
          </details>
        ))}
      </section>
      <aside className="space-y-6 border border-border bg-card p-6 lg:sticky lg:top-28">
        <BookOpen className="size-5 text-blue" aria-hidden="true" />
        <div><p className="font-mono text-[10px] uppercase tracking-[0.2em] text-muted-foreground">Your study desk</p><h2 className="mt-2 text-xl font-semibold">Make a little progress.</h2><p className="mt-2 text-sm leading-relaxed text-muted-foreground">Choose a focus from the course, or mix questions from every unit.</p></div>
        <label className="block text-sm">Question format<select value={mode} onChange={e => setMode(e.target.value as "mcq" | "frq")} className="mt-2 w-full rounded-md border border-input bg-background p-2"><option value="mcq">Multiple choice</option><option value="frq">Free response</option></select></label>
        <label className="block text-sm">Session length<select value={count} onChange={e => setCount(Number(e.target.value))} className="mt-2 w-full rounded-md border border-input bg-background p-2">{[5, 10, 20].map(n => <option key={n} value={n}>Up to {n} questions</option>)}</select></label>
        {error && <p role="alert" className="text-sm text-destructive">{error}</p>}
        <PillButton className="w-full" arrow disabled={busy} onClick={() => void practice()}>{busy ? "Preparing…" : "Practice the whole course"}</PillButton>
        <div className="border-t border-border pt-5"><p className="mb-3 text-xs leading-relaxed text-muted-foreground">New to this course? A diagnostic helps build your first study plan.</p><DiagnosticStartButton subjectId={subject.id} /></div>
        <p className="text-[11px] leading-relaxed text-muted-foreground">Original practice material. Not affiliated with or endorsed by College Board. Practice feedback is not an official AP grade.</p>
      </aside>
    </div>
  );
}
