"use client";

import { useSession } from "next-auth/react";
import { useRouter } from "next/navigation";
import { useEffect } from "react";

export default function UserPage() {
  const { data: session, status } = useSession();
  const router = useRouter();

  // Redirect if not authenticated
  useEffect(() => {
    if (status === "unauthenticated") {
      router.push("/");
    }
  }, [status, router]);

  if (status === "loading") {
    return (
      <div className="flex justify-center items-center min-h-[80vh] text-[var(--muted)]">
        Loading your profile...
      </div>
    );
  }

  const user = session?.user;

  return (
    <div className="section section-light min-h-screen flex flex-col items-center justify-start py-12 px-4 sm:px-6">
      <div className="card w-full max-w-md text-center">
        <h1 className="text-2xl font-semibold mb-4 text-[var(--foreground)]">
          Your Account
        </h1>

        {user?.image && (
          <img
            src={user.image}
            alt="Profile avatar"
            className="w-24 h-24 rounded-full mx-auto border border-[var(--border)] mb-4 object-cover"
          />
        )}

        <div className="space-y-2">
          <p className="text-lg font-medium text-[var(--foreground)]">
            {user?.name || "Unnamed User"}
          </p>
          <p className="text-[var(--muted)]">{user?.email}</p>
        </div>

        <div className="mt-6 border-t border-[var(--border)] pt-4 text-sm text-[var(--muted)]">
          <p>Linked providers update automatically after login.</p>
        </div>
      </div>
    </div>
  );
}
