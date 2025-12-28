/* eslint-disable @typescript-eslint/no-explicit-any */
import NextAuth, { type NextAuthOptions } from "next-auth";
import CredentialsProvider from "next-auth/providers/credentials";
import DiscordProvider from "next-auth/providers/discord";

const FLASK_API_BASE = process.env.FLASK_API_BASE ?? "http://localhost:5000";

/**
 * Helper: parse Flask error payloads safely
 */
async function readError(res: Response) {
  try {
    const ct = res.headers.get("content-type") || "";
    if (ct.includes("application/json")) {
      const data = await res.json();
      return data?.error || JSON.stringify(data);
    }
    const text = await res.text();
    return text || `HTTP ${res.status}`;
  } catch {
    return `HTTP ${res.status}`;
  }
}

export const authOptions: NextAuthOptions = {
  providers: [
    // ----------------------------------------------------
    // EMAIL + PASSWORD (Flask)
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
        const email = credentials?.email?.trim();
        const password = credentials?.password;

        if (!email || !password) return null;

        const isSignup = credentials?.isSignup === "true";
        const endpoint = isSignup
          ? `${FLASK_API_BASE}/auth/signup`
          : `${FLASK_API_BASE}/auth/login`;

        const payload: Record<string, any> = { email, password };
        if (isSignup && credentials?.username) {
          payload.username = credentials.username;
        }

        const res = await fetch(endpoint, {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify(payload),
        });

        if (!res.ok) {
          throw new Error(await readError(res));
        }

        const flaskUser = await res.json();

        // Normalize Flask response → NextAuth "user"
        const id = flaskUser?.id ?? email; // UUID string expected
        const name =
          flaskUser?.name ??
          flaskUser?.username ??
          (email ? email.split("@")[0] : null);

        return {
          id,
          name,
          email,
          image: flaskUser?.image ?? null,
          linked_accounts: flaskUser?.linked_accounts ?? [],
          accessToken: flaskUser?.accessToken ?? null,
        } as any;
      },
    }),

    // ----------------------------------------------------
    // DISCORD (OAuth) → synced into Flask on signIn
    // ----------------------------------------------------
    DiscordProvider({
      clientId: process.env.DISCORD_CLIENT_ID ?? "",
      clientSecret: process.env.DISCORD_CLIENT_SECRET ?? "",
    }),
  ],

  session: {
    strategy: "jwt",
  },

  callbacks: {
    /**
     * OAuth sign-in → sync with Flask
     */
    async signIn({ user, account }) {
      // Credentials provider already returns Flask-shaped user
      if (account?.provider === "credentials") return true;
      if (!account) return false;

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
        // Flask uses 403 for "account conflict"
        throw new Error(await readError(res));
      }

      if (!res.ok) return false;

      const flaskUser = await res.json();

      user.name =
        flaskUser?.name ??
        flaskUser?.username ??
        user.name ??
        flaskUser?.email ??
        user.email ??
        null;

      user.email = flaskUser?.email ?? user.email ?? null;
      user.image = flaskUser?.image ?? user.image ?? null;

      (user as any).linked_accounts = flaskUser?.linked_accounts ?? [];
      (user as any).accessToken = flaskUser?.accessToken ?? null;

      // ✅ Keep UUID string (no toString needed)
      (user as any).id = flaskUser?.id ?? user.email;

      return true;
    },

    /**
     * JWT storage
     * ✅ Store id in token.sub and also token.id for convenience.
     * ✅ session.user.id will come from token.sub.
     */
    async jwt({ token, user, trigger, session }) {
      // Initial login (credentials or oauth after signIn)
      if (user) {
        const uid = (user as any).id ?? user.email ?? token.sub;
        token.sub = uid as string; // canonical id slot
        (token as any).id = uid;

        token.name = user.name;
        token.email = user.email;
        token.picture = (user as any).image ?? token.picture;

        (token as any).linked_accounts = (user as any).linked_accounts ?? [];
        (token as any).accessToken = (user as any).accessToken ?? null;
      }

      // session.update(...)
      if (trigger === "update" && session) {
        const s: any = session;

        if (typeof s.name !== "undefined") token.name = s.name;
        if (typeof s.email !== "undefined") token.email = s.email;

        if (typeof s.image !== "undefined") token.picture = s.image;
        if (typeof s.picture !== "undefined") token.picture = s.picture;

        if (typeof s.linked_accounts !== "undefined") {
          (token as any).linked_accounts = s.linked_accounts;
        }

        if (typeof s.accessToken !== "undefined") {
          (token as any).accessToken = s.accessToken;
        }

        // Allow id updates if ever needed
        if (typeof s.user?.id !== "undefined") {
          token.sub = s.user.id;
          (token as any).id = s.user.id;
        } else if (typeof s.id !== "undefined") {
          token.sub = s.id;
          (token as any).id = s.id;
        }
      }

      return token;
    },

    /**
     * Expose JWT → session
     * ✅ Put id onto session.user.id
     * ✅ Also put id on session.id
     */
    async session({ session, token }) {
      session.user = session.user ?? ({} as any);

      const uid = (token.sub ?? (token as any).id ?? null) as string | null;

      // Attach UUID to user
      (session.user as any).id = uid;

      // Attach UUID to session root as well
      (session as any).id = uid;

      session.user.name = (token.name as string | null) ?? null;
      session.user.email = (token.email as string | null) ?? null;
      session.user.image = (token.picture as string | null) ?? null;

      (session as any).linked_accounts = (token as any).linked_accounts ?? [];
      (session as any).accessToken = (token as any).accessToken ?? null;

      return session;
    },

    /**
     * Disable NextAuth redirect weirdness
     */
    async redirect({ url, baseUrl }) {
      const parsed = new URL(url, baseUrl);
      const error = parsed.searchParams.get("error");

      if (error) {
        return `${baseUrl}?error=${encodeURIComponent(error)}`;
      }

      return url.startsWith(baseUrl) ? url : baseUrl;
    },
  },

  pages: {
    error: "/", // prevent /api/auth/error
  },

  secret: process.env.NEXTAUTH_SECRET,
};

const handler = NextAuth(authOptions);
export { handler as GET, handler as POST };
