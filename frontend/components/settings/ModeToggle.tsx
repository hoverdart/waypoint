"use client";

import { useState } from "react";
import { useRouter } from "next/navigation";
import { Surface } from "@/components/kit/Surface";
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
    <Surface className="space-y-4 p-6">
      <h2 className="font-display text-lg text-ink">Mode</h2>
      <div className="flex items-center justify-between gap-4">
        <div>
          <Label htmlFor="mode-switch">Gamified mode</Label>
          <p className="text-sm text-muted-foreground">
            Same mastery engine, plus XP, streaks, and badges.
          </p>
        </div>
        <Switch id="mode-switch" checked={mode === "gamified"} disabled={saving} onCheckedChange={handleToggle} />
      </div>
    </Surface>
  );
}
