"use client";

import { useSession } from "next-auth/react";
import { useEffect } from "react";
import { useRouter } from "next/navigation";

export default function AuthGuard({requiredAuthLevel }: {requiredAuthLevel: number | null }) {
  const { status, data: session } = useSession();
  const router = useRouter();

  useEffect(() => {
    if (status === "unauthenticated") {
      router.push("/"); // Redirect to login if not authenticated
    } else if (status === "authenticated" && requiredAuthLevel !== null) {
      // Ensure the user has the correct authorization level
      if (!session?.user?.auth || session.user.auth < requiredAuthLevel) {
        router.back()
      }
    }
  }, [status, session?.user?.auth, router, requiredAuthLevel]);

  if (status === "loading") {
    return (
<div></div>
    );
  }

  return null;
}
