"use client";

import React, { useMemo, useState } from "react";
import { useRouter } from "next/navigation";
import { FaSearch, FaCog } from "react-icons/fa";

type V20Character = {
  id: string;
  name: string;
  clan: string;
  concept?: string;
  chronicle?: string;
  sect?: string;
  nature?: string;
  demeanor?: string;
  generation?: string; // e.g. "10th"
  lastUpdated?: string; // display or ISO-ish
  isExample: boolean;
  portraitUrl?: string;
  bannerUrl?: string;
};

function useAuth() {
  // Replace with your real auth/session hook
  return { isSignedIn: true };
}

type SortKey = "nameAsc" | "updatedDesc" | "clanAsc";

export default function V20CharactersPage() {
  const router = useRouter();
  const { isSignedIn } = useAuth();

  // Replace with API results
  const allCharacters: V20Character[] = [
    {
      id: "1",
      name: "Lucien Blackwood",
      clan: "Toreador",
      concept: "Decadent Artist",
      chronicle: "The Gateway",
      sect: "Camarilla",
      nature: "Bon Vivant",
      demeanor: "Gallant",
      generation: "11th",
      lastUpdated: "2025-12-12",
      isExample: false,
      portraitUrl: "/images/portraits/lucien.png",
      bannerUrl: "/images/banners/vtm-1.jpg",
    },
    {
      id: "2",
      name: "Mirela Vance",
      clan: "Tremere",
      concept: "Occult Scholar",
      chronicle: "NOLA Chantry",
      sect: "Camarilla",
      nature: "Architect",
      demeanor: "Pedant",
      generation: "10th",
      lastUpdated: "2025-12-01",
      isExample: false,
      portraitUrl: "/images/portraits/mirela.png",
      bannerUrl: "/images/banners/vtm-2.jpg",
    },
    {
      id: "ex-1",
      name: "Sebastian Crowe",
      clan: "Ventrue",
      concept: "Corporate Tyrant",
      chronicle: "Example",
      sect: "Camarilla",
      nature: "Director",
      demeanor: "Judge",
      generation: "9th",
      lastUpdated: "2025-10-20",
      isExample: true,
      portraitUrl: "/images/portraits/sebastian.png",
      bannerUrl: "/images/banners/vtm-3.jpg",
    },
  ];

  const [query, setQuery] = useState("");
  const [sortKey, setSortKey] = useState<SortKey>("updatedDesc");

  const characters = useMemo(() => {
    const q = query.trim().toLowerCase();

    let filtered = !q
      ? allCharacters
      : allCharacters.filter((c) => {
          const hay = [
            c.name,
            c.clan,
            c.concept ?? "",
            c.chronicle ?? "",
            c.sect ?? "",
            c.nature ?? "",
            c.demeanor ?? "",
            c.generation ?? "",
            c.isExample ? "example" : "",
          ]
            .join(" ")
            .toLowerCase();

          return hay.includes(q);
        });

    filtered = [...filtered].sort((a, b) => {
      if (sortKey === "nameAsc") return a.name.localeCompare(b.name);
      if (sortKey === "clanAsc") return a.clan.localeCompare(b.clan);
      // updatedDesc default
      return (b.lastUpdated ?? "").localeCompare(a.lastUpdated ?? "");
    });

    return filtered;
  }, [query, sortKey, allCharacters]);

  const openCharacter = (id: string) =>
    router.push(`/creators/vtm-20th-anniversary/character/${id}`);

  return (
    <div className="section section-light characters-shell">
      <div className="characters-wrap">
        {/* Header */}
        <div className="characters-header">
          <div>
            <h1 className="characters-title">
              Vampire: The Masquerade 20th Anniversary
            </h1>

            <div className="characters-subline">
              <span>Characters:</span>
              <a href="#">75/Unlimited</a>
            </div>
          </div>

          <div className="characters-actions">
            {isSignedIn && (
              <button
                className="hero-button"
                onClick={() =>
                  router.push("/creators/vtm-20th-anniversary/create")
                }
              >
                CREATE A CHARACTER
              </button>
            )}

            <a className="characters-download" href="#">
              ↓ Download a blank character sheet
            </a>
          </div>
        </div>

        {/* Controls */}
        <div className="characters-controls">
          <div className="characters-controls-row">
            <div className="characters-search">
              <div className="search-wrap">
                <FaSearch className="search-icon" />
                <input
                  value={query}
                  onChange={(e) => setQuery(e.target.value)}
                  placeholder="Search by Name, Clan, Sect, Chronicle, Concept..."
                />
              </div>
            </div>

            <div className="characters-sort">
              <label>Sort By</label>
              <select
                value={sortKey}
                onChange={(e) => setSortKey(e.target.value as SortKey)}
              >
                <option value="updatedDesc">Updated: Newest</option>
                <option value="nameAsc">Name: A to Z</option>
                <option value="clanAsc">Clan: A to Z</option>
              </select>

              <button
                type="button"
                className="characters-settings"
                onClick={() => console.log("Settings")}
              >
                <FaCog />
                Settings
              </button>
            </div>
          </div>
        </div>

        {/* Grid */}
        <div className="character-grid">
          {characters.map((c) => (
            <CharacterTile
              key={c.id}
              character={c}
              onView={() => openCharacter(c.id)}
              onEdit={() =>
                router.push(
                  `/creators/vtm-20th-anniversary/character/${c.id}/edit`
                )
              }
              onCopy={() => console.log("Copy", c.id)}
              onDelete={() => console.log("Delete", c.id)}
            />
          ))}
        </div>
      </div>
    </div>
  );
}

