import FeaturesBox from "../components/FeaturesBox";

export default function FeaturesSection() {
  return (
    <section
      id="discover"
      className="py-32 bg-[var(--color-foreground)] text-[var(--color-background)] transition-colors duration-300"
    >
      <div className="container mx-auto px-6">
        <h2 className="text-4xl md:text-5xl font-bold text-center mb-12 tracking-wide">
          Discover Our Features
        </h2>
        <div className="grid grid-cols-1 md:grid-cols-3 gap-12">
          <FeaturesBox 
            title="Tutorials" 
            description="Dive into comprehensive guides and tutorials covering TTRPG mechanics and video game strategies." 
            link="/tutorials" 
            tag="Learn More" 
          />
          <FeaturesBox 
            title="Character Creation" 
            description="Craft your unique characters with our intuitive creation tools and detailed resources." 
            link="/character-creation" 
            tag="Start Creating" 
          />
          <FeaturesBox 
            title="Wikis & Lore" 
            description="Explore expansive lore, rich histories, and detailed wikis of your favorite game universes." 
            link="/wikis" 
            tag="Discover More" 
          />
        </div>
      </div>
    </section>
  );
}
