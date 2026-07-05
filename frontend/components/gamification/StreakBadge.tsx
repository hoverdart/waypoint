import { Badge } from "@/components/ui/badge";

export function StreakBadge({ days }: { days: number }) {
  return (
    <Badge variant="secondary" className="gap-1 text-sm">
      {days > 0 ? `🔥 ${days}-day streak` : "🔥 Start a streak today"}
    </Badge>
  );
}
