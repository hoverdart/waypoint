import Link from "next/link";
import { Show, UserButton } from "@clerk/nextjs";
import { LogoLockup } from "@/components/brand/Logo";
import { NavLinks } from "@/components/nav/NavLinks";
import { HeaderShell } from "@/components/nav/HeaderShell";
import { PillLink } from "@/components/kit/PillButton";
import { AnimatedLoginLink } from "@/components/auth/AnimatedLoginLink";

export function SiteHeader() {
  return (
    <HeaderShell>
      <Link href="/" className="shrink-0 transition-opacity hover:opacity-70">
        <LogoLockup />
      </Link>

      <Show when="signed-in">
        <NavLinks />
      </Show>

      <div className="flex shrink-0 items-center gap-2">
        <Show when="signed-in">
          <Link
            href="/settings"
            className="hidden rounded-full px-3 py-1.5 text-sm font-medium text-ink-soft transition-colors hover:bg-ink/5 hover:text-ink sm:block"
          >
            Settings
          </Link>
          <span className="flex items-center">
            <UserButton />
          </span>
        </Show>
        <Show when="signed-out">
          <AnimatedLoginLink
            className="rounded-full px-3 py-1.5 text-sm font-medium text-ink-soft transition-colors hover:bg-ink/5 hover:text-ink"
          >
            Log in
          </AnimatedLoginLink>
          <PillLink href="/signup" size="sm" arrow>
            Get started
          </PillLink>
        </Show>
      </div>
    </HeaderShell>
  );
}
