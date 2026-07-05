import "server-only";
import { auth } from "@clerk/nextjs/server";

/**
 * Server-side token getter for Server Components / Server Actions, matched
 * to lib/api/client.ts's TokenSource shape. [VERIFY vs Clerk's current docs]
 * getToken()'s exact call shape if Clerk's SDK changes across majors.
 */
export async function getServerAuthToken(): Promise<string | null> {
  const { getToken } = await auth();
  return getToken();
}
