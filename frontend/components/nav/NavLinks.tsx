"use client";

import Link from "next/link";
import { usePathname } from "next/navigation";
import { cn } from "@/lib/utils";

const NAV_LINKS = [
  { href: "/dashboard", label: "Dashboard" },
  { href: "/daily-plan", label: "Today" },
  { href: "/subjects", label: "Courses" },
  { href: "/analytics", label: "Progress" },
  { href: "/practice", label: "Practice" },
];

export function NavLinks({ mobile = false }: { mobile?: boolean }) {
  const pathname = usePathname();
  return (
    <nav aria-label={mobile ? "Mobile navigation" : "Main navigation"} className={cn(mobile ? "fixed inset-x-0 bottom-0 z-50 flex justify-around border-t border-border bg-background px-2 pt-2 pb-[max(0.5rem,env(safe-area-inset-bottom))] md:hidden" : "hidden items-center gap-1 text-sm md:flex")}>
      {NAV_LINKS.map(link => {
        const active = pathname === link.href || pathname?.startsWith(`${link.href}/`);
        return <Link key={link.href} href={link.href} aria-current={active ? "page" : undefined} className={cn("rounded-md px-2 py-2 text-xs sm:text-sm font-medium transition-colors focus-visible:ring-2 focus-visible:ring-ring", active ? "bg-blue-soft text-blue" : "text-ink-soft hover:bg-muted hover:text-ink")}>{link.label}</Link>;
      })}
      {mobile && <Link href="/settings" className="rounded-md px-2 py-2 text-sm text-ink-soft">Settings</Link>}
    </nav>
  );
}
