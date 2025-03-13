"use client";

import Accordion from "@/components/Accordion";
import { CaitiffBackground } from "@/data/vtm5_characterCreation";
import React, { useEffect, useState } from "react";

export default function CaitiffBackgrounds({
  onBackgroundSelect,
  backgroundSelect,
  totalMerits,
  totalFlaws,
  merits,
  flaws
}: {
  onBackgroundSelect: (val: {
    merits: CaitiffBackground[];
    flaws: CaitiffBackground[];
  }) => void;
  backgroundSelect: {
    merits: CaitiffBackground[];
    flaws: CaitiffBackground[];
  };
  totalMerits: number;
  totalFlaws: number;
  merits: CaitiffBackground[];
  flaws: CaitiffBackground[];
}) {
  const [selectedMerits, setSelectedMerits] = useState<CaitiffBackground[]>(
    backgroundSelect.merits
  );
  const [selectedFlaws, setSelectedFlaws] = useState<CaitiffBackground[]>(
    backgroundSelect.flaws
  );
  const [modalData, setModalData] = useState<CaitiffBackground | null>(null);
  const [openAccordion, setOpenAccordion] = useState<"merits" | "flaws" | null>(null);

  function toggleAccordion(section: "merits" | "flaws") {
    setOpenAccordion(openAccordion === section ? null : section);
  }


  function toggleSelection(item: CaitiffBackground, type: "merit" | "flaw", disabled? : boolean | null) {
    let updatedMerits = [...selectedMerits];
    let updatedFlaws = [...selectedFlaws];

    if (type === "merit") {
      updatedMerits = updatedMerits.some((m) => m.ID === item.ID)
        ? updatedMerits.filter((m) => m.ID !== item.ID) // Deselect
        : disabled == false ? [...updatedMerits, item] : updatedMerits // Select
    } else {
      updatedFlaws = updatedFlaws.some((f) => f.ID === item.ID)
        ? updatedFlaws.filter((f) => f.ID !== item.ID)
        : [...updatedFlaws, item];
    }

    setSelectedMerits(updatedMerits);
    setSelectedFlaws(updatedFlaws);
    onBackgroundSelect({merits: updatedMerits, flaws: updatedFlaws});
  }

  useEffect(() => {
    if(backgroundSelect.merits != merits)
    {
      setSelectedMerits(backgroundSelect.merits)
    }
  }, [backgroundSelect])

  return (
    <div className="container mx-auto sm:p-6">
      <h2 className="sm:text-2xl text-base font-bold text-center">
        Select Your Caitiff Merits & Flaws (Optional)
      </h2>
      <h2 className="text-sm text-center mb-4">
            These will be counted against your total Merits & Flaws
      </h2>

{/* Desktop View */}
      <div className="hidden sm:grid grid-cols-1 md:grid-cols-2 gap-6">
        {/* Merits Section */}
        <div>
          <h3 className="text-lg font-semibold mb-2">Merits [{totalMerits}]</h3>
          <div className="grid grid-cols-1 sm:grid-cols-3 gap-4">
            {merits.map((merit) => 
            {
                const disabled = totalMerits - parseInt(merit.Values) < 0 && !backgroundSelect.merits.find((val) => val.ID == merit.ID);

                return    (
                    <div
                      key={merit.ID}
                      className={`relative p-4 border rounded-lg ${!disabled && "cursor-pointer"} transition ${
                        selectedMerits.some((m) => m.ID === merit.ID)
                          ? "border-[var(--color-primary)] bg-[var(--color-primary-light)] shadow-md"
                          : "border-[var(--color-border)] bg-[var(--color-background)]"
                      }`}
                      onClick={() => toggleSelection(merit, "merit", disabled)}
                    >
                      <h4 className="font-bold">{merit.Name} [{merit.Values}]</h4>
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
                  )
            }
         )}
          </div>
        </div>

        {/* Flaws Section */}
        <div>
          <h3 className="text-lg font-semibold mb-2">Flaws [{totalFlaws}]</h3>
          <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
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
                <h4 className="font-bold text-ellipsis line-clamp-1">
                  {flaw.Name} [{flaw.Values}]
                </h4>
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

{/* Mobile View */}

      <div className="sm:hidden space-y-3">
        {/* Merits Section */}
        <Accordion title={`Merits [${totalMerits}]`} isOpen={openAccordion === "merits"} toggle={() => toggleAccordion("merits")}>
        <div className="grid grid-cols-1 sm:grid-cols-2 gap-4 max-h-[40vh]">
        {merits.map((merit) => 
            {
                const disabled = totalMerits - parseInt(merit.Values) < 0 && !backgroundSelect.merits.find((val) => val.ID == merit.ID);

                return    (
                    <div
                      key={merit.ID}
                      className={`relative p-4 border rounded-lg ${!disabled && "cursor-pointer"} transition ${
                        selectedMerits.some((m) => m.ID === merit.ID)
                          ? "border-[var(--color-primary)] bg-[var(--color-primary-light)] shadow-md"
                          : "border-[var(--color-border)] bg-[var(--color-background)]"
                      }`}
                      onClick={() => toggleSelection(merit, "merit", disabled)}
                    >
                      <h4 className="font-bold text-xs line-clamp-1 text-ellipsis">{merit.Name} </h4>
                      <h4 className="text-xs text-center">[{merit.Values}]</h4>
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
                  )
            }
         )}
          </div>
        </Accordion>
        {/* Flaws Section */}
        <Accordion title={`Flaws [${totalFlaws}]`} isOpen={openAccordion === "flaws"} toggle={() => toggleAccordion("flaws")}>
          <div className="grid grid-cols-1 sm:grid-cols-2 gap-4 max-h-[40vh]">
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
                      <h4 className="font-bold text-xs line-clamp-1">{flaw.Name} [{flaw.Values}]</h4>
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
        </Accordion>
      </div>

      {/* Modal for More Info */}
      {modalData && (
        <div className="fixed inset-0 flex items-center justify-center backdrop-blur-sm px-4 transition-all duration-200">
          <div className="bg-[var(--color-background)] text-[var(--color-foreground)] p-6 rounded-lg shadow-lg w-full max-w-md border border-[var(--color-border)] relative">
            <button
              onClick={() => setModalData(null)}
              className="absolute top-2 right-2 text-[var(--color-muted)] hover:text-[var(--color-foreground)]"
            >
              ✖
            </button>
            <h2 className="text-xl font-bold">{modalData.Name}</h2>
            <p className="mt-2 text-sm">{modalData.Description}</p>
          </div>
        </div>
      )}
    </div>
  );
}
