import Image from "next/image";

export default function LatestNewsSection() {
  return (
    <section className="py-10 bg-white">
      <div className="container mx-auto px-4">
        <h2 className="text-3xl font-bold text-center mb-8">Latest News</h2>
        <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
          {/* News Card 1 */}
          <div className="bg-gray-100 rounded-lg overflow-hidden shadow">
            <Image
              src="/images/news1.jpg" // Update with your image path
              alt="News article 1"
              width={400}
              height={250}
              className="w-full"
            />
            <div className="p-6">
              <h3 className="text-xl font-semibold mb-2">Epic Expansion Released</h3>
              <p className="mb-4">
                Discover the new expansion that brings more adventures, characters, and realms to explore.
              </p>
              <a href="/news/epic-expansion" className="text-blue-600 hover:underline">
                Read More
              </a>
            </div>
          </div>
          {/* News Card 2 */}
          <div className="bg-gray-100 rounded-lg overflow-hidden shadow">
            <Image
              src="/images/news2.jpg" // Update with your image path
              alt="News article 2"
              width={400}
              height={250}
              className="w-full"
            />
            <div className="p-6">
              <h3 className="text-xl font-semibold mb-2">Developer Insights</h3>
              <p className="mb-4">
                Get an exclusive look into the minds of our developers as they share behind-the-scenes details.
              </p>
              <a href="/news/developer-insights" className="text-blue-600 hover:underline">
                Read More
              </a>
            </div>
          </div>
          {/* News Card 3 */}
          <div className="bg-gray-100 rounded-lg overflow-hidden shadow">
            <Image
              src="/images/news3.jpg" // Update with your image path
              alt="News article 3"
              width={400}
              height={250}
              className="w-full"
            />
            <div className="p-6">
              <h3 className="text-xl font-semibold mb-2">Community Milestone</h3>
              <p className="mb-4">
                Join us in celebrating a milestone as our community reaches new heights.
              </p>
              <a href="/news/community-milestone" className="text-blue-600 hover:underline">
                Read More
              </a>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
}
