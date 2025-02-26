import { NextResponse } from "next/server";
import api from "@/other/axios";

export async function GET() {
  try {
    const ADMIN_KEY = process.env.NEXT_PUBLIC_ADMIN_SECRET_KEY; // Securely stored in backend
    const API_KEY = process.env.NEXT_PUBLIC_API_KEY

    if (!ADMIN_KEY) {
      return NextResponse.json({ error: "Admin key is missing" }, { status: 500 });
    }

    const res = await api.get("list-api-keys", {
      headers: { "secret-key": ADMIN_KEY },
    });

    return NextResponse.json(res.data.filter((val: { api_key: string | undefined; }) => val.api_key != API_KEY));
  } catch {
    return NextResponse.json({ error: "Failed to fetch API keys" }, { status: 500 });
  }
}
