import { Card, CardContent } from "@/components/ui/card";
import { LinkButton } from "@/components/shared/LinkButton";

const REASONS = [
  {
    title: "Learning GPS",
    body: "Not \"study Unit 4\" - specific, actionable direction like \"you keep missing implicit differentiation after chain rule problems, spend 12 minutes here.\"",
  },
  {
    title: "Mistake memory",
    body: "We track why an answer was wrong - didn't know it, careless slip, misread, guessed - and personalize practice around the pattern, not just the topic.",
  },
  {
    title: "A reason for everything",
    body: "Every recommendation shows its driving reason: your mastery dropped, this unit is high-frequency on the exam, or we just need more evidence.",
  },
];

const SUBJECTS = [
  "AP Calculus AB",
  "AP Biology",
  "AP Psychology",
  "AP US History",
  "AP Chemistry",
  "AP Computer Science A",
];

export default function Home() {
  return (
    <div className="flex flex-1 flex-col">
      <section className="mx-auto flex w-full max-w-4xl flex-1 flex-col items-center justify-center gap-6 px-4 py-24 text-center">
        <h1 className="max-w-2xl text-4xl font-semibold tracking-tight sm:text-5xl">
          Every day, we tell you exactly what to study next to maximize your AP score.
        </h1>
        <p className="max-w-xl text-lg text-muted-foreground">
          WayPoint is a deterministic study GPS, not another question bank. Mastery tracking,
          a daily plan with real reasons behind it, and AI only when you&apos;re genuinely stuck.
        </p>
        <div className="flex flex-col gap-3 sm:flex-row">
          <LinkButton size="lg" href="/signup">
            Get started free
          </LinkButton>
          <LinkButton size="lg" variant="outline" href="/login">
            Log in
          </LinkButton>
        </div>
      </section>

      <section className="mx-auto grid w-full max-w-5xl gap-4 px-4 pb-20 sm:grid-cols-3">
        {REASONS.map((reason) => (
          <Card key={reason.title}>
            <CardContent className="pt-6">
              <h2 className="mb-2 font-medium">{reason.title}</h2>
              <p className="text-sm text-muted-foreground">{reason.body}</p>
            </CardContent>
          </Card>
        ))}
      </section>

      <section className="mx-auto w-full max-w-4xl px-4 pb-24 text-center">
        <p className="mb-4 text-sm font-medium text-muted-foreground">Launching with</p>
        <div className="flex flex-wrap justify-center gap-2">
          {SUBJECTS.map((subject) => (
            <span
              key={subject}
              className="rounded-full border px-3 py-1 text-sm text-muted-foreground"
            >
              {subject}
            </span>
          ))}
        </div>
      </section>
    </div>
  );
}
