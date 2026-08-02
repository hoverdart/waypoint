import { Surface } from "@/components/kit/Surface";
import { Reveal } from "@/components/motion/Reveal";
import { Marquee } from "@/components/motion/Marquee";
import { CountUp } from "@/components/motion/CountUp";
import { Highlight, SectionHeading } from "@/components/kit/Typography";

/** What the product does, in plain numbers - not fabricated testimonials.
 * These describe how the engine behaves, so nothing here has to be attributed
 * to a person who doesn't exist. */
const FACTS = [
  { stat: 6, suffix: "", label: "AP courses mapped to real College Board unit weightings" },
  { stat: 4, suffix: " signals", label: "Mastery, confidence, retention and a per-topic timer behind every pick" },
  { stat: 100, suffix: "%", label: "Of daily plan items show the reason they were chosen" },
  { stat: 20, suffix: " min", label: "A typical daily plan — sized to the time you actually have" },
];

const REASONS = [
  "Your mastery dropped",
  "You haven't practiced this recently",
  "This unit is high-frequency on the AP exam",
  "We need more evidence to estimate your mastery",
  "Your retention is fading here",
];

export function ProofMarquee() {
  return (
    <section aria-label="How the engine reasons" className="py-24 sm:py-28">
      <div className="mx-auto w-full max-w-6xl px-6">
        <Reveal>
          <SectionHeading
            eyebrow="Under the hood"
            title={
              <>
                Deterministic by default. <Highlight tone="violet">AI only when you&apos;re stuck.</Highlight>
              </>
            }
            sub="The plan itself is math you can inspect, not a black box. Explanations are pre-written; a model only steps in when you ask for a different angle."
          />
        </Reveal>

        <div className="mt-14 grid gap-4 sm:grid-cols-2 lg:grid-cols-4">
          {FACTS.map((fact, i) => (
            <Reveal key={fact.label} index={i}>
              <Surface className="h-full p-6">
                <p className="font-display text-4xl text-ink">
                  <CountUp value={fact.stat} suffix={fact.suffix} />
                </p>
                <p className="mt-3 text-sm leading-relaxed text-muted-foreground">{fact.label}</p>
              </Surface>
            </Reveal>
          ))}
        </div>
      </div>

      {/* The actual reason strings the planner emits, drifting past. */}
      <div className="mt-14">
        <Reveal>
          <p className="mb-5 text-center text-xs font-semibold tracking-[0.14em] text-muted-foreground uppercase">
            Reasons the planner gives
          </p>
        </Reveal>
        <Marquee duration={38}>
          {REASONS.map((reason) => (
            <span
              key={reason}
              className="rounded-full border border-border/70 bg-card/80 px-5 py-3 text-sm text-ink-soft shadow-hairline backdrop-blur"
            >
              “{reason}”
            </span>
          ))}
        </Marquee>
      </div>
    </section>
  );
}
