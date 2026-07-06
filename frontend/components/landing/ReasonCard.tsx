"use client";

import { ReactNode } from "react";
import { motion, useReducedMotion } from "framer-motion";

export function ReasonCard({
  icon,
  title,
  body,
  index = 0,
}: {
  icon: ReactNode;
  title: string;
  body: string;
  index?: number;
}) {
  const reduceMotion = useReducedMotion();

  return (
    <motion.div
      initial={{ opacity: 0, y: reduceMotion ? 0 : 20 }}
      whileInView={{ opacity: 1, y: 0 }}
      viewport={{ once: true, margin: "-80px" }}
      transition={{ duration: reduceMotion ? 0 : 0.5, delay: reduceMotion ? 0 : index * 0.1, ease: "easeOut" }}
      whileHover={reduceMotion ? undefined : { y: -4 }}
      className="rounded-3xl border border-border/80 bg-card p-6 shadow-sm transition-shadow hover:shadow-md"
    >
      <span className="mb-4 flex size-11 items-center justify-center rounded-xl bg-blue-soft text-navy">
        {icon}
      </span>
      <h3 className="font-heading mb-2 text-lg font-semibold text-navy">{title}</h3>
      <p className="text-sm leading-relaxed text-muted-foreground">{body}</p>
    </motion.div>
  );
}
