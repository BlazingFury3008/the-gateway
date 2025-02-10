import { Facebook, Twitter, Instagram, Github } from "lucide-react";

export default function Footer() {
  return (
    <footer className="py-8 bg-[var(--color-background)] text-[var(--color-foreground)] border-t border-[var(--color-border)] transition-colors duration-300">
      <div className="container mx-auto px-4">
        <div className="flex flex-col md:flex-row justify-between items-center text-center md:text-left space-y-6 md:space-y-0">
          {/* Brand & Copyright */}
          <div>
            <h2 className="text-xl font-bold">The Gateway</h2>
            <p className="text-sm text-gray-500 dark:text-gray-400">
              &copy; {new Date().getFullYear()} All rights reserved.
            </p>
          </div>

          {/* Navigation Links */}
          <div className="flex space-x-6">
            <a href="/about" className="hover:text-gray-600 dark:hover:text-gray-300 transition">
              About Us
            </a>
            <a href="/contact" className="hover:text-gray-600 dark:hover:text-gray-300 transition">
              Contact
            </a>
            <a href="/privacy" className="hover:text-gray-600 dark:hover:text-gray-300 transition">
              Privacy Policy
            </a>
          </div>

          {/* Social Media Icons */}
          <div className="flex space-x-4">
            <a
              href="https://facebook.com"
              target="_blank"
              rel="noopener noreferrer"
              className="hover:text-gray-600 dark:hover:text-gray-300 transition"
            >
              <Facebook size={20} />
            </a>
            <a
              href="https://twitter.com"
              target="_blank"
              rel="noopener noreferrer"
              className="hover:text-gray-600 dark:hover:text-gray-300 transition"
            >
              <Twitter size={20} />
            </a>
            <a
              href="https://instagram.com"
              target="_blank"
              rel="noopener noreferrer"
              className="hover:text-gray-600 dark:hover:text-gray-300 transition"
            >
              <Instagram size={20} />
            </a>
            <a
              href="https://github.com/BlazingFury3008/the-gateway"
              target="_blank"
              rel="noopener noreferrer"
              className="hover:text-gray-600 dark:hover:text-gray-300 transition"
            >
              <Github size={20} />
            </a>
          </div>
        </div>
      </div>
    </footer>
  );
}
