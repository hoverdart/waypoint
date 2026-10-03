"use client";

import { useRef, useState } from "react";
import { useRouter } from "next/navigation";
import { Inbox } from "lucide-react";
import { Surface } from "@/components/kit/Surface";
import { PillButton } from "@/components/kit/PillButton";
import { EmptyState } from "@/components/kit/EmptyState";
import { ReportQuestionDialog } from "@/components/shared/ReportQuestionDialog";
import { AnswerInput, ApiError, Question, savePracticeDraft, submitDiagnostic, submitPractice } from "@/lib/api";
import { useApiToken } from "@/lib/hooks/useApiToken";
import { QuestionProgressIndicator } from "./QuestionProgressIndicator";
import { McqQuestionForm } from "./McqQuestionForm";
import { FrqQuestionForm } from "./FrqQuestionForm";
import { ConfidenceRatingInput } from "./ConfidenceRatingInput";

interface LocalAnswer {
  selected_option_id: number | null;
  free_response_text: string;
  confidence_rating: number | null;
  hints_used: number;
  time_seconds: number;
}

function emptyAnswer(): LocalAnswer {
  return { selected_option_id: null, free_response_text: "", confidence_rating: null, hints_used: 0, time_seconds: 0 };
}

export function PracticeSessionRoot({
  sessionId,
  sessionType,
  questions,
  planItemId,
  subjectName,
  topicName,
  reason,
  initialAnswers = [],
  initialIndex = 0,
}: {
  sessionId: number;
  sessionType: string;
  questions: Question[];
  planItemId?: number;
  subjectName?: string;
  topicName?: string;
  reason?: string;
  initialAnswers?: AnswerInput[];
  initialIndex?: number;
}) {
  const router = useRouter();
  const getToken = useApiToken();
  const isDiagnostic = sessionType === "diagnostic";

  const [index, setIndex] = useState(Math.min(Math.max(0, initialIndex), Math.max(0, questions.length - 1)));
  const [answers, setAnswers] = useState<Record<number, LocalAnswer>>(() => Object.fromEntries(initialAnswers.map(a => [a.question_id, {
    selected_option_id: a.selected_option_id ?? null,
    free_response_text: a.free_response_text ?? "",
    confidence_rating: a.confidence_rating ?? null,
    hints_used: a.hints_used ?? 0,
    time_seconds: a.time_seconds ?? 0,
  }])));
  const [submitting, setSubmitting] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [saved, setSaved] = useState(initialAnswers.length > 0);
  const requestInFlight = useRef(false);
  const questionStartedAt = useRef(Date.now());

  if (questions.length === 0) {
    return (
      <div className="mx-auto w-full max-w-2xl px-6 py-16">
        <EmptyState
          icon={<Inbox className="size-5" aria-hidden="true" />}
          title="No questions available for this topic yet."
          description="Our question bank is still growing here - try a different topic for now."
        />
      </div>
    );
  }

  const question = questions[index];
  const isLast = index === questions.length - 1;
  const currentAnswer = answers[question.id] ?? emptyAnswer();
  const canAdvance =
    question.type === "mcq" ? currentAnswer.selected_option_id !== null : currentAnswer.free_response_text.trim().length > 0;

  function patchCurrentAnswer(patch: Partial<LocalAnswer>) {
    setSaved(false);
    setAnswers((prev) => ({ ...prev, [question.id]: { ...currentAnswer, ...patch } }));
  }

  async function finishSession(finalAnswers: Record<number, LocalAnswer>) {
    if (requestInFlight.current) return;
    requestInFlight.current = true;
    setSubmitting(true);
    setError(null);
    try {
      const answerInputs: AnswerInput[] = questions.map((q) => {
        const a = finalAnswers[q.id] ?? emptyAnswer();
        return {
          question_id: q.id,
          selected_option_id: a.selected_option_id,
          free_response_text: a.free_response_text || null,
          time_seconds: a.time_seconds,
          hints_used: a.hints_used,
          confidence_rating: a.confidence_rating,
        };
      });

      if (isDiagnostic) {
        await submitDiagnostic(sessionId, answerInputs, getToken);
      } else {
        await submitPractice(sessionId, answerInputs, getToken, planItemId);
      }
      router.push(`/practice/results/${sessionId}`);
    } catch (cause) {
      if (cause instanceof ApiError && cause.status === 409) {
        router.push(`/practice/results/${sessionId}`);
      } else {
        setError("Your answers are still here. We could not submit this session. Please try Finish again.");
      }
    } finally {
      requestInFlight.current = false;
      setSubmitting(false);
    }
  }

  function collectAnswers() {
    const elapsed = Math.max(0, Math.round((Date.now() - questionStartedAt.current) / 1000));
    questionStartedAt.current = Date.now();
    const updated = { ...answers, [question.id]: { ...currentAnswer, time_seconds: Math.min(86400, currentAnswer.time_seconds + elapsed) } };
    setAnswers(updated);
    return updated;
  }

  async function saveAndMove(nextIndex: number, exit = false) {
    if (requestInFlight.current) return;
    requestInFlight.current = true;
    setSubmitting(true);
    setError(null);
    const updated = collectAnswers();
    try {
      const draft = Object.entries(updated).map(([id, answer]) => ({ question_id: Number(id), ...answer }));
      await savePracticeDraft(sessionId, draft, nextIndex, getToken, planItemId);
      setSaved(true);
      if (exit) router.push("/practice");
      else setIndex(nextIndex);
      questionStartedAt.current = Date.now();
    } catch {
      setError("We couldn't save your progress. Your answers are still here—please try again before leaving.");
    } finally {
      requestInFlight.current = false;
      setSubmitting(false);
    }
  }

  function handleNext() {
    if (isLast) void finishSession(collectAnswers());
    else void saveAndMove(index + 1);
  }

  return (
    <div className="mx-auto w-full max-w-2xl space-y-7 px-6 py-10 sm:py-12">
      {(subjectName || topicName || (index === 0 && reason)) && (
        <div className="space-y-1">
          {(subjectName || topicName) && (
            <p className="text-sm font-medium text-ink">
              {[subjectName, topicName].filter(Boolean).join(" · ")}
            </p>
          )}
          {index === 0 && reason && <p className="text-sm text-muted-foreground">{reason}</p>}
        </div>
      )}
      <div className="flex items-center justify-between gap-3">
        <p role="status" className="text-xs text-muted-foreground">{saved ? "Progress saved to your account" : "Progress saves when you move between questions"}</p>
        <PillButton variant="ghost" size="sm" disabled={submitting} onClick={() => void saveAndMove(index, true)}>Save &amp; exit</PillButton>
      </div>
      {error && <p role="alert" className="rounded-md border border-destructive/30 p-4 text-sm text-destructive">{error}</p>}
      <QuestionProgressIndicator current={index + 1} total={questions.length} isDiagnostic={isDiagnostic} />

      <Surface className="space-y-7 p-6 sm:p-8">
        <p className="text-lg leading-relaxed whitespace-pre-wrap text-ink">{question.prompt}</p>

        <fieldset disabled={submitting} className="space-y-7">
        {question.type === "mcq" ? (
          <McqQuestionForm
            question={question}
            selectedOptionId={currentAnswer.selected_option_id}
            onSelect={(optionId) => patchCurrentAnswer({ selected_option_id: optionId })}
          />
        ) : (
          <FrqQuestionForm
            value={currentAnswer.free_response_text}
            onChange={(text) => patchCurrentAnswer({ free_response_text: text })}
          />
        )}

        <ConfidenceRatingInput
          value={currentAnswer.confidence_rating}
          onChange={(rating) => patchCurrentAnswer({ confidence_rating: rating })}
        />

        </fieldset>
        {question.type === "frq" && <p className="text-xs leading-relaxed text-muted-foreground">Free-response feedback uses a keyword checklist. Treat it as practice guidance, not an official AP grade.</p>}
        <div className="flex flex-wrap items-center justify-between gap-3 border-t border-border/70 pt-5">
          <div className="flex items-center gap-1">
            <PillButton
              variant="ghost"
              size="sm"
              disabled={submitting || currentAnswer.hints_used >= 100}
              onClick={() => patchCurrentAnswer({ hints_used: currentAnswer.hints_used + 1 })}
            >
              Hint used ({currentAnswer.hints_used})
            </PillButton>
            <ReportQuestionDialog questionId={question.id} />
          </div>
          <div className="flex gap-2">
          <PillButton variant="secondary" disabled={index === 0 || submitting} onClick={() => void saveAndMove(index - 1)}>Back</PillButton>
          <PillButton disabled={!canAdvance || submitting} onClick={handleNext}>
            {isLast ? (submitting ? "Submitting..." : "Finish") : "Next"}
          </PillButton>
          </div>
        </div>
      </Surface>
    </div>
  );
}
