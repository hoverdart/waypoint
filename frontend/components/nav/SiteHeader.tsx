import Link from "next/link";
import { Show, UserButton } from "@clerk/nextjs";
import { LinkButton } from "@/components/shared/LinkButton";
import { LogoLockup } from "@/components/brand/Logo";
import { NavLinks } from "@/components/nav/NavLinks";

export async function SiteHeader() {
  return (
    <header className="sticky top-0 z-40 border-b border-border/70 bg-background/85 backdrop-blur-md">
      <div className="mx-auto flex h-16 max-w-6xl items-center justify-between px-4">
        <Link href="/" className="transition-opacity hover:opacity-80">
          <LogoLockup />
        </Link>

        <Show when="signed-in">
          <NavLinks />
        </Show>

        <div className="flex items-center gap-3">
          <Show when="signed-in">
            <Link
              href="/settings"
              className="rounded-lg px-3 py-1.5 text-sm font-medium text-muted-foreground transition-colors hover:bg-blue-soft/60 hover:text-navy"
            >
              Settings
            </Link>
            <span className="rounded-full ring-2 ring-blue-soft">
              <UserButton />
            </span>
          </Show>
          <Show when="signed-out">
            <LinkButton variant="ghost" href="/login">
              Log in
            </LinkButton>
            <LinkButton href="/signup" className="bg-navy text-navy-foreground hover:bg-navy-soft">
              Sign up
            </LinkButton>
          </Show>
        </div>
      </div>
    </header>
  );
}
