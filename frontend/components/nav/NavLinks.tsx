"use client";

import Link from "next/link";
import { usePathname } from "next/navigation";
import { cn } from "@/lib/utils";

const NAV_LINKS = [
  { href: "/dashboard", label: "Dashboard" },
  { href: "/daily-plan", label: "Daily Plan" },
  { href: "/subjects", label: "Subjects" },
  { href: "/analytics", label: "Analytics" },
];

export function NavLinks() {
  const pathname = usePathname();

  return (
    <nav className="hidden items-center gap-1 text-sm sm:flex">
      {NAV_LINKS.map((link) => {
        const isActive = pathname === link.href || pathname?.startsWith(`${link.href}/`);
        return (
          <Link
            key={link.href}
            href={link.href}
            aria-current={isActive ? "page" : undefined}
            className={cn(
              "relative rounded-lg px-3 py-1.5 font-medium transition-colors",
              isActive
                ? "bg-white/10 text-navy-foreground"
                : "text-navy-foreground/65 hover:bg-white/10 hover:text-navy-foreground"
            )}
          >
            {link.label}
            {isActive && <span className="absolute inset-x-3 -bottom-1 h-0.5 rounded-full bg-blue" />}
          </Link>
        );
      })}
    </nav>
  );
}
