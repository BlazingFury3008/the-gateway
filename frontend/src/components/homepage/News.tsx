import React from "react";

export default function News() {
  const articles = [
    { title: "Big Update Coming Soon!", date: "2025-09-20", snippet: "We're working on a huge content patch with new features..." },
    { title: "Community Spotlight", date: "2025-09-15", snippet: "Check out the incredible mods and fan art from our players!" },
    { title: "Patch Notes v1.2", date: "2025-09-10", snippet: "Bug fixes, balance changes, and quality-of-life improvements." },
    { title: "Upcoming Maintenance", date: "2025-09-05", snippet: "Servers will be down for scheduled upgrades and fixes." },
    { title: "New Expansion Teased!", date: "2025-08-30", snippet: "Hints of new lands and adventures on the horizon..." },
    { title: "Q&A with the Devs", date: "2025-08-25", snippet: "Developers answer your most asked questions live!" },
    { title: "Community Contest Winners", date: "2025-08-20", snippet: "Congratulations to the top submissions!" },
  ];

  // Slice based on breakpoint logic
  const visibleArticles = articles.slice(0, 6); // cap to 6 for large

  return (
    <section id="news" className="section section-light scroll-mt-16">
      <h2 className="section-title">News</h2>

      {/* Responsive grid */}
      <div className="grid gap-6 sm:grid-cols-1 md:grid-cols-2 lg:grid-cols-3">
        {visibleArticles.map((a, idx) => {
          // Hide beyond 4 on md, beyond 6 on lg
          const isHiddenMd = idx >= 4; // hide after 4 on md
          const isHiddenLg = idx >= 6; // hide after 6 on lg
          return (
            <article
              key={idx}
              className={`card ${
                (isHiddenMd ? "hidden md:block" : "") ||
                (isHiddenLg ? "hidden lg:block" : "")
              }`}
            >
              <h3 className="font-semibold text-lg mb-1">{a.title}</h3>
              <p className="text-sm text-[var(--muted)] mb-2">{a.date}</p>
              <p className="text-sm">{a.snippet}</p>
            </article>
          );
        })}
      </div>

      {/* See All */}
      <div className="flex justify-center mt-8">
        <button className="hero-button px-6 py-2 text-base">
          See All News
        </button>
      </div>
    </section>
  );
}
