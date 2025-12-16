/* eslint-disable @typescript-eslint/no-explicit-any */
"use client";

import { useSession } from "next-auth/react";
import { useEffect, useMemo, useRef, useState } from "react";
import { useRouter, useSearchParams } from "next/navigation";

const FLASK_API_BASE =
  process.env.NEXT_PUBLIC_FLASK_API_BASE ?? "http://localhost:5000";

function friendlyAuthError(code: string) {
  switch (code) {
    case "AccessDenied":
      return "Access was denied.";
    case "login_required":
      return "Please log in again.";
    default:
      return `Error: ${code}`;
  }
}

function cx(...classes: Array<string | false | null | undefined>) {
  return classes.filter(Boolean).join(" ");
}

const cardBase =
  "rounded-xl border border-[var(--border)] bg-[var(--navbar)] p-5 sm:p-6 shadow-sm";
const title = "text-lg font-semibold text-[var(--foreground)]";
const subtitle = "mt-1 text-sm text-[var(--muted)]";
const label = "text-xs font-medium text-[var(--muted)]";
const divider = "h-px w-full bg-[var(--border)]";

const btnBase =
  "inline-flex items-center justify-center rounded-lg px-4 py-2.5 text-sm font-medium transition disabled:opacity-50 disabled:cursor-not-allowed";
const btnPrimary =
  "bg-[var(--primary)] text-white hover:bg-[var(--secondary)]";

