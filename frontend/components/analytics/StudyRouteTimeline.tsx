"use client";

import { motion, useReducedMotion } from "framer-motion";
import { SubjectMastery } from "@/lib/api";
import { TopicMasteryPill } from "@/components/shared/MasteryPills";
import { AnimatedCheckpoint } from "@/components/shared/AnimatedCheckpoint";

/** Replaces the bare UnitMasteryChart bar chart - units rendered as a route,
 * each with a checkpoint marker and its topics as mastery-tier pills, from
 * the same SubjectMastery.units[] data (no new fields needed). */
export function StudyRouteTimeline({ mastery }: { mastery: SubjectMastery }) {
  const reduceMotion = useReducedMotion();

  return (
    <ol className="space-y-5">
      {mastery.units.map((unit, i) => (
        <motion.li
          key={unit.unit_id}
          initial={{ opacity: 0, y: reduceMotion ? 0 : 10 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true, margin: "-40px" }}
          transition={{ duration: reduceMotion ? 0 : 0.4, delay: reduceMotion ? 0 : i * 0.05, ease: "easeOut" }}
          className="relative border-l-2 border-border/70 pl-5 last:border-transparent"
        >
          <span className="absolute -left-[11px] top-0">
            <AnimatedCheckpoint done={unit.mastery_score >= 0.7} />
          </span>
          <div className="flex flex-wrap items-center justify-between gap-2">
            <p className="font-heading text-sm font-semibold text-navy">{unit.unit_name}</p>
            <TopicMasteryPill masteryScore={unit.mastery_score} />
          </div>
          <ul className="mt-2 flex flex-wrap gap-1.5">
            {unit.topics.map((topic) => (
              <li key={topic.topic_id}>
                <TopicMasteryPill masteryScore={topic.mastery_score} label={topic.topic_name} className="opacity-90" />
              </li>
            ))}
          </ul>
        </motion.li>
      ))}
    </ol>
  );
}
