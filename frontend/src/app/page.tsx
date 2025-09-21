import Events from "@/components/homepage/Events";
import Forums from "@/components/homepage/Forums";
import Hero from "@/components/homepage/Hero";
import News from "@/components/homepage/News";

export default function Home() {
  return (
    <div className="font-sans">
      <Hero />
      <News />
      <Forums />
      <Events />
    </div>
  );
}
