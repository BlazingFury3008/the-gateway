import React, { useEffect, useMemo, useState } from "react";
import Divider from "../../Divider";
import InfoLabel from "../../InfoLabel";
import { V20Character, V20Clan, V20Data, V20Nature } from "../DataTypes";
import { BsCircle, BsCircleFill } from "react-icons/bs";

const PAGE_NAMES = [
  "Basic Stats",
  "Attributes",
  "Abilities",
  "Specialties",
  "Disciplines",
  "Backgrounds",
  "Freebie Points",
  "Final Overview/Submission",
];

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
            className="underline cursor-pointer"
            onClick={() => {
              setCharData({});
              setPage(0);
            }}
          >
            RESTART
          </span>
          {canProceed ? "AHH" : "NAA"}
        </p>

        {/* IMPORTANT: this container must NOT scroll */}
        <div className="flex-1 min-h-0 border p-4 rounded-lg flex flex-col overflow-hidden">
          <h2 className="text-xl font-bold mb-2">{PAGE_NAMES[page]}</h2>

          <div className="my-2">
            <Divider />
          </div>

          {/* ✅ ONLY THIS SCROLLS */}
          <div className="flex-1 min-h-0 overflow-y-auto pr-2">
            {page === 0 && (
              <div className="flex flex-col min-h-0">
                {/* FORM FIELDS */}
                <div className="flex-none">
                  <div className="mt-4 grid grid-cols-2 gap-3">
                    <div>
                      <InfoLabel
                        label="Name"
                        htmlFor="name"
                        info="Your character's full name or the name they go by."
                      />
                      <input id="name" type="text" />
                    </div>

                    <div>
                      <InfoLabel
                        label="Concept"
                        htmlFor="concept"
                        info="A short phrase that sums up who your character is (e.g. ‘Brooding Tremere Scholar’)."
                      />
                      <input id="concept" type="text" />
                    </div>

                    <div>
                      <InfoLabel
                        label="Nature"
                        htmlFor="nature"
                        info="Nature is your character's true inner self—their core personality and what truly fulfills them."
                      />
                      <select
                        name="nature"
                        id="nature"
                        value={
                          charData.basic_stats?.nature?.id || data.nature[0].id
                        }
                        onChange={(v) =>
                          setCharData({
                            ...charData,
                            basic_stats: {
                              ...charData.basic_stats,
                              nature: data.nature.find(
                                (n) => n.id === Number(v.target.value)
                              ),
                            },
                          })
                        }
                      >
                        {data.nature?.map((n: V20Nature, i: number) => (
                          <option key={i} value={n.id}>
                            {n.name} ({n.description})
                          </option>
                        ))}
                      </select>
                    </div>

                    <div>
                      <InfoLabel
                        label="Demeanor"
                        htmlFor="demeanor"
                        info="Demeanor is how your character presents themselves to others, which may or may not match their Nature."
                      />
                      <select
                        name="demeanor"
                        id="demeanor"
                        value={
                          charData.basic_stats?.demeanor?.id ||
                          data.nature[0].id
                        }
                        onChange={(v) =>
                          setCharData({
                            ...charData,
                            basic_stats: {
                              ...charData.basic_stats,
                              demeanor: data.nature.find(
                                (n) => n.id === Number(v.target.value)
                              ),
                            },
                          })
                        }
                      >
                        {data.nature?.map((n: V20Nature, i: number) => (
                          <option key={i} value={n.id}>
                            {n.name} ({n.description})
                          </option>
                        ))}
                      </select>
                    </div>

                    <div>
                      <InfoLabel
                        label="Clan"
                        htmlFor="clan"
                        info="The vampire clan your character belongs to, which determines Disciplines, weaknesses, and social ties."
                      />
                      <select
                        name="clan"
                        id="clan"
                        value={
                          charData.basic_stats?.clan?.id || data.clan[0].id
                        }
                        onChange={(v) =>
                          setCharData({
                            ...charData,
                            basic_stats: {
                              ...charData.basic_stats,
                              clan: data.clan.find(
                                (c) => c.id === Number(v.target.value)
                              ),
                            },
                          })
                        }
                      >
                        {data.clan?.map((c: V20Clan, i: number) => (
                          <option key={i} value={c.id}>
                            {c.name}
                          </option>
                        ))}
                      </select>
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
                <div className="mt-3 whitespace-pre-wrap text-sm">
                  {charData.basic_stats?.clan?.information ||
                    data.clan[0].information}
                </div>

                <div className="w-[60%] mx-auto">
                  <Divider />
                </div>

                <div className="whitespace-pre-wrap text-sm">
                  {charData.basic_stats?.clan?.weakness ||
                    data.clan[0].weakness}
                </div>
              </div>
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
          </div>
        </div>
      </div>

      {/* BUTTON ROW – pinned to bottom */}
      <div className="mt-4 flex flex-col gap-3 sm:flex-row sm:items-center sm:justify-between w-[80%] md:w-full mx-auto">
        {/* Left group */}
        <div className="flex flex-col gap-3 sm:flex-row sm:gap-3 w-full">
          <button
            type="button"
            className="navbar_button w-full sm:w-auto"
            disabled={page === 0}
            onClick={() => setPage((p) => Math.max(0, p - 1))}
          >
            Prev
          </button>

          <button
            type="button"
            className="navbar_button w-full sm:w-auto"
            disabled={
              page === maxPageIndex ||
              ((page === 1 || page === 2) && !canProceed)
            }
            onClick={() => setPage((p) => Math.min(maxPageIndex, p + 1))}
          >
            Next
          </button>
        </div>

        {/* Right group */}
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

export function V20_Ability({
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

  const [data, setData] = useState<Record<string, number>>({});

  // ✅ load saved tier order (per attr_label) if it exists
  const [selectedLabel, setSelectedLabel] = useState<Tier[]>(() => {
    // eslint-disable-next-line @typescript-eslint/no-explicit-any
    const saved = (charData as any)?.tier_order?.[attr_label] as
      | Tier[]
      | undefined;

    if (Array.isArray(saved) && saved.length === 3) return saved;
    return ["NONE", "NONE", "NONE"];
  });

  // Load dots from charData
  useEffect(() => {
    const labels = score_label.flat();
    const tmp: Record<string, number> = {};
    labels.forEach((label) => {
      // eslint-disable-next-line @typescript-eslint/no-explicit-any
      const section = (charData as any)?.[attr_label] as
        | Record<string, number>
        | undefined;
      tmp[label] = section?.[label] ?? min_val;
    });
    setData(tmp);
  }, [score_label, charData, attr_label, min_val]);

  // ✅ Persist tier order into charData so it survives page changes
  useEffect(() => {
    setCharData({
      ...charData,
      // eslint-disable-next-line @typescript-eslint/no-explicit-any
      tier_order: {
        // eslint-disable-next-line @typescript-eslint/no-explicit-any
        ...((charData as any)?.tier_order ?? {}),
        [attr_label]: selectedLabel,
      },
    } as any);
    // intentionally NOT depending on charData to avoid loops
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [selectedLabel, attr_label]);

  const sumByIndex = useMemo(() => {
    return [0, 1, 2].map((i) => {
      let s = 0;
      (score_label[i] ?? []).forEach((k) => {
        const cur = data[k] ?? min_val;
        s += Math.max(0, cur - min_val);
      });
      return s;
    });
  }, [data, score_label, min_val]);

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
    let sum_true: boolean = true;

    sumByIndex.forEach((val, key) => {
      if (val != maxByIndex[key]) sum_true = false;
    });

    setCanProceed(
      !overByIndex.some((x) => x > 0) &&
        !selectedLabel.includes("NONE") &&
        sum_true
    );
  }, [overByIndex, setCanProceed, selectedLabel]);

  // Persist dots to charData
  useEffect(() => {
    // eslint-disable-next-line @typescript-eslint/no-explicit-any
    const currentSection = ((charData as any)?.[attr_label] ?? {}) as Record<
      string,
      number
    >;

    let changed = false;
    for (const k of Object.keys(data)) {
      if (currentSection[k] !== data[k]) {
        changed = true;
        break;
      }
    }
    if (!changed) return;

    setCharData({
      ...charData,
      // eslint-disable-next-line @typescript-eslint/no-explicit-any
      [attr_label]: { ...currentSection, ...data },
    } as any);
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [data]);

  return (
    <div>
      <div className="lg:flex-row flex-col flex justify-between sm:w-[80%] w-[90%] mx-auto">
        {[0, 1, 2].map((key) => (
          <div className="w-full" key={key}>
            <h1
              className="sheet-panel-title mb-0 text-center cursor-pointer"
              onClick={() => {
                setData((prev) => {
                  const tmp = { ...prev };
                  (score_label[key] ?? []).forEach((stat) => {
                    tmp[stat] = min_val;
                  });
                  return tmp;
                });

                const tmp_label = [...selectedLabel];
                tmp_label[key] = "NONE";
                setSelectedLabel(tmp_label);
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
              {score_label[key]?.map((l) => {
                const current = data[l] ?? min_val;

                return (
                  <div
                    key={l}
                    className="flex items-center justify-between lg:mx-1 mx-auto lg:w-[100%] w-[90%] px-2 lg:border-x"
                  >
                    <span
                      className="lg:flex-4 flex-2 mr-2 cursor-pointer"
                      onClick={() =>
                        setData((prev) => ({ ...prev, [l]: min_val }))
                      }
                    >
                      {l}
                    </span>

                    <span className="flex-1 flex gap-1">
                      {[1, 2, 3, 4, 5].map((v) => (
                        <Attr_Circle
                          key={v}
                          isSolid={v <= current}
                          sum={sumByIndex[key]}
                          max_val={maxByIndex[key]}
                          onClick={() =>
                            setData((prev) => ({ ...prev, [l]: v }))
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
        ))}
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
