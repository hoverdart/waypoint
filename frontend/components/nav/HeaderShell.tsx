import { ReactNode } from "react";

export function HeaderShell({ children }: { children: ReactNode }) {
  return <header className="sticky top-0 z-40 border-b border-border bg-background/95 backdrop-blur-md"><div className="mx-auto flex h-20 max-w-6xl items-center justify-between gap-4 px-6">{children}</div></header>;
}
