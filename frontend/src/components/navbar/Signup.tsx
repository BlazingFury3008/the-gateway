"use client";

import { useState } from "react";
import { FaEye, FaEyeSlash } from "react-icons/fa";
import { signIn } from "next-auth/react";

export default function Signup() {
  const [email, setEmail] = useState("");
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [confirmPassword, setConfirmPassword] = useState("");
  const [showPassword, setShowPassword] = useState(false);
  const [showConfirm, setShowConfirm] = useState(false);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [success, setSuccess] = useState<string | null>(null);

  const handleSignup = async (e: React.FormEvent) => {
    e.preventDefault();
    setError(null);
    setSuccess(null);

    if (!email || !username || !password || !confirmPassword) {
      setError("All fields are required");
      return;
    }

    if (password !== confirmPassword) {
      setError("Passwords do not match");
      return;
    }

    setLoading(true);

    // Send signup request via NextAuth credentials provider
    const res = await signIn("credentials", {
      email,
      password,
      isSignup: "true", // signals Flask to use /auth/signup
      redirect: false,
    });

    setLoading(false);

    if (res?.error) {
      setError("Signup failed. Please try again.");
    } else if (res?.ok) {
      setSuccess("Account created successfully!");
      // Optional: refresh or close modal
      window.location.reload();
    }
  };

  return (
    <div>
      <form onSubmit={handleSignup} className="flex flex-col gap-3">
        {/* Username */}
        <input
          type="text"
          value={username}
          onChange={(e) => setUsername(e.target.value)}
          placeholder="Username"
          required
          className="p-2 rounded bg-[var(--background)] border border-[var(--border)] text-[var(--foreground)] focus:outline-none"
        />

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

        {/* Confirm Password */}
        <div className="relative">
          <input
            type={showConfirm ? "text" : "password"}
            value={confirmPassword}
            onChange={(e) => setConfirmPassword(e.target.value)}
            placeholder="Confirm Password"
            required
            className="p-2 rounded bg-[var(--background)] border border-[var(--border)] text-[var(--foreground)] focus:outline-none w-full pr-10"
          />
          <button
            type="button"
            onClick={() => setShowConfirm(!showConfirm)}
            className="absolute right-3 top-1/2 -translate-y-1/2 text-[var(--muted)]"
          >
            {showConfirm ? <FaEyeSlash /> : <FaEye />}
          </button>
        </div>

        {error && (
          <p className="text-red-500 text-sm font-medium text-center">{error}</p>
        )}
        {success && (
          <p className="text-green-500 text-sm font-medium text-center">
            {success}
          </p>
        )}

        <button
          type="submit"
          disabled={loading}
          className="bg-[var(--primary)] hover:bg-[var(--secondary)] rounded p-2 text-white transition disabled:opacity-50"
        >
          {loading ? "Signing up..." : "Sign Up"}
        </button>
      </form>
    </div>
  );
}
