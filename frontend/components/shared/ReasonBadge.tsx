import { Badge } from "@/components/ui/badge";

/** Renders the planner's plain-English "reason" string consistently everywhere
 * it appears (daily plan, practice session, results). */
export function ReasonBadge({ reason }: { reason: string }) {
  return (
    <Badge variant="secondary" className="font-normal">
      {reason}
    </Badge>
  );
}
