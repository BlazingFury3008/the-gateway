"use client";

import React, { useMemo, useState } from "react";
import { useRouter } from "next/navigation";
import { FaSearch, FaCog } from "react-icons/fa";

type V20Character = {
  id: string;
  name: string;

  clan: string;
  sect?: string;
  concept?: string;
  chronicle?: string;

  generation?: number;
  nature?: string;
  demeanor?: string;

  lastUpdated?: string;
  isExample: boolean;

  portraitUrl?: string;
  bannerUrl?: string;
};

function useAuth() {
  // Swap this for your real auth
  return { isSignedIn: true };
}

type SortKey = "nameAsc" | "updatedDesc" | "clanAsc" | "generationAsc";

export default function V20CharactersPage() {
  const router = useRouter();
  const { isSignedIn } = useAuth();

  const allCharacters: V20Character[] = [
    {
      id: "1",
      name: "Lucien Blackwood",
      clan: "Toreador",
      sect: "Camarilla",
      concept: "Decadent Artist",
      chronicle: "The Gateway",
      generation: 12,
      nature: "Bon Vivant",
      demeanor: "Gallant",
      lastUpdated: "2025-12-12",
      isExample: false,
      portraitUrl: "/images/portraits/lucien.png",
      bannerUrl: "/images/banners/v20-1.jpg",
    },
    {
      id: "2",
      name: "Mirela Vance",
      clan: "Tremere",
      sect: "Camarilla",
      concept: "Occult Scholar",
      chronicle: "NOLA Chantry",
      generation: 11,
      nature: "Architect",
      demeanor: "Scholar",
      lastUpdated: "2025-12-01",
      isExample: false,
      portraitUrl: "/images/portraits/mirela.png",
      bannerUrl: "/images/banners/v20-2.jpg",
    },
    {
      id: "ex-1",
      name: "Sebastian Crowe",
      clan: "Ventrue",
      sect: "Camarilla",
      concept: "Corporate Tyrant",
      chronicle: "Example Chronicle",
      generation: 10,
      nature: "Director",
      demeanor: "Autocrat",
      lastUpdated: "2025-10-20",
      isExample: true,
      portraitUrl: "/images/portraits/sebastian.png",
      bannerUrl: "/images/banners/v20-3.jpg",
    },
  ];

  const [query, setQuery] = useState("");
  const [sortKey, setSortKey] = useState<SortKey>("updatedDesc");
  const [showCreateModal, setShowCreateModal] = useState(false);

  const { userCharacters, exampleCharacters } = useMemo(() => {
    const q = query.trim().toLowerCase();

    const filtered = !q
      ? allCharacters
      : allCharacters.filter((c) => {
          const hay = [
            c.name,
            c.clan,
            c.sect ?? "",
            c.concept ?? "",
            c.chronicle ?? "",
            c.nature ?? "",
            c.demeanor ?? "",
            c.generation != null ? `gen ${c.generation}` : "",
          ]
            .join(" ")
            .toLowerCase();

          return hay.includes(q);
        });

    const sorted = [...filtered].sort((a, b) => {
      if (sortKey === "nameAsc") return a.name.localeCompare(b.name);
      if (sortKey === "clanAsc") return a.clan.localeCompare(b.clan);
      if (sortKey === "generationAsc")
        return (a.generation ?? 99) - (b.generation ?? 99);
      // updatedDesc default
      return (b.lastUpdated ?? "").localeCompare(a.lastUpdated ?? "");
    });

    return {
      userCharacters: sorted.filter((c) => !c.isExample),
      exampleCharacters: sorted.filter((c) => c.isExample),
    };
  }, [query, sortKey, allCharacters]);

  const openCharacter = (id: string) =>
    router.push(`/creators/vtm-20th-anniversary/character/${id}`);

  const editCharacter = (id: string) =>
    router.push(`/creators/vtm-20th-anniversary/character/${id}/edit`);

  const copyCharacter = (id: string) => {
    // TODO: wire to backend
    console.log("Copy", id);
  };

  const deleteCharacter = (id: string) => {
    // TODO: wire to backend
    console.log("Delete", id);
  };

  return (
    <>
      <div className="section section-light">
        <div className="mx-auto w-full max-w-6xl">
          {/* Header */}
          <div className="flex flex-col gap-4 sm:flex-row sm:items-start sm:justify-between">
            <div>
              <h1 className="text-3xl sm:text-4xl font-extrabold tracking-tight text-[var(--foreground)]">
                Vampire: The Masquerade 20th Anniversary
              </h1>
              <div className="mt-3 text-sm text-[var(--foreground)]">
                Characters:{" "}
                <span className="font-semibold">
                  {userCharacters.length + exampleCharacters.length}
                </span>
              </div>
            </div>

            <div className="flex flex-col items-end gap-2">
              {isSignedIn && (
                <button
                  className="hero-button"
                  type="button"
                  onClick={() => setShowCreateModal(true)}
                >
                  CREATE A CHARACTER
                </button>
              )}

              <a
                href="/vtm-v20/blank-character-sheet.pdf"
                className="text-xs text-[var(--foreground)] underline underline-offset-2 opacity-90 hover:opacity-100"
              >
                ↓ Download a blank character sheet
              </a>
            </div>
          </div>

          {/* Controls */}
          <div className="mt-6 rounded-lg border border-[var(--border)] bg-[var(--navbar)] p-4 shadow-sm">
            <div className="flex flex-col gap-3 lg:flex-row lg:items-center">
              {/* Search */}
              <div className="flex-1">
                <div className="relative">
                  <FaSearch className="pointer-events-none absolute left-3 top-1/2 -translate-y-1/2 text-[var(--muted)]" />
                  <input
                    value={query}
                    onChange={(e) => setQuery(e.target.value)}
                    placeholder="Search by Name, Clan, Sect, Chronicle, Concept..."
                    className="pl-9"
                  />
                </div>
              </div>

              {/* Sort & Settings */}
              <div className="flex items-center justify-end gap-3">
                <div className="flex items-center gap-2">
                  <span className="text-xs font-semibold text-[var(--muted)]">
                    Sort By
                  </span>
                  <select
                    value={sortKey}
                    onChange={(e) => setSortKey(e.target.value as SortKey)}
                    className="h-11 rounded-md border border-[var(--border)] bg-[var(--background)] px-3 text-sm font-semibold text-[var(--foreground)] outline-none"
                  >
                    <option value="updatedDesc">Updated: Newest</option>
                    <option value="nameAsc">Name: A to Z</option>
                    <option value="clanAsc">Clan: A to Z</option>
                    <option value="generationAsc">
                      Generation: Lowest First
                    </option>
                  </select>
                </div>

                <button
                  type="button"
                  onClick={() => console.log("Settings")}
                  className="inline-flex h-11 items-center gap-2 rounded-md border border-[var(--border)] bg-[var(--background)] px-4 text-sm font-semibold text-[var(--foreground)] hover:bg-[var(--navbar)]"
                >
                  <FaCog className="text-[var(--muted)]" />
                  Settings
                </button>
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
              mode="user"
              onView={openCharacter}
              onEdit={editCharacter}
              onCopy={copyCharacter}
              onDelete={deleteCharacter}
            />
          )}

          {/* Example Sheets */}
          <div className={isSignedIn ? "mt-10" : "mt-6"}>
            <LibrarySection
              title="Example Sheets"
              subtitle="Read-only sample characters you can view or copy"
              characters={exampleCharacters}
              emptyText="No example sheets available."
              mode="example"
              onView={openCharacter}
              onCopy={copyCharacter}
            />
          </div>
        </div>
      </div>

      {showCreateModal && (
        <CreateCharacterModal
          onClose={() => setShowCreateModal(false)}
          onConfirm={() => {
            // TODO: Use form values from the modal if you want to send them along
            setShowCreateModal(false);
            router.push("/creators/vtm-20th-anniversary/create");
          }}
        />
      )}
    </>
  );
}

