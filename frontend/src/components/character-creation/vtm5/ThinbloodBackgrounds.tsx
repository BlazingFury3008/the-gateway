"use client";

import { ThinbloodBackground } from "@/data/vtm5_characterCreation";
import React, { useState } from "react";
import Accordion from "@/components/Accordion"; // Import custom Accordion

export default function ThinbloodBackgrounds({
  onBackgroundSelect,
  backgroundSelect,
  merits,
  flaws,
}: {
  onBackgroundSelect: (val: { merits: ThinbloodBackground[]; flaws: ThinbloodBackground[] }) => void;
  backgroundSelect: { merits: ThinbloodBackground[]; flaws: ThinbloodBackground[] };
  merits: ThinbloodBackground[];
  flaws: ThinbloodBackground[];
}) {
  const [selectedMerits, setSelectedMerits] = useState<ThinbloodBackground[]>(backgroundSelect.merits);
  const [selectedFlaws, setSelectedFlaws] = useState<ThinbloodBackground[]>(backgroundSelect.flaws);
  const [modalData, setModalData] = useState<ThinbloodBackground | null>(null);
  const [openAccordion, setOpenAccordion] = useState<"merits" | "flaws" | null>(null);

  function toggleAccordion(section: "merits" | "flaws") {
    setOpenAccordion(openAccordion === section ? null : section);
  }

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

    if (updatedMerits.length > 3 || updatedFlaws.length > 3) return; // Max 3 per category

    setSelectedMerits(updatedMerits);
    setSelectedFlaws(updatedFlaws);
    onBackgroundSelect({ merits: updatedMerits, flaws: updatedFlaws });
  }

  return (
    <div className="container mx-auto sm:p-6">
            <h2 className="sm:text-xl text-base sm:font-bold text-center mb-4">
            Select Your Thinblood Merits & Flaws</h2>

      {/* Mobile Layout - Use Accordions */}
      <div className="sm:hidden grid grid-cols-1 md:grid-cols-2 gap-6">
        <Accordion title={`Merits [${selectedMerits.length}]`} isOpen={openAccordion === "merits"} toggle={() => toggleAccordion("merits")}>
          <div className="grid grid-cols-2 md:grid-cols-3 gap-4">
            {merits.map((merit) => (
              <div
                key={merit.ID}
                className={`relative p-4 border rounded-lg cursor-pointer transition-all ${
                  selectedMerits.some((m) => m.ID === merit.ID)
                    ? "border-[var(--color-primary)] bg-[var(--color-primary-light)]"
                    : "border-[var(--color-border)] bg-[var(--color-background)]"
                }`}
                onClick={() => toggleSelection(merit, "merit")}
              >
                <h4 className="font-bold text-xs line-clamp-1">{merit.Name}</h4>
                <button
                  className="text-[var(--color-primary)] underline text-xs md:mt-2"
                  onClick={(e) => {
                    e.stopPropagation();
                    setModalData(merit);
                  }}
                >
                  More Info
                </button>
              </div>
            ))}
          </div>
        </Accordion>

        <Accordion title={`Flaws [${selectedFlaws.length}]`} isOpen={openAccordion === "flaws"} toggle={() => toggleAccordion("flaws")}>
          <div className="grid grid-cols-2 md:grid-cols-3 gap-4">
            {flaws.map((flaw) => (
              <div
                key={flaw.ID}
                className={`relative p-4 border rounded-lg cursor-pointer transition-all ${
                  selectedFlaws.some((f) => f.ID === flaw.ID)
                    ? "border-[var(--color-primary)] bg-[var(--color-primary-light)]"
                    : "border-[var(--color-border)] bg-[var(--color-background)]"
                }`}
                onClick={() => toggleSelection(flaw, "flaw")}
              >
                <h4 className="font-bold text-xs line-clamp-1">{flaw.Name}</h4>
                <button
                  className="text-[var(--color-primary)] underline text-xs md:mt-2"
                  onClick={(e) => {
                    e.stopPropagation();
                    setModalData(flaw);
                  }}
                >
                  More Info
                </button>
              </div>
            ))}
          </div>
        </Accordion>
      </div>

      {/* Desktop Layout - Use Grid */}
      <div className="hidden sm:inline">
        <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
          {/* Merits Section */}
          <div>
            <h3 className="text-lg font-semibold mb-2">Merits</h3>
            <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-2 lg:grid-cols-3 gap-4">
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
                    <h4 className="font-bold  line-clamp-1 md:text-base">{merit.Name}</h4>
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
          <div>
            <h3 className="text-lg font-semibold mb-2">Flaws</h3>
            <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-2 lg:grid-cols-3 gap-4">
              {flaws.map((flaw) => (
                    <div
                    key={flaw.ID}
                    className={`relative p-4 border rounded-lg cursor-pointer transition ${
                      selectedFlaws.some((m) => m.ID === flaw.ID)
                        ? "border-[var(--color-primary)] bg-[var(--color-primary-light)] shadow-md"
                        : "border-[var(--color-border)] bg-[var(--color-background)]"
                    }`}
                    onClick={() => toggleSelection(flaw, "flaw")}
                  >
                    <h4 className="font-bold line-clamp-1">{flaw.Name}</h4>
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
      </div>

      {/* Modal for More Info */}
      {modalData && (
        <div className="fixed inset-0 flex items-center justify-center backdrop-blur-sm p-4">
          <div className="bg-[var(--color-background)] text-[var(--color-foreground)] p-6 rounded-lg shadow-lg w-full max-w-md border border-[var(--color-border)] relative max-h-[90vh] overflow-y-auto">
            <button onClick={() => setModalData(null)} className="absolute top-2 right-2 text-[var(--color-muted)] hover:text-[var(--color-foreground)]">
              ✖
            </button>
            <h2 className="text-xl font-bold">{modalData.Name}</h2>
            <p className="text-xs">{modalData.Description}</p>
            <p className="text-xs mt-2"><span className="font-bold">Reference:</span>{modalData.Reference}</p>
          </div>
        </div>
      )}
    </div>
  );
}
