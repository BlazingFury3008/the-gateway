/* eslint-disable @typescript-eslint/no-explicit-any */
"use client";
import React, { useEffect, useState } from "react";
import { useRouter } from "next/navigation";
import { signIn, useSession } from "next-auth/react";
import { EyeIcon, EyeOffIcon } from "lucide-react";
import api from "@/other/axios";

export default function LoginPage() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [showPassword, setShowPassword] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [loading, setLoading] = useState(false);

  const router = useRouter();
  const { status } = useSession();

  useEffect(() => {
    if (status === "authenticated") {
      router.push("/profile");
    }
  }, [status, router]);

  if (status !== "unauthenticated") {
    return (
      <div className="flex items-center justify-center min-h-screen">
        <div className="animate-spin rounded-full h-16 w-16 border-t-4 border-blue-500"></div>
      </div>
    );
  }

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setError(null);
    setLoading(true);

    try {
      const res = await api.post("/login", { email, password });
      localStorage.setItem("access_token", res.data.access_token);
      console.log(res)

      const loginRes = await signIn("credentials", { email, password, redirect: false });
      console.log(loginRes)

      if (loginRes?.error) {
        setError("Invalid email or password.");
      } else {
        router.push("/"); // Redirect to dashboard
      }
    } catch (error: any) {
      setError("An error occurred.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen flex items-center justify-center bg-[var(--color-background)] text-[var(--color-foreground)] transition-colors duration-300">
      <div className="w-full max-w-md p-8 rounded-2xl shadow-lg border border-[var(--color-border)] transition bg-[var(--color-form)]">
        <h2 className="text-2xl font-semibold text-center mb-6">Login</h2>

        {error && <p className="text-red-500 text-center mb-4">{error}</p>}

        <form onSubmit={handleSubmit} className="space-y-5">
          {/* Email Field */}
          <div>
            <label htmlFor="email" className="block text-sm font-medium text-[var(--color-foreground)]">
              Email
            </label>
            <input
              type="email"
              id="email"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              required
              className="input w-full px-3 py-2 border rounded-lg shadow-sm bg-[var(--color-background)] text-[var(--color-foreground)] border-[var(--color-border)] focus:outline-none focus:ring focus:ring-indigo-300 dark:focus:ring-indigo-500"
            />
          </div>

          {/* Password Field with Show/Hide Toggle */}
          <div className="relative">
            <label htmlFor="password" className="block text-sm font-medium text-[var(--color-foreground)]">
              Password
            </label>
            <input
              type={showPassword ? "text" : "password"}
              id="password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              required
              className="input w-full px-3 py-2 border rounded-lg shadow-sm bg-[var(--color-background)] text-[var(--color-foreground)] border-[var(--color-border)] focus:outline-none focus:ring focus:ring-indigo-300 dark:focus:ring-indigo-500"
            />
            <button
              type="button"
              onClick={() => setShowPassword(!showPassword)}
              className="absolute right-3 top-10 transform -translate-y-1/2 text-gray-500 dark:text-gray-400 hover:text-gray-700 dark:hover:text-gray-300"
            >
              {showPassword ? <EyeOffIcon size={20} /> : <EyeIcon size={20} />}
            </button>
          </div>

          {/* Submit Button */}
          <button
            type="submit"
            className="w-full bg-indigo-600 text-white py-2 rounded-lg hover:bg-indigo-700 dark:hover:bg-indigo-500 transition"
            disabled={loading}
          >
            {loading ? "Logging in..." : "Login"}
          </button>

          {/* Extra Links */}
          <div className="text-center text-sm text-[var(--color-foreground)] mt-3">
            <p>
              <a href="/forgot-password" className="text-indigo-600 dark:text-indigo-400 hover:underline">
                Forgot Password?
              </a>
            </p>
            <p className="mt-2">
              Don&#39;t have an account?{" "}
              <a href="/signup" className="text-indigo-600 dark:text-indigo-400 hover:underline">
                Sign Up
              </a>
            </p>
          </div>
        </form>
      </div>
    </div>
  );
}
