"use client";

import { useSession } from "next-auth/react";
import { useEffect } from "react";
import { useRouter } from "next/navigation";

export default function AuthGuard({ children, requiredAuthLevel }: { children: React.ReactNode; requiredAuthLevel: number | null }) {
  const { status, data: session } = useSession();
  const router = useRouter();

  useEffect(() => {
    if (status === "unauthenticated") {
      router.push("/login"); // Redirect to login if not authenticated
    } else if (status === "authenticated" && requiredAuthLevel !== null) {
      // Ensure the user has the correct authorization level
      if (!session?.user?.auth || session.user.auth < requiredAuthLevel) {
        router.back()
      }
    }
  }, [status, session?.user?.auth, router, requiredAuthLevel]);

  if (status === "loading") {
    return (
      <div className="flex items-center justify-center min-h-screen">
        <div className="animate-spin rounded-full h-16 w-16 border-t-4 border-blue-500"></div>
      </div>
    );
  }

  return <>{children}</>;
}
