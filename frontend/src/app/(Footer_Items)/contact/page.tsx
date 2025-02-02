"use client";
import React, { useState } from "react";

export default function EmailForm() {
  const [email, setEmail] = useState("");
  const [name, setName] = useState("");
  const [subject, setSubject] = useState("");
  const [content, setContent] = useState("");
  const [submitted, setSubmitted] = useState(false);

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    console.log("Email:", email);
    console.log("Name:", name);
    console.log("Subject:", subject);
    console.log("Content:", content);
    setSubmitted(true);
  };

  return (
    <div className="min-h-screen flex items-center justify-center bg-gray-100">
      <div className="max-w-lg w-full bg-white p-8 rounded-2xl shadow-lg">
        <h2 className="text-2xl font-semibold mb-6 text-center">Contact Us</h2>

        {submitted ? (
          <p className="text-green-600 text-center">Thank you for your message!</p>
        ) : (
          <form onSubmit={handleSubmit} className="space-y-5">
            {/* Name Field */}
            <div>
              <label htmlFor="name" className="block text-sm font-medium text-gray-700">
                Name
              </label>
              <input
                type="text"
                id="name"
                value={name}
                onChange={(e) => setName(e.target.value)}
                required
                className="w-full px-3 py-2 border rounded-lg shadow-sm focus:outline-none focus:ring focus:ring-indigo-300"
              />
            </div>

            {/* Email Field */}
            <div>
              <label htmlFor="email" className="block text-sm font-medium text-gray-700">
                Email
              </label>
              <input
                type="email"
                id="email"
                value={email}
                onChange={(e) => setEmail(e.target.value)}
                required
                className="w-full px-3 py-2 border rounded-lg shadow-sm focus:outline-none focus:ring focus:ring-indigo-300"
              />
            </div>

            {/* Subject Field */}
            <div>
              <label htmlFor="subject" className="block text-sm font-medium text-gray-700">
                Subject
              </label>
              <input
                type="text"
                id="subject"
                value={subject}
                onChange={(e) => setSubject(e.target.value)}
                required
                className="w-full px-3 py-2 border rounded-lg shadow-sm focus:outline-none focus:ring focus:ring-indigo-300"
              />
            </div>

            {/* Content Field */}
            <div>
              <label htmlFor="content" className="block text-sm font-medium text-gray-700">
                Content
              </label>
              <textarea
                id="content"
                value={content}
                onChange={(e) => setContent(e.target.value)}
                required
                rows={5}
                className="w-full px-3 py-2 border rounded-lg shadow-sm focus:outline-none focus:ring focus:ring-indigo-300"
              />
            </div>

            {/* Submit Button */}
            <button
              type="submit"
              className="w-full bg-indigo-600 text-white py-2 rounded-lg hover:bg-indigo-700 transition"
            >
              Send
            </button>
          </form>
        )}
      </div>
    </div>
  );
}
