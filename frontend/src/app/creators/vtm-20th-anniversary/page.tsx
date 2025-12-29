"use client";

import CharactersLibrary from "@/components/components/characterlib/CharacterLibrary";
import V20_Creator from "@/components/components/characterlib/creators/V20_Creator";
import { V20_Character, V20_Data } from "@/components/components/characterlib/DataTypes";
import { useSession } from "next-auth/react";
import { useEffect, useState } from "react";

type CharacterItem = {
  id: string;
  name: string;
  subtitle: string;
};

export default function Page() {
  const { status, data: session } = useSession();

  const [charData, setCharData] = useState<V20_Character>({});
  const [showModal, setShowModal] = useState(false);
  const [allChars, setAllChars] = useState<CharacterItem[]>([]);
  const [constants, setConstants] = useState<V20_Data>({
    nature: [],
  });

  const base = process.env.NEXT_PUBLIC_FLASK_API_BASE ?? "";

  useEffect(() => {
    if (status !== "authenticated" || !session?.user) return;
    if (!base) {
      console.error("NEXT_PUBLIC_FLASK_API_BASE is not set");
      return;
    }

    const getCharacters = async () => {
      try {
        const userId = (session.user as { id?: string }).id;
        if (!userId) return;

        const res = await fetch(
          `${base}/characters?game=V20&user_id=${encodeURIComponent(userId)}`,
          {
            method: "GET",
            headers: {
              "Content-Type": "application/json",
              "X-API-Key": process.env.NEXT_PUBLIC_DATA_API_KEY ?? "",
            },
          }
        );

        if (!res.ok) {
          console.error("Failed to fetch characters:", res.statusText);
          return;
        }

        const tmp_data = (await res.json()) as unknown;

        if (Array.isArray(tmp_data)) {
          setAllChars(tmp_data as CharacterItem[]);
        } else {
          setAllChars([]);
        }
      } catch (err) {
        console.error("Error fetching characters:", err);
      }
    };

    void getCharacters();
  }, [status, session, base]);

  useEffect(() => {
    if (!base) {
      console.error("NEXT_PUBLIC_FLASK_API_BASE is not set");
      return;
    }

    const fetchConstants = async () => {
      try {
        const natures = await fetch(`${base}/data/v20/nature`, {
          method: "GET",
          headers: {
            "Content-Type": "application/json",
            "X-API-Key": process.env.NEXT_PUBLIC_DATA_API_KEY ?? "",
          },
        }).then((res) => res.json());

        console.log("Fetched natures:", natures);

        const tmp = {
          nature: natures,
        };

        setConstants(tmp);
      } catch (err) {
        console.error("Error fetching constants:", err);
      }
    };

    void fetchConstants();
  }, [base]);

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
        <div className="sheet-backdrop" onClick={() => setShowModal(false)}>
          <div
            className="sheet-panel flex flex-col"
            onClick={(e) => e.stopPropagation()}
          >
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

            <div className="sheet-panel-body flex-1 flex flex-col overflow-hidden">
              <V20_Creator
                data={constants}
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
