/* eslint-disable @typescript-eslint/no-explicit-any */
"use client";

import { useState, useEffect } from "react";

type EventItem = {
  id?: string | number;
  name: string;
  date: string;
  description: string;
};

export default function Events() {
  const [events, setEvents] = useState<EventItem[]>([]);
  const [loading, setLoading] = useState(true);
  const [err, setErr] = useState<string | null>(null);

  const amount = 4;

  useEffect(() => {
    const controller = new AbortController();

    async function load() {
      try {
        setLoading(true);
        setErr(null);

        const base = process.env.NEXT_PUBLIC_FLASK_API_BASE;
        if (!base) throw new Error("Missing NEXT_PUBLIC_FLASK_API_BASE");

        const res = await fetch(`${base}/data/events?amount=${amount}`, {
          method: "GET",
          headers: {
            "Content-Type": "application/json",
            "X-API-Key": process.env.NEXT_PUBLIC_DATA_API_KEY ?? "",
          },
          cache: "no-store",
          signal: controller.signal,
        });

        const data = await res.json().catch(() => null);

        if (!res.ok) {
          throw new Error(data?.error || "Failed to load events");
        }

        setEvents(Array.isArray(data) ? data : []);
      } catch (e: any) {
        if (e?.name === "AbortError") return;
        setErr(e?.message || "Failed to load events");
      } finally {
        setLoading(false);
      }
    }

    load();
    return () => controller.abort();
  }, []);

  return (
    <section id="events" className="section section-light scroll-mt-16">
      <h2 className="section-title">Events</h2>
      <p className="text-sm text-[var(--muted)] -mt-3">
        Browse the latest events.
      </p>

      <div className="grid gap-6 sm:grid-cols-2 lg:grid-cols-3">
        {loading && (
          <div className="p-4 text-sm text-[var(--muted)]">Loading events</div>
        )}

        {!loading && err && (
          <div className="p-4 text-sm text-red-500">{err}</div>
        )}

        {!loading && !err && events.length === 0 && (
          <div className="p-4 text-sm text-[var(--muted)]">
            No events found.
          </div>
        )}

        {events.map((e) => (
          <div
            key={e.id ?? `${e.name}-${e.date}`}
            className="card flex flex-col"
          >
            <h3 className="font-semibold text-lg mb-1">{e.name}</h3>
            <p className="text-sm text-[var(--muted)] mb-2">{e.date}</p>
            <p className="text-sm flex-grow">{e.description}</p>
            <button className="hero-button mt-3 self-start px-3 py-1 text-sm">
              Learn More
            </button>
          </div>
        ))}
      </div>
    </section>
  );
}
