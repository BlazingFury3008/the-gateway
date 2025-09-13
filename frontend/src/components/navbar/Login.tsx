import { useState } from "react";
import { FcGoogle } from "react-icons/fc";
import { FaDiscord, FaEye, FaEyeSlash } from "react-icons/fa";
import { signIn } from "next-auth/react";

export default function Login() {
  const [showPassword, setShowPassword] = useState(false);

  return (
    <div>
      <form className="flex flex-col gap-3">
        <input
          type="text"
          placeholder="Username"
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

        <button
          type="submit"
  
          className="bg-[var(--primary)] hover:bg-[var(--secondary)] rounded !p-2 text-white"
          onClick={() => signIn()}
        >
          Login
        </button>
      </form>

      <div className="my-4 border-t border-[var(--border)]"></div>

      {/* Social logins */}
      <div className="flex flex-col gap-2">
        <button 
        onClick={() => signIn("google")}
        className="flex items-center justify-center gap-2 bg-white hover:bg-gray-100 text-black rounded !p-2 border">
          <FcGoogle size={20} />
          <span>Continue with Google</span>
        </button>

        <button 
                onClick={() => signIn("google")}
className="flex items-center justify-center gap-2 bg-[#5865F2] hover:bg-[#4752C4] text-white rounded !p-2">
          <FaDiscord size={20} />
          <span>Continue with Discord</span>
        </button>
      </div>
    </div>
  );
}