/* ---------------- Sections & Tiles ---------------- */

type LibrarySectionMode = "user" | "example";

function LibrarySection({
  title,
  subtitle,
  characters,
  emptyText,
  mode,
  onView,
  onEdit,
  onCopy,
  onDelete,
}: {
  title: string;
  subtitle?: string;
  characters: V20Character[];
  emptyText: string;
  mode: LibrarySectionMode;
  onView: (id: string) => void;
  onEdit?: (id: string) => void;
  onCopy?: (id: string) => void;
  onDelete?: (id: string) => void;
}) {
  return (
    <section className="mt-8">
      <div className="mb-4">
        <div className="flex items-end justify-between gap-4">
          <h2 className="section-title m-0 border-0 p-0 text-[var(--foreground)]">
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
        <div className="mt-4 grid grid-cols-1 gap-5 md:grid-cols-2 xl:grid-cols-3">
          {characters.map((c) => (
            <CharacterTile
              key={c.id}
              character={c}
              mode={mode}
              onView={() => onView(c.id)}
              onEdit={onEdit ? () => onEdit(c.id) : undefined}
              onCopy={onCopy ? () => onCopy(c.id) : undefined}
              onDelete={onDelete ? () => onDelete(c.id) : undefined}
            />
          ))}
        </div>
      )}
    </section>
  );
}

