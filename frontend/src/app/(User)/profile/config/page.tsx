"use client";

import { useEffect, useState } from "react";
import {
  user_configuration,
  convertConfigToSaved,
} from "@/data/config";
import { FaCheck, FaTimes, FaEdit, FaSave, FaUndo } from "react-icons/fa";
import { useSession } from "next-auth/react";

export default function ConfigDisplayer() {
  const [editable, setEditable] = useState(false);
  const { data: session, status, update } = useSession();
  const defaultConfig = convertConfigToSaved(user_configuration);
  const [userConfig, setUserConfig] = useState<any>(null);

  // Load user configuration from session
  useEffect(() => {
    if (session?.user?.config) {
      try {
        const parsedConfig = JSON.parse(session.user.config);
        setUserConfig(parsedConfig);
        console.log("🔍 Parsed User Config:", parsedConfig);
      } catch (error) {
        console.error("❌ Failed to parse user config:", error);
        setUserConfig(defaultConfig);
      }
    } else {
      setUserConfig(defaultConfig);
    }
  }, [session]);

  // Toggle boolean option
  function toggleOption(configId: string, option: string) {
    if (!editable) return;

    setUserConfig((prevConfig: any) =>
      prevConfig.map((item: any) =>
        item.id === configId
          ? {
              ...item,
              options: {
                ...item.options,
                [option]: {
                  ...item.options[option],
                  value: !(
                    item.options?.[option]?.value ??
                    defaultConfig[configId]?.[option]?.default
                  ),
                },
              },
            }
          : item
      )
    );
  }

  // Renders each config option
  function renderOption(config: any, option: string) {
    const optionValue =
      userConfig?.find((val: any) => val.id === config.id)?.options?.[option]
        ?.value ?? defaultConfig[config.id]?.[option]?.default;

    return (
      <div
        key={option}
        className={`border flex items-center justify-between px-4 py-3 rounded-lg transition-all duration-200 cursor-pointer border-[var(--color-foreground-soft)] bg-[var(--color-form)] hover:shadow-md ${
          editable ? "hover:bg-[var(--color-background-hover)]" : ""
        }`}
        onClick={() => toggleOption(config.id, option)}
      >
        <h1 className="text-md font-medium">{option}</h1>

        {config.options[option].type === "boolean" && (
          <div>
            {editable ? (
              <input
                type="checkbox"
                name={option}
                id={option}
                readOnly
                checked={optionValue}
                className="w-5 h-5 cursor-pointer"
              />
            ) : optionValue ? (
              <FaCheck size={24} className="text-green-500" />
            ) : (
              <FaTimes size={24} className="text-red-500" />
            )}
          </div>
        )}
      </div>
    );
  }

  return (
    <div className="container mx-auto p-6">
      {/* Header */}
      <div className="flex justify-between items-center mb-4">
        <h1 className="text-4xl font-bold">Configuration</h1>
        {editable ? (
          <div className="space-x-2 flex">
            <button
              onClick={() => {
                setEditable(false);
                console.log("✅ Changes saved!");
              }}
              className="px-4 py-2 bg-green-600 text-white rounded-md shadow-md hover:bg-green-500 flex items-center gap-2"
            >
              <FaSave /> Save
            </button>
            <button
              onClick={() => {
                setEditable(false);
                setUserConfig(JSON.parse(session?.user?.config || "{}"));
                console.log("🔄 Reset to previous configuration.");
              }}
              className="px-4 py-2 bg-gray-600 text-white rounded-md shadow-md hover:bg-gray-500 flex items-center gap-2"
            >
              <FaUndo /> Cancel
            </button>
          </div>
        ) : (
          <button
            onClick={() => setEditable(true)}
            className="px-4 py-2 bg-blue-600 text-white rounded-md shadow-md hover:bg-blue-500 flex items-center gap-2"
          >
            <FaEdit /> Edit
          </button>
        )}
      </div>

      {/* Configuration List */}
      <div className="">
        {user_configuration.map((config) => (
          <div key={config.id} className="mb-6">
            <h1
              className={`text-lg font-bold ${
                config.header_level === "H1" ? "text-2xl" : ""
              }`}
            >
              {config.header}
            </h1>
            <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-4 gap-4 text-sm">
              {Object.keys(config.options).map((option) =>
                renderOption(config, option)
              )}
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}
