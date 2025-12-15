"use client";

import React, { useMemo } from "react";
import { useSession } from "next-auth/react";
import { useRouter } from "next/navigation";

type UserShape = {
  name?: string | null;
  email?: string | null;
  image?: string | null;
};

export default function Overview() {
  const { data: session, status } = useSession();
  const router = useRouter();

  const user = useMemo<UserShape | null>(() => {
    if (!session?.user) return null;
    return {
      name: session.user.name ?? null,
      email: session.user.email ?? null,
      // eslint-disable-next-line @typescript-eslint/no-explicit-any
      image: (session.user as any).image ?? null,
    };
  }, [session]);

  if (status === "loading") {
    return <div className="text-sm text-[var(--muted)]">Loading overview…</div>;
  }

  const goToTab = (tab: string) => {
    router.replace(`/user?tab=${encodeURIComponent(tab)}`, { scroll: false });
  };

  return (
    <div>
      <div className="flex flex-col sm:flex-row sm:items-center sm:justify-between gap-4">
        <div>
          <p className="text-xs uppercase tracking-wider text-[var(--muted)]">
            Profile
          </p>
          <h2 className="text-xl font-semibold text-[var(--foreground)] mt-1">
            {user?.name || "Unnamed User"}
          </h2>
          <p className="text-sm text-[var(--muted)] mt-1">
            {user?.email || "—"}
          </p>
        </div>

        <div className="flex gap-2">
          <button
            type="button"
            className="px-3 py-2 text-sm rounded-lg border border-[var(--border)] text-[var(--foreground)] hover:bg-black/5 dark:hover:bg-white/5 transition"
          >
            Edit (soon)
          </button>
          <button
            type="button"
            className="px-3 py-2 text-sm rounded-lg bg-[var(--primary)] text-[var(--primary-foreground)] hover:opacity-90 transition"
          >
            New Character
          </button>
        </div>
      </div>

      <div className="h-px w-full bg-[var(--border)] my-4" />

      <div className="grid grid-cols-1 sm:grid-cols-3 gap-3">
        <button
          type="button"
          onClick={() => goToTab("messages")}
          className="text-left rounded-xl border border-[var(--border)] p-4 hover:bg-black/5 dark:hover:bg-white/5 transition cursor-pointer"
        >
          <p className="text-xs text-[var(--muted)]">Messages</p>
          <p className="text-2xl font-semibold text-[var(--foreground)] mt-1">
            —
          </p>
        </button>

        <button
          type="button"
          onClick={() => goToTab("forumPosts")}
          className="text-left rounded-xl border border-[var(--border)] p-4 hover:bg-black/5 dark:hover:bg-white/5 transition cursor-pointer"
        >
          <p className="text-xs text-[var(--muted)]">Forum Posts</p>
          <p className="text-2xl font-semibold text-[var(--foreground)] mt-1">
            —
          </p>
        </button>

        <button
          type="button"
          onClick={() => goToTab("characters")}
          className="text-left rounded-xl border border-[var(--border)] p-4 hover:bg-black/5 dark:hover:bg-white/5 transition cursor-pointer"
        >
          <p className="text-xs text-[var(--muted)]">Characters</p>
          <p className="text-2xl font-semibold text-[var(--foreground)] mt-1">
            —
          </p>
        </button>
      </div>
    </div>
  );
}
