import { LucideIcon } from "lucide-react";
import Link from "next/link";

export default function OptionsBox({
  title,
  desc,
  linkText,
  link,
  icon: Icon,
}: {
  title: string;
  desc: string;
  linkText: string;
  link: string;
  icon: LucideIcon;
}) {
  return (
    <Link
      href={link}
      className="group block p-6 rounded-lg shadow-md transition-all duration-300 transform hover:scale-105 hover:shadow-lg
                 bg-[var(--color-background-soft)] hover:bg-[var(--color-background-hover)] 
                 border border-[var(--color-border)]"
    >
      <div className="flex items-center space-x-4">
        <Icon
          size={32}
          className="text-[var(--color-primary)] transition-all duration-300 group-hover:text-[var(--color-primary-hover)]"
        />
        <div>
          {/* Title */}
          <h2
            className="text-xl font-semibold transition-all duration-300 text-[var(--color-foreground)]
                         group-hover:text-[var(--color-primary-hover)]"
          >
            {title}
          </h2>
          {/* Description */}
          <p
            className="text-[var(--color-foreground-soft)] transition-all duration-300 
                        group-hover:text-[var(--color-foreground-hover)]"
          >
            {desc}
          </p>
          {/* Link */}
          <span
            className="inline-block mt-2 text-[var(--color-primary)] hover:underline transition-all duration-300 
                           group-hover:text-[var(--color-primary-hover)]"
          >
            {linkText}
          </span>
        </div>
      </div>
    </Link>
  );
}
