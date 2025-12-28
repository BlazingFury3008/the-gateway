import NextAuth, { DefaultSession } from "next-auth";

declare module "next-auth" {
  interface Session {
    id?: string | null;
    linked_accounts?: any[]; // or a stricter type if you know the shape
    accessToken?: string | null;
    user: {
      id?: string | null;
    } & DefaultSession["user"];
  }

  interface User {
    id?: string | null;
    linked_accounts?: any[];
    accessToken?: string | null;
  }
}

declare module "next-auth/jwt" {
  interface JWT {
    id?: string | null;
    linked_accounts?: any[];
    accessToken?: string | null;
  }
}
