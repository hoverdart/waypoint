"use client";

import Link from "next/link";
import { useState } from "react";
import { Surface } from "@/components/kit/Surface";
import { PillButton } from "@/components/kit/PillButton";
import { Chip } from "@/components/kit/Pills";
import { ExplainButton } from "@/components/shared/ExplainButton";
import { AnswerBreakdownItem } from "@/lib/api";
import { useStartPlanItem } from "@/lib/hooks/useStartPlanItem";

export function AnswerBreakdownCard({ item, subjectId }: { item: AnswerBreakdownItem; subjectId?: number }) {
  const startPlanItem = useStartPlanItem();
  const [startingAnother, setStartingAnother] = useState(false);
  const selectedExplanation = item.explanations.find((e) => e.option_id === item.selected_option_id);
  const generalExplanation = item.explanations.find((e) => e.option_id === null);
  const misconception =
    selectedExplanation?.misconception_tag ?? item.explanations.find((explanation) => explanation.misconception_tag)?.misconception_tag;

  async function handleTryAnother() {
    if (!subjectId) return;
    setStartingAnother(true);
    try {
      await startPlanItem({
        subject_id: subjectId,
        topic_id: item.topic_id,
        item_type: item.type === "frq" ? "frq" : undefined,
      });
    } finally {
      setStartingAnother(false);
    }
  }

  return (
    <Surface className="space-y-4 p-5 sm:p-6">
      <div className="flex items-start justify-between gap-4">
        <p className="text-sm leading-relaxed text-ink">{item.prompt}</p>
        <Chip tone={item.is_correct ? "green" : "coral"} dot className="shrink-0">
          {item.is_correct ? "Correct" : "Incorrect"}
        </Chip>
      </div>

      <p className="text-sm text-muted-foreground">
        Correct answer: <span className="font-medium text-ink">{item.correct_answer}</span>
        {" · "}
        {item.score}/{item.max_score} pts
      </p>

      {(generalExplanation || selectedExplanation || misconception) && (
        <div className="space-y-3 rounded-2xl bg-blue-soft/50 p-4 text-sm leading-relaxed text-ink">
          {generalExplanation && (
            <div>
              <p className="text-xs font-semibold tracking-[0.12em] text-blue uppercase">Key idea</p>
              <p className="mt-1">{generalExplanation.explanation}</p>
            </div>
          )}
          {selectedExplanation && (
            <div>
              <p className="text-xs font-semibold tracking-[0.12em] text-blue uppercase">
                {item.is_correct ? "Why you were right" : "Why that’s wrong"}
              </p>
              <p className="mt-1">{selectedExplanation.explanation}</p>
            </div>
          )}
          {misconception && (
            <div>
              <p className="text-xs font-semibold tracking-[0.12em] text-blue uppercase">Fast way to remember</p>
              <p className="mt-1">Watch out for: {misconception}</p>
            </div>
          )}
        </div>
      )}

      <div className="flex flex-wrap items-center gap-3">
        {subjectId && (
          <Link href={`/analytics?subject=${subjectId}`} className="text-xs font-medium text-blue hover:underline">
            Related AP skill
          </Link>
        )}
        {subjectId && (
          <PillButton variant="secondary" size="sm" disabled={startingAnother} onClick={handleTryAnother}>
            {startingAnother ? "Starting..." : "Try another similar question"}
          </PillButton>
        )}
        {!item.is_correct && (
          <ExplainButton
            questionId={item.question_id}
            selectedOptionId={item.selected_option_id}
            freeResponseText={item.free_response_text}
          />
        )}
      </div>
    </Surface>
  );
}
