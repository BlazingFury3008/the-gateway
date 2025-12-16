"use client";

import React, { useEffect, useRef, useState } from "react";
import NavProfile from "./NavProfile";
import { FaMoon, FaSun, FaBars, FaTimes } from "react-icons/fa";
import Login from "./Login";
import { useSession } from "next-auth/react";
import { useRouter, usePathname } from "next/navigation";
import { useTheme } from "@/app/theme-provider";

/* =========================
   NAV CONFIG
========================= */
type NavItem = {
  Label: string;
  link: string;
};

const NAV_ITEMS: NavItem[] = [
  { Label: "Forums", link: "/forums" },
  { Label: "Characters", link: "/characters" },
  { Label: "News", link: "/news" },
  { Label: "Events", link: "/events" },
  { Label: "Contact", link: "/contact" },
  { Label: "Wikis", link: "/wiki" },
];

/* =========================
   PROFILE SEARCH
========================= */
const SEARCH_ENDPOINT = "/data/profiles/search"; // example: GET ?q=...
const PROFILE_ROUTE = (r: ProfileResult) => `/profile/${r.id ?? r.username}`; // change if needed

type ProfileResult = {
  id?: string | number;
  username: string;
  displayName?: string;
  avatarUrl?: string;
};

function ProfileSearch({
  variant = "desktop",
  onNavigate,
}: {
  variant?: "desktop" | "mobile";
  onNavigate: (href: string) => void;
}) {
  const [q, setQ] = useState("");
  const [open, setOpen] = useState(false);
  const [loading, setLoading] = useState(false);
  const [err, setErr] = useState<string | null>(null);
  const [results, setResults] = useState<ProfileResult[]>([]);
  const wrapperRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    function onDown(e: MouseEvent) {
      if (
        wrapperRef.current &&
        !wrapperRef.current.contains(e.target as Node)
      ) {
        setOpen(false);
      }
    }
    document.addEventListener("mousedown", onDown);
    return () => document.removeEventListener("mousedown", onDown);
  }, []);

  useEffect(() => {
    const trimmed = q.trim();
    if (trimmed.length < 2) {
      setResults([]);
      setErr(null);
      setLoading(false);
      return;
    }

    const controller = new AbortController();
    const t = setTimeout(async () => {
      try {
        setLoading(true);
        setErr(null);

        const base = process.env.NEXT_PUBLIC_FLASK_API_BASE;
        if (!base) throw new Error("Missing NEXT_PUBLIC_FLASK_API_BASE");

        const res = await fetch(
          `${base}${SEARCH_ENDPOINT}?q=${encodeURIComponent(trimmed)}`,
          {
            method: "GET",
            headers: {
              "Content-Type": "application/json",
              "X-API-Key": process.env.NEXT_PUBLIC_DATA_API_KEY ?? "",
            },
            cache: "no-store",
            signal: controller.signal,
          }
        );

        const data = await res.json().catch(() => null);

        if (!res.ok) {
          throw new Error(data?.error || "Failed to search profiles");
        }

        setResults(Array.isArray(data) ? data : []);
      } catch (e: any) {
        if (e?.name === "AbortError") return;
        setErr(e?.message || "Failed to search profiles");
        setResults([]);
      } finally {
        setLoading(false);
      }
    }, 250);

    return () => {
      clearTimeout(t);
      controller.abort();
    };
  }, [q]);

  const inputClasses =
    variant === "mobile"
      ? "w-full px-4 py-3 rounded-md border border-[var(--border)] bg-[var(--background)] text-[var(--foreground)]"
      : "w-72 md:w-80 px-3 py-2 rounded-md border border-[var(--border)] bg-[var(--background)] text-[var(--foreground)] text-sm";

  return (
    <div className="relative" ref={wrapperRef}>
      <div className="relative">
        <input
          value={q}
          onChange={(e) => {
            setQ(e.target.value);
            setOpen(true);
          }}
          onFocus={() => setOpen(true)}
          placeholder="Search profiles…"
          className={`${inputClasses} pl-4`}
          aria-label="Search profiles"
        />
      </div>

      <div
        className={`absolute left-0 right-0 mt-2 rounded-2xl border border-[var(--border)] bg-[var(--navbar)] shadow-xl overflow-hidden transition ${
          open ? "opacity-100" : "opacity-0 pointer-events-none"
        }`}
      >
        <div className="p-2">
          {q.trim().length < 2 && (
            <div className="px-3 py-2 text-sm text-[var(--muted)]">
              Type at least 2 characters.
            </div>
          )}

          {q.trim().length >= 2 && loading && (
            <div className="px-3 py-2 text-sm text-[var(--muted)]">
              Searching…
            </div>
          )}

          {q.trim().length >= 2 && !loading && err && (
            <div className="px-3 py-2 text-sm text-red-500">{err}</div>
          )}

          {q.trim().length >= 2 && !loading && !err && results.length === 0 && (
            <div className="px-3 py-2 text-sm text-[var(--muted)]">
              No profiles found.
            </div>
          )}

          {!loading && !err && results.length > 0 && (
            <div className="flex flex-col">
              {results.slice(0, 8).map((r) => (
                <button
                  key={`${r.id ?? r.username}`}
                  onClick={() => {
                    setOpen(false);
                    setQ("");
                    onNavigate(PROFILE_ROUTE(r));
                  }}
                  className="w-full text-left px-3 py-2 rounded-xl hover:bg-[var(--background)] transition flex items-center gap-3"
                >
                  <div className="w-8 h-8 rounded-full bg-[var(--border)] overflow-hidden flex items-center justify-center text-xs text-[var(--muted)]">
                    {r.avatarUrl ? (
                      // eslint-disable-next-line @next/next/no-img-element
                      <img
                        src={r.avatarUrl}
                        alt=""
                        className="w-full h-full object-cover"
                      />
                    ) : (
                      (r.displayName ?? r.username).slice(0, 2).toUpperCase()
                    )}
                  </div>

                  <div className="min-w-0">
                    <div className="text-sm font-semibold truncate">
                      {r.displayName ?? r.username}
                    </div>
                    <div className="text-xs text-[var(--muted)] truncate">
                      @{r.username}
                    </div>
                  </div>
                </button>
              ))}
            </div>
          )}
        </div>
      </div>
    </div>
  );
}

