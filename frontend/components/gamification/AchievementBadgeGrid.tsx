import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Badge as BadgeType } from "@/lib/api";
import { AchievementBadge } from "./AchievementBadge";

export function AchievementBadgeGrid({ badges }: { badges: BadgeType[] }) {
  return (
    <Card>
      <CardHeader>
        <CardTitle>Achievements</CardTitle>
      </CardHeader>
      <CardContent>
        {badges.length === 0 ? (
          <p className="text-sm text-muted-foreground">
            No badges yet - complete a practice session to earn your first one.
          </p>
        ) : (
          <div className="grid gap-2 sm:grid-cols-2">
            {badges.map((badge) => (
              <AchievementBadge key={badge.id} badge={badge} />
            ))}
          </div>
        )}
      </CardContent>
    </Card>
  );
}
