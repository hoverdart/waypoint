import { Sigma, Dna, Brain, Landmark, FlaskConical, Code2 } from "lucide-react";
import { Surface } from "@/components/kit/Surface";
import { Reveal } from "@/components/motion/Reveal";

/** The six launch subjects. e2e/unauthenticated.spec.ts asserts each name
 * verbatim, scoped to this section's aria-label - keep both intact. */
const SUBJECTS = [
  { name: "AP Calculus AB", icon: Sigma },
  { name: "AP Biology", icon: Dna },
  { name: "AP Psychology", icon: Brain },
  { name: "AP US History", icon: Landmark },
  { name: "AP Chemistry", icon: FlaskConical },
  { name: "AP Computer Science A", icon: Code2 },
];

export function SubjectShowcase() {
  return (
    <section aria-label="Priority AP subjects" className="mx-auto w-full max-w-6xl px-6 pb-24 sm:pb-28">
      <Reveal>
        <p className="text-center text-xs font-semibold tracking-[0.14em] text-muted-foreground uppercase">
          Launching with
        </p>
      </Reveal>

      <div className="mt-8 grid grid-cols-2 gap-3 sm:grid-cols-3 lg:grid-cols-6">
        {SUBJECTS.map(({ name, icon: Icon }, i) => (
          <Reveal key={name} index={i}>
            <Surface interactive className="flex h-full flex-col items-center gap-2.5 px-3 py-5 text-center">
              <span className="flex size-9 items-center justify-center rounded-full bg-blue-soft text-blue">
                <Icon className="size-4" aria-hidden="true" />
              </span>
              <span className="text-xs font-medium text-ink">{name}</span>
            </Surface>
          </Reveal>
        ))}
      </div>
    </section>
  );
}
