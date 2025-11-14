import NextAuth, { NextAuthOptions } from "next-auth";
import CredentialsProvider from "next-auth/providers/credentials";
import GoogleProvider from "next-auth/providers/google";
import DiscordProvider from "next-auth/providers/discord";

const FLASK_API_BASE = process.env.FLASK_API_BASE ?? "http://localhost:5000";

export const authOptions: NextAuthOptions = {
  providers: [
    // ----------------------------------------------------
    // EMAIL + PASSWORD
    // ----------------------------------------------------
    CredentialsProvider({
      name: "Email & Password",
      credentials: {
        email: { label: "Email", type: "email" },
        username: { label: "Username", type: "text" },
        password: { label: "Password", type: "password" },
        isSignup: { label: "Signup", type: "text" },
      },

      async authorize(credentials) {
        if (!credentials?.email || !credentials?.password) return null;

        const isSignup = credentials.isSignup === "true";
        const endpoint = isSignup
          ? `${FLASK_API_BASE}/auth/signup`
          : `${FLASK_API_BASE}/auth/login`;

        try {
          const payload: Record<string, any> = {
            email: credentials.email,
            password: credentials.password,
          };

          if (isSignup && credentials.username) {
            payload.username = credentials.username;
          }

          const res = await fetch(endpoint, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(payload),
          });

          if (res.status === 409) {
            const error = await res.json();
            throw new Error(error.error || "Signup failed");
          }

          if (!res.ok) {
            const text = await res.text();
            throw new Error(text || "Login/Signup failed");
          }

          const user = await res.json();

          return {
            id: user.id?.toString() ?? user.email,
            name: user.username ?? user.name ?? user.email,
            email: user.email,
            image: user.image ?? null,
            linked_accounts: user.linked_accounts ?? [],
            accessToken: user.accessToken ?? null,
          };
        } catch (err: any) {
          console.error("Flask auth failed:", err.message);
          throw new Error(err.message || "Authentication failed");
        }
      },
    }),

    // ----------------------------------------------------
    // GOOGLE
    // ----------------------------------------------------
    GoogleProvider({
      clientId: process.env.GOOGLE_CLIENT_ID ?? "",
      clientSecret: process.env.GOOGLE_CLIENT_SECRET ?? "",
    }),

    // ----------------------------------------------------
    // DISCORD
    // ----------------------------------------------------
    DiscordProvider({
      clientId: process.env.DISCORD_CLIENT_ID ?? "",
      clientSecret: process.env.DISCORD_CLIENT_SECRET ?? "",
    }),
  ],

  session: { strategy: "jwt" },

  // --------------------------------------------------------
  // CALLBACKS
  // --------------------------------------------------------
  callbacks: {
    async signIn({ user, account }) {
      if (account?.provider === "credentials") return true;

      try {
        const res = await fetch(`${FLASK_API_BASE}/auth/sync-user`, {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({
            email: user.email,
            name: user.name,
            provider: account.provider,
            image: user.image,
          }),
        });

        if (res.status === 403) {
          const data = await res.json();
          const msg = encodeURIComponent(data.error || "Account conflict");
          throw new Error(msg);
        }

        if (!res.ok) return false;

        const flaskUser = await res.json();

        user.name =
          flaskUser.username ??
          flaskUser.name ??
          user.name ??
          flaskUser.email;
        user.email = flaskUser.email ?? user.email;
        user.image = flaskUser.image ?? user.image;

        (user as any).linked_accounts = flaskUser.linked_accounts ?? [];
        (user as any).accessToken = flaskUser.accessToken ?? null;

        return true;
      } catch (err) {
        console.error("OAuth sync error:", err);
        throw err;
      }
    },

    async jwt({ token, user }) {
      if (user) {
        token.name = user.name;
        token.email = user.email;
        token.picture = user.image;
        token.linked_accounts = (user as any).linked_accounts ?? [];
        token.accessToken = (user as any).accessToken ?? null;
      }
      return token;
    },

    async session({ session, token }) {
      session.user = {
        ...session.user,
        name: token.name,
        email: token.email,
        image: token.picture,
      };
      (session as any).linked_accounts = token.linked_accounts;
      (session as any).accessToken = token.accessToken;
      return session;
    },

    // --------------------------------------------------------
    // REDIRECT: ALWAYS RETURN TO PRIOR PAGE
    // --------------------------------------------------------
    async redirect({ url, baseUrl }) {
      const parsed = new URL(url, baseUrl);

      const error = parsed.searchParams.get("error");
      let callback = parsed.searchParams.get("callbackUrl");

      // Fallback 1: nextauth referer
      const referer = parsed.searchParams.get("referer");
      if (!callback && referer) callback = referer;

      // Fallback 2: browser referrer
      if (!callback && typeof window !== "undefined" && document.referrer) {
        callback = document.referrer;
      }

      // Final fallback
      if (!callback) callback = baseUrl;

      // Error → go back with ?error=
      if (error) {
        return `${callback}?error=${encodeURIComponent(error)}`;
      }

      return callback;
    },
  },

  // --------------------------------------------------------
  // IMPORTANT: disable default NextAuth error redirect
  // --------------------------------------------------------
  pages: {
    error: "/", // prevents /api/auth/error redirection
  },

  secret: process.env.NEXTAUTH_SECRET,
  experimental: { enableWebAuthn: true },
};

const handler = NextAuth(authOptions);
export { handler as GET, handler as POST };
