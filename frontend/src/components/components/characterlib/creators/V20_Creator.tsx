import React, {
  useDebugValue,
  useEffect,
  useMemo,
  useRef,
  useState,
} from "react";
import Divider from "../../Divider";
import InfoLabel from "../../InfoLabel";
import { V20Character, V20Clan, V20Data, V20Nature } from "../DataTypes";
import { BsCircle, BsCircleFill } from "react-icons/bs";
import { SearchableDropdown } from "../../SearchableSelect";

const PAGE_NAMES = [
  "Basic Stats",
  "Attributes",
  "Abilities",
  "Specialties",
  "Disciplines",
  "Virtues",
  "Backgrounds",
  "Freebie Points",
  "Final Overview/Submission",
];

function blankCharacter(): V20Character {
  return {
    basic_stats: {
      name: "",
      concept: "",
      nature: null,
      demeanor: null,
      clan: null,
      starting_generation: 13,
    },
    tier_order: {},
    Attributes: {
      Physical: { Dexterity: 1, Strength: 1, Stamina: 1 },
      Social: { Manipulation: 1, Charisma: 1, Appearance: 1 },
      Mental: { Perception: 1, Intelligence: 1, Wits: 1 },
    },
    Abilities: {
      Talents: {
        Alertness: 0,
        Athletics: 0,
        Awareness: 0,
        Brawl: 0,
        Empathy: 0,
        Expression: 0,
        Intimidation: 0,
        Leadership: 0,
        Streetwise: 0,
        Subterfuge: 0,
      },
      Skills: {
        "Animal Ken": 0,
        Crafts: 0,
        Drive: 0,
        Etiquette: 0,
        Firearms: 0,
        Larceny: 0,
        Melee: 0,
        Performance: 0,
        Stealth: 0,
        Survival: 0,
      },
      Knowledges: {
        Academics: 0,
        Computer: 0,
        Finance: 0,
        Investigation: 0,
        Law: 0,
        Medicine: 0,
        Occult: 0,
        Politics: 0,
        Science: 0,
        Technology: 0,
      },
    },
    Specialties: {},
  };
}

