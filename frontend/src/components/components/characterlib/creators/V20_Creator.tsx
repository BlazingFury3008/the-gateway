import React, { useState } from "react";
import Divider from "../../Divider";
import InfoLabel from "../../InfoLabel";

const PAGE_NAMES = ["Basic Stats", "Attributes", "Abilities"];

export default function V20_Creator({
  data,
  charData,
  setCharData,
  onCancel,
}: {
  data: Record<string, unknown>;
  charData: Record<string, unknown>;
  setCharData: (d: Record<string, unknown>) => void;
  onCancel: () => void;
}) {
  const [page, setPage] = useState<number>(0);
  const maxPageIndex = PAGE_NAMES.length - 1;

  return (
    // takes full height given by parent
    <div className="flex flex-col h-full">
      {/* MAIN CONTENT (fills space above buttons) */}
      <div className="flex-1 flex flex-col">
        <p className="mb-3 text-sm">Set up your new character here.</p>

        <div className="flex-1 overflow-y-auto min-h-[100px] border p-4 rounded-lg">
          <h2 className="text-xl font-bold mb-2">{PAGE_NAMES[page]}</h2>
          <Divider />

          {page === 0 && (
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
                <input id="nature" type="text" />
              </div>

              <div>
                <InfoLabel
                  label="Demeanor"
                  htmlFor="demeanor"
                  info="Demeanor is howf your character presents themselves to others, which may or may not match their Nature."
                />
                <input id="demeanor" type="text" />
              </div>

              <div>
                <InfoLabel
                  label="Clan"
                  htmlFor="clan"
                  info="The vampire clan your character belongs to, which determines Disciplines, weaknesses, and social ties."
                />
                <input id="clan" type="text" />
              </div>

              <div>
                <InfoLabel
                  label="Starting Generation"
                  htmlFor="startingGen"
                  info="The Generation you start play at; This is before the Generation Background is applied, so typically this is 13th Generation; However for high power games, this may change"
                />
                <select
                  id="startingGen"
                  value={charData?.basic_stats?.starting_gen || 13}
                  onChange={(v) =>
                    setCharData({
                      ...charData,
                      basic_stats: {
                        ...charData.basic_stats,
                        starting_gen: Number(v.target.value),
                      },
                    })
                  }
                >
                  {[13, 12, 11, 10, 9, 8, 7, 6, 5, 4].map((v) => {
                    return <option value={v}>{v}</option>;
                  })}
                </select>
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
