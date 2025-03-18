/* eslint-disable react-hooks/rules-of-hooks */
import { defaultSkills } from "@/data/vtm5_characterCreation";
import { Circle } from "lucide-react";
import React, { useEffect, useState } from "react";

export default function Skills({
  skills,
  setSkills,
  skillsLayout,
}: {
  skills: { skill: string; value: number }[];
  setSkills: (newSkills: { skill: string; value: number }[]) => void;
  skillsLayout: number[][];
}) {
  const [allowed, setAllowed] = useState<number[]>([]);
  const [specAllowed, setSpecAllowed] = useState<number[]>([]);
  const [balancedAllowed, setBalancedAllowed] = useState<number[]>([]);
  const [jackAllowed, setJackAllowed] = useState<number[]>([]);

  const [isSpec, setIsSpec] = useState(true);
  const [isBala, setIsBala] = useState(true);
  const [isJack, setIsJack] = useState(true);

  function compareArrays(array1: number[], array2: number[]) {
    const tmp = [...array1]; // Copy array1

    for (const val of array2) {
      const index = tmp.indexOf(val);
      if (index === -1) {
        return false; // If a value is missing, return false
      }
      tmp.splice(index, 1); // Remove one occurrence
    }

    return true; // If all values matched, return true
  }

  function subtractArrays(array1: number[], array2: number[]) {
    const tmp = [...array1]; // Copy original array

    // Remove only one occurrence of each value from `array2` in `tmp`
    array2.forEach((val) => {
      const index = tmp.indexOf(val);
      if (index !== -1) tmp.splice(index, 1); // Remove only one occurrence
    });

    return tmp;
  }

  useEffect(() => {
    if (!Array.isArray(skills) || !Array.isArray(skillsLayout)) return;

    // Create copies of skill layouts
    const specTmp = [...skillsLayout[0]];
    const balTmp = [...skillsLayout[1]];
    const jackTmp = [...skillsLayout[2]];

    // Get skill values excluding `0`
    const skillVals = skills.map((val) => val.value).filter((val) => val !== 0);

    // Check if the skill selection can still match each layout
    const isSpecTmp = compareArrays(specTmp, skillVals);
    const isBalTmp = compareArrays(balTmp, skillVals);
    const isJackTmp = compareArrays(jackTmp, skillVals);

    // Remove selected skill values from the respective layouts (one occurrence at a time)
    skills.forEach((skill) => {
      const removeFromLayout = (layout: number[]) => {
        const index = layout.indexOf(skill.value);
        if (index !== -1) layout.splice(index, 1); // Remove one occurrence
      };

      removeFromLayout(specTmp);
      removeFromLayout(balTmp);
      removeFromLayout(jackTmp);
    });

    // Update state with the filtered allowed values
    const allowedValues = [
      ...new Set([
        ...(isSpecTmp ? specTmp : []),
        ...(isBalTmp ? balTmp : []),
        ...(isJackTmp ? jackTmp : []),
      ]),
    ];

    setAllowed(allowedValues);
    setSpecAllowed(specTmp);
    setBalancedAllowed(balTmp);
    setJackAllowed(jackTmp);

    setIsSpec(isSpecTmp);
    setIsBala(isBalTmp);
    setIsJack(isJackTmp);
  }, [skills, skillsLayout]);

  // Organizing skills in a column-major order
  const numColumns = 9;
  const numRows = Math.ceil(skills.length / numColumns);

  const columnMajorSkills: { skill: string; value: number }[][] = [];
  for (let col = 0; col < numColumns; col++) {
    columnMajorSkills.push([]);
    for (let row = 0; row < numRows; row++) {
      const index = row * numColumns + col;
      if (index < skills.length) {
        columnMajorSkills[col].push(skills[index]);
      }
    }
  }

  return (
    <div>
      <div className="text-center mb-4 overflow-none sm:scroll-m-0">
        <h2 className="text-lg sm:text-xl font-bold p-0">Skills</h2>
        <button
          className="text-xs underline text-[var(--color-primary)] hover:text-[var(--color-primary-hover)]"
          onClick={() =>
            setSkills(defaultSkills.map((skill) => ({ ...skill })))
          }
        >
          Reset
        </button>
        <div className="sm:w-[50%] w-full text-center mx-auto text-sm space-y-2">
          {[
            {
              name: "Specialized",
              isValid: isSpec,
              allowed: specAllowed,
              layout: skillsLayout[0],
            },
            {
              name: "Balanced",
              isValid: isBala,
              allowed: balancedAllowed,
              layout: skillsLayout[1],
            },
            {
              name: "Jack-Of-All",
              isValid: isJack,
              allowed: jackAllowed,
              layout: skillsLayout[2],
            },
          ].map(({ name, isValid, allowed, layout }, index) => {
            const removedValues = subtractArrays(layout, allowed);

            // If the layout is not valid, show "N/A"
            if (!isValid) {
              return (
                <div key={index} className="font-bold text-base sm:text-sm">
                  {name}: N/A <br />
                </div>
              );
            }

            return (
              <div
                key={index}
                className="flex flex-col sm:flex-row justify-center items-center text-center"
              >
                {/* Name */}
                <span className="font-bold text-base sm:text-sm">{name}:</span>

                <div>
                  {/* Allowed Values */}
                  <span className="text-base sm:text-sm">
                    {allowed.length > 0 ? (
                      allowed.join(",")
                    ) : (
                      <span className="text-[var(--color-muted)]">Done!</span>
                    )}
                  </span>

                  {/* Strikethrough (Used Values) - Only Show if `allowed.length > 0` */}
                  {allowed.length > 0 && removedValues.length > 0 && (
                    <span className="text-[var(--color-foreground-soft)] inline-flex items-center whitespace-nowrap">
                      <span>|</span>
                      {removedValues.map((val, idx) => (
                        <span key={idx} className="line-through">
                          {val}
                          {idx !== removedValues.length - 1 && ","}
                        </span>
                      ))}
                    </span>
                  )}
                </div>
              </div>
            );
          })}
        </div>
        <div className="text-xs w-[50%] text-center mx-auto">
          Press the skill name to set the skill to 0
        </div>
      </div>

      {/* Grid layout for column-major order */}
      <div className="grid sm:grid-cols-3 grid-rows-3 gap-4 sm:gap-2 w-full lg:px-5 lg:w-[70%] md:w-[85%] sm:w-[90%] mx-auto">
        {Array.from({ length: numRows }).map((_, rowIndex) => (
          <div key={rowIndex} className="grid grid-rows-3 gap-4">
            {columnMajorSkills.map((column, colIndex) => {
              const skill = column[rowIndex];
              return skill ? (
                <div
                  key={colIndex}
                  className="flex justify-between items-center sm:w-[70%]"
                >
                  <div
                    className="text-[var(--color-foreground)] text-ellipsis sm:w-[40%] w-[50%] overflow-hidden cursor-pointer"
                    onClick={() => {
                      setSkills(
                        skills.map((a) =>
                          a.skill === skill.skill ? { ...a, value: 0 } : a
                        )
                      );
                    }}
                  >
                    {skill.skill}
                  </div>
                  <div className="flex space-x-1 sm:w-[60%] w-[50%] justify-end">
                    {[1, 2, 3, 4, 5].map((val) => {
                      const isFilled = skill.value >= val;
                      return (
                        <Circle
                          key={val}
                          className={`${
                            !allowed.includes(val) && skill.value < val
                              ? "text-[var(--color-danger)]"
                              : "text-[var(--color-foreground)] cursor-pointer"
                          } ${isFilled && "fill-[var(--color-foreground)]"}`}
                          onClick={() => {
                            if (!allowed.includes(val)) {
                              return;
                            }
                            const updatedSkills = skills.map((a) =>
                              a.skill === skill.skill
                                ? { ...a, value: val }
                                : a
                            );
                            setSkills(updatedSkills);
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
