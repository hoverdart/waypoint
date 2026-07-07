"use client";

import { useState } from "react";
import Link from "next/link";
import { Badge } from "@/components/ui/badge";
import { Card, CardContent } from "@/components/ui/card";
import { ExplainButton } from "@/components/shared/ExplainButton";
import { WayPointButton } from "@/components/shared/WayPointButton";
import { useStartPlanItem } from "@/lib/hooks/useStartPlanItem";
import { AnswerBreakdownItem } from "@/lib/api";

/** Five-section review layout: Key idea, Why right/wrong, Fast way to
 * remember (repurposes the explanation's misconception_tag - a real trap to
 * watch for, not a fabricated mnemonic), Related AP skill and Try another
 * similar question (both need subjectId, resolved client-side from the
 * session detail rather than adding a backend field). */
export function AnswerBreakdownCard({ item, subjectId }: { item: AnswerBreakdownItem; subjectId?: number }) {
  const startPlanItem = useStartPlanItem();
  const [startingAnother, setStartingAnother] = useState(false);

  const selectedExplanation = item.explanations.find((e) => e.option_id === item.selected_option_id);
  const generalExplanation = item.explanations.find((e) => e.option_id === null);
  const misconception =
    selectedExplanation?.misconception_tag ?? item.explanations.find((e) => e.misconception_tag)?.misconception_tag;

  async function handleTryAnother() {
    if (!subjectId) return;
    setStartingAnother(true);
    try {
      await startPlanItem({ subject_id: subjectId, topic_id: item.topic_id, item_type: item.type === "frq" ? "frq" : undefined });
    } finally {
      setStartingAnother(false);
    }
  }

  return (
    <Card>
      <CardContent className="space-y-4 pt-6">
        <div className="flex items-start justify-between gap-4">
          <p className="text-sm text-navy">{item.prompt}</p>
          <Badge variant={item.is_correct ? "default" : "destructive"} className="shrink-0">
            {item.is_correct ? "Correct" : "Incorrect"}
          </Badge>
        </div>

        <p className="text-sm text-muted-foreground">
          Correct answer: <span className="font-medium text-foreground">{item.correct_answer}</span>
          {" · "}
          {item.score}/{item.max_score} pts
        </p>

        {(generalExplanation || selectedExplanation || misconception) && (
          <div className="space-y-3 rounded-xl bg-muted/50 p-4 text-sm">
            {generalExplanation && (
              <div>
                <p className="text-xs font-semibold tracking-wide text-blue uppercase">Key idea</p>
                <p className="mt-1 text-navy">{generalExplanation.explanation}</p>
              </div>
            )}
            {selectedExplanation && (
              <div>
                <p className="text-xs font-semibold tracking-wide text-blue uppercase">
                  {item.is_correct ? "Why you were right" : "Why that's wrong"}
                </p>
                <p className="mt-1 text-navy">{selectedExplanation.explanation}</p>
              </div>
            )}
            {misconception && (
              <div>
                <p className="text-xs font-semibold tracking-wide text-blue uppercase">Fast way to remember</p>
                <p className="mt-1 text-navy">Watch out for: {misconception}</p>
              </div>
            )}
          </div>
        )}

        <div className="flex flex-wrap items-center gap-3">
          {subjectId && (
            <Link
              href={`/analytics?subject=${subjectId}`}
              className="text-xs font-medium text-blue underline-offset-2 hover:underline"
            >
              Related AP skill →
            </Link>
          )}
          {subjectId && (
            <WayPointButton
              variant="secondary"
              size="sm"
              showArrow={false}
              disabled={startingAnother}
              onClick={handleTryAnother}
            >
              {startingAnother ? "Starting..." : "Try another similar question"}
            </WayPointButton>
          )}
          {!item.is_correct && (
            <ExplainButton
              questionId={item.question_id}
              selectedOptionId={item.selected_option_id}
              freeResponseText={item.free_response_text}
            />
          )}
        </div>
      </CardContent>
    </Card>
  );
}
