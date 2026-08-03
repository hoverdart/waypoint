import { beforeEach, describe, expect, it, vi } from "vitest";
import { render, screen, waitFor } from "@testing-library/react";
import userEvent from "@testing-library/user-event";
import { ProfileSettings } from "./ProfileSettings";

const mocks = vi.hoisted(() => ({ refresh: vi.fn(), updateMe: vi.fn() }));

vi.mock("next/navigation", () => ({ useRouter: () => ({ refresh: mocks.refresh }) }));
vi.mock("@/lib/hooks/useApiToken", () => ({ useApiToken: () => "test-token" }));
vi.mock("@/lib/api", async (importOriginal) => ({ ...(await importOriginal<typeof import("@/lib/api")>()), updateMe: mocks.updateMe }));

describe("ProfileSettings", () => {
  beforeEach(() => vi.clearAllMocks());

  it("updates both profile fields", async () => {
    const user = userEvent.setup();
    mocks.updateMe.mockResolvedValue({});
    render(<ProfileSettings initialName="Ada" initialGrade={10} />);

    await user.clear(screen.getByLabelText("Name"));
    await user.type(screen.getByLabelText("Name"), "Grace");
    await user.selectOptions(screen.getByLabelText("Grade"), "11");
    await user.click(screen.getByRole("button", { name: "Save profile" }));

    await waitFor(() => expect(mocks.updateMe).toHaveBeenCalledWith(
      { display_name: "Grace", grade_level: 11 },
      "test-token"
    ));
    expect(mocks.refresh).toHaveBeenCalled();
  });
});
