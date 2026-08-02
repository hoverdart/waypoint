import { Chip } from "@/components/kit/Pills";

/** Renders the planner's plain-English "reason" string consistently everywhere
 * it appears (daily plan, practice session, results). */
export function ReasonBadge({ reason }: { reason: string }) {
  return (
    <Chip tone="neutral" className="font-normal">
      {reason}
    </Chip>
  );
}
