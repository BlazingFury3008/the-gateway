import React from "react";

export default function Navbar_Subdropdown({
  title,
  sub_domains,
  domain_link,
}: {
  title: string;
  sub_domains: { title: string; link: string }[];
  domain_link: string;
}) {
  return (
    <li className="relative group px-4 py-2 cursor-pointer">
      <a className="hover:underline" href={domain_link}>
        {title}
      </a>
      <ul className="absolute text-xs left-0 top-full min-w-[500px] bg-gray-700 text-white shadow-md rounded-md group-hover:flex flex-col opacity-0 group-hover:opacity-100 transition-opacity duration-200 pointer-events-none group-hover:pointer-events-auto py-2">
        {sub_domains.map(({ title, link }, index) => (
          <li key={index} className="px-3 py-2 hover:bg-gray-600">
            <a href={domain_link + link} className="block px-4">
              {title}
            </a>
          </li>
        ))}
      </ul>
    </li>
  );
}