export default function V20_Creator({
  data,
  charData,
  setCharData,
  onCancel,
}: {
  data: V20Data;
  charData: V20Character;
  setCharData: (d: V20Character) => void;
  onCancel: () => void;
}) {
  const [page, setPage] = useState<number>(0);
  const maxPageIndex = PAGE_NAMES.length - 1;

  // allow child pages to block navigation
  const [canProceed, setCanProceed] = useState(true);

  // ✅ scroll the ACTUAL scrolling container, not the window
  const scrollRef = useRef<HTMLDivElement>(null);

  const goToPage = (next: number) => {
    setPage(next);
    // next tick after layout, reset scroll
    requestAnimationFrame(() => {
      scrollRef.current?.scrollTo({ top: 0, behavior: "smooth" });
    });
  };

  // ✅ reset gating when not on gated pages
  useEffect(() => {
    if (page === 0) setCanProceed(true);
  }, [page]);

  return (
    <div className="flex flex-col h-full min-h-0">
      <div className="flex-1 min-h-0 flex flex-col">
        <p className="mb-3 text-sm">
          Set up your new character here, or{" "}
          <span
            className="underline cursor-pointer select-none"
            onClick={() => {
              setCharData(blankCharacter());
              goToPage(0);
            }}
          >
            RESTART
          </span>
        </p>

        <div className="flex-1 min-h-0 border p-4 rounded-lg flex flex-col overflow-hidden">
          <h2 className="text-xl font-bold mb-2">{PAGE_NAMES[page]}</h2>

          <div className="my-2">
            <Divider />
          </div>

          {/* ✅ ONLY THIS SCROLLS */}
          <div ref={scrollRef} className="flex-1 min-h-0 overflow-y-auto pr-2">
            {page === 0 && (
              <V20_BasicStats
                charData={charData}
                setCharData={setCharData}
                data={data}
                setCanProceed={setCanProceed}
              />
            )}

            {page === 1 && (
              <V20_Ability
                charData={charData}
                head_label={["Physical", "Social", "Mental"]}
                score_label={[
                  ["Strength", "Dexterity", "Stamina"],
                  ["Charisma", "Manipulation", "Appearance"],
                  ["Perception", "Intelligence", "Wits"],
                ]}
                values={[7, 5, 3]}
                min_val={1}
                setCharData={setCharData}
                attr_label={"Attributes"}
                setCanProceed={setCanProceed}
                limit={5}
              />
            )}

            {page === 2 && (
              <V20_Ability
                charData={charData}
                head_label={["Talents", "Skills", "Knowledges"]}
                score_label={[
                  [
                    "Alertness",
                    "Athletics",
                    "Awareness",
                    "Brawl",
                    "Empathy",
                    "Expression",
                    "Intimidation",
                    "Leadership",
                    "Streetwise",
                    "Subterfuge",
                  ],
                  [
                    "Animal Ken",
                    "Crafts",
                    "Drive",
                    "Etiquette",
                    "Firearms",
                    "Larceny",
                    "Melee",
                    "Performance",
                    "Stealth",
                    "Survival",
                  ],
                  [
                    "Academics",
                    "Computer",
                    "Finance",
                    "Investigation",
                    "Law",
                    "Medicine",
                    "Occult",
                    "Politics",
                    "Science",
                    "Technology",
                  ],
                ]}
                values={[13, 9, 5]}
                min_val={0}
                setCharData={setCharData}
                attr_label={"Abilities"}
                setCanProceed={setCanProceed}
                limit={3}
              />
            )}

            {page === 3 && (
              <V20_Specialties
                charData={charData}
                setCharData={setCharData}
                setCanProceed={setCanProceed}
              />
            )}

            {page === 4 && (
              <V20_Disciplines
                charData={charData}
                setCharData={setCharData}
                data={data}
              />
            )}
            {page === 5 && <div />}
            {page === 6 && <div />}
            {page === 7 && <div />}
            {page === 8 && <div />}
          </div>
        </div>
      </div>

      {/* BUTTON ROW – pinned to bottom */}
      <div className="mt-4 flex flex-col gap-3 sm:flex-row sm:items-center sm:justify-between w-[80%] md:w-full mx-auto">
        <div className="flex flex-col gap-3 sm:flex-row sm:gap-3 w-full">
          <button
            type="button"
            className="navbar_button w-full sm:w-auto"
            disabled={page === 0}
            onClick={() => goToPage(Math.max(0, page - 1))}
          >
            Prev
          </button>

          {page !== PAGE_NAMES.length - 1 ? (
            <button
              type="button"
              className="navbar_button w-full sm:w-auto"
              disabled={
                page === maxPageIndex || (!canProceed && page !== maxPageIndex)
              }
              onClick={() => goToPage(Math.min(maxPageIndex, page + 1))}
            >
              Next
            </button>
          ) : (
            <button
              type="button"
              className="navbar_button w-full sm:w-auto"
              onClick={() => goToPage(Math.min(maxPageIndex, page + 1))}
            >
              Submit
            </button>
          )}
        </div>

        <button
          type="button"
          className="navbar_button w-full sm:w-auto"
          onClick={onCancel}
        >
          Cancel
        </button>
      </div>
    </div>
  );
}

