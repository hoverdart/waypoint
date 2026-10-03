import { redirect } from "next/navigation";
import { getPracticeHistory } from "@/lib/api";
import { getServerAuthToken } from "@/lib/auth/getServerAuthToken";
import { PracticeHistory } from "@/components/practice/PracticeHistory";
import { PillLink } from "@/components/kit/PillButton";

export default async function PracticePage() {
  const token = await getServerAuthToken();
  if (!token) redirect("/login");
  const sessions = await getPracticeHistory(token);
  return <div className="mx-auto w-full max-w-5xl px-6 py-12">
    <header className="mb-12 flex flex-wrap items-end justify-between gap-6"><div><p className="font-mono text-xs uppercase tracking-[0.2em] text-blue">The practice notebook</p><h1 className="editorial-title mt-4 text-5xl sm:text-6xl">Every attempt counts.</h1><p className="mt-5 max-w-xl text-muted-foreground">Pick up where you left off, or look back at what you learned.</p></div><PillLink href="/subjects" variant="secondary" arrow>Start a new session</PillLink></header>
    <PracticeHistory initialSessions={sessions} />
  </div>;
}
