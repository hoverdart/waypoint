import { Hero } from "@/components/landing/Hero";
import { SubjectShowcase } from "@/components/landing/SubjectShowcase";
import { FinalCta } from "@/components/landing/FinalCta";
import { LandingFooter } from "@/components/landing/LandingFooter";

const STEPS = [
  { title: "Start where you are.", body: "A short diagnostic samples the course. Find the ideas you already understand and the ones that deserve another look.", note: "01 / FIND YOUR FOOTING" },
  { title: "Make today manageable.", body: "Set the time you have. Your daily plan prioritizes weak spots and overdue review, with a reason behind every recommendation.", note: "02 / FOLLOW YOUR PLAN" },
  { title: "Learn from every attempt.", body: "Work through original questions, read the explanations, and watch your topic mastery develop. Save a session whenever life interrupts.", note: "03 / KEEP MOVING" },
];

export default function Home() {
  return <div className="flex flex-1 flex-col overflow-x-clip">
    <Hero />
    <section aria-label="How WayPoint works" className="mx-auto w-full max-w-6xl px-6 pt-6 pb-20 sm:pb-28">
      <div className="mb-10 flex flex-wrap items-end justify-between gap-6"><h2 className="editorial-title max-w-lg text-4xl sm:text-5xl">A good plan leaves<br />room for being human.</h2><p className="max-w-xs text-sm leading-6 text-muted-foreground">You don’t need to study everything tonight.<br />You need a useful next step.</p></div>
      <div className="grid gap-8 md:grid-cols-3">{STEPS.map(step => <article key={step.note} className="border-t border-ink/30 pt-6"><p className="font-mono text-[10px] tracking-[0.14em] text-blue">{step.note}</p><h3 className="mt-5 text-xl font-semibold tracking-tight">{step.title}</h3><p className="mt-3 text-sm leading-7 text-muted-foreground">{step.body}</p></article>)}</div>
    </section>
    <SubjectShowcase />
    <FinalCta />
    <LandingFooter />
  </div>;
}
