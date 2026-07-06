"use client";

import { motion, useReducedMotion } from "framer-motion";
import { ArrowRight } from "lucide-react";
import { LogoMark } from "@/components/brand/Logo";
import { LinkButton } from "@/components/shared/LinkButton";

export function FinalCta() {
  const reduceMotion = useReducedMotion();

  return (
    <section className="px-4 pb-20">
      <motion.div
        initial={{ opacity: 0, y: reduceMotion ? 0 : 20 }}
        whileInView={{ opacity: 1, y: 0 }}
        viewport={{ once: true, margin: "-80px" }}
        transition={{ duration: reduceMotion ? 0 : 0.5 }}
        className="relative mx-auto flex w-full max-w-5xl flex-col items-center gap-5 overflow-hidden rounded-[2.5rem] bg-gradient-to-br from-navy to-navy-soft px-6 py-16 text-center"
      >
        <div className="pointer-events-none absolute -top-24 -right-24 size-72 rounded-full bg-blue/25 blur-3xl" aria-hidden="true" />
        <LogoMark size={40} className="ring-white/20" />
        <h2 className="font-heading max-w-xl text-2xl font-semibold tracking-tight text-navy-foreground sm:text-3xl">
          Stop guessing what to study. Start following your path.
        </h2>
        <p className="max-w-md text-navy-foreground/70">
          Free to start - WayPoint builds your first study path in under two minutes.
        </p>
        <div className="flex flex-col gap-3 sm:flex-row">
          <LinkButton
            href="/signup"
            size="lg"
            className="group/cta rounded-full bg-blue px-5 text-blue-foreground shadow-lg shadow-blue/20 hover:bg-blue/90"
          >
            Get started free
            <ArrowRight className="size-4 transition-transform duration-200 group-hover/cta:translate-x-0.5" aria-hidden="true" />
          </LinkButton>
        </div>
      </motion.div>
    </section>
  );
}
