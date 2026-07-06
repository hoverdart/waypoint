"use client";

import { motion, useReducedMotion } from "framer-motion";
import { Flame, Award } from "lucide-react";

export function MiniQuestPreview() {
  const reduceMotion = useReducedMotion();

  return (
    <div className="space-y-2.5">
      <div className="flex items-center gap-1.5">
        <span className="rounded-full bg-accent-amber/15 px-2 py-0.5 text-xs font-semibold text-accent-amber">
          +120 XP
        </span>
        <span className="inline-flex items-center gap-1 rounded-full bg-accent-coral/15 px-2 py-0.5 text-xs font-semibold text-accent-coral">
          <Flame className="size-3" aria-hidden="true" />
          3-day streak
        </span>
        <Award className="ml-auto size-5 text-accent-violet" aria-hidden="true" />
      </div>
      <div>
        <div className="mb-1 flex items-center justify-between text-[0.7rem] text-muted-foreground">
          <span>Daily Quest</span>
          <span>3/5</span>
        </div>
        <div className="h-1.5 w-full overflow-hidden rounded-full bg-secondary">
          <motion.div
            className="h-full rounded-full bg-gradient-to-r from-blue to-accent-violet"
            initial={{ width: reduceMotion ? "60%" : "0%" }}
            animate={{ width: "60%" }}
            transition={reduceMotion ? { duration: 0 } : { duration: 0.7, delay: 0.3, ease: "easeOut" }}
          />
        </div>
      </div>
    </div>
  );
}
