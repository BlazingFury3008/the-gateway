export default function Events() {
  const events = [
    { name: "Halloween Event", date: "Oct 31, 2025", description: "Spooky quests, limited-time loot, and community contests." },
    { name: "Winter Festival", date: "Dec 15, 2025", description: "Snowball fights, cozy cosmetics, and holiday cheer!" },
    { name: "Spring Tournament", date: "Apr 10, 2026", description: "Competitive matches with unique rewards for winners." },
  ];

  return (
    <section id="events" className="section section-light scroll-mt-16">
      <h2 className="section-title">Events</h2>
      <div className="grid gap-6 sm:grid-cols-2 lg:grid-cols-3">
        {events.map((e, idx) => (
          <div key={idx} className="card flex flex-col">
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
