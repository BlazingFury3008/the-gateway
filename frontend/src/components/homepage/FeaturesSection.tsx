export default function FeaturesSection() {
    return (
      <section className="py-10 bg-gray-300 text-gray-700">
        <div className="container mx-auto px-4">
          <h2 className="text-3xl font-bold text-center mb-8">Discover Our Features</h2>
          <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
            {/* Tutorials Feature */}
            <div className="bg-white p-6 rounded-lg shadow">
              <h3 className="text-xl font-semibold mb-2">Tutorials</h3>
              <p className="mb-4">
                Dive into comprehensive guides and tutorials covering TTRPG mechanics and video game strategies.
              </p>
              <a href="/tutorials" className="text-blue-600 hover:underline">
                Learn More
              </a>
            </div>
            {/* Character Creation Feature */}
            <div className="bg-white p-6 rounded-lg shadow">
              <h3 className="text-xl font-semibold mb-2">Character Creation</h3>
              <p className="mb-4">
                Craft your unique characters with our intuitive creation tools and detailed resources.
              </p>
              <a href="/character-creation" className="text-blue-600 hover:underline">
                Start Creating
              </a>
            </div>
            {/* Wikis & Lore Feature */}
            <div className="bg-white p-6 rounded-lg shadow">
              <h3 className="text-xl font-semibold mb-2">Wikis & Lore</h3>
              <p className="mb-4">
                Explore expansive lore, rich histories, and detailed wikis of your favorite game universes.
              </p>
              <a href="/wikis" className="text-blue-600 hover:underline">
                Discover More
              </a>
            </div>
          </div>
        </div>
      </section>
    );
  }
  