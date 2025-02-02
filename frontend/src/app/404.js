'use client'; // This file must be a client component

import { useEffect } from 'react';

export default function GlobalError({ error, reset }) {
  useEffect(() => {
    // Log the error to an error reporting service if needed
    console.error('Global error boundary caught an error:', error);
  }, [error]);

  return (
    <html>
      <head>
        <title>Something went wrong</title>
      </head>
      <body className="min-h-screen flex flex-col items-center justify-center px-4 text-center">
        <h1 className="text-4xl font-bold mb-4">Oops, an error occurred!</h1>
        <p className="mb-8">We are working to fix the issue. Please try again later.</p>
        <button
          onClick={() => reset()}
          className="bg-blue-600 hover:bg-blue-700 text-white px-6 py-3 rounded-full"
        >
          Try Again
        </button>
      </body>
    </html>
  );
}
