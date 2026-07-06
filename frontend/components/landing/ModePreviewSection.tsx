"use client";

import { motion, useReducedMotion } from "framer-motion";
import { Compass, Sparkles } from "lucide-react";
import { MiniMasteryRing } from "@/components/onboarding/MiniMasteryRing";
import { MiniAnalyticsPreview } from "@/components/onboarding/MiniAnalyticsPreview";
import { MiniQuestPreview } from "@/components/onboarding/MiniQuestPreview";

export function ModePreviewSection() {
  const reduceMotion = useReducedMotion();

  return (
    <section className="mx-auto w-full max-w-5xl px-4 py-20">
      <motion.div
        initial={{ opacity: 0, y: reduceMotion ? 0 : 16 }}
        whileInView={{ opacity: 1, y: 0 }}
        viewport={{ once: true, margin: "-80px" }}
        transition={{ duration: reduceMotion ? 0 : 0.5 }}
        className="mb-10 text-center"
      >
        <h2 className="font-heading text-2xl font-semibold tracking-tight text-navy sm:text-3xl">
          One study engine, two ways to feel about it
        </h2>
        <p className="mx-auto mt-2 max-w-xl text-muted-foreground">
          Every student gets the same mastery tracking and priority scoring underneath - you just choose how it shows up.
        </p>
      </motion.div>

      <div className="grid gap-5 sm:grid-cols-2">
        <motion.div
          initial={{ opacity: 0, y: reduceMotion ? 0 : 20 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true, margin: "-80px" }}
          transition={{ duration: reduceMotion ? 0 : 0.5 }}
          className="rounded-3xl border border-border/80 bg-card p-6 shadow-sm"
        >
          <div className="mb-4 flex items-center gap-3">
            <span className="flex size-10 items-center justify-center rounded-xl bg-blue-soft text-navy">
              <Compass className="size-5" aria-hidden="true" />
            </span>
            <p className="font-semibold text-navy">Professional</p>
          </div>
          <p className="mb-4 text-sm text-muted-foreground">
            Clean dashboard, mastery analytics, exam-readiness tracking, and focused review.
          </p>
          <div className="space-y-3 rounded-2xl border border-border/70 bg-muted/50 p-4">
            <div className="flex items-center gap-3">
              <MiniMasteryRing value={72} />
              <div>
                <p className="text-xs font-medium text-navy">Exam Readiness</p>
                <p className="text-xs text-muted-foreground">Weak Topics: 3</p>
              </div>
            </div>
            <MiniAnalyticsPreview />
          </div>
        </motion.div>

        <motion.div
          initial={{ opacity: 0, y: reduceMotion ? 0 : 20 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true, margin: "-80px" }}
          transition={{ duration: reduceMotion ? 0 : 0.5, delay: reduceMotion ? 0 : 0.1 }}
          className="rounded-3xl border border-border/80 bg-card p-6 shadow-sm"
        >
          <div className="mb-4 flex items-center gap-3">
            <span className="flex size-10 items-center justify-center rounded-xl bg-blue-soft text-navy">
              <Sparkles className="size-5" aria-hidden="true" />
            </span>
            <p className="font-semibold text-navy">Gamified</p>
          </div>
          <p className="mb-4 text-sm text-muted-foreground">
            Same study engine, plus XP, streaks, badges, and daily quests.
          </p>
          <div className="rounded-2xl border border-border/70 bg-muted/50 p-4">
            <MiniQuestPreview />
          </div>
        </motion.div>
      </div>
    </section>
  );
}
