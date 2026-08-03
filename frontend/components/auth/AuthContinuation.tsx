"use client";

import { useEffect } from "react";
import { useRouter } from "next/navigation";
import { Check } from "lucide-react";
import { motion } from "framer-motion";
import { useSafeReducedMotion } from "@/components/motion/useSafeReducedMotion";

export function AuthContinuation({ destination }: { destination: string }) {
  const router = useRouter();
  const reduceMotion = useSafeReducedMotion();

  useEffect(() => {
    if (reduceMotion) {
      router.replace(destination);
      return;
    }
    const timeout = window.setTimeout(() => router.replace(destination), 420);
    return () => window.clearTimeout(timeout);
  }, [destination, reduceMotion, router]);

  return (
    <div className="flex flex-1 items-center justify-center px-6 py-16" aria-live="polite">
      <motion.div
        initial={{ opacity: 0, y: reduceMotion ? 0 : 12, scale: reduceMotion ? 1 : 0.96 }}
        animate={{ opacity: 1, y: 0, scale: 1 }}
        transition={{ duration: reduceMotion ? 0 : 0.3, ease: [0.22, 1, 0.36, 1] }}
        className="flex w-full max-w-sm flex-col items-center rounded-surface border border-border/70 bg-card px-6 py-10 text-center shadow-lift"
      >
        <motion.span
          initial={{ scale: reduceMotion ? 1 : 0.5 }}
          animate={{ scale: 1 }}
          transition={{ duration: reduceMotion ? 0 : 0.35, delay: reduceMotion ? 0 : 0.08, type: "spring", stiffness: 260, damping: 16 }}
          className="flex size-12 items-center justify-center rounded-full bg-blue text-blue-foreground"
        >
          <Check className="size-6" strokeWidth={3} aria-hidden="true" />
        </motion.span>
        <h1 className="mt-5 font-display text-xl text-ink">You’re in</h1>
        <p className="mt-2 text-sm text-muted-foreground">Taking you to your WayPoint.</p>
      </motion.div>
    </div>
  );
}
