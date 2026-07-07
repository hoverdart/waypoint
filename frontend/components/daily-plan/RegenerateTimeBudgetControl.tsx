"use client";

import { Tooltip, TooltipContent, TooltipTrigger } from "@/components/ui/tooltip";
import { WayPointButton } from "@/components/shared/WayPointButton";

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
          <WayPointButton
            variant="secondary"
            size="sm"
            showArrow={false}
            aria-disabled="true"
            className="cursor-not-allowed opacity-60"
            onClick={(e) => e.preventDefault()}
          >
            Regenerate for less time
          </WayPointButton>
        }
      />
      <TooltipContent>Adjusting today&apos;s plan for a shorter session isn&apos;t available yet.</TooltipContent>
    </Tooltip>
  );
}
