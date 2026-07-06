"use client";

import { motion, useReducedMotion } from "framer-motion";

const WAYPOINTS = [
  { cx: 150, cy: 440, delay: 0 },
  { cx: 420, cy: 330, delay: 0.4 },
  { cx: 700, cy: 250, delay: 0.8 },
  { cx: 950, cy: 170, delay: 1.2 },
  { cx: 1150, cy: 110, delay: 1.6 },
];

/** Purely decorative: a winding study-path line with drifting waypoint dots
 * and faint compass-ring geometry, echoing the logo's road/compass mark
 * without reading as a literal map or GPS app. */
export function AnimatedPathBackground() {
  const reduceMotion = useReducedMotion();

  return (
    <div className="pointer-events-none absolute inset-0 -z-10 overflow-hidden" aria-hidden="true">
      <div className="absolute -top-32 -left-32 size-96 rounded-full bg-blue/15 blur-3xl" />
      <div className="absolute -right-32 -bottom-32 size-96 rounded-full bg-navy/10 blur-3xl" />

      <svg
        viewBox="0 0 1200 600"
        preserveAspectRatio="xMidYMid slice"
        className="absolute inset-0 h-full w-full opacity-[0.35]"
      >
        <circle
          cx="1000"
          cy="120"
          r="140"
          fill="none"
          stroke="var(--navy)"
          strokeWidth="1"
          strokeDasharray="2 8"
          opacity="0.4"
        />
        <circle
          cx="150"
          cy="470"
          r="90"
          fill="none"
          stroke="var(--blue)"
          strokeWidth="1"
          strokeDasharray="2 8"
          opacity="0.4"
        />

        <motion.path
          d="M -20 480 C 200 420, 300 300, 500 320 C 700 340, 750 200, 1000 160 C 1100 140, 1150 120, 1220 100"
          fill="none"
          stroke="var(--blue)"
          strokeWidth="2"
          strokeLinecap="round"
          initial={reduceMotion ? { pathLength: 1, opacity: 0.5 } : { pathLength: 0, opacity: 0 }}
          animate={{ pathLength: 1, opacity: 0.5 }}
          transition={reduceMotion ? { duration: 0 } : { duration: 1.8, ease: "easeInOut" }}
        />

        {WAYPOINTS.map((point, i) => (
          <motion.circle
            key={i}
            cx={point.cx}
            cy={point.cy}
            r={5}
            fill="var(--blue)"
            initial={{ opacity: 0, scale: 0 }}
            animate={
              reduceMotion
                ? { opacity: 0.6, scale: 1 }
                : { opacity: [0.4, 0.9, 0.4], scale: 1, y: [0, -6, 0] }
            }
            transition={
              reduceMotion
                ? { duration: 0 }
                : {
                    scale: { duration: 0.4, delay: 0.6 + point.delay },
                    opacity: { duration: 3, repeat: Infinity, delay: 1 + point.delay, ease: "easeInOut" },
                    y: { duration: 3, repeat: Infinity, delay: 1 + point.delay, ease: "easeInOut" },
                  }
            }
          />
        ))}
      </svg>
    </div>
  );
}
