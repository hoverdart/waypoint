import { PillLink } from "@/components/kit/PillButton";

export function FinalCta() {
  return <section aria-label="Get started" className="mx-auto w-full max-w-6xl px-6 py-20 sm:py-28"><div className="grid items-center gap-8 border-l-2 border-accent-coral pl-6 sm:pl-10 md:grid-cols-[1fr_auto]"><div><p className="font-mono text-[10px] uppercase tracking-[0.18em] text-accent-coral">The next page is yours.</p><h2 className="editorial-title mt-4 text-4xl sm:text-5xl">Let’s make a start.</h2><p className="mt-5 max-w-lg text-base leading-7 text-muted-foreground">Bring your goals and a little time. We’ll help you figure out what comes next.</p></div><PillLink href="/signup" size="lg" arrow className="justify-self-start">Create your study plan</PillLink></div></section>;
}
