/** Ambient page backdrop: two soft radial lobes washing down from above the
 * top edge, over a fine grain layer. Fixed and non-interactive so it stays
 * put while content scrolls past it. */
export function AuraBackdrop() {
  return (
    <div aria-hidden="true" className="pointer-events-none fixed inset-0 -z-10 overflow-hidden">
      <div className="aura absolute inset-x-0 top-0 h-[70vh] opacity-70 dark:opacity-50" />
      <div className="grain absolute inset-0 opacity-[0.035] mix-blend-multiply dark:opacity-[0.06] dark:mix-blend-screen" />
    </div>
  );
}
