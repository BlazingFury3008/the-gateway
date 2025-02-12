import { links } from "@/components/ProfilePage/links";
import OptionsBox from "@/components/ProfilePage/OptionsBox";

export default function ProfilePage() {
  return (
    <div className="p-4 sm:p-6 grid grid-cols-1 sm:grid-cols-1 md:grid-cols-2 lg:grid-cols-2 lg:gap-x-16 gap-4 lg:mx-20">
      {links.map((link, index) => (
        <OptionsBox
          key={index}
          title={link.title}
          desc={`Manage your ${link.title.toLowerCase()} and explore related content.`} 
          linkText={link.linkText}
          link={link.link}
          icon={link.icon}
        />
      ))}
    </div>
  );
}
