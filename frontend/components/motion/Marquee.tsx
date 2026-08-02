"use client";

import { ReactNode } from "react";
import { motion } from "framer-motion";
import { useSafeReducedMotion } from "@/components/motion/useSafeReducedMotion";
import { cn } from "@/lib/utils";

/** Continuously drifting horizontal row. Children are rendered twice back
 * to back and the track is translated by exactly -50%, so the loop is
 * seamless. Falls back to a normal swipeable overflow row when motion is
 * reduced. */
export function Marquee({
  children,
  duration = 42,
  reverse = false,
  className,
}: {
  children: ReactNode;
  duration?: number;
  reverse?: boolean;
  className?: string;
}) {
  const reduceMotion = useSafeReducedMotion();

  if (reduceMotion) {
    return (
      <div className={cn("flex gap-4 overflow-x-auto pb-2", className)}>
        {children}
      </div>
    );
  }

  return (
    <div
      className={cn("group/marquee relative overflow-hidden", className)}
      style={{
        maskImage: "linear-gradient(to right, transparent, black 6%, black 94%, transparent)",
        WebkitMaskImage: "linear-gradient(to right, transparent, black 6%, black 94%, transparent)",
      }}
    >
      <motion.div
        className="flex w-max gap-4"
        animate={{ x: reverse ? ["-50%", "0%"] : ["0%", "-50%"] }}
        transition={{ duration, ease: "linear", repeat: Infinity }}
      >
        <div className="flex shrink-0 gap-4">{children}</div>
        <div className="flex shrink-0 gap-4" aria-hidden="true">
          {children}
        </div>
      </motion.div>
    </div>
  );
}
