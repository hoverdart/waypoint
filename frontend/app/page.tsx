import { Compass, Brain, Lightbulb } from "lucide-react";
import { LinkButton } from "@/components/shared/LinkButton";
import { AnimatedPathBackground } from "@/components/brand/AnimatedPathBackground";
import { FloatingStudySignals } from "@/components/brand/FloatingStudySignals";
import { HeroPreviewCard } from "@/components/landing/HeroPreviewCard";
import { ReasonCard } from "@/components/landing/ReasonCard";
import { ModePreviewSection } from "@/components/landing/ModePreviewSection";
import { SubjectShowcase } from "@/components/landing/SubjectShowcase";
import { FinalCta } from "@/components/landing/FinalCta";
import { LandingFooter } from "@/components/landing/LandingFooter";

const REASONS = [
  {
    icon: <Compass className="size-5" aria-hidden="true" />,
    title: "Learning GPS",
    body: "Not \"study Unit 4\" - specific, actionable direction like \"you keep missing implicit differentiation after chain rule problems, spend 12 minutes here.\"",
  },
  {
    icon: <Brain className="size-5" aria-hidden="true" />,
    title: "Mistake memory",
    body: "We track why an answer was wrong - didn't know it, careless slip, misread, guessed - and personalize practice around the pattern, not just the topic.",
  },
  {
    icon: <Lightbulb className="size-5" aria-hidden="true" />,
    title: "A reason for everything",
    body: "Every recommendation shows its driving reason: your mastery dropped, this unit is high-frequency on the exam, or we just need more evidence.",
  },
];

export default function Home() {
  return (
    <div className="flex flex-1 flex-col">
      <section aria-label="Hero" className="relative isolate overflow-hidden">
        <AnimatedPathBackground />
        <FloatingStudySignals />

        <div className="mx-auto flex w-full max-w-6xl flex-col items-center gap-12 px-4 py-20 sm:py-28 lg:flex-row lg:items-center lg:justify-between lg:py-32">
          <div className="flex max-w-xl flex-col items-center gap-6 text-center lg:items-start lg:text-left">
            <span className="rounded-full border border-blue/30 bg-blue-soft px-3 py-1 text-xs font-semibold tracking-wide text-navy uppercase">
              AI-guided AP study path
            </span>
            <h1 className="font-heading text-4xl font-semibold tracking-tight text-navy sm:text-5xl">
              Every day, we tell you exactly what to study next to maximize your AP score.
            </h1>
            <p className="max-w-lg text-lg text-muted-foreground">
              WayPoint is a deterministic study GPS, not another question bank. Mastery tracking,
              a daily plan with real reasons behind it, and AI only when you&apos;re genuinely stuck.
            </p>
            <div className="flex flex-col gap-3 sm:flex-row">
              <LinkButton
                size="lg"
                href="/signup"
                className="group/hero rounded-full bg-gradient-to-r from-navy to-blue px-5 text-navy-foreground shadow-md shadow-navy/20 hover:opacity-95"
              >
                Get started free
              </LinkButton>
              <LinkButton size="lg" variant="outline" href="/login" className="rounded-full px-5">
                Log in
              </LinkButton>
            </div>
          </div>

          <div className="hidden lg:block">
            <HeroPreviewCard />
          </div>
        </div>
      </section>

      <section className="mx-auto grid w-full max-w-5xl gap-4 px-4 pb-20 sm:grid-cols-3">
        {REASONS.map((reason, i) => (
          <ReasonCard key={reason.title} icon={reason.icon} title={reason.title} body={reason.body} index={i} />
        ))}
      </section>

      <ModePreviewSection />
      <SubjectShowcase />
      <FinalCta />
      <LandingFooter />
    </div>
  );
}
