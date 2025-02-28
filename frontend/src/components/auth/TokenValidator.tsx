"use client";
import { useSession, signOut } from "next-auth/react";
import { usePathname } from "next/navigation";
import { useEffect } from "react";

export default function TokenValidator() {
  const { data: session, status, update } = useSession();
  const path = usePathname();

  useEffect(() => {
    if (status === "loading" || !session?.expires) return;

    try {
      const expirationTime = new Date(session.expires).getTime();
      const currentTime = Date.now();

      if (expirationTime < currentTime) {
        console.warn("Session expired. Logging out...");
        signOut();
      } else if (expirationTime - currentTime < 60 * 60 * 1000) {
        update();
      }
    } catch (error) {
      console.error("Error in TokenValidator:", error);
    }
  }, [path]);

  return null;
}
