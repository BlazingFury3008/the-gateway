"use client";

import React, { useState, useRef, useEffect } from "react";
import { useSession, signOut } from "next-auth/react";
import { useRouter } from "next/navigation";
import { FaUser, FaSignOutAlt } from "react-icons/fa";

export default function NavProfile() {
  const { data: session, update } = useSession();
  const router = useRouter();
  const [open, setOpen] = useState(false);
  const ref = useRef<HTMLDivElement>(null);

  const user = session?.user;

  // Close dropdown when clicking outside
  useEffect(() => {
    const handleClickOutside = (e: MouseEvent) => {
      if (ref.current && !ref.current.contains(e.target as Node)) {
        setOpen(false);
      }
    };
    document.addEventListener("mousedown", handleClickOutside);
    return () => document.removeEventListener("mousedown", handleClickOutside);
  }, []);

  if (!user) return null;

  return (
    <div ref={ref} className="relative">
      {/* Profile button */}
      <button
        onClick={() => setOpen(!open)}
        className="flex items-center gap-2 !px-2 py-1 rounded-md border border-[var(--border)] bg-[var(--background)] text-[var(--foreground)] hover:bg-[var(--navbar)] transition-all navbar-button"
      >
        {user.image ? (
          <img
            src={user.image}
            alt="User avatar"
            className="w-8 h-8 rounded-full border border-[var(--border)] object-cover"
          />
        ) : (
          <div className="w-8 h-8 rounded-full flex items-center justify-center bg-[var(--primary)] text-white font-semibold">
            {user.name ? user.name[0].toUpperCase() : "U"}
          </div>
        )}
        <span className="hidden sm:inline font-medium">{user.name || "User"}</span>
      </button>

      {/* Dropdown */}
      <div
        className={`absolute right-0 mt-2 w-56 rounded-xl bg-[var(--navbar)] border border-[var(--border)] shadow-lg overflow-hidden transition-all duration-300 ${
          open
            ? "opacity-100 scale-100 translate-y-0"
            : "opacity-0 scale-95 -translate-y-2 pointer-events-none"
        }`}
      >
        <div className="p-3 border-b border-[var(--border)]">
          <p className="font-semibold text-[var(--foreground)]">
            {user.name || "User"}
          </p>
          <p className="text-sm text-[var(--muted)] truncate">{user.email}</p>
        </div>

        <button
          onClick={() => {
            router.push("/user");
            setOpen(false);
          }}
          className="w-full flex items-center gap-2 px-4 py-2 text-left text-[var(--foreground)] hover:bg-[var(--background)] transition"
        >
          <FaUser />
          <span>Profile</span>
        </button>

        <button
          onClick={async () => {
            setOpen(false);
            await signOut({ redirect: false }); // ← instant sign-out, no page change
            await update(); // refresh session so UI updates immediately
          }}
          className="w-full flex items-center gap-2 px-4 py-2 text-left text-red-500 hover:bg-[var(--background)] transition"
        >
          <FaSignOutAlt />
          <span>Sign Out</span>
        </button>
      </div>
    </div>
  );
}
