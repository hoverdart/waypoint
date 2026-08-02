import { ReactNode } from "react";
import { Compass, Brain, Lightbulb, Gauge } from "lucide-react";
import { Surface } from "@/components/kit/Surface";
import { Reveal } from "@/components/motion/Reveal";
import { SectionHeading } from "@/components/kit/Typography";
import { MasteryMock, ModesMock } from "./mocks";

function BentoCard({
  icon,
  title,
  body,
  visual,
  index,
  className,
}: {
  icon: ReactNode;
  title: string;
  body: string;
  visual?: ReactNode;
  index: number;
  className?: string;
}) {
  return (
    <Reveal index={index} className={className}>
      <Surface interactive className="flex h-full flex-col gap-4 overflow-hidden p-7">
        <span className="flex size-10 items-center justify-center rounded-full bg-blue-soft text-blue">{icon}</span>
        <div>
          <h3 className="font-display text-xl text-ink">{title}</h3>
          <p className="mt-2 text-sm leading-relaxed text-muted-foreground">{body}</p>
        </div>
        {visual && <div className="mt-auto flex justify-center pt-2">{visual}</div>}
      </Surface>
    </Reveal>
  );
}

/** Asymmetric feature grid: one wide card carrying a product visual, then a
 * row of narrower supporting cards. */
export function BentoGrid() {
  return (
    <section aria-label="Why WayPoint" className="mx-auto w-full max-w-6xl px-6 py-24 sm:py-28">
      <Reveal>
        <SectionHeading
          eyebrow="Why it works"
          title={<>A study plan that can explain itself.</>}
          sub="Most tools hand you more questions. WayPoint decides what's worth your next twenty minutes, and tells you why."
        />
      </Reveal>

      <div className="mt-14 grid gap-4 lg:grid-cols-3">
        <Reveal className="lg:col-span-2">
          <Surface interactive className="flex h-full flex-col gap-8 overflow-hidden p-7 sm:flex-row sm:items-center sm:p-9">
            <div className="max-w-sm">
              <span className="flex size-10 items-center justify-center rounded-full bg-blue-soft text-blue">
                <Gauge className="size-5" aria-hidden="true" />
              </span>
              <h3 className="font-display mt-4 text-2xl text-ink">Know exactly where you stand.</h3>
              <p className="mt-3 text-sm leading-relaxed text-muted-foreground">
                Mastery, confidence and retention are tracked per topic, then rolled up into a predicted AP score
                you can actually act on — with the weak units called out by name.
              </p>
            </div>
            <div className="flex flex-1 justify-center sm:justify-end">
              <MasteryMock />
            </div>
          </Surface>
        </Reveal>

        <BentoCard
          index={1}
          icon={<Compass className="size-5" aria-hidden="true" />}
          title="Direction, not homework"
          body="Not “review Unit 4”. Something specific: you keep missing implicit differentiation after chain rule — spend twelve minutes here."
        />

        <BentoCard
          index={2}
          icon={<Brain className="size-5" aria-hidden="true" />}
          title="It remembers your mistakes"
          body="We separate didn't-know-it from careless slip from misread, and shape practice around the pattern rather than the topic."
        />

        <BentoCard
          index={3}
          icon={<Lightbulb className="size-5" aria-hidden="true" />}
          title="A reason for everything"
          body="Every pick shows what drove it: your mastery dropped, this unit is high-frequency on the exam, or we still need more evidence."
        />

        <Reveal index={4}>
          <Surface interactive className="flex h-full flex-col gap-4 p-7">
            <div>
              <h3 className="font-display text-xl text-ink">Two ways to study</h3>
              <p className="mt-2 text-sm leading-relaxed text-muted-foreground">
                Same engine underneath. Pick the version of yourself that actually shows up.
              </p>
            </div>
            <div className="mt-auto pt-2">
              <ModesMock />
            </div>
          </Surface>
        </Reveal>
      </div>
    </section>
  );
}
