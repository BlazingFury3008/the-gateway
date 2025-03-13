import { Circle } from "lucide-react";
import React, { useEffect, useState } from "react";
import { defaultAttributes } from "@/data/vtm5_characterCreation";

export default function Attributes({
  attributes,
  setAttributes,
}: {
  attributes: { attribute: string; value: number }[];
  setAttributes: (attrList: { attribute: string; value: number }[]) => void;
}) {
  const [isDarkMode, setIsDarkMode] = useState(false);

  useEffect(() => {
    const checkDarkMode = () => {
      setIsDarkMode(window.matchMedia("(prefers-color-scheme: dark)").matches);
    };

    checkDarkMode();
    window.matchMedia("(prefers-color-scheme: dark)").addEventListener("change", checkDarkMode);

    return () => {
      window.matchMedia("(prefers-color-scheme: dark)").removeEventListener("change", checkDarkMode);
    };
  }, []);

  return (
    <div>
      <div className="text-center mb-4">
        <h2 className="text-lg sm:text-xl font-bold p-0">Attributes</h2>
        <button
          className="text-xs underline text-[var(--color-primary)] hover:text-[var(--color-primary-hover)]"
          onClick={() => setAttributes(defaultAttributes.map(attr => ({ ...attr })))}
        >
          Reset
        </button>
      </div>

      <div className="grid grid-cols-1 sm:grid-cols-3 sm:p-6 w-[90%] mx-auto gap-4">
        {attributes.map((attr, index) => (
          <div key={index} className="flex justify-between items-center">
            <div className="text-black dark:text-white">{attr.attribute}</div>
            <div className="flex space-x-1">
              {[1, 2, 3, 4, 5].map((val) => {
                const isFilled = attr.value >= val;

                return (
                  <Circle
                    key={val}
                    className={`w-5 h-5 cursor-pointer transition-all
                      ${isFilled ? "fill-black dark:fill-white" : "fill-white dark:fill-black"}
                      stroke-black dark:stroke-white`}
                    onClick={() => {
                      const updatedAttributes = attributes.map(a =>
                        a.attribute === attr.attribute ? { ...a, value: val } : a
                      );
                      setAttributes(updatedAttributes);
                    }}
                  />
                );
              })}
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}
