import type { Config } from "tailwindcss";

export default {
  content: [
    "./src/pages/**/*.{js,ts,jsx,tsx,mdx}",
    "./src/components/**/*.{js,ts,jsx,tsx,mdx}",
    "./src/app/**/*.{js,ts,jsx,tsx,mdx}",
  ],
  darkMode: "media", // Uses system preference (no class toggling)
  theme: {
    extend: {
      colors: {
        background: {
          DEFAULT: "var(--background)", // Dynamic theme color
        },
        foreground: {
          DEFAULT: "var(--foreground)", // Dynamic theme color
        },
      },
    },
  },
  plugins: [],
} satisfies Config;
