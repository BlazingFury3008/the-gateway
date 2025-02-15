'use client';
import Link from "next/link";
import React from "react";

interface SelectionBoxProps {
  title: string;
  description: string;
  icon: React.ReactNode;
  link: string;
  bgColor: string; // RGBA Color (e.g., "rgba(130, 0, 0, 0.8)")
  enabled: boolean;
}

export default function SelectionBox({ title, description, icon, link, bgColor, enabled }: SelectionBoxProps) {
  // Adjusted RGBA transparency for better contrast in light mode
  const modifiedBgColor = bgColor.replace(/[\d\.]+\)$/g, "0.3)"); 

  if (!enabled) {
    return (
      <div className="group relative opacity-60 grayscale transition-all duration-300">
        <div className="relative w-full h-52 rounded-lg shadow-lg overflow-hidden bg-[var(--color-form)] border border-[var(--color-border)]">
          <div
            className="absolute inset-0 transition-opacity duration-500 ease-in-out"
            style={{
              background: `linear-gradient(to right, rgba(150,150,150,0.8) 0%, rgba(0,0,0,0.1) 100%)`,
            }}
          ></div>

          {/* Content */}
          <div className="relative z-10 flex flex-col justify-center items-center text-center p-6">
            <div className="mb-3 text-4xl text-[var(--color-foreground)]">{icon}</div>
            <h2 className="text-xl font-semibold text-[var(--color-foreground)]">{title}</h2>
            <p className="text-sm text-[var(--color-foreground-soft)]">{description}</p>
          </div>
        </div>
      </div>
    );
  }

  return (
    <Link href={link}>
      <div className="group relative cursor-pointer">
        <div className="relative w-full h-52 rounded-lg shadow-lg overflow-hidden transition-transform duration-500 ease-in-out transform bg-[var(--color-form)] hover:scale-105 hover:shadow-xl border border-[var(--color-border)]">
          {/* ✅ Better gradient for light mode */}
          <div
            className="absolute inset-0 transition-opacity duration-500 ease-in-out group-hover:bg-opacity-50"
            style={{
              background: `linear-gradient(to right, ${bgColor} 0%, ${modifiedBgColor} 100%)`,
            }}
          ></div>

          {/* Content */}
          <div className="relative z-10 flex flex-col justify-center items-center text-center p-6">
            <div className="mb-3 text-4xl text-[var(--color-foreground)]">{icon}</div>
            <h2 className="text-xl font-semibold text-[var(--color-foreground)]">{title}</h2>
            <p className="text-sm text-[var(--color-foreground-soft)]">{description}</p>
          </div>
        </div>
      </div>
    </Link>
  );
}
