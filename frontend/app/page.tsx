import { Hero } from "@/components/landing/Hero";
import { BentoGrid } from "@/components/landing/BentoGrid";
import { SubjectShowcase } from "@/components/landing/SubjectShowcase";
import { ProofMarquee } from "@/components/landing/ProofMarquee";
import { FinalCta } from "@/components/landing/FinalCta";
import { LandingFooter } from "@/components/landing/LandingFooter";
import { ScrollScene, type ScrollStep } from "@/components/motion/ScrollScene";
import { SectionHeading } from "@/components/kit/Typography";
import { Reveal } from "@/components/motion/Reveal";
import { DiagnoseMock, MasteryMock, PlanMock } from "@/components/landing/mocks";

/** The pinned scroll sequence. These visuals are server-rendered here and
 * handed to ScrollScene as JSX slots, which is why the mocks stay hook-free. */
const STEPS: ScrollStep[] = [
  {
    eyebrow: "Step one",
    title: "Start with an honest baseline.",
    body: "A short diagnostic spreads questions across the whole course, weighted the way the real exam is. Twenty questions in, WayPoint knows which units are actually shaky.",
    visual: <DiagnoseMock />,
  },
  {
    eyebrow: "Step two",
    title: "Get one plan, sized to your day.",
    body: "Tell us you have twenty minutes and you get a twenty-minute plan — the highest-priority topics first, each one carrying the reason it made the cut.",
    visual: <PlanMock />,
  },
  {
    eyebrow: "Step three",
    title: "Watch readiness move.",
    body: "Every session updates mastery, confidence and retention per topic, rolls up into a predicted AP score, and reshapes tomorrow's plan automatically.",
    visual: <MasteryMock />,
  },
];

export default function Home() {
  return (
    <div className="flex flex-1 flex-col">
      <Hero visual={<PlanMock />} />

      <BentoGrid />

      <div className="mx-auto w-full max-w-6xl px-6">
        <Reveal>
          <SectionHeading
            eyebrow="How it works"
            title="Three steps, then it runs itself."
            sub="Scroll through the loop WayPoint repeats every single day."
          />
        </Reveal>
      </div>
      <ScrollScene steps={STEPS} label="How WayPoint works" className="mt-10" />

      <ProofMarquee />
      <SubjectShowcase />
      <FinalCta />
      <LandingFooter />
    </div>
  );
}