export default function TabSettings() {
  const { data: session, update } = useSession();
  const router = useRouter();
  const params = useSearchParams();

  const flaskToken = (session as any)?.accessToken as string | null;

  const hasCredentials = useMemo(() => {
    const linked = ((session as any)?.linked_accounts ?? []) as string[];
    return linked.map((p) => p.toLowerCase()).includes("credentials");
  }, [session]);

  /* ---------------- Username ---------------- */
  const [username, setUsername] = useState(session?.user?.name ?? "");
  const [usernameSaving, setUsernameSaving] = useState(false);

  /* ---------------- Password ---------------- */
  const [currentPassword, setCurrentPassword] = useState("");
  const [newPassword, setNewPassword] = useState("");
  const [confirmPassword, setConfirmPassword] = useState("");
  const [passwordSaving, setPasswordSaving] = useState(false);

  /* ---------------- Feedback ---------------- */
  const [msg, setMsg] = useState<string | null>(null);
  const [err, setErr] = useState<string | null>(null);

  const didInit = useRef(false);

  useEffect(() => {
    if (didInit.current) return;
    didInit.current = true;

    const error = params.get("error");
    if (!error) return;

    setErr(friendlyAuthError(error));

    const sp = new URLSearchParams(params.toString());
    sp.delete("error");
    router.replace(`/user?${sp.toString()}`);
  }, [params, router]);

  /* ---------------- Username Save ---------------- */
  async function saveUsername() {
    setErr(null);
    setMsg(null);

    const next = username.trim();
    if (!flaskToken) return setErr("Session expired. Please log in again.");
    if (!next) return setErr("Username cannot be empty.");

    setUsernameSaving(true);
    try {
      const res = await fetch(`${FLASK_API_BASE}/auth/set-username`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          Authorization: `Bearer ${flaskToken}`,
        },
        body: JSON.stringify({ username: next }),
      });

      const data = await res.json().catch(() => ({}));
      if (!res.ok) throw new Error(data.error || "Failed to update username");

      await update({
        image: data.image,
        picture: data.image, // keep both because some callbacks map picture->image
        name: username,
        email: data.email,
        linked_accounts: data.linked_accounts,
        accessToken: data.accessToken, // if your backend rotates tokens; harmless if same
      });
      setMsg("Username updated.");
    } catch (e: any) {
      setErr(e?.message || "Failed to update username.");
    } finally {
      setUsernameSaving(false);
    }
  }

  /* ---------------- Password Save ---------------- */
  async function savePassword() {
    setErr(null);
    setMsg(null);

    if (!flaskToken) return setErr("Session expired. Please log in again.");
    if (newPassword.length < 8)
      return setErr("Password must be at least 8 characters.");
    if (newPassword !== confirmPassword) return setErr("Passwords do not match.");
    if (hasCredentials && !currentPassword)
      return setErr("Current password is required.");

    setPasswordSaving(true);
    try {
      const res = await fetch(`${FLASK_API_BASE}/auth/set-password`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          Authorization: `Bearer ${flaskToken}`,
        },
        body: JSON.stringify({
          current_password: hasCredentials ? currentPassword : undefined,
          new_password: newPassword,
        }),
      });

      const data = await res.json().catch(() => ({}));
      if (!res.ok) throw new Error(data.error || "Failed to update password");

      setCurrentPassword("");
      setNewPassword("");
      setConfirmPassword("");

      await update({
        accessToken: data.accessToken,
        linked_accounts: data.linked_accounts,
      });

      setMsg(hasCredentials ? "Password updated." : "Password set.");
    } catch (e: any) {
      setErr(e?.message || "Failed to update password.");
    } finally {
      setPasswordSaving(false);
    }
  }

  /* ---------------- UI ---------------- */
  return (
    <div className="space-y-6">
      <header className="space-y-1">
        <p className="text-xs uppercase tracking-wider text-[var(--muted)]">
          Preferences
        </p>
        <h2 className="text-2xl font-semibold text-[var(--foreground)]">
          Account Settings
        </h2>
        <p className="text-sm text-[var(--muted)]">
          Manage your username and password.
        </p>
      </header>
      <div className={divider} />

      {msg && (
        <div className="rounded-xl border border-[var(--border)] bg-[var(--navbar)] p-4 text-sm text-[var(--foreground)] shadow-sm">
          {msg}
        </div>
      )}

      {err && (
        <div className="rounded-xl border border-red-500/40 bg-red-500/10 p-4 text-sm text-red-600">
          {err}
        </div>
      )}


      {/* Username */}
      <section className={cx(cardBase, "space-y-4 bg-[var(--foreground)")}>
        <div>
          <h3 className={title}>Username</h3>
          <p className={subtitle}>This name is shown publicly.</p>
        </div>

        <div className="grid grid-cols-1 gap-3 sm:grid-cols-[1fr_auto] sm:items-end">
          <div>
            <label className={label} htmlFor="username">
              Username
            </label>
            <input
              id="username"
              type="text"
              value={username}
              onChange={(e) => setUsername(e.target.value)}
              className="mt-1"
            />
          </div>

          <button
            onClick={saveUsername}
            disabled={usernameSaving || !username.trim()}
            className={cx(btnBase, btnPrimary, "sm:min-w-[120px]")}
          >
            {usernameSaving ? "Saving..." : "Save"}
          </button>
        </div>
      </section>

      {/* Password */}
      <section className={cx(cardBase, "space-y-4")}>
        <div>
          <h3 className={title}>{hasCredentials ? "Change password" : "Set a password"}</h3>
          <p className={subtitle}>
            {hasCredentials ? "Update your existing password." : "Add a password to your account."}
          </p>
        </div>

        {hasCredentials && (
          <div>
            <label className={label} htmlFor="currentPassword">
              Current password
            </label>
            <input
              id="currentPassword"
              type="password"
              value={currentPassword}
              onChange={(e) => setCurrentPassword(e.target.value)}
              className="mt-1"
            />
          </div>
        )}

        <div className="grid grid-cols-1 gap-3 sm:grid-cols-2">
          <div>
            <label className={label} htmlFor="newPassword">
              New password
            </label>
            <input
              id="newPassword"
              type="password"
              value={newPassword}
              onChange={(e) => setNewPassword(e.target.value)}
              className="mt-1"
            />
          </div>

          <div>
            <label className={label} htmlFor="confirmPassword">
              Confirm new password
            </label>
            <input
              id="confirmPassword"
              type="password"
              value={confirmPassword}
              onChange={(e) => setConfirmPassword(e.target.value)}
              className="mt-1"
            />
          </div>
        </div>

        <div className="flex flex-col-reverse gap-3 sm:flex-row sm:items-center sm:justify-between">
          <p className="text-xs text-[var(--muted)]">
            Minimum 8 characters recommended.
          </p>

          <button
            onClick={savePassword}
            disabled={
              passwordSaving ||
              !newPassword ||
              !confirmPassword ||
              (hasCredentials && !currentPassword)
            }
            className={cx(btnBase, btnPrimary)}
          >
            {passwordSaving
              ? "Saving..."
              : hasCredentials
              ? "Update password"
              : "Set password"}
          </button>
        </div>
      </section>
    </div>
  );
}
