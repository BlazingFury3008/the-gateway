import Link from 'next/link';

export default function NotFound() {
  return (
    <html>
      <head>
        <title>Page Not Found</title>
      </head>
      <body className="min-h-screen flex flex-col items-center justify-center px-4 text-center">
        <h1 className="text-5xl font-bold mb-4">404 - Page Not Found</h1>
        <p className="mb-8">
          The page you’re looking for doesn’t exist.
        </p>
        <Link href="/">
          <a className="text-blue-600 hover:underline">Go back home</a>
        </Link>
      </body>
    </html>
  );
}
