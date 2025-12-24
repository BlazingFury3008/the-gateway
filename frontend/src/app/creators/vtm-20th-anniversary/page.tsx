"use client";

import CharactersLibrary from "@/components/components/characterlib/CharacterLibrary";
import V20_Creator from "@/components/components/characterlib/creators/V20_Creator";
import { useSession } from "next-auth/react";
import { useState } from "react";

export default function Page() {
  const { status } = useSession();
  const localStorageKey = "V20";

  const [charData, setCharData] = useState({})

  const [showModal, setShowModal] = useState(false);

  return (
    <div>
      <CharactersLibrary
        title={"Vampire: The Masquerade 20th Anniversary"}
        itemLabel="Characters"
        onCreate={() => setShowModal(true)}
        items={[]}
        example_items={[
          {
            name: "Aristos",
            subtitle: "Clan Tremere • 13th Generation",
            id: "1",
          },
        ]}
        onViewItem={() => alert("View")}
        onEditItem={() => alert("Edit")}
        onDeleteItem={() => alert("Delete")}
        onCopyItem={() => alert("Copy")}
      />

      {showModal && (
        <div
          className="sheet-backdrop"
          onClick={() => setShowModal(false)}
        >
          <div
            className="sheet-panel flex flex-col"
            onClick={(e) => e.stopPropagation()}
          >
            {/* HEADER */}
            <div className="sheet-panel-header">
              <h2 className="sheet-panel-title">Create Character</h2>
              <button
                type="button"
                className="sheet-panel-close"
                onClick={() => setShowModal(false)}
              >
                ✕
              </button>
            </div>

            {/* BODY – this must give height to V20_Creator */}
            <div className="sheet-panel-body flex-1 flex flex-col overflow-hidden">
              <V20_Creator
                data={{}}
                charData={charData}
                setCharData={setCharData}
                onCancel={() => setShowModal(false)}
              />
            </div>
          </div>
        </div>
      )}
    </div>
  );
}
