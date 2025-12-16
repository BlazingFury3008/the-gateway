"use client";

import React, { useState, useRef, useEffect } from "react";
import { useSession, signOut } from "next-auth/react";
import { useRouter } from "next/navigation";
import { FaUser, FaSignOutAlt } from "react-icons/fa";
import Navbar from "./Navbar";

export default function NavProfile({onNavigate}) {
  const { data: session, update } = useSession();
  const router = useRouter();
  const [open, setOpen] = useState(false);
  const ref = useRef<HTMLDivElement>(null);

  const user = session?.user;
  if (!user) return null;

  // Close dropdown when clicking outside (desktop only)
  useEffect(() => {
    const handleClickOutside = (e: MouseEvent) => {
      if (ref.current && !ref.current.contains(e.target as Node))
        setOpen(false);
    };
    document.addEventListener("mousedown", handleClickOutside);
    return () => document.removeEventListener("mousedown", handleClickOutside);
  }, []);

  // Close dropdown on resize
  useEffect(() => {
    const onResize = () => setOpen(false);
    window.addEventListener("resize", onResize);
    return () => window.removeEventListener("resize", onResize);
  }, []);

  const handleProfileClick = () => {
    // If on mobile, go straight to /user (no dropdown)
    if (window.matchMedia("(max-width: 639px)").matches) {
      router.push("/user");
      onNavigate();
      return;
    }
    // Desktop: toggle dropdown
    setOpen((v) => !v);
  };

  return (
    <div ref={ref} className="relative">
      {/* Profile button */}
      <button
        type="button"
        onClick={handleProfileClick}
        className="w-full flex items-center gap-3 px-3 py-1 rounded-md border border-[var(--border)] bg-[var(--background)] text-[var(--foreground)] hover:bg-[var(--navbar)] transition-all navbar-button"
      >
        {user.image ? (
          // eslint-disable-next-line @next/next/no-img-element
          <img
            src={user.image}
            alt="User avatar"
            className="w-9 h-9 rounded-full border border-[var(--border)] object-cover shrink-0"
          />
        ) : (
          <div className="w-9 h-9 rounded-full flex items-center justify-center bg-[var(--primary)] text-white font-semibold shrink-0">
            {user.name ? user.name[0].toUpperCase() : "U"}
          </div>
        )}

        <span className="min-w-0 flex-1 font-medium truncate">
          {user.name || "User"}
        </span>
      </button>

      {/* MOBILE: Sign out button below (only visible on mobile) */}
      <button
        type="button"
        onClick={async () => {
          await signOut({ redirect: false });
          await update();
        }}
        className="mt-2 w-full sm:hidden flex items-center justify-center gap-2 px-3 py-2 rounded-md border border-[var(--border)]
                   bg-[var(--background)] text-red-500 hover:bg-[var(--navbar)] transition"
      >
        <FaSignOutAlt />
        <span>Sign Out</span>
      </button>

      {/* DESKTOP: Dropdown (hidden on mobile) */}
      <div
        className={`hidden sm:block absolute right-0 mt-2 w-56 rounded-xl bg-[var(--navbar)] border border-[var(--border)] shadow-lg overflow-hidden transition-all duration-200 z-50 ${
          open
            ? "opacity-100 scale-100 translate-y-0 pointer-events-auto"
            : "opacity-0 scale-95 -translate-y-2 pointer-events-none"
        }`}
      >
        <div className="p-3 border-b border-[var(--border)]">
          <p className="font-semibold text-[var(--foreground)] truncate">
            {user.name || "User"}
          </p>
          <p className="text-sm text-[var(--muted)] truncate">{user.email}</p>
        </div>

        <button
          type="button"
          onClick={() => {
            router.push("/user");
            setOpen(false);
          }}
          className="w-full flex items-center gap-2 px-4 py-3 text-left text-[var(--foreground)] hover:bg-[var(--background)] transition"
        >
          <FaUser />
          <span>Profile</span>
        </button>

        <button
          type="button"
          onClick={async () => {
            setOpen(false);
            await signOut({ redirect: false });
            await update();
          }}
          className="w-full flex items-center gap-2 px-4 py-3 text-left text-red-500 hover:bg-[var(--background)] transition"
        >
          <FaSignOutAlt />
          <span>Sign Out</span>
        </button>
      </div>
    </div>
  );
}
