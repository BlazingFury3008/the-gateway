"use client";

import { useEffect, useRef } from "react";
import { usePathname, useSearchParams } from "next/navigation";

/**
 * Calls your backend refresh endpoint whenever the URL changes.
 * Assumes the refresh token is stored as an HttpOnly cookie (recommended),
 * and the endpoint returns a new accessToken (JWT) in JSON.
 */
export default function TokenRefresher() {
  const pathname = usePathname();
  const searchParams = useSearchParams();

  // Prevent double-calls in React Strict Mode in dev
  const didRunOnceForUrl = useRef<string>("");

  useEffect(() => {
    const url = `${pathname}?${searchParams?.toString() ?? ""}`;

    // Avoid duplicate calls for same URL (helps in dev + avoids noisy refreshes)
    if (didRunOnceForUrl.current === url) return;
    didRunOnceForUrl.current = url;

    const refresh = async () => {
      try {
        // Call your refresh endpoint
        const res = await fetch(`${process.env.NEXT_PUBLIC_API_URL}/auth/refresh`, {
          method: "POST",
          credentials: "include", // <-- important for HttpOnly cookies
          headers: { "Content-Type": "application/json" },
        });

        if (!res.ok) return;

        const data = await res.json();

        // Store the new access token wherever your app expects it:
        // - memory (context/zustand)
        // - localStorage (less ideal)
        // Here’s a simple localStorage example:
        if (data?.accessToken) {
          localStorage.setItem("accessToken", data.accessToken);
        }
      } catch {
        // ignore refresh failures; user may be logged out
      }
    };

    refresh();
  }, [pathname, searchParams]);

  return null;
}
