import React, { useEffect, useState } from "react";
import Divider from "../../Divider";
import InfoLabel from "../../InfoLabel";
import { V20Character, V20Clan, V20Data, V20Nature } from "../DataTypes";
import { BsCircle, BsCircleFill } from "react-icons/bs";

const PAGE_NAMES = ["Basic Stats", "Attributes", "Abilities"];

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

  return (
    // takes full height given by parent
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
        </p>

        {/* IMPORTANT: this container must NOT scroll */}
        <div className="flex-1 min-h-0 border p-4 rounded-lg flex flex-col overflow-hidden">
          <h2 className="text-xl font-bold mb-2">{PAGE_NAMES[page]}</h2>
          <Divider />

          {page === 0 && (
            <div className="flex flex-col min-h-0 overflow-hidden">
              {/* FORM FIELDS (NOT SCROLLABLE) */}
              <div className="flex-none overflow-hidden">
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
                        charData.basic_stats?.demeanor?.id || data.nature[0].id
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
                      value={charData.basic_stats?.clan?.id || data.clan[0].id}
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
                      info="The Generation you start play at; This is before the Generation Background is applied, so typically this is 13th Generation; However for high power games, this may change"
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
                      {[13, 12, 11, 10, 9, 8, 7, 6, 5, 4].map(
                        (v: number, i: number) => (
                          <option value={v} key={i}>
                            {v}
                          </option>
                        )
                      )}
                    </select>
                  </div>
                </div>

                <Divider />
              </div>

              {/* INFO + WEAKNESS (ONLY THIS SCROLLS) */}
              <div className="flex-1 min-h-0 overflow-y-auto pr-2">
                <div className="whitespace-pre-wrap text-sm">
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
            />
          )}
          {page === 2 && (
            <V20_Ability
              charData={charData}
              head_label={["Talents", "Skills", "Knowledges"]}
              score_label={[]}
              values={[]}
              min_val={0}
              setCharData={setCharData}
              attr_label={"Abilities"}
            />
          )}

          {/* TODO: render other pages when page === 1 or 2 */}
        </div>
      </div>

      {/* BUTTON ROW – pinned to bottom of this component */}
      <div className="mt-4 flex items-center justify-between">
        <div className="flex gap-2">
          <button
            type="button"
            className="navbar_button"
            disabled={page === 0}
            onClick={() => setPage((p) => Math.max(0, p - 1))}
          >
            Prev
          </button>

          <button
            type="button"
            className="navbar_button"
            disabled={page === maxPageIndex}
            onClick={() => setPage((p) => Math.min(maxPageIndex, p + 1))}
          >
            Next
          </button>
        </div>

        <button type="button" className="navbar_button" onClick={onCancel}>
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
}: {
  charData: V20Character;
  setCharData: (d: V20Character) => void;
  attr_label: string;
  head_label: string[];
  score_label: string[][];
  values: number[]; // expected order: [PRIMARY, SECONDARY, TERTIARY]
  min_val: number;
}) {
  type Tier = "NONE" | "PRIMARY" | "SECONDARY" | "TERTIARY";
  const tierOptions: Tier[] = ["NONE", "PRIMARY", "SECONDARY", "TERTIARY"];

  const [data, setData] = useState<Record<string, number>>({});

  const [sum, setSum] = useState<number[]>([0, 0, 0]);
  const [maxByIndex, setMaxByIndex] = useState(values);
  const [selectedLabel, setSelectedLabel] = useState<Tier[]>([
    "NONE",
    "NONE",
    "NONE",
  ]);

  // Initialize local dot data from charData
  useEffect(() => {
    const labels = score_label.flat();
    const tmp: Record<string, number> = {};

    labels.forEach((label) => {
      // eslint-disable-next-line @typescript-eslint/no-explicit-any
      const section = (charData as any)?.[attr_label] as
        | Record<string, number>
        | undefined;
      const val = section?.[label];
      tmp[label] = val ?? min_val;
    });

    setData(tmp);
  }, [score_label, charData, attr_label, min_val]);

  useEffect(() => {
    const tier_key = {
      PRIMARY: values[0],
      SECONDARY: values[1],
      TERTIARY: values[2],
    };
    const tmp_arr = selectedLabel.map((label: Tier) => {
      if (label == "NONE") return 0;
      return tier_key[label];
    });

    setMaxByIndex(tmp_arr); // or whatever state you want to update
  }, [selectedLabel, values]);

  useEffect(() => {
    const sum_tmp: number[] = [];
    console.log(data)
    head_label.forEach((hL, hI) => {
      let val = 0;
      score_label[hI].forEach((sL, sI) => {
        val = val + (data[sL] ?? 0) - min_val;
      });
      sum_tmp.push(val);
    });

    setSum(sum_tmp);
  }, [head_label, data, score_label, min_val]);

  return (
    <div>
      <div className="lg:flex-row flex-col flex justify-between flex-1 sm:w-[80%] w-[90%] mx-auto">
        {values.map((val, key) => (
          <div className="w-full" key={key}>
            <h1 className="sheet-panel-title mb-0 text-center">
              {head_label[key]} {maxByIndex[key]} {sum[key]}
            </h1>
            <div className="text-center py-2 mx-2">
              <select
                className="max-w-[180px] text-sm uppercase"
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
            </div>

            <div>
              {score_label[key]?.map((l) => (
                <div
                  key={l}
                  className="flex items-center justify-between lg:mx-1 mx-auto lg:w-[100%] w-[70%] px-2 lg:border-x mb-3"
                >
                  <span className="lg:flex-4 flex-2 mr-2 cursor-pointer" onClick={() => {setData((prev) => ({ ...prev, [l]: min_val }));}}>{l}</span>
                  <span className="flex-1 flex gap-1">
                    {[1, 2, 3, 4, 5].map((v) => (
                      <Attr_Circle
                        key={v}
                        isSolid={v <= (data[l] ?? 0)}
                        sum={sum[key]}
                        max_val={maxByIndex[key]}
                        onClick={() => {
                          setData((prev) => ({ ...prev, [l]: v }));
                        }}
                        val={v - data[l]}
                      />
                    ))}
                  </span>
                </div>
              ))}
            </div>
          </div>
        ))}

      </div>
              <div className="subtitle mx-auto text-center">
          Clicking on an Attributes Name will reset the attribute to the minimum value
        </div>
    </div>
  );
}

function Attr_Circle({
  onClick,
  isSolid = false,
  sum,
  max_val,
  val,
}: {
  onClick?: () => void;
  isSolid?: boolean;
  sum?: number;
  max_val?: number;
  val: number;
}) {
  const isDisabled =
    typeof sum === "number" &&
    typeof max_val === "number" &&
    !isSolid && // allow turning off filled dots; block only adding new ones
    val + sum > max_val;
  return (
    <div
      onClick={isDisabled ? undefined : onClick}
      className={`group inline-flex ${
        isDisabled ? "cursor-not-allowed opacity-40" : "cursor-pointer"
      }`}
      aria-disabled={isDisabled}
    >
      {/* Outline */}
      <BsCircle
        className={isSolid ? "hidden" : "flex group-hover:hidden"}
        color="red"
      />

      {/* Filled */}
      <BsCircleFill
        className={isSolid ? "flex" : "hidden group-hover:flex"}
        color={isSolid ? "gray" : "red"}
      />
    </div>
  );
}
