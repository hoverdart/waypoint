"use client";

import { useEffect, useState } from "react";
import {
  DropdownMenu,
  DropdownMenuContent,
  DropdownMenuItem,
  DropdownMenuTrigger,
} from "@/components/ui/dropdown-menu";
import { PillButton } from "@/components/kit/PillButton";
import { ApiError, ExplainAction, explainQuestion, getAiUsage } from "@/lib/api";
import { useApiToken } from "@/lib/hooks/useApiToken";

const ACTIONS: { value: ExplainAction; label: string }[] = [
  { value: "why_wrong", label: "Why was my answer wrong?" },
  { value: "explain_differently", label: "Explain differently" },
  { value: "analogy", label: "Give an analogy" },
  { value: "easier_example", label: "Give an easier example" },
  { value: "harder_example", label: "Give a harder example" },
];

export function ExplainButton({
  questionId,
  selectedOptionId,
  freeResponseText,
}: {
  questionId: number;
  selectedOptionId?: number | null;
  freeResponseText?: string | null;
}) {
  const getToken = useApiToken();
  const [usageExhausted, setUsageExhausted] = useState(false);
  const [loading, setLoading] = useState(false);
  const [explanation, setExplanation] = useState<string | null>(null);

  useEffect(() => {
    getAiUsage(getToken)
      .then((usage) => setUsageExhausted(usage.free_used >= usage.max_allowed))
      .catch(() => {});
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

  async function handleAction(action: ExplainAction) {
    setLoading(true);
    setExplanation(null);
    try {
      const result = await explainQuestion(
        { question_id: questionId, action, selected_option_id: selectedOptionId, free_response_text: freeResponseText },
        getToken
      );
      setExplanation(result.explanation);
      setUsageExhausted(result.free_used >= result.max_allowed);
    } catch (e) {
      if (e instanceof ApiError && e.status === 429) {
        setUsageExhausted(true);
        setExplanation("You've used your AI explanations for this week - check back next week.");
      } else if (e instanceof ApiError && e.status === 503) {
        setExplanation(e.detail);
      } else {
        setExplanation("Something went wrong fetching an explanation.");
      }
    } finally {
      setLoading(false);
    }
  }

  return (
    <div className="space-y-2">
      <DropdownMenu>
        <DropdownMenuTrigger
          render={<PillButton variant="secondary" size="sm" disabled={usageExhausted || loading} />}
        >
          {loading ? "Thinking..." : "Explain with AI"}
        </DropdownMenuTrigger>
        <DropdownMenuContent className="rounded-2xl">
          {ACTIONS.map((action) => (
            <DropdownMenuItem key={action.value} onClick={() => handleAction(action.value)}>
              {action.label}
            </DropdownMenuItem>
          ))}
        </DropdownMenuContent>
      </DropdownMenu>
      {explanation && (
        <p className="rounded-2xl bg-blue-soft/50 p-4 text-sm leading-relaxed text-ink">{explanation}</p>
      )}
    </div>
  );
}
