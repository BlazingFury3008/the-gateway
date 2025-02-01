'use client';
import React, { useState } from "react";
import Navbar_Subdropdown from "./navbar_subdropdown";
import Navbar_Link from "./navbar_link";
import MenuIcon from "@mui/icons-material/Menu";
import CloseIcon from "@mui/icons-material/Close";

export default function Navbar() {
  const [isOpen, setIsOpen] = useState(false);

  return (
    <div className="h-16 bg-gray-800 font-mono flex items-center justify-between px-4">
      {/* Logo / Title */}
      <h3 className="text-lg text-white text-center mt-2 hidden md:block">The Gateway</h3>
      <button className="text-lg text-white text-center mt-2 md:hidden" aria-label="Toggle Menu">
        The Gateway
      </button>

      {/* Button for small screens */}
      <button
        className="md:hidden"
        onClick={() => setIsOpen(!isOpen)}
        aria-label="Toggle Menu"
      >
        {isOpen ? <CloseIcon fontSize="large" /> : <MenuIcon fontSize="large" />}
      </button>

      {/* Desktop Menu */}
      <div className="hidden md:flex">
        <ul className="mx-2 flex gap-4 text-sm text-white">
          <Navbar_Link title="Home" link="/" />
          <Navbar_Subdropdown
            title="Wiki"
            domain_link="/wiki"
            sub_domains={[
              { title: "Vampire: The Masquerade 5th Ed", link: "/VTM_5th_Ed" },
              { title: "Hunter: The Reckoning 5th Ed", link: "/HTR_5th_Ed" },
              { title: "Werewolf: The Apocalypse 5th Ed", link: "/WTA_5th_Ed" },
            ]}
          />
          <Navbar_Subdropdown
            title="Character Creation"
            domain_link="/cc"
            sub_domains={[
              { title: "Vampire: The Masquerade 5th Ed", link: "/VTM_5th_Ed" },
              { title: "Hunter: The Reckoning 5th Ed", link: "/HTR_5th_Ed" },
              { title: "Werewolf: The Apocalypse 5th Ed", link: "/WTA_5th_Ed" },
            ]}
          />
        </ul>
      </div>

      {/* Mobile Sliding Panel */}
      <div
        className={`fixed top-0 right-0 bg-gray-900 w-screen h-full text-white transform transition-transform duration-300 ease-in-out ${
          isOpen ? "translate-x-0" : "translate-x-full"
        } md:hidden`}
      >
        <button className="absolute top-4 right-4" onClick={() => setIsOpen(false)}>
          <CloseIcon fontSize="large" />
        </button>
        <ul className="mt-12 space-y-4 px-6">
          <Navbar_Link title="Home" link="/" />
          <Navbar_Subdropdown
            title="Wiki"
            domain_link="/wiki"
            sub_domains={[
              { title: "Vampire: The Masquerade 5th Ed", link: "/VTM_5th_Ed" },
              { title: "Hunter: The Reckoning 5th Ed", link: "/HTR_5th_Ed" },
              { title: "Werewolf: The Apocalypse 5th Ed", link: "/WTA_5th_Ed" },
            ]}
          />
          <Navbar_Subdropdown
            title="Character Creation"
            domain_link="/cc"
            sub_domains={[
              { title: "Vampire: The Masquerade 5th Ed", link: "/VTM_5th_Ed" },
              { title: "Hunter: The Reckoning 5th Ed", link: "/HTR_5th_Ed" },
              { title: "Werewolf: The Apocalypse 5th Ed", link: "/WTA_5th_Ed" },
            ]}
          />
        </ul>
      </div>
    </div>
  );
}
