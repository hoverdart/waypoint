"use client";

import { Tooltip, TooltipContent, TooltipTrigger } from "@/components/ui/tooltip";
import { PillButton } from "@/components/kit/PillButton";

/** Visibly present but honestly non-functional - there's no backend support
 * yet for regenerating a plan against a different time budget. Shown with
 * an explanatory tooltip rather than hidden, per the redesign brief's
 * "regenerate for less time" ask. Uses aria-disabled (not the native
 * `disabled` attribute) so it stays hoverable/focusable for the tooltip. */
export function RegenerateTimeBudgetControl() {
  return (
    <Tooltip>
      <TooltipTrigger
        render={
          <PillButton
            variant="secondary"
            size="sm"
            aria-disabled="true"
            className="cursor-not-allowed opacity-60"
            onClick={(e) => e.preventDefault()}
          >
            Regenerate for less time
          </PillButton>
        }
      />
      <TooltipContent>Adjusting today&apos;s plan for a shorter session isn&apos;t available yet.</TooltipContent>
    </Tooltip>
  );
}
