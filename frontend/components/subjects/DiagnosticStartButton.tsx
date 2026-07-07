"use client";

import { useState } from "react";
import { useRouter } from "next/navigation";
import { WayPointButton } from "@/components/shared/WayPointButton";
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
    } finally {
      setBusy(false);
    }
  }

  return (
    <WayPointButton variant="secondary" size="sm" showArrow={false} disabled={busy} onClick={handleClick}>
      {busy ? "Starting..." : "Take diagnostic"}
    </WayPointButton>
  );
}
