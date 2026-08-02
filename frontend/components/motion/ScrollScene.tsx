"use client";

import { ReactNode, useRef, useState } from "react";
import { motion, useMotionValueEvent, useScroll } from "framer-motion";
import { useSafeReducedMotion } from "@/components/motion/useSafeReducedMotion";
import { cn } from "@/lib/utils";

export interface ScrollStep {
  eyebrow: string;
  title: string;
  body: string;
  visual: ReactNode;
}

const EASE = [0.22, 1, 0.36, 1] as const;

function StepPanel({
  step,
  index,
  active,
}: {
  step: ScrollStep;
  index: number;
  active: number;
}) {
  const isActive = index === active;
  const hasPassed = index < active;

  return (
    <motion.div
      // Steps are stacked; only the active one is visible, reachable and
      // exposed to assistive tech. The others slide out the way they came.
      animate={{ opacity: isActive ? 1 : 0, y: isActive ? 0 : hasPassed ? -28 : 28 }}
      transition={{ duration: 0.5, ease: EASE }}
      aria-hidden={!isActive}
      className={cn(
        "absolute inset-0 grid items-center gap-10 lg:grid-cols-2",
        isActive ? "pointer-events-auto" : "pointer-events-none"
      )}
    >
      <div className="max-w-md">
        <p className="text-xs font-semibold tracking-[0.14em] text-blue uppercase">{step.eyebrow}</p>
        <h3 className="font-display mt-3 text-3xl text-ink sm:text-4xl">{step.title}</h3>
        <p className="mt-4 text-base leading-relaxed text-muted-foreground">{step.body}</p>
      </div>
      <motion.div
        animate={{ scale: isActive ? 1 : 0.97 }}
        transition={{ duration: 0.5, ease: EASE }}
        className="flex justify-center lg:justify-end"
      >
        {step.visual}
      </motion.div>
    </motion.div>
  );
}

/** Apple-style pinned scroll sequence: the section is several viewports
 * tall, but its content sticks to the screen while the steps cross-fade
 * through as you scroll.
 *
 * The active step is derived from scroll progress into a single piece of
 * state, and the panels tween between visible states. Driving each panel's
 * opacity directly off a per-step `useTransform` proved unreliable - the
 * transform updated but opacity stayed pinned at its initial value, leaving
 * two steps painted on top of each other.
 *
 * Collapses to a plain stacked list under `prefers-reduced-motion`, where
 * pinning would hold the viewport hostage. */
export function ScrollScene({
  steps,
  className,
  label,
}: {
  steps: ScrollStep[];
  className?: string;
  label?: string;
}) {
  const ref = useRef<HTMLDivElement>(null);
  const reduceMotion = useSafeReducedMotion();
  const { scrollYProgress } = useScroll({ target: ref, offset: ["start start", "end end"] });
  const [active, setActive] = useState(0);

  useMotionValueEvent(scrollYProgress, "change", (p) => {
    // Nudge the boundary slightly past the band edge so a step is fully
    // settled before the next one takes over.
    const next = Math.min(steps.length - 1, Math.max(0, Math.floor(p * steps.length - 0.001)));
    setActive((prev) => (prev === next ? prev : next));
  });

  if (reduceMotion) {
    return (
      <section aria-label={label} className={cn("mx-auto w-full max-w-6xl px-6", className)}>
        <div className="space-y-20">
          {steps.map((step) => (
            <div key={step.title} className="grid items-center gap-10 lg:grid-cols-2">
              <div className="max-w-md">
                <p className="text-xs font-semibold tracking-[0.14em] text-blue uppercase">{step.eyebrow}</p>
                <h3 className="font-display mt-3 text-3xl text-ink sm:text-4xl">{step.title}</h3>
                <p className="mt-4 text-base leading-relaxed text-muted-foreground">{step.body}</p>
              </div>
              <div className="flex justify-center lg:justify-end">{step.visual}</div>
            </div>
          ))}
        </div>
      </section>
    );
  }

  return (
    <section
      ref={ref}
      aria-label={label}
      className={cn("relative", className)}
      style={{ height: `${steps.length * 100}vh` }}
    >
      <div className="sticky top-0 flex h-screen items-center overflow-hidden">
        <div className="relative mx-auto h-[26rem] w-full max-w-6xl px-6">
          {steps.map((step, i) => (
            <StepPanel key={step.title} step={step} index={i} active={active} />
          ))}
        </div>

        <div className="absolute bottom-14 left-1/2 flex -translate-x-1/2 gap-2" aria-hidden="true">
          {steps.map((step, i) => (
            <motion.span
              key={step.title}
              animate={{ width: i === active ? 28 : 8, opacity: i === active ? 1 : 0.25 }}
              transition={{ duration: 0.4, ease: EASE }}
              className="h-2 rounded-full bg-blue"
            />
          ))}
        </div>
      </div>
    </section>
  );
}
