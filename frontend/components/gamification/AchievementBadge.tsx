import { Badge as BadgeType } from "@/lib/api";

export function AchievementBadge({ badge }: { badge: BadgeType }) {
  return (
    <div className="flex items-center gap-3 rounded-md border p-3">
      <span className="text-2xl leading-none">{badge.icon ?? "🏅"}</span>
      <div className="space-y-0.5">
        <p className="text-sm font-medium">{badge.name}</p>
        {badge.description && <p className="text-xs text-muted-foreground">{badge.description}</p>}
      </div>
    </div>
  );
}
