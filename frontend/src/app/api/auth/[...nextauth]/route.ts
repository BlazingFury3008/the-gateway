import NextAuth, { NextAuthOptions } from "next-auth";
import CredentialsProvider from "next-auth/providers/credentials";
import axios from "axios";

const BACKEND_URL = process.env.NEXT_PUBLIC_BACKEND_URL || "http://localhost:8000";

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
            return {
              id: res.data.user.uuid || res.data.user.id, // Ensure correct ID is stored
              name: res.data.user.name,
              email: res.data.user.email,
              auth: res.data.user.auth,
              accessToken: res.data.access_token,
            };
          }
          return null;
        } catch (error: any) {
          console.error("Login error:", error.response?.data || error.message);
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
        token.id = user.id;
        token.name = user.name;
        token.email = user.email;
        token.auth = user.auth; // Default auth if undefined
        token.accessToken = user.accessToken;
      }
      return token;
    },
    async session({ session, token }) {
      session.user = {
        id: token.id,
        name: token.name,
        email: token.email,
        auth: token.auth, // Ensure auth is included
      };
      session.accessToken = token.accessToken;
      return session;
    },
  },
  secret: process.env.NEXTAUTH_SECRET, // Secure secret from environment variables
  debug: true, // Enables debugging in logs
};

const handler = NextAuth(authOptions);

export { handler as GET, handler as POST };
