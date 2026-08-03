import Link from "next/link";
import { LogoLockup } from "@/components/brand/Logo";
import { AnimatedLoginLink } from "@/components/auth/AnimatedLoginLink";

const LINKS = [
  { href: "/login", label: "Log in" },
  { href: "/signup", label: "Sign up" },
  { href: "/subjects", label: "Courses" },
];

export function LandingFooter() {
  return (
    <footer className="px-6 pb-14">
      <div className="mx-auto flex w-full max-w-5xl flex-col items-center gap-5 text-center">
        <LogoLockup size={26} />
        <p className="text-sm text-muted-foreground">Study less. Know more.</p>

        <div className="h-px w-full max-w-xs bg-border" />

        <nav className="flex flex-wrap justify-center gap-5 text-sm text-muted-foreground">
          {LINKS.map((link) => link.href === "/login" ? (
            <AnimatedLoginLink key={link.href} className="transition-colors hover:text-ink">{link.label}</AnimatedLoginLink>
          ) : (
            <Link key={link.href} href={link.href} className="transition-colors hover:text-ink">{link.label}</Link>
          ))}
        </nav>

        <p className="text-xs text-muted-foreground">&copy; 2026 WayPoint. Built for students chasing a 5.</p>
      </div>
    </footer>
  );
}
