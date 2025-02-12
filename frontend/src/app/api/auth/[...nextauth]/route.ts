import NextAuth from "next-auth";
import CredentialsProvider from "next-auth/providers/credentials";
import axios from "axios";


// Access the variable
const BACKEND_URL = process.env.HOST_URL;

// ✅ Replace `process.env.NEXT_PUBLIC_BACKEND_URL` with your actual backend URL
//const BACKEND_URL = "http://localhost:8000";  // Change this for production

const handler = NextAuth({
  providers: [
    CredentialsProvider({
      name: "Credentials",
      credentials: {
        email: { label: "Email", type: "text" },
        password: { label: "Password", type: "password" },
      },
      async authorize(credentials) {
        try {
          const res = await axios.post(`${BACKEND_URL}/login`, {
            email: credentials?.email,
            password: credentials?.password,
          });

          if (res.data.access_token) {
            return {
              id: res.data.access_token,
              name: res.data.user.name,  // ✅ Get username
              email: res.data.user.email,
              accessToken: res.data.access_token,
            };
          }
          return null;
        } catch (error) {
          throw new Error("Invalid credentials");
        }
      },
    }),
  ],
  session: { strategy: "jwt" },
  callbacks: {
    async jwt({ token, user }) {
      if (user) {
        token.accessToken = user.accessToken;
        token.name = user.name;  // ✅ Store username
        token.email = user.email;
      }
      return token;
    },
    async session({ session, token }) {
      session.accessToken = token.accessToken;
      session.user = {
        name: token.name,  // ✅ Ensure username is in session
        email: token.email,
      };
      return session;
    },
  },
  secret: "your_secret_key",  // Replace with an actual secret key
});

export { handler as GET, handler as POST };
