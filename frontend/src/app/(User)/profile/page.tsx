"use client";
import { useSession } from "next-auth/react";
import { FileText, Users, Star, Edit } from "lucide-react";
import Image from "next/image";
import { useRouter } from "next/navigation";

const DEFAULT_AVATAR = "https://cdn-icons-png.flaticon.com/512/847/847969.png";

export default function ProfilePage() {
  const { data: session, status } = useSession();
  const router = useRouter();

  if (status === "loading") {
    return <p className="text-center text-gray-500 dark:text-gray-400">Loading profile...</p>;
  }

  if (status === "unauthenticated") {
    return (
      <div className="text-center text-red-500">
        <p>You must be logged in to view your profile.</p>
        <button
          onClick={() => router.push("/api/auth/signin")}
          className="mt-4 bg-blue-600 text-white px-4 py-2 rounded-lg"
        >
          Sign In
        </button>
      </div>
    );
  }

  const user = session?.user;

  return (
    <div className="space-y-6">
      {/* Profile Header */}
      <div className="bg-white dark:bg-gray-800 p-6 rounded-2xl shadow-md flex items-center gap-6">
      <Image
  src={user?.image || DEFAULT_AVATAR}
  alt="Profile Picture"
  width={80}
  height={80}
  className="rounded-full border-2 border-gray-300 dark:border-gray-600"
/>
        <div className="flex-1">
          <h1 className="text-2xl font-bold text-gray-900 dark:text-gray-100">{user?.name || "Unknown User"}</h1>
          <p className="text-gray-600 dark:text-gray-400">{user?.email || "No email available"}</p>
        </div>
        <button className="flex items-center gap-2 bg-gray-200 dark:bg-gray-700 text-gray-900 dark:text-white px-4 py-2 rounded-lg">
          <Edit size={18} />
          Edit Profile
        </button>
      </div>

      {/* Stats Section (Dummy Data for Now) */}
      <div className="grid grid-cols-3 gap-6">
        <StatCard label="Content" value={12} icon={FileText} />
        <StatCard label="Characters" value={8} icon={Users} />
        <StatCard label="Favourites" value={25} icon={Star} />
      </div>

      {/* Navigation Buttons */}
      <div className="grid grid-cols-3 gap-4">
        <ProfileNavButton label="My Content" icon={FileText} href="/profile/content" />
        <ProfileNavButton label="My Characters" icon={Users} href="/profile/characters" />
        <ProfileNavButton label="My Favourites" icon={Star} href="/profile/favourites" />
      </div>
    </div>
  );
}

/* Stats Card Component */
function StatCard({ label, value, icon: Icon }: { label: string; value: number; icon: any }) {
  return (
    <div className="bg-white dark:bg-gray-800 p-6 rounded-xl shadow-md flex items-center gap-4">
      <Icon size={28} className="text-gray-700 dark:text-gray-300" />
      <div>
        <h2 className="text-xl font-semibold text-gray-900 dark:text-gray-100">{value}</h2>
        <p className="text-gray-600 dark:text-gray-400">{label}</p>
      </div>
    </div>
  );
}

/* Navigation Button Component */
function ProfileNavButton({ label, icon: Icon, href }: { label: string; icon: any; href: string }) {
  return (
    <a
      href={href}
      className="flex items-center justify-center gap-2 bg-gray-200 dark:bg-gray-700 text-gray-900 dark:text-white 
      px-6 py-3 rounded-xl text-lg font-medium transition hover:bg-gray-300 dark:hover:bg-gray-600"
    >
      <Icon size={20} />
      {label}
    </a>
  );
}