function CharacterTile({
  character,
  onView,
  onEdit,
  onCopy,
  onDelete,
}: {
  character: V20Character;
  onView: () => void;
  onEdit: () => void;
  onCopy: () => void;
  onDelete: () => void;
}) {
  const subtitle = useMemo(() => {
    // Compact, V20-relevant line under the name (still reads like the screenshot)
    const left = [
      character.clan,
      character.sect ? `• ${character.sect}` : null,
      character.generation ? `• ${character.generation} Gen` : null,
    ]
      .filter(Boolean)
      .join(" ");

    const right = [
      character.concept ? `— ${character.concept}` : null,
      character.chronicle ? `• ${character.chronicle}` : null,
      character.lastUpdated ? `• Updated ${character.lastUpdated}` : null,
    ]
      .filter(Boolean)
      .join(" ");

    return [left, right].filter(Boolean).join(" ");
  }, [character]);

  return (
    <div className="character-tile">
      <div
        className="character-banner"
        style={
          character.bannerUrl
            ? { backgroundImage: `url(${character.bannerUrl})` }
            : undefined
        }
      >
        <div className="character-banner-content">
          <Portrait name={character.name} src={character.portraitUrl} />
          <div className="character-meta">
            <div className="character-name">{character.name}</div>
            <div className="character-subtitle">{subtitle}</div>
          </div>

          {character.isExample ? (
            <div
              style={{
                marginLeft: "auto",
                fontSize: 12,
                fontWeight: 800,
                color: "rgba(255,255,255,0.85)",
                border: "1px solid rgba(255,255,255,0.25)",
                borderRadius: 6,
                padding: "4px 8px",
                background: "rgba(0,0,0,0.15)",
              }}
            >
              EXAMPLE
            </div>
          ) : null}
        </div>
      </div>

      <div className="character-actions">
        <button className="character-action" onClick={onView} type="button">
          VIEW
        </button>
        <button className="character-action" onClick={onEdit} type="button">
          EDIT
        </button>
        <button className="character-action" onClick={onCopy} type="button">
          COPY
        </button>
        <button
          className="character-action delete"
          onClick={onDelete}
          type="button"
        >
          DELETE
        </button>
      </div>
    </div>
  );
}

function Portrait({ name, src }: { name: string; src?: string }) {
  const initials = useMemo(() => {
    const parts = name.trim().split(/\s+/).slice(0, 2);
    return parts.map((p) => p[0]?.toUpperCase()).join("");
  }, [name]);

  return (
    <div className="character-portrait" aria-label={`${name} portrait`}>
      {src ? (
        <img
          src={src}
          alt={`${name} portrait`}
          onError={(e) => {
            (e.currentTarget as HTMLImageElement).style.display = "none";
          }}
        />
      ) : null}

      <div className="character-portrait-fallback">{initials || "?"}</div>
    </div>
  );
}
