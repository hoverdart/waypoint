"use client";

import { useSyncExternalStore } from "react";

const QUERY = "(prefers-reduced-motion: reduce)";

/** Not every environment that runs this code has matchMedia - jsdom doesn't
 * implement it at all, and it predates some of the browsers we still parse in. */
function canQuery(): boolean {
  return typeof window !== "undefined" && typeof window.matchMedia === "function";
}

function subscribe(onStoreChange: () => void): () => void {
  if (!canQuery()) return () => {};
  const mql = window.matchMedia(QUERY);
  mql.addEventListener("change", onStoreChange);
  return () => mql.removeEventListener("change", onStoreChange);
}

function getSnapshot(): boolean {
  return canQuery() ? window.matchMedia(QUERY).matches : false;
}

/** React uses this for the server render *and* for hydration, then re-renders
 * with the real client value. That's the whole point of this hook. */
function getServerSnapshot(): boolean {
  return false;
}

/**
 * Hydration-safe replacement for framer's `useReducedMotion`.
 *
 * The framer hook reports `false` during SSR (there's no `matchMedia` on the
 * server) but can report `true` on the very first client render. Any component
 * that *structurally* branches on it - returning a different element tree, a
 * different `initial` style, or a different `useState` seed - then renders
 * server HTML that doesn't match the client, so React throws
 * "Hydration failed..." and regenerates the whole subtree. That also stranded
 * `useScroll`'s target ref ("Target ref is defined but not hydrated").
 *
 * `useSyncExternalStore` is the right primitive here: it guarantees the
 * hydrating render matches the server via `getServerSnapshot`, then swaps in
 * the real preference on the next render. It also subscribes, so toggling the
 * OS setting updates the UI live - which a one-shot mount check wouldn't do.
 */
export function useSafeReducedMotion(): boolean {
  return useSyncExternalStore(subscribe, getSnapshot, getServerSnapshot);
}
