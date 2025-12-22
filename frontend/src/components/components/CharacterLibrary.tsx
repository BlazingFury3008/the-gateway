"use client";

import React, { useMemo, useState } from "react";
import { FaSearch, FaCog } from "react-icons/fa";

/**
 * Generic character representation for any game.
 * Map your own backend model to this shape.
 */
export type GameCharacter = {
  id: string;
  name: string;

  /** e.g. "Level 7 Fighter | Half-Orc | Curse of Strahd" OR "Neonate | Brujah | Anarch" */
  primaryLine?: string;

  /** e.g. "Updated 2025-01-01" or "Campaign: The Gateway" */
  secondaryLine?: string;

  /** Optional extra string to search on; if omitted, we search name + lines. */
  searchText?: string;

  /** Optional – used for "Updated: Newest" sort. */
  lastUpdated?: string;

  /** Example characters only show VIEW + COPY. */
  isExample?: boolean;

  portraitUrl?: string;
  bannerUrl?: string;
};

export type SortKey = "nameAsc" | "updatedDesc";

export type CharacterLibraryProps = {
  /** Page header title, e.g. "Characters Library" or a specific game name. */
  gameTitle: string;
  /** Optional subtitle under the main title. */
  gameSubtitle?: string;

  /** All characters for this game (user + examples). */
  characters: GameCharacter[];

  /** Where to send the user for a blank sheet download (optional). */
  blankSheetHref?: string;

  /** Placeholder text for the search input. */
  searchPlaceholder?: string;

  /** Default sort key; "updatedDesc" or "nameAsc". */
  defaultSortKey?: SortKey;

  /** Show the "Create a Character" button + sheet. */
  enableCreate?: boolean;

  /**
   * Called when user confirms "Continue" in the create-character sheet.
   * Parent should handle navigation or logic.
   */
  onCreateConfirm?: () => void;

  /** Called when the Settings button is clicked. */
  onSettingsClick?: () => void;

  /** Label overrides if you want different wording per game. */
  labels?: {
    createButton?: string;
    blankSheetLink?: string;
    totalCharactersPrefix?: string; // e.g. "Characters:"
    yourCharactersTitle?: string;
    yourCharactersSubtitle?: string;
    exampleCharactersTitle?: string;
    exampleCharactersSubtitle?: string;
    noUserCharacters?: string;
    noExampleCharacters?: string;
    sortBy?: string;
    sortUpdatedNewest?: string;
    sortNameAsc?: string;
    actionsView?: string;
    actionsEdit?: string;
    actionsCopy?: string;
    actionsDelete?: string;
    sheetTitle?: string;
    sheetBody?: string;
    sheetCancel?: string;
    sheetContinue?: string;
  };

  /** Callbacks for tile actions; you decide routing/behavior. */
  onViewCharacter: (id: string) => void;
  onEditCharacter?: (id: string) => void;
  onCopyCharacter?: (id: string) => void;
  onDeleteCharacter?: (id: string) => void;
};

/**
 * Generic, reusable character library component.
 * Plug this into any game page and feed it data + callbacks.
 */
