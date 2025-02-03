import ProfileSidebar from "@/components/ProfilePage/ProfileSidebar";

export default function ProfileLayout({ children }: { children: React.ReactNode }) {
  return (
    <div className="flex min-h-screen bg-gray-50 dark:bg-gray-900 pt-5">
      {/* Sidebar */}
      <ProfileSidebar/>

      {/* Main Content */}
      <main className="flex-1 px-6 pb-6 md:px-8 md:pb-8 lg:px-10 lg:pb-10 md:pt-3 pt-1 lg:pt-5">
        <div className="max-w-4xl mx-auto">{children}</div>
      </main>
    </div>
  );
}
