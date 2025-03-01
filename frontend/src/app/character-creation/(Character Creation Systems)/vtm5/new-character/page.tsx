"use client";

import { useState } from "react";
import ClanSelection from "@/components/character-creation/vtm5/ClanSelection";
import ThinbloodBackgrounds from "@/components/character-creation/vtm5/ThinbloodBackgrounds";

export default function CharacterCreationPage() {
  const [selectedClan, setSelectedClan] = useState<number | null>(null);
  const [page, setPage] = useState<number>(0);

  function handleNextStep() {
    if (page === 0 && selectedClan === null) return; // Prevent advancing if clan is not selected
    if (page === 0) setPage(selectedClan === 16 ? 1 : 2);
    else if (page === 1) setPage(2);
  }

  function handleBackStep() {
    if (page === 2 && selectedClan !== 16) setPage(0);
    else if (page > 0) setPage(page - 1);
  }

  function displayPage() {
    if (page === 0) return <ClanSelection onClanSelect={setSelectedClan} clanSelect={selectedClan} />;
    if (page === 1) return <ThinbloodBackgrounds onNext={() => setPage(2)} />;
    if (page === 2) return <div className="text-center">Next step content goes here...</div>;
    return null;
  }

  return (
    <div className="mx-auto p-6">
      <h1 className="text-3xl font-bold text-center">Character Creation</h1>
      {displayPage()}
      <div className="flex justify-between mt-6">
        <button
          onClick={handleBackStep}
          disabled={page == 0}
          className="px-6 py-3 bg-red-600 text-white rounded-lg shadow-md disabled:bg-gray-400"
        >
          Back
        </button>
        <button
          onClick={handleNextStep}
          disabled={page === 0 && selectedClan === null}
          className="px-6 py-3 bg-red-600 text-white rounded-lg shadow-md disabled:bg-gray-400"
        >
          Next
        </button>
      </div>
    </div>
  );
}
