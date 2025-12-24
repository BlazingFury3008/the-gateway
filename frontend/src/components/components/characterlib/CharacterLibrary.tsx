"use client";

import React, { useMemo, useState } from "react";
import CharacterTile from "./CharacterTile";
import Divider from "../Divider";
import { useSession } from "next-auth/react";

/**
 * Represents a single tile in the library grid.
 *
 * This is already in the "display shape" the UI needs:
 * - `name` → large title text
 * - `subtitle` → smaller description line
 * - optional `bannerUrl` / `portraitUrl` → artwork
 *
 * Add extra fields (e.g. `level`, `clan`, `xp`) for sorting
 * or for use inside your click handlers.
 */
export type LibraryItem = {
  /** Unique ID for this entry (used as React key and in callbacks). */
  id: string;

  /** Main title on the card (character name, coterie name, ship name, etc.). */
  name: string;

  /** Short description line under the title (e.g. level/species/class). */
  subtitle: string;

  /**
   * Extra string used for searching.
   * If not set, searching uses `"${name} ${subtitle}"`.
   */
  searchText?: string;

  /** Optional banner background image URL. */
  bannerUrl?: string;

  /** Optional portrait image URL for the small square avatar. */
  portraitUrl?: string;

  /**
   * Any extra data you want to attach (level, clan, tags, etc.).
   * Your sort functions and click handlers can read these fields.
   */
  [key: string]: unknown;
};

/**
 * Configures one entry in the "Sort By" dropdown.
 *
 * Example:
 * ```ts
 * const sortByLevelDesc: LibrarySortOption = {
 *   id: "level-desc",
 *   label: "Level: High to Low",
 *   compare: (a, b) => (b.level as number) - (a.level as number),
 * };
 * ```
 */
export type LibrarySortOption = {
  /** Key used to identify this sort option (and used by `defaultSortId`). */
  id: string;

  /** Text shown in the sort dropdown (e.g. "Level: High to Low"). */
  label: string;

  /**
   * Comparison function for `Array.sort`.
   * Return:
   * - negative → `a` comes before `b`
   * - positive → `a` comes after `b`
   * - 0 → equal for this sort
   */
  compare: (a: LibraryItem, b: LibraryItem) => number;
};

/**
 * Props for the reusable `CharactersLibrary` component.
 *
 * You pass in:
 * - a list of items (`items`) already in display shape
 * - optional example items (`example_items`) shown in a separate section
 * - optional sort options (`sortOptions`)
 * - optional handlers for create/view/edit/copy/delete
 *
 * Basic example:
 *
 * ```tsx
 * <CharactersLibrary
 *   title="My Characters"
 *   itemLabel="Characters"
 *   items={items}
 *   example_items={exampleItems}
 *   sortOptions={sortOptions}
 *   defaultSortId="level-desc"
 *   onCreate={() => ...}
 *   onViewItem={(item) => ...}
 * />
 * ```
 */
