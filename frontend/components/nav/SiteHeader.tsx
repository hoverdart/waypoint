import Link from "next/link";
import { Show, UserButton } from "@clerk/nextjs";
import { LinkButton } from "@/components/shared/LinkButton";
import { ExamCountdown } from "@/components/shared/ExamCountdown";
import { LogoLockup } from "@/components/brand/Logo";
import { NavLinks } from "@/components/nav/NavLinks";
import { DashboardSubjectSummary, getDashboard } from "@/lib/api";
import { getServerAuthToken } from "@/lib/auth/getServerAuthToken";

/** Compact "current AP courses + nearest exam" strip for the signed-in
 * header. Fails silently (renders nothing) on any auth/fetch hiccup, since
 * losing this decoration shouldn't take down the header on every route. */
async function HeaderCourseStrip() {
  const token = await getServerAuthToken();
  if (!token) return null;

  let subjects: DashboardSubjectSummary[] = [];
  try {
    subjects = (await getDashboard(token)).subjects;
  } catch {
    return null;
  }
  if (subjects.length === 0) return null;

  const nearestExam = subjects
    .filter((s) => s.exam_date)
    .sort((a, b) => (a.exam_date! < b.exam_date! ? -1 : 1))[0];

  return (
    <div className="hidden items-center gap-2 border-l border-white/10 pl-4 lg:flex">
      {subjects.slice(0, 4).map((subject) => (
        <span
          key={subject.subject_id}
          className="rounded-full bg-white/10 px-2.5 py-1 text-xs font-medium text-navy-foreground/85"
        >
          {subject.subject_name}
        </span>
      ))}
      {nearestExam && <ExamCountdown examDate={nearestExam.exam_date} tone="dark" />}
    </div>
  );
}

export async function SiteHeader() {
  return (
    <header className="sticky top-0 z-40 border-b border-white/10 bg-navy/95 backdrop-blur-md">
      <div className="mx-auto flex h-16 max-w-6xl items-center justify-between gap-4 px-4">
        <div className="flex items-center gap-4">
          <Link href="/" className="transition-opacity hover:opacity-80">
            <LogoLockup variant="light" />
          </Link>
          <Show when="signed-in">
            <HeaderCourseStrip />
          </Show>
        </div>

        <Show when="signed-in">
          <NavLinks />
        </Show>

        <div className="flex items-center gap-3">
          <Show when="signed-in">
            <Link
              href="/settings"
              className="rounded-lg px-3 py-1.5 text-sm font-medium text-navy-foreground/65 transition-colors hover:bg-white/10 hover:text-navy-foreground"
            >
              Settings
            </Link>
            <span className="rounded-full ring-2 ring-white/20">
              <UserButton />
            </span>
          </Show>
          <Show when="signed-out">
            <LinkButton
              variant="ghost"
              href="/login"
              className="text-navy-foreground/80 hover:bg-white/10 hover:text-navy-foreground"
            >
              Log in
            </LinkButton>
            <LinkButton href="/signup" className="bg-white text-navy hover:bg-white/90">
              Sign up
            </LinkButton>
          </Show>
        </div>
      </div>
    </header>
  );
}
