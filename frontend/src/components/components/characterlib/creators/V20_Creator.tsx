import React, { useState } from "react";
import Divider from "../../Divider";
import InfoLabel from "../../InfoLabel";
import { V20Character, V20Clan, V20Data, V20Nature } from "../DataTypes";

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
                  {charData.basic_stats?.clan?.weakness || data.clan[0].weakness}
                </div>
              </div>
            </div>
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
