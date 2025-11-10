import NextAuth, { NextAuthOptions } from "next-auth";
import CredentialsProvider from "next-auth/providers/credentials";
import GoogleProvider from "next-auth/providers/google";
import DiscordProvider from "next-auth/providers/discord";

const FLASK_API_BASE = process.env.FLASK_API_BASE || "http://localhost:5000";

export const authOptions: NextAuthOptions = {
  providers: [
    // --- Email + Password ---
    CredentialsProvider({
      name: "Email & Password",
      credentials: {
        email: { label: "Email", type: "email" },
        password: { label: "Password", type: "password" },
        isSignup: { label: "Signup", type: "boolean" },
      },
      async authorize(credentials) {
        if (!credentials?.email || !credentials?.password) return null;

        const endpoint = credentials.isSignup === "true"
          ? `${FLASK_API_BASE}/auth/signup`
          : `${FLASK_API_BASE}/auth/login`;

        const res = await fetch(endpoint, {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({
            email: credentials.email,
            password: credentials.password,
          }),
        });

        if (!res.ok) {
          console.error("Flask auth failed:", await res.text());
          return null;
        }

        const user = await res.json(); // Flask should return { id, name, email, ... }
        return user;
      },
    }),

    // --- Google OAuth ---
    GoogleProvider({
      clientId: process.env.GOOGLE_CLIENT_ID || "",
      clientSecret: process.env.GOOGLE_CLIENT_SECRET || "",
    }),

    // --- Discord OAuth ---
    DiscordProvider({
      clientId: process.env.DISCORD_CLIENT_ID || "",
      clientSecret: process.env.DISCORD_CLIENT_SECRET || "",
    }),
  ],

  session: { strategy: "jwt" },

  callbacks: {
    // Called on OAuth login (Google/Discord)
    async signIn({ user, account }) {
      // Skip for Credentials provider — Flask already handled signup/login
      if (account?.provider === "credentials") return true;

      try {
        const res = await fetch(`${FLASK_API_BASE}/auth/sync-user`, {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({
            email: user.email,
            name: user.name,
            provider: account?.provider,
            image: user.image,
          }),
        });

        if (!res.ok) {
          console.error("Flask sync failed:", await res.text());
          return false;
        }

        const flaskData = await res.json();
        (user as any).flaskData = flaskData;
        return true;
      } catch (err) {
        console.error("Error syncing Flask user:", err);
        return false;
      }
    },

    async jwt({ token, user }) {
      if (user?.flaskData) token.flaskData = user.flaskData;
      if (user?.accessToken) token.accessToken = user.accessToken;
      return token;
    },

    async session({ session, token }) {
      if (token?.flaskData) session.flaskData = token.flaskData;
      if (token?.accessToken) session.accessToken = token.accessToken;
      return session;
    },
  },

  pages: {
    signIn: "/login", // optional custom login page
  },

  experimental: { enableWebAuthn: true },
};

const handler = NextAuth(authOptions);
export { handler as GET, handler as POST };
