"use client";

import React, { useState } from "react";
import Link from "next/link";
import { useSession, signOut } from "next-auth/react";
import { useRouter } from "next/navigation";
import ThemeToggle from "../ThemeToggle";
import Image from "next/image";

const DEFAULT_AVATAR = "https://cdn-icons-png.flaticon.com/512/847/847969.png";

export default function Navbar() {
  const { data: session, status } = useSession();
  const [dropdownOpen, setDropdownOpen] = useState(false);
  const router = useRouter();

  const handleLogout = async () => {
    await signOut({ redirect: false });
    router.replace("/");
  };

  return (
    <>
      <nav className="fixed top-0 left-0 w-full bg-[var(--color-background)] text-[var(--color-foreground)] border-b border-[var(--color-border)] shadow-md px-6 py-4 z-50 transition-colors duration-300">
        <div className="max-w-7xl mx-auto flex items-center justify-between">
          {/* Logo with Animation */}
          <Link
            href="/"
            className="text-2xl font-bold transition-transform duration-300 hover:scale-105"
          >
            The Gateway
          </Link>

          <div className="flex space-x-6 items-center">
            {status === "loading" ? (
              <div className="w-24 h-10 bg-gray-300 dark:bg-gray-700 animate-pulse rounded-lg"></div>
            ) : session?.user ? (
              <div className="relative">
                {/* User Button */}
                <button
                  onClick={() => setDropdownOpen(!dropdownOpen)}
                  className="flex items-center space-x-2 focus:outline-none"
                >
                  <Image
                    src={session.user.image || DEFAULT_AVATAR}
                    alt="User Avatar"
                    className="w-10 h-10 rounded-full border border-gray-400 dark:border-gray-600"
                    width={40}
                    height={40}
                  />
                  <span className="text-sm font-medium">
                    {session.user.name || "User"}
                  </span>
                </button>

                {/* Dropdown Menu */}
                {dropdownOpen && (
                  <div className="absolute right-0 top-full mt-2 w-48 bg-[var(--color-background)] border border-[var(--color-border)] shadow-lg rounded-lg p-2 z-50 transition-opacity duration-300">
                    <p className="px-4 py-2 text-sm text-[var(--color-foreground)]">
                      {session.user.name}
                    </p>
                    <Link
                      href="/profile"
                      onClick={() => setDropdownOpen(false)}
                    >
                      <p className="px-4 py-2 hover:bg-gray-200 dark:hover:bg-gray-700 rounded-md cursor-pointer transition">
                        Edit Profile
                      </p>
                    </Link>

                    <button
                      className="w-full text-left px-4 py-2 hover:bg-gray-200 dark:hover:bg-gray-700 rounded-md cursor-pointer transition"
                      onClick={handleLogout}
                    >
                      Logout
                    </button>
                  </div>
                )}
              </div>
            ) : (
              <div className="flex space-x-4">
                <Link href="/login">
                  <button className="px-4 py-2 border border-[var(--color-foreground)] rounded-md hover:bg-[var(--color-foreground)] hover:text-[var(--color-background)] transition">
                    Log In
                  </button>
                </Link>
              </div>
            )}

            {/* Theme Toggle Button */}
            <ThemeToggle />
          </div>
        </div>
      </nav>

      {/* Offset to prevent content overlap */}
      <div className="pt-16"></div>
    </>
  );
}
