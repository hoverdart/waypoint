"use client";

import { motion, useReducedMotion } from "framer-motion";

export function MiniMasteryRing({ value = 72, size = 56 }: { value?: number; size?: number }) {
  const reduceMotion = useReducedMotion();
  const stroke = 5;
  const radius = (size - stroke) / 2;
  const circumference = 2 * Math.PI * radius;
  const offset = circumference * (1 - value / 100);

  return (
    <div className="relative shrink-0" style={{ width: size, height: size }}>
      <svg width={size} height={size} viewBox={`0 0 ${size} ${size}`} className="-rotate-90">
        <circle cx={size / 2} cy={size / 2} r={radius} fill="none" stroke="var(--border)" strokeWidth={stroke} />
        <motion.circle
          cx={size / 2}
          cy={size / 2}
          r={radius}
          fill="none"
          stroke="var(--blue)"
          strokeWidth={stroke}
          strokeLinecap="round"
          strokeDasharray={circumference}
          initial={{ strokeDashoffset: circumference }}
          animate={{ strokeDashoffset: offset }}
          transition={reduceMotion ? { duration: 0 } : { duration: 1, ease: "easeOut", delay: 0.3 }}
        />
      </svg>
      <div className="absolute inset-0 flex items-center justify-center text-xs font-semibold text-ink tabular-nums">
        {value}%
      </div>
    </div>
  );
}