function V20_BasicStats({
  charData,
  setCharData,
  data,
  setCanProceed,
}: {
  charData: V20Character;
  setCharData: (d: V20Character) => void;
  data: V20Data;
  setCanProceed: (d: boolean) => void;
}) {
  useEffect(() => {
    const b = charData.basic_stats;
    if (!b) return setCanProceed(false);

    setCanProceed(
      b.name?.trim() !== "" &&
        b.clan !== null &&
        b.nature !== null &&
        b.demeanor !== null &&
        b.concept?.trim() !== "" &&
        b.starting_generation !== 0
    );
  }, [charData]);

  return (
    <div className="flex flex-col min-h-0">
      {/* FORM FIELDS */}
      <div className="flex-none">
        <div className="mt-4 grid sm:grid-cols-2 grid-cols-1 gap-3">
          <div>
            <InfoLabel
              label="Name"
              htmlFor="name"
              info="Your character's full name or the name they go by."
            />
            <input
              id="name"
              type="text"
              value={charData.basic_stats?.name || ""}
              onChange={(v) => {
                setCharData({
                  ...charData,
                  basic_stats: {
                    ...charData.basic_stats,
                    name: v.target.value,
                  },
                });
              }}
            />
          </div>

          <div>
            <InfoLabel
              label="Concept"
              htmlFor="concept"
              info="A short phrase that sums up who your character is (e.g. ‘Brooding Tremere Scholar’)."
            />
            <input
              id="concept"
              type="text"
              value={charData.basic_stats?.concept || ""}
              onChange={(v) => {
                setCharData({
                  ...charData,
                  basic_stats: {
                    ...charData.basic_stats,
                    concept: v.target.value,
                  },
                });
              }}
            />{" "}
          </div>

          <div>
            <InfoLabel
              label="Nature"
              htmlFor="nature"
              info="Nature is your character's true inner self—their core personality and what truly fulfills them."
            />
            <SearchableDropdown<V20Nature>
              items={data.nature ?? []}
              value={charData.basic_stats?.nature ?? null}
              onChange={(nature) => {
                setCharData({
                  ...charData,
                  basic_stats: {
                    ...charData.basic_stats,
                    nature,
                  },
                });
              }}
              getKey={(c) => c.id}
              getLabel={(c) => c.name}
              placeholder="-- Select Nature --"
            />
          </div>

          <div>
            <InfoLabel
              label="Demeanor"
              htmlFor="demeanor"
              info="Demeanor is how your character presents themselves to others, which may or may not match their Nature."
            />
            <SearchableDropdown<V20Nature>
              items={data.nature ?? []}
              value={charData.basic_stats?.demeanor ?? null}
              onChange={(demeanor) => {
                setCharData({
                  ...charData,
                  basic_stats: {
                    ...charData.basic_stats,
                    demeanor,
                  },
                });
              }}
              getKey={(c) => c.id}
              getLabel={(c) => c.name}
              placeholder="-- Select Demeanor --"
            />
          </div>

          <div>
            <InfoLabel
              label="Clan"
              htmlFor="clan"
              info="The vampire clan your character belongs to, which determines Disciplines, weaknesses, and social ties."
            />
            <SearchableDropdown<V20Clan>
              items={data.clan ?? []}
              value={charData.basic_stats?.clan ?? null}
              onChange={(clan) => {
                setCharData({
                  ...charData,
                  basic_stats: {
                    ...charData.basic_stats,
                    clan,
                  },
                });
              }}
              getKey={(c) => c.id}
              getLabel={(c) => c.name}
              placeholder="-- Select Clan --"
            />
          </div>

          <div>
            <InfoLabel
              label="Starting Generation"
              htmlFor="startingGen"
              info="The Generation you start play at; This is before the Generation Background is applied..."
            />
            <select
              id="startingGen"
              value={charData?.basic_stats?.starting_generation || 13}
              onChange={(v) =>
                setCharData({
                  ...charData,
                  basic_stats: {
                    ...charData.basic_stats,
                    starting_generation: Number(v.target.value),
                  },
                })
              }
            >
              {[13, 12, 11, 10, 9, 8, 7, 6, 5, 4].map((v, i) => (
                <option value={v} key={i}>
                  {v}
                </option>
              ))}
            </select>
          </div>
        </div>

        <Divider />
      </div>

      {/* INFO + WEAKNESS */}
      <div className="mt-3 whitespace-pre-wrap text-sm text-center">
        {charData.basic_stats?.clan?.information || "N/A"}
      </div>

      <div className="w-[60%] mx-auto">
        <Divider />
      </div>

      <div className="whitespace-pre-wrap text-sm text-center">
        {charData.basic_stats?.clan?.weakness || "N/A"}
      </div>
    </div>
  );
}

