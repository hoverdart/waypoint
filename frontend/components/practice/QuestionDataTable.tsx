import type { DataTable } from "@/lib/api/types";

export function QuestionDataTable({ table }: { table?: DataTable | null }) {
  if (!table) return null;
  return <figure className="min-w-0 [overflow-wrap:anywhere] space-y-3 rounded-lg border border-border bg-background p-4">
    <div role="region" aria-label={table.caption} tabIndex={0} className="overflow-x-auto focus-visible:outline-2 focus-visible:outline-ring">
      <table className="w-full min-w-72 border-collapse text-left text-sm">
        <caption className="pb-4 text-left font-semibold">{table.caption}</caption>
        <thead><tr>{table.columns.map((column, index) => <th key={index} scope="col" className="border-b border-border px-2 py-2 align-bottom whitespace-nowrap">{column}</th>)}</tr></thead>
        <tbody>{table.rows.map((row, index) => <tr key={index}>{row.map((cell, column) => column === 0
          ? <th key={column} scope="row" className="border-b border-border px-2 py-3 font-medium">{cell}</th>
          : <td key={column} className="border-b border-border px-2 py-3 tabular-nums whitespace-nowrap">{cell}</td>)}</tr>)}</tbody>
      </table>
    </div>
    {table.note && <figcaption className="text-xs leading-relaxed text-muted-foreground">{table.note}</figcaption>}
  </figure>;
}
