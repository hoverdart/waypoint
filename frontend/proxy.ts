// Next.js 16 renamed the `middleware.ts` convention to `proxy.ts` (same
// underlying API - NextRequest/NextResponse, matcher config - just renamed;
// see AGENTS.md). Clerk's `clerkMiddleware()` helper itself is unaffected by
// the rename: it still returns a plain Next.js middleware-shaped function,
// which we now export as `proxy` instead of `middleware`.
import { clerkMiddleware, createRouteMatcher } from "@clerk/nextjs/server";

const isPublicRoute = createRouteMatcher(["/", "/login(.*)", "/signup(.*)"]);

export default clerkMiddleware(async (auth, req) => {
  if (!isPublicRoute(req)) {
    await auth.protect();
  }
});

export const config = {
  matcher: ["/((?!_next|.*\\..*).*)", "/(api|trpc)(.*)"],
};
