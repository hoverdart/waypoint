"use client";

import Link from "next/link";
import { usePathname } from "next/navigation";
import { motion } from "framer-motion";
import { cn } from "@/lib/utils";

const NAV_LINKS = [
  { href: "/dashboard", label: "Dashboard" },
  { href: "/daily-plan", label: "Today" },
  { href: "/subjects", label: "Courses" },
  { href: "/analytics", label: "Progress" },
];

export function NavLinks() {
  const pathname = usePathname();

  return (
    <nav className="hidden items-center gap-0.5 text-sm md:flex">
      {NAV_LINKS.map((link) => {
        const isActive = pathname === link.href || pathname?.startsWith(`${link.href}/`);
        return (
          <Link
            key={link.href}
            href={link.href}
            aria-current={isActive ? "page" : undefined}
            className={cn(
              "relative rounded-full px-3.5 py-1.5 font-medium transition-colors duration-200",
              isActive ? "text-ink" : "text-ink-soft hover:text-ink"
            )}
          >
            {/* A single shared pill that slides between items rather than
                fading in per-link, so switching routes reads as one object
                moving. */}
            {isActive && (
              <motion.span
                layoutId="nav-active-pill"
                transition={{ type: "spring", stiffness: 380, damping: 32 }}
                className="absolute inset-0 -z-10 rounded-full bg-ink/[0.07]"
              />
            )}
            {link.label}
          </Link>
        );
      })}
    </nav>
  );
}
