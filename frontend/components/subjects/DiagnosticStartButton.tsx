"use client";

import { toast } from "sonner";
import { useState } from "react";
import { useRouter } from "next/navigation";
import { PillButton } from "@/components/kit/PillButton";
import { startDiagnostic } from "@/lib/api";
import { useApiToken } from "@/lib/hooks/useApiToken";

export function DiagnosticStartButton({ subjectId }: { subjectId: number }) {
  const router = useRouter();
  const getToken = useApiToken();
  const [busy, setBusy] = useState(false);

  async function handleClick() {
    setBusy(true);
    try {
      const session = await startDiagnostic(subjectId, getToken);
      router.push(`/practice/session/${session.session_id}`);
    } catch (error) {
      toast.error(error instanceof Error ? error.message : "Could not start the diagnostic. Try again.");
    } finally {
      setBusy(false);
    }
  }

  return (
    <PillButton variant="secondary" size="sm" disabled={busy} onClick={handleClick}>
      {busy ? "Starting..." : "Take diagnostic"}
    </PillButton>
  );
}
