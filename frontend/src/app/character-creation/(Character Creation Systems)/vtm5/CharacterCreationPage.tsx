"use client";

import { useEffect, useState } from "react";
import Image from "next/image";
import { vtm5_getClanSymbol } from "@/app/helper";
import { Info } from "lucide-react";
import { VampireData } from "./page";


export default function CharacterCreationPage({
  guide,
  data,
}: {
  guide: boolean;
  data: VampireData | undefined;
}) {
  const [page, setPage] = useState<number>(0);

  if (!data || !data.clan || data.clan.length === 0) {
    return <div className="text-center text-red-500">No data available {JSON.stringify(data)}</div>;
  }

  const Clan_Select = ({ data }: { data: VampireData }) => {
    const [currentClan, setCurrentClan] = useState<number>(0);
    const [disciplines, setDisciplines] = useState<string[]>([]);

    useEffect(() => {
      if (!data || !data.disciplines || !data.clanDisciplines) {
        setDisciplines([]);
        return;
      }

      const clanDisciplineIDs = data.clanDisciplines
        .filter((clanDiscipline) => clanDiscipline.clanID === currentClan + 1)
        .map((discipline) => discipline.disciplineID);

      const filteredDisciplines = data.disciplines
        .filter((discipline) => clanDisciplineIDs.includes(discipline.ID))
        .map((discipline) => discipline.Name);

      setDisciplines(filteredDisciplines);
    }, [data,]);

    return (
      <div className="grid grid-cols-2 sm:grid-cols-2 md:grid-cols-4 gap-4">
        {data.clan.map((clan, index) => (
          <div
            key={index}
            className="p-4 bg-[var(--color-background-soft)] text-[var(--color-foreground)] border border-[var(--color-border)] rounded-lg shadow-md flex-col sm:flex-row text-center flex items-center justify-between"
          >
            {/* Clan Name */}
            <h3 className="text-base sm:text-xl font-bold mb-2">{clan.Name}</h3>
      
            {/* Clan Symbol */}
            <div className="relative w-12 h-12 sm:w-8 sm:h-8">
              <Image
                src={vtm5_getClanSymbol(clan.Name)}
                alt={`${clan.Name} Symbol`}
                layout="fill"
                objectFit="contain"
                className="clan-symbol"
              />
            </div>
          </div>
        ))}
      </div>
      

    );
  };

  return (
    <div className="flex flex-col items-center justify-center">
      {page === 0 && <Clan_Select data={data} />}
    </div>
  );
}
