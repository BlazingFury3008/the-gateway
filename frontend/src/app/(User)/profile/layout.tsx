"use client";

import AuthGuard from "@/components/auth/AuthGuard";
import ProfileSidebar from "@/components/ProfilePage/ProfileSidebar";
import { useSession } from "next-auth/react";
import Link from "next/link";
import { usePathname } from "next/navigation";
import { useEffect } from "react";

export default function ProfileLayout({ children }: { children: React.ReactNode }) {
  const { data: session } = useSession();
  const pathname = usePathname();

  useEffect(() => {
    window.scrollTo({ top: 0, behavior: "smooth" });
  }, [pathname]);

  return (
    <div className="flex min-h-screen sm:flex-row flex-col">
      {/* 🖥️ Desktop Sidebar (Always Visible) */}
      <AuthGuard requiredAuthLevel={1} />
      <div className="hidden sm:block w-64 bg-[var(--color-background)] border-r border-[var(--color-border)]">
        <ProfileSidebar />
      </div>

      {/* 📱 Mobile Topbar (Now Relative to Parent) */}
      <div className="sm:hidden w-full bg-[var(--color-form)] shadow-md border-b border-[var(--color-border)] flex items-center justify-between p-4">

        {/* User Welcome Message */}
        <h1 className="text-lg font-semibold text-[var(--color-foreground)]">
          {session?.user?.name ? `Welcome, ${session.user.name}!` : "Welcome!"}
        </h1>

        {/* Admin Page Button */}
        {session?.user?.auth === 6 && (
          <Link href="/admin" className="bg-blue-600 text-white px-4 py-2 rounded-lg text-sm">
            Admin
          </Link>
        )}
      </div>

      {/* 🖥️ Main Content Area */}
      <main className="flex flex-col flex-grow min-h-screen bg-[var(--color-background)] text-[var(--color-foreground)] transition-colors duration-300">
        {/* 🖥️ Desktop Header (Hidden on Mobile) */}
        <header className="hidden sm:flex p-6 border-b border-[var(--color-border)] bg-[var(--color-form)] shadow-sm justify-between items-center">
          <h1 className="text-2xl sm:text-3xl font-bold">
            {session?.user?.name ? `Welcome Back, ${session.user.name}!` : "Welcome Back!"}
          </h1>
          {session?.user?.auth === 6 && (
            <Link
              href="/admin"
              className="px-4 py-2 bg-blue-600 hover:bg-blue-700 text-white rounded-lg shadow-md transition"
            >
              Admin Page
            </Link>
          )}
        </header>

        {/* 📱 Mobile Content Padding Fix */}
        <div className="sm:p-6 flex-1 overflow-y-auto pt-6 pb-6 px-6">{children}</div>
      </main>
    </div>
  );
}
