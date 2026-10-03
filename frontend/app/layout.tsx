import type { Metadata } from "next";
import { ClerkProvider } from "@clerk/nextjs";
import { shadcn } from "@clerk/ui/themes";
import { TooltipProvider } from "@/components/ui/tooltip";
import { Toaster } from "@/components/ui/sonner";
import { SiteHeader } from "@/components/nav/SiteHeader";
import { ScrollProgressBar } from "@/components/motion/ScrollProgressBar";
import "./globals.css";

export const metadata: Metadata = {
  title: "WayPoint",
  description: "Every day, we tell you exactly what to study next to maximize your AP score.",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <ClerkProvider appearance={{ theme: shadcn }}>
      <html
        lang="en"
        className="h-full antialiased"
      >
        <body className="relative min-h-full flex flex-col">
          <a href="#main-content" className="sr-only focus:not-sr-only focus:fixed focus:top-2 focus:left-2 focus:z-50 focus:bg-card focus:p-3">Skip to content</a>
          <TooltipProvider>
            <ScrollProgressBar />
            <SiteHeader />
            <main id="main-content" className="flex flex-1 flex-col pb-20 md:pb-0">{children}</main>
          </TooltipProvider>
          <Toaster />
        </body>
      </html>
    </ClerkProvider>
  );
}
