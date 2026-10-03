import Link from "next/link";
import { ArrowUpRight } from "lucide-react";

const SUBJECTS = [
  { name: "AP Calculus AB", mark: "∫", note: "Change, one small step at a time.", color: "#e7ecdf" },
  { name: "AP Biology", mark: "Aa", note: "The extraordinary logic of living things.", color: "#e3ece6" },
  { name: "AP Psychology", mark: "ψ", note: "Get curious about how we think.", color: "#ece5df" },
  { name: "AP US History", mark: "1776", note: "See the connections behind the dates.", color: "#ede7d5" },
  { name: "AP Chemistry", mark: "H₂", note: "Find the patterns in the reactions.", color: "#e1e8eb" },
  { name: "AP Computer Science A", mark: "{ }", note: "Build the reasoning behind the code.", color: "#e8e5ed" },
];

export function SubjectShowcase() {
  return <section aria-label="Priority AP subjects" className="border-y border-border bg-[#eeeee5] py-16 sm:py-20">
    <div className="mx-auto w-full max-w-6xl px-6"><div className="mb-10 flex flex-wrap items-end justify-between gap-5"><div><p className="font-mono text-[10px] uppercase tracking-[0.18em] text-blue">Six subjects. So many possibilities.</p><h2 className="editorial-title mt-4 text-4xl sm:text-5xl">What’s on your desk?</h2></div><Link href="/subjects" className="text-sm font-medium text-blue underline underline-offset-4">Browse all courses</Link></div>
      <div className="grid gap-4 sm:grid-cols-2 lg:grid-cols-3">{SUBJECTS.map(subject => <Link key={subject.name} href="/subjects" className="group flex min-h-44 flex-col border border-ink/10 bg-card p-6 transition-colors hover:border-blue focus-visible:outline-2 focus-visible:outline-ring"><div className="mb-6 flex items-start justify-between"><span className="flex h-12 min-w-12 items-center justify-center px-2 font-serif text-2xl text-ink" style={{ backgroundColor: subject.color }} aria-hidden="true">{subject.mark}</span><ArrowUpRight className="size-4 text-ink-soft transition-transform group-hover:-translate-y-0.5 group-hover:translate-x-0.5" aria-hidden="true" /></div><h3 className="text-base font-semibold">{subject.name}</h3><p className="mt-2 text-sm text-muted-foreground">{subject.note}</p></Link>)}</div>
    </div>
  </section>;
}
