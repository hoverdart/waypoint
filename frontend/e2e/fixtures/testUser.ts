import { createClerkClient } from "@clerk/backend";

/** Creates a throwaway Clerk user for one E2E run and returns a `remove()`
 * cleanup function. Requires CLERK_SECRET_KEY - callers should skip the
 * whole spec first if it isn't set, rather than let this throw. */
export async function createTestUser() {
  const clerkClient = createClerkClient({ secretKey: process.env.CLERK_SECRET_KEY! });
  const email = `waypoint-e2e-${Date.now()}-${Math.random().toString(36).slice(2)}@example.com`;

  const user = await clerkClient.users.createUser({
    emailAddress: [email],
    skipPasswordRequirement: true,
    firstName: "E2E",
    lastName: "Tester",
  });

  return {
    email,
    userId: user.id,
    async remove() {
      await clerkClient.users.deleteUser(user.id);
    },
  };
}
