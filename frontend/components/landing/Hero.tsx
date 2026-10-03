import { PillLink } from "@/components/kit/PillButton";

const COURSES = ["Calculus AB", "Biology", "Psychology", "US History", "Chemistry", "Computer Science A"];

export function Hero() {
  return <section aria-label="Hero" className="mx-auto w-full max-w-6xl px-6 pt-12 pb-16 lg:pt-20">
    <div className="flex items-center justify-between border-b border-border pb-4 font-mono text-[10px] uppercase tracking-[0.18em] text-ink-soft"><span>A field guide to your next 5</span><span>Made for the work in between.</span></div>
    <div className="grid items-center gap-14 py-12 lg:grid-cols-[1.1fr_0.9fr] lg:py-20">
      <div>
        <p className="mb-6 text-sm font-medium text-accent-coral">Less second-guessing. More getting somewhere.</p>
        <h1 className="editorial-title max-w-2xl text-6xl sm:text-7xl lg:text-[88px]">Big ambitions.<br />Small, <em className="text-blue">daily</em><br />breakthroughs.</h1>
        <p className="mt-7 max-w-md text-base leading-7 text-ink-soft">Every day, we tell you exactly what to study next to maximize your AP score. A clear plan, thoughtful practice, and room to get it wrong along the way.</p>
        <div className="mt-8 flex flex-wrap gap-3"><PillLink href="/signup" size="lg" arrow>Find your starting point</PillLink><PillLink href="#courses" variant="ghost" size="lg">Explore the courses ↓</PillLink></div>
        <p className="mt-5 text-xs text-muted-foreground">Six AP courses. Your pace. One place to begin.</p>
      </div>
      <div className="relative mx-auto w-full max-w-md">
        <div className="absolute -inset-3 rotate-3 border border-border bg-[#e9e6d9]" aria-hidden="true" />
        <div className="relative border border-border bg-card p-7 shadow-lift sm:p-9">
          <div className="flex justify-between border-b border-border pb-6"><span className="font-mono text-[10px] uppercase tracking-[0.2em]">The daily study note</span><span className="text-xs text-accent-coral">An example day</span></div>
          <h2 className="editorial-title mt-7 text-4xl">A little further<br />than yesterday.</h2>
          <p className="mt-3 text-sm text-muted-foreground">Three focused stops. Then, go live your life.</p>
          <ol className="mt-8 space-y-0">
            {[
              { number: "01", course: "BIOLOGY", title: "Make sense of cell signals", detail: "Revisit a concept before it fades.", time: "8 min" },
              { number: "02", course: "CALCULUS AB", title: "Find your limits", detail: "Turn a shaky topic into a steady one.", time: "12 min" },
              { number: "03", course: "US HISTORY", title: "Connect cause and effect", detail: "Put your reasoning into words.", time: "10 min" },
            ].map(item => <li key={item.number} className="flex gap-4 border-t border-border py-5"><span className="pt-1 font-mono text-xs text-muted-foreground">{item.number}</span><div className="flex-1"><p className="font-mono text-[9px] tracking-[0.14em] text-blue">{item.course}</p><h3 className="mt-1 font-semibold">{item.title}</h3><p className="mt-1 text-xs text-muted-foreground">{item.detail}</p></div><span className="pt-1 text-xs text-muted-foreground">{item.time}</span></li>)}
          </ol>
          <div className="flex justify-between border-t border-ink pt-5 text-xs font-medium"><span>A plan built around what you know.</span><span>30 min</span></div>
        </div>
      </div>
    </div>
    <div id="courses" className="scroll-mt-28 border-y border-border py-6"><p className="mb-4 font-mono text-[10px] uppercase tracking-[0.18em] text-muted-foreground">Pick your direction</p><div className="flex flex-wrap gap-x-7 gap-y-3">{COURSES.map(course => <span key={course} className="text-sm font-medium">{course}</span>)}</div></div>
  </section>;
}