export type CharactersLibraryProps = {
  /** Text shown as the main page heading (e.g. "My Characters"). */
  title: string;

  /** Label used in the count line (e.g. "Characters", "Coteries"). Defaults to `"Items"`. */
  itemLabel?: string;

  /** List of items to display as cards in the main grid. */
  items: LibraryItem[];

  /**
   * Optional list of example items (e.g. starter characters, templates).
   * If provided and non-empty, they are shown in a separate “Example Characters”
   * section below the main grid.
   */
  example_items?: LibraryItem[];

  /**
   * Available sort options for the "Sort By" dropdown.
   * If omitted or empty, the sort dropdown is hidden.
   */
  sortOptions?: LibrarySortOption[];

  /**
   * ID of the sort option to use initially.
   * Should match one of `sortOptions[i].id`. If omitted, uses the first option.
   */
  defaultSortId?: string;

  /** Placeholder text for the search input. Defaults to `"Search…"`. */
  searchPlaceholder?: string;

  /**
   * Called when the "Create" button is clicked.
   * If not provided, the "Create" button is not rendered.
   */
  onCreate?: () => void;

  /** Text shown on the "Create" button. Defaults to `"CREATE"`. */
  createLabel?: string;

  /**
   * Called when the "Download blank" link is clicked.
   * If not provided, this link is not rendered.
   */
  onDownloadBlank?: () => void;

  /** Text for the "Download blank" link. Defaults to `"Download a blank sheet"`. */
  downloadLabel?: string;

  /**
   * Called when the "Settings" button is clicked.
   * If not provided, the settings button is not rendered.
   */
  onSettingsClick?: () => void;

  /** Text for the "Settings" button. Defaults to `"Settings"`. */
  settingsLabel?: string;

  /**
   * Called when the "VIEW" button on a tile is clicked.
   * If not provided, no VIEW button is shown.
   */
  onViewItem?: (item: LibraryItem) => void;

  /**
   * Called when the "EDIT" button on a tile is clicked.
   * If not provided, no EDIT button is shown.
   */
  onEditItem?: (item: LibraryItem) => void;

  /**
   * Called when the "COPY" button on a tile is clicked.
   * If not provided, no COPY button is shown.
   */
  onCopyItem?: (item: LibraryItem) => void;

  /**
   * Called when the "DELETE" button on a tile is clicked.
   * If not provided, no DELETE button is shown.
   */
  onDeleteItem?: (item: LibraryItem) => void;
};

/**
 * A generic, system-agnostic library grid for RPG-style entities.
 *
 * Features:
 * - Header with title, item count, and optional create/download actions
 * - Search input that filters items by name/subtitle/searchText
 * - Optional "Sort By" dropdown driven by `sortOptions`
 * - Main grid of `CharacterTile` cards with VIEW / EDIT / COPY / DELETE
 * - Optional second grid for example items (e.g. sample characters)
 *
 * @param props.title             Heading text at the top of the page.
 * @param props.itemLabel         Label used before the count (e.g. "Characters").
 * @param props.items             List of items to render in the main grid.
 * @param props.example_items     List of example items to render in a separate section.
 * @param props.sortOptions       Available sort modes for the dropdown.
 * @param props.defaultSortId     ID of the initially selected sort option.
 * @param props.searchPlaceholder Placeholder text for the search field.
 * @param props.onCreate          Handler for the main "Create" button.
 * @param props.createLabel       Label for the "Create" button.
 * @param props.onDownloadBlank   Handler for the "Download blank" link.
 * @param props.downloadLabel     Label for the "Download blank" link.
 * @param props.onSettingsClick   Handler for the "Settings" button.
 * @param props.settingsLabel     Label for the "Settings" button.
 * @param props.onViewItem        Called when a tile's VIEW button is clicked.
 * @param props.onEditItem        Called when a tile's EDIT button is clicked.
 * @param props.onCopyItem        Called when a tile's COPY button is clicked.
 * @param props.onDeleteItem      Called when a tile's DELETE button is clicked.
 */
