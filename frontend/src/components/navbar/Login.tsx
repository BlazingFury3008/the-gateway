"use client";

import { useState } from "react";
import { FcGoogle } from "react-icons/fc";
import { FaDiscord, FaEye, FaEyeSlash } from "react-icons/fa";
import { signIn, useSession } from "next-auth/react";

export default function Login() {
  const { update } = useSession(); // get the update() function to refresh session
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [showPassword, setShowPassword] = useState(false);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const handleLogin = async (e: React.FormEvent) => {
    e.preventDefault();
    setLoading(true);
    setError(null);

    try {
      const res = await signIn("credentials", {
        redirect: false,
        email,
        password,
      });

      setLoading(false);

      if (res?.error) {
        setError("Invalid email or password");
      } else if (res?.ok) {
        // Refresh session so Navbar updates without page reload
        await update();
      }
    } catch (err) {
      console.error("Login error:", err);
      setError("Something went wrong. Please try again.");
      setLoading(false);
    }
  };

  const handleSocialLogin = async (provider: "google" | "discord") => {
    try {
      const res = await signIn(provider, { redirect: false });
      if (res?.ok) await update(); // refresh session on success
    } catch (err) {
      console.error(`${provider} login failed:`, err);
      setError("Social login failed. Please try again.");
    }
  };

  return (
    <div className="flex flex-col gap-4">
      <form onSubmit={handleLogin} className="flex flex-col gap-3">
        {/* Email */}
        <input
          type="email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          placeholder="Email"
          required
          className="p-2 rounded bg-[var(--background)] border border-[var(--border)] text-[var(--foreground)] focus:outline-none"
        />

        {/* Password */}
        <div className="relative">
          <input
            type={showPassword ? "text" : "password"}
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            placeholder="Password"
            required
            className="p-2 rounded bg-[var(--background)] border border-[var(--border)] text-[var(--foreground)] focus:outline-none w-full pr-10"
          />
          <button
            type="button"
            onClick={() => setShowPassword(!showPassword)}
            className="absolute right-3 top-1/2 -translate-y-1/2 text-[var(--muted)]"
          >
            {showPassword ? <FaEyeSlash /> : <FaEye />}
          </button>
        </div>

        {error && (
          <p className="text-red-500 text-sm font-medium text-center">{error}</p>
        )}

        <button
          type="submit"
          disabled={loading}
          className="bg-[var(--primary)] hover:bg-[var(--secondary)] rounded p-2 text-white transition disabled:opacity-50"
        >
          {loading ? "Logging in..." : "Login"}
        </button>
      </form>

      <div className="my-4 border-t border-[var(--border)]" />

      {/* Social logins */}
      <div className="flex flex-col gap-2">        <button
          onClick={() => handleSocialLogin("discord")}
          className="flex items-center justify-center gap-2 bg-[#5865F2] hover:bg-[#4752C4] text-white rounded p-2 transition"
        >
          <FaDiscord size={20} />
          <span>Login/Signup with Discord</span>
        </button>
      </div>
    </div>
  );
}
