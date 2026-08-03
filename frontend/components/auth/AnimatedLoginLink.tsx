"use client";

import { AnchorHTMLAttributes, ReactNode, useState } from "react";
import { useRouter } from "next/navigation";
import { motion } from "framer-motion";
import { useSafeReducedMotion } from "@/components/motion/useSafeReducedMotion";

/**
 * A deliberately small cross-route motion cue. It keeps a real href for
 * progressive enhancement and modified clicks, then gives normal clicks just
 * enough time to acknowledge intent before App Router navigation starts.
 */
export function AnimatedLoginLink({ href = "/login", children, onClick, ...props }: Omit<AnchorHTMLAttributes<HTMLAnchorElement>, "href"> & { href?: string; children: ReactNode }) {
  const router = useRouter();
  const reduceMotion = useSafeReducedMotion();
  const [leaving, setLeaving] = useState(false);

  function handleClick(event: React.MouseEvent<HTMLAnchorElement>) {
    onClick?.(event);
    if (event.defaultPrevented || event.button !== 0 || event.metaKey || event.ctrlKey || event.shiftKey || event.altKey) return;
    event.preventDefault();
    if (leaving) return;
    if (reduceMotion) {
      router.push(href);
      return;
    }
    setLeaving(true);
    window.setTimeout(() => router.push(href), 160);
  }

  return (
    <motion.span
      animate={leaving ? { opacity: 0.65, scale: 0.96, y: -2 } : { opacity: 1, scale: 1, y: 0 }}
      transition={{ duration: reduceMotion ? 0 : 0.16, ease: "easeOut" }}
    >
      <a href={href} onClick={handleClick} {...props}>{children}</a>
    </motion.span>
  );
}
