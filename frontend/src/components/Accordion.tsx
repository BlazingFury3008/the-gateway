"use client";

import React from "react";

interface AccordionProps {
  title: string;
  isOpen: boolean;
  toggle: () => void;
  children: React.ReactNode;
}

export default function Accordion({ title, isOpen, toggle, children }: AccordionProps) {
  return (
    <div className="border border-[var(--color-border)] rounded-lg shadow-md bg-[var(--color-background-soft)]">
      {/* Accordion Header */}
      <button
        className="w-full flex justify-between items-center px-4 py-3 text-[var(--color-foreground)] font-semibold text-lg transition-all duration-300 hover:bg-[var(--color-background-hover)]"
        onClick={toggle}
      >
        {title}
        <span className={`transform transition-transform duration-300 ${isOpen ? "rotate-180" : "rotate-0"}`}>
          ▼
        </span>
      </button>

      {/* Collapsible Content */}
      <div
        className={`transition-all duration-300 ease-in-out p-2 ${
          isOpen ? "max-h-[500px] opacity-100" : "max-h-0 opacity-0"
        } overflow-scroll`}
      >
        {children}
      </div>
    </div>
  );
}
