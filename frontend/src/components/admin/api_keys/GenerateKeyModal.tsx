"use client";
import { useState } from "react";

export default function GenerateKeyModal({ isOpen, onClose, onSubmit } : {isOpen: boolean, onClose: () => void, onSubmit: (val: string) => void}) {
  const [keyName, setKeyName] = useState("");

  if (!isOpen) return null;

  return (
    <div className="fixed inset-0 flex items-center justify-center z-50">
      {/* Background Blur */}
      <div className="absolute inset-0 bg-black bg-opacity-50 backdrop-blur-lg" onClick={onClose}></div>

      {/* Modal Content */}
      <div className="bg-[var(--color-background)] text-[var(--color-foreground)] p-6 rounded-lg shadow-lg w-96 z-50 modal-enter">
        <h2 className="text-xl font-bold mb-4">Generate API Key</h2>
        
        <label className="block text-sm font-medium mb-2">Key Name</label>
        <input
          type="text"
          className="input"
          placeholder="Enter key name..."
          value={keyName}
          onChange={(e) => setKeyName(e.target.value)}
        />

        {/* Buttons */}
        <div className="flex justify-end space-x-3 mt-4">
          <button className="btn btn-danger" onClick={onClose}>Cancel</button>
          <button className={`btn ${keyName == "" ? "bg-gray-700" : "btn-primary"}`} disabled={keyName==""} onClick={() => onSubmit(keyName)}>Generate</button>
        </div>
      </div>
    </div>
  );
}
