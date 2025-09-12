import { useState } from "react";
import { FaEye, FaEyeSlash } from "react-icons/fa";

export default function Signup() {
  const [showPassword, setShowPassword] = useState(false);
  const [showConfirm, setShowConfirm] = useState(false);

  return (
    <div>
      <form className="flex flex-col gap-3">
        <input
          type="text"
          placeholder="Username"
          className="p-2 rounded bg-[var(--background)] border border-[var(--border)] text-[var(--foreground)] focus:outline-none"
        />

        <input
          type="email"
          placeholder="Email"
          className="p-2 rounded bg-[var(--background)] border border-[var(--border)] text-[var(--foreground)] focus:outline-none"
        />

        <div className="relative">
          <input
            type={showPassword ? "text" : "password"}
            placeholder="Password"
            className="p-2 rounded bg-[var(--background)] border border-[var(--border)] text-[var(--foreground)] focus:outline-none w-full pr-10"
          />
          <button
            type="button"
            onClick={() => setShowPassword(!showPassword)}
            className="navbar_hide_pwd absolute right-3 top-1/2 -translate-y-1/2 text-[var(--muted)]"
          >
            {showPassword ? <FaEyeSlash /> : <FaEye />}
          </button>
        </div>

        <div className="relative">
          <input
            type={showConfirm ? "text" : "password"}
            placeholder="Confirm Password"
            className="p-2 rounded bg-[var(--background)] border border-[var(--border)] text-[var(--foreground)] focus:outline-none w-full pr-10"
          />
          <button
            type="button"
            onClick={() => setShowConfirm(!showConfirm)}
            className="navbar_hide_pwd absolute right-3 top-1/2 -translate-y-1/2 text-[var(--muted)]"
          >
            {showConfirm ? <FaEyeSlash /> : <FaEye />}
          </button>
        </div>

        <button
          type="submit"
          className="bg-[var(--primary)] hover:bg-[var(--secondary)] rounded p-2 text-white"
        >
          Sign Up
        </button>
      </form>
    </div>
  );
}
