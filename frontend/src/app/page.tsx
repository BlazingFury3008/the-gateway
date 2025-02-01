import CommunitySpotlight from "@/components/homepage/CommunitySpotlight";
import FeaturesSection from "@/components/homepage/FeaturesSection";
import HeroSection from "@/components/homepage/HeroSection";
import LatestNewsSection from "@/components/homepage/LatestNewsSection";
import UpcomingEventsSection from "@/components/homepage/UpcommingEventsSection";
import Image from "next/image";
import Link from "next/link";

export default function Home() {
  return (
    <main>
      <HeroSection />
      <FeaturesSection />
      <LatestNewsSection />
      <UpcomingEventsSection />
      <CommunitySpotlight />
    </main>
  );
}
