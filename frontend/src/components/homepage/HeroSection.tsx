"use client";
import { useState, useEffect } from "react";
import Image from "next/image";
import { randomInt } from "crypto";

export default function HeroSection() {
  const images = [
    "/static/Carousel-Images/Hunter_Logo_white.svg",
    "/static/Carousel-Images/VampireLogoBIGred.svg",
    "/static/Carousel-Images/WEREWOLF_NewLogo_white.svg",
  ];

  // Add the first image at the end to create a seamless loop
  const extendedImages = [...images, images[0]];

  const [currentIndex, setCurrentIndex] = useState(Math.floor(Math.random() * images.length));
  const [isTransitioning, setIsTransitioning] = useState(true);
  const transitionDuration = 1000; // 1 second transition
  const slideInterval = 5000; // 5 seconds per slide

  useEffect(() => {
    const timer = setInterval(() => {
      setCurrentIndex((prevIndex) => prevIndex + 1);
    }, slideInterval);

    return () => clearInterval(timer);
  }, []);

  // When reaching the duplicate image, reset the index **without transition**
  useEffect(() => {
    if (currentIndex === images.length) {
      setTimeout(() => {
        setIsTransitioning(false); // Disable transition
        setCurrentIndex(0); // Reset index instantly

        // Re-enable transition after a slight delay
        setTimeout(() => setIsTransitioning(true), 50);
      }, transitionDuration);
    }
  }, [currentIndex]);

  return (
    <section className="relative h-96 w-full overflow-hidden flex items-center justify-center mb-8">
      {/* Scrolling Image Slider */}
      <div
        className="absolute inset-0 flex"
        style={{
          transform: `translateX(-${currentIndex * 100}%)`,
          transition: isTransitioning ? `transform ${transitionDuration}ms ease-in-out` : "none",
        }}
      >
        {extendedImages.map((image, index) => (
          <div
            key={index}
            className="w-full h-full flex-shrink-0 relative flex items-center justify-center opacity-85"
          >
            <Image
              src={image}
              alt={`Slide ${index + 1}`}
              fill
              priority={index === 0}
              className="object-contain w-auto h-auto max-w-full max-h-full"
              quality={100}
            />
          </div>
        ))}
      </div>

      {/* Overlay */}
      <div className="absolute inset-0 bg-black opacity-50"></div>

      {/* Hero Text and CTA */}
      <div className="absolute inset-0 flex flex-col justify-center items-center text-white text-center px-4">
        <h1 className="text-4xl md:text-6xl font-bold">Welcome to The Gateway</h1>
        <p className="mt-4 max-w-xl">
          Your ultimate hub for all things TTRPG and video game adventures.
          Whether you’re exploring new worlds or crafting your own, you’re in
          the right place.
        </p>
        <a
          href="/explore"
          className="mt-6 bg-blue-600 hover:bg-blue-700 text-white px-6 py-3 rounded-full text-lg"
        >
          Explore Now
        </a>
      </div>
    </section>
  );
}