export function CharacterLibrary({
  gameTitle,
  gameSubtitle,
  characters,
  blankSheetHref,
  searchPlaceholder = "Search by name, tags, campaign, or description...",
  defaultSortKey = "updatedDesc",
  enableCreate = true,
  onCreateConfirm,
  onSettingsClick,
  labels,
  onViewCharacter,
  onEditCharacter,
  onCopyCharacter,
  onDeleteCharacter,
}: CharacterLibraryProps) {
  const [query, setQuery] = useState("");
  const [sortKey, setSortKey] = useState<SortKey>(defaultSortKey);
  const [showCreateSheet, setShowCreateSheet] = useState(false);

  const {
    createButton = "CREATE A CHARACTER",
    blankSheetLink = "↓ Download a blank character sheet",
    totalCharactersPrefix = "Characters:",
    yourCharactersTitle = "Your Characters",
    yourCharactersSubtitle = "Your saved sheets for this game",
    exampleCharactersTitle = "Example Characters",
    exampleCharactersSubtitle = "Read-only sample characters you can view or copy",
    noUserCharacters = "No characters yet. Create one to get started.",
    noExampleCharacters = "No example characters available.",
    sortBy = "Sort By",
    sortUpdatedNewest = "Updated: Newest",
    sortNameAsc = "Name: A to Z",
    actionsView = "VIEW",
    actionsEdit = "EDIT",
    actionsCopy = "COPY",
    actionsDelete = "DELETE",
    sheetTitle = "Create a Character",
    sheetBody = "Start a new character sheet for this game. You'll choose details such as class, clan, playbook, species, or other traits on the next screen.",
    sheetCancel = "Cancel",
    sheetContinue = "Continue",
  } = labels ?? {};

  const { userCharacters, exampleCharacters } = useMemo(() => {
    const q = query.trim().toLowerCase();

    const filtered = !q
      ? characters
      : characters.filter((c) => {
          const haystack =
            c.searchText ??
            [c.name, c.primaryLine ?? "", c.secondaryLine ?? ""]
              .join(" ")
              .toLowerCase();
          return haystack.includes(q);
        });

    const sorted = [...filtered].sort((a, b) => {
      if (sortKey === "nameAsc") return a.name.localeCompare(b.name);
      return (b.lastUpdated ?? "").localeCompare(a.lastUpdated ?? "");
    });

    return {
      userCharacters: sorted.filter((c) => !c.isExample),
      exampleCharacters: sorted.filter((c) => c.isExample),
    };
  }, [query, sortKey, characters]);

  const totalCount = userCharacters.length + exampleCharacters.length;

  const handleCreateConfirmInternal = () => {
    setShowCreateSheet(false);
    onCreateConfirm?.();
  };

  return (
    <>
      <div className="section section-light">
        <div className="mx-auto w-full max-w-6xl">
          {/* Header */}
          <div className="flex flex-col gap-4 sm:flex-row sm:items-start sm:justify-between">
            <div>
              <h1 className="text-3xl sm:text-4xl font-extrabold tracking-tight text-[var(--foreground)]">
                {gameTitle}
              </h1>
              {gameSubtitle && (
                <p className="mt-1 text-sm text-[var(--muted)]">
                  {gameSubtitle}
                </p>
              )}
              <div className="mt-3 text-sm text-[var(--foreground)]">
                {totalCharactersPrefix}{" "}
                <span className="font-semibold">{totalCount}</span>
              </div>
            </div>

            <div className="flex flex-col items-end gap-2">
              {enableCreate && (
                <button
                  className="hero-button"
                  type="button"
                  onClick={() => setShowCreateSheet(true)}
                >
                  {createButton}
                </button>
              )}

              {blankSheetHref && (
                <a
                  href={blankSheetHref}
                  className="text-xs text-[var(--foreground)] underline underline-offset-2 opacity-90 hover:opacity-100"
                >
                  {blankSheetLink}
                </a>
              )}
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
                    placeholder={searchPlaceholder}
                    className="pl-9"
                  />
                </div>
              </div>

              {/* Sort & Settings */}
              <div className="flex items-center justify-end gap-3">
                <div className="flex items-center gap-2">
                  <span className="text-xs font-semibold text-[var(--muted)]">
                    {sortBy}
                  </span>
                  <select
                    value={sortKey}
                    onChange={(e) => setSortKey(e.target.value as SortKey)}
                    className="h-11 rounded-md border border-[var(--border)] bg-[var(--background)] px-3 text-sm font-semibold text-[var(--foreground)] outline-none"
                  >
                    <option value="updatedDesc">{sortUpdatedNewest}</option>
                    <option value="nameAsc">{sortNameAsc}</option>
                  </select>
                </div>

                <button
                  type="button"
                  onClick={onSettingsClick}
                  className="inline-flex h-11 items-center gap-2 rounded-md border border-[var(--border)] bg-[var(--background)] px-4 text-sm font-semibold text-[var(--foreground)] hover:bg-[var(--navbar)]"
                >
                  <FaCog className="text-[var(--muted)]" />
                  Settings
                </button>
              </div>
            </div>
          </div>

          {/* Your Characters */}
          <LibrarySection
            title={yourCharactersTitle}
            subtitle={yourCharactersSubtitle}
            characters={userCharacters}
            emptyText={noUserCharacters}
            mode="user"
            labels={{ actionsView, actionsEdit, actionsCopy, actionsDelete }}
            onView={onViewCharacter}
            onEdit={onEditCharacter}
            onCopy={onCopyCharacter}
            onDelete={onDeleteCharacter}
          />

          {/* Example Characters */}
          <div className="mt-10">
            <LibrarySection
              title={exampleCharactersTitle}
              subtitle={exampleCharactersSubtitle}
              characters={exampleCharacters}
              emptyText={noExampleCharacters}
              mode="example"
              labels={{ actionsView, actionsCopy }}
              onView={onViewCharacter}
              onCopy={onCopyCharacter}
            />
          </div>
        </div>
      </div>

      {enableCreate && showCreateSheet && (
        <CreateCharacterSheet
          title={sheetTitle}
          body={sheetBody}
          cancelLabel={sheetCancel}
          continueLabel={sheetContinue}
          onClose={() => setShowCreateSheet(false)}
          onConfirm={handleCreateConfirmInternal}
        />
      )}
    </>
  );
}

