'use client';

import AuthGuard from "@/components/auth/AuthGuard";
import "../../globals.css";
import Sidebar from "@/components/admin/Sidebar";
import { useEffect, useState } from "react";
import api from "@/lib/axios";
import { excludedTables } from "@/components/admin/menu";

export default function AdminLayout({
  children,
}: Readonly<{ children: React.ReactNode }>) {
  const [tables, setTables] = useState<string[] | null>(null);

  useEffect(() => {
    const fetchTables = async () => {
      try {
        const res = await api.get("/tables");
        setTables(res.data.tables.filter((t : string) => !excludedTables.includes(t)));
      } catch (error) {
        console.error("Error fetching tables:", error);
      }
    };

    fetchTables();
  }, []); // Dependency array ensures it runs once on mount

  return (
    <AuthGuard requiredAuthLevel={6}>
      <div className="min-h-screen bg-[var(--color-background-soft)] flex mt-2">
        {/* Sidebar - Ensure it has height */}
        <div className="min-w-56 max-w-56 min-h-screen bg-[var(--color-background)]">
          <Sidebar databaseTables={tables || []} />
        </div>

        {/* Main content with a background to make it visible */}
        <div className="flex-1 min-h-screen bg-[var(--color-background-soft)]">
          {children}
        </div>
      </div>
    </AuthGuard>
  );
}