function CharacterTile({
  character,
  mode,
  onView,
  onEdit,
  onCopy,
  onDelete,
}: {
  character: V20Character;
  mode: LibrarySectionMode;
  onView: () => void;
  onEdit?: () => void;
  onCopy?: () => void;
  onDelete?: () => void;
}) {
  const subtitle = useMemo(() => {
    const left = [
      character.sect ? character.sect : null,
      character.generation != null ? `Gen ${character.generation}` : null,
    ].filter(Boolean);

    const right = [
      character.clan,
      character.concept ? `— ${character.concept}` : null,
      character.chronicle ? `• ${character.chronicle}` : null,
      character.lastUpdated ? `• Updated ${character.lastUpdated}` : null,
    ].filter(Boolean);

    const a = left.length ? `${left.join(" | ")} | ` : "";
    return a + right.join(" ");
  }, [character]);

  // Build action list based on mode
  const actions: { label: string; onClick?: () => void; variant?: "danger" }[] =
    mode === "example"
      ? [
          { label: "VIEW", onClick: onView },
          { label: "COPY", onClick: onCopy },
        ]
      : [
          { label: "VIEW", onClick: onView },
          { label: "EDIT", onClick: onEdit },
          { label: "COPY", onClick: onCopy },
          { label: "DELETE", onClick: onDelete, variant: "danger" },
        ];

  return (
    <div className="card p-0 overflow-hidden">
      {/* Banner */}
      <div
        className="relative h-24 w-full bg-[var(--background)]"
        style={
          character.bannerUrl
            ? {
                backgroundImage: `url(${character.bannerUrl})`,
                backgroundSize: "cover",
                backgroundPosition: "center",
              }
            : undefined
        }
      >
        <div className="absolute inset-0 bg-black/40" />
        <div className="absolute inset-x-3 bottom-3 flex items-center gap-3">
          <Portrait name={character.name} src={character.portraitUrl} />
          <div className="min-w-0">
            <div className="truncate text-lg font-semibold text-white">
              {character.name}
            </div>
            <div className="truncate text-xs text-white/80">{subtitle}</div>
          </div>
        </div>
      </div>

      {/* Actions */}
      <div className="flex border-t border-[var(--border)] text-xs sm:text-sm font-semibold">
        {actions.map((a, idx) => (
          <button
            key={idx}
            type="button"
            onClick={a.onClick}
            className={`flex-1 py-2.5 border-r border-[var(--border)] bg-[var(--navbar)] hover:bg-[var(--background)] ${
              a.variant === "danger"
                ? "text-orange-500"
                : "text-[var(--foreground)]"
            } ${idx === actions.length - 1 ? "last:border-r-0" : ""}`}
          >
            {a.label}
          </button>
        ))}
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
    <div
      className="relative h-12 w-12 shrink-0 overflow-hidden rounded-md border border-white/30 bg-[var(--navbar)]"
      aria-label={`${name} portrait`}
    >
      {src ? (
        <img
          src={src}
          alt={`${name} portrait`}
          className="h-full w-full object-cover"
          onError={(e) => {
            (e.currentTarget as HTMLImageElement).style.display = "none";
          }}
        />
      ) : null}
      <div className="absolute inset-0 flex items-center justify-center text-sm font-bold text-white/85 bg-black/20">
        {initials || "?"}
      </div>
    </div>
  );
}

