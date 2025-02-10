import type { Metadata } from "next";
import { Geist, Geist_Mono } from "next/font/google";
import "./globals.css";
import Footer from "@/components/Footer";
import Navbar from "@/components/navbar/navbar";
import SessionProviderWrapper from "@/components/components/SessionProviderWrapper";
import ThemeProvider from "@/components/ThemeProvider";

const geistSans = Geist({
  variable: "--font-geist-sans",
  subsets: ["latin"],
});

const geistMono = Geist_Mono({
  variable: "--font-geist-mono",
  subsets: ["latin"],
});

// ✅ Define metadata in the Server Component
export const metadata: Metadata = {
  title: "The Gateway",
  description: "A platform for creating, managing, and exploring TTRPGs and games.",
  keywords: ["TTRPG", "Game Development", "Character Manager", "Worldbuilding", "Next.js", "React"],
};

export default function RootLayout({
  children,
}: Readonly<{ children: React.ReactNode }>) {
  return (
    <html lang="en">
      <body className={`${geistSans.variable} ${geistMono.variable} antialiased font-[family-name:var(--font-geist-mono)] select-none bg-black`}>
        <SessionProviderWrapper>
          <ThemeProvider>
             <Navbar />
          <div className="">{children}</div>
          <Footer />
          </ThemeProvider>
         
        </SessionProviderWrapper>
      </body>
    </html>
  );
}
