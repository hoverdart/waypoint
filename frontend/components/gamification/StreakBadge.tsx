import { Chip } from "@/components/kit/Pills";

export function StreakBadge({ days }: { days: number }) {
  return (
    <Chip tone="amber" className="px-3 py-1.5 text-sm">
      {days > 0 ? `🔥 ${days}-day streak` : "🔥 Start a streak today"}
    </Chip>
  );
}
