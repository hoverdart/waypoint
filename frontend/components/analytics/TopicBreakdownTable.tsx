import { Table, TableBody, TableCell, TableHead, TableHeader, TableRow } from "@/components/ui/table";
import { Chip } from "@/components/kit/Pills";
import { cn } from "@/lib/utils";
import { SubjectMastery } from "@/lib/api";

const HEAD = "h-9 px-3 text-xs font-semibold tracking-[0.14em] text-muted-foreground uppercase";
const NUM = "px-3 py-3 text-right tabular-nums text-ink-soft";

/** Tone-codes a mastery score the same way MasteryChip does, while leaving
 * the cell showing the bare percentage this table has always shown. */
function masteryTone(score: number) {
  if (score < 0.4) return "coral" as const;
  if (score < 0.7) return "amber" as const;
  return "green" as const;
}

export function TopicBreakdownTable({ mastery }: { mastery: SubjectMastery }) {
  const rows = mastery.units.flatMap((unit) =>
    unit.topics.map((topic) => ({ unitName: unit.unit_name, ...topic }))
  );

  return (
    <Table>
      <TableHeader>
        <TableRow className="border-border/60 hover:bg-transparent">
          <TableHead className={HEAD}>Topic</TableHead>
          <TableHead className={HEAD}>Unit</TableHead>
          <TableHead className={cn(HEAD, "text-right")}>Mastery</TableHead>
          <TableHead className={cn(HEAD, "text-right")}>Confidence</TableHead>
          <TableHead className={cn(HEAD, "text-right")}>Attempts</TableHead>
        </TableRow>
      </TableHeader>
      <TableBody>
        {rows.map((row) => (
          <TableRow key={row.topic_id} className="border-border/50 hover:bg-blue-soft/25">
            <TableCell className="px-3 py-3 font-medium text-ink">{row.topic_name}</TableCell>
            <TableCell className="px-3 py-3 text-muted-foreground">{row.unitName}</TableCell>
            <TableCell className="px-3 py-3 text-right">
              <Chip tone={masteryTone(row.mastery_score)} className="tabular-nums">
                {Math.round(row.mastery_score * 100)}%
              </Chip>
            </TableCell>
            <TableCell className={NUM}>{Math.round(row.confidence_score * 100)}%</TableCell>
            <TableCell className={NUM}>{row.attempts_count}</TableCell>
          </TableRow>
        ))}
      </TableBody>
    </Table>
  );
}
