const API_BASE_URL = process.env.NEXT_PUBLIC_API_BASE_URL ?? "http://localhost:8000";

export class ApiError extends Error {
  status: number;
  detail: string;

  constructor(status: number, detail: string) {
    super(detail);
    this.name = "ApiError";
    this.status = status;
    this.detail = detail;
  }
}

export type TokenSource = string | null | undefined | (() => Promise<string | null>);

interface ApiFetchOptions {
  method?: "GET" | "POST" | "PATCH" | "DELETE";
  body?: unknown;
  token?: TokenSource;
  searchParams?: Record<string, string | number | boolean | undefined>;
}

async function resolveToken(token: TokenSource): Promise<string | null> {
  if (typeof token === "function") return token();
  return token ?? null;
}

/**
 * Every network call in the app goes through this function - never fetch()
 * directly from a component. Accepts a token getter rather than importing
 * Clerk here, so this module works identically from Server Components,
 * Server Actions, and Client Components regardless of how each obtains the
 * session token.
 */
export async function apiFetch<T>(path: string, options: ApiFetchOptions = {}): Promise<T> {
  const { method = "GET", body, token, searchParams } = options;

  const url = new URL(path, API_BASE_URL);
  if (searchParams) {
    for (const [key, value] of Object.entries(searchParams)) {
      if (value !== undefined) url.searchParams.set(key, String(value));
    }
  }

  const headers: Record<string, string> = {};
  const resolvedToken = await resolveToken(token);
  if (resolvedToken) headers.Authorization = `Bearer ${resolvedToken}`;
  if (body !== undefined) headers["Content-Type"] = "application/json";

  const response = await fetch(url.toString(), {
    method,
    headers,
    body: body !== undefined ? JSON.stringify(body) : undefined,
    cache: "no-store",
  });

  if (!response.ok) {
    let detail = response.statusText;
    try {
      const data = await response.json();
      detail = data.detail ?? detail;
    } catch {
      // response body wasn't JSON - fall back to statusText
    }
    throw new ApiError(response.status, detail);
  }

  if (response.status === 204) return undefined as T;
  return response.json() as Promise<T>;
}
