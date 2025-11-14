"use client";

import React, { useEffect, useState } from "react";
import { FaTimes } from "react-icons/fa";
import { useSearchParams, useRouter } from "next/navigation";

type ModalType = "error" | "notice" | "success" | "warning";

export default function SystemModal() {
  const searchParams = useSearchParams();
  const router = useRouter();

  const error = searchParams.get("error");
  const notice = searchParams.get("notice");
  const success = searchParams.get("success");
  const warning = searchParams.get("warning");

  const [open, setOpen] = useState(false);
  const [message, setMessage] = useState<string | null>(null);
  const [type, setType] = useState<ModalType>("notice");

  // Detect modal type + message automatically
  useEffect(() => {
    if (error) {
      setType("error");
      setMessage(error);
      setOpen(true);
    } else if (success) {
      setType("success");
      setMessage(success);
      setOpen(true);
    } else if (warning) {
      setType("warning");
      setMessage(warning);
      setOpen(true);
    } else if (notice) {
      setType("notice");
      setMessage(notice);
      setOpen(true);
    } else {
      setOpen(false);
      setMessage(null);
    }
  }, [error, notice, success, warning]);
  

  function closeModal() {
    setOpen(false);

    // Remove query params but keep user on same page
    router.replace(window.location.pathname, { scroll: false });
  }

  if (!open || !message) return null;

  const titleMap: Record<ModalType, string> = {
    error: "Error",
    success: "Success",
    warning: "Warning",
    notice: "Notice",
  };

  const colorMap: Record<ModalType, string> = {
    error: "text-red-400 border-red-400",
    success: "text-green-400 border-green-400",
    warning: "text-yellow-400 border-yellow-400",
    notice: "text-[var(--foreground)] border-[var(--border)]",
  };

  return (
    <div
      className="fixed inset-0 bg-black/60 z-[200] flex items-center justify-center p-4"
      onClick={closeModal}
    >
      <div
        className={`relative bg-[var(--navbar)] rounded-2xl shadow-2xl p-6 w-full max-w-md text-center animate-fadeIn border ${colorMap[type]}`}
        onClick={(e) => e.stopPropagation()}
      >
        <h2 className="text-lg font-semibold mb-3">{titleMap[type]}</h2>
        <p className="text-[var(--muted)] mb-6 leading-relaxed">{message}</p>

        <button
          onClick={closeModal}
          className="px-4 py-2 rounded-md bg-[var(--primary)] text-white hover:bg-[var(--secondary)] transition"
        >
          OK
        </button>

        <button
          className="absolute top-3 right-3 text-[var(--muted)] hover:text-[var(--foreground)]"
          onClick={closeModal}
        >
          <FaTimes />
        </button>
      </div>
    </div>
  );
}
