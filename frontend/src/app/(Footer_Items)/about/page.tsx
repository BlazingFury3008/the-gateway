import React from 'react';

export default function Page() {
  return (
    <div className="flex flex-col items-center justify-center min-h-screen bg-gray-900 p-6">
      <div className="max-w-3xl w-full bg-gray-800 p-8 rounded-2xl shadow-lg">
        <h1 className="text-4xl font-bold text-center text-white mb-6">About Me</h1>
        <p className="text-lg text-gray-300 leading-relaxed text-center">
          Hi, I'm Aiden, a passionate developer with a love for technology, gaming, and interactive storytelling. My goal
          is to create tools and platforms that empower players and developers to bring their ideas to life.
        </p>
        <p className="mt-4 text-lg text-gray-300 leading-relaxed text-center">
          My journey began with the development of a character creation app for Hunter: The Reckoning 5th Edition,
          followed by a website designed for a small community to craft their own Vampire: The Masquerade 5th Edition
          characters. These projects deepened my commitment to innovation in the gaming space.
        </p>
        <p className="mt-4 text-lg text-gray-300 leading-relaxed text-center">
          Today, I continue to explore new ways to enhance storytelling and gameplay experiences. Whether you're a player
          looking for better tools or a creator developing your next project, I'm here to support your journey.
        </p>
        <p className="mt-6 text-lg text-gray-300 text-center">
          Have questions or ideas? Reach out to me <a href="/contact" className="text-blue-400">here</a>
        </p>
      </div>
    </div>
  );
}
