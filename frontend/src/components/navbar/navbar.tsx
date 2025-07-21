"use client";

import React, { useState, useRef, useEffect } from "react";
import Link from "next/link";
import { useSession, signOut, signIn } from "next-auth/react";
import ThemeToggle from "../ThemeToggle";
import { EyeIcon, EyeOffIcon } from "lucide-react";
import Image from "next/image";
import { DEFAULT_USER_ICON } from "@/app/helper";
import { FaDiscord, FaGoogle } from "react-icons/fa";

export default function Navbar() {
  const { status, data: session } = useSession();
  const [dropdownOpen, setDropdownOpen] = useState(false);
  const dropdownRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    const handleClickOutside = (event: MouseEvent) => {
      if (
        dropdownRef.current &&
        !dropdownRef.current.contains(event.target as Node)
      ) {
        setDropdownOpen(false);
      }
    };

    if (dropdownOpen)
      document.addEventListener("mousedown", handleClickOutside);
    return () => document.removeEventListener("mousedown", handleClickOutside);
  }, [dropdownOpen]);

  const handleLogout = async () => {
    setDropdownOpen(false);
    await signOut({ redirect: false });
  };

  return (
    <>
      <nav className="fixed top-0 left-0 w-full bg-[var(--color-background)] text-[var(--color-foreground)] border-b border-[var(--color-border)] shadow-md px-4 sm:px-6 py-3 z-50 transition-colors duration-300">
        <div className="max-w-7xl mx-auto flex items-center justify-between">
          <Link
            href="/"
            className="sm:text-2xl text-lg font-bold transition-transform duration-300 hover:scale-105 min-w-[120px]"
          >
            The Gateway
          </Link>

          <div className="flex items-center space-x-3 sm:space-x-4">
            {status === "authenticated" ? (
              <div className="relative" ref={dropdownRef}>
                <button
                  onClick={() => setDropdownOpen(!dropdownOpen)}
                  className="flex items-center gap-2 px-2 py-1 rounded-md transition-colors"
                >
                  <div className="rounded-full border-2 border-[var(--color-border)] overflow-hidden w-9 h-9">
                    <Image
                      src={session?.user?.image || DEFAULT_USER_ICON}
                      alt="Profile picture"
                      width={36}
                      height={36}
                      className="object-cover w-full h-full"
                    />
                  </div>
                  <div className="hidden sm:inline text-sm font-medium">
                    {session.user?.name}
                  </div>
                </button>

                {dropdownOpen && (
                  <div className="absolute right-0 top-full mt-2 w-40 bg-[var(--color-background)] border border-[var(--color-border)] shadow-lg rounded-lg p-1 z-50">
                    <Link
                      href="/profile"
                      onClick={() => setDropdownOpen(false)}
                    >
                      <p className="px-4 py-2 hover:bg-gray-200 dark:hover:bg-gray-700 rounded-md cursor-pointer transition">
                        Profile
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
              <div className="relative" ref={dropdownRef}>
                <button
                  onClick={() => setDropdownOpen(!dropdownOpen)}
                  className="btn btn-primary px-3 py-2 text-sm sm:text-base"
                >
                  Login
                </button>

                {dropdownOpen && (
                  <LoginDropdown close={() => setDropdownOpen(false)} />
                )}
              </div>
            )}

            <ThemeToggle />
          </div>
        </div>
      </nav>

      <div className="pt-14 sm:pt-16"></div>
    </>
  );
}

interface LoginDropdownProps {
  close: () => void;
}

function LoginDropdown({ close }: LoginDropdownProps) {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [showPassword, setShowPassword] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [loading, setLoading] = useState(false);

  const handleLogin = async (e: React.FormEvent) => {
    e.preventDefault();
    setError(null);
    setLoading(true);

    try {
      const res = await signIn("credentials", {
        email,
        password,
        redirect: false,
      });

      if (res?.error) {
        setError("Invalid email or password.");
      } else {
        close();
      }
    } catch (err: unknown) {
      setError("Login failed. Try again.");
      console.log(err)
    } finally {
      setLoading(false);
    }
  };

  return (
<div
  className="fixed inset-0 backdrop-blur-sm flex items-center justify-center sm:absolute sm:right-4 sm:top-full sm:mt-8 sm:min-w-40 sm:justify-end sm:items-start z-50"
  onClick={close}
>
  <div
    className="bg-[var(--color-background)] border border-[var(--color-border)] shadow-2xl rounded-xl p-6 w-full sm:min-w-80 max-w-md mx-auto"
    onClick={(e) => e.stopPropagation()}
  >
    <h2 className="text-xl font-semibold mb-4 text-center">Welcome Back</h2>

    {error && (
      <p className="text-red-500 mb-4 text-sm text-center">{error}</p>
    )}

    <form onSubmit={handleLogin} className="space-y-4">
      {/* Email */}
      <input
        type="email"
        placeholder="Email"
        className="input w-full"
        value={email}
        onChange={(e) => setEmail(e.target.value)}
        required
      />

      {/* Password */}
      <div className="relative">
        <input
          type={showPassword ? "text" : "password"}
          placeholder="Password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          className="input w-full pr-10"
          required
        />
        <button
          type="button"
          onClick={() => setShowPassword(!showPassword)}
          className="absolute inset-y-0 right-3 flex items-center text-gray-500 hover:text-gray-800 dark:hover:text-gray-300"
        >
          {showPassword ? <EyeOffIcon size={20} /> : <EyeIcon size={20} />}
        </button>
      </div>

      {/* Login Button */}
      <button
        type="submit"
        className="btn btn-primary w-full"
        disabled={loading}
      >
        {loading ? "Logging in..." : "Login"}
      </button>
    </form>

    {/* Divider */}
    <div className="relative my-6">
      <div className="absolute inset-0 flex items-center">
        <div className="w-full border-t border-gray-300 dark:border-gray-700" />
      </div>
      <div className="relative flex justify-center text-xs uppercase">
        <span className="bg-[var(--color-background)] px-2 text-gray-500 dark:text-gray-400">
          or
        </span>
      </div>
    </div>

    {/* Social Login */}
    <div className="flex justify-center gap-4 mb-6">
      <button
        onClick={() => signIn("google")}
        className="btn btn-outline flex items-center gap-2 px-4 py-2 border border-[var(--color-foreground)] sm:border-0"
      >
        <FaGoogle className="text-xl" />
        <span className="hidden sm:inline">Google</span>
      </button>
      <button
        onClick={() => signIn("discord")}
        className="btn btn-outline flex items-center gap-2 px-4 py-2 border border-[var(--color-foreground)] sm:border-0"
      >
        <FaDiscord className="text-xl" />
        <span className="hidden sm:inline">Discord</span>
      </button>
    </div>

    {/* Additional Links */}
    <div className="text-center text-sm text-[var(--color-foreground)] space-y-2">
      <Link
        href="/forgot-password"
        className="text-[var(--color-secondary)] hover:underline"
      >
        Forgot Password?
      </Link>
      <p>
        Don&apos;t have an account?{" "}
        <Link
          href="/signup"
          className="text-[var(--color-secondary)] hover:underline"
          onClick={close}
        >
          Sign Up
        </Link>
      </p>
    </div>
  </div>
</div>

  );
}
