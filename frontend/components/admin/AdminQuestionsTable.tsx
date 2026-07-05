import Link from "next/link";
import { Badge } from "@/components/ui/badge";
import { Table, TableBody, TableCell, TableHead, TableHeader, TableRow } from "@/components/ui/table";
import { AdminQuestion } from "@/lib/api";

const STATUS_VARIANT: Record<AdminQuestion["validation_status"], "default" | "secondary" | "destructive" | "outline"> = {
  draft: "outline",
  needs_review: "secondary",
  approved: "default",
  rejected: "destructive",
};

export function AdminQuestionsTable({ questions }: { questions: AdminQuestion[] }) {
  return (
    <Table>
      <TableHeader>
        <TableRow>
          <TableHead>ID</TableHead>
          <TableHead>Prompt</TableHead>
          <TableHead>Type</TableHead>
          <TableHead>Difficulty</TableHead>
          <TableHead>Status</TableHead>
        </TableRow>
      </TableHeader>
      <TableBody>
        {questions.map((q) => (
          <TableRow key={q.id}>
            <TableCell>{q.id}</TableCell>
            <TableCell className="max-w-md truncate">
              <Link href={`/admin/questions/${q.id}`} className="hover:underline">
                {q.prompt}
              </Link>
            </TableCell>
            <TableCell className="uppercase text-muted-foreground">{q.type}</TableCell>
            <TableCell>{q.difficulty}</TableCell>
            <TableCell>
              <Badge variant={STATUS_VARIANT[q.validation_status]}>{q.validation_status}</Badge>
            </TableCell>
          </TableRow>
        ))}
      </TableBody>
    </Table>
  );
}
