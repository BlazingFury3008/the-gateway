import React, { useState } from "react";

interface InfoLabelProps {
  label: string;
  htmlFor?: string;
  info?: React.ReactNode;
}

export default function InfoLabel({ label, htmlFor, info }: InfoLabelProps) {
  const [open, setOpen] = useState(false);

  if (!info) {
    return (
      <label htmlFor={htmlFor} className="block text-sm font-medium mb-1 truncate">
        {label}
      </label>
    );
  }

  return (
    <div
      className="relative flex items-center gap-1 mb-1 w-full min-w-0"
      onBlur={() => setOpen(false)}
    >
      <label htmlFor={htmlFor} className="text-sm font-medium truncate min-w-0 flex-1">
        {label}
      </label>

      <button
        type="button"
        className="shrink-0 w-5 h-5 text-xs rounded-full border border-[var(--border)] bg-[var(--background)] text-[var(--muted)] flex items-center justify-center hover:bg-[var(--navbar)]"
        aria-label={`More info about ${label}`}
        aria-expanded={open}
        onClick={() => setOpen((o) => !o)}
      >
        ?
      </button>

      {open && (
        <div className="absolute left-0 top-full mt-2 w-64 text-xs bg-[var(--navbar)] border border-[var(--border)] rounded-md p-2 shadow-lg z-20">
          {info}
        </div>
      )}
    </div>
  );
}
