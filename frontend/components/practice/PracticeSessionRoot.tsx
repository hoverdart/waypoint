"use client";

import { useRef, useState } from "react";
import { useRouter } from "next/navigation";
import { CardContent } from "@/components/ui/card";
import { WayPointCard } from "@/components/shared/WayPointCard";
import { WayPointButton } from "@/components/shared/WayPointButton";
import { ReportQuestionDialog } from "@/components/shared/ReportQuestionDialog";
import { AnswerInput, Question, submitDiagnostic, submitPractice } from "@/lib/api";
import { useApiToken } from "@/lib/hooks/useApiToken";
import { StudySessionHeader } from "./StudySessionHeader";
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
}: {
  sessionId: number;
  sessionType: string;
  questions: Question[];
  planItemId?: number;
  subjectName?: string;
  topicName?: string;
  reason?: string;
}) {
  const router = useRouter();
  const getToken = useApiToken();
  const isDiagnostic = sessionType === "diagnostic";

  const [index, setIndex] = useState(0);
  const [answers, setAnswers] = useState<Record<number, LocalAnswer>>({});
  const [submitting, setSubmitting] = useState(false);
  const questionStartedAt = useRef(Date.now());

  if (questions.length === 0) {
    return (
      <div className="mx-auto w-full max-w-2xl px-4 py-16 text-center">
        <WayPointCard elevated>
          <CardContent className="space-y-2 pt-6">
            <p className="font-medium text-navy">No questions available for this topic yet.</p>
            <p className="text-sm text-muted-foreground">
              Our question bank is still growing here - try a different topic for now.
            </p>
          </CardContent>
        </WayPointCard>
      </div>
    );
  }

  const question = questions[index];
  const isLast = index === questions.length - 1;
  const currentAnswer = answers[question.id] ?? emptyAnswer();
  const canAdvance =
    question.type === "mcq" ? currentAnswer.selected_option_id !== null : currentAnswer.free_response_text.trim().length > 0;

  function patchCurrentAnswer(patch: Partial<LocalAnswer>) {
    setAnswers((prev) => ({ ...prev, [question.id]: { ...currentAnswer, ...patch } }));
  }

  async function finishSession(finalAnswers: Record<number, LocalAnswer>) {
    setSubmitting(true);
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
    } finally {
      setSubmitting(false);
    }
  }

  function handleNext() {
    const elapsed = Math.round((Date.now() - questionStartedAt.current) / 1000);
    const finalAnswers = { ...answers, [question.id]: { ...currentAnswer, time_seconds: elapsed } };
    setAnswers(finalAnswers);

    if (isLast) {
      void finishSession(finalAnswers);
    } else {
      setIndex((i) => i + 1);
      questionStartedAt.current = Date.now();
    }
  }

  return (
    <div className="mx-auto w-full max-w-2xl space-y-6 px-4 py-8">
      <StudySessionHeader
        current={index + 1}
        total={questions.length}
        isDiagnostic={isDiagnostic}
        subjectName={subjectName}
        topicName={topicName}
        reason={index === 0 ? reason : undefined}
      />

      <WayPointCard elevated>
        <CardContent className="space-y-5 pt-6">
          <p className="whitespace-pre-wrap text-base text-navy">{question.prompt}</p>

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

          <div className="flex items-center justify-between border-t border-border/70 pt-4">
            <div className="flex items-center gap-2">
              <WayPointButton
                variant="ghost"
                size="sm"
                showArrow={false}
                onClick={() => patchCurrentAnswer({ hints_used: currentAnswer.hints_used + 1 })}
              >
                Hint used ({currentAnswer.hints_used})
              </WayPointButton>
              <ReportQuestionDialog questionId={question.id} />
            </div>
            <WayPointButton showArrow={false} disabled={!canAdvance || submitting} onClick={handleNext}>
              {isLast ? (submitting ? "Submitting..." : "Finish") : "Next"}
            </WayPointButton>
          </div>
        </CardContent>
      </WayPointCard>
    </div>
  );
}
