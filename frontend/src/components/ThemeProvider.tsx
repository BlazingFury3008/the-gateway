"use client";

import { useEffect, useState } from "react";

export default function ThemeProvider({ children }: { children: React.ReactNode }) {
  const [themeLoaded, setThemeLoaded] = useState(false);
  const [isFading, setIsFading] = useState(false);

  useEffect(() => {
    const theme = localStorage.getItem("theme") || "light"; // Default to light mode
    document.documentElement.classList.add(theme);

    setTimeout(() => {
      setIsFading(true); // Start fade-out animation
      setTimeout(() => setThemeLoaded(true), 500); // Remove after animation completes
    }, 500); // Keep visible briefly before fading
  }, []);

  if (!themeLoaded) {
    return (
      <div
        className={`fixed inset-0 flex items-center justify-center bg-background transition-opacity duration-500 ${
          isFading ? "opacity-0" : "opacity-100"
        }`}
      >
        {/* Clean Loading Spinner */}
        <div className="relative flex items-center justify-center">
          <div className="absolute h-60 w-60 border-4 border-[var(--color-border)] border-t-transparent rounded-full animate-spin"></div>
          <div className="h-48 w-48 bg-[var(--color-border)] rounded-full animate-pulse"></div>
        </div>
      </div>
    );
  }

  return <>{children}</>;
}
