import NextAuth from "next-auth";
import CredentialsProvider from "next-auth/providers/credentials";
import axios from "axios";

const BACKEND_URL = process.env.NEXT_PUBLIC_BACKEND_URL || "http://localhost:8000";

const handler = NextAuth({
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
              id: res.data.user.id,  // Ensure ID is correctly stored
              name: res.data.user.name,
              email: res.data.user.email,
              accessToken: res.data.access_token,
            };
          }
          return null;
        } catch (error: any) {
          console.error("Login error:", error.response?.data || error.message);
          throw new Error("Invalid credentials");
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
        token.accessToken = user.accessToken;
        token.name = user.name;
        token.email = user.email;
      }
      return token;
    },
    async session({ session, token }) {
      session.accessToken = token.accessToken;
      session.user = {
        name: token.name,
        email: token.email,
      };
      return session;
    },
  },
  secret: process.env.NEXTAUTH_SECRET, // Secure secret from environment variables
});

export { handler as GET, handler as POST };
