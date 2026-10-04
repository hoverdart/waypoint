import { fireEvent, render, screen, waitFor } from "@testing-library/react";
import { beforeEach, describe, expect, it, vi } from "vitest";
import { CourseStudy } from "./CourseStudy";
const { start, push } = vi.hoisted(() => ({ start: vi.fn(), push: vi.fn() }));
vi.mock("next/navigation", () => ({ useRouter: () => ({ push }) }));
vi.mock("@/lib/hooks/useApiToken", () => ({ useApiToken: () => "token" }));
vi.mock("@/lib/api", () => ({ startPractice: start }));
vi.mock("./DiagnosticStartButton", () => ({ DiagnosticStartButton: () => <button>Take diagnostic</button> }));
const subject = { id: 1, name: "AP Biology", ap_exam_code: "biology", description: "Living systems", is_active: true, display_order: 1, units: [{ id: 2, subject_id: 1, name: "Cell structure", description: "Inside the cell", display_order: 1, ap_weight_min: 10, ap_weight_max: 13, topics: [{ id: 3, unit_id: 2, name: "Organelles", description: "Cell machinery", skill_tags: [], display_order: 1 }] }] };
describe("CourseStudy", () => {
  it("does not describe unknown unit weights as zero percent of the exam", () => {
    render(<CourseStudy subject={{ ...subject, units: [{ ...subject.units[0], ap_weight_min: 0, ap_weight_max: 0 }] }} />);
    expect(screen.getByText(/No official unit weighting/)).toBeVisible();
    expect(screen.queryByText(/0–0%/)).not.toBeInTheDocument();
  });

  beforeEach(() => vi.clearAllMocks());
  it("searches topics and explains empty results", () => {
    render(<CourseStudy subject={subject} />);
    fireEvent.change(screen.getByLabelText("Search units and topics"), { target: { value: "nothing" } });
    expect(screen.getByText(/No topics match/)).toBeInTheDocument();
    fireEvent.change(screen.getByLabelText("Search units and topics"), { target: { value: "Organelles" } });
    expect(screen.getByText("Cell structure")).toBeInTheDocument();
  });
  it("starts selected topic practice with chosen format and count", async () => {
    start.mockResolvedValue({ session_id: 42, questions: [{ id: 1 }] });
    render(<CourseStudy subject={subject} />);
    fireEvent.change(screen.getByLabelText("Question format"), { target: { value: "frq" } });
    fireEvent.change(screen.getByLabelText("Session length"), { target: { value: "5" } });
    fireEvent.click(screen.getByLabelText("Practice Organelles"));
    await waitFor(() => expect(push).toHaveBeenCalledWith("/practice/session/42"));
    expect(start).toHaveBeenCalledWith({ subject_id: 1, unit_id: 2, topic_id: 3, session_type: "frq", question_count: 5 }, "token");
  });
  it("shows recoverable API errors", async () => {
    start.mockRejectedValue(new Error("Try again shortly"));
    render(<CourseStudy subject={subject} />);
    fireEvent.click(screen.getByRole("button", { name: "Practice the whole course" }));
    expect(await screen.findByRole("alert")).toHaveTextContent("Try again shortly");
    expect(push).not.toHaveBeenCalled();
  });
  it("does not navigate into an empty question session", async () => {
    start.mockResolvedValue({ session_id: 42, questions: [] });
    render(<CourseStudy subject={subject} />);
    fireEvent.click(screen.getByRole("button", { name: "Practice the whole course" }));
    expect(await screen.findByRole("alert")).toHaveTextContent("no questions");
    expect(push).not.toHaveBeenCalled();
  });
});
