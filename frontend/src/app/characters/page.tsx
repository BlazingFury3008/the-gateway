/* eslint-disable react-hooks/exhaustive-deps */
"use client";

import React, { useMemo, useState } from "react";
import { useRouter } from "next/navigation";
import { FaTint, FaSearch, FaBook } from "react-icons/fa";

interface CharacterCreatorInfo {
  title: string;
  description: string;
  colour: string;
  link: string;
  icon: React.ComponentType<{
    className?: string;
    style?: React.CSSProperties;
  }>;
}

export default function Page() {
  const router = useRouter();

  const characterCreators: CharacterCreatorInfo[] = [
    {
      title: "Vampire The Masquerade: 20th Anniversary Edition",
      description:
        "A character creator for Vampire The Masquerade: 20th Anniversary Edition",
      colour: "#8B0000",
      link: "/creators/vtm-20th-anniversary",
      icon: FaTint,
    },
    {
      title: "Mage: The Ascension: 20th Anniversary Edition",
      description:
        "A character creator for Mage: The Ascension: 20th Anniversary Edition",
      colour: "#00008B",
      link: "/creators/mage-20th-anniversary",
      icon: FaBook,
    },
  ];

  const [query, setQuery] = useState("");

  const filteredCreators = useMemo(() => {
    const q = query.trim().toLowerCase();
    if (!q) return characterCreators;
    return characterCreators.filter(
      (c) =>
        c.title.toLowerCase().includes(q) ||
        c.description.toLowerCase().includes(q)
    );
  }, [query, characterCreators]);

  return (
    <div className="min-h-[calc(100vh-4rem)] px-4 py-12">
      <div className="mx-auto flex max-w-4xl flex-col items-center gap-8">
        {/* Header */}
        <div className="text-center">
          <h1 className="text-3xl font-semibold tracking-tight">
            Character Creators
          </h1>
          <p className="mt-2 text-sm text-zinc-400">
            Choose a system and start building
          </p>
        </div>

        {/* Search Bar */}
        <div className="w-full max-w-xl">
          <div className="relative">
            <FaSearch className="pointer-events-none absolute left-4 top-1/2 -translate-y-1/2 text-zinc-400" />
            <input
              value={query}
              onChange={(e) => setQuery(e.target.value)}
              placeholder="Search creators..."
              className="w-full rounded-2xl border border-zinc-800 bg-zinc-950/60 py-3 pl-11 pr-4 text-sm text-zinc-100 placeholder:text-zinc-500 outline-none focus:border-zinc-700"
            />
          </div>
        </div>

        {/* Creator Tabs */}
        <div className="grid w-full grid-cols-1 gap-4 sm:grid-cols-2">
          {filteredCreators.map((creator) => (
            <CreatorTab
              key={creator.link}
              info={creator}
              onNavigate={() => router.push(creator.link)}
            />
          ))}

          {filteredCreators.length === 0 && (
            <div className="col-span-full rounded-2xl border border-zinc-800 bg-zinc-950/40 p-6 text-center text-sm text-zinc-400">
              No creators found for “{query}”
            </div>
          )}
        </div>
      </div>
    </div>
  );
}

function CreatorTab({
  info,
  onNavigate,
}: {
  info: CharacterCreatorInfo;
  onNavigate: () => void;
}) {
  const Icon = info.icon;

  return (
    <div
      onClick={onNavigate}
      className="group relative cursor-pointer overflow-hidden rounded-2xl border bg-zinc-950/40 p-5 transition hover:-translate-y-0.5 hover:bg-zinc-950/60"
      style={{ borderColor: `${info.colour}55` }}
    >
      {/* Top accent bar */}
      <div
        className="absolute inset-x-0 top-0 h-1"
        style={{ backgroundColor: info.colour }}
      />

      <div className="flex gap-4">
        {/* Icon */}
        <div
          className="flex h-12 w-12 shrink-0 items-center justify-center rounded-2xl border"
          style={{
            borderColor: `${info.colour}55`,
            backgroundColor: `${info.colour}22`,
          }}
        >
          <Icon className="text-xl" style={{ color: info.colour }} />
        </div>

        {/* Content */}
        <div className="min-w-0">
          <h2
            className="truncate text-lg font-semibold"
            style={{ color: info.colour }}
          >
            {info.title}
          </h2>

          <p className="mt-1 line-clamp-2 text-sm text-zinc-300">
            {info.description}
          </p>

          <div className="mt-4">
            <button
              onClick={(e) => {
                e.stopPropagation();
                onNavigate();
              }}
              className="inline-flex items-center gap-2 rounded-xl border px-3 py-2 text-sm font-medium transition hover:bg-zinc-900/60"
              style={{
                borderColor: `${info.colour}55`,
                color: info.colour,
              }}
            >
              Visit Creator →
            </button>
          </div>
        </div>
      </div>
    </div>
  );
}
