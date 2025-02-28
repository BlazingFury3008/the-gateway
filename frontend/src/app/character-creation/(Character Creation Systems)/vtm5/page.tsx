"use client";
import { useSession } from "next-auth/react";
import React, { useEffect, useState } from "react";
import Link from "next/link";
import Image from "next/image";
import api from "@/other/axios";
import { vtm5_getClanSymbol } from "@/app/helper";
import { Info } from "lucide-react";
import CharacterCreationPage from "./CharacterCreationPage";

interface Character {
  id: string;
  name: string;
  clan: string;
  generation: number;
  creationDate: string;
  xpSpent: number;
  xpToSpend: number;
}

interface VampireData {
  clan: {
    ID: number;
    Name: string;
    Reference: string;
    "Clan Bane": string;
    "Variant Bane": string;
    Description: string;
  }[];
  clanDisciplines: {
    ID: number;
    clanID: number;
    disciplineID: number;
  }[]
  disciplines: {
    ID: number;
    Name: string;
    Reference: string;
  }[]
}

export default function Page() {
  const { data: session } = useSession();
  const [characters, setCharacters] = useState<Character[]>([]);
  const [defaultCharacters] = useState<Character[]>([
    {
      id: "1",
      name: "Arin the Brave",
      clan: "Ventrue",
      generation: 10,
      creationDate: "",
      xpSpent: 0,
      xpToSpend: 15,
    },
    {
      id: "2",
      name: "Lyra Moonshadow",
      clan: "Tremere",
      generation: 11,
      creationDate: "",
      xpSpent: 0,
      xpToSpend: 15,
    },
  ]);
  const [showGuide, setShowGuide] = useState(false);
  const [characterCreationModal, setCharacterCreationModal] = useState(false);
  const [data, setData] = useState<VampireData | undefined>();

  async function getData() {
    const tmpData: VampireData = {
      clan: [],
      clanDisciplines: [],
      disciplines: {
        ID: 0,
        Name: "",
        Reference: ""
      }
    };
    const clanData = await api.get("/data/vtm5_clan");
    const clanDisciplines = await api.get("/data/vtm5_clandisciplinejunction");
    const disciplines = await api.get("/data/vtm5_disciplinegroups")

    tmpData.clan = clanData.data;
    tmpData.clanDisciplines = clanDisciplines.data
    tmpData.disciplines = disciplines.data

    setData(tmpData);
  }

  useEffect(() => {
    async function fetchCharacters() {
      if (session) {
        try {
          const response = await api.get("/characters");
          setCharacters(response.data);
        } catch (error) {
          console.error("Error fetching characters:", error);
          setCharacters([]);
        }
      } else {
        const storedCharacters = localStorage.getItem("characters");
        if (storedCharacters) {
          setCharacters(JSON.parse(storedCharacters));
        }
      }
    }
    fetchCharacters();
    getData();
  }, [session]);

  return (
    <div className="container mx-auto p-6">
      {/* Header Section */}
      <div className="flex flex-col md:flex-row justify-between items-center mb-6">
        <h1 className="text-3xl font-bold">
          {session ? `Welcome, ${session.user?.name}` : "Your Characters"}
        </h1>
      </div>
      {/* Create Character Button */}
      <div className="mt-6 flex justify-center">
        <button
          onClick={() => setCharacterCreationModal(true)}
          className="px-8 py-4 text-lg font-semibold tracking-wide bg-gradient-to-r from-red-600 to-black text-white rounded-xl shadow-lg transform hover:scale-105 transition duration-300"
        >
          + Create a New Character
        </button>
      </div>
      {/* Enable Guide Checkbox (Moved Below) */}
      <div className="mt-1 flex justify-center">
        <label className="flex items-center space-x-2 text-sm cursor-pointer">
          <input
            type="checkbox"
            checked={showGuide}
            onChange={() => setShowGuide(!showGuide)}
            className="w-5 h-5 text-blue-600 bg-gray-300 border-gray-400 rounded focus:ring-blue-500 cursor-pointer"
          />
          <span className="text-gray-900 dark:text-gray-200">Enable Guide</span>
        </label>
      </div>
      {/* Character Cards Grid */}
      <h2 className="text-center text-lg mt-3">My Characters</h2>
      {characters.length > 0 ? (
        <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-6 mt-6">
          {characters.map((char) => (
            <CharacterCard
              key={char.id}
              char={char}
              onClick={() => alert("Open Character")}
            />
          ))}
        </div>
      ) : (
        <div>
          <p className="text-center p-2 text-[var(--color-foreground-soft)]">
            No Characters Available
          </p>
        </div>
      )}{" "}
      <h2 className="text-center text-lg">Default Characters</h2>
      <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-6 mt-6">
        {defaultCharacters.map((char) => (
          <CharacterCard
            key={char.id}
            char={char}
            onClick={() => alert("Character")}
          />
        ))}
      </div>
      {characterCreationModal && (
        <div
  className="fixed inset-0 flex items-center justify-center bg-black bg-opacity-50 backdrop-blur-sm z-50 p-2 sm:p-6"
  onClick={() => setCharacterCreationModal(false)} // Click outside to close
>
  <div
    className="bg-[var(--color-background)] text-[var(--color-foreground)] border border-[var(--color-border)] shadow-lg rounded-lg w-full h-full sm:max-w-[1200px] sm:h-auto sm:min-h-[600px] flex flex-col 
    transform transition-all modal-enter overflow-hidden"
    onClick={(e) => e.stopPropagation()} // Prevent closing when clicking inside modal
  >
    {/* Modal Header */}
    <div className="flex justify-between items-center p-4 border-b border-[var(--color-border)]">
      <h2 className="text-xl sm:text-2xl font-bold">Create a New Character</h2>
      <button
        onClick={() => setCharacterCreationModal(false)}
        className="text-[var(--color-foreground-soft)] hover:text-[var(--color-foreground-hover)] transition"
      >
        ✖
      </button>
    </div>

    {/* Content Area (Scrollable) */}
    <div className="flex-1 overflow-auto px-4 py-2 sm:p-6">
      <CharacterCreationPage guide={showGuide} data={data} />
      {/* Add Form Here */}
    </div>

    {/* Modal Footer */}
    <div className="p-4 border-t border-[var(--color-border)] text-center">
      <button
        onClick={() => setCharacterCreationModal(false)}
        className="btn btn-danger shadow-md transform hover:scale-105 transition"
      >
        Close
      </button>
    </div>
  </div>
</div>

      )}
    </div>
  );
}

