import { Surface } from "@/components/kit/Surface";
import { PillLink } from "@/components/kit/PillButton";
import { Reveal } from "@/components/motion/Reveal";
import { Highlight } from "@/components/kit/Typography";

export function FinalCta() {
  return (
    <section aria-label="Get started" className="px-6 pb-24 sm:pb-28">
      <Reveal>
        <Surface tone="raised" className="relative mx-auto w-full max-w-5xl overflow-hidden px-6 py-20 text-center">
          {/* The aura, echoed inside the card so the page's last beat feels
              like its first. */}
          <div className="aura pointer-events-none absolute inset-x-0 top-0 h-56 opacity-60" aria-hidden="true" />

          <div className="relative">
            <h2 className="font-display text-balance-display mx-auto max-w-2xl text-3xl text-ink sm:text-4xl md:text-5xl">
              Know what to study <Highlight>tomorrow morning</Highlight>.
            </h2>
            <p className="mx-auto mt-5 max-w-md text-base text-muted-foreground">
              WayPoint builds your first study path in under two minutes.
            </p>
            <div className="mt-9 flex justify-center">
              <PillLink href="/signup" size="lg" arrow>
                Get started free
              </PillLink>
            </div>
            <p className="mt-5 text-xs text-muted-foreground">Free while we&apos;re in beta · No credit card</p>
          </div>
        </Surface>
      </Reveal>
    </section>
  );
}
