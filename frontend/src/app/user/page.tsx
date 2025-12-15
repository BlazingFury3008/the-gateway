"use client";

import Settings from "@/components/user/Settings";
import { useSession } from "next-auth/react";
import { useRouter } from "next/navigation";
import React, { useEffect, useMemo, useState } from "react";

type TabKey =
  | "overview"
  | "messages"
  | "forumPosts"
  | "characters"
  | "homebrew"
  | "settings";

export default function UserPage() {
  const { data: session, status } = useSession();
  const router = useRouter();

  useEffect(() => {
    if (status === "unauthenticated") router.push("/");
  }, [status, router]);

  const user = session?.user;

  const tabs = useMemo(
    () =>
      [
        { key: "overview", label: "Overview" },
        { key: "messages", label: "Messages" },
        { key: "forumPosts", label: "Forum Posts" },
        { key: "characters", label: "Characters" },
        { key: "homebrew", label: "Homebrew" },
        { key: "settings", label: "Settings/Options" },
      ] as const,
    []
  );

  const [activeTab, setActiveTab] = useState<TabKey>("overview");

  if (status === "loading") {
    return (
      <div className="flex justify-center items-center min-h-[80vh] text-[var(--muted)]">
        Loading your profile...
      </div>
    );
  }

  const TabPill = ({
    tabKey,
    label,
  }: {
    tabKey: TabKey;
    label: string;
  }) => {
    const isActive = activeTab === tabKey;

    return (
      <button
        type="button"
        onClick={() => setActiveTab(tabKey)}
        className={[
          "relative px-3 py-2 text-sm rounded-full transition-all whitespace-nowrap",
          "border border-[var(--border)]",
          "backdrop-blur-sm",
          isActive
            ? "text-[var(--foreground)] bg-[var(--background)] shadow-sm"
            : "text-[var(--muted)] bg-transparent hover:bg-black/5 dark:hover:bg-white/5 hover:text-[var(--foreground)]",
        ].join(" ")}
        aria-current={isActive ? "page" : undefined}
      >
        {/* active indicator */}
        <span
          className={[
            "absolute -bottom-[2px] left-1/2 -translate-x-1/2 h-[3px] w-8 rounded-full transition-opacity",
            "bg-[var(--primary)]",
            isActive ? "opacity-100" : "opacity-0",
          ].join(" ")}
        />
        {label}
      </button>
    );
  };

  const PanelShell = ({ children }: { children: React.ReactNode }) => (
    <div className="rounded-2xl border border-[var(--border)] bg-[var(--background)]/60 backdrop-blur-sm p-5 sm:p-6">
      {children}
    </div>
  );

  const Divider = () => (
    <div className="h-px w-full bg-[var(--border)] my-4" />
  );

  const Panel = () => {
    switch (activeTab) {
      case "overview":
        return (
          <PanelShell>
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

            <Divider />

            <div className="grid grid-cols-1 sm:grid-cols-3 gap-3">
              <div className="rounded-xl border border-[var(--border)] p-4">
                <p className="text-xs text-[var(--muted)]">Messages</p>
                <p className="text-2xl font-semibold text-[var(--foreground)] mt-1">
                  —
                </p>
              </div>
              <div className="rounded-xl border border-[var(--border)] p-4">
                <p className="text-xs text-[var(--muted)]">Forum Posts</p>
                <p className="text-2xl font-semibold text-[var(--foreground)] mt-1">
                  —
                </p>
              </div>
              <div className="rounded-xl border border-[var(--border)] p-4">
                <p className="text-xs text-[var(--muted)]">Characters</p>
                <p className="text-2xl font-semibold text-[var(--foreground)] mt-1">
                  —
                </p>
              </div>
            </div>
          </PanelShell>
        );

      case "messages":
        return (
          <PanelShell>
            <div className="flex items-start justify-between gap-4">
              <div>
                <p className="text-xs uppercase tracking-wider text-[var(--muted)]">
                  Inbox
                </p>
                <h2 className="text-xl font-semibold text-[var(--foreground)] mt-1">
                  Messages
                </h2>
                <p className="text-sm text-[var(--muted)] mt-1">
                  Coming soon: conversations, notifications, and replies.
                </p>
              </div>
              <button
                type="button"
                className="px-3 py-2 text-sm rounded-lg bg-[var(--primary)] text-[var(--primary-foreground)] hover:opacity-90 transition"
              >
                New Message
              </button>
            </div>

            <Divider />

            <div className="rounded-xl border border-[var(--border)] p-4 text-sm text-[var(--muted)]">
              No messages to show yet.
            </div>
          </PanelShell>
        );

      case "forumPosts":
        return (
          <PanelShell>
            <div>
              <p className="text-xs uppercase tracking-wider text-[var(--muted)]">
                Activity
              </p>
              <h2 className="text-xl font-semibold text-[var(--foreground)] mt-1">
                Forum Posts
              </h2>
              <p className="text-sm text-[var(--muted)] mt-1">
                Coming soon: your threads, replies, and bookmarks.
              </p>
            </div>

            <Divider />

            <div className="rounded-xl border border-[var(--border)] p-4 text-sm text-[var(--muted)]">
              Nothing here yet.
            </div>
          </PanelShell>
        );

      case "characters":
        return (
          <PanelShell>
            <div className="flex items-start justify-between gap-4">
              <div>
                <p className="text-xs uppercase tracking-wider text-[var(--muted)]">
                  Library
                </p>
                <h2 className="text-xl font-semibold text-[var(--foreground)] mt-1">
                  Characters
                </h2>
                <p className="text-sm text-[var(--muted)] mt-1">
                  Coming soon: browse, create, and manage your characters.
                </p>
              </div>
              <button
                type="button"
                className="px-3 py-2 text-sm rounded-lg bg-[var(--primary)] text-[var(--primary-foreground)] hover:opacity-90 transition"
              >
                Create
              </button>
            </div>

            <Divider />

            <div className="grid grid-cols-1 sm:grid-cols-2 gap-3">
              <div className="rounded-xl border border-[var(--border)] p-4 text-sm text-[var(--muted)]">
                No characters yet.
              </div>
              <div className="rounded-xl border border-[var(--border)] p-4 text-sm text-[var(--muted)]">
                Drafts will appear here.
              </div>
            </div>
          </PanelShell>
        );

      case "homebrew":
        return (
          <PanelShell>
            <div className="flex items-start justify-between gap-4">
              <div>
                <p className="text-xs uppercase tracking-wider text-[var(--muted)]">
                  Workshop
                </p>
                <h2 className="text-xl font-semibold text-[var(--foreground)] mt-1">
                  Homebrew
                </h2>
                <p className="text-sm text-[var(--muted)] mt-1">
                  Coming soon: create and publish homebrew content.
                </p>
              </div>
              <button
                type="button"
                className="px-3 py-2 text-sm rounded-lg border border-[var(--border)] text-[var(--foreground)] hover:bg-black/5 dark:hover:bg-white/5 transition"
              >
                New (soon)
              </button>
            </div>

            <Divider />

            <div className="rounded-xl border border-[var(--border)] p-4 text-sm text-[var(--muted)]">
              No homebrew yet.
            </div>
          </PanelShell>
        );

      case "settings":
        return (
          <PanelShell>
            <Settings/>
          </PanelShell>
        );

      default:
        return null;
    }
  };

  return (
    <div className="section section-light min-h-screen flex flex-col items-center justify-start py-12 px-4 sm:px-6">
      <div className="w-full max-w-5xl space-y-6">
        {/* Top banner card */}
        <div className="card overflow-hidden">
          <div className="relative">
            {/* subtle header gradient */}
            <div className="h-24 sm:h-28 bg-gradient-to-r from-black/10 via-black/0 to-black/10 dark:from-white/5 dark:via-white/0 dark:to-white/5" />
            <div className="px-5 sm:px-6 pb-5 -mt-10 sm:-mt-12 flex flex-col sm:flex-row sm:items-end sm:justify-between gap-4">
              <div className="flex items-center gap-4">
                {user?.image ? (
                  <img
                    src={user.image}
                    alt="Profile avatar"
                    className="w-20 h-20 sm:w-24 sm:h-24 rounded-2xl border border-[var(--border)] object-cover bg-[var(--background)]"
                  />
                ) : (
                  <div className="w-20 h-20 sm:w-24 sm:h-24 rounded-2xl border border-[var(--border)] flex items-center justify-center text-[var(--muted)] bg-[var(--background)]">
                    ?
                  </div>
                )}

                <div>
                  <p className="text-xs uppercase tracking-wider text-[var(--muted)]">
                    Account
                  </p>
                  <h1 className="text-2xl sm:text-3xl font-semibold text-[var(--foreground)] mt-1">
                    {user?.name || "Unnamed User"}
                  </h1>
                  <p className="text-sm text-[var(--muted)] mt-1">
                    {user?.email || "—"}
                  </p>
                </div>
              </div>

              {/* tab row */}
              <div className="flex gap-2 overflow-x-auto pb-1">
                {tabs.map((t) => (
                  <TabPill key={t.key} tabKey={t.key} label={t.label} />
                ))}
              </div>
            </div>
          </div>
        </div>

        {/* Active panel */}
        <Panel />
      </div>
    </div>
  );
}
