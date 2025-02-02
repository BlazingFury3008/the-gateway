import { LucideIcon } from "lucide-react";

interface SidebarButtonProps {
  label: string;
  icon: LucideIcon;
  href?: string;
  onClick?: () => void;
  variant?: "default" | "danger";
}

export default function SidebarButton({ label, icon: Icon, href, onClick, variant = "default" }: SidebarButtonProps) {
  const baseStyles = "flex items-center space-x-2 p-3 rounded-lg transition-all duration-200";
  const defaultStyles = "bg-gray-800 text-white hover:bg-gray-700";
  const dangerStyles = "bg-red-600 text-white hover:bg-red-500";

  return (
    <a
      href={href}
      onClick={onClick}
      className={`${baseStyles} ${variant === "danger" ? dangerStyles : defaultStyles}`}
    >
      <Icon size={20} />
      <span>{label}</span>
    </a>
  );
}
