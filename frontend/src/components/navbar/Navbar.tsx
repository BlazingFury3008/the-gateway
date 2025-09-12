"use client";
import React, { useEffect, useRef, useState } from "react";
import NavProfile from "./NavProfile";
import { FaMoon, FaSun } from "react-icons/fa";
import Login from "./Login";
import Signup from "./Signup";

export default function Navbar() {
  const [loggedIn, setLoggedIn] = useState(false);
  const [theme, setTheme] = useState<"light" | "dark" | null>(null);

  // Load theme from localStorage on mount
  useEffect(() => {
    const savedTheme = localStorage.getItem("theme") as "light" | "dark" | null;
    if (savedTheme) {
      setTheme(savedTheme);
      document.documentElement.setAttribute("data-theme", savedTheme);
    } else {
      // fallback to system preference
      const prefersDark = window.matchMedia("(prefers-color-scheme: dark)").matches;
      const initialTheme = prefersDark ? "dark" : "light";
      setTheme(initialTheme);
      document.documentElement.setAttribute("data-theme", initialTheme);
    }
  }, []);

  // Apply theme whenever it changes
  useEffect(() => {
    if (theme) {
      document.documentElement.setAttribute("data-theme", theme);
      localStorage.setItem("theme", theme);
    }
  }, [theme]);

  return (
    <div className="h-18 navbar rounded-b-md flex">
      <div className="h-full flex items-center">
        <h1 className="font-bold ml-5 w-64 text-2xl text-center">
          The Gateway
        </h1>
      </div>
      <div className="flex justify-between h-full w-full items-center">
        {/* Navbar Buttons */}
        <div className="w-8/11 flex justify-baseline h-full items-center">
          <button className="navbar_button">Home</button>
        </div>
        {/* Login/Signup + Theme Toggle */}
        <div className="w-3/11 h-full items-center flex space-x-2">
          {loggedIn ? <NavProfile /> : <LoginComponent />}
          {theme && (
            <button
              onClick={() => setTheme(theme === "light" ? "dark" : "light")}
              className="!p-2 !rounded-full bg-[var(--background)] text-[var(--foreground)] border border-[var(--border)] hover:bg-[var(--primary)] hover:text-white transition"
            >
              {theme === "light" ? <FaMoon /> : <FaSun />}
            </button>
          )}
        </div>
      </div>
    </div>
  );
}


function LoginComponent() {
  const [isOpen, setIsOpen] = useState(false);
  const [activeTab, setActiveTab] = useState<"login" | "signup">("login");

  const wrapperRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    function handleClickOutside(event: MouseEvent) {
      if (
        wrapperRef.current &&
        !wrapperRef.current.contains(event.target as Node)
      ) {
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
      {/* Button to open/close login modal */}
      <button
        onClick={() => setIsOpen(!isOpen)}
        className="navbar_login bg-[var(--navbar)] text-white"
      >
        Login / Signup
      </button>

      {/* Popup */}
      <div
        className={`absolute right-0 border border-[var(--border)] w-96 rounded-2xl p-5 bg-[var(--navbar)] mt-2 shadow-xl text-[var(--foreground)] transform transition-all duration-300 origin-top ${
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

        {/* Animated Content */}
        <div className="relative min-h-[280px] overflow-hidden">
          <div
            className={`absolute inset-0 transform transition-all duration-300 ${
              activeTab === "login"
                ? "translate-x-0 opacity-100"
                : "-translate-x-full opacity-0"
            }`}
          >
            <Login />
          </div>
          <div
            className={`absolute inset-0 transform transition-all duration-300 ${
              activeTab === "signup"
                ? "translate-x-0 opacity-100"
                : "translate-x-full opacity-0"
            }`}
          >
            <Signup />
          </div>
        </div>
      </div>
    </div>
  );
}
