"use client";

import { ReactNode, useRef } from "react";
import { motion, useScroll, useTransform } from "framer-motion";
import { useSafeReducedMotion } from "@/components/motion/useSafeReducedMotion";
import { pillClass, PillLink } from "@/components/kit/PillButton";
import { Highlight } from "@/components/kit/Typography";
import { AnimatedLoginLink } from "@/components/auth/AnimatedLoginLink";

/** Landing hero. As you scroll away, the whole block eases out and drifts
 * up rather than simply sliding off - the page's first signal that motion
 * here is scroll-driven.
 *
 * The headline copy is asserted verbatim by e2e/unauthenticated.spec.ts;
 * keep the sentence intact if you restyle this. */
export function Hero({ visual }: { visual: ReactNode }) {
  const ref = useRef<HTMLDivElement>(null);
  const reduceMotion = useSafeReducedMotion();
  const { scrollYProgress } = useScroll({ target: ref, offset: ["start start", "end start"] });
  const opacity = useTransform(scrollYProgress, [0, 0.75], [1, 0]);
  const y = useTransform(scrollYProgress, [0, 1], [0, -70]);
  const scale = useTransform(scrollYProgress, [0, 1], [1, 0.96]);

  const style = reduceMotion ? undefined : { opacity, y, scale };

  /**
   * Entry transition. `initial`/`animate` stay unconditional on purpose:
   * dropping `animate` when motion is reduced leaves framer holding the
   * `initial` opacity of 0 with no target to move to, which stranded the whole
   * hero invisible. Zeroing the duration instead snaps it straight to the
   * visible state.
   */
  const enter = (duration: number, delay = 0) => ({
    duration: reduceMotion ? 0 : duration,
    delay: reduceMotion ? 0 : delay,
    ease: [0.22, 1, 0.36, 1] as const,
  });

  return (
    <section ref={ref} aria-label="Hero" className="relative isolate">
      <motion.div
        style={style}
        className="mx-auto grid w-full max-w-6xl items-center gap-14 px-6 pt-16 pb-24 sm:pt-24 lg:grid-cols-[1.05fr_0.95fr] lg:pt-28 lg:pb-32"
      >
        <div className="flex flex-col items-center text-center lg:items-start lg:text-left">
          <motion.span
            initial={{ opacity: 0, y: 12 }}
            animate={{ opacity: 1, y: 0 }}
            transition={enter(0.5)}
            className="inline-flex items-center gap-2 rounded-full border border-border/70 bg-card/70 px-3 py-1.5 text-xs font-medium text-ink-soft shadow-hairline backdrop-blur"
          >
            <span className="size-1.5 rounded-full bg-accent-green" aria-hidden="true" />
            Built for the 2026 AP exams
          </motion.span>

          <motion.h1
            initial={{ opacity: 0, y: 18 }}
            animate={{ opacity: 1, y: 0 }}
            transition={enter(0.65, 0.06)}
            className="font-display text-balance-display mt-6 text-4xl text-ink sm:text-5xl lg:text-6xl"
          >
            Every day, we tell you <Highlight animated>exactly what to study next</Highlight> to maximize your AP score.
          </motion.h1>

          <motion.p
            initial={{ opacity: 0, y: 18 }}
            animate={{ opacity: 1, y: 0 }}
            transition={enter(0.65, 0.14)}
            className="mt-6 max-w-xl text-lg leading-relaxed text-muted-foreground"
          >
            Not another question bank. WayPoint tracks what you actually know, then hands you one short,
            specific plan each morning — and shows you the reason behind every pick.
          </motion.p>

          <motion.div
            initial={{ opacity: 0, y: 18 }}
            animate={{ opacity: 1, y: 0 }}
            transition={enter(0.65, 0.22)}
            className="mt-9 flex flex-col items-center gap-3 sm:flex-row"
          >
            <PillLink href="/signup" size="lg" arrow>
              Get started free
            </PillLink>
            <AnimatedLoginLink className={pillClass("secondary", "lg")}>
              Log in
            </AnimatedLoginLink>
          </motion.div>

          <motion.p
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            transition={enter(0.5, 0.34)}
            className="mt-5 text-xs text-muted-foreground"
          >
            Free while we&apos;re in beta · No credit card
          </motion.p>
        </div>

        <motion.div
          initial={{ opacity: 0, y: 28, scale: 0.97 }}
          animate={{ opacity: 1, y: 0, scale: 1 }}
          transition={enter(0.8, 0.18)}
          className="flex justify-center lg:justify-end"
        >
          {visual}
        </motion.div>
      </motion.div>
    </section>
  );
}
