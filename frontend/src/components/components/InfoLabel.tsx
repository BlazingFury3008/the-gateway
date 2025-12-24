import React, { useState } from "react";

interface InfoLabelProps {
  label: string;
  htmlFor?: string;
  info?: React.ReactNode;
}

export default function InfoLabel({ label, htmlFor, info }: InfoLabelProps) {
  const [open, setOpen] = useState(false);

  if (!info) {
    // plain label if no info text provided
    return (
      <label htmlFor={htmlFor} className="block text-sm font-medium mb-1">
        {label}
      </label>
    );
  }

  return (
    <div
      className="relative inline-flex items-center gap-1 mb-1"
      onBlur={() => setOpen(false)}
    >
      <label htmlFor={htmlFor} className="block text-sm font-medium">
        {label}
      </label>

      {/* little ? button */}
      <button
        type="button"
        className="w-5 h-5 text-xs rounded-full border border-[var(--border)] bg-[var(--background)] text-[var(--muted)] flex items-center justify-center hover:bg-[var(--navbar)]"
        aria-label={`More info about ${label}`}
        aria-expanded={open}
        onClick={() => setOpen((o) => !o)}
      >
        ?
      </button>

      {open && (
        <div className="absolute left-0 mt-2 w-64 text-xs bg-[var(--navbar)] border border-[var(--border)] rounded-md p-2 shadow-lg z-20">
          {info}
        </div>
      )}
    </div>
  );
}
