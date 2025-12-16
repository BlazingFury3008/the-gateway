/* eslint-disable @typescript-eslint/no-explicit-any */
"use client";

import React, { useEffect, useState } from "react";

type NewsArticle = {
  id?: string | number;
  title: string;
  date: string;
  snippet: string;
};

export default function News() {
  const [articles, setArticles] = useState<NewsArticle[]>([]);
  const [loading, setLoading] = useState(true);
  const [err, setErr] = useState<string | null>(null);

  const amount = 6;

  useEffect(() => {
    const controller = new AbortController();

    async function load() {
      try {
        setLoading(true);
        setErr(null);

        const base = process.env.NEXT_PUBLIC_FLASK_API_BASE;
        if (!base) throw new Error("Missing NEXT_PUBLIC_FLASK_API_BASE");

        const res = await fetch(`${base}/data/news?amount=${amount}`, {
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
          throw new Error(data?.error || "Failed to load news");
        }

        setArticles(Array.isArray(data) ? data : []);
      } catch (e: any) {
        if (e?.name === "AbortError") return;
        setErr(e?.message || "Failed to load news");
      } finally {
        setLoading(false);
      }
    }

    load();
    return () => controller.abort();
  }, []);

  return (
    <section id="news" className="section section-light scroll-mt-16">
      <h2 className="section-title">News</h2>
      <p className="text-sm text-[var(--muted)] -mt-3">
        Browse the latest news.
      </p>
      <div className="grid gap-6 sm:grid-cols-1 md:grid-cols-2 lg:grid-cols-3">
        {loading && (
          <div className="p-4 text-sm text-[var(--muted)]">Loading news</div>
        )}

        {!loading && err && (
          <div className="p-4 text-sm text-red-500">{err}</div>
        )}

        {!loading && !err && articles.length === 0 && (
          <div className="p-4 text-sm text-[var(--muted)]">No news found.</div>
        )}

        {articles.map((a) => (
          <article key={a.id ?? `${a.title}-${a.date}`} className="card">
            <h3 className="font-semibold text-lg mb-1">{a.title}</h3>
            <p className="text-sm text-[var(--muted)] mb-2">{a.date}</p>
            <p className="text-sm">{a.snippet}</p>
          </article>
        ))}
      </div>

      <div className="flex justify-center mt-8">
        <button className="hero-button px-6 py-2 text-base">
          See All News
        </button>
      </div>
    </section>
  );
}
