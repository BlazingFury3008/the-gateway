'use client'

import { links } from "@/components/ProfilePage/links";
import OptionsBox from "@/components/ProfilePage/OptionsBox";

export default function ProfilePage() {

  return (
    <div className="p-6 grid grid-cols-1 md:grid-cols-1 lg:grid-cols-2 lg:gap-x-16 gap-6 lg:mx-20">
      {links.map((link, index) => (
        <OptionsBox
          key={index}
          title={link.title}
          desc={`Manage your ${link.title.toLowerCase()} and explore related content.`} // Auto-generate descriptions
          linkText={link.linkText}
          link={link.link}
          icon={link.icon} // Pass the icon to OptionsBox
        />
      ))}
    </div>
  );
}
