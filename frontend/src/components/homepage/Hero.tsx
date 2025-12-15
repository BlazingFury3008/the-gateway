"use client";

import React, { useEffect, useState } from "react";
import Image from "next/image";
import { useTheme } from "@/app/theme-provider";

type HeroImage = {
  src: string;
  scaleMobile: number;
  scaleDesktop: number;
  translateYMobile: string;
  translateYDesktop: string;
  darkInvert?: boolean;
};

export default function Hero() {
  const images: HeroImage[] = [
    {
      src: "/Hero-Images/Vampire.png",
      scaleMobile: 1.5,
      scaleDesktop: 1.4,
      translateYMobile: "0px",
      translateYDesktop: "0px",
      darkInvert: false,
    },
    {
      src: "/Hero-Images/Werewolf.png",
      scaleMobile: 0.5,
      scaleDesktop: .5,
      translateYMobile: "0px",
      translateYDesktop: "0px",
      darkInvert: true,
    },
  ];

  const intervalTime = 5000;
  const [current, setCurrent] = useState(0);
  const [progressing, setProgressing] = useState(false);
  const { theme } = useTheme();

  // Track breakpoint in JS (matches Tailwind's sm: 640px)
  const [isDesktop, setIsDesktop] = useState(false);
  useEffect(() => {
    const mq = window.matchMedia("(min-width: 640px)");
    const apply = () => setIsDesktop(mq.matches);
    apply();
    mq.addEventListener?.("change", apply);
    return () => mq.removeEventListener?.("change", apply);
  }, []);

  // Auto-advance carousel
  useEffect(() => {
    const timer = setInterval(() => {
      setCurrent((prev) => (prev + 1) % images.length);
    }, intervalTime);
    return () => clearInterval(timer);
  }, [images.length]);

  // Restart progress bar animation when image changes
  useEffect(() => {
    setProgressing(false);
    const t = setTimeout(() => setProgressing(true), 50);
    return () => clearTimeout(t);
  }, [current]);

  const scrollToSection = (id: string) => {
    const el = document.getElementById(id);
    if (el) el.scrollIntoView({ behavior: "smooth" });
  };

  return (
    <div className="relative h-[300px] sm:h-[400px] flex items-center justify-center overflow-hidden z-0">
      {/* Background carousel */}
      <div className="absolute inset-0 -z-10 select-none pointer-events-none">
        <div
          className="flex h-full w-full transition-transform duration-1000 ease-in-out"
          style={{ transform: `translateX(-${current * 100}%)` }}
        >
          {images.map((img, idx) => {
            const shouldInvert = theme === "dark" && img.darkInvert;

            const scale = isDesktop ? img.scaleDesktop : img.scaleMobile;
            const ty = isDesktop ? img.translateYDesktop : img.translateYMobile;

            return (
              <div
                key={idx}
                className="relative w-full h-full flex-shrink-0 flex items-center justify-center bg-[var(--background)]"
              >
                {/* Transform wrapper YOU control (this is the important part) */}
                <div
                  className="absolute inset-0"
                  style={{
                    transform: `translateY(${ty}) scale(${scale})`,
                    transformOrigin: "center",
                    transition: "transform 500ms ease",
                    filter: shouldInvert ? "invert(1)" : "none",
                  }}
                >
                  <Image
                    src={img.src}
                    alt={`Slide ${idx}`}
                    fill
                    priority={idx === 0}
                    className="object-contain opacity-80 select-none pointer-events-none"
                  />
                </div>
              </div>
            );
          })}
        </div>

        {/* Overlay */}
        <div
          className="absolute inset-0 -z-10"
          style={{
            backgroundColor:
              theme === "dark" ? "rgba(0,0,0,0.55)" : "rgba(0,0,0,0.40)",
          }}
        />
      </div>

      {/* Foreground content */}
      <div className="absolute bottom-6 left-1/2 -translate-x-1/2 flex flex-col items-center gap-3 z-10 w-full px-4">
        <div className="flex flex-col sm:flex-row flex-wrap gap-2 sm:gap-4 w-full sm:w-auto">
          <button
            className="hero-button w-full sm:w-auto text-base sm:text-sm py-3 sm:py-1 bg-opacity-80 sm:bg-opacity-100"
            onClick={() => scrollToSection("news")}
          >
            News
          </button>
          <button
            className="hero-button w-full sm:w-auto text-base sm:text-sm py-3 sm:py-1 bg-opacity-80 sm:bg-opacity-100"
            onClick={() => scrollToSection("forums")}
          >
            Forums
          </button>
          <button
            className="hero-button w-full sm:w-auto text-base sm:text-sm py-3 sm:py-1 bg-opacity-80 sm:bg-opacity-100"
            onClick={() => scrollToSection("events")}
          >
            Events
          </button>
          <button className="hero-button w-full sm:w-auto text-base sm:text-sm py-3 sm:py-1 bg-opacity-80 sm:bg-opacity-100">
            Random Wiki
          </button>
          <button className="hero-button w-full sm:w-auto text-base sm:text-sm py-3 sm:py-1 bg-opacity-80 sm:bg-opacity-100">
            Random Profile
          </button>
        </div>

        <div className="flex gap-1 sm:gap-2 mt-2 items-center">
          {images.map((_, idx) => {
            const isPast = idx < current;
            const isActive = idx === current;

            return (
              <div
                key={idx}
                className="h-2 rounded-full bg-gray-500/40 overflow-hidden transition-all duration-500"
                style={{
                  width: isActive ? "2rem" : "0.5rem",
                  backgroundColor: isPast
                    ? "var(--primary)"
                    : "rgba(107,114,128,0.4)",
                }}
              >
                {isActive && (
                  <div
                    className="h-full bg-[var(--primary)]"
                    style={{
                      width: progressing ? "100%" : "0%",
                      transition: progressing
                        ? `width ${intervalTime}ms linear`
                        : "none",
                    }}
                  />
                )}
              </div>
            );
          })}
        </div>
      </div>
    </div>
  );
}
