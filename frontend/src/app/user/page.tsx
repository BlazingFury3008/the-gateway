"use client";

import Friends from "@/components/user/Friends";
import Overview from "@/components/user/Overview";
import Settings from "@/components/user/Settings";
import { useSession } from "next-auth/react";
import { useRouter, useSearchParams } from "next/navigation";
import React, {
  useEffect,
  useMemo,
  useState,
  useCallback,
  useRef,
} from "react";
import Image from "next/image";
import Forums from "@/components/user/Forums";
import Characters from "@/components/user/Characters";
import Messages from "@/components/user/Messages";
import Homebrew from "@/components/user/Homebrew";
import Wikis from "@/components/user/Wikis";

const FLASK_API_BASE =
  process.env.NEXT_PUBLIC_FLASK_API_BASE ?? "http://localhost:5000";

type TabKey =
  | "overview"
  | "friends"
  | "messages"
  | "forumPosts"
  | "characters"
  | "homebrew"
  | "wiki"
  | "settings";

const isTabKey = (v: string | null): v is TabKey => {
  return (
    v === "overview" ||
    v === "friends" ||
    v === "messages" ||
    v === "forumPosts" ||
    v === "characters" ||
    v === "homebrew" ||
    v === "wiki" ||
    v === "settings"
  );
};

