"use client";

import { ElementType, ReactNode } from "react";
import { motion } from "framer-motion";
import { useSafeReducedMotion } from "@/components/motion/useSafeReducedMotion";

type RevealDirection = "up" | "down" | "left" | "right" | "none";

const OFFSET: Record<RevealDirection, { x?: number; y?: number }> = {
  up: { y: 24 },
  down: { y: -24 },
  left: { x: 24 },
  right: { x: -24 },
  none: {},
};

/** The workhorse scroll animation: content fades and glides into place the
 * first time it enters the viewport, then stays put. `index` staggers
 * siblings without every call site hand-computing a delay.
 *
 * Under `prefers-reduced-motion` this renders a plain element with no
 * transform and no opacity animation at all - never a delayed fade, which
 * would leave content invisible for users who opted out of motion. */
export function Reveal({
  children,
  as = "div",
  direction = "up",
  index = 0,
  delay = 0,
  duration = 0.55,
  distance,
  once = true,
  className,
  ...rest
}: {
  children: ReactNode;
  as?: ElementType;
  direction?: RevealDirection;
  index?: number;
  delay?: number;
  duration?: number;
  distance?: number;
  once?: boolean;
  className?: string;
} & Record<string, unknown>) {
  const reduceMotion = useSafeReducedMotion();
  const MotionTag = motion[as as keyof typeof motion] as typeof motion.div;

  if (reduceMotion) {
    const Tag = as as ElementType;
    return (
      <Tag className={className} {...rest}>
        {children}
      </Tag>
    );
  }

  const base = OFFSET[direction];
  const offset = distance
    ? Object.fromEntries(Object.entries(base).map(([k, v]) => [k, Math.sign(v ?? 0) * distance]))
    : base;

  return (
    <MotionTag
      initial={{ opacity: 0, ...offset }}
      whileInView={{ opacity: 1, x: 0, y: 0 }}
      viewport={{ once, margin: "-12% 0px -8% 0px" }}
      transition={{ duration, delay: delay + index * 0.07, ease: [0.22, 1, 0.36, 1] }}
      className={className}
      {...rest}
    >
      {children}
    </MotionTag>
  );
}
