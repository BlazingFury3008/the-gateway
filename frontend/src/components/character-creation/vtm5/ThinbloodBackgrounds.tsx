"use client";

import api from "@/other/axios";
import React, { useEffect, useState } from "react";

interface ThinbloodBackground {
  ID: number;
  Name: string;
  Description: string;
  Reference: string;
}

export default function ThinbloodBackgrounds({ onNext }: { onNext: () => void }) {
  const [merits, setMerits] = useState<ThinbloodBackground[]>([]);
  const [flaws, setFlaws] = useState<ThinbloodBackground[]>([]);
  const [selectedMerits, setSelectedMerits] = useState<ThinbloodBackground[]>([]);
  const [selectedFlaws, setSelectedFlaws] = useState<ThinbloodBackground[]>([]);
  const [error, setError] = useState<string | null>(null);
  const [modalData, setModalData] = useState<ThinbloodBackground | null>(null);

  useEffect(() => {
    async function fetchBackgrounds() {
      try {
        const flawsResponse = await api.get("/data/vtm5_thinbloodflaws/");
        setFlaws(flawsResponse.data);

        const meritsResponse = await api.get("/data/vtm5_thinbloodmerits/");
        setMerits(meritsResponse.data);
      } catch (error) {
        console.error("Error fetching thinblood backgrounds:", error);
      }
    }
    fetchBackgrounds();
  }, []);

  function toggleSelection(item: ThinbloodBackground, type: "merit" | "flaw") {
    let updatedMerits = [...selectedMerits];
    let updatedFlaws = [...selectedFlaws];

    if (type === "merit") {
      updatedMerits = updatedMerits.some((m) => m.ID === item.ID)
        ? updatedMerits.filter((m) => m.ID !== item.ID) // Deselect
        : [...updatedMerits, item]; // Select
    } else {
      updatedFlaws = updatedFlaws.some((f) => f.ID === item.ID)
        ? updatedFlaws.filter((f) => f.ID !== item.ID)
        : [...updatedFlaws, item];
    }

    // Ensure max selection of 3 per category
    if (updatedMerits.length > 3 || updatedFlaws.length > 3) return;

    setSelectedMerits(updatedMerits);
    setSelectedFlaws(updatedFlaws);
  }

  function validateSelection() {
    if (selectedMerits.length < 1 || selectedFlaws.length < 1) {
      setError("You must select at least one merit and one flaw.");
      return false;
    }
    if (selectedMerits.length !== selectedFlaws.length) {
      setError("You must have the same number of merits and flaws.");
      return false;
    }
    setError(null);
    return true;
  }

  return (
    <div className="container mx-auto p-6">
      <h2 className="text-2xl font-bold text-center mb-4">Select Your Thinblood Merits & Flaws</h2>
      {error && <p className="text-[var(--color-destructive)] text-center mb-4">{error}</p>}

      <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
        {/* Merits Section */}
        <div>
          <h3 className="text-lg font-semibold mb-2">Merits</h3>
          <div className="grid grid-cols-1 sm:grid-cols-3 gap-4">
            {merits.map((merit) => (
              <div
                key={merit.ID}
                className={`relative p-4 border rounded-lg cursor-pointer transition ${
                  selectedMerits.some((m) => m.ID === merit.ID)
                    ? "border-[var(--color-primary)] bg-[var(--color-primary-light)] shadow-md"
                    : "border-[var(--color-border)] bg-[var(--color-background)]"
                }`}
                onClick={() => toggleSelection(merit, "merit")}
              >
                <h4 className="font-bold">{merit.Name}</h4>
                <div className="flex justify-between mt-2">
                  <button
                    className="text-[var(--color-primary)] underline text-sm"
                    onClick={(e) => {
                      e.stopPropagation();
                      setModalData(merit);
                    }}
                  >
                    More Info
                  </button>
                </div>
              </div>
            ))}
          </div>
        </div>

        {/* Flaws Section */}
        <div>
          <h3 className="text-lg font-semibold mb-2">Flaws</h3>
          <div className="grid grid-cols-1 sm:grid-cols-3 gap-4">
            {flaws.map((flaw) => (
              <div
                key={flaw.ID}
                className={`relative p-4 border rounded-lg cursor-pointer transition ${
                  selectedFlaws.some((f) => f.ID === flaw.ID)
                    ? "border-[var(--color-primary)] bg-[var(--color-primary-light)] shadow-md"
                    : "border-[var(--color-border)] bg-[var(--color-background)]"
                }`}
                onClick={() => toggleSelection(flaw, "flaw")}
              >
                <h4 className="font-bold text-ellipsis line-clamp-1">{flaw.Name}</h4>
                <div className="flex justify-between mt-2">
                  <button
                    className="text-[var(--color-primary)] underline text-sm"
                    onClick={(e) => {
                      e.stopPropagation();
                      setModalData(flaw);
                    }}
                  >
                    More Info
                  </button>
                </div>
              </div>
            ))}
          </div>
        </div>
      </div>

      {/* Modal for More Info */}
      {modalData && (
        <div className="fixed inset-0 flex items-center justify-center bg-black bg-opacity-50 px-4">
          <div className="bg-[var(--color-background)] text-[var(--color-foreground)] p-6 rounded-lg shadow-lg w-full max-w-md border border-[var(--color-border)] relative">
            <button
              onClick={() => setModalData(null)}
              className="absolute top-2 right-2 text-[var(--color-muted)] hover:text-[var(--color-foreground)]"
            >
              ✖
            </button>
            <h2 className="text-xl font-bold">{modalData.Name}</h2>
            <p className="mt-2 text-sm">{modalData.Description}</p>
            <p className="mt-2 text-xs text-[var(--color-muted)]">
              <strong>Reference:</strong> {modalData.Reference}
            </p>
          </div>
        </div>
      )}
    </div>
  );
}
