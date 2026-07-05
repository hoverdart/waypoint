import Link from "next/link";
import { ComponentProps } from "react";
import { Button } from "@/components/ui/button";

/**
 * Button styled as a link to another route. This shadcn build uses Base UI
 * (not Radix), whose Button expects `nativeButton={false}` whenever the
 * `render` target isn't an actual `<button>` - easy to forget, so it's
 * baked in here once instead of repeated at every call site.
 */
type LinkButtonProps = Omit<ComponentProps<typeof Button>, "render" | "nativeButton"> & {
  href: string;
};

export function LinkButton({ href, children, ...buttonProps }: LinkButtonProps) {
  return <Button nativeButton={false} render={<Link href={href}>{children}</Link>} {...buttonProps} />;
}
