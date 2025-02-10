"use client";
import { Home, LogOut, User } from "lucide-react";
import SidebarButton from "./SidebarButton";
import { links } from "./links";
import { useSession } from "next-auth/react";

export default function ProfileSidebar() {
  const {data: session} = useSession()
  return (
    <div className="hidden md:flex w-64 h-screen bg-[var(--color-background-soft)] text-[var(--color-foreground)] border-r border-[var(--color-border)] shadow-md flex-col">
      {/* Profile Header */}
      <div className="flex flex-col items-center py-6 border-b border-[var(--color-border)]">
        <div className="w-16 h-16 rounded-full bg-gray-400 dark:bg-gray-600 flex items-center justify-center text-white">
          <User size={32} />
        </div>
        <p className="mt-2 font-semibold">{session?.user?.name}</p>
      </div>

      {/* Navigation Links */}
      <nav className="flex-1 p-4 space-y-4">
        <SidebarButton label="Dashboard" icon={Home} href="/profile" />
        {links.map((link, index) => (
        <SidebarButton label={link.title} icon={link.icon} href={link.link} key={index} />

        ))}
      </nav>

      {/* Logout Button */}
      <div className="p-4 border-t border-[var(--color-border)]">
        <SidebarButton label="Logout" icon={LogOut} href="/logout" variant="danger" />
      </div>
    </div>
  );
}
