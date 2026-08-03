"use client";

import { SignIn } from "@clerk/nextjs";
import { motion } from "framer-motion";
import { useSafeReducedMotion } from "@/components/motion/useSafeReducedMotion";

export function LoginScreen({ returnTo }: { returnTo: string }) {
  const reduceMotion = useSafeReducedMotion();
  const continuationUrl = `/auth/continue?returnTo=${encodeURIComponent(returnTo)}`;

  return (
    <motion.div
      initial={{ opacity: 0, y: reduceMotion ? 0 : 16, scale: reduceMotion ? 1 : 0.98 }}
      animate={{ opacity: 1, y: 0, scale: 1 }}
      transition={{ duration: reduceMotion ? 0 : 0.38, ease: [0.22, 1, 0.36, 1] }}
      className="flex flex-1 items-center justify-center py-16"
    >
      <SignIn path="/login" routing="path" signUpUrl="/signup" forceRedirectUrl={continuationUrl} />
    </motion.div>
  );
}
