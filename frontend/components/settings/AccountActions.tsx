"use client";

import { useState } from "react";
import { useClerk } from "@clerk/nextjs";
import { PillButton } from "@/components/kit/PillButton";

export function AccountActions() {
  const clerk = useClerk();
  const [busy, setBusy] = useState(false);
  const [error, setError] = useState<string | null>(null);

  async function signOut() {
    setBusy(true);
    setError(null);
    try {
      await clerk.signOut({ redirectUrl: "/" });
    } catch {
      setError("Could not sign out. Please try again.");
      setBusy(false);
    }
  }

  return <div className="mt-4 space-y-3">
    <div className="flex flex-wrap gap-3">
      <PillButton variant="secondary" size="sm" onClick={() => clerk.openUserProfile()}>Manage account</PillButton>
      <PillButton variant="ghost" size="sm" disabled={busy} onClick={() => void signOut()}>{busy ? "Signing out…" : "Sign out"}</PillButton>
    </div>
    {error && <p role="alert" className="text-sm text-destructive">{error}</p>}
  </div>;
}
