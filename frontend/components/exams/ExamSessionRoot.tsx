"use client";
import { useCallback, useEffect, useRef, useState } from "react";
import { useRouter } from "next/navigation";
import { AnswerInput } from "@/lib/api";
import { beginExamSection, ExamSession, finishExamSection, getExam, saveExamDraft } from "@/lib/api/exams";
import { useApiToken } from "@/lib/hooks/useApiToken";
import { PillButton, PillLink } from "@/components/kit/PillButton";
import { Surface } from "@/components/kit/Surface";
import { McqQuestionForm } from "@/components/practice/McqQuestionForm";
import { FrqQuestionForm } from "@/components/practice/FrqQuestionForm";

function answerMap(answers: AnswerInput[]) { return Object.fromEntries(answers.map(a => [a.question_id, a])); }
function secondsLeft(exam: ExamSession) {
  const deadline = exam.sections[exam.current_section].deadline;
  return deadline ? Math.max(0, Math.ceil((Date.parse(deadline) - Date.parse(exam.server_time)) / 1000)) : 0;
}

export function ExamSessionRoot({ initialExam }: { initialExam: ExamSession }) {
  const token = useApiToken();
  const router = useRouter();
  const [exam, setExam] = useState(initialExam);
  const [answers, setAnswers] = useState<Record<number, AnswerInput>>(() => answerMap(initialExam.answers));
  const [index, setIndex] = useState(initialExam.current_index);
  const [remaining, setRemaining] = useState(() => secondsLeft(initialExam));
  const [dirty, setDirty] = useState(false);
  const [busy, setBusy] = useState<"saving" | "working" | null>(null);
  const [error, setError] = useState<string | null>(null);
  const [confirm, setConfirm] = useState(false);
  const inFlight = useRef(false);
  const editVersion = useRef(0);
  const section = exam.sections[exam.current_section];
  const expired = section.status === "expired" || (section.status === "active" && remaining === 0);
  const question = exam.questions[index];

  useEffect(() => {
    const start = performance.now();
    const initial = secondsLeft(exam);
    const tick = () => setRemaining(Math.max(0, initial - Math.floor((performance.now() - start) / 1000)));
    tick();
    const interval = setInterval(tick, 1000);
    return () => clearInterval(interval);
  }, [exam]);

  useEffect(() => {
    if (!dirty) return;
    const warn = (event: BeforeUnloadEvent) => { event.preventDefault(); event.returnValue = ""; };
    window.addEventListener("beforeunload", warn);
    return () => window.removeEventListener("beforeunload", warn);
  }, [dirty]);

  const save = useCallback(async (nextIndex = index, working = false): Promise<boolean> => {
    if (inFlight.current) return false;
    inFlight.current = true;
    const version = editVersion.current;
    setBusy(working ? "working" : "saving"); setError(null);
    try {
      const saved = await saveExamDraft(exam.session_id, exam.current_section, Object.values(answers), nextIndex, exam.revision, token);
      // A student can continue typing during an autosave. Never replace those edits.
      setExam(saved);
      if (version === editVersion.current) setDirty(false);
      setIndex(nextIndex);
      return true;
    } catch (cause) {
      setError(`${cause instanceof Error ? cause.message : "Could not save"}. Your local answers are still here. Retry saving, or reload the server draft if another tab changed it.`);
      return false;
    } finally { inFlight.current = false; setBusy(null); }
  }, [answers, exam, index, token]);

  useEffect(() => {
    if (!dirty || busy || error || expired || section.status !== "active") return;
    const timer = setTimeout(() => void save(), 1500);
    return () => clearTimeout(timer);
  }, [dirty, busy, error, expired, section.status, save]);

  function adopt(next: ExamSession) {
    setExam(next); setAnswers(answerMap(next.answers)); setIndex(next.current_index);
    setDirty(false); setConfirm(false);
    if (next.completed) router.push(`/practice/results/${next.session_id}`);
  }
  async function transition(kind: "start" | "finish" | "reload") {
    if (inFlight.current) return;
    if (kind === "finish" && !expired && dirty && !await save(index, true)) return;
    inFlight.current = true; setBusy("working"); setError(null);
    try {
      const next = kind === "reload" ? await getExam(exam.session_id, token) : kind === "start"
        ? await beginExamSection(exam.session_id, exam.current_section, token)
        : await finishExamSection(exam.session_id, exam.current_section, token);
      adopt(next);
    } catch (cause) { setError(cause instanceof Error ? cause.message : "Could not update the exam. Please retry or reload the saved state."); }
    finally { inFlight.current = false; setBusy(null); }
  }
  function edit(patch: Partial<AnswerInput>) {
    if (!question) return;
    editVersion.current += 1;
    setDirty(true);
    setAnswers(previous => ({ ...previous, [question.id]: { ...previous[question.id], ...patch, question_id: question.id } }));
  }
  const unanswered = exam.questions.filter(q => !answers[q.id]?.selected_option_id && !answers[q.id]?.free_response_text?.trim()).length;
  return <div className="mx-auto min-w-0 w-full max-w-3xl space-y-6 px-6 py-10 [overflow-wrap:anywhere]">
    <header className="border-b border-border pb-6"><p className="font-mono text-xs uppercase tracking-widest text-blue">Timed rehearsal · {exam.time_multiplier}× time</p><h1 className="mt-3 font-display text-3xl sm:text-4xl">{exam.title}</h1><p className="mt-3 text-sm text-muted-foreground">{exam.break_policy}</p></header>
    <div className="flex flex-wrap items-center justify-between gap-4"><h2 className="font-semibold">Section {exam.current_section + 1}: {section.title}</h2>{section.status !== "ready" && <p role="timer" aria-label="Time remaining" className="font-mono text-xl tabular-nums">{Math.floor(remaining / 60)}:{String(remaining % 60).padStart(2, "0")}</p>}</div>
    {error && <div className="space-y-3 border border-destructive/30 p-4"><p role="alert" className="text-sm text-destructive">{error}</p><p className="text-xs text-muted-foreground">Reloading replaces local edits with the last server draft.</p><PillButton size="sm" variant="secondary" disabled={!!busy} onClick={() => void transition("reload")}>Reload saved draft</PillButton></div>}
    {section.status === "ready" ? <Surface className="space-y-5 p-6"><h3 className="font-display text-2xl">Take a breath.</h3><p className="text-sm leading-relaxed">{section.instructions}</p><p className="text-sm text-muted-foreground">Your next clock starts when you press Begin. The previous section is locked.</p><PillButton disabled={!!busy} onClick={() => void transition("start")}>Begin {section.title}</PillButton></Surface>
      : expired ? <Surface className="space-y-4 p-6"><h3 className="font-display text-2xl">Time is up.</h3><p className="text-sm">Only answers saved before the deadline will count. This section can no longer be edited.</p><PillButton disabled={!!busy} onClick={() => void transition("finish")}>Close expired section</PillButton></Surface>
      : question && <>
        <div className="flex flex-wrap items-center justify-between gap-3"><p role="status" className="text-xs text-muted-foreground">{busy === "saving" ? "Saving…" : dirty ? "Unsaved edits · autosaves after a short pause" : "Saved to your account"}</p><PillButton size="sm" variant="secondary" disabled={!!busy} onClick={() => void save(index, true)}>Save now</PillButton></div>
        <details className="border-y border-border py-3"><summary className="cursor-pointer text-sm">Review all questions · {unanswered} unanswered</summary><div className="mt-4 grid grid-cols-6 gap-2 sm:grid-cols-9">{exam.questions.map((q, position) => <button key={q.id} type="button" disabled={!!busy} aria-current={position === index ? "step" : undefined} aria-label={`Go to question ${position + 1}${answers[q.id]?.selected_option_id || answers[q.id]?.free_response_text?.trim() ? ", answered" : ", unanswered"}`} className="rounded-lg border border-border p-2 text-sm aria-[current=step]:border-blue aria-[current=step]:bg-blue-soft" onClick={() => void save(position, true)}>{position + 1}</button>)}</div></details>
        <Surface className="space-y-6 p-5 sm:p-8"><p className="font-mono text-xs text-muted-foreground">Question {index + 1} / {exam.questions.length}</p><p className="whitespace-pre-wrap text-base leading-relaxed">{question.prompt}</p><fieldset disabled={busy === "working"}>
          {question.type === "mcq" ? <McqQuestionForm question={question} selectedOptionId={answers[question.id]?.selected_option_id} onSelect={id => edit({ selected_option_id: id })} /> : <FrqQuestionForm value={answers[question.id]?.free_response_text ?? ""} onChange={text => edit({ free_response_text: text })} />}
        </fieldset><div className="flex flex-wrap justify-between gap-3"><PillButton variant="secondary" disabled={!!busy || index === 0} onClick={() => void save(index - 1, true)}>Previous</PillButton>{index + 1 < exam.questions.length && <PillButton disabled={!!busy} onClick={() => void save(index + 1, true)}>Next question</PillButton>}</div></Surface>
        {confirm ? <div className="space-y-4 border border-border p-5"><p className="text-sm">{unanswered} unanswered. Closing this section permanently locks its answers. You cannot return to it.</p><div className="flex flex-wrap gap-3"><PillButton disabled={!!busy} onClick={() => void transition("finish")}>Save and close section</PillButton><PillButton variant="secondary" disabled={!!busy} onClick={() => setConfirm(false)}>Keep working</PillButton></div></div> : <PillButton variant="secondary" disabled={!!busy} onClick={() => setConfirm(true)}>Finish section</PillButton>}
      </>}
    {!dirty && <PillLink href="/practice" size="sm" variant="ghost">{section.status === "ready" ? "Leave page · break remains untimed" : "Leave page · clock continues"}</PillLink>}
  </div>;
}
