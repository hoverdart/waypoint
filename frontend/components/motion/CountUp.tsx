"use client";

import { useEffect, useRef, useState } from "react";
import { animate, useInView } from "framer-motion";
import { useSafeReducedMotion } from "@/components/motion/useSafeReducedMotion";

/** Counts from zero to `value` the first time it scrolls into view, or snaps
 * straight to it when motion is reduced.
 *
 * The displayed number always starts at 0 - seeding state from the
 * reduced-motion preference instead would render a different number on the
 * server than on the client and break hydration. */
export function CountUp({
  value,
  duration = 1.1,
  suffix = "",
  className,
}: {
  value: number;
  duration?: number;
  suffix?: string;
  className?: string;
}) {
  const ref = useRef<HTMLSpanElement>(null);
  const inView = useInView(ref, { once: true, margin: "-10% 0px" });
  const reduceMotion = useSafeReducedMotion();
  const [display, setDisplay] = useState(0);

  useEffect(() => {
    if (!inView || reduceMotion) return;

    const controls = animate(0, value, {
      duration,
      ease: [0.22, 1, 0.36, 1],
      onUpdate: (v) => setDisplay(Math.round(v)),
    });
    return () => controls.stop();
  }, [inView, reduceMotion, value, duration]);

  // Derived rather than pushed into state from the effect. During SSR and
  // hydration `reduceMotion` is false, so both render 0 and hydration matches;
  // afterwards a reduced-motion reader simply gets the final number.
  const shown = reduceMotion ? value : display;

  return (
    <span ref={ref} className={className}>
      {shown}
      {suffix}
    </span>
  );
}
