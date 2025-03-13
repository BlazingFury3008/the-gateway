import { Clan, ThinbloodBackground } from "@/data/vtm5_characterCreation";
import React, { useEffect, useState } from "react";

export default function ClanBaneSelection({
  selectedClan,
  clans,
  thinbloodAdv,
  isVariant,
  setSelectedBane,
  selectedBane,
}: {
  selectedClan: number | null;
  clans: Clan[];
  thinbloodAdv: { merits: ThinbloodBackground[]; flaws: ThinbloodBackground[] };
  isVariant: boolean | undefined;
  setSelectedBane: (bane: string) => void;
  selectedBane: string;
}) {
  // Initialize selected clan bane correctly
  const [selectedClanBane, setSelectedClanBane] = useState<Clan | null>(() => {
    if (selectedClan === null) return null;
    if (selectedClan === 15 || selectedClan === 16) {
      return clans.find(
        (clan) => (clan["Clan Bane"] === selectedBane || clan["Variant Bane"] === selectedBane) && clan.ID != 16 && clan.ID != 15
      ) || null;
    }
    return clans.find((clan) => clan.ID === selectedClan) || null;
  });

  const [selectedBaneType, setSelectedBaneType] = useState<"Standard" | "Variant">(selectedClanBane?.["Variant Bane"] == selectedBane ? "Variant" : "Standard");
  const [dropdownOptions, setDropdownOptions] = useState<Clan[]>([]);

  // Update dropdown options when selected clan changes
  useEffect(() => {
    setDropdownOptions(
      clans.filter((clan) => {
        if (clan.ID === 15 || clan.ID === 16) return false;

        if (selectedClan === 16) {
          const hasBeastialTemper = thinbloodAdv.flaws.some((flaw) => flaw.Name === "Beastial Temper");
          const hasCatenatingBlood = thinbloodAdv.merits.some((merit) => merit.Name === "Catenating Blood");

          if (!hasBeastialTemper && [1, 2, 3].includes(clan.ID)) return false;
          if (!hasCatenatingBlood && clan.ID === 12) return false;
        }

        return true;
      })
    );
  }, [selectedClan, thinbloodAdv, clans]);

  // Update selected clan bane when the selectedClan changes
  useEffect(() => {
    if (selectedClan === null) {
      setSelectedClanBane(null);
      return;
    }

    if (selectedClan === 15 || selectedClan === 16) {
      setSelectedClanBane(
        clans.find((clan) => clan["Clan Bane"] === selectedBane || clan["Variant Bane"] === selectedBane) || null
      );
    } else {
      setSelectedClanBane(clans.find((clan) => clan.ID === selectedClan) || null);
    }
  }, [selectedClan, selectedBane, clans]);

  useEffect(() => {
    if (
      selectedBane !== selectedClanBane?.["Clan Bane"] &&
      selectedBane !== selectedClanBane?.["Variant Bane"]
    ) {
      setSelectedBane(selectedClanBane?.["Clan Bane"] || ""); // Default to Standard Bane if available
      setSelectedBaneType("Standard"); // Ensure the type is reset to Standard
    }
  }, [selectedClanBane]);
  

  return (
    <div className="container mx-auto flex flex-col items-center px-4">
      <h2 className="text-lg sm:text-xl font-bold text-center mb-4">
        Select Your Clan Bane
      </h2>

      {/* Clan Dropdown Selection (Visible for Thinblood & Caitiff) */}
      {(selectedClan === 15 || selectedClan === 16) && (
        <div className="w-full flex flex-col items-center">
          <ClanDropdown
            dropdownOptions={dropdownOptions}
            selectedClan={selectedClanBane}
            onSelect={setSelectedClanBane}
          />
        </div>
      )}

      {/* Clan Bane Details (Only Show if a Bane is Selected) */}
      {selectedClanBane && (
        <div className="mt-4 bg-[var(--color-background)] p-6 rounded-lg shadow-lg text-[var(--color-foreground)] w-full max-w-sm sm:max-w-lg">
          {/* Standard vs. Variant Bane Selection */}
          {isVariant && (
            <div className="flex justify-center gap-2 sm:gap-4 mb-4">
              <button
                className={`btn ${
                  selectedBaneType === "Standard"
                    ? "btn-primary"
                    : "bg-[var(--color-background-soft)] text-[var(--color-foreground)]"
                }`}
                onClick={() => {
                  setSelectedBaneType("Standard");
                  setSelectedBane(selectedClanBane["Clan Bane"]);
                }}
              >
                Standard Bane
              </button>
              {selectedClanBane["Variant Bane"] != "" && selectedClanBane != null && (<button
                className={`btn ${
                  selectedBaneType === "Variant"
                    ? "btn-primary"
                    : "bg-[var(--color-background-soft)] text-[var(--color-foreground)]"
                }`}
                onClick={() => {
                  setSelectedBaneType("Variant");
                  setSelectedBane(selectedClanBane["Variant Bane"]);
                }}
              >
                Variant Bane
              </button>)}
            </div>
          )}

          {/* Bane Description */}
          <div className="max-h-[28vh] sm:max-h-[40vh] overflow-auto p-3 bg-[var(--color-background-soft)] rounded-md">
            <div className="font-bold text-[var(--color-foreground)] text-sm sm:text-base">
              {selectedBaneType === "Standard"
                ? selectedClanBane["Clan Bane"]?.split(":")[0]
                : selectedClanBane["Variant Bane"]?.split(":")[0]}
            </div>
            <div className="text-[var(--color-foreground-soft)] text-xs sm:text-sm">
              {selectedBaneType === "Standard"
                ? selectedClanBane["Clan Bane"]?.split(":")[1]
                : selectedClanBane["Variant Bane"]?.split(":")[1]}
            </div>
          </div>
        </div>
      )}
    </div>
  );
}

