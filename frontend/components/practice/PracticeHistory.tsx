"use client";

import { useState } from "react";
import { PracticeHistoryItem, getPracticeHistory } from "@/lib/api";
import { useApiToken } from "@/lib/hooks/useApiToken";
import { PillButton, PillLink } from "@/components/kit/PillButton";

export function PracticeHistory({ initialSessions }: { initialSessions: PracticeHistoryItem[] }) {
  const [sessions, setSessions] = useState(initialSessions);
  const [more, setMore] = useState(initialSessions.length === 30);
  const [busy, setBusy] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const token = useApiToken();
  async function loadMore() {
    setBusy(true);
    setError(null);
    try {
      const next = await getPracticeHistory(token, sessions.length);
      setSessions(previous => [...previous, ...next]);
      setMore(next.length === 30);
    } catch {
      setError("Couldn't load older sessions. Please try again.");
    } finally { setBusy(false); }
  }
  if (!sessions.length) return <div className="border-y border-border py-16 text-center"><h2 className="editorial-title text-3xl">Your first page is waiting.</h2><p className="mx-auto mt-4 mb-6 max-w-md text-sm leading-relaxed text-muted-foreground">Choose a course and start a practice session. Your saved work and completed sessions will live here.</p><PillLink href="/subjects" arrow>Choose a course</PillLink></div>;
  return <div>
    <ul className="divide-y divide-border border-y border-border">
      {sessions.map(session => <li key={session.session_id} className="flex flex-wrap items-center justify-between gap-5 py-6">
        <div className="flex gap-5"><div className="hidden w-14 pt-1 font-mono text-xs text-muted-foreground sm:block">#{String(session.session_id).padStart(3, "0")}</div><div><p className="mb-2 font-mono text-[10px] uppercase tracking-[0.12em] text-blue">{session.is_exam ? "Exam rehearsal" : session.session_type === "mcq" ? "Multiple choice" : session.session_type === "frq" ? "Free response" : session.session_type.replaceAll("_", " ")} · {session.completed_at ? "Completed" : "In progress"}</p><h2 className="text-lg font-semibold">{session.subject_name}</h2><p className="mt-2 text-sm text-muted-foreground">{session.completed_at ? (session.graded_count === 0 ? `${session.self_review_count} responses · rubric self-review` : `${session.correct_count} of ${session.graded_count ?? session.total_questions} scored questions correct · ${Math.round(session.score * 100)}%${session.self_review_count ? ` · ${session.self_review_count} rubric responses` : ""}`) : `${session.answered_count} of ${session.total_questions} questions saved`}</p></div></div>
        <PillLink variant={session.completed_at ? "secondary" : "primary"} href={session.is_exam && !session.completed_at ? `/exams/${session.session_id}` : `/practice/${session.completed_at ? "results" : "session"}/${session.session_id}`} arrow>{session.completed_at ? "Review answers" : "Resume session"}</PillLink>
      </li>)}
    </ul>
    {error && <p role="alert" className="mt-6 text-sm text-destructive">{error}</p>}
    {more && <PillButton className="mt-6" variant="secondary" disabled={busy} onClick={() => void loadMore()}>{busy ? "Loading…" : "Older sessions"}</PillButton>}
  </div>;
}
