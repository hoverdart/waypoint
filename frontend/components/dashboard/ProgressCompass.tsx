"use client";

import { motion, useReducedMotion } from "framer-motion";
import { DashboardSubjectSummary } from "@/lib/api";

const RING_COLORS = ["var(--blue)", "var(--accent-violet)", "var(--accent-amber)", "var(--accent-green)", "var(--accent-coral)"];

/** Circular multi-subject readiness visual - one concentric ring per
 * enrolled subject, computed client-side from mastery_score already on
 * Dashboard.subjects (no backend gap). */
export function ProgressCompass({ subjects, size = 128 }: { subjects: DashboardSubjectSummary[]; size?: number }) {
  const reduceMotion = useReducedMotion();
  const stroke = 9;
  const gap = 4;

  const overall = subjects.length
    ? Math.round((subjects.reduce((sum, s) => sum + s.mastery_score, 0) / subjects.length) * 100)
    : 0;

  return (
    <div className="flex items-center gap-5">
      <div className="relative shrink-0" style={{ width: size, height: size }}>
        <svg width={size} height={size} viewBox={`0 0 ${size} ${size}`} className="-rotate-90">
          {subjects.map((subject, i) => {
            const radius = (size - stroke) / 2 - i * (stroke + gap);
            if (radius <= 0) return null;
            const circumference = 2 * Math.PI * radius;
            const value = Math.round(subject.mastery_score * 100);
            const offset = circumference * (1 - value / 100);
            return (
              <g key={subject.subject_id}>
                <circle cx={size / 2} cy={size / 2} r={radius} fill="none" stroke="var(--border)" strokeWidth={stroke} />
                <motion.circle
                  cx={size / 2}
                  cy={size / 2}
                  r={radius}
                  fill="none"
                  stroke={RING_COLORS[i % RING_COLORS.length]}
                  strokeWidth={stroke}
                  strokeLinecap="round"
                  strokeDasharray={circumference}
                  initial={{ strokeDashoffset: circumference }}
                  animate={{ strokeDashoffset: offset }}
                  transition={reduceMotion ? { duration: 0 } : { duration: 1, ease: "easeOut", delay: 0.15 * i }}
                />
              </g>
            );
          })}
        </svg>
        <div className="absolute inset-0 flex flex-col items-center justify-center">
          <span className="font-heading text-2xl font-semibold text-navy">{overall}%</span>
          <span className="text-[0.65rem] text-muted-foreground">exam-ready</span>
        </div>
      </div>
      <ul className="space-y-1.5">
        {subjects.map((subject, i) => (
          <li key={subject.subject_id} className="flex items-center gap-2 text-xs">
            <span
              className="size-2 shrink-0 rounded-full"
              style={{ backgroundColor: RING_COLORS[i % RING_COLORS.length] }}
              aria-hidden="true"
            />
            <span className="font-medium text-navy">{subject.subject_name}</span>
            <span className="text-muted-foreground">{Math.round(subject.mastery_score * 100)}%</span>
          </li>
        ))}
      </ul>
    </div>
  );
}
