"use client";
import React, { useState } from "react";

interface Subdomain {
  title: string;
  link: string;
}

interface Navbar_SubdropdownProps {
  title: string;
  domain_link: string;
  sub_domains: Subdomain[];
}

const Navbar_Subdropdown: React.FC<Navbar_SubdropdownProps> = ({
  title,
  domain_link,
  sub_domains,
}) => {
  const [isOpen, setIsOpen] = useState(false);
  const [isPanelOpen, setIsPanelOpen] = useState(false);
  const [openSubdomain, setOpenSubdomain] = useState<number | null>(null);

  return (
    <li className="relative">
      {/* Large Screens - Hover Dropdown */}
      <div
        className="hidden md:block"
        onMouseEnter={() => setIsOpen(true)}
        onMouseLeave={() => setIsOpen(false)}
      >
        <a
          href={domain_link}
          className="text-white px-4 py-2 block hover:underline focus:outline-none focus:ring-2 focus:ring-blue-500"
        >
          {title}
        </a>
        {isOpen && (
          <div className="absolute w-[320px] left-0 bg-gray-800 z-20 text-left">
            <ul className="space-y-2 text-white py-2">
              {sub_domains.map((subdomain, index) => (
                <li key={index}>
                  <a
                    href={domain_link + subdomain.link}
                    className="block py-2 px-4 hover:bg-gray-700 border-b-2 border-b-red-800"
                  >
                    {subdomain.title}
                  </a>
                </li>
              ))}
            </ul>
          </div>
        )}
      </div>

      {/* Small Screens - Fullscreen Slide-up Panel */}
      <div className="md:hidden xs:block">
        <button
          onClick={() => {
            setIsPanelOpen(true);
            setIsOpen(false)
          }}
          className="text-white px-4 py-2 block w-full text-left hover:underline focus:outline-none focus:ring-2 focus:ring-blue-500"
        >
          {title}
        </button>

        {/* Fullscreen Sliding Panel */}
        <div
          className={`fixed inset-0 bg-slate-900 bg-opacity-90 z-40 transform transition-transform duration-300 ease-in-out ${
            isPanelOpen
              ? "translate-y-0 opacity-100"
              : "translate-y-full opacity-0"
          }`}
        >
          <div className="p-6 text-white flex justify-between items-center">
            <span className="text-xl font-bold">{title}</span>
            <button
              onClick={() => setIsPanelOpen(false)}
              className="text-gray-400 hover:text-white text-2xl"
            >
              ✖
            </button>
          </div>

          <ul className="space-y-4 text-white px-6">
            {sub_domains.map((subdomain, index) => (
              <li key={index}>
                <button className="w-full text-left py-3 px-4 bg-gray-800 hover:bg-gray-700 font-semibold rounded-lg">
                  <a href={domain_link + subdomain.link}>{subdomain.title}</a>
                </button>
              </li>
            ))}
          </ul>
        </div>
      </div>
    </li>
  );
};

export default Navbar_Subdropdown;
