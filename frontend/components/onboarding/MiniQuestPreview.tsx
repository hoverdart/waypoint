"use client";

import { motion, useReducedMotion } from "framer-motion";
import { Flame, Award } from "lucide-react";
import { Chip } from "@/components/kit/Pills";

export function MiniQuestPreview() {
  const reduceMotion = useReducedMotion();

  return (
    <div className="space-y-3">
      <div className="flex items-center gap-1.5">
        <Chip tone="amber" className="font-semibold">
          +120 XP
        </Chip>
        <Chip tone="coral" className="font-semibold">
          <Flame className="size-3" aria-hidden="true" />
          3-day streak
        </Chip>
        <Award className="ml-auto size-5 text-accent-violet" aria-hidden="true" />
      </div>
      <div>
        <div className="mb-1.5 flex items-center justify-between text-[0.7rem] text-muted-foreground">
          <span>Daily Quest</span>
          <span className="tabular-nums">3/5</span>
        </div>
        <div className="h-1.5 w-full overflow-hidden rounded-full bg-muted">
          <motion.div
            className="h-full rounded-full bg-blue"
            initial={{ width: reduceMotion ? "60%" : "0%" }}
            animate={{ width: "60%" }}
            transition={reduceMotion ? { duration: 0 } : { duration: 0.7, delay: 0.3, ease: "easeOut" }}
          />
        </div>
      </div>
    </div>
  );
}
