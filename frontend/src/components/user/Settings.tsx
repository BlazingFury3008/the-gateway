/* eslint-disable @typescript-eslint/no-explicit-any */
"use client";

import { useSession } from "next-auth/react";
import { useMemo, useRef, useState, useEffect } from "react";
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

export default function TabSettings() {
  const { data: session, update, status } = useSession();
  const router = useRouter();
  const params = useSearchParams();

  const flaskToken = (session as any)?.accessToken as string | null;

  const hasCredentials = useMemo(() => {
    const linked = ((session as any)?.linked_accounts ?? []) as string[];
    console.log("linked accounts:", linked);
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
    if (error) setErr(friendlyAuthError(error));

    if (error) {
      const sp = new URLSearchParams(params.toString());
      sp.delete("error");
      router.replace(`/user?${sp.toString()}`);
    }
  }, [params, router]);

  /* ---------------- Username Save ---------------- */

  async function saveUsername() {
    setErr(null);
    setMsg(null);

    if (!flaskToken) {
      setErr("Session expired. Please log in again.");
      return;
    }

    if (!username.trim()) {
      setErr("Username cannot be empty.");
      return;
    }

    setUsernameSaving(true);
    try {
      const res = await fetch(`${FLASK_API_BASE}/auth/set-username`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          Authorization: `Bearer ${flaskToken}`,
        },
        body: JSON.stringify({ username }),
      });

      const data = await res.json().catch(() => ({}));
      if (!res.ok) throw new Error(data.error || "Failed to update username");

      await update({
        name: data.name,
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

    if (!flaskToken) {
      setErr("Session expired. Please log in again.");
      return;
    }

    if (newPassword.length < 8) {
      setErr("Password must be at least 8 characters.");
      return;
    }

    if (newPassword !== confirmPassword) {
      setErr("Passwords do not match.");
      return;
    }

    if (hasCredentials && !currentPassword) {
      setErr("Current password is required.");
      return;
    }

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
      <div>
        <p className="text-xs uppercase tracking-wider text-[var(--muted)]">
          Preferences
        </p>
        <h2 className="text-xl font-semibold text-[var(--foreground)] mt-1">
          Account Settings
        </h2>
        <p className="mt-1 text-sm text-[var(--muted)]">
          Manage your username and password.
        </p>
      </div>

      {msg && (
        <div className="rounded-xl border border-[var(--border)] bg-[var(--background)]/60 backdrop-blur-sm p-4 text-sm">
          {msg}
        </div>
      )}

      {err && (
        <div className="rounded-xl border border-red-500/40 bg-red-500/10 p-4 text-sm text-red-600">
          {err}
        </div>
      )}
      <div className="h-px w-full bg-[var(--border)] my-4" />

      {/* Username */}
      <section className="rounded-2xl border border-[var(--border)] bg-[var(--background)]/60 backdrop-blur-sm p-3 space-y-2">
        <div>
          <h3 className="text-base font-semibold text-[var(--foreground)]">
            Username
          </h3>
          <p className="text-sm text-[var(--muted)] mt-1">
            This name is shown publicly.
          </p>
        </div>

        <div className="flex items-end gap-3">
          {/* Input */}
          <div className="flex-1">
            <label className="text-xs text-[var(--muted)]">Username</label>
            <input
              type="text"
              value={username}
              onChange={(e) => setUsername(e.target.value)}
              className="h-[50px] w-full rounded-lg border border-[var(--border)] bg-[var(--background)] px-3 py-2.5 text-[var(--foreground)] outline-none focus:ring-2 focus:ring-[var(--primary)]/30"
            />
          </div>

          {/* Button */}
          <button
            onClick={saveUsername}
            disabled={usernameSaving || !username.trim()}
            className="h-[50px] rounded-lg bg-[var(--primary)] px-4 text-sm text-[var(--primary-foreground)] disabled:opacity-50"
          >
            {usernameSaving ? "Saving..." : "Save"}
          </button>
        </div>
      </section>

      {/* Password */}
      <section className="rounded-2xl border border-[var(--border)] bg-[var(--background)]/60 backdrop-blur-sm p-5 sm:p-6 space-y-4">
        <div>
          <h3 className="text-base font-semibold text-[var(--foreground)]">
            {hasCredentials ? "Change password" : "Set a password"}
          </h3>
          <p className="text-sm text-[var(--muted)] mt-1">
            {hasCredentials
              ? "Update your existing password."
              : "Add a password to your account."}
          </p>
        </div>

        {hasCredentials && (
          <div>
            <label className="text-xs text-[var(--muted)]">
              Current password
            </label>
            <input
              type="password"
              value={currentPassword}
              onChange={(e) => setCurrentPassword(e.target.value)}
              className="mt-1 w-full rounded-lg border border-[var(--border)] bg-[var(--background)] px-3 py-2.5"
            />
          </div>
        )}

        <div className="grid grid-cols-1 sm:grid-cols-2 gap-3">
          <div>
            <label className="text-xs text-[var(--muted)]">New password</label>
            <input
              type="password"
              value={newPassword}
              onChange={(e) => setNewPassword(e.target.value)}
              className="mt-1 w-full rounded-lg border border-[var(--border)] bg-[var(--background)] px-3 py-2.5"
            />
          </div>

          <div>
            <label className="text-xs text-[var(--muted)]">
              Confirm new password
            </label>
            <input
              type="password"
              value={confirmPassword}
              onChange={(e) => setConfirmPassword(e.target.value)}
              className="mt-1 w-full rounded-lg border border-[var(--border)] bg-[var(--background)] px-3 py-2.5"
            />
          </div>
        </div>

        <div className="flex justify-between items-center gap-3">
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
            className="rounded-lg bg-[var(--primary)] px-4 py-2.5 text-sm text-[var(--primary-foreground)] disabled:opacity-50"
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
