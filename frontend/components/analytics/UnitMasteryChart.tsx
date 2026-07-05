"use client";

import { Bar, BarChart, CartesianGrid, XAxis, YAxis } from "recharts";
import { ChartContainer, ChartTooltip, ChartTooltipContent, type ChartConfig } from "@/components/ui/chart";
import { SubjectMastery } from "@/lib/api";

const chartConfig: ChartConfig = {
  mastery: { label: "Mastery", color: "var(--primary)" },
};

export function UnitMasteryChart({ mastery }: { mastery: SubjectMastery }) {
  const data = mastery.units.map((unit) => ({
    name: unit.unit_name.length > 18 ? `${unit.unit_name.slice(0, 18)}...` : unit.unit_name,
    mastery: Math.round(unit.mastery_score * 100),
  }));

  return (
    <ChartContainer config={chartConfig} className="aspect-auto h-64 w-full">
      <BarChart data={data}>
        <CartesianGrid vertical={false} />
        <XAxis dataKey="name" tickLine={false} axisLine={false} angle={-20} textAnchor="end" height={60} />
        <YAxis domain={[0, 100]} tickLine={false} axisLine={false} width={32} />
        <ChartTooltip content={<ChartTooltipContent />} />
        <Bar dataKey="mastery" fill="var(--color-mastery)" radius={4} />
      </BarChart>
    </ChartContainer>
  );
}
