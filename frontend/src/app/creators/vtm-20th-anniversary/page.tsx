"use client";

import { fetchData } from "@/app/helper";
import CharactersLibrary from "@/components/components/characterlib/CharacterLibrary";
import V20_Creator from "@/components/components/characterlib/creators/V20_Creator";
import {
  V20Character,
  V20Data,
  V20Clan,
  V20Nature,
  V20Advantage,
  V20Discipline,
  V20SorceryPath,
  V20Background,
  V20MagicType,
} from "@/components/components/characterlib/DataTypes";
import { useSession } from "next-auth/react";
import { useEffect, useState } from "react";

type CharacterItem = {
  id: string;
  name: string;
  subtitle: string;
};

export default function Page() {
  const { status, data: session } = useSession();

  const [charData, setCharData] = useState<V20Character>({} as V20Character);
  const [showModal, setShowModal] = useState(false);
  const [allChars, setAllChars] = useState<CharacterItem[]>([]);
  const [constants, setConstants] = useState<V20Data>({
    nature: [],
    merits: [],
    flaws: [],
    disciplines: [],
    sorcery_paths: [],
    backgrounds: [],
    clan: [],
  });

  const base = process.env.NEXT_PUBLIC_FLASK_API_BASE ?? "";

  // Fetch characters
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

  // Fetch constants (nature, clan, etc.)
  useEffect(() => {
    const loadConstants = async () => {
      const [
        clan_data,
        merit_data,
        flaw_data,
        discipline_data,
        nature_data,
        sorcery_data,
        background_data,
        magic_type,
      ] = await Promise.all([
        fetchData<V20Clan[]>("v20/clan"),
        fetchData<V20Advantage[]>("v20/merit"),
        fetchData<V20Advantage[]>("v20/flaw"),
        fetchData<V20Discipline[]>("v20/discipline"),
        fetchData<V20Nature[]>("v20/nature"),
        fetchData<V20SorceryPath[]>("v20/sorcery"),
        fetchData<V20Background[]>("v20/backgrounds"),
        fetchData<V20MagicType[]>("v20/m_type"),
      ]);

      setConstants({
        nature: nature_data,
        disciplines: discipline_data,
        clan: clan_data,
        merits: merit_data,
        flaws: flaw_data,
        sorcery_paths: sorcery_data,
        backgrounds: background_data,
        magic_types: magic_type,
      });
    };

    loadConstants().catch(console.error);
  }, []);

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
            className="sheet-panel flex flex-col max-h-[90vh] h-[90vh]"
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

            <div className="sheet-panel-body flex-1 min-h-0 flex flex-col overflow-hidden">
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
