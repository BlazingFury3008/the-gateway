"use client";
import { useState } from "react";
import { Menu, X, Home, Settings, Shield, LogOut } from "lucide-react";
import SidebarButton from "./SidebarButton";

export default function ProfileSidebar() {
  const [isOpen, setIsOpen] = useState(false);

  return (
    <>
      {/* Mobile Hamburger Button */}
      <button
        className="md:hidden fixed top-4 left-4 z-50 bg-gray-800 text-white p-2 rounded-md"
        onClick={() => setIsOpen(!isOpen)}
      >
        {isOpen ? <X size={24} /> : <Menu size={24} />}
      </button>

      {/* Sidebar Panel */}
      <div
        className={`border-r-white border-r-2 fixed top-0 left-0 h-full min-h-screen w-64 bg-gray-900 text-white shadow-lg transition-transform duration-300 ease-in-out
        ${isOpen ? "translate-x-0" : "-translate-x-64"} md:translate-x-0 md:relative flex flex-col`}
      >
        {/* Sidebar Header */}
        <div className="flex items-center justify-between p-5 border-b border-gray-700">
          <h2 className="text-xl font-bold">Profile</h2>
          <button className="md:hidden" onClick={() => setIsOpen(false)}>
            <X size={24} />
          </button>
        </div>

        {/* Navigation Links */}
        <nav className="flex-1 p-5 space-y-4">
          <SidebarButton label="Dashboard" icon={Home} href="/profile" />
          <SidebarButton label="Settings" icon={Settings} href="/profile/settings" />
          <SidebarButton label="Security" icon={Shield} href="/profile/security" />
        </nav>

        {/* Logout Button (At the Bottom) */}
        <div className="p-5 border-t border-gray-700">
          <SidebarButton label="Logout" icon={LogOut} href="/logout" variant="danger" />
        </div>
      </div>

      {/* Overlay for Mobile */}
      {isOpen && (
        <div
          className="fixed inset-0 bg-black bg-opacity-50 z-40 md:hidden"
          onClick={() => setIsOpen(false)}
        />
      )}
    </>
  );
}
