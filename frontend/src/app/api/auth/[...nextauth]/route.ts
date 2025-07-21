import NextAuth, { NextAuthOptions } from "next-auth";
import CredentialsProvider from "next-auth/providers/credentials";
import GoogleProvider from "next-auth/providers/google";
import DiscordProvider from "next-auth/providers/discord";
import axios from "axios";
import { jwtDecode } from "jwt-decode";
import api from "@/other/axios";

const BACKEND_URL = process.env.NEXT_PUBLIC_BACKEND_URL || "http://localhost:8000";

export const authOptions: NextAuthOptions = {
  providers: [
    CredentialsProvider({
      name: "Credentials",
      credentials: {
        email: { label: "Email", type: "text" },
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

          if (res.data?.access_token) {
            const decodedToken = jwtDecode<{ exp: number }>(res.data.access_token);

            return {
              id: res.data.user.uuid || res.data.user.id,
              name: res.data.user.name,
              email: res.data.user.email,
              auth: res.data.user.auth,
              config: res.data.user.config,
              image: res.data.user.image || null,
              accessToken: res.data.access_token,
              expiresAt: decodedToken.exp * 1000,
            };
          }

          return null;
        } catch (error: any) {
          console.error("❌ Login error:", error.response?.data || error.message);
          throw new Error(error.response?.data?.detail || "Invalid credentials");
        }
      },
    }),

    GoogleProvider({
      clientId: process.env.GOOGLE_CLIENT_ID!,
      clientSecret: process.env.GOOGLE_CLIENT_SECRET!,
    }),

    DiscordProvider({
      clientId: process.env.DISCORD_CLIENT_ID!,
      clientSecret: process.env.DISCORD_CLIENT_SECRET!,
    }),
  ],

  session: {
    strategy: "jwt",
  },

  callbacks: {
    async jwt({ token, user, account, profile }) {
      if (account && user) {
        let image = user.image || null;

        if (account.provider === "google" && profile?.picture) {
          image = `${profile.picture}?sz=128`;
        }

        if (account.provider === "discord" && profile?.avatar && profile?.id) {
          const format = profile.avatar.startsWith("a_") ? "gif" : "png";
          image = `https://cdn.discordapp.com/avatars/${profile.id}/${profile.avatar}.${format}?size=512`;
        }

        return {
          ...token,
          id: user.id,
          name: user.name,
          email: user.email,
          image,
          accessToken: account.access_token || user.accessToken,
          expiresAt: user.expiresAt || Date.now() + 60 * 60 * 1000,
          auth: user.auth || "OAuth",
          config: user.config || null,
        };
      }

      return token;
    },

    async session({ session, token }) {
      if (!token?.accessToken || token?.error) {
        return {} as any;
      }

      return {
        ...session,
        user: {
          id: token.id,
          name: token.name,
          email: token.email,
          image: token.image,
          auth: token.auth || "OAuth",
          config: token.config || "DefaultConfig",
        },
        accessToken: token.accessToken,
        expires: new Date(token.expiresAt || Date.now() + 3600000).toISOString(),
      };
    },

    async signIn({account, profile}) {
      if(account?.provider === "google")
      {
        console.log("Google")
        api.post("/google-auth", {
          account:account,
          profile:profile
        })
        
      }
      else if(account?.provider == "discord")
      {
        console.log("Discord")
        api.post("/discord-auth", {
          account:account,
          profile:profile
        })
      }

      return true
    }
  },

  pages: {
    signIn: "/login",
  },

  secret: process.env.NEXTAUTH_SECRET,
  debug: process.env.NODE_ENV === "development",
};

const handler = NextAuth(authOptions);

export { handler as GET, handler as POST };
