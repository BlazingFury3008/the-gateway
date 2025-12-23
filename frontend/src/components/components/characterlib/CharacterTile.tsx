"use client";

import React from "react";
import Image from "next/image";

export type CharacterTileProps = {
  name: string;
  subtitle: string; // e.g. "Level 20 | Aasimar | Warlock/..."
  bannerUrl?: string;
  portraitUrl?: string;

  // Only show the button if the handler exists:
  onView?: () => void;
  onEdit?: () => void;
  onCopy?: () => void;
  onDelete?: () => void;
};

export default function CharacterTile({
  name,
  subtitle,
  bannerUrl,
  portraitUrl,
  onView,
  onEdit,
  onCopy,
  onDelete,
}: CharacterTileProps) {
  const hasAnyActions = onView || onEdit || onCopy || onDelete;

  return (
    <article className="character-tile">
      {/* Top banner */}
      <div
        className="character-banner"
        style={
          bannerUrl
            ? { backgroundImage: `url(${bannerUrl})` }
            : undefined
        }
      >
        <div className="character-banner-content">
          {/* Portrait */}
          <div className="character-portrait relative">
            {portraitUrl ? (
              <Image
                src={portraitUrl}
                alt={`${name} portrait`}
                fill
                sizes="48px"
                className="object-cover rounded"
              />
            ) : (
              <div className="character-portrait-fallback">
                {name?.[0] ?? "?"}
              </div>
            )}
          </div>

          <div className="character-meta">
            <div className="character-name">{name}</div>
            <div className="character-subtitle">{subtitle}</div>
          </div>
        </div>
      </div>

      {/* Bottom action row */}
      {hasAnyActions && (
        <div className="character-actions">
          {onView && (
            <button
              type="button"
              className="character-action"
              onClick={onView}
            >
              VIEW
            </button>
          )}

          {onEdit && (
            <button
              type="button"
              className="character-action"
              onClick={onEdit}
            >
              EDIT
            </button>
          )}

          {onCopy && (
            <button
              type="button"
              className="character-action"
              onClick={onCopy}
            >
              COPY
            </button>
          )}

          {onDelete && (
            <button
              type="button"
              className="character-action delete"
              onClick={onDelete}
            >
              DELETE
            </button>
          )}
        </div>
      )}
    </article>
  );
}