// Dropdown Component
interface ClanDropdownProps {
  dropdownOptions: Clan[];
  selectedClan: Clan | null;
  onSelect: (clan: Clan) => void;
}

function ClanDropdown({ dropdownOptions, selectedClan, onSelect }: ClanDropdownProps) {
  const [isOpen, setIsOpen] = useState(false);
  const [search, setSearch] = useState("");

  const filteredClans = dropdownOptions.filter((clan) =>
    clan.Name.toLowerCase().includes(search.toLowerCase())
  );

  return (
    <div className="relative w-full max-w-xs sm:max-w-sm flex flex-col items-center">
      <button
        className="w-full btn bg-[var(--color-background-soft)] text-[var(--color-foreground)] border border-[var(--color-border)] flex justify-between items-center shadow-md"
        onClick={() => setIsOpen(!isOpen)}
      >
        {selectedClan ? selectedClan.Name : "Select a Clan"}
        <span className={`transition-transform ${isOpen ? "rotate-180" : "rotate-0"}`}>▼</span>
      </button>

      {isOpen && (
        <div className="absolute left-0 mt-1 w-full bg-[var(--color-background)] border border-[var(--color-border)] rounded-md shadow-lg max-h-60 overflow-y-auto z-10 p-2 no-scrollbar">
          <input
            type="text"
            placeholder="Search clan..."
            value={search}
            onChange={(e) => setSearch(e.target.value)}
            className="input mb-2"
          />

          <ul className="text-[var(--color-foreground)] text-sm">
            {filteredClans.length > 0 ? (
              filteredClans.map((clan) => (
                <li
                  key={clan.ID}
                  className={`px-4 py-2 cursor-pointer hover:bg-[var(--color-background-hover)] rounded-md ${
                    selectedClan?.ID === clan.ID ? "bg-[var(--color-background-hover)]" : ""
                  }`}
                  onClick={() => {
                    onSelect(clan);
                    setSearch("");
                    setIsOpen(false);
                  }}
                >
                  {clan.Name}
                </li>
              ))
            ) : (
              <li className="px-4 py-2 text-gray-500">No clans found</li>
            )}
          </ul>
        </div>
      )}
    </div>
  );
}
