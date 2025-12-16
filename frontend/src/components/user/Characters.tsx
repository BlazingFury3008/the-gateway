import React from "react";
import Divider from "../components/Divider";

export default function Characters() {
  return (
    <>
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
          disabled={true}
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
    </>
  );
}
