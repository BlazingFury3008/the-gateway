import Link from 'next/link';
import React from 'react';

export default function FeaturesBox({
  title,
  description,
  link,
  tag,
}: {
  title: string;
  description: string;
  link: string;
  tag: string;
}) {
  return (
    <Link href={link}>
      <div className="bg-white p-8 rounded-lg shadow-lg transform hover:scale-105 transition-transform duration-300 cursor-pointer">
        <h3 className="text-2xl font-semibold mb-3">{title}</h3>
        <p className="mb-6">{description}</p>
        <span className="inline-block text-blue-600 hover:underline font-medium">
          {tag}
        </span>
      </div>
    </Link>
  );
}
