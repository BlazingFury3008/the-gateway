"use client";
import GenerateKeyModal from "@/components/admin/api_keys/GenerateKeyModal";
import { useEffect, useState } from "react";

export default function Page() {
  const [apiKeys, setApiKeys] = useState<{ api_key: string; name: string; is_active: boolean }[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const [isModalOpen, setIsModalOpen] = useState(false); // Track modal state

  useEffect(() => {
    async function getApiKeys() {
      try {
        const res = await fetch("/api/get-api-keys");
        if (!res.ok) throw new Error("Failed to fetch API keys");

        const data = await res.json();
        setApiKeys(data);
      } catch (err) {
        console.error("Failed to fetch API keys:", err);
        setError("Error fetching API keys");
      } finally {
        setLoading(false);
      }
    }

    getApiKeys();
  }, []);

  async function GenerateAPIKey(name: string) {
    try {
      const res = await fetch(`/api/generate-api-key`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ name }),
      });

      if (!res.ok) throw new Error("Failed to generate API key");

      const newKey = await res.json();
      setApiKeys((prevKeys) => [...prevKeys, newKey]);
      setIsModalOpen(false); // Close modal after success
    } catch (err) {
      console.error("Error generating API key:", err);
    }
  }

  return (
    <div className="p-4 w-full">
      <h1 className="text-3xl font-bold mb-4 text-center">API Keys</h1>

      {loading ? (
        <p className="text-center">Loading...</p>
      ) : error ? (
        <p className="text-red-500 text-center">{error}</p>
      ) : (
        <div className="overflow-x-auto">
          <table className="border-collapse border border-gray-500 w-5/6 mx-auto text-center">
            <thead>
              <tr className="bg-[var(--color-foreground-soft)] text-[var(--color-background)] font-bold text-lg">
                <th className="border border-gray-500 p-3">Name</th>
                <th className="border border-gray-500 p-3">API Key</th>
                <th className="border border-gray-500 p-3">Active</th>
                <th className="border border-gray-500 p-3">Options</th>
              </tr>
            </thead>
            <tbody>
              {apiKeys.map((key, i) => (
                <tr key={i} className="hover:bg-gray-100">
                  <td className="border border-gray-500 px-3 py-2">{key.name}</td>
                  <td className="border border-gray-500 px-3 py-2">{key.api_key}</td>
                  <td className="border border-gray-500 px-3 py-2">
                    {key.is_active ? "Yes" : "No"}
                  </td>
                  <td className="border border-gray-500 px-3 py-2">
                    <div className="flex justify-center space-x-2">
                      <button className="bg-red-500 text-white px-3 py-1 rounded hover:bg-red-600">Delete</button>
                      <button className="bg-yellow-500 text-white px-3 py-1 rounded hover:bg-yellow-600">Disable</button>
                    </div>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      )}

      {/* Generate Key Button */}
      <div className="flex justify-center mt-6">
        <button className="px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-600" onClick={() => setIsModalOpen(true)}>
          Generate API Key
        </button>
      </div>

      {/* Generate Key Modal */}
      <GenerateKeyModal isOpen={isModalOpen} onClose={() => setIsModalOpen(false)} onSubmit={GenerateAPIKey} />
    </div>
  );
}
