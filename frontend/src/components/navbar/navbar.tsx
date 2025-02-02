"use client";

import React, { useState } from "react";
import Link from "next/link";
import { useSession, signOut } from "next-auth/react";
import { useRouter } from "next/navigation";

const DEFAULT_AVATAR = "https://cdn-icons-png.flaticon.com/512/847/847969.png";

export default function Navbar() {
  const { data: session, status } = useSession();
  const [dropdownOpen, setDropdownOpen] = useState(false);
  const router = useRouter();

  const handleLogout = async () => {
    await signOut({ redirect: false });

    router.replace("/")
   
  };

  return (
    <>
      <nav className="fixed top-0 left-0 w-full bg-gray-900 backdrop-blur-lg border-b border-white text-white shadow-md px-6 py-4 z-50">
        <div className="max-w-7xl mx-auto flex items-center justify-between">
          <Link href="/" className="text-2xl font-bold">
            The Gateway
          </Link>

          <div>
            {status === "loading" ? (
              <div className="w-24 h-10 bg-gray-700 animate-pulse rounded-lg"></div>
            ) : session?.user ? (
              <div className="relative">
                <button
                  onClick={() => setDropdownOpen(!dropdownOpen)}
                  className="flex items-center space-x-2 focus:outline-none"
                >
                  <img
                    src={session.user.image || DEFAULT_AVATAR}
                    alt="User Avatar"
                    className="w-10 h-10 rounded-full border border-gray-400"
                  />
                  <span className="text-sm font-medium">{session.user.name || "User"}</span>
                </button>

                {dropdownOpen && (
                  <div className="absolute right-0 top-full mt-2 w-48 bg-slate-800 rounded-lg shadow-lg p-2 z-50 border border-gray-700">
                    <p className="px-4 py-2 text-sm text-gray-300">{session.user.name}</p>
                    <Link href="/profile">
                      <p className="px-4 py-2 hover:bg-slate-700 rounded-md cursor-pointer">
                        Edit Profile
                      </p>
                    </Link>
                    <button
                      className="w-full text-left px-4 py-2 hover:bg-slate-700 rounded-md cursor-pointer"
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
                  <button className="px-4 py-2 border border-white rounded-md hover:bg-white hover:text-black transition">
                    Log In
                  </button>
                </Link>
              </div>
            )}
          </div>
        </div>
      </nav>

      <div className="pt-16"></div>
    </>
  );
}
