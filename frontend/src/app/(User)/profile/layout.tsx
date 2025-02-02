import ProfileSidebar from "@/components/ProfilePage/ProfileNavbar";

export default function ProfileLayout({ children }: { children: React.ReactNode }) {
  return (
    <div className="flex min-h-screen">
      {/* Sidebar */}
      <ProfileSidebar />

      {/* Main Content Area */}
      <main className="flex-1 p-6 bg-gray-100 dark:bg-gray-900 text-gray-900 dark:text-gray-100">
        {children}
      </main>
    </div>
  );
}
