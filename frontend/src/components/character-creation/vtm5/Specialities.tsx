import React, { useEffect, useState } from "react";

export default function Specialities({
  skills,
  specialities,
  setSpecialities,
}: {
  skills: { skill: string; value: number }[];
  specialities: {
    craft: string;
    science: string;
    performance: string;
    academics: string;
    dropdownSkill: string;
    dropdownSpec: string;
  };
  setSpecialities: (data: {
    craft: string;
    science: string;
    performance: string;
    academics: string;
    dropdownSkill: string;
    dropdownSpec: string;
  }) => void;
}) {
  const [academicSpec, setAcademicSpec] = useState<string>(specialities.academics);
  const [scienceSpec, setScienceSpec] = useState<string>(specialities.science);
  const [performanceSpec, setPerformanceSpec] = useState<string>(specialities.performance);
  const [craftSpec, setCraftSpec] = useState<string>(specialities.craft);
  const [dropdownSkill, setDropdownSkill] = useState<string>(specialities.dropdownSkill);
  const [dropdownSpec, setDropdownSpec] = useState<string>(specialities.dropdownSpec);

  const [dropdownValue, setDropdownValue] = useState<string[]>([]);

  useEffect(() => {
    setDropdownValue(
      skills.filter((val) => val.value != 0).map((val) => val.skill)
    );
  }, [skills]);

  useEffect(() => {
    setSpecialities({
      craft: craftSpec,
      science: scienceSpec,
      academics: academicSpec,
      performance: performanceSpec,
      dropdownSpec: dropdownSpec,
      dropdownSkill: dropdownSkill
    })

  }, [academicSpec, scienceSpec, performanceSpec, craftSpec, dropdownSpec, dropdownSkill])

  return (
    <div>
      <div className="text-center mb-4 overflow-none sm:scroll-m-0">
        <h2 className="text-lg sm:text-xl font-bold p-0">Specialities</h2>
      </div>
      <div className="lg:w-[30%] md:w-[40%] sm:w-[60%] mx-auto space-y-3">
        {skills.filter((val) => val.skill == "Academics")[0].value != 0 && (
          <div>
            {" "}
            <input
              className="input"
              type="text"
              value={academicSpec}
              onChange={(e) => setAcademicSpec(e.target.value)}
              placeholder="Academics Speciality..."
            />
          </div>
        )}
        {skills.filter((val) => val.skill == "Science")[0].value != 0 && (
          <div>
            {" "}
            <input
              className="input"
              type="text"
              value={scienceSpec}
              onChange={(e) => setScienceSpec(e.target.value)}
              placeholder="Science Speciality..."
            />
          </div>
        )}{" "}
        {skills.filter((val) => val.skill == "Performance")[0].value != 0 && (
          <div>
            {" "}
            <input
              className="input"
              type="text"
              value={performanceSpec}
              onChange={(e) => setPerformanceSpec(e.target.value)}
              placeholder="Performance Speciality..."
            />
          </div>
        )}{" "}
        {skills.filter((val) => val.skill == "Craft")[0].value != 0 && (
          <div>
            {" "}
            <input
              className="input"
              type="text"
              value={craftSpec}
              onChange={(e) => setCraftSpec(e.target.value)}
              placeholder="Craft Speciality..."
            />
          </div>
        )}
        <div className="flex space-x-2">
          <SpecDropdown
            dropdownOptions={dropdownValue}
            selectedSkill={dropdownSkill}
            onSelect={setDropdownSkill}
          />
          <input
            className="input"
            type="text"
            value={dropdownSpec}
            onChange={(e) => setDropdownSpec(e.target.value)}
            placeholder={dropdownSkill + " Speciality..."}
          />
        </div>
      </div>
    </div>
  );
}

function SpecDropdown({
  dropdownOptions,
  selectedSkill,
  onSelect,
}: {
  dropdownOptions: string[];
  selectedSkill: string;
  onSelect: (val: string) => void;
}) {
  const [isOpen, setIsOpen] = useState(false);
  const [search, setSearch] = useState("");

  const filteredSkills = dropdownOptions.filter((skill) =>
    skill.toLowerCase().includes(search.toLowerCase())
  );

  return (
    <div className="relative w-full max-w-[40vw] sm:max-w-sm flex flex-col items-center">
      <button
        className="w-full btn bg-[var(--color-background-soft)] text-[var(--color-foreground)] border border-[var(--color-border)] flex justify-between items-center shadow-md"
        onClick={() => setIsOpen(!isOpen)}
      >
        {selectedSkill != "" ? selectedSkill : "Select Skill"}
        <span
          className={`transition-transform ${
            isOpen ? "rotate-180" : "rotate-0"
          }`}
        >
          ▼
        </span>
      </button>

      {isOpen && (
        <div className="absolute left-0 mt-1 w-full bg-[var(--color-background)] border border-[var(--color-border)] rounded-md shadow-lg max-h-60 overflow-y-auto z-10 p-2 no-scrollbar">
          <input
            type="text"
            placeholder="Search Skill..."
            value={search}
            onChange={(e) => setSearch(e.target.value)}
            className="input mb-2"
          />

          <ul className="text-[var(--color-foreground)] text-sm">
            {filteredSkills.length > 0 ? (
              filteredSkills.map((skill, index) => (
                <li
                  key={index}
                  className={`px-4 py-2 cursor-pointer hover:bg-[var(--color-background-hover)] rounded-md ${
                    selectedSkill == skill
                      ? "bg-[var(--color-background-hover)]"
                      : ""
                  }`}
                  onClick={() => {
                    onSelect(skill);
                    setSearch("");
                    setIsOpen(false);
                  }}
                >
                  {skill}
                </li>
              ))
            ) : (
              <li className="px-4 py-2 text-gray-500">No Skill found</li>
            )}
          </ul>
        </div>
      )}
    </div>
  );
}
