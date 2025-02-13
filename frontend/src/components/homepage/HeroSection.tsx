"use client";
import { useState, useEffect } from "react";
import Image from "next/image";

export default function HeroSection() {
  const transitionDuration = 1000; // Adjust as needed
  const images = [
    "/static/Carousel-Images/Hunter_Logo_white.svg",
    "/static/Carousel-Images/VampireLogoBIGred.svg",
    "/static/Carousel-Images/WEREWOLF_NewLogo_white.svg",
  ];

  // Clone first image at the end for smooth looping
  const loopedImages = [...images, images[0]]; 

  const invertConfig: Record<string, "always" | "dark-only" | "light-only" | "none"> = {
    "/static/Carousel-Images/Hunter_Logo_white.svg": "light-only",
    "/static/Carousel-Images/VampireLogoBIGred.svg": "none",
    "/static/Carousel-Images/WEREWOLF_NewLogo_white.svg": "light-only",
  };

  const [currentIndex, setCurrentIndex] = useState(0);
  const [isTransitioning, setIsTransitioning] = useState(true);
  const [isDarkMode, setIsDarkMode] = useState(false);

  useEffect(() => {
    const checkDarkMode = () => {
      setIsDarkMode(document.documentElement.classList.contains("dark"));
    };

    checkDarkMode();
    const observer = new MutationObserver(checkDarkMode);
    observer.observe(document.documentElement, { attributes: true });

    return () => observer.disconnect();
  }, []);

  useEffect(() => {
    const timer = setInterval(() => {
      setCurrentIndex((prevIndex) => prevIndex + 1);
    }, 5000);

    return () => clearInterval(timer);
  }, []);

  // Reset the index instantly when reaching the cloned slide
  useEffect(() => {
    if (currentIndex === images.length) {
      setTimeout(() => {
        setIsTransitioning(false); // Disable transition momentarily
        setCurrentIndex(0); // Reset index instantly
      }, transitionDuration);

      setTimeout(() => setIsTransitioning(true), transitionDuration + 50); // Re-enable transition
    }
  }, [currentIndex]);

  return (
    <section className="relative min-h-[600px] md:min-h-[900px] w-full overflow-hidden flex items-center justify-center bg-[var(--color-background-soft)] transition-colors duration-300">
      {/* Infinite Scrolling Image Slider */}
      <div
        className="absolute inset-0 flex transition-transform ease-in-out"
        style={{
          transform: `translateX(-${currentIndex * 100}%)`,
          transition: isTransitioning ? `transform ${transitionDuration}ms ease-in-out` : "none",
        }}
      >
        {loopedImages.map((image, index) => {
          let invertClass = "";
          if (invertConfig[image] === "always") {
            invertClass = "invert";
          } else if (invertConfig[image] === "dark-only" && isDarkMode) {
            invertClass = "invert";
          } else if (invertConfig[image] === "light-only" && !isDarkMode) {
            invertClass = "invert";
          }

          return (
            <div
              key={index}
              className="w-full h-full flex-shrink-0 relative flex items-center justify-center opacity-40"
              style={{ width: "100%" }} // Ensures each slide takes full width
            >
              <Image
                src={image}
                alt={`Slide ${index + 1}`}
                fill
                priority={index === 0}
                className={`p-24 object-contain w-auto h-auto max-w-full max-h-full transition-opacity duration-500 ${invertClass}`}
                quality={100}
              />
            </div>
          );
        })}
      </div>

      {/* Overlay for better text contrast */}
      <div className="absolute inset-0 bg-[var(--color-overlay)] transition-colors duration-300"></div>

      {/* Hero Text and Call-to-Action */}
      <div className="absolute inset-0 flex flex-col justify-center items-center text-outline text-[var(--color-foreground)] text-center px-6">
        <h1 className="text-5xl md:text-7xl font-extrabold tracking-wide">
          Welcome to The Gateway
        </h1>
        <p className="mt-6 max-w-2xl text-lg md:text-2xl xs:text-md font-medium leading-relaxed text-[var(--color-foreground-soft)]">
          Your ultimate hub for all things TTRPG and video game adventures.
          Whether you’re exploring new worlds or crafting your own, you’re in
          the right place.
        </p>
        <a
          href="#discover"
          className="mt-8 bg-[var(--color-secondary)] hover:bg-[var(--color-secondary-hover)] text-[var(--color-background)] px-8 py-4 rounded-full text-xl font-semibold shadow-lg transition"
        >
          Explore Now
        </a>
      </div>
    </section>
  );
}
