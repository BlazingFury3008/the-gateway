import NextAuth, { NextAuthOptions } from "next-auth";
import CredentialsProvider from "next-auth/providers/credentials";
import GoogleProvider from "next-auth/providers/google";
import DiscordProvider from "next-auth/providers/discord";

const FLASK_API_BASE = process.env.FLASK_API_BASE ?? "http://localhost:5000";

export const authOptions: NextAuthOptions = {
  providers: [
    // --- Email, Password, and Username (for signup) ---
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

          if (!res.ok) {
            console.error(
              `[Flask Auth] ${isSignup ? "Signup" : "Login"} failed:`,
              await res.text()
            );
            return null;
          }

          const user = await res.json();

          // Use only authoritative Flask data
          return {
            id: user.id?.toString() ?? user.email,
            name: user.username ?? user.name ?? user.email,
            email: user.email,
            image: user.image ?? null,
            linked_accounts: user.linked_accounts ?? [],
            accessToken: user.accessToken ?? null,
          };
        } catch (err) {
          console.error("Error connecting to Flask API:", err);
          return null;
        }
      },
    }),

    // --- Google OAuth ---
    GoogleProvider({
      clientId: process.env.GOOGLE_CLIENT_ID ?? "",
      clientSecret: process.env.GOOGLE_CLIENT_SECRET ?? "",
    }),

    // --- Discord OAuth ---
    DiscordProvider({
      clientId: process.env.DISCORD_CLIENT_ID ?? "",
      clientSecret: process.env.DISCORD_CLIENT_SECRET ?? "",
    }),
  ],

  session: { strategy: "jwt" },

  callbacks: {
    // Sync Google/Discord users to Flask and always prefer Flask’s data
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

        if (!res.ok) {
          console.error("Flask sync failed:", await res.text());
          return false;
        }

        const flaskUser = await res.json();

        // Overwrite user data with Flask’s canonical record
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
        console.error("Error syncing Flask user:", err);
        return false;
      }
    },

    async jwt({ token, user }) {
      // Merge user data into token (from Flask’s record)
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
      // Reflect canonical Flask user info in session
      if (token) {
        session.user = {
          ...session.user,
          name: token.name,
          email: token.email,
          image: token.picture,
        };
        (session as any).linked_accounts = token.linked_accounts;
        (session as any).accessToken = token.accessToken;
      }
      return session;
    },
  },

  secret: process.env.NEXTAUTH_SECRET,
  experimental: { enableWebAuthn: true },
};

const handler = NextAuth(authOptions);
export { handler as GET, handler as POST };
