import type { ReleasedExamResource } from "@/lib/api/types";

export function ReleasedExamResources({ resources }: { resources: ReleasedExamResource[] }) {
  if (!resources.length) return null;
  return <section aria-labelledby="released-exams" className="mb-10 border-y border-border py-6">
    <p className="font-mono text-xs uppercase tracking-widest text-blue">From the exam archive</p>
    <h2 id="released-exams" className="mt-2 font-display text-2xl">Practice with released AP questions</h2>
    <p className="mt-3 max-w-2xl text-sm leading-relaxed text-muted-foreground">Open College Board’s released free-response questions, then compare your work with the scoring guides and available student samples. Older materials may use a different course framework or exam format.</p>
    <ul className="mt-5 divide-y divide-border">
      {resources.map(resource => <li key={resource.url} className="py-3">
        <a href={resource.url} target="_blank" rel="noopener noreferrer" className="text-sm font-medium text-blue underline underline-offset-4">
          {resource.title}<span className="sr-only"> (opens College Board in a new tab)</span> ↗
        </a>
        <span className="ml-3 text-xs text-muted-foreground">{resource.kind === "archive" ? "Official archive" : "PDF"}</span>
      </li>)}
    </ul>
    <p className="mt-3 text-xs text-muted-foreground">These resources open on College Board’s website. Work completed there is not saved or scored in WayPoint.</p>
  </section>;
}
