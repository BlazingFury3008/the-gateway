"use client";
import { useSession } from "next-auth/react";
import React, { useEffect, useState } from "react";
import Link from "next/link";
import Image from "next/image";
import api from "@/other/axios";
import { vtm5_getClanSymbol } from "@/app/helper";
import Accordion from "@mui/material/Accordion";
import AccordionDetails from "@mui/material/AccordionDetails";
import AccordionSummary from "@mui/material/AccordionSummary";
import {
  character_creation_modes,
  characterCreationOptions,
  optionalRulesSelection,
} from "@/data/vtm5_characterCreation";
import { X } from "lucide-react";

interface Character {
  id: string;
  name: string;
  clan: string;
  generation: number;
  creationDate: string;
  xpSpent: number;
  xpToSpend: number;
}

export default function Page() {
  const { data: session } = useSession();
  const [characters, setCharacters] = useState<Character[]>([]);
  const [displayModal, setDisplayModal] = useState<boolean>(false);
  const [selectedOption, setSelectedOption] = useState<{
    label: string;
    href: string;
  } | null>();
  const [optionalRules, setOptionalRules] = useState<
    { label: string; href: string }[]
  >([]);


  const baseUrl = "/character-creation/vtm5/new-character?mode=";
  const queryParams = `${selectedOption?.href || ""}&&${
    optionalRules.length ? `optional_rules=${optionalRules.map((rule) => rule.href).join("+")}` : ""
  }`;

  useEffect(() => {
    async function fetchCharacters() {
      if (session) {
        try {
          const response = await api.get("data/characters");
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
          onClick={() => setDisplayModal(true)}
          className="px-8 py-4 text-lg font-semibold tracking-wide bg-gradient-to-r from-red-600 to-black text-white rounded-xl shadow-lg transform hover:scale-105 transition duration-300"
        >
          + Create a Character
        </button>
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
      )}
      <div
        className={`fixed inset-0 flex items-center justify-center bg-black bg-opacity-50 transition-opacity backdrop-blur-sm ${
          !displayModal ? "hidden" : "opacity-100"
        }`}
      >
        <div className="bg-[var(--color-background)] border border-[var(--color-border)] rounded-lg shadow-lg p-6 w-[600] flex flex-col items-center space-y-4">
          <div className="flex justify-between w-full">
            <h1>Select Option:</h1>
            <div>
            <button onClick={() => setDisplayModal(false)}>
              <X />
            </button>
            </div>

          </div>
          {character_creation_modes.map((mode, index) => (
            <Link
              key={index}
              className="w-full text-center px-4 py-2 text-lg font-semibold tracking-wide bg-gradient-to-r from-red-600 to-black text-white rounded-xl shadow-lg transform hover:scale-105 transition duration-300"
              href={`${baseUrl}${mode}${queryParams}`}
            >
              {mode === "custom"
                ? "No Restrictions"
                : mode.charAt(0).toUpperCase() + mode.slice(1)}
            </Link>
          ))}

          <Accordion
            className="border border-[var(--color-border)] rounded-lg shadow-md transition-all w-full"
            sx={{
              backgroundColor: "var(--color-background)",
              color: "var(--color-foreground)",
            }}
          >
            {/* Accordion Header */}
            <AccordionSummary className="px-4 py-3 font-semibold hover:bg-[var(--color-border-light)] transition w-full">
              Extra Options
            </AccordionSummary>

            {/* Accordion Content */}
            <AccordionDetails className="px-4 py-3 bg-[var(--color-background-soft)] text-[var(--color-foreground-muted)] transition-all">
              {characterCreationOptions.map((option, key: number) => (
                <div
                  key={key}
                  onClick={() => {
                    if (selectedOption?.label == option.label) {
                      setSelectedOption(null);
                    } else {
                      setSelectedOption(option);
                    }
                  }}
                  className="w-full cursor-pointer mb-1"
                >
                  <input
                    type="checkbox"
                    name=""
                    id=""
                    className="mr-2"
                    checked={selectedOption?.label == option.label}
                    readOnly
                  />
                  {option.label}
                </div>
              ))}
            </AccordionDetails>
          </Accordion>
          <Accordion
            className="border border-[var(--color-border)] rounded-lg shadow-md transition-all w-full"
            sx={{
              backgroundColor: "var(--color-background)",
              color: "var(--color-foreground)",
            }}
          >
            {/* Accordion Header */}
            <AccordionSummary className="px-4 py-3 font-semibold hover:bg-[var(--color-border-light)] transition w-full">
              Optional Rules
            </AccordionSummary>

            {/* Accordion Content */}
            <AccordionDetails className="px-4 py-3 bg-[var(--color-background-soft)] text-[var(--color-foreground-muted)] transition-all">
              {optionalRulesSelection.map((option, key: number) => (
                <div
                  key={key}
                  onClick={() => {
                    if (optionalRules.includes(option)) {
                      setOptionalRules(
                        optionalRules.filter(
                          (rule: { label: string; href: string }) =>
                            rule.href != option.href
                        )
                      );
                    } else {
                      setOptionalRules([...optionalRules, option]);
                    }
                  }}
                  className="w-full cursor-pointer mb-1"
                >
                  <input
                    type="checkbox"
                    name=""
                    id=""
                    className="mr-2"
                    checked={optionalRules.includes(option)}
                    readOnly
                  />
                  {option.label}
                </div>
              ))}
            </AccordionDetails>
          </Accordion>
        </div>
      </div>
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
