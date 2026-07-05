import Link from "next/link";
import { Show, UserButton } from "@clerk/nextjs";
import { LinkButton } from "@/components/shared/LinkButton";

const NAV_LINKS = [
  { href: "/dashboard", label: "Dashboard" },
  { href: "/daily-plan", label: "Daily Plan" },
  { href: "/subjects", label: "Subjects" },
  { href: "/analytics", label: "Analytics" },
];

export async function SiteHeader() {
  return (
    <header className="border-b bg-background">
      <div className="mx-auto flex h-14 max-w-6xl items-center justify-between px-4">
        <Link href="/" className="font-semibold tracking-tight">
          WayPoint
        </Link>

        <Show when="signed-in">
          <nav className="hidden items-center gap-6 text-sm text-muted-foreground sm:flex">
            {NAV_LINKS.map((link) => (
              <Link key={link.href} href={link.href} className="hover:text-foreground">
                {link.label}
              </Link>
            ))}
          </nav>
        </Show>

        <div className="flex items-center gap-3">
          <Show when="signed-in">
            <Link href="/settings" className="text-sm text-muted-foreground hover:text-foreground">
              Settings
            </Link>
            <UserButton />
          </Show>
          <Show when="signed-out">
            <LinkButton variant="ghost" href="/login">
              Log in
            </LinkButton>
            <LinkButton href="/signup">Sign up</LinkButton>
          </Show>
        </div>
      </div>
    </header>
  );
}