/* ---------------- Create Character Modal ---------------- */

function CreateCharacterModal({
  onClose,
  onConfirm,
}: {
  onClose: () => void;
  onConfirm: () => void;
}) {
  const [name, setName] = useState("");
  const [clan, setClan] = useState("");
  const [sect, setSect] = useState("");
  const [concept, setConcept] = useState("");
  const [chronicle, setChronicle] = useState("");
  const [generation, setGeneration] = useState<number | "">("");
  const [nature, setNature] = useState("");
  const [demeanor, setDemeanor] = useState("");

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();

    // You can pass this data upward by changing `onConfirm`
    // to accept a payload, e.g. onConfirm(formData)
    const draft = {
      name,
      clan,
      sect,
      concept,
      chronicle,
      generation: generation === "" ? undefined : Number(generation),
      nature,
      demeanor,
    };
    console.log("New V20 character draft:", draft);

    onConfirm();
  };

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center bg-black/50 px-4">
      <form onSubmit={handleSubmit} className="card max-w-md w-full">
        <h2 className="mb-2 text-xl font-semibold text-[var(--foreground)]">
          Create a V20 Character
        </h2>
        <p className="mb-4 text-sm text-[var(--muted)]">
          Start a new Vampire: The Masquerade 20th Anniversary character sheet.
          You&apos;ll be able to refine details after this step.
        </p>

        <div className="space-y-3 mb-4">
          <div>
            <label className="mb-1 block text-xs font-semibold text-[var(--muted)]">
              Name
            </label>
            <input
              value={name}
              onChange={(e) => setName(e.target.value)}
              placeholder="Lucien Blackwood"
            />
          </div>

          <div className="grid grid-cols-1 gap-3 sm:grid-cols-2">
            <div>
              <label className="mb-1 block text-xs font-semibold text-[var(--muted)]">
                Clan
              </label>
              <input
                value={clan}
                onChange={(e) => setClan(e.target.value)}
                placeholder="Toreador"
              />
            </div>
            <div>
              <label className="mb-1 block text-xs font-semibold text-[var(--muted)]">
                Sect
              </label>
              <input
                value={sect}
                onChange={(e) => setSect(e.target.value)}
                placeholder="Camarilla"
              />
            </div>
          </div>

          <div>
            <label className="mb-1 block text-xs font-semibold text-[var(--muted)]">
              Concept
            </label>
            <input
              value={concept}
              onChange={(e) => setConcept(e.target.value)}
              placeholder="Decadent Artist"
            />
          </div>

          <div>
            <label className="mb-1 block text-xs font-semibold text-[var(--muted)]">
              Chronicle
            </label>
            <input
              value={chronicle}
              onChange={(e) => setChronicle(e.target.value)}
              placeholder="The Gateway"
            />
          </div>

          <div className="grid grid-cols-1 gap-3 sm:grid-cols-3">
            <div>
              <label className="mb-1 block text-xs font-semibold text-[var(--muted)]">
                Generation
              </label>
              <input
                type="number"
                min={3}
                max={16}
                value={generation}
                onChange={(e) =>
                  setGeneration(e.target.value === "" ? "" : Number(e.target.value))
                }
                placeholder="12"
              />
            </div>
            <div>
              <label className="mb-1 block text-xs font-semibold text-[var(--muted)]">
                Nature
              </label>
              <input
                value={nature}
                onChange={(e) => setNature(e.target.value)}
                placeholder="Bon Vivant"
              />
            </div>
            <div>
              <label className="mb-1 block text-xs font-semibold text-[var(--muted)]">
                Demeanor
              </label>
              <input
                value={demeanor}
                onChange={(e) => setDemeanor(e.target.value)}
                placeholder="Gallant"
              />
            </div>
          </div>
        </div>

        <div className="flex flex-col gap-2 sm:flex-row sm:justify-end">
          <button
            type="button"
            onClick={onClose}
            className="px-4 py-2 text-sm font-semibold text-[var(--muted)] border border-[var(--border)] rounded-md bg-[var(--background)] hover:bg-[var(--navbar)]"
          >
            Cancel
          </button>
          <button type="submit" className="hero-button">
            Continue
          </button>
        </div>
      </form>
    </div>
  );
}
