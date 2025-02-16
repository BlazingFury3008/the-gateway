import AuthGuard from "@/components/auth/AuthGuard"
import "../../globals.css"

export default function AdminLayout({
  children,
}: Readonly<{ children: React.ReactNode }>) {
  return (
    <AuthGuard requiredAuthLevel={6} >
         <div>
    {children}
   </div>
    </AuthGuard>

  );
}
