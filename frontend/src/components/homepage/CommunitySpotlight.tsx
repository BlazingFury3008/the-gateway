import Image from "next/image";

export default function CommunitySpotlight() {
  return (
    <section className="py-10 bg-white">
      <div className="container mx-auto px-4">
        <h2 className="text-3xl font-bold text-center mb-8">Community Spotlight</h2>
        <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
          {/* Spotlight 1 */}
          <div className="bg-gray-100 p-6 rounded-lg shadow">
            <div className="flex items-center mb-4">
              <Image
                src="/images/user1.jpg" // Update with your image path
                alt="User 1"
                width={60}
                height={60}
                className="rounded-full"
              />
              <div className="ml-4">
                <h4 className="text-lg font-bold">Alex Johnson</h4>
                <span className="text-sm text-gray-600">Game Master</span>
              </div>
            </div>
            <p>
              &ldquo;The Gateway has transformed the way I engage with my players. The resources and community support are unmatched!&rdquo;
            </p>
          </div>
          {/* Spotlight 2 */}
          <div className="bg-gray-100 p-6 rounded-lg shadow">
            <div className="flex items-center mb-4">
              <Image
                src="/images/user2.jpg" // Update with your image path
                alt="User 2"
                width={60}
                height={60}
                className="rounded-full"
              />
              <div className="ml-4">
                <h4 className="text-lg font-bold">Maria Garcia</h4>
                <span className="text-sm text-gray-600">Content Creator</span>
              </div>
            </div>
            <p>
              &ldquo;From tutorials to character creation, every aspect of The Gateway fuels my creativity and passion for gaming.&rdquo;
            </p>
          </div>
        </div>
      </div>
    </section>
  );
}
