"use client";

import React, { useMemo, useState } from "react";
import { useRouter } from "next/navigation";
import { FaPlus, FaSearch, FaSkull } from "react-icons/fa";

type V20Character = {
  id: string;
  name: string;
  clan: string;
  concept?: string;
  chronicle?: string;
  lastUpdated?: string; // ISO or display string
  isExample: boolean;
  portraitUrl?: string; // "/images/..." or remote URL
};

function useAuth() {
  // Replace with your real auth/session hook
  return { isSignedIn: true };
}

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
      lastUpdated: "2025-12-12",
      isExample: false,
      portraitUrl: "/images/portraits/lucien.png",
    },
    {
      id: "2",
      name: "Mirela Vance",
      clan: "Tremere",
      concept: "Occult Scholar",
      chronicle: "NOLA Chantry",
      lastUpdated: "2025-12-01",
      isExample: false,
      portraitUrl: "/images/portraits/mirela.png",
    },
    {
      id: "ex-1",
      name: "Sebastian Crowe",
      clan: "Ventrue",
      concept: "Corporate Tyrant",
      chronicle: "Example",
      lastUpdated: "2025-10-20",
      isExample: true,
      portraitUrl: "/images/portraits/sebastian.png",
    },
  ];

  const [query, setQuery] = useState("");

  const { userCharacters, exampleCharacters } = useMemo(() => {
    const q = query.trim().toLowerCase();

    const filtered = !q
      ? allCharacters
      : allCharacters.filter((c) => {
          const hay = `${c.name} ${c.clan} ${c.concept ?? ""} ${
            c.chronicle ?? ""
          }`.toLowerCase();
          return hay.includes(q);
        });

    return {
      userCharacters: filtered.filter((c) => !c.isExample),
      exampleCharacters: filtered.filter((c) => c.isExample),
    };
  }, [query, allCharacters]);

  const openCharacter = (id: string) =>
    router.push(`/creators/vtm-20th-anniversary/character/${id}`);

  return (
    <div className="section section-light">
      <div className="mx-auto w-full max-w-5xl">
        {/* Header */}
        <div className="mb-6 text-center">
          <h1 className="text-2xl sm:text-3xl font-bold tracking-tight text-foreground">
            Vampire: The Masquerade 20th Anniversary
          </h1>
          <p className="mt-2 text-sm text-[var(--muted)]">Characters library</p>
        </div>

        {/* Actions row */}
        <div className="mb-10 flex flex-col gap-3 sm:flex-row sm:items-center sm:justify-center">
          {isSignedIn && (
            <button
              className="hero-button"
              onClick={() =>
                router.push("/creators/vtm-20th-anniversary/create")
              }
            >
              <FaPlus className="mr-2" />
              Create Character
            </button>
          )}

          <div className="w-full sm:w-[420px]">
            <div className="relative">
              <FaSearch className="pointer-events-none absolute left-3 top-1/2 -translate-y-1/2 text-[var(--muted)]" />
              <input
                value={query}
                onChange={(e) => setQuery(e.target.value)}
                placeholder="Search by name, clan, chronicle..."
                className="pl-9"
              />
            </div>
          </div>
        </div>

        {/* Your Characters */}
        {isSignedIn && (
          <LibrarySection
            title="Your Characters"
            subtitle="Your saved V20 sheets"
            characters={userCharacters}
            emptyText="No characters yet. Create one to get started."
            onOpen={openCharacter}
          />
        )}

        {/* Example Characters */}
        <div className={isSignedIn ? "mt-12" : ""}>
          <LibrarySection
            title="Example Characters"
            subtitle="Read-only sheets you can view for reference"
            characters={exampleCharacters}
            emptyText="No example characters available."
            onOpen={openCharacter}
          />
        </div>
      </div>
    </div>
  );
}

function LibrarySection({
  title,
  subtitle,
  characters,
  emptyText,
  onOpen,
}: {
  title: string;
  subtitle?: string;
  characters: V20Character[];
  emptyText: string;
  onOpen: (id: string) => void;
}) {
  return (
    <section>
      <div className="mb-4">
        <div className="flex items-end justify-between gap-4">
          <h2 className="section-title m-0 border-0 p-0 text-foreground">
            {title}
          </h2>
          {subtitle && (
            <div className="text-sm text-[var(--muted)]">{subtitle}</div>
          )}
        </div>
        <div className="mt-3 border-b border-[var(--border)]" />
      </div>

      {characters.length === 0 ? (
        <div className="card text-center text-sm text-[var(--muted)]">
          {emptyText}
        </div>
      ) : (
        <div className="flex flex-col gap-3">
          {characters.map((c) => (
            <CharacterRow
              key={c.id}
              character={c}
              onOpen={() => onOpen(c.id)}
            />
          ))}
        </div>
      )}
    </section>
  );
}

function CharacterRow({
  character,
  onOpen,
}: {
  character: V20Character;
  onOpen: () => void;
}) {
  return (
    <button
      onClick={onOpen}
      className="card w-full text-left"
    >
      <div className="flex items-center gap-4  hover:bg-[var(--background)]">
        {/* Portrait */}
        <Portrait name={character.name} src={character.portraitUrl} />

        {/* Main info */}
        <div className="min-w-0 flex-1">
          <div className="flex items-center justify-between gap-3">
            <div className="truncate text-base font-semibold text-foreground">
              {character.name}
            </div>

            <div className="flex items-center gap-2">
              {character.isExample && (
                <span className="rounded-md border border-[var(--border)] bg-[var(--background)] px-2 py-1 text-xs text-[var(--muted)]">
                  Example
                </span>
              )}
            </div>
          </div>

          <div className="mt-1 flex flex-wrap items-center gap-x-3 gap-y-1 text-sm text-[var(--muted)]">
            <span className="text-foreground/90">{character.clan}</span>
            {character.concept ? <span>— {character.concept}</span> : null}
            {character.chronicle ? <span>• {character.chronicle}</span> : null}
            {character.lastUpdated ? (
              <span>• Updated {character.lastUpdated}</span>
            ) : null}
          </div>
        </div>

        {/* Right-side cue */}
        <div className="hidden sm:flex items-center text-[var(--muted)]">
          <span className="text-sm">Open →</span>
        </div>
      </div>
    </button>
  );
}

function Portrait({ name, src }: { name: string; src?: string }) {
  const initials = useMemo(() => {
    const parts = name.trim().split(/\s+/).slice(0, 2);
    return parts.map((p) => p[0]?.toUpperCase()).join("");
  }, [name]);

  // If you want: swap this <img> for next/image later.
  // Using <img> keeps it simple with your current global styles.
  return (
    <div
      className="relative shrink-0 overflow-hidden rounded-lg border"
      style={{
        width: 56,
        height: 56,
        borderColor: "var(--border)",
        background: "var(--navbar)",
      }}
    >
      {src ? (
        <img
          src={src}
          alt={`${name} portrait`}
          className="h-full w-full object-cover"
          onError={(e) => {
            // If the image fails, hide it so the fallback shows
            (e.currentTarget as HTMLImageElement).style.display = "none";
          }}
        />
      ) : null}

      {/* Fallback overlay (shows if no src OR img hidden after error) */}
      <div className="absolute inset-0 flex items-center justify-center">
        <div className="flex items-center gap-2 text-[var(--muted)]">
          <FaSkull />
          <span className="text-sm font-semibold">{initials}</span>
        </div>
      </div>
    </div>
  );
}