function V20_Ability({
  charData,
  setCharData,
  attr_label,
  head_label,
  score_label,
  values,
  min_val,
  setCanProceed,
  limit,
}: {
  charData: V20Character;
  setCharData: (d: V20Character) => void;
  attr_label: string;
  head_label: string[];
  score_label: string[][];
  values: number[];
  min_val: number;
  setCanProceed: (ok: boolean) => void;
  limit: number;
}) {
  type Tier = "NONE" | "PRIMARY" | "SECONDARY" | "TERTIARY";
  const tierOptions: Tier[] = ["NONE", "PRIMARY", "SECONDARY", "TERTIARY"];

  // data is now: { [CategoryName]: { [StatName]: number } }
  const [data, setData] = useState<Record<string, Record<string, number>>>({});

  // ✅ load saved tier order (per attr_label) if it exists
  const [selectedLabel, setSelectedLabel] = useState<Tier[]>(() => {
    // eslint-disable-next-line @typescript-eslint/no-explicit-any
    const saved = (charData as any)?.tier_order?.[attr_label] as
      | Tier[]
      | undefined;
    if (Array.isArray(saved) && saved.length === 3) return saved;
    return ["NONE", "NONE", "NONE"];
  });

  // Load dots from charData as nested: [attr_label][head_label][score_label]
  useEffect(() => {
    // eslint-disable-next-line @typescript-eslint/no-explicit-any
    const section = ((charData as any)?.[attr_label] ?? {}) as Record<
      string,
      Record<string, number>
    >;

    const tmp: Record<string, Record<string, number>> = {};

    [0, 1, 2].forEach((i) => {
      const cat = head_label[i] ?? `Category${i}`;
      const stats = score_label[i] ?? [];
      const catObj = (section?.[cat] ?? {}) as Record<string, number>;

      tmp[cat] = {};
      stats.forEach((stat) => {
        tmp[cat][stat] = catObj?.[stat] ?? min_val;
      });
    });

    setData(tmp);
  }, [score_label, head_label, charData, attr_label, min_val]);

  // ✅ Persist tier order into charData so it survives page changes
  useEffect(() => {
    setCharData({
      ...charData,
      tier_order: {
        // eslint-disable-next-line @typescript-eslint/no-explicit-any
        ...(((charData as any)?.tier_order ?? {}) as Record<string, unknown>),
        [attr_label]: selectedLabel,
      },
    });
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [selectedLabel, attr_label]);

  const sumByIndex = useMemo(() => {
    return [0, 1, 2].map((i) => {
      const cat = head_label[i] ?? `Category${i}`;
      let s = 0;
      (score_label[i] ?? []).forEach((stat) => {
        const cur = data?.[cat]?.[stat] ?? min_val;
        s += Math.max(0, cur - min_val);
      });
      return s;
    });
  }, [data, score_label, head_label, min_val]);

  const maxByIndex = useMemo(() => {
    const tierKey: Record<Exclude<Tier, "NONE">, number> = {
      PRIMARY: values[0] ?? 0,
      SECONDARY: values[1] ?? 0,
      TERTIARY: values[2] ?? 0,
    };

    // NONE => Infinity (lets you swap freely)
    return selectedLabel.map((t) => (t === "NONE" ? Infinity : tierKey[t]));
  }, [selectedLabel, values]);

  const overByIndex = useMemo(() => {
    return [0, 1, 2].map((i) => {
      const max = maxByIndex[i];
      if (!Number.isFinite(max)) return 0;
      return Math.max(0, sumByIndex[i] - max);
    });
  }, [sumByIndex, maxByIndex]);

  useEffect(() => {
    let sum_true = true;
    sumByIndex.forEach((val, key) => {
      if (val !== maxByIndex[key]) sum_true = false;
    });

    setCanProceed(
      !overByIndex.some((x) => x > 0) &&
        !selectedLabel.includes("NONE") &&
        sum_true
    );
  }, [overByIndex, setCanProceed, selectedLabel, sumByIndex, maxByIndex]);

  // Persist dots to charData as nested
  useEffect(() => {
    // eslint-disable-next-line @typescript-eslint/no-explicit-any
    const currentSection =
      (((charData as any)?.[attr_label] ?? {}) as Record<
        string,
        Record<string, number>
      >) ?? {};

    // detect changes
    let changed = false;
    for (const cat of Object.keys(data)) {
      const curCat = currentSection[cat] ?? {};
      const nextCat = data[cat] ?? {};
      for (const stat of Object.keys(nextCat)) {
        if (curCat[stat] !== nextCat[stat]) {
          changed = true;
          break;
        }
      }
      if (changed) break;
    }
    if (!changed) return;

    const mergedSection: Record<string, Record<string, number>> = {
      ...currentSection,
    };
    for (const cat of Object.keys(data)) {
      mergedSection[cat] = {
        ...(mergedSection[cat] ?? {}),
        ...(data[cat] ?? {}),
      };
    }

    setCharData({
      ...charData,
      [attr_label]: mergedSection,
    });
  }, [data, attr_label, setCharData, charData]);

  return (
    <div>
      <div className="grid lg:grid-cols-3 grid-cols-1 justify-between sm:w-[80%] w-[90%] mx-auto min-h-0">
        {[0, 1, 2].map((key) => {
          const cat = head_label[key] ?? `Category${key}`;

          return (
            <div className="w-full" key={key}>
              <h1
                className="sheet-panel-title mb-0 text-center cursor-pointer"
                onClick={() => {
                  // reset all stats in this category
                  setData((prev) => {
                    const next = { ...prev };
                    const nextCat = { ...(next[cat] ?? {}) };
                    (score_label[key] ?? []).forEach((stat) => {
                      nextCat[stat] = min_val;
                    });
                    next[cat] = nextCat;
                    return next;
                  });

                  // reset tier for this category
                  setSelectedLabel((prev) => {
                    const tmp = [...prev];
                    tmp[key] = "NONE";
                    return tmp;
                  });
                }}
              >
                {head_label[key]}
              </h1>

              <div className="text-center py-2 mx-2">
                <select
                  className="select-compact max-w-[180px] uppercase"
                  value={selectedLabel[key]}
                  onChange={(e: React.ChangeEvent<HTMLSelectElement>) => {
                    const next = e.target.value as Tier;
                    setSelectedLabel((prev) => {
                      const tmp = [...prev];
                      tmp[key] = next;
                      return tmp;
                    });
                  }}
                >
                  {tierOptions.map((l) => (
                    <option
                      key={l}
                      value={l}
                      disabled={
                        l !== "NONE" &&
                        selectedLabel.includes(l) &&
                        selectedLabel[key] !== l
                      }
                    >
                      {l}
                    </option>
                  ))}
                </select>

                <div className="text-sm mt-1">
                  <span className="font-semibold">
                    {sumByIndex[key]} /{" "}
                    {Number.isFinite(maxByIndex[key]) ? maxByIndex[key] : "0"}
                  </span>

                  {overByIndex[key] > 0 && (
                    <span className="ml-2 text-red-400">
                      Over by {overByIndex[key]}
                    </span>
                  )}
                </div>
              </div>

              <div>
                {score_label[key]?.map((stat) => {
                  const current = data?.[cat]?.[stat] ?? min_val;

                  return (
                    <div
                      key={stat}
                      className="flex items-center justify-between lg:mx-1 mx-auto lg:w-[100%] w-[90%] px-2 lg:border-x"
                    >
                      <span
                        className="lg:flex-4 flex-2 mr-2 cursor-pointer"
                        onClick={() =>
                          setData((prev) => ({
                            ...prev,
                            [cat]: { ...(prev[cat] ?? {}), [stat]: min_val },
                          }))
                        }
                      >
                        {stat}
                      </span>

                      <span className="flex-1 flex gap-1">
                        {[1, 2, 3, 4, 5].map((v) => (
                          <Attr_Circle
                            key={v}
                            isSolid={v <= current}
                            sum={sumByIndex[key]}
                            max_val={maxByIndex[key]}
                            onClick={() =>
                              setData((prev) => ({
                                ...prev,
                                [cat]: { ...(prev[cat] ?? {}), [stat]: v },
                              }))
                            }
                            delta={v - current}
                            target={v}
                            limit={limit}
                          />
                        ))}
                      </span>
                    </div>
                  );
                })}
              </div>
            </div>
          );
        })}
      </div>

      <div className="w-[50%] mx-auto">
        <Divider />
      </div>
      <div className="subtitle mx-auto text-center mt-1">
        Clicking on an {attr_label} Name will reset the attribute to the minimum
        value
        <br />
        Clicking on a category name will reset the entire category
      </div>
    </div>
  );
}

function Attr_Circle({
  onClick,
  isSolid = false,
  sum,
  max_val,
  delta,
  target,
  limit,
}: {
  onClick?: () => void;
  isSolid?: boolean;
  sum?: number;
  max_val?: number;
  delta: number; // v - current
  target: number; // v
  limit: number; // max rating allowed
}) {
  const overTierCap =
    typeof sum === "number" &&
    typeof max_val === "number" &&
    Number.isFinite(max_val) &&
    !isSolid &&
    delta > 0 &&
    sum + delta > max_val;

  const overStatCap = target > limit;

  const isDisabled = overTierCap || overStatCap;

  return (
    <div
      onClick={isDisabled ? undefined : onClick}
      className={`group inline-flex ${
        isDisabled ? "cursor-not-allowed opacity-40" : "cursor-pointer"
      }`}
      aria-disabled={isDisabled}
    >
      <BsCircle
        className={isSolid ? "hidden" : "flex group-hover:hidden"}
        color="red"
      />
      <BsCircleFill
        className={isSolid ? "flex" : "hidden group-hover:flex"}
        color={isSolid ? "gray" : "red"}
      />
    </div>
  );
}

function V20_Specialties({
  charData,
  setCharData,
  setCanProceed,
}: {
  charData: V20Character;
  setCharData: (d: V20Character) => void;
  setCanProceed: (b: boolean) => void;
}) {
  const SPECIALITY_LIST = [
    "Expression",
    "Performance",
    "Crafts",
    "Academics",
    "Law",
    "Science",
    "Technology",
  ];

  const [traitData, setTraitData] = useState<Record<string, number>>({});

  useEffect(() => {
    const allSkills: Record<string, number> = {
      ...charData.Attributes.Physical,
      ...charData.Attributes.Social,
      ...charData.Attributes.Mental,
      ...charData.Abilities.Talents,
      ...charData.Abilities.Skills,
      ...charData.Abilities.Knowledges,
    };

    setTraitData(allSkills);

    const needsSpecialty = (key: string, val: number) =>
      val >= 4 || (SPECIALITY_LIST.includes(key) && val > 0);

    // build a cleaned specialties map WITHOUT mutating charData
    const prevSpec = charData.Specialties ?? {};
    const nextSpec: Record<string, string> = { ...prevSpec };

    let changed = false;

    for (const [key, val] of Object.entries(allSkills)) {
      // if trait is 0, specialty should not exist
      if (val === 0 && nextSpec[key] != null) {
        delete nextSpec[key];
        changed = true;
      }
    }

    // proceed check: every required key must have non-empty specialty
    let proceed = true;
    for (const [key, val] of Object.entries(allSkills)) {
      if (!needsSpecialty(key, val)) continue;

      const s = nextSpec[key];
      if (typeof s !== "string" || s.trim() === "") {
        proceed = false;
        break;
      }
    }

    setCanProceed(proceed);

    // only write back if we actually removed anything
    if (changed) {
      setCharData({
        ...charData,
        Specialties: nextSpec,
      });
    }
  }, [charData, setCanProceed, setCharData]);

  return (
    <div>
      <div className="grid grid-rows-3 grid-cols-2 gap-3 sm:w-[60%] w-[100%] mx-auto sm:grid-cols-3">
        {Object.keys(traitData).map((key) => {
          const val = traitData[key] ?? 0;
          const show = val >= 4 || (SPECIALITY_LIST.includes(key) && val > 0);
          if (!show) return null;

          return (
            <div key={key}>
              <InfoLabel
                label={`${key}${
                  SPECIALITY_LIST.includes(key) ? "*" : ""
                } [${val}]`}
              />
              <input
                type="text"
                value={charData.Specialties?.[key] ?? ""}
                onChange={(e) => {
                  setCharData({
                    ...charData,
                    Specialties: {
                      ...(charData.Specialties ?? {}),
                      [key]: e.target.value,
                    },
                  });
                }}
              />
            </div>
          );
        })}
      </div>
    </div>
  );
}

function V20_Disciplines({
  charData,
  setCharData,
  data,
}: {
  charData: V20Character;
  setCharData: (d: V20Character) => void;
  data: V20Data;
}) {
  if (charData.basic_stats?.clan?.name != "Caitiff") {
    return (
      <div>
        {charData.basic_stats?.clan?.discipline_1 && (
          <div>{charData.basic_stats?.clan?.discipline_1.name}</div>
        )}
        {charData.basic_stats?.clan?.discipline_2 && (
          <div>{charData.basic_stats?.clan?.discipline_2.name}</div>
        )}{" "}
        {charData.basic_stats?.clan?.discipline_3 && (
          <div>{charData.basic_stats?.clan?.discipline_3.name}</div>
        )}{" "}
        {charData.basic_stats?.clan?.discipline_4 && (
          <div>{charData.basic_stats?.clan?.discipline_4.name}</div>
        )}
      </div>
    );
  }
  else {
    return (
      <div>
        CAITIFF
      </div>
    )
  }
}
