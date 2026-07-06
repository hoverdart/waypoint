"use client";

import { motion, useReducedMotion } from "framer-motion";
import { Sigma, Dna, Brain, Landmark, FlaskConical, Code2 } from "lucide-react";

const SUBJECTS = [
  { name: "AP Calculus AB", icon: Sigma },
  { name: "AP Biology", icon: Dna },
  { name: "AP Psychology", icon: Brain },
  { name: "AP US History", icon: Landmark },
  { name: "AP Chemistry", icon: FlaskConical },
  { name: "AP Computer Science A", icon: Code2 },
];

export function SubjectShowcase() {
  const reduceMotion = useReducedMotion();

  return (
    <section aria-label="Priority AP subjects" className="mx-auto w-full max-w-5xl px-4 pb-20">
      <motion.p
        initial={{ opacity: 0 }}
        whileInView={{ opacity: 1 }}
        viewport={{ once: true }}
        className="mb-6 text-center text-sm font-medium text-muted-foreground"
      >
        Launching with
      </motion.p>
      <div className="grid grid-cols-2 gap-3 sm:grid-cols-3 lg:grid-cols-6">
        {SUBJECTS.map(({ name, icon: Icon }, i) => (
          <motion.div
            key={name}
            initial={{ opacity: 0, y: reduceMotion ? 0 : 14 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true, margin: "-40px" }}
            transition={{ duration: reduceMotion ? 0 : 0.4, delay: reduceMotion ? 0 : i * 0.06 }}
            whileHover={reduceMotion ? undefined : { y: -3 }}
            className="flex flex-col items-center gap-2 rounded-2xl border border-border/70 bg-card px-3 py-4 text-center shadow-sm"
          >
            <span className="flex size-9 items-center justify-center rounded-lg bg-blue-soft text-navy">
              <Icon className="size-4" aria-hidden="true" />
            </span>
            <span className="text-xs font-medium text-navy">{name}</span>
          </motion.div>
        ))}
      </div>
    </section>
  );
}
