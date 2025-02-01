"use client";
import { useState, useEffect } from "react";
import Image from "next/image";

export default function HeroSection() {
  // Array of hero image paths
  const images = [
    "/static/Carousel-Images/Hunter_Logo_white.svg",
    "static/Carousel-Images/VampireLogoBIGred.svg",
    "/static/Carousel-Images/WEREWOLF_NewLogo_white.svg",
  ];

  // State to track the current image index
  const [currentIndex, setCurrentIndex] = useState(0);

  useEffect(() => {
    const timer = setInterval(() => {
      setCurrentIndex((prevIndex) => (prevIndex + 1) % images.length);
    }, 5000); // Change image every 5 seconds

    return () => clearInterval(timer);
  }, [images.length]);

  return (
    <section className="relative h-96 w-full overflow-hidden flex items-center justify-center">
      {/* Image Slider Container */}
      <div
        className="absolute inset-0 flex transition-transform duration-1000 ease-in-out"
        style={{ transform: `translateX(-${currentIndex * 100}%)` }}
      >
        {images.map((image, index) => (
          <div
            key={index}
            className="w-full h-full flex-shrink-0 relative flex items-center justify-center opacity-85"
          >
            <Image
              src={image}
              alt={`Slide ${index + 1}`}
              fill
              priority={index === 0} // Prioritize first image for faster loading
              className="object-contain w-auto h-auto max-w-full max-h-full"
              quality={100}
            />
          </div>
        ))}
      </div>

      {/* Overlay for better text contrast */}
      <div className="absolute inset-0 bg-black opacity-50"></div>

      {/* Hero Text and Call-to-Action */}
      <div className="absolute inset-0 flex flex-col justify-center items-center text-white text-center px-4">
        <h1 className="text-4xl md:text-6xl font-bold">
          Welcome to The Gateway
        </h1>
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
