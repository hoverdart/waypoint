"use client";

import { QuestionDataTable } from "@/components/practice/QuestionDataTable";

import Link from "next/link";
import { RubricSelfReview } from "./RubricSelfReview";
import { useState } from "react";
import { Surface } from "@/components/kit/Surface";
import { PillButton } from "@/components/kit/PillButton";
import { Chip } from "@/components/kit/Pills";
import { ExplainButton } from "@/components/shared/ExplainButton";
import { AnswerBreakdownItem } from "@/lib/api";
import { useStartPlanItem } from "@/lib/hooks/useStartPlanItem";

export function AnswerBreakdownCard({ item, subjectId, sessionId }: { item: AnswerBreakdownItem; subjectId?: number; sessionId?: number }) {
  const selfReview = item.scoring_method === "self_review";
  const startPlanItem = useStartPlanItem();
  const [startingAnother, setStartingAnother] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const selectedOption = item.options?.find(option => option.id === item.selected_option_id);
  const correctOption = item.options?.find(option => option.label === item.correct_answer);
  const selectedExplanation = item.explanations.find((e) => e.option_id === item.selected_option_id);
  const generalExplanation = item.explanations.find((e) => e.option_id === null);
  const misconception =
    selectedExplanation?.misconception_tag ?? generalExplanation?.misconception_tag;

  async function handleTryAnother() {
    if (!subjectId) return;
    setStartingAnother(true);
    setError(null);
    try {
      await startPlanItem({
        subject_id: subjectId,
        topic_id: item.topic_id,
        item_type: item.type === "frq" ? "frq" : undefined,
      });
    } catch {
      setError("Could not start another question. Please try again.");
    } finally {
      setStartingAnother(false);
    }
  }

  return (
    <Surface className="space-y-4 p-5 sm:p-6">
      <div className="flex items-start justify-between gap-4">
        <QuestionDataTable table={item.data_table} />
        <p className="whitespace-pre-wrap [overflow-wrap:anywhere] text-sm leading-relaxed text-ink">{item.prompt}</p>
        <Chip tone={item.is_correct ? "green" : "coral"} dot className="shrink-0">
          {selfReview ? "Rubric self-review" : item.type === "frq" ? "Checklist feedback" : item.is_correct ? "Correct" : "Incorrect"}
        </Chip>
      </div>

      <div className="space-y-3 text-sm">
        <div><p className="text-xs font-semibold text-muted-foreground">Your answer</p><p className="mt-1 whitespace-pre-wrap [overflow-wrap:anywhere] text-ink">{item.type === "frq" ? item.free_response_text || "No response" : selectedOption ? `${selectedOption.label}. ${selectedOption.text}` : "No answer recorded"}</p></div>
        <div><p className="text-xs font-semibold text-muted-foreground">{item.type === "frq" ? "Model response" : "Correct answer"}</p><p className="mt-1 whitespace-pre-wrap [overflow-wrap:anywhere] text-ink">{correctOption ? `${correctOption.label}. ${correctOption.text}` : item.correct_answer}</p></div>
        {!selfReview && <p className="text-muted-foreground">{item.score}/{item.max_score} pts</p>}
        {item.type === "frq" && !selfReview && <div className="border-t border-border pt-3">
          <p className="font-medium">Review your reasoning</p>
          <ul className="mt-2 list-disc space-y-2 pl-5">{item.rubric?.map((criterion, index) => <li key={index}>{criterion.point} <span className="text-muted-foreground">({criterion.points} pts)</span></li>)}</ul>
          <p className="mt-3 text-xs leading-relaxed text-muted-foreground">The automated score checks keywords, not the quality of your reasoning. Compare your work with each criterion and the model response. This is practice feedback, not an official AP grade.</p>
        </div>}
      </div>
      {selfReview && sessionId && <RubricSelfReview item={item} sessionId={sessionId} />}
      {error && <p role="alert" className="text-sm text-destructive">{error}</p>}

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
        {!item.is_correct && !selfReview && (
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
