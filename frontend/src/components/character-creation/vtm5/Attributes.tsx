/* eslint-disable react-hooks/rules-of-hooks */
import { Circle } from "lucide-react";
import React, { useEffect, useState } from "react";
import { defaultAttributes } from "@/data/vtm5_characterCreation";

export default function Attributes({
  attributes,
  setAttributes,
  attributeLayout,
}: {
  attributes: { attribute: string; value: number }[];
  setAttributes: (attrList: { attribute: string; value: number }[]) => void;
  attributeLayout: number[];
}) {
  const [allowed, setAllowed] = useState<number[]>([]);

  useEffect(() => {
    const tmp = [...attributeLayout];

    attributes.forEach((val) => {
      const indexToRemove = tmp.indexOf(val.value);
      if (indexToRemove !== -1) {
        tmp.splice(indexToRemove, 1); // Remove one occurrence
      }
    });

    setAllowed(tmp);
  }, [attributes, attributeLayout]);

  // Organizing attributes in a column-major order
  const numColumns = 3;
  const numRows = Math.ceil(attributes.length / numColumns);

  const columnMajorAttributes: { attribute: string; value: number }[][] = [];
  for (let col = 0; col < numColumns; col++) {
    columnMajorAttributes.push([]);
    for (let row = 0; row < numRows; row++) {
      const index = row * numColumns + col;
      if (index < attributes.length) {
        columnMajorAttributes[col].push(attributes[index]);
      }
    }
  }

  return (
    <div>
      <div className="text-center mb-4">
        <h2 className="text-lg sm:text-xl font-bold p-0">Attributes</h2>
        <button
          className="text-xs underline text-[var(--color-primary)] hover:text-[var(--color-primary-hover)]"
          onClick={() =>
            setAttributes(defaultAttributes.map((attr) => ({ ...attr })))
          }
        >
          Reset
        </button>
        <div className="text-xs w-[50%] text-center mx-auto">
          Press the attribute name to set the attribute to 0
        </div>
      </div>

      {/* Grid layout for column-major order */}
      <div className="grid sm:grid-cols-3 grid-rows-3 gap-4 sm:gap-2 w-full lg:px-5 lg:w-[70%] md:w-[85%] sm:w-[90%] mx-auto">
        {Array.from({ length: numRows }).map((_, rowIndex) => (
          <div key={rowIndex} className="grid grid-rows-3 gap-4">
            {columnMajorAttributes.map((column, colIndex) => {
              const attr = column[rowIndex];
              return attr ? (
                <div
                  key={colIndex}
                  className="flex justify items-center sm:w-[70%]"
                >
                  <div
                    className="text-[var(--color-foreground)] text-ellipsis sm:w-[40%] w-[50%] overflow-hidden cursor-pointer"
                    onClick={() => {
                      setAttributes(
                        attributes.map((a) =>
                          a.attribute === attr.attribute ? { ...a, value: 1 } : a
                        )
                      );
                    }}
                  >
                    {attr.attribute}
                  </div>
                  <div className="flex space-x-1 sm:w-[60%] w-[50%] justify-end">
                    {[1, 2, 3, 4, 5].map((val) => {
                      const isFilled = attr.value >= val;
                      return (
                        <Circle
                          key={val}
                          className={`${
                            !allowed.includes(val) && attr.value < val
                              ? "text-[var(--color-danger)]"
                              : "text-[var(--color-foreground)] cursor-pointer"
                          } ${isFilled && "fill-[var(--color-foreground)]"}`}
                          onClick={() => {
                            if (!allowed.includes(val)) {
                              return;
                            }
                            const updatedAttributes = attributes.map((a) =>
                              a.attribute === attr.attribute
                                ? { ...a, value: val }
                                : a
                            );
                            setAttributes(updatedAttributes);
                          }}
                        />
                      );
                    })}
                  </div>
                </div>
              ) : (
                <div key={colIndex}></div>
              );
            })}
          </div>
        ))}
      </div>
    </div>
  );
}
