"use client";
import { useEffect, useState, useMemo, Component, ReactElement } from "react";
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
} from "@/data/vtm5_characterCreation";
import api from "@/lib/axios";
import Attributes from "@/components/character-creation/vtm5/Attributes";
import Skills from "@/components/character-creation/vtm5/Skills";
import Specialities from "@/components/character-creation/vtm5/Specialities";

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

  //Page Logic
  const [page, setPage] = useState<number>(0);
  const searchParams = useSearchParams();
  const mode = searchParams.get("mode");
  const optionalRules = searchParams.get("optional_rules")?.split(" ") || [];

  // Optional Rules
  const or_variantBane = optionalRules.includes("variant-bane");
  const or_additionFlaw = optionalRules.includes("additional-flaw");

  // Merit and Flaw limits based on mode
  const maxMerits = mode === "ancilla" ? 9 : 7;
  const minFlaws = mode === "ancilla" ? 4 : 2;
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

  const attributeLayout = [4, 3, 3, 3, 2, 2, 2, 2, 1];

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
        ] = await Promise.all([
          api.get("/data/vtm5_clan/"),
          api.get("/data/vtm5_clandisciplinejunction/"),
          api.get("/data/vtm5_disciplinegroups/"),
          api.get("/data/vtm5_caitiffmerits/"),
          api.get("/data/vtm5_caitiffflaws/"),
          api.get("/data/vtm5_thinbloodmerits/"),
          api.get("/data/vtm5_thinbloodflaws/"),
        ]);

        // Store fetched data
        setClans(clanRes.data);
        setDisciplineJunction(junctionRes.data);
        setDisciplines(disciplineRes.data);
        setCaitiffMerits(caitiffMeritsRes.data);
        setCaitiffFlaws(caitiffFlawsRes.data);
        setThinbloodMerits(thinbloodMeritsRes.data);
        setThinbloodFlaws(thinbloodFlawsRes.data);
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
      if (or_additionFlaw && flawVal < 0) flawDiff = -flawVal;
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
    (selectedClan !== null && selectedClan < 15 && or_variantBane);

  const allPages: { component: ReactElement; check: boolean }[] = [
    {
      component: (
        <ClanSelection
          clans={clans}
          onClanSelect={setSelectedClan}
          clanSelect={selectedClan}
          isVariant={or_variantBane}
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
          isVariant={or_variantBane}
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
        />
      ),
      check: true,
    },
    {
      component: <Skills />,
      check: true,
    },
    {
      component: <Specialities />,
      check: true,
    },
  ];

  function handleBackStep() {
    for (let index = 1; index < allPages.length; index++) {
      if (allPages[page - index].check) {
        setPage(page - index);
        return;
      }
    }
  }

  function handleNextStep() {
    for (let index = 1; index < allPages.length - page; index++) {
      if (allPages[page + index].check) {
        setPage(page + index);
        return;
      }
    }
  }

  // Disable "Next" button conditions
  const isDisabled = useMemo(() => {
    if (page === 0) return selectedClan === null;
    if (page === 1) {
      if (selectedClan === 15) return meritPoints < 0;
      if (selectedClan === 16)
        return thinbloodAdv.merits.length !== thinbloodAdv.flaws.length;
    }
    if (page === 3) {
      return selectedBane == "";
    }

    return false;
  }, [page, selectedClan, meritPoints, thinbloodAdv]);

  return (
    <div className="mx-auto p-6">
      <h1 className="sm:text-3xl text-xl font-bold text-center">
        Character Creation
      </h1>

      {/* Page transition container */}
      <div className="relative w-full sm:h-[700px] overflow-scroll">
        <div
          key={page}
          className="relative w-full transition-all duration-500 ease-in-out opacity-100 translate-y-0 min-h-[62vh] overflow-scroll"
        >
          {loading && <div>Loading Data..</div>}
          {!loading && allPages[page].component}
        </div>
      </div>

      <div className="flex justify-between mt-6">
        <button
          onClick={handleBackStep}
          disabled={page === 0}
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
