import { Badge as BadgeType } from "@/lib/api";

export function AchievementBadge({ badge }: { badge: BadgeType }) {
  return (
    <div className="flex items-center gap-3 rounded-2xl bg-muted/40 p-4">
      <span className="flex size-10 shrink-0 items-center justify-center rounded-full bg-card text-xl leading-none shadow-hairline">
        {badge.icon ?? "🏅"}
      </span>
      <div className="min-w-0 space-y-0.5">
        <p className="text-sm font-medium text-ink">{badge.name}</p>
        {badge.description && (
          <p className="text-xs leading-relaxed text-muted-foreground">{badge.description}</p>
        )}
      </div>
    </div>
  );
}
