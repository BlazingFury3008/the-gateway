"use client";

import React, { useEffect, useState } from "react";
import SelectionBox from "@/components/character-creation/SelectionBox";
import { gameSystems } from "./gameSystems";

export default function CharacterCreationPage() {
  const [filterText, setFilterText] = useState("");
  const [filterEnabled, setFilterEnabled] = useState(false);
  const [filterSelection, setFilterSelections] = useState(gameSystems);

  useEffect(() => {
    let filteredSystems = gameSystems;

    if (filterText.trim() !== "") {
      filteredSystems = filteredSystems.filter((val) =>
        val.title.toLowerCase().includes(filterText.toLowerCase())
      );
    }

    if (filterEnabled) {
      filteredSystems = filteredSystems.filter((val) => val.enabled);
    }

    setFilterSelections(filteredSystems);
  }, [filterText, filterEnabled]);

  return (
    <div className="min-h-screen py-12 px-6 bg-[var(--color-background-soft)] text-[var(--color-foreground)] transition-colors duration-300">
      <div className="max-w-6xl mx-auto">
        <h1 className="text-3xl sm:text-4xl font-bold text-center mb-6">
          Character Creation
        </h1>
        <p className="text-lg text-center text-[var(--color-foreground-soft)] mb-8">
          Search and select a game system to start creating your character.
        </p>

        {/* SEARCH INPUT AND FILTER TOGGLE */}
        <div className="flex flex-col sm:flex-row items-center justify-center mb-10 gap-4">
          <input
            type="text"
            value={filterText}
            onChange={(e) => setFilterText(e.target.value)}
            placeholder="Search game systems..."
            className="w-full max-w-lg px-4 py-3 text-lg bg-[var(--color-form)] border border-[var(--color-border)] rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-[var(--color-primary)] transition-all duration-200"
          />
          <label className="flex items-center gap-2 text-lg">
            <input
              type="checkbox"
              checked={filterEnabled}
              onChange={(e) => setFilterEnabled(e.target.checked)}
              className="w-5 h-5 text-[var(--color-primary)] bg-[var(--color-form)] border border-[var(--color-border)] rounded focus:ring-2 focus:ring-[var(--color-primary)] cursor-pointer transition-all duration-200"
            />
            Show only available
          </label>
        </div>

        {/* GAME SYSTEM GRID OR MESSAGE */}
        {filterSelection.length > 0 ? (
          <div
            className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-8 opacity-100 animate-fade-in"
            style={{ animationDelay: "0.2s" }}
          >
            {filterSelection.map((system, index) => (
              <SelectionBox
                key={index}
                title={system.title}
                description={system.description}
                icon={system.icon}
                link={system.link}
                bgColor={system.bgColor}
                enabled={system.enabled}
              />
            ))}
          </div>
        ) : (
          <p className="text-center text-lg text-[var(--color-foreground-soft)]">
            No matching game systems found.
          </p>
        )}
      </div>
    </div>
  );
}
