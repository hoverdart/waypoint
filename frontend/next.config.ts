import path from "node:path";
import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  turbopack: { root: path.resolve(__dirname) },
  poweredByHeader: false,
  headers: async () => [{ source: "/:path*", headers: [
    { key: "X-Content-Type-Options", value: "nosniff" },
    { key: "X-Frame-Options", value: "DENY" },
    { key: "Content-Security-Policy", value: "frame-ancestors 'none'; object-src 'none'; base-uri 'self'" },
    { key: "Referrer-Policy", value: "strict-origin-when-cross-origin" },
  ] }],
};

export default nextConfig;
