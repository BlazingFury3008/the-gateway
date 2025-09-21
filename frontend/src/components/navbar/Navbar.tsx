"use client";
import React, { useEffect, useRef, useState } from "react";
import NavProfile from "./NavProfile";
import { FaMoon, FaSun, FaBars, FaTimes } from "react-icons/fa";
import Login from "./Login";
import Signup from "./Signup";
import { useSession } from "next-auth/react";
import { useRouter } from "next/navigation";

export default function Navbar() {
  const { data: session, status } = useSession();
  const [theme, setTheme] = useState<"light" | "dark" | null>(null);
  const [drawerOpen, setDrawerOpen] = useState(false);
  const router = useRouter();

  // Load theme from localStorage
  useEffect(() => {
    const savedTheme = localStorage.getItem("theme") as "light" | "dark" | null;
    if (savedTheme) {
      setTheme(savedTheme);
      document.documentElement.setAttribute("data-theme", savedTheme);
    } else {
      const prefersDark = window.matchMedia("(prefers-color-scheme: dark)").matches;
      const initialTheme = prefersDark ? "dark" : "light";
      setTheme(initialTheme);
      document.documentElement.setAttribute("data-theme", initialTheme);
    }
  }, []);

  // Apply theme changes
  useEffect(() => {
    if (theme) {
      document.documentElement.setAttribute("data-theme", theme);
      localStorage.setItem("theme", theme);
    }
  }, [theme]);

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

      {/* Desktop nav (placeholder for future links) */}
      <div className="hidden sm:flex gap-4 items-center" />

      {/* Right side */}
      <div className="flex items-center gap-3">
        {/* Theme toggle */}
        {theme && (
          <button
            onClick={() => setTheme(theme === "light" ? "dark" : "light")}
            className="!p-2 !rounded-full bg-[var(--background)] text-[var(--foreground)] border border-[var(--border)] hover:bg-[var(--primary)] hover:text-white transition"
          >
            {theme === "light" ? <FaMoon /> : <FaSun />}
          </button>
        )}

        {/* Desktop login/profile */}
        <div className="hidden sm:block">
          {status === "authenticated" ? <NavProfile /> : <LoginComponent />}
        </div>

        {/* Mobile drawer toggle */}
        <button
          className="sm:hidden p-2 rounded-md text-[var(--foreground)] border border-[var(--border)]"
          onClick={() => setDrawerOpen(true)}
        >
          <FaBars />
        </button>
      </div>

      {/* Mobile drawer */}
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
          >
            <FaTimes size={20} />
          </button>

          {/* Drawer content */}
          {status === "authenticated" ? (
            <NavProfile />
          ) : (
            <LoginComponent mobile />
          )}
        </div>
      </>
    </nav>
  );
}

/* --- Login Component --- */
function LoginComponent({ mobile = false }: { mobile?: boolean }) {
  const [isOpen, setIsOpen] = useState(false);
  const [activeTab, setActiveTab] = useState<"login" | "signup">("login");

  if (mobile) {
    return (
      <>
        {/* Trigger button inside drawer */}
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

        {/* Full-width top sheet */}
        <div
          className={`fixed top-0 left-0 w-full max-h-[90%] bg-[var(--navbar)] border-b border-[var(--border)] shadow-xl z-50 transform transition-transform duration-300 ${
            isOpen ? "translate-y-0" : "-translate-y-full"
          }`}
        >
          {/* Header */}
          <div className="flex justify-between items-center p-4 border-b border-[var(--border)]">
            <div className="flex gap-4">
              <button
                className={`pb-2 transition-colors ${
                  activeTab === "login"
                    ? "border-b-2 border-[var(--primary)] font-semibold"
                    : "text-[var(--muted)]"
                }`}
                onClick={() => setActiveTab("login")}
              >
                Login
              </button>
              <button
                className={`pb-2 transition-colors ${
                  activeTab === "signup"
                    ? "border-b-2 border-[var(--primary)] font-semibold"
                    : "text-[var(--muted)]"
                }`}
                onClick={() => setActiveTab("signup")}
              >
                Sign Up
              </button>
            </div>
            <button onClick={() => setIsOpen(false)} className="text-[var(--muted)]">
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

  /* --- Desktop dropdown version --- */
  const wrapperRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    function handleClickOutside(event: MouseEvent) {
      if (wrapperRef.current && !wrapperRef.current.contains(event.target as Node)) {
        setIsOpen(false);
      }
    }
    if (isOpen) {
      document.addEventListener("mousedown", handleClickOutside);
    } else {
      document.removeEventListener("mousedown", handleClickOutside);
    }
    return () => {
      document.removeEventListener("mousedown", handleClickOutside);
    };
  }, [isOpen]);

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
        {/* Tabs */}
        <div className="flex gap-4 mb-4 border-b border-[var(--border)]">
          <button
            className={`pb-2 transition-colors ${
              activeTab === "login"
                ? "border-b-2 border-[var(--primary)] font-semibold"
                : "text-[var(--muted)]"
            }`}
            onClick={() => setActiveTab("login")}
          >
            Login
          </button>
          <button
            className={`pb-2 transition-colors ${
              activeTab === "signup"
                ? "border-b-2 border-[var(--primary)] font-semibold"
                : "text-[var(--muted)]"
            }`}
            onClick={() => setActiveTab("signup")}
          >
            Sign Up
          </button>
        </div>

        {/* Content */}
        <div className="relative min-h-[280px] overflow-hidden">
          {activeTab === "login" ? <Login /> : <Signup />}
        </div>
      </div>
    </div>
  );
}
