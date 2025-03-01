/* eslint-disable @typescript-eslint/no-explicit-any */
"use client";

import { useEffect, useState } from "react";
import Image from "next/image";
import api from "@/other/axios";
import ClanModal from "./ClanModal";
import { vtm5_getClanSymbol } from "@/app/helper";

interface Clan {
  ID: number;
  Name: string;
  "Clan Bane": string;
  "Variant Bane": string;
  Description: string;
}

interface Discipline {
  ID: number;
  Name: string;
  Description: string;
}

export default function ClanSelection({ onClanSelect, clanSelect }: { onClanSelect: (clanId: number) => void, clanSelect: number | null }) {
  const [clans, setClans] = useState<Clan[]>([]);
  const [selectedClan, setSelectedClan] = useState<number | null>(null);
  const [showModal, setShowModal] = useState(false);
  const [disciplines, setDisciplines] = useState<Discipline[]>([]);
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

  // Fetch Clans
  useEffect(() => {
    async function fetchClans() {
      try {
        const response = await api.get("/data/vtm5_clan/");
        setClans(response.data);
      } catch (error) {
        console.error("Error fetching clans:", error);
      }
    }
    fetchClans();
  }, []);

  // Fetch Disciplines for Selected Clan
  async function fetchDisciplines(clanId: number) {
    try {
      const junctionRes = await api.get(`/data/vtm5_clandisciplinejunction/`);
      const disciplineIds = junctionRes.data
        .filter((entry: any) => entry.clanID === clanId)
        .map((entry: any) => entry.disciplineID);

      const disciplinePromises = disciplineIds.map((id: number) => api.get(`/data/vtm5_disciplinegroups/${id}`));
      const disciplineResponses = await Promise.all(disciplinePromises);
      setDisciplines(disciplineResponses.map(res => res.data));
    } catch (error) {
      console.error("Error fetching disciplines:", error);
    }
  }

  function handleMoreInfo(clanId: number) {
    setSelectedClan(clanId);
    fetchDisciplines(clanId);
    setShowModal(true);
  }

  return (
    <div className="container mx-auto p-4 sm:p-6 sm:text-base text-sm">
      <h1 className="text-2xl sm:text-3xl font-bold text-center mb-6">Select Your Clan</h1>

      {/* Clan List */}
      <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-4 sm:gap-2">
        {clans.map((clan, index) => (
          <div
            key={clan.ID}
            className={`relative flex flex-col items-center p-6 rounded-lg border border-gray-300 shadow-md transition hover:shadow-lg cursor-pointer overflow-hidden ${
              clanSelect === clan.ID ? "bg-[var(--color-foreground-soft)]" : "bg-[var(--color-background)]"
            } ${clans.length % 2 === 1 && index === clans.length - 1 ? "sm:col-span-2 md:col-span-1" : ""}`}
            onClick={() => {
              onClanSelect(clan.ID);
              setSelectedClan(clan.ID);
            }}
          >
            {/* Background Clan Image */}
            <div className="absolute inset-0">
              <Image
                src={vtm5_getClanSymbol(clan.Name)}
                alt={`${clan.Name} Symbol`}
                fill
                className={`object-cover opacity-20 blur-[2px] select-none ${isDarkMode && "invert"}`}
              />
            </div>

            {/* Overlay to improve readability */}
            <div className="absolute inset-0 bg-black bg-opacity-40"></div>

            {/* Content (Text & Button) */}
            <div className="relative z-10 text-center w-full">
              <h3 className="text-lg font-semibold text-white">{clan.Name}</h3>
              <button
                className="mt-2 w-full sm:w-auto px-4 py-2 bg-blue-500 text-white rounded-md"
                onClick={(e) => {
                  e.stopPropagation();
                  handleMoreInfo(clan.ID);
                }}
              >
                More Info
              </button>
            </div>
          </div>
        ))}
      </div>

      {/* Modal */}
      {showModal && selectedClan !== null && (
        <ClanModal
          clan={clans.find((clan) => clan.ID === selectedClan)!}
          disciplines={disciplines}
          onClose={() => setShowModal(false)}
        />
      )}
    </div>
  );
}
