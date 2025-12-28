"use client";

import CharactersLibrary from "@/components/components/characterlib/CharacterLibrary";
import V20_Creator from "@/components/components/characterlib/creators/V20_Creator";
import { useSession } from "next-auth/react";
import { useEffect, useState } from "react";

type CharacterItem = {
  id: string;
  name: string;
  subtitle: string;
};

export default function Page() {
  const { status, data: session } = useSession();

  const [charData, setCharData] = useState<Record<string, any>>({});
  const [showModal, setShowModal] = useState(false);
  const [allChars, setAllChars] = useState<CharacterItem[]>([]);

  useEffect(() => {
    // Only fetch once the session is ready and authenticated
    if (status !== "authenticated" || !session?.user) return;

    const getCharacters = async () => {
      try {
        const userId = session.user.id
        if (userId) {

        const res = await fetch(
          `/characters?game=V20&user_id=${encodeURIComponent(userId)}`,
          {
            method: "GET",
            headers: {
              "Content-Type": "application/json",
            },
          }
        );

        if (!res.ok) {
          console.error("Failed to fetch characters:", res.statusText);
          return;
        }

        const tmp_data = await res.json();
        setAllChars(Array.isArray(tmp_data) ? tmp_data : []);
        }

      } catch (err) {
        console.error("Error fetching characters:", err);
      }
    };

    getCharacters();
  }, [status, session]);

  return (
    <div>
      <CharactersLibrary
        title="Vampire: The Masquerade 20th Anniversary"
        itemLabel="Characters"
        onCreate={() => setShowModal(true)}
        items={allChars}
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
