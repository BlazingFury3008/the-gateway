'use client';
import React, { useState } from "react";
import Navbar_Subdropdown from "./navbar_subdropdown";
import Navbar_Link from "./navbar_link";
import MenuIcon from "@mui/icons-material/Menu";
import CloseIcon from "@mui/icons-material/Close";

export default function Navbar() {
  const [isOpen, setIsOpen] = useState(false);

  return (
    <>
      {/* MOBILE NAVBAR */}
      <div className="h-16 bg-slate-900 font-mono flex items-center justify-between px-4 md:hidden">
        {/* Title on left */}
        <h3 className="text-lg text-white">The Gateway</h3>
        {/* Toggle button on right */}
        <button onClick={() => setIsOpen(!isOpen)} aria-label="Toggle Menu" className="text-white">
          {isOpen ? <CloseIcon fontSize="large" /> : <MenuIcon fontSize="large" />}
        </button>
      </div>

      {/* MOBILE SLIDING PANEL */}
      <div
        className={`fixed top-0 right-0 bg-slate-900 w-screen h-full text-white transform transition-transform duration-300 ease-in-out ${
          isOpen ? "translate-x-0" : "translate-x-full"
        } md:hidden`}
      >
        <button className="absolute top-4 right-4" onClick={() => setIsOpen(false)} aria-label="Close Menu">
          <CloseIcon fontSize="large" />
        </button>
        <ul className="mt-4 space-y-4 px-6">
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

      {/* DESKTOP NAVBAR */}
      <div className="hidden md:flex flex-col bg-slate-900 font-mono">
        {/* Top row: Title centered */}
        <div className="h-12 flex items-center justify-center">
          <h3 className="text-lg text-white">The Gateway</h3>
        </div>
        {/* Bottom row: Options centered */}
        <div className="flex items-center justify-center border-t border-gray-700">
          <ul className="flex gap-8 text-sm text-white">
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
    </>
  );
}
