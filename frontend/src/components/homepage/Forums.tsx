/* eslint-disable @typescript-eslint/no-explicit-any */
"use client";

import React, { useEffect, useState } from "react";
import { useRouter } from "next/navigation";

type Forum = {
  id: string;
  title: string;
  description?: string | null;
};

export default function Forums() {
  const router = useRouter();

  const [forums, setForums] = useState<Forum[]>([]);
  const [loading, setLoading] = useState(true);
  const [err, setErr] = useState<string | null>(null);

  const amount = 4;

  useEffect(() => {
    let cancelled = false;

    async function load() {
      try {
        setLoading(true);
        setErr(null);

        const res = await fetch(
          `${process.env.NEXT_PUBLIC_FLASK_API_BASE}/data/forum?amount=${amount}`,
          {
            method: "GET",
            headers: {
              "Content-Type": "application/json",
              "X-API-Key": process.env.NEXT_PUBLIC_DATA_API_KEY ?? "",
            },
            cache: "no-store",
          }
        );

        const data = await res.json().catch(() => null);

        if (!res.ok) {
          throw new Error(data?.error || "Failed to load forums");
        }

        if (!cancelled) {
          setForums(Array.isArray(data) ? data : []);
        }
      } catch (e: any) {
        if (!cancelled) setErr(e?.message || "Failed to load forums");
      } finally {
        if (!cancelled) setLoading(false);
      }
    }

    load();
    return () => {
      cancelled = true;
    };
  }, []);

  return (
    <section id="forums" className="section section-dark scroll-mt-16">
      <div className="flex items-end justify-between gap-4">
        <div>
          <h2 className="section-title">Forums</h2>
          <p className="text-sm text-[var(--muted)] -mt-3">
            Browse the latest forum categories.
          </p>
        </div>

        <button
          onClick={() => router.push("/forums")}
          className="hero-button px-6 py-2 text-base"
          type="button"
        >
          See All Forums
        </button>
      </div>

      <div className="mt-6 border border-[var(--border)] rounded-lg overflow-hidden">
        {loading && (
          <div className="p-4 text-sm text-[var(--muted)]">Loading forums…</div>
        )}

        {!loading && err && (
          <div className="p-4 text-sm text-red-500">{err}</div>
        )}

        {!loading && !err && forums.length === 0 && (
          <div className="p-4 text-sm text-[var(--muted)]">
            No forums found.
          </div>
        )}

        {!loading && !err && forums.length > 0 && (
          <div className="divide-y divide-[var(--border)]">
            {forums.map((f) => (
              <div
                key={f.id}
                className="p-4 hover:bg-[var(--background)]/50 transition flex justify-between items-center gap-4"
              >
                <div className="min-w-0">
                  <h3 className="font-medium truncate">{f.title}</h3>
                  <p className="text-sm text-[var(--muted)] truncate">
                    {f.description?.trim()
                      ? f.description
                      : "No description provided."}
                  </p>
                </div>

                <button
                  type="button"
                  onClick={() => router.push(`/forums/${f.id}`)}
                  className="hero-button text-sm px-3 py-1 whitespace-nowrap"
                >
                  View
                </button>
              </div>
            ))}
          </div>
        )}
      </div>
    </section>
  );
}
