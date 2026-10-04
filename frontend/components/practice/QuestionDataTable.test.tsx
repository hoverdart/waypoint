import { render, screen, within } from "@testing-library/react";
import { describe, expect, it } from "vitest";
import { QuestionDataTable } from "./QuestionDataTable";

describe("QuestionDataTable", () => {
  it("renders caption, scoped headers, cells and attribution", () => {
    render(<QuestionDataTable table={{ caption: "Historical income", columns: ["Year", "Income"], rows: [["1974", "$11,200"], ["1975", "$11,800"]], note: "Nominal dollars; Census P60-104." }} />);
    const table = screen.getByRole("table", { name: "Historical income" });
    expect(within(table).getAllByRole("columnheader")).toHaveLength(2);
    expect(within(table).getByRole("rowheader", { name: "1974" })).toHaveAttribute("scope", "row");
    expect(within(table).getByRole("cell", { name: "$11,800" })).toBeVisible();
    expect(screen.getByRole("region", { name: "Historical income" })).toHaveAttribute("tabindex", "0");
    expect(screen.getByText("Nominal dollars; Census P60-104.")).toBeVisible();
  });
  it("renders source content as text rather than HTML", () => {
    const { container } = render(<QuestionDataTable table={{ caption: "<script>alert(1)</script>", columns: ["Year", "Value"], rows: [["1975", "<img src=x onerror=alert(1)>"]] }} />);
    expect(screen.getByText("<img src=x onerror=alert(1)>")).toBeVisible();
    expect(container.querySelector("script, img")).toBeNull();
  });
  it("leaves existing questions without tables unchanged", () => {
    const { container } = render(<QuestionDataTable />);
    expect(container).toBeEmptyDOMElement();
  });
});
