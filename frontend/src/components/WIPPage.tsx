"use client";
import React from "react";
import { useRouter } from "next/navigation";

export default function WIPPage() {
  const router = useRouter();

  return (
    <div className="flex flex-col items-center justify-center min-h-screen bg-[var(--color-background-soft)] text-gray-800">
      <h1 className="text-4xl font-bold mb-4 text-[var(--color-foreground)]">🚧 Work in Progress 🚧</h1>
      <p className="text-lg text-center max-w-lg mb-6 text-[var(--color-foreground)]">
        This page is currently under construction. Check back soon for updates!
      </p>
      <button
        onClick={() => router.back()}
        className="px-4 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700 transition"
      >
        Go Back
      </button>
    </div>
  );
}
