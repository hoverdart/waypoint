import type { Metadata } from "next";
import { Geist, Geist_Mono, Plus_Jakarta_Sans } from "next/font/google";
import { ClerkProvider } from "@clerk/nextjs";
import { shadcn } from "@clerk/ui/themes";
import { TooltipProvider } from "@/components/ui/tooltip";
import { Toaster } from "@/components/ui/sonner";
import { SiteHeader } from "@/components/nav/SiteHeader";
import { AuraBackdrop } from "@/components/motion/AuraBackdrop";
import { ScrollProgressBar } from "@/components/motion/ScrollProgressBar";
import "./globals.css";

const geistSans = Geist({
  variable: "--font-geist-sans",
  subsets: ["latin"],
});

const geistMono = Geist_Mono({
  variable: "--font-geist-mono",
  subsets: ["latin"],
});

// Display face for headlines - a geometric humanist sans that holds up at
// very large sizes and heavy weights, which is what this design language
// leans on instead of decorative type.
const jakarta = Plus_Jakarta_Sans({
  variable: "--font-jakarta",
  subsets: ["latin"],
  weight: ["500", "600", "700", "800"],
});

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
        className={`${geistSans.variable} ${geistMono.variable} ${jakarta.variable} h-full antialiased`}
      >
        <body className="relative min-h-full flex flex-col">
          <AuraBackdrop />
          <TooltipProvider>
            <ScrollProgressBar />
            <SiteHeader />
            <main className="flex flex-1 flex-col">{children}</main>
          </TooltipProvider>
          <Toaster />
        </body>
      </html>
    </ClerkProvider>
  );
}
