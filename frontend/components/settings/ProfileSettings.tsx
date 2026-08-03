"use client";

import { useState } from "react";
import { useRouter } from "next/navigation";
import { ApiError, updateMe } from "@/lib/api";
import { useApiToken } from "@/lib/hooks/useApiToken";
import { Surface } from "@/components/kit/Surface";
import { PillButton } from "@/components/kit/PillButton";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";

const GRADES = [9, 10, 11, 12];

export function ProfileSettings({ initialName, initialGrade }: { initialName: string | null; initialGrade?: number | null }) {
  const router = useRouter();
  const getToken = useApiToken();
  const [name, setName] = useState(initialName ?? "");
  const [grade, setGrade] = useState(initialGrade?.toString() ?? "");
  const [saving, setSaving] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const valid = name.trim().length > 0 && GRADES.includes(Number(grade));

  async function handleSubmit(event: React.FormEvent<HTMLFormElement>) {
    event.preventDefault();
    if (!valid) return;
    setSaving(true);
    setError(null);
    try {
      await updateMe({ display_name: name.trim(), grade_level: Number(grade) }, getToken);
      router.refresh();
    } catch (cause) {
      setError(cause instanceof ApiError ? cause.detail : "We couldn't save your profile. Please try again.");
    } finally {
      setSaving(false);
    }
  }

  return (
    <Surface className="p-6">
      <form className="space-y-5" onSubmit={handleSubmit}>
        <div>
          <h2 className="font-display text-lg text-ink">Profile</h2>
          <p className="mt-1 text-sm text-muted-foreground">These details personalize your WayPoint experience.</p>
        </div>
        <div className="grid gap-4 sm:grid-cols-2">
          <div className="space-y-1.5">
            <Label htmlFor="settings-display-name">Name</Label>
            <Input id="settings-display-name" autoComplete="name" value={name} onChange={(event) => setName(event.target.value)} />
          </div>
          <div className="space-y-1.5">
            <Label htmlFor="settings-grade">Grade</Label>
            <select
              id="settings-grade"
              value={grade}
              onChange={(event) => setGrade(event.target.value)}
              className="h-8 w-full rounded-lg border border-input bg-transparent px-2.5 text-sm outline-none focus-visible:border-ring focus-visible:ring-3 focus-visible:ring-ring/50"
            >
              <option value="">Select grade</option>
              {GRADES.map((level) => <option key={level} value={level}>{level}th grade</option>)}
            </select>
          </div>
        </div>
        {error && <p role="alert" className="text-sm text-destructive">{error}</p>}
        <PillButton type="submit" disabled={!valid || saving}>{saving ? "Saving..." : "Save profile"}</PillButton>
      </form>
    </Surface>
  );
}
