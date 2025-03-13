"use client";

import { useEffect, useState } from "react";
import Image from "next/image";
import ClanModal from "./ClanModal";
import { vtm5_getClanSymbol } from "@/app/helper";
import {
  Clan,
  Discipline,
  DisciplineJunction,
} from "@/data/vtm5_characterCreation";

export default function ClanSelection({
  clans,
  onClanSelect,
  clanSelect,
  isVariant,
  disciplines,
  disciplineJunction,
}: {
  clans: Clan[];
  onClanSelect: (clanId: number) => void;
  clanSelect: number | null;
  isVariant: boolean | undefined;
  disciplines: Discipline[];
  disciplineJunction: DisciplineJunction[];
}) {
  const [selectedClan, setSelectedClan] = useState<Clan | null>(null);
  const [showModal, setShowModal] = useState(false);
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

  function handleMoreInfo(clan: Clan) {
    setSelectedClan(clan);
    setShowModal(true);
  }

  return (
    <div className="container mx-auto px-4">
      <h2 className="text-lg sm:text-xl font-bold text-center mb-4 overflow-scroll">
        Select Your Clan
      </h2>

      {/* Mobile Layout */}
      <div className="sm:hidden flex space-x-4 overflow-x-auto p-4 scrollbar-hide snap-x snap-mandatory no-scrollbar h-96 ">
        {clans.map((clan) => (
          <div
            key={clan.ID}
            className={`relative flex flex-col items-center min-w-48 min-h-[180px] max-h-[180px] my-auto p-4 justify-center rounded-lg border border-gray-300 shadow-md transition hover:shadow-lg cursor-pointer overflow-hidden hover:scale-105 duration-300 ease-in-out ${
              clanSelect === clan.ID
                ? "bg-[var(--color-foreground-soft)]"
                : "bg-[var(--color-background)]"
            } snap-center`}
            onClick={() => onClanSelect(clan.ID)}
          >
            {/* Background Clan Image */}
            <div className="absolute inset-0">
              <Image
                src={vtm5_getClanSymbol(clan.Name)}
                alt={`${clan.Name} Symbol`}
                fill
                className={`object-cover opacity-15 blur-[1px] select-none ${
                  isDarkMode ? "invert" : ""
                }`}
              />
            </div>

            {/* Overlay */}
            <div className="absolute inset-0 bg-black bg-opacity-50"></div>

            {/* Content */}
            <div className="relative z-10 text-center w-full">
              <h3 className="text-base font-semibold text-white">
                {clan.Name}
              </h3>
              <button
                className="mt-2 w-full px-3 py-1 bg-blue-500 text-white rounded-md text-sm"
                onClick={(e) => {
                  e.stopPropagation();
                  handleMoreInfo(clan);
                }}
              >
                More Info
              </button>
            </div>
          </div>
        ))}
      </div>

      {/* Desktop Grid Layout */}
      <div className="hidden sm:grid grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-4 p-6 overflow-scroll">
        {clans.map((clan) => (
          <div
            key={clan.ID}
            className={`relative flex flex-col items-center p-6 rounded-lg border border-gray-300 shadow-md transition hover:shadow-lg cursor-pointer overflow-hidden hover:scale-105 duration-300 ease-in-out ${
              clanSelect === clan.ID
                ? "bg-[var(--color-foreground-soft)]"
                : "bg-[var(--color-background)]"
            }`}
            onClick={() => onClanSelect(clan.ID)}
          >
            {/* Background Clan Image */}
            <div className="absolute inset-0">
              <Image
                src={vtm5_getClanSymbol(clan.Name)}
                alt={`${clan.Name} Symbol`}
                fill
                className={`object-cover opacity-15 blur-[1px] select-none ${
                  isDarkMode && "invert"
                }`}
              />
            </div>

            {/* Overlay */}
            <div className="absolute inset-0 bg-black bg-opacity-40"></div>

            {/* Content */}
            <div className="relative z-10 text-center w-full">
              <h3 className="sm:text-lg font-semibold text-white">
                {clan.Name}
              </h3>
              <button
                className="mt-2 w-full sm:w-auto px-4 py-2 bg-blue-500 text-white rounded-md"
                onClick={(e) => {
                  e.stopPropagation();
                  handleMoreInfo(clan);
                }}
              >
                More Info
              </button>
            </div>
          </div>
        ))}
      </div>

      {/* Modal */}
      {showModal && selectedClan && (
        <div className="fixed inset-0 flex items-center justify-center backdrop-blur-sm bg-opacity-60 z-[110] px-4">
          <ClanModal
            clan={selectedClan}
            disciplines={disciplines.filter((group) =>
              disciplineJunction
                .filter((junc) => junc.clanID === selectedClan.ID)
                .map((junc) => junc.disciplineID)
                .includes(group.ID)
            )}
            onClose={() => setShowModal(false)}
            isVariant={isVariant}
          />
        </div>
      )}
    </div>
  );
}
