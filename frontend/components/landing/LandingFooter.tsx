import Link from "next/link";
import { LogoLockup } from "@/components/brand/Logo";

export function LandingFooter() {
  return (
    <footer className="border-t border-border/70 px-4 py-8">
      <div className="mx-auto flex w-full max-w-5xl flex-col items-center justify-between gap-4 text-sm text-muted-foreground sm:flex-row">
        <LogoLockup size={24} />
        <p>&copy; 2026 WayPoint. Built for students chasing a 5.</p>
        <div className="flex gap-4">
          <Link href="/login" className="hover:text-navy">
            Log in
          </Link>
          <Link href="/signup" className="hover:text-navy">
            Sign up
          </Link>
        </div>
      </div>
    </footer>
  );
}
