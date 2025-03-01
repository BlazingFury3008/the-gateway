import NextAuth, { NextAuthOptions } from "next-auth";
import CredentialsProvider from "next-auth/providers/credentials";
import axios from "axios";
import { jwtDecode } from "jwt-decode";

const BACKEND_URL = process.env.NEXT_PUBLIC_BACKEND_URL || "http://localhost:8000";

async function refreshAccessToken(token: any) {
  try {
    console.log("🔄 Refreshing access token...");

    const res = await axios.post(`${BACKEND_URL}/refresh-token`, {
      accessToken: token.accessToken,
    });

    if (!res.data.access_token) {
      throw new Error("No new access token returned.");
    }

    const decodedToken = jwtDecode<{ exp: number }>(res.data.access_token);

    console.log("✅ New access token received.");

    return {
      ...token,
      accessToken: res.data.access_token,
      expiresAt: decodedToken.exp * 1000, // Convert expiration to milliseconds
    };
  } catch (error) {
    console.error("❌ Token refresh failed:", error);

    return {
      ...token,
      error: "RefreshTokenError", // Flag that refresh failed
    };
  }
}

export const authOptions: NextAuthOptions = {
  providers: [
    CredentialsProvider({
      name: "Credentials",
      credentials: {
        email: { label: "Email", type: "text", placeholder: "example@email.com" },
        password: { label: "Password", type: "password" },
      },
      async authorize(credentials) {
        if (!credentials?.email || !credentials?.password) {
          throw new Error("Email and password are required.");
        }

        try {
          const res = await axios.post(`${BACKEND_URL}/login`, {
            email: credentials.email,
            password: credentials.password,
          });

          if (res.data.access_token) {
            const decodedToken = jwtDecode<{ exp: number }>(res.data.access_token);

            return {
              id: res.data.user.uuid || res.data.user.id,
              name: res.data.user.name,
              email: res.data.user.email,
              auth: res.data.user.auth,
              accessToken: res.data.access_token,
              expiresAt: decodedToken.exp * 1000, // Convert to milliseconds
            };
          }
          return null;
        } catch (error: any) {
          console.error("❌ Login error:", error.response?.data || error.message);
          throw new Error(error.response?.data?.detail || "Invalid credentials");
        }
      },
    }),
  ],
  session: {
    strategy: "jwt",
  },
  callbacks: {
    async jwt({ token, user }) {
      if (user) {
        return {
          id: user.id,
          name: user.name,
          email: user.email,
          auth: user.auth,
          accessToken: user.accessToken,
          expiresAt: user.expiresAt,
        };
      }

      // Ensure expiresAt is always defined
      if (!token.expiresAt) {
        console.warn("⚠️ Token missing expiration, logging out...");
        return {} as any;
      }

      // Refresh token if it's close to expiring (5 minutes threshold)
      const shouldRefresh = Date.now() > token.expiresAt - 5 * 60 * 1000;

      if (shouldRefresh) {
        return await refreshAccessToken(token);
      }

      // If token is expired, clear session
      if (Date.now() > token.expiresAt) {
        console.warn("⏳ JWT expired, logging out...");
        return {} as any;
      }

      return token;
    },
    async session({ session, token }) {
      if (!token.accessToken || token.error === "RefreshTokenError") {
        console.warn("❌ Session expired or refresh failed.");
        return null;
      }

      session.user = {
        id: token.id,
        name: token.name,
        email: token.email,
        auth: token.auth,
      };
      session.accessToken = token.accessToken;
      session.expires = new Date(token.expiresAt).toISOString(); // Convert to ISO string

      return session;
    },
  },
  secret: process.env.NEXTAUTH_SECRET,
  debug: true,
};

const handler = NextAuth(authOptions);

export { handler as GET, handler as POST };
