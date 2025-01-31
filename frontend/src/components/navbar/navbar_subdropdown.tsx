'use client'
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
        className="hidden sm:block"
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
          <div className="absolute w-[320px] sm:inset-x-0 left-0 bg-gray-800 z-20 text-left">
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
      <div className="sm:hidden">
        <button
          onClick={() => setIsPanelOpen(true)}
          className="text-white px-4 py-2 block w-full text-left hover:underline focus:outline-none focus:ring-2 focus:ring-blue-500"
        >
          {title}
        </button>

        {/* Fullscreen Sliding Panel */}
        <div
          className={`fixed inset-0 bg-gray-900 bg-opacity-90 z-40 transform transition-transform duration-300 ease-in-out ${
            isPanelOpen ? "translate-y-0 opacity-100" : "translate-y-full opacity-0"
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
                <button
                  onClick={() =>
                    setOpenSubdomain(openSubdomain === index ? null : index)
                  }
                  className="w-full text-left py-3 px-4 bg-gray-800 hover:bg-gray-700 text-lg font-semibold rounded-lg"
                >
                  {subdomain.title}
                </button>
                {openSubdomain === index && (
                  <a
                    href={domain_link + subdomain.link}
                    className="block py-2 px-6 bg-gray-700 text-md hover:bg-gray-600 rounded-lg mt-2"
                  >
                    Go to {subdomain.title}
                  </a>
                )}
              </li>
            ))}
          </ul>
        </div>
      </div>
    </li>
  );
};

export default Navbar_Subdropdown;