/* =========================
   NAVBAR
========================= */
export default function Navbar() {
  const { status, update } = useSession();
  const { theme, toggleTheme } = useTheme();
  const [drawerOpen, setDrawerOpen] = useState(false);
  const router = useRouter();
  const pathname = usePathname();

  useEffect(() => {
    if (status === "loading") update();
  }, [status, update]);

  // Disable background scroll when drawer is open (mobile)
  useEffect(() => {
    if (!drawerOpen) return;

    const body = document.body;
    const prevOverflow = body.style.overflow;
    const prevPaddingRight = body.style.paddingRight;

    const scrollbarWidth =
      window.innerWidth - document.documentElement.clientWidth;

    body.style.overflow = "hidden";
    if (scrollbarWidth > 0) body.style.paddingRight = `${scrollbarWidth}px`;

    return () => {
      body.style.overflow = prevOverflow;
      body.style.paddingRight = prevPaddingRight;
    };
  }, [drawerOpen]);

  const isLoading = status === "loading";
  const isAuthenticated = status === "authenticated";

  function navigate(href: string) {
    setDrawerOpen(false);

    const [path, hash] = href.split("#");
    if (hash && (path === "" || path === pathname)) {
      const el = document.getElementById(hash);
      if (el) {
        el.scrollIntoView({ behavior: "smooth", block: "start" });
        return;
      }
    }

    router.push(href);
  }

  return (
    <header className="sticky top-0 z-50">
      <nav className="navbar h-16 flex items-center justify-between px-4 sm:px-6 border-b border-[var(--border)] bg-[var(--navbar)]">
        <h1
          className="font-bold text-lg sm:text-xl cursor-pointer text-[var(--foreground)]"
          onClick={() => navigate("/")}
        >
          The Gateway
        </h1>

        <div className="flex items-center gap-3">
          <button
            onClick={toggleTheme}
            className="!p-3 !rounded-full bg-[var(--background)] text-[var(--foreground)] border border-[var(--border)] hover:bg-[var(--primary)] hover:text-white transition"
            aria-label="Toggle Theme"
          >
            {theme === "light" ? <FaMoon /> : <FaSun />}
          </button>

          <div className="hidden sm:block">
            {isLoading ? (
              <div className="animate-pulse w-9 h-9 rounded-full bg-[var(--border)]" />
            ) : isAuthenticated ? (
              <NavProfile onNavigate={navigate}/>
            ) : (
              <LoginComponent />
            )}
          </div>

          <button
            className="sm:hidden p-2 rounded-md text-[var(--foreground)] border border-[var(--border)]"
            onClick={() => setDrawerOpen(true)}
            aria-label="Open menu"
          >
            <FaBars />
          </button>
        </div>

        <>
          <div
            className={`fixed inset-0 bg-black/50 z-40 transition-opacity duration-300 ${
              drawerOpen ? "opacity-100" : "opacity-0 pointer-events-none"
            }`}
            onClick={() => setDrawerOpen(false)}
          />

          <div
            className={`fixed top-0 right-0 h-full w-full max-w-sm bg-[var(--navbar)] border-l border-[var(--border)] z-50 p-6 flex flex-col gap-6 transform transition-transform duration-300 ${
              drawerOpen ? "translate-x-0" : "translate-x-full"
            }`}
          >
            <button
              className="self-end p-2 text-[var(--foreground)]"
              onClick={() => setDrawerOpen(false)}
              aria-label="Close menu"
            >
              <FaTimes size={20} />
            </button>

            <ProfileSearch variant="mobile" onNavigate={navigate} />

            <div className="flex flex-col gap-2">
              {NAV_ITEMS.map((item) => (
                <button
                  key={item.link}
                  onClick={() => navigate(item.link)}
                  className="text-left w-full px-4 py-3 rounded-md border border-[var(--border)] bg-[var(--background)] text-[var(--foreground)]
                             hover:bg-[var(--primary)] hover:text-white transition"
                >
                  {item.Label}
                </button>
              ))}
            </div>

            <div className="mt-auto">
              {isLoading ? (
                <div className="animate-pulse w-9 h-9 rounded-full bg-[var(--border)]" />
              ) : isAuthenticated ? (
                <NavProfile onNavigate={navigate}/>
              ) : (
                <LoginComponent mobile />
              )}
            </div>
          </div>
        </>
      </nav>

      <div className="hidden sm:block border-b border-[var(--border)] bg-[var(--navbar)]">
        <div className="px-4 sm:px-6 h-12 flex items-center justify-between gap-4">
          <div className="flex items-center gap-2">
            {NAV_ITEMS.map((item) => (
              <button
                key={item.link}
                onClick={() => navigate(item.link)}
                className="px-3 py-2 rounded-md text-sm text-[var(--foreground)]
                           hover:bg-[var(--background)] border border-transparent hover:border-[var(--border)] transition"
              >
                {item.Label}
              </button>
            ))}
          </div>

          <ProfileSearch variant="desktop" onNavigate={navigate} />
        </div>
      </div>
    </header>
  );
}

