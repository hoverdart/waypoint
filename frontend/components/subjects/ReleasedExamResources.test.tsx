import { render, screen } from "@testing-library/react";
import { describe, expect, it } from "vitest";
import { ReleasedExamResources } from "./ReleasedExamResources";

describe("ReleasedExamResources", () => {
  it("shows external questions and scoring with clear tracking limits", () => {
    render(<ReleasedExamResources resources={[
      { title: "2025 · Set 1 · Questions", url: "https://apcentral.collegeboard.org/media/pdf/ap25-frq-english-language-set-1.pdf", kind: "questions", year: 2025, checked_on: "2026-10-04" },
      { title: "Official archive", url: "https://apcentral.collegeboard.org/courses/ap-biology/exam/past-exam-questions", kind: "archive", year: null, checked_on: "2026-10-04" },
    ]} />);
    const links = screen.getAllByRole("link");
    expect(links).toHaveLength(2);
    expect(links[0]).toHaveAttribute("target", "_blank");
    expect(links[0]).toHaveAttribute("rel", "noopener noreferrer");
    expect(screen.getByText(/not saved or scored in WayPoint/)).toBeInTheDocument();
    expect(screen.getByText(/Older materials may use a different/)).toBeInTheDocument();
  });
  it("omits an empty catalog", () => {
    const { container } = render(<ReleasedExamResources resources={[]} />);
    expect(container).toBeEmptyDOMElement();
  });
});
