import Link from "next/link";
import { Chip } from "@/components/kit/Pills";
import { Table, TableBody, TableCell, TableHead, TableHeader, TableRow } from "@/components/ui/table";
import { AdminQuestion } from "@/lib/api";

const STATUS_TONE: Record<AdminQuestion["validation_status"], "neutral" | "amber" | "green" | "coral"> = {
  draft: "neutral",
  needs_review: "amber",
  approved: "green",
  rejected: "coral",
};

const HEAD = "h-9 px-3 text-xs font-semibold tracking-[0.14em] text-muted-foreground uppercase";

export function AdminQuestionsTable({ questions }: { questions: AdminQuestion[] }) {
  return (
    <Table>
      <TableHeader>
        <TableRow className="border-border/60 hover:bg-transparent">
          <TableHead className={HEAD}>ID</TableHead>
          <TableHead className={HEAD}>Prompt</TableHead>
          <TableHead className={HEAD}>Type</TableHead>
          <TableHead className={HEAD}>Difficulty</TableHead>
          <TableHead className={HEAD}>Status</TableHead>
        </TableRow>
      </TableHeader>
      <TableBody>
        {questions.map((q) => (
          <TableRow key={q.id} className="border-border/50 hover:bg-blue-soft/25">
            <TableCell className="px-3 py-3 tabular-nums text-muted-foreground">{q.id}</TableCell>
            <TableCell className="max-w-md truncate px-3 py-3">
              <Link href={`/admin/questions/${q.id}`} className="text-ink hover:text-blue hover:underline">
                {q.prompt}
              </Link>
            </TableCell>
            <TableCell className="px-3 py-3 text-muted-foreground uppercase">{q.type}</TableCell>
            <TableCell className="px-3 py-3 text-ink-soft">{q.difficulty}</TableCell>
            <TableCell className="px-3 py-3">
              <Chip tone={STATUS_TONE[q.validation_status]}>{q.validation_status}</Chip>
            </TableCell>
          </TableRow>
        ))}
      </TableBody>
    </Table>
  );
}
