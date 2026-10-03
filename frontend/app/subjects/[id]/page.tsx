import Link from "next/link";
import { notFound } from "next/navigation";
import { getSubject } from "@/lib/api";
import { ApiError } from "@/lib/api/client";
import { CourseStudy } from "@/components/subjects/CourseStudy";

export default async function CoursePage({ params }: { params: Promise<{ id: string }> }) {
  const { id } = await params;
  const subjectId = Number(id);
  if (!Number.isSafeInteger(subjectId) || subjectId < 1) notFound();
  const subject = await getSubject(subjectId).catch(error => {
    if (error instanceof ApiError && error.status === 404) notFound();
    throw error;
  });
  return <div className="mx-auto w-full max-w-6xl px-6 py-10">
    <Link href="/subjects" className="text-sm text-muted-foreground hover:text-foreground">← All courses</Link>
    <header className="mt-10 mb-12 border-b border-border pb-10">
      <p className="font-mono text-xs uppercase tracking-[0.2em] text-blue">The course notebook / {subject.units.length} units</p>
      <h1 className="mt-4 font-display text-4xl sm:text-6xl">{subject.name}</h1>
      <p className="mt-5 max-w-2xl text-lg leading-relaxed text-muted-foreground">{subject.description}</p>
    </header>
    <CourseStudy subject={subject} />
  </div>;
}
