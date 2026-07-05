"use client";

import { useState } from "react";
import { useRouter } from "next/navigation";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Switch } from "@/components/ui/switch";
import { Label } from "@/components/ui/label";
import { UserMode, updateMe } from "@/lib/api";
import { useApiToken } from "@/lib/hooks/useApiToken";

export function ModeToggle({ initialMode }: { initialMode: UserMode }) {
  const router = useRouter();
  const getToken = useApiToken();
  const [mode, setMode] = useState(initialMode);
  const [saving, setSaving] = useState(false);

  async function handleToggle(checked: boolean) {
    const nextMode: UserMode = checked ? "gamified" : "professional";
    setMode(nextMode);
    setSaving(true);
    try {
      await updateMe({ mode: nextMode }, getToken);
      router.refresh();
    } finally {
      setSaving(false);
    }
  }

  return (
    <Card>
      <CardHeader>
        <CardTitle>Mode</CardTitle>
      </CardHeader>
      <CardContent className="flex items-center justify-between">
        <div>
          <Label htmlFor="mode-switch">Gamified mode</Label>
          <p className="text-sm text-muted-foreground">
            Same mastery engine, plus XP, streaks, and badges.
          </p>
        </div>
        <Switch id="mode-switch" checked={mode === "gamified"} disabled={saving} onCheckedChange={handleToggle} />
      </CardContent>
    </Card>
  );
}
