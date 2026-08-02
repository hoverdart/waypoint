"use client";

import { motion, useScroll, useSpring } from "framer-motion";
import { useSafeReducedMotion } from "@/components/motion/useSafeReducedMotion";

/** Hairline reading-progress bar pinned to the very top of the viewport.
 * Spring-smoothed so it eases rather than tracking the wheel 1:1. */
export function ScrollProgressBar() {
  const { scrollYProgress } = useScroll();
  const reduceMotion = useSafeReducedMotion();
  const scaleX = useSpring(scrollYProgress, { stiffness: 120, damping: 30, restDelta: 0.001 });

  if (reduceMotion) return null;

  return (
    <motion.div
      aria-hidden="true"
      style={{ scaleX }}
      className="fixed inset-x-0 top-0 z-50 h-0.5 origin-left bg-gradient-to-r from-blue via-accent-violet to-blue"
    />
  );
}
