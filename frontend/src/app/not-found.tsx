'use client'

import { useRouter } from "next/navigation";


export default function NotFound() {

  const router = useRouter()
  return (
    <div className="flex flex-col items-center justify-center min-h-screen bg-gray-100 px-2">
      <h1 className="text-4xl font-bold text-red-600">404</h1>
      <h1 className="text-4xl font-bold text-red-600">Page Not Found</h1>
      <p className="text-lg text-gray-700 mt-4 text-center w-1/2">
        Oops! The page you are looking for does not exist.
      </p>
      <a href="/" className="mt-6 px-4 py-2 bg-blue-600 text-white rounded-lg">
        Go Home
      </a>
      <a onClick={() => router.back()} className="mt-6 px-4 py-2 bg-blue-600 text-white rounded-lg">
        Go Back
      </a>
    </div>
  );
}
