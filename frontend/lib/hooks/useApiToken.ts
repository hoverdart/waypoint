"use client";

import { useAuth } from "@clerk/nextjs";
import { useCallback } from "react";

/** Client-side token getter for lib/api/client.ts's TokenSource shape. */
export function useApiToken() {
  const { getToken } = useAuth();
  return useCallback(() => getToken(), [getToken]);
}