export default function CharactersLibrary({
  title,
  itemLabel = "Items",
  items,
  example_items,
  sortOptions,
  defaultSortId,
  searchPlaceholder = "Search…",
  onCreate,
  createLabel = "CREATE",
  onDownloadBlank,
  downloadLabel = "Download a blank sheet",
  onSettingsClick,
  settingsLabel = "Settings",
  onViewItem,
  onEditItem,
  onCopyItem,
  onDeleteItem,
}: CharactersLibraryProps) {
  const {data, status} = useSession()
  const [search, setSearch] = useState("");
  const [sortId, setSortId] = useState<string | undefined>(
    defaultSortId ?? sortOptions?.[0]?.id
  );

  const activeSort = useMemo(
    () => sortOptions?.find((s) => s.id === sortId) ?? sortOptions?.[0],
    [sortOptions, sortId]
  );

  const filtered = useMemo(() => {
    const q = search.toLowerCase().trim();

    let list = items.filter((item) => {
      if (!q) return true;

      const baseText =
        item.searchText ?? `${item.name} ${item.subtitle}`.toLowerCase();

      return baseText.toLowerCase().includes(q);
    });

    if (activeSort) {
      list = [...list].sort(activeSort.compare);
    }

    return list;
  }, [items, search, activeSort]);

  return (
    <div className="characters-shell">
      <div className="characters-wrap">
        {/* Header */}
        <header className="characters-header">
          <div>
            <h1 className="characters-title">{title}</h1>
            <p className="characters-subline">
              {itemLabel}: <strong>{items.length}</strong>
            </p>
          </div>

          <div className="characters-actions">
            {onCreate && (
              <button
                type="button"
                className="hero-button"
                onClick={onCreate}
              >
                {createLabel}
              </button>
            )}

            {onDownloadBlank && (
              <button
                type="button"
                className="characters-download"
                onClick={onDownloadBlank}
              >
                {downloadLabel}
              </button>
            )}
          </div>
        </header>

        {/* Search / sort row */}
        <section className="characters-controls">
          <div className="characters-controls-row">
            <div className="characters-search">
              <div className="search-wrap">
                <span className="search-icon">🔍</span>
                <input
                  type="text"
                  placeholder={searchPlaceholder}
                  value={search}
                  onChange={(e) => setSearch(e.target.value)}
                />
              </div>
            </div>

            <div className="characters-sort">
              {sortOptions && sortOptions.length > 0 && (
                <>
                  <label>Sort By:</label>
                  <select
                    value={activeSort?.id ?? ""}
                    onChange={(e) => setSortId(e.target.value)}
                  >
                    {sortOptions.map((opt) => (
                      <option key={opt.id} value={opt.id}>
                        {opt.label}
                      </option>
                    ))}
                  </select>
                </>
              )}

              {onSettingsClick && (
                <button
                  type="button"
                  className="characters-settings"
                  onClick={onSettingsClick}
                >
                  <span>⚙</span>
                  <span>{settingsLabel}</span>
                </button>
              )}
            </div>
          </div>
        </section>

        {/* Main grid */}
        <section className="character-grid min-h-[150px]">
          {filtered.length > 0 ? (
            filtered.map((item) => (
              <CharacterTile
                key={item.id}
                name={item.name}
                subtitle={item.subtitle}
                bannerUrl={item.bannerUrl as string | undefined}
                portraitUrl={item.portraitUrl as string | undefined}
                onView={onViewItem ? () => onViewItem(item) : undefined}
                onEdit={onEditItem ? () => onEditItem(item) : undefined}
                onCopy={onCopyItem ? () => onCopyItem(item) : undefined}
                onDelete={
                  onDeleteItem ? () => onDeleteItem(item) : undefined
                }
              />
            ))
          ) : (
            <div className="col-span-full flex min-h-[150px] w-full items-center justify-center text-center">
              <h2 className="mb-2 text-xs font-semibold uppercase tracking-wide text-[var(--muted)]">
                No characters found, try adjusting your search
                {onCreate && (
                  <>
                    {"; "}
                    <button
                      type="button"
                      className="underline cursor-pointer uppercase"
                      onClick={onCreate}
                    >
                      or create a new one!
                    </button>
                  </>
                )}
                . <br />
                {status != "authenticated" && <span>Characters created will be stored in Local Storage until you log in or create an account</span>}
              </h2>
            </div>
          )}
        </section>

        <Divider />

        {/* Example characters section */}
        {example_items && example_items.length > 0 && (
          <section className="mt-6">
            <h2 className="mb-2 text-xs font-semibold uppercase tracking-wide text-[var(--muted)]">
              Example Characters
            </h2>
            <div className="character-grid">
              {example_items.map((item) => (
                <CharacterTile
                  key={item.id}
                  name={item.name}
                  subtitle={item.subtitle}
                  bannerUrl={item.bannerUrl as string | undefined}
                  portraitUrl={item.portraitUrl as string | undefined}
                  onView={
                    onViewItem ? () => onViewItem(item) : undefined
                  }
                  onCopy={
                    onCopyItem ? () => onCopyItem(item) : undefined
                  }
                />
              ))}
            </div>
          </section>
        )}
      </div>
    </div>
  );
}
