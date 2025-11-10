"use client";

import React, { useEffect, useRef, useState } from "react";
import NavProfile from "./NavProfile";
import { FaMoon, FaSun, FaBars, FaTimes } from "react-icons/fa";
import Login from "./Login";
import Signup from "./Signup";
import { useSession } from "next-auth/react";
import { useRouter } from "next/navigation";
import { useTheme } from "@/app/theme-provider";

export default function Navbar() {
  const { data: session, status, update } = useSession();
  const { theme, toggleTheme } = useTheme();
  const [drawerOpen, setDrawerOpen] = useState(false);
  const router = useRouter();

  // Refresh session once on mount to avoid stale client cache
  useEffect(() => {
    if (status === "loading") update();
  }, [status, update]);

  const isLoading = status === "loading";
  const isAuthenticated = status === "authenticated";

  return (
    <nav
      className="navbar sticky top-0 h-16 flex items-center justify-between 
                 px-4 sm:px-6 border-b border-[var(--border)] 
                 bg-[var(--navbar)] z-50"
    >
      {/* Logo */}
      <h1
        className="font-bold text-lg sm:text-xl cursor-pointer text-[var(--foreground)]"
        onClick={() => router.push("/")}
      >
        The Gateway
      </h1>

      {/* Center links placeholder */}
      <div className="hidden sm:flex gap-4 items-center" />

      {/* Right side */}
      <div className="flex items-center gap-3">
        {/* Theme toggle */}
        <button
          onClick={toggleTheme}
          className="!p-3 !rounded-full bg-[var(--background)] text-[var(--foreground)] border border-[var(--border)] hover:bg-[var(--primary)] hover:text-white transition"
          aria-label="Toggle Theme"
        >
          {theme === "light" ? <FaMoon /> : <FaSun />}
        </button>

        {/* Desktop auth area */}
        <div className="hidden sm:block">
          {isLoading ? (
            <div className="animate-pulse w-9 h-9 rounded-full bg-[var(--border)]" />
          ) : isAuthenticated ? (
            <NavProfile />
          ) : (
            <LoginComponent />
          )}
        </div>

        {/* Mobile drawer toggle */}
        <button
          className="sm:hidden p-2 rounded-md text-[var(--foreground)] border border-[var(--border)]"
          onClick={() => setDrawerOpen(true)}
          aria-label="Open menu"
        >
          <FaBars />
        </button>
      </div>

      {/* --- Mobile Drawer --- */}
      <>
        {/* Backdrop */}
        <div
          className={`fixed inset-0 bg-black/50 z-40 transition-opacity duration-300 ${
            drawerOpen ? "opacity-100" : "opacity-0 pointer-events-none"
          }`}
          onClick={() => setDrawerOpen(false)}
        />

        {/* Drawer */}
        <div
          className={`fixed top-0 right-0 h-full w-full max-w-sm bg-[var(--navbar)] border-l border-[var(--border)] z-50 p-6 flex flex-col gap-6 transform transition-transform duration-300 ${
            drawerOpen ? "translate-x-0" : "translate-x-full"
          }`}
        >
          {/* Close */}
          <button
            className="self-end p-2 text-[var(--foreground)]"
            onClick={() => setDrawerOpen(false)}
            aria-label="Close menu"
          >
            <FaTimes size={20} />
          </button>

          {/* Drawer content */}
          {isLoading ? (
            <div className="animate-pulse w-9 h-9 rounded-full bg-[var(--border)]" />
          ) : isAuthenticated ? (
            <NavProfile />
          ) : (
            <LoginComponent mobile />
          )}
        </div>
      </>
    </nav>
  );
}

/* --- Login / Signup dropdown/modal --- */
function LoginComponent({ mobile = false }: { mobile?: boolean }) {
  const [isOpen, setIsOpen] = useState(false);
  const [activeTab, setActiveTab] = useState<"login" | "signup">("login");
  const wrapperRef = useRef<HTMLDivElement>(null);

  // Close dropdown on outside click
  useEffect(() => {
    function handleClickOutside(event: MouseEvent) {
      if (wrapperRef.current && !wrapperRef.current.contains(event.target as Node)) {
        setIsOpen(false);
      }
    }
    document.addEventListener("mousedown", handleClickOutside);
    return () => document.removeEventListener("mousedown", handleClickOutside);
  }, []);

  // --- Mobile version ---
  if (mobile) {
    return (
      <>
        <button
          onClick={() => setIsOpen(true)}
          className="w-full px-4 py-2 rounded-md border border-[var(--border)] bg-[var(--background)] text-[var(--foreground)] hover:bg-[var(--primary)] hover:text-white transition"
        >
          Login / Signup
        </button>

        {/* Backdrop */}
        <div
          className={`fixed inset-0 bg-black/50 z-40 transition-opacity duration-300 ${
            isOpen ? "opacity-100" : "opacity-0 pointer-events-none"
          }`}
          onClick={() => setIsOpen(false)}
        />

        {/* Modal */}
        <div
          className={`fixed top-0 left-0 w-full max-h-[90%] bg-[var(--navbar)] border-b border-[var(--border)] shadow-xl z-50 transform transition-transform duration-300 ${
            isOpen ? "translate-y-0" : "-translate-y-full"
          }`}
        >
          {/* Tabs */}
          <div className="flex justify-between items-center p-4 border-b border-[var(--border)]">
            <div className="flex gap-4">
              {["login", "signup"].map((tab) => (
                <button
                  key={tab}
                  className={`pb-2 transition-colors ${
                    activeTab === tab
                      ? "border-b-2 border-[var(--primary)] font-semibold"
                      : "text-[var(--muted)]"
                  }`}
                  onClick={() => setActiveTab(tab as "login" | "signup")}
                >
                  {tab === "login" ? "Login" : "Sign Up"}
                </button>
              ))}
            </div>
            <button
              onClick={() => setIsOpen(false)}
              className="text-[var(--muted)]"
              aria-label="Close modal"
            >
              <FaTimes />
            </button>
          </div>

          {/* Content */}
          <div className="p-4 overflow-y-auto max-h-[70vh]">
            {activeTab === "login" ? <Login /> : <Signup />}
          </div>
        </div>
      </>
    );
  }

  // --- Desktop dropdown ---
  return (
    <div className="relative" ref={wrapperRef}>
      <button
        onClick={() => setIsOpen(!isOpen)}
        className="navbar_login bg-[var(--navbar)] text-[var(--foreground)]"
      >
        Login / Signup
      </button>

      <div
        className={`absolute right-0 border border-[var(--border)] w-80 sm:w-96 rounded-2xl p-5 bg-[var(--navbar)] mt-2 shadow-xl text-[var(--foreground)] transform transition-all duration-300 origin-top ${
          isOpen
            ? "opacity-100 scale-100 translate-y-0"
            : "opacity-0 scale-95 -translate-y-2 pointer-events-none"
        }`}
      >
        <div className="flex gap-4 mb-4 border-b border-[var(--border)]">
          {["login", "signup"].map((tab) => (
            <button
              key={tab}
              className={`pb-2 transition-colors ${
                activeTab === tab
                  ? "border-b-2 border-[var(--primary)] font-semibold"
                  : "text-[var(--muted)]"
              }`}
              onClick={() => setActiveTab(tab as "login" | "signup")}
            >
              {tab === "login" ? "Login" : "Sign Up"}
            </button>
          ))}
        </div>

        {/* Content */}
        <div className="relative min-h-[280px] overflow-hidden">
          {activeTab === "login" ? <Login /> : <Signup />}
        </div>
      </div>
    </div>
  );
}
