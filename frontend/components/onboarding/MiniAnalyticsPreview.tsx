"use client";

import { motion, useReducedMotion } from "framer-motion";

const BARS = [38, 52, 44, 68, 60, 82];

export function MiniAnalyticsPreview() {
  const reduceMotion = useReducedMotion();

  return (
    <div className="flex h-12 items-end gap-1" aria-hidden="true">
      {BARS.map((height, i) => (
        <motion.div
          key={i}
          className="w-2 rounded-full bg-gradient-to-t from-blue to-blue/50"
          initial={{ height: reduceMotion ? `${height}%` : "10%" }}
          animate={{ height: `${height}%` }}
          transition={reduceMotion ? { duration: 0 } : { duration: 0.5, delay: 0.1 * i, ease: "easeOut" }}
        />
      ))}
    </div>
  );
}