/* =========================
   LOGIN COMPONENT
========================= */
function LoginComponent({ mobile = false }: { mobile?: boolean }) {
  const [isOpen, setIsOpen] = useState(false);
  const wrapperRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    function handleClickOutside(event: MouseEvent) {
      if (
        wrapperRef.current &&
        !wrapperRef.current.contains(event.target as Node)
      ) {
        setIsOpen(false);
      }
    }
    document.addEventListener("mousedown", handleClickOutside);
    return () => document.removeEventListener("mousedown", handleClickOutside);
  }, []);

  if (mobile) {
    return (
      <>
        <button
          onClick={() => setIsOpen(true)}
          className="w-full px-4 py-2 rounded-md border border-[var(--border)] bg-[var(--background)] text-[var(--foreground)]
                     hover:bg-[var(--primary)] hover:text-white transition"
        >
          Login / Signup
        </button>

        <div
          className={`fixed inset-0 bg-black/50 z-40 transition-opacity duration-300 ${
            isOpen ? "opacity-100" : "opacity-0 pointer-events-none"
          }`}
          onClick={() => setIsOpen(false)}
        />

        <div
          className={`fixed top-0 left-0 w-full max-h-[90%] bg-[var(--navbar)] border-b border-[var(--border)] shadow-xl z-50 transform transition-transform duration-300 ${
            isOpen ? "translate-y-0" : "-translate-y-full"
          }`}
        >
          <div className="p-4">
            <Login />
          </div>
        </div>
      </>
    );
  }

  return (
    <div className="relative" ref={wrapperRef}>
      <button
        onClick={() => setIsOpen(!isOpen)}
        className="navbar_login bg-[var(--navbar)] text-[var(--foreground)]"
      >
        Login / Signup
      </button>

      <div
        className={`absolute right-0 border border-[var(--border)] w-80 sm:w-96 rounded-2xl p-5 bg-[var(--navbar)] mt-2 shadow-xl text-[var(--foreground)]
                    transform transition-all duration-300 origin-top z-50 ${
                      isOpen
                        ? "opacity-100 scale-100 translate-y-0"
                        : "opacity-0 scale-95 -translate-y-2 pointer-events-none"
                    }`}
      >
        <Login />
      </div>
    </div>
  );
}
