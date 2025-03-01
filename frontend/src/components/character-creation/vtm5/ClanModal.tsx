"use client";

import Image from "next/image";
import { vtm5_getClanSymbol } from "@/app/helper";
import { useEffect, useState } from "react";

interface Clan {
  ID: number;
  Name: string;
  Description: string;
  "Clan Bane": string;
  "Variant Bane": string;
}

interface Discipline {
  ID: number;
  Name: string;
}

export default function ClanModal({
  clan,
  disciplines,
  onClose,
}: {
  clan: Clan;
  disciplines: Discipline[];
  onClose: () => void;
}) {

  const [isDarkMode, setIsDarkMode] = useState(false);

  useEffect(() => {
    const checkDarkMode = () => {
      setIsDarkMode(document.documentElement.classList.contains("dark"));
    };

    checkDarkMode();
    const observer = new MutationObserver(checkDarkMode);
    observer.observe(document.documentElement, { attributes: true });

    return () => observer.disconnect();
  }, []);


  return (
    <div className="fixed inset-0 flex items-center justify-center bg-black bg-opacity-50 backdrop-blur-sm px-4 z-50">
      {/* Modal Container */}
      <div className="relative bg-[var(--color-background)] text-foreground p-6 rounded-2xl shadow-lg w-full max-w-[90%] sm:max-w-[700px] border border-border overflow-hidden">
        
        {/* Background Image */}
        <div className="absolute inset-0">
          <Image
            src={vtm5_getClanSymbol(clan.Name)}
            alt={`${clan.Name} Symbol`}
            fill
            className={`object-cover p-8 opacity-20 blur-[1px] select-none ${isDarkMode && "invert"}`}
          />
        </div>

        {/* Dark Overlay for Readability */}
        <div className="absolute inset-0 bg-black bg-opacity-50"></div>

        {/* Sticky Header */}
        <div className="sticky top-0 left-0 right-0 p-4 border-b border-border z-10">
          <h2 className="text-2xl font-bold text-center">{clan.Name}</h2>
        </div>

        {/* Scrollable Content */}
        <div className="relative z-10 overflow-y-auto max-h-[60vh] p-2">
          <p className="text-sm text-muted text-center mt-1">
            {clan.Description}
          </p>

          {/* Clan Bane */}
          <div className="mt-4">
            <h3 className="text-lg font-semibold text-primary">Clan Bane</h3>
            <p className="text-sm">
              <span className="font-bold">
                {clan["Clan Bane"].split(":")[0]}:
              </span>{" "}
              {clan["Clan Bane"].split(":")[1]}
            </p>
          </div>

          {/* Variant Bane */}
          {clan["Variant Bane"] && (
            <div className="mt-4">
              <h3 className="text-lg font-semibold text-primary">
                Variant Bane
              </h3>
              <p className="text-sm">
              <span className="font-bold">
                {clan["Variant Bane"].split(":")[0]}:
              </span>{" "}
              {clan["Variant Bane"].split(":")[1]}
            </p>
            </div>
          )}

          {/* Disciplines */}
          <div className="mt-4">
            <h3 className="text-lg font-semibold text-primary">Disciplines</h3>
            <p className="text-sm">
              {disciplines.length > 0 ? (
                disciplines.map((discipline) => discipline.Name).join(", ")
              ) : (
                <span className="italic">No disciplines found.</span>
              )}
            </p>
          </div>
        </div>

        {/* Sticky Close Button */}
        <div className="sticky bottom-0 left-0 right-0  p-4 flex justify-end border-t border-border">
          <button
            onClick={onClose}
            className="px-4 py-2 bg-red-600 text-white rounded-lg hover:bg-red-500 transition"
          >
            Close
          </button>
        </div>
      </div>
    </div>
  );
}
