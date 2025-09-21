"use client";
import React, { useEffect, useState } from "react";
import Image from "next/image";

export default function Hero() {
  const images = [
    {
      src: "/Hero-Images/Vampire.png",
      scaleMobile: "scale-100",
      scaleDesktop: "scale-150",
      darkInvert: false,
    },
    {
      src: "/Hero-Images/Werewolf.png",
      scaleMobile: "scale-90",
      scaleDesktop: "scale-120",
      darkInvert: true,
    },
  ];

  const intervalTime = 5000;
  const [current, setCurrent] = useState(0);
  const [progressing, setProgressing] = useState(false);
  const [theme, setTheme] = useState<"light" | "dark">("light");

  // Auto-advance carousel
  useEffect(() => {
    const timer = setInterval(() => {
      setCurrent((prev) => (prev + 1) % images.length);
    }, intervalTime);
    return () => clearInterval(timer);
  }, [images.length]);

  // Restart progress bar animation
  useEffect(() => {
    setProgressing(false);
    const t = setTimeout(() => setProgressing(true), 50);
    return () => clearTimeout(t);
  }, [current]);

  // Detect theme (based on <html data-theme="...">)
  useEffect(() => {
    const observer = new MutationObserver(() => {
      const docTheme = document.documentElement.getAttribute("data-theme");
      if (docTheme === "dark" || docTheme === "light") {
        setTheme(docTheme);
      }
    });
    observer.observe(document.documentElement, {
      attributes: true,
      attributeFilter: ["data-theme"],
    });
    return () => observer.disconnect();
  }, []);

  // Smooth scroll helper
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
            const invertClass =
              theme === "dark" && img.darkInvert ? "invert" : "";
            return (
              <div
                key={idx}
                className="relative w-full h-full flex-shrink-0 flex items-center justify-center bg-[var(--background)]"
              >
                <Image
                  src={img.src}
                  alt={`Slide ${idx}`}
                  fill
                  className={`object-contain opacity-80 select-none pointer-events-none 
                    ${img.scaleMobile} sm:${img.scaleDesktop} ${invertClass}`}
                  priority={idx === 0}
                />
              </div>
            );
          })}
        </div>
        <div className="absolute inset-0 bg-black/40 -z-10" />
      </div>

      {/* Foreground content */}
      <div className="absolute bottom-6 left-1/2 -translate-x-1/2 flex flex-col items-center gap-3 z-10 w-full px-4">
        {/* Buttons */}
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

        {/* Indicators */}
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
