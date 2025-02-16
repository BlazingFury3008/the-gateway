import { LucideIcon } from "lucide-react";
import Link from "next/link";

interface SidebarButtonProps {
  label: string;
  icon: LucideIcon;
  href: string;
  variant?: "default" | "danger";
}

export default function SidebarButton({ label, icon: Icon, href, variant = "default" }: SidebarButtonProps) {
  const baseStyles =
    "flex items-center space-x-3 p-3 rounded-lg transition-all duration-300 w-full text-left";
  const defaultStyles =
    "bg-[var(--color-background)] text-[var(--color-foreground)] hover:bg-gray-200 dark:hover:bg-gray-700 border border-[var(--color-border)] shadow-sm";
  const dangerStyles = "bg-red-600 text-white hover:bg-red-500";

  return (
    <Link
    
      href={href}
      className={`${baseStyles} ${variant === "danger" ? dangerStyles : defaultStyles}`}
    >
      <Icon size={20} />
      <span>{label}</span>
    </Link>
  );
}
