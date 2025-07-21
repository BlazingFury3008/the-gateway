"use client";
import { Home, LogOut } from "lucide-react";
import SidebarButton from "./SidebarButton";
import { links } from "./links";
import { useSession } from "next-auth/react";
import Image from "next/image";
import { DEFAULT_USER_ICON } from "@/app/helper";

export default function ProfileSidebar() {
  const { data: session } = useSession();
  return (
    <div className="hidden md:flex w-64 h-screen bg-[var(--color-form)] text-[var(--color-foreground)] border-r border-[var(--color-border)] shadow-md flex-col">
      {/* Profile Header */}
      <div className="flex flex-col items-center py-6 border-b border-[var(--color-border)]">
        <div className="w-16 h-16 rounded-full bg-gray-400 dark:bg-gray-600 flex items-center justify-center text-white border overflow-hidden">
          <Image
            src={session?.user?.image || DEFAULT_USER_ICON}
            alt="Profile picture"
            width={256}
            height={256}
            className="object-cover w-full h-full"
            quality={100}
          />{" "}
        </div>
        <p className="mt-2 font-semibold">{session?.user?.name}</p>
      </div>

      {/* Navigation Links */}
      <nav className="flex-1 p-4 space-y-4">
        <SidebarButton label="Dashboard" icon={Home} href="/profile" />
        {links.map((link, index) => (
          <SidebarButton
            label={link.title}
            icon={link.icon}
            href={link.link}
            key={index}
          />
        ))}
      </nav>

      {/* Logout Button */}
      <div className="p-4 border-t border-[var(--color-border)]">
        <SidebarButton
          label="Logout"
          icon={LogOut}
          href="/logout"
          variant="danger"
        />
      </div>
    </div>
  );
}
