import React from "react";

export default function Forums() {
  const threads = [
    { title: "Best builds for beginners?", replies: 42, author: "Alice" },
    { title: "Lore discussion: hidden details", replies: 15, author: "Bob" },
    { title: "Introduce yourself!", replies: 88, author: "Charlie" },
    { title: "PvP balance feedback", replies: 23, author: "Dana" },
    { title: "Fan art megathread", replies: 61, author: "Eli" },
  ];

  // Only show first 4 on homepage
  const visibleThreads = threads.slice(0, 4);

  return (
    <section id="forums" className="section section-dark scroll-mt-16">
      <h2 className="section-title">Forums</h2>

      <div className="divide-y divide-[var(--border)] border border-[var(--border)] rounded-lg overflow-hidden">
        {visibleThreads.map((t, idx) => (
          <div
            key={idx}
            className="p-4 hover:bg-[var(--background)]/50 transition flex justify-between items-center"
          >
            <div>
              <h3 className="font-medium">{t.title}</h3>
              <p className="text-sm text-[var(--muted)]">
                Posted by {t.author} • {t.replies} replies
              </p>
            </div>
            <button className="hero-button text-sm px-3 py-1">View</button>
          </div>
        ))}
      </div>

      {/* See All */}
      <div className="flex justify-center mt-8">
        <button className="hero-button px-6 py-2 text-base">
          See All Forums
        </button>
      </div>
    </section>
  );
}