function CharacterCard({
  char,
  onClick,
}: {
  char: Character;
  onClick: () => void;
}) {
 
  return (
    <div
      key={char.id}
      onClick={onClick}
      className="hover:scale-105 cursor-pointer relative p-6 rounded-lg shadow-md overflow-hidden text-white bg-gradient-to-b dark:from-red-900 dark:to-black from-gray-200 to-white transition-all duration-300"
    >
      {/* Background Clan Symbol */}
      <div className="absolute inset-0 opacity-20 dark:opacity-40">
        <Image
          src={vtm5_getClanSymbol(char.clan)}
          alt={`${char.clan} Symbol`}
          layout="fill"
          objectFit="contain"
          className="dark:invert-0 invert"
        />
      </div>

      {/* Foreground Content */}
      <div className="relative z-5">
        <h2 className="text-lg font-semibold">{char.name}</h2>
        <p className="text-gray-300">
          <strong>Clan:</strong> {char.clan}
        </p>
        <p className="text-gray-300">
          <strong>Generation:</strong> {char.generation}th
        </p>
        <p className="text-gray-400 text-sm">
          <strong>Created:</strong>{" "}
          {new Date(char.creationDate).toLocaleDateString()}
        </p>
        <div className="mt-4 flex justify-between items-center text-sm">
          <span className="text-green-400">
            <strong>XP Spent:</strong> {char.xpSpent}
          </span>
          <span className="text-yellow-400">
            <strong>XP Left:</strong> {char.xpToSpend}
          </span>
        </div>
      </div>
    </div>
  );
}

