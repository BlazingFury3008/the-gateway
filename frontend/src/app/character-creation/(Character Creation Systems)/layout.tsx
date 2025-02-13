import React from "react";

export default function Layout({ children }: { children: React.ReactNode }) {
  return <div className="w-screen h-screen px-3 pt-2 bg-[var(--color-background-soft)]">{children}</div>;
}
