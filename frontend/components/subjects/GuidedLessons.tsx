"use client";

import { useState } from "react";
import { checkLesson, getLessons, GuidedLesson } from "@/lib/api/lessons";
import { useApiToken } from "@/lib/hooks/useApiToken";
import { PillButton } from "@/components/kit/PillButton";

export function GuidedLessons({ unitId, onPractice, practiceBusy, practiceMode = "mcq" }: {
  unitId: number; onPractice: (topicId: number) => void; practiceBusy: boolean; practiceMode?: "mcq" | "frq";
}) {
  const token = useApiToken();
  const [lessons, setLessons] = useState<GuidedLesson[] | null>(null);
  const [active, setActive] = useState(0);
  const [answer, setAnswer] = useState<number | null>(null);
  const [feedback, setFeedback] = useState<{ correct: boolean; feedback: string } | null>(null);
  const [busy, setBusy] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const lesson = lessons?.[active];
  const practiceTopicId = lesson?.practice_topic_ids?.[practiceMode] ?? null;

  async function load() {
    setBusy(true); setError(null);
    try {
      const result = await getLessons(unitId, token);
      setLessons(result);
      const next = result.findIndex(item => !item.completed);
      setActive(next < 0 ? 0 : next);
    } catch { setError("Couldn't load your lessons. Please try again."); }
    finally { setBusy(false); }
  }

  function move(index: number) {
    setActive(index); setAnswer(null); setFeedback(null); setError(null);
  }

  async function check() {
    if (!lesson || answer === null || busy) return;
    setBusy(true); setError(null);
    try {
      const result = await checkLesson(unitId, lesson, answer, token);
      setFeedback(result);
      if (result.correct) setLessons(current => current?.map(item => item.slug === lesson.slug ? { ...item, completed: true } : item) ?? null);
    } catch { setError("Couldn't save your check. Try again; your selection is still here. If this lesson was updated, reload the page."); }
    finally { setBusy(false); }
  }

  return <section aria-label="Guided lessons" className="border-l-2 border-blue bg-blue-soft/30 p-5 sm:p-7">
    {!lessons ? <><h3 className="text-lg font-semibold">Learn, then put it to work.</h3><p className="my-3 text-sm text-muted-foreground">Short explanations, worked examples, and checks you can retry. Your completed lessons are saved.</p><PillButton size="sm" disabled={busy} onClick={() => void load()}>{busy ? "Loading lessons…" : "Open guided lessons"}</PillButton></> : !lesson ? <p>No guided lessons are available for this unit yet.</p> : <>
      <p className="font-mono text-xs text-muted-foreground">{lessons.filter(item => item.completed).length} of {lessons.length} lessons completed · Skill {lesson.skill}</p>
      <nav aria-label="Lesson sequence" className="my-5 flex flex-wrap gap-2">{lessons.map((item, index) => <button key={item.slug} disabled={busy} aria-current={index === active ? "step" : undefined} onClick={() => move(index)} className={`rounded-full border px-3 py-2 text-xs focus-visible:ring-2 focus-visible:ring-ring ${index === active ? "border-blue bg-blue text-white" : "border-border"}`}>{index + 1}. {item.title}{item.completed ? " ✓" : ""}</button>)}</nav>
      <h3 className="text-2xl font-semibold tracking-tight">{lesson.title}</h3>
      <p className="mt-2 text-sm font-medium">{lesson.objective}</p>
      <div className="my-6 space-y-4 text-sm leading-7">{lesson.explanation.map((paragraph, index) => <p key={index}>{paragraph}</p>)}</div>
      <h4 className="text-sm font-semibold">See it in context</h4>
      <blockquote className="my-3 border-l border-blue pl-4 text-sm italic leading-7">{lesson.example}</blockquote>
      <p className="text-xs text-muted-foreground">Original fictional example</p>
      <p className="my-4 text-sm leading-7">{lesson.walkthrough}</p>
      <fieldset disabled={busy} className="mt-6 space-y-3"><legend className="mb-3 text-sm font-semibold">Try it: {lesson.prompt}</legend>{lesson.options.map((option, index) => <label key={index} className="flex cursor-pointer gap-3 rounded-md border border-border bg-background p-3 text-sm leading-6"><input className="mt-1.5" type="radio" name={`lesson-${unitId}-${lesson.slug}`} checked={answer === index} onChange={() => { setAnswer(index); setFeedback(null); }} />{option}</label>)}</fieldset>
      <PillButton className="mt-4" size="sm" disabled={busy || answer === null} onClick={() => void check()}>{busy ? "Saving…" : "Check understanding"}</PillButton>
      {feedback && <div role="status" className="mt-4 text-sm leading-6"><p className="font-semibold">{feedback.correct ? "Lesson complete" : "Take another look"}</p><p>{feedback.feedback}</p></div>}
      <div className="mt-6 flex flex-wrap gap-3">{active < lessons.length - 1 && <PillButton size="sm" disabled={busy} onClick={() => move(active + 1)}>Next lesson</PillButton>}<PillButton size="sm" disabled={busy || practiceBusy || practiceTopicId === null} onClick={() => { if (practiceTopicId !== null) onPractice(practiceTopicId); }}>Apply it in practice</PillButton></div>
      <p className="mt-3 text-xs text-muted-foreground">{practiceTopicId !== null ? `Practice will focus on skill ${lesson.skill} in your selected format.` : `No ${practiceMode === "mcq" ? "multiple-choice" : "free-response"} practice is available for this lesson yet. Choose another format or use the unit practice below.`}</p>
      <p className="mt-4 text-xs text-muted-foreground">A completed check records your lesson progress. Practice separately to develop and measure your skills.</p>
    </>}
    {error && <p role="alert" className="mt-4 text-sm text-destructive">{error}</p>}
  </section>;
}
