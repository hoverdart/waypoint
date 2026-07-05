"use client";

import { useRef, useState } from "react";
import { useRouter } from "next/navigation";
import { Card, CardContent } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { ReportQuestionDialog } from "@/components/shared/ReportQuestionDialog";
import { AnswerInput, Question, submitDiagnostic, submitPractice } from "@/lib/api";
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
}: {
  sessionId: number;
  sessionType: string;
  questions: Question[];
  planItemId?: number;
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
        <Card>
          <CardContent className="space-y-2 pt-6">
            <p className="font-medium">No questions available for this topic yet.</p>
            <p className="text-sm text-muted-foreground">
              Our question bank is still growing here - try a different topic for now.
            </p>
          </CardContent>
        </Card>
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
      <QuestionProgressIndicator current={index + 1} total={questions.length} isDiagnostic={isDiagnostic} />

      <Card>
        <CardContent className="space-y-5 pt-6">
          <p className="whitespace-pre-wrap text-base">{question.prompt}</p>

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

          <div className="flex items-center justify-between border-t pt-4">
            <div className="flex items-center gap-2">
              <Button
                variant="ghost"
                size="sm"
                onClick={() => patchCurrentAnswer({ hints_used: currentAnswer.hints_used + 1 })}
              >
                Hint used ({currentAnswer.hints_used})
              </Button>
              <ReportQuestionDialog questionId={question.id} />
            </div>
            <Button disabled={!canAdvance || submitting} onClick={handleNext}>
              {isLast ? (submitting ? "Submitting..." : "Finish") : "Next"}
            </Button>
          </div>
        </CardContent>
      </Card>
    </div>
  );
}
