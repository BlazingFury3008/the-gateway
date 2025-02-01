export default function UpcomingEventsSection() {
    return (
      <section className="py-10 bg-gray-100">
        <div className="container mx-auto px-4">
          <h2 className="text-3xl font-bold text-center mb-8">Upcoming Events</h2>
          <div className="space-y-6">
            {/* Event 1 */}
            <div className="bg-white p-6 rounded-lg shadow flex flex-col md:flex-row md:items-center">
              <div className="md:w-1/4">
                <span className="text-lg font-bold">March 15, 2025</span>
              </div>
              <div className="md:w-3/4">
                <h3 className="text-xl font-semibold">Live Q&amp;A with the Developers</h3>
                <p className="mb-2">
                  Join our live session to ask questions, get insights, and interact with our development team.
                </p>
                <a href="/events/live-qa" className="text-blue-600 hover:underline">
                  Learn More
                </a>
              </div>
            </div>
            {/* Event 2 */}
            <div className="bg-white p-6 rounded-lg shadow flex flex-col md:flex-row md:items-center">
              <div className="md:w-1/4">
                <span className="text-lg font-bold">April 5, 2025</span>
              </div>
              <div className="md:w-3/4">
                <h3 className="text-xl font-semibold">Virtual Art Expo</h3>
                <p className="mb-2">
                  Explore fan art, character designs, and behind-the-scenes visuals from our community and artists.
                </p>
                <a href="/events/art-expo" className="text-blue-600 hover:underline">
                  Discover More
                </a>
              </div>
            </div>
            {/* Event 3 */}
            <div className="bg-white p-6 rounded-lg shadow flex flex-col md:flex-row md:items-center">
              <div className="md:w-1/4">
                <span className="text-lg font-bold">May 10, 2025</span>
              </div>
              <div className="md:w-3/4">
                <h3 className="text-xl font-semibold">TTRPG Workshop Series</h3>
                <p className="mb-2">
                  Enhance your gameplay and storytelling skills in our interactive workshop series.
                </p>
                <a href="/events/workshop-series" className="text-blue-600 hover:underline">
                  Sign Up
                </a>
              </div>
            </div>
          </div>
        </div>
      </section>
    );
  }
  