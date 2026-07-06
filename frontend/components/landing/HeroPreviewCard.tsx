"use client";

import { motion, useReducedMotion } from "framer-motion";
import { ClipboardCheck } from "lucide-react";
import { MiniMasteryRing } from "@/components/onboarding/MiniMasteryRing";
import { MiniAnalyticsPreview } from "@/components/onboarding/MiniAnalyticsPreview";

/** A glimpse of the real dashboard, floating beside the hero copy - shows
 * rather than tells what "personalized study path" actually means. */
export function HeroPreviewCard() {
  const reduceMotion = useReducedMotion();

  return (
    <motion.div
      initial={{ opacity: 0, y: reduceMotion ? 0 : 24, rotate: reduceMotion ? 0 : -2 }}
      animate={{ opacity: 1, y: 0, rotate: -2 }}
      transition={{ duration: reduceMotion ? 0 : 0.7, delay: 0.3, ease: "easeOut" }}
      whileHover={reduceMotion ? undefined : { rotate: 0, y: -4 }}
      className="w-full max-w-sm rounded-3xl border border-border/80 bg-card p-5 shadow-[0_30px_80px_-30px_var(--navy)]"
    >
      <div className="mb-4 flex items-center justify-between">
        <div>
          <p className="text-xs text-muted-foreground">AP Biology</p>
          <p className="font-semibold text-navy">Exam Readiness</p>
        </div>
        <MiniMasteryRing value={72} size={48} />
      </div>

      <div className="mb-4 space-y-2 rounded-2xl bg-muted/60 p-3">
        <div className="flex items-center gap-2 text-xs">
          <ClipboardCheck className="size-3.5 text-blue" aria-hidden="true" />
          <span className="font-medium text-navy">Next: Unit 4 FRQ review</span>
        </div>
        <p className="text-xs text-muted-foreground">Your mastery dropped on Cellular Respiration - 12 min</p>
      </div>

      <div className="flex items-center justify-between">
        <p className="text-xs text-muted-foreground">Mastery trend</p>
        <MiniAnalyticsPreview />
      </div>
    </motion.div>
  );
}
