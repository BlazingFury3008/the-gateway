"use client";
import { useEffect, useState, useMemo, ReactElement } from "react";
import { useSearchParams } from "next/navigation";

import ClanSelection from "@/components/character-creation/vtm5/ClanSelection";
import ThinbloodBackgrounds from "@/components/character-creation/vtm5/ThinbloodBackgrounds";
import CaitiffBackgrounds from "@/components/character-creation/vtm5/CaitiffBackgrounds";
import ClanBaneSelection from "@/components/character-creation/vtm5/ClanBaneSelection";

import {
  Clan,
  Discipline,
  CaitiffBackground,
  ThinbloodBackground,
  DisciplineJunction,
  defaultAttributes,
  defaultSkills,
  DisciplinePower,
  default_config,
  config_interface,
} from "@/data/vtm5_characterCreation";
import api from "@/lib/axios";
import Attributes from "@/components/character-creation/vtm5/Attributes";
import Skills from "@/components/character-creation/vtm5/Skills";
import Specialities from "@/components/character-creation/vtm5/Specialities";
import Disciplines from "@/components/character-creation/vtm5/Disciplines";
import Config from "@/components/character-creation/vtm5/Config";
import BasicStats from "@/components/character-creation/vtm5/BasicStats";

export default function CharacterCreationPage() {
  //Selected Data
  const [selectedClan, setSelectedClan] = useState<number | null>(null);
  const [thinbloodAdv, setThinbloodAdv] = useState<{
    merits: ThinbloodBackground[];
    flaws: ThinbloodBackground[];
  }>({ merits: [], flaws: [] });
  const [caitiffAdv, setCaitiffAdv] = useState<{
    merits: CaitiffBackground[];
    flaws: CaitiffBackground[];
  }>({ merits: [], flaws: [] });
  const [selectedBane, setSelectedBane] = useState<string>("");
  const [selectedAttributes, setSelectedAttributes] = useState<
    { attribute: string; value: number }[]
  >([...defaultAttributes]);
  const [selectedSkills, setSelectedSkills] = useState<
    { skill: string; value: number }[]
  >([...defaultSkills]);
  const [specialities, setSpecialities] = useState<{
    craft: string;
    science: string;
    performance: string;
    academics: string;
    dropdownSkill: string;
    dropdownSpec: string;
  }>({
    craft: "",
    science: "",
    performance: "",
    academics: "",
    dropdownSkill: "",
    dropdownSpec: "",
  });
  const [selectedDisciplinePowers, setSelectedDisciplinePowers] = useState<
    DisciplinePower[]
  >([]);

  //Page Logic
  const [page, setPage] = useState<number>(0);
  const [isConfirm, setIsConfirm] = useState(false);
  const [configOption, setConfigOptions] =
    useState<config_interface>(default_config);

  // Merit and Flaw limits based on mode
  const maxMerits = configOption.age === "ancilla" ? 9 : 7;
  const minFlaws = configOption.age === "ancilla" ? 4 : 2;
  const [meritPoints, setMeritPoints] = useState(maxMerits);
  const [flawPoints, setFlawPoints] = useState(minFlaws);

  // Data State
  const [clans, setClans] = useState<Clan[]>([]);
  const [disciplineJunction, setDisciplineJunction] = useState<
    DisciplineJunction[]
  >([]);
  const [disciplines, setDisciplines] = useState<Discipline[]>([]);
  const [caitiffMerits, setCaitiffMerits] = useState<CaitiffBackground[]>([]);
  const [caitiffFlaws, setCaitiffFlaws] = useState<CaitiffBackground[]>([]);
  const [thinbloodMerits, setThinbloodMerits] = useState<ThinbloodBackground[]>(
    []
  );
  const [thinbloodFlaws, setThinbloodFlaws] = useState<ThinbloodBackground[]>(
    []
  );
  const [disciplinePowers, setDisciplinePowers] = useState<DisciplinePower[]>(
    []
  );
  const [extraDisciplinePowers, setExtraDisciplinePowers] = useState();
  const [extraDisciplineGroups, setExtraDisciplineGroups] = useState();
  const [merits, setMerits] = useState();
  const [flaws, setFlaws] = useState();
  const [havenMerits, setHavenMerits] = useState();
  const [havenFlaws, setHavenFlaws] = useState();
  const [predatorTypes, setPredatorTypes] = useState();

  const attributeLayout = [4, 3, 3, 3, 2, 2, 2, 2, 1];
  const specialised = [4, 3, 3, 3, 2, 2, 2, 1, 1, 1];
  const balanced = [3, 3, 3, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1];
  const jackofall = [3, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1];

  //Loading
  const [loading, setLoading] = useState(true);

  // Fetch all required data on mount
  useEffect(() => {
    async function fetchData() {
      try {
        setLoading(true);
        const [
          clanRes,
          junctionRes,
          disciplineRes,
          caitiffMeritsRes,
          caitiffFlawsRes,
          thinbloodMeritsRes,
          thinbloodFlawsRes,
          disciplinePowersRes,
          extraDisciplineGroupsRes,
          extraDisciplinePowersRes,
          meritsRes,
          flawsRes,
          havenMeritsRes,
          havenFlawsRes,
          predatorTypeRes,
        ] = await Promise.all([
          api.get("/data/vtm5_clan/"),
          api.get("/data/vtm5_clandisciplinejunction/"),
          api.get("/data/vtm5_disciplinegroups/"),
          api.get("/data/vtm5_caitiffmerits/"),
          api.get("/data/vtm5_caitiffflaws/"),
          api.get("/data/vtm5_thinbloodmerits/"),
          api.get("/data/vtm5_thinbloodflaws/"),
          api.get("/data/vtm5_disciplinepowers/"),
          api.get("/data/vtm5_extradisciplinegroups/"),
          api.get("/data/vtm5_extradisciplinepowers/"),
          api.get("/data/vtm5_merits/"),
          api.get("/data/vtm5_flaws/"),
          api.get("/data/vtm5_havenmerits/"),
          api.get("/data/vtm5_havenflaws/"),
          api.get("/data/vtm5_predatortype/"),
        ]);

        // Store fetched data
        setClans(clanRes.data);
        setDisciplineJunction(junctionRes.data);
        setDisciplines(disciplineRes.data);
        setCaitiffMerits(caitiffMeritsRes.data);
        setCaitiffFlaws(caitiffFlawsRes.data);
        setThinbloodMerits(thinbloodMeritsRes.data);
        setThinbloodFlaws(thinbloodFlawsRes.data);
        setDisciplinePowers(disciplinePowersRes.data);
        setExtraDisciplineGroups(extraDisciplineGroupsRes.data);
        setExtraDisciplinePowers(extraDisciplinePowersRes.data);
        setMerits(meritsRes.data);
        setFlaws(flawsRes.data);
        setHavenMerits(havenMeritsRes.data);
        setHavenFlaws(havenFlawsRes.data);
        setPredatorTypes(predatorTypeRes.data);
      } catch (error) {
        console.error("Error fetching data:", error);
      } finally {
        setLoading(false);
      }
    }

    fetchData();
  }, []);

  useEffect(() => {
    setSelectedBane(
      selectedClan != null
        ? clans.filter((clan) => clan.ID == selectedClan)[0]["Clan Bane"]
        : ""
    );
  }, [selectedClan]);

  useEffect(() => {
    if (selectedClan != 15) {
      setCaitiffAdv({ merits: [], flaws: [] });
    }

    if (selectedClan != 16) {
      setThinbloodAdv({ merits: [], flaws: [] });
    }
  }, [page]);

  // Update Merit/Flaw points dynamically
  useEffect(() => {
    let flawDiff = 0;
    if (caitiffAdv.flaws) {
      const flawVal =
        minFlaws -
        caitiffAdv.flaws.reduce(
          (acc, flaw) => acc + parseInt(flaw.Values, 10) || 0,
          0
        );
      if (configOption.additionalFlaw && flawVal < 0) flawDiff = -flawVal;
      setFlawPoints(Math.max(flawVal, 0));
    }
    if (caitiffAdv.merits) {
      setMeritPoints(
        maxMerits +
          flawDiff -
          caitiffAdv.merits.reduce(
            (acc, merit) => acc + parseInt(merit.Values, 10) || 0,
            0
          )
      );
    }
  }, [caitiffAdv]);

  // Check if Clan Bane selection is required
  const requiresBaneSelection =
    (selectedClan === 15 &&
      caitiffAdv.flaws.some((flaw) => flaw.Name === "Clan Curse")) ||
    (selectedClan === 16 &&
      thinbloodAdv.flaws.some((flaw) => flaw.Name === "Clan Curse")) ||
    (selectedClan !== null && selectedClan < 15 && configOption.variantBane);

  const allPages: { component: ReactElement; check: boolean }[] = [
    {
      component: (
        <Config
          configOption={configOption}
          setConfigOptions={setConfigOptions}
        />
      ),
      check: true,
    },
    {
      component: <BasicStats />,
      check: true,
    },
    {
      component: (
        <ClanSelection
          clans={clans}
          onClanSelect={setSelectedClan}
          clanSelect={selectedClan}
          isVariant={configOption.variantBane}
          disciplines={disciplines}
          disciplineJunction={disciplineJunction}
        />
      ),
      check: true,
    },
    {
      component: (
        <ThinbloodBackgrounds
          onBackgroundSelect={setThinbloodAdv}
          backgroundSelect={thinbloodAdv}
          merits={thinbloodMerits}
          flaws={thinbloodFlaws}
        />
      ),
      check: selectedClan == 16,
    },
    {
      component: (
        <CaitiffBackgrounds
          onBackgroundSelect={setCaitiffAdv}
          backgroundSelect={caitiffAdv}
          merits={caitiffMerits}
          flaws={caitiffFlaws}
          totalMerits={meritPoints}
          totalFlaws={flawPoints}
        />
      ),
      check: selectedClan == 15,
    },
    {
      component: (
        <ClanBaneSelection
          selectedClan={selectedClan}
          thinbloodAdv={thinbloodAdv}
          isVariant={configOption.variantBane}
          clans={clans}
          setSelectedBane={setSelectedBane}
          selectedBane={selectedBane}
        />
      ),
      check: requiresBaneSelection,
    },
    {
      component: (
        <Attributes
          attributes={selectedAttributes}
          setAttributes={setSelectedAttributes}
          attributeLayout={attributeLayout}
        />
      ),
      check: !true,
    },
    {
      component: (
        <Skills
          skills={selectedSkills}
          setSkills={setSelectedSkills}
          skillsLayout={[specialised, balanced, jackofall]}
        />
      ),
      check: !true,
    },
    {
      component: (
        <Specialities
          skills={selectedSkills}
          specialities={specialities}
          setSpecialities={setSpecialities}
        />
      ),
      check: selectedSkills.filter((val) => val.value > 0).length > 0,
    },
    {
      component: (
        <Disciplines
          selectedClan={selectedClan}
          disciplineJunction={disciplineJunction}
          disciplinePowers={disciplinePowers}
          disciplineGroups={disciplines}
          selectedDisciplines={selectedDisciplinePowers}
          setSelectedDisciplines={setSelectedDisciplinePowers}
          thinbloodAdv={thinbloodAdv}
        />
      ),
      check: true,
    },
  ];

  function handleBackStep() {
    for (let index = 1; index < allPages.length; index++) {
      if (allPages[page - index].check) {
        setPage(page - index);
        window.scrollTo({ top: 0, behavior: "smooth" }); // Scrolls to top smoothly
        return;
      }
    }
  }

  function handleNextStep() {
    if (page == 0) {
      setIsConfirm(true);
      return;
    }
    for (let index = 1; index < allPages.length - page; index++) {
      if (allPages[page + index].check) {
        setPage(page + index);
        window.scrollTo({ top: 0, behavior: "smooth" }); // Scrolls to top smoothly
        return;
      }
    }
  }

  // Disable "Next" button conditions
  const isDisabled = useMemo(() => {
    if (page === 2) return selectedClan === null;
    if (page === 3) {
      if (selectedClan === 15) return meritPoints < 0;
      if (selectedClan === 16)
        return thinbloodAdv.merits.length !== thinbloodAdv.flaws.length;
    }
    if (page === 5) {
      return selectedBane == "";
    }
    if (page == 6) {
      return (
        JSON.stringify(selectedAttributes.map((val) => val.value).sort()) !==
        JSON.stringify([...attributeLayout].sort())
      );
    }
    if (page == 7) {
      return !(
        JSON.stringify(
          selectedSkills
            .map((val) => val.value)
            .filter((val) => val != 0)
            .sort()
        ) === JSON.stringify([...specialised].sort()) ||
        JSON.stringify(
          selectedSkills
            .map((val) => val.value)
            .filter((val) => val != 0)
            .sort()
        ) === JSON.stringify([...balanced].sort()) ||
        JSON.stringify(
          selectedSkills
            .map((val) => val.value)
            .filter((val) => val != 0)
            .sort()
        ) === JSON.stringify([...jackofall].sort())
      );
    }
    if (page === 8) {
      const getSkillValue = (skillName: string) => {
        const skill = selectedSkills.find((val) => val.skill === skillName);
        return skill ? skill.value : 0; // Default to 0 if skill is not found to avoid errors
      };

      const academics =
        getSkillValue("Academics") == 0 || specialities.academics !== "";
      const science =
        getSkillValue("Science") == 0 || specialities.science !== "";
      const performance =
        getSkillValue("Performance") == 0 || specialities.performance !== "";
      const craft = getSkillValue("Craft") == 0 || specialities.craft !== "";
      const dropdownSpec = specialities.dropdownSpec !== "";
      const dropdownSkill = specialities.dropdownSkill !== "";

      return !(
        academics &&
        science &&
        performance &&
        craft &&
        dropdownSpec &&
        dropdownSkill
      );
    }

    return false;
  }, [
    page,
    selectedClan,
    meritPoints,
    thinbloodAdv,
    selectedAttributes,
    attributeLayout,
    selectedSkills,
    specialities,
  ]);

  return (
    <div className="mx-auto py-6 px-2 sm:px-6">
      <h1 className="sm:text-3xl text-xl font-bold text-center">
        Character Creation
      </h1>

      {/* Page transition container */}
      <div className="relative w-full sm:h-[700px] overflow-scroll sm:overflow-hidden">
        <div
          key={page}
          className="relative w-full transition-all duration-500 ease-in-out opacity-100 translate-y-0 min-h-[62vh] overflow-scroll"
        >
          {loading && <div>Loading Data..</div>}
          {!loading && allPages[page].component}
        </div>
        {isConfirm && (
  <div className="fixed inset-0 z-50 backdrop-blur-sm flex items-center justify-center">
    <div className="bg-[var(--color-background)] text-[var(--color-foreground)] rounded-lg p-6 shadow-lg w-full max-w-md modal-enter">
      <h2 className="text-xl font-bold mb-4">Confirm Configuration</h2>
      <p className="mb-6">
        Are you sure you want to continue? Your configuration choices (such as Age, Variant Bane, etc.) will be locked in and cannot be changed later.
      </p>
      <div className="flex justify-end space-x-4">
        <button
          onClick={() => setIsConfirm(false)}
          className="btn bg-gray-300 text-gray-900 hover:bg-gray-400 dark:bg-gray-700 dark:text-white dark:hover:bg-gray-600"
        >
          Cancel
        </button>
        <button
          onClick={() => {
            setIsConfirm(false);
            setPage(1); // Proceed to next step
          }}
          className="btn btn-danger"
        >
          Confirm
        </button>
      </div>
    </div>
  </div>
)}

      </div>

      <div className="flex justify-between mt-6">
        <button
          onClick={handleBackStep}
          disabled={page < 2}
          className="px-6 py-3 bg-red-600 text-white rounded-lg shadow-md disabled:bg-gray-400 transition-all duration-300 ease-in-out hover:bg-red-700"
        >
          Back
        </button>

        <button
          onClick={handleNextStep}
          disabled={isDisabled}
          className={`px-6 py-3 text-white rounded-lg shadow-md transition-all duration-300 ease-in-out ${
            isDisabled
              ? "bg-gray-400 cursor-not-allowed"
              : "bg-red-600 hover:bg-red-700"
          }`}
        >
          Next
        </button>
      </div>
    </div>
  );
}
