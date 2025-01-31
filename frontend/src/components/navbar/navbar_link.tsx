import React from "react";

export default function Navbar_Link({
  title,
  link,
}: {
  title: string;
  link: string;
}) {
  return (
    <li className="relative group">
      <a
        href={link}
        className="text-white px-4 py-2 block hover:underline focus:outline-none focus:ring-2 focus:ring-blue-500"
      >
        {title}
      </a>
    </li>
  );
}