/* ---------------- Sections & Tiles ---------------- */

type LibrarySectionMode = "user" | "example";

type LibrarySectionLabels = {
  actionsView: string;
  actionsEdit?: string;
  actionsCopy?: string;
  actionsDelete?: string;
};

type LibrarySectionProps = {
  title: string;
  subtitle?: string;
  characters: GameCharacter[];
  emptyText: string;
  mode: LibrarySectionMode;
  labels: LibrarySectionLabels;
  onView: (id: string) => void;
  onEdit?: (id: string) => void;
  onCopy?: (id: string) => void;
  onDelete?: (id: string) => void;
};

function LibrarySection({
  title,
  subtitle,
  characters,
  emptyText,
  mode,
  labels,
  onView,
  onEdit,
  onCopy,
  onDelete,
}: LibrarySectionProps) {
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
              labels={labels}
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

type CharacterTileProps = {
  character: GameCharacter;
  mode: LibrarySectionMode;
  labels: LibrarySectionLabels;
  onView: () => void;
  onEdit?: () => void;
  onCopy?: () => void;
  onDelete?: () => void;
};

function CharacterTile({
  character,
  mode,
  labels,
  onView,
  onEdit,
  onCopy,
  onDelete,
}: CharacterTileProps) {
  const subtitle = useMemo(() => {
    const parts = [character.primaryLine, character.secondaryLine];
    if (!character.secondaryLine && character.lastUpdated) {
      parts.push(`Updated ${character.lastUpdated}`);
    }
    return parts.filter(Boolean).join(" • ");
  }, [character]);

  const actions: { label: string; onClick?: () => void; danger?: boolean }[] =
    mode === "example"
      ? [
          { label: labels.actionsView, onClick: onView },
          { label: labels.actionsCopy ?? "COPY", onClick: onCopy },
        ]
      : [
          { label: labels.actionsView, onClick: onView },
          { label: labels.actionsEdit ?? "EDIT", onClick: onEdit },
          { label: labels.actionsCopy ?? "COPY", onClick: onCopy },
          {
            label: labels.actionsDelete ?? "DELETE",
            onClick: onDelete,
            danger: true,
          },
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
              a.danger ? "text-orange-500" : "text-[var(--foreground)]"
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

/* ---------------- Slide-up Sheet Component ---------------- */

type CreateCharacterSheetProps = {
  title: string;
  body: string;
  cancelLabel: string;
  continueLabel: string;
  onClose: () => void;
  onConfirm: () => void;
};

function CreateCharacterSheet({
  title,
  body,
  cancelLabel,
  continueLabel,
  onClose,
  onConfirm,
}: CreateCharacterSheetProps) {
  return (
    <div className="sheet-backdrop" role="dialog" aria-modal="true">
      <div className="sheet-panel">
        <div className="sheet-panel-header">
          <h2 className="sheet-panel-title">{title}</h2>
          <button
            type="button"
            className="sheet-panel-close"
            onClick={onClose}
            aria-label="Close"
          >
            ✕
          </button>
        </div>

        <div className="sheet-panel-body">
          <p>{body}</p>
        </div>

        <div className="sheet-panel-actions">
          <button
            type="button"
            onClick={onClose}
            className="px-4 py-2 text-sm font-semibold text-[var(--muted)] border border-[var(--border)] rounded-md bg-[var(--background)] hover:bg-[var(--navbar)]"
          >
            {cancelLabel}
          </button>
          <button
            type="button"
            onClick={onConfirm}
            className="hero-button px-4 py-2 text-sm"
          >
            {continueLabel}
          </button>
        </div>
      </div>
    </div>
  );
}
