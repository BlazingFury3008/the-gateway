import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  reactStrictMode: true,
  images: {
    remotePatterns: [
      {
        protocol: "https",
        hostname: "cdn-icons-png.flaticon.com",
        pathname: "/**",
      },
    ],
  },
};

module.exports = {
  images: {
    domains: ["cdn-icons-png.flaticon.com"],
  },
};



export default nextConfig;