export default function UserPage() {
  const { data: session, status, update } = useSession();
  const router = useRouter();
  const params = useSearchParams();

  useEffect(() => {
    if (status === "unauthenticated") router.push("/");
  }, [status, router]);

  const user = session?.user;
  const flaskToken = (session as any)?.accessToken as string | null;

  const tabs = useMemo(
    () =>
      [
        { key: "overview", label: "Overview" },
        { key: "friends", label: "Friends" },
        { key: "messages", label: "Messages" },
        { key: "forumPosts", label: "Forum Posts" },
        { key: "characters", label: "Characters" },
        { key: "homebrew", label: "Homebrew" },
        { key: "wiki", label: "Wiki" },
        { key: "settings", label: "Settings/Options" },
      ] as const,
    []
  );

  // URL tab (?tab=...)
  const tabFromUrl = params.get("tab");
  const derivedTab: TabKey = isTabKey(tabFromUrl) ? tabFromUrl : "overview";
  const [activeTab, setActiveTab] = useState<TabKey>(derivedTab);

  useEffect(() => {
    setActiveTab(derivedTab);
  }, [derivedTab]);

  const setTabInUrl = useCallback(
    (tab: TabKey) => {
      const sp = new URLSearchParams(params.toString());
      sp.set("tab", tab);
      router.replace(`/user?${sp.toString()}`, { scroll: false });
    },
    [params, router]
  );

  const onSelectTab = (tab: TabKey) => {
    setActiveTab(tab);
    setTabInUrl(tab);
  };

  const TabPill = ({ tabKey, label }: { tabKey: TabKey; label: string }) => {
    const isActive = activeTab === tabKey;

    return (
      <button
        type="button"
        onClick={() => onSelectTab(tabKey)}
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
    <div className="rounded-2xl border border-[var(--border)] bg-[var(--navbar)]/60 backdrop-blur-sm p-5 sm:p-6">
      {children}
    </div>
  );

  const Panel = () => {
    switch (activeTab) {
      case "overview":
        return (
          <PanelShell>
            <Overview />
          </PanelShell>
        );

      case "friends":
        return (
          <PanelShell>
            <Friends />
          </PanelShell>
        );

      case "messages":
        return (
          <PanelShell>
            <Messages />
          </PanelShell>
        );

      case "forumPosts":
        return (
          <PanelShell>
            <Forums />
          </PanelShell>
        );

      case "characters":
        return (
          <PanelShell>
            <Characters />
          </PanelShell>
        );

      case "homebrew":
        return (
          <PanelShell>
            <Homebrew />
          </PanelShell>
        );

      case "settings":
        return (
          <PanelShell>
            <Settings />
          </PanelShell>
        );
      case "wiki":
        return (
          <PanelShell>
            <Wikis />
          </PanelShell>
        );

      default:
        return null;
    }
  };

  // Avatar display (robust)
  const [avatarOk, setAvatarOk] = useState(true);
  const avatarSrc =
    typeof user?.image === "string" && user.image.trim().length > 0
      ? user.image
      : null;

  useEffect(() => {
    setAvatarOk(true);
  }, [avatarSrc]);

  // Avatar upload
  const fileInputRef = useRef<HTMLInputElement | null>(null);
  const [avatarUploading, setAvatarUploading] = useState(false);
  const [avatarMsg, setAvatarMsg] = useState<string | null>(null);
  const [avatarErr, setAvatarErr] = useState<string | null>(null);

  const pickAvatar = () => {
    setAvatarMsg(null);
    setAvatarErr(null);

    if (!flaskToken) {
      setAvatarErr("Session expired. Please log in again.");
      return;
    }
    fileInputRef.current?.click();
  };

  async function uploadAvatar(file: File) {
    setAvatarMsg(null);
    setAvatarErr(null);

    if (!flaskToken) {
      setAvatarErr("Session expired. Please log in again.");
      return;
    }

    // Basic validation
    const allowed = ["image/png", "image/jpeg", "image/webp"];
    if (!allowed.includes(file.type)) {
      setAvatarErr("Please upload a PNG, JPG, or WEBP image.");
      return;
    }
    if (file.size > 5 * 1024 * 1024) {
      setAvatarErr("Max file size is 5MB.");
      return;
    }

    setAvatarUploading(true);
    try {
      const fd = new FormData();
      fd.append("image", file);

      const res = await fetch(`${FLASK_API_BASE}/auth/set-image`, {
        method: "POST",
        headers: {
          Authorization: `Bearer ${flaskToken}`,
        },
        body: fd,
      });

      const data = await res.json().catch(() => ({}));
      if (!res.ok) throw new Error(data.error || "Failed to upload image.");

      // Ensure avatar rerenders + avoid cached image URL
      const newUrl = String(data.image || "");
      setAvatarOk(true);

      // Patch NextAuth session so header & other components update immediately
      await update({
        image: newUrl,
        picture: newUrl, // keep both because some callbacks map picture->image
        name: data.name,
        email: data.email,
        linked_accounts: data.linked_accounts,
        accessToken: data.accessToken, // if your backend rotates tokens; harmless if same
      });

      setAvatarMsg("Profile picture updated.");
    } catch (e: any) {
      setAvatarErr(e?.message || "Failed to upload image.");
    } finally {
      setAvatarUploading(false);
    }
  }

  const onAvatarFileChange: React.ChangeEventHandler<HTMLInputElement> = async (
    e
  ) => {
    const file = e.target.files?.[0] ?? null;
    // reset input so selecting the same file again still triggers change
    e.target.value = "";
    if (!file) return;
    await uploadAvatar(file);
  };

  const msgTimerRef = useRef<number | null>(null);

  useEffect(() => {
    // clear any existing timer
    if (msgTimerRef.current !== null) {
      window.clearTimeout(msgTimerRef.current);
      msgTimerRef.current = null;
    }

    // start timer only when message is non-null
    if (avatarMsg !== null) {
      msgTimerRef.current = window.setTimeout(() => {
        setAvatarMsg(null);
      }, 5000);
    }

    return () => {
      if (msgTimerRef.current !== null) {
        window.clearTimeout(msgTimerRef.current);
        msgTimerRef.current = null;
      }
    };
  }, [avatarMsg]);

  if (status === "loading") {
    return (
      <div className="flex justify-center items-center min-h-[80vh] text-[var(--muted)]">
        Loading your profile...
      </div>
    );
  }

  return (
    <div className="section section-light min-h-screen flex flex-col items-center justify-start py-12 px-4 sm:px-6">
      <div className="w-full max-w-5xl space-y-6">
        {/* Top banner card */}
        <div className="card overflow-hidden">
          {/* Gradient header ONLY */}
          <div className="relative">
            <div className="h-24 sm:h-28 bg-gradient-to-r from-black/10 via-black/0 to-black/10 dark:from-white/5 dark:via-white/0 dark:to-white/5" />

            {/* Identity row */}
            <div className="px-5 sm:px-6 pb-4 -mt-10 sm:-mt-12">
              <div className="flex flex-col sm:flex-row sm:items-end sm:justify-between gap-4">
                <div className="flex items-center gap-4">
                  {/* Hidden file input */}
                  <input
                    ref={fileInputRef}
                    type="file"
                    accept="image/png,image/jpeg,image/webp"
                    className="hidden"
                    onChange={onAvatarFileChange}
                  />

                  {/* Clickable avatar */}
                  <button
                    type="button"
                    onClick={pickAvatar}
                    disabled={avatarUploading || !flaskToken}
                    className="relative group disabled:opacity-60 disabled:cursor-not-allowed rounded-2xl"
                    title={
                      flaskToken
                        ? "Click to change profile picture"
                        : "Log in again to change profile picture"
                    }
                  >
                    {avatarSrc && avatarOk ? (
                      <Image
                        src={avatarSrc}
                        alt="Profile avatar"
                        width={96}
                        height={96}
                        unoptimized
                        onError={() => setAvatarOk(false)}
                        className="w-24 h-24 sm:w-24 sm:h-24 rounded-2xl border border-[var(--border)] object-cover bg-[var(--background)]"
                      />
                    ) : (
                      <div className="w-20 h-20 sm:w-24 sm:h-24 rounded-2xl border border-[var(--border)] flex items-center justify-center text-[var(--muted)] bg-[var(--background)]">
                        ?
                      </div>
                    )}

                    {/* Hover overlay */}
                    <div className="absolute inset-0 rounded-2xl bg-black/0 group-hover:bg-black/40 transition flex items-center justify-center">
                      <span className="text-xs text-white opacity-0 group-hover:opacity-100 transition">
                        {avatarUploading ? "Uploading…" : "Change"}
                      </span>
                    </div>
                  </button>

                  <div>
                    <p className="text-xs uppercase tracking-wider text-[var(--muted)]">
                      Account {user && user.id ? `#${user.id}` : "--"}
                    </p>
                    <h1 className="text-2xl sm:text-3xl font-semibold text-[var(--foreground)] mt-1">
                      {user?.name || "Unnamed User"}
                    </h1>
                    <p className="text-sm text-[var(--muted)] mt-1">
                      {user?.email || "—"}
                    </p>

<div className="h-12">
                      {(avatarMsg || avatarErr) && (
                      <p
                        className={[
                          "text-xs",
                          avatarErr ? "text-red-600" : "text-[var(--muted)]",
                        ].join(" ")}
                      >
                        {avatarErr ?? avatarMsg}
                      </p>
                    )}
</div>
                  </div>
                </div>
              </div>
            </div>
          </div>

          {/* PURE BLACK SECTION: tabs */}
          <div className="px-5 sm:px-6 pb-5">
            <div className="flex flex-wrap gap-2 justify-center sm:justify-end">
              {tabs.map((t) => (
                <TabPill key={t.key} tabKey={t.key} label={t.label} />
              ))}
            </div>
          </div>
        </div>

        {/* Active panel */}
        <Panel />
      </div>
    </div>
  );
}
