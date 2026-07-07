import { Table, TableBody, TableCell, TableHead, TableHeader, TableRow } from "@/components/ui/table";
import { SubjectMastery } from "@/lib/api";
import { WeakSpotBadge } from "@/components/shared/MasteryPills";

export function TopicBreakdownTable({ mastery }: { mastery: SubjectMastery }) {
  const rows = mastery.units.flatMap((unit) =>
    unit.topics.map((topic) => ({ unitName: unit.unit_name, ...topic }))
  );

  return (
    <Table>
      <TableHeader>
        <TableRow>
          <TableHead>Topic</TableHead>
          <TableHead>Unit</TableHead>
          <TableHead className="text-right">Mastery</TableHead>
          <TableHead className="text-right">Confidence</TableHead>
          <TableHead className="text-right">Attempts</TableHead>
        </TableRow>
      </TableHeader>
      <TableBody>
        {rows.map((row) => (
          <TableRow key={row.topic_id}>
            <TableCell className="font-medium text-navy">{row.topic_name}</TableCell>
            <TableCell className="text-muted-foreground">{row.unitName}</TableCell>
            <TableCell className="text-right">
              {row.mastery_score < 0.4 ? (
                <WeakSpotBadge label={`${Math.round(row.mastery_score * 100)}%`} />
              ) : (
                `${Math.round(row.mastery_score * 100)}%`
              )}
            </TableCell>
            <TableCell className="text-right">{Math.round(row.confidence_score * 100)}%</TableCell>
            <TableCell className="text-right">{row.attempts_count}</TableCell>
          </TableRow>
        ))}
      </TableBody>
    </Table>
  );
}
