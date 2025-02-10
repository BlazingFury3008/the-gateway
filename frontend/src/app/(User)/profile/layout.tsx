'use client'
import AuthGuard from "@/components/auth/AuthGuard";
import ProfileSidebar from "@/components/ProfilePage/ProfileSidebar";
import { useSession } from "next-auth/react";

export default function ProfileLayout({ children }: { children: React.ReactNode }) {
    const { data: session } = useSession();
  
  return (
    <AuthGuard>
      <div className="flex h-screen">
        {/* Sidebar */}
        <ProfileSidebar />

        {/* Main Content Area */}
        <main className="flex-1 flex flex-col bg-[var(--color-background)] text-[var(--color-foreground)] transition-colors duration-300">
          {/* User Profile Header */}
          <header className="p-6 border-b border-[var(--color-border)] bg-[var(--color-background-soft)] shadow-sm flex justify-between items-center">
            <h1 className="text-3xl font-bold">Welcome Back, {session?.user?.name}!</h1>
            <button className="px-4 py-2 bg-blue-600 hover:bg-blue-700 text-white rounded-lg shadow-md transition">
              Edit Profile
            </button>
          </header>

          {/* Content Area */}
          <div className="p-6 flex-1">{children}</div>
        </main>
      </div>
    </AuthGuard>
  );
}
