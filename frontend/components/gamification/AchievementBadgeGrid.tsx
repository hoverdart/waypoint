import { Surface } from "@/components/kit/Surface";
import { Badge as BadgeType } from "@/lib/api";
import { AchievementBadge } from "./AchievementBadge";

export function AchievementBadgeGrid({ badges }: { badges: BadgeType[] }) {
  return (
    <Surface className="p-6 sm:p-7">
      <h2 className="font-display text-lg text-ink">Achievements</h2>
      {badges.length === 0 ? (
        <p className="mt-3 text-sm leading-relaxed text-muted-foreground">
          No badges yet - complete a practice session to earn your first one.
        </p>
      ) : (
        <div className="mt-5 grid gap-3 sm:grid-cols-2">
          {badges.map((badge) => (
            <AchievementBadge key={badge.id} badge={badge} />
          ))}
        </div>
      )}
    </Surface>
  );
}
