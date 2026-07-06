import { afterEach, describe, expect, it, vi } from "vitest";
import { apiFetch, ApiError } from "./client";

function mockFetchOnce(response: Partial<Response> & { jsonBody?: unknown }) {
  const { jsonBody, ...rest } = response;
  const fetchMock = vi.fn().mockResolvedValue({
    ok: true,
    status: 200,
    statusText: "OK",
    json: async () => jsonBody,
    ...rest,
  } as Response);
  vi.stubGlobal("fetch", fetchMock);
  return fetchMock;
}

describe("apiFetch", () => {
  afterEach(() => {
    vi.unstubAllGlobals();
  });

  it("resolves with the parsed JSON body on success", async () => {
    mockFetchOnce({ jsonBody: { id: 1, name: "AP Calculus AB" } });
    const result = await apiFetch<{ id: number; name: string }>("/subjects/1");
    expect(result).toEqual({ id: 1, name: "AP Calculus AB" });
  });

  it("sends an Authorization header when given a static token", async () => {
    const fetchMock = mockFetchOnce({ jsonBody: {} });
    await apiFetch("/dashboard", { token: "static-token" });
    const [, init] = fetchMock.mock.calls[0];
    expect(init.headers.Authorization).toBe("Bearer static-token");
  });

  it("resolves a token getter function before sending the request", async () => {
    const fetchMock = mockFetchOnce({ jsonBody: {} });
    await apiFetch("/dashboard", { token: async () => "async-token" });
    const [, init] = fetchMock.mock.calls[0];
    expect(init.headers.Authorization).toBe("Bearer async-token");
  });

  it("omits the Authorization header when no token is given", async () => {
    const fetchMock = mockFetchOnce({ jsonBody: {} });
    await apiFetch("/subjects");
    const [, init] = fetchMock.mock.calls[0];
    expect(init.headers.Authorization).toBeUndefined();
  });

  it("serializes the body and sets Content-Type for mutating requests", async () => {
    const fetchMock = mockFetchOnce({ jsonBody: {} });
    await apiFetch("/onboarding", { method: "POST", body: { mode: "gamified" } });
    const [, init] = fetchMock.mock.calls[0];
    expect(init.method).toBe("POST");
    expect(init.headers["Content-Type"]).toBe("application/json");
    expect(init.body).toBe(JSON.stringify({ mode: "gamified" }));
  });

  it("appends defined search params to the URL", async () => {
    const fetchMock = mockFetchOnce({ jsonBody: {} });
    await apiFetch("/admin/questions", { searchParams: { validation_status: "approved", page: undefined } });
    const [url] = fetchMock.mock.calls[0];
    expect(url).toContain("validation_status=approved");
    expect(url).not.toContain("page=");
  });

  it("throws an ApiError with the response status and detail message on failure", async () => {
    mockFetchOnce({ ok: false, status: 403, statusText: "Forbidden", jsonBody: { detail: "Admins only" } });
    await expect(apiFetch("/admin/questions")).rejects.toMatchObject(
      new ApiError(403, "Admins only")
    );
  });

  it("falls back to statusText when the error response isn't JSON", async () => {
    const fetchMock = vi.fn().mockResolvedValue({
      ok: false,
      status: 500,
      statusText: "Internal Server Error",
      json: async () => {
        throw new Error("not json");
      },
    } as unknown as Response);
    vi.stubGlobal("fetch", fetchMock);

    await expect(apiFetch("/dashboard")).rejects.toMatchObject(
      new ApiError(500, "Internal Server Error")
    );
  });

  it("returns undefined for a 204 No Content response", async () => {
    mockFetchOnce({ status: 204 });
    const result = await apiFetch("/daily-plan/items/1");
    expect(result).toBeUndefined();
  });
});
