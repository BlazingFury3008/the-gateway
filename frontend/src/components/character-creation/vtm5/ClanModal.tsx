"use client";

import Image from "next/image";
import { vtm5_getClanSymbol } from "@/app/helper";
import { Clan, Discipline } from "@/data/vtm5_characterCreation";

export default function ClanModal({
  clan,
  disciplines,
  onClose,
  isVariant,
}: {
  clan: Clan;
  disciplines: Discipline[];
  onClose: () => void;
  isVariant: boolean | undefined;
}) {
  return (
    <div className="relative bg-[var(--color-background)] text-foreground p-2 sm:p-6 rounded-xl shadow-xl w-full max-w-[95%] sm:max-w-[700px] border border-border overflow-hidden flex flex-col max-h-[60vh]">
      {/* Background Image */}
      <div className="absolute inset-0 opacity-15">
        <Image
          src={vtm5_getClanSymbol(clan.Name)}
          alt={`${clan.Name} Symbol`}
          fill
          className="object-cover blur-[1px] select-none"
        />
      </div>

      {/* Content */}
      <div className="relative z-10 overflow-y-auto pb-4 flex-1 max-h-[50vh]">
        <h2 className="text-xl font-bold text-center mb-2">{clan.Name}</h2>
        <p className="text-xs">{clan.Description}</p>

        <h3 className="mt-4 text-base font-semibold">Clan Bane</h3>
        <p className="text-xs"><span className="font-bold">{clan["Clan Bane"].split(":")[0]}:</span>{clan["Clan Bane"].split(":")[1]}</p>

        {isVariant && clan["Variant Bane"] && (
          <>
            <h3 className="mt-4 text-base font-semibold">Variant Bane</h3>
            <p className="text-xs"><span className="font-bold">{clan["Variant Bane"].split(":")[0]}:</span>{clan["Variant Bane"].split(":")[1]}</p>
            </>
        )}

        <h3 className="mt-4 text-base font-semibold">Disciplines</h3>
        <p className="text-xs">{disciplines.map(d => d.Name).join(", ")}</p>
      </div>

      <button onClick={onClose} className="p-2 bg-red-600 text-white rounded-lg z-20">
        Close
      </button>
    </div>
  );
}
