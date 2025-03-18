import React, { useState } from "react";
import { Discipline, DisciplineJunction, DisciplinePower } from "@/data/vtm5_characterCreation";

export default function Disciplines({
    selectedClan,
    disciplineJunction,
    disciplinePowers,
    disciplineGroups,
    selectedDisciplines,
    setSelectedDisciplines
}: {
    selectedClan: number | null;
    disciplineJunction: DisciplineJunction[];
    disciplinePowers: DisciplinePower[];
    disciplineGroups: Discipline[];
    selectedDisciplines: DisciplinePower[];
    setSelectedDisciplines: (data: DisciplinePower[]) => void;
}) {
    const [modalDiscipline, setModalDiscipline] = useState<Discipline | null>(null);

    const clanDisciplines = disciplineJunction
        .filter(junction => junction.clanID === selectedClan)
        .map(junction => junction.disciplineID);

    const availableDisciplines = disciplineGroups.filter(d => clanDisciplines.includes(d.ID));

    return (
        <div className="p-4 max-w-3xl mx-auto space-y-6">
            <h2 className="text-2xl font-bold text-center">Disciplines</h2>
            <div className="grid grid-cols-2 sm:grid-cols-3 gap-4">
                {availableDisciplines.map(discipline => (
                    <button
                        key={discipline.ID}
                        className="btn card w-full"
                        onClick={() => setModalDiscipline(discipline)}
                    >
                        <h3 className="text-lg font-semibold text-center">{discipline.Name}</h3>
                    </button>
                ))}
            </div>
            {modalDiscipline && (
                <DisciplineModal
                    discipline={modalDiscipline}
                    disciplinePowers={disciplinePowers.filter(
                        power => power.DisciplineGroup === modalDiscipline.ID && power.Level <= 3
                    )}
                    selectedDisciplines={selectedDisciplines}
                    setSelectedDisciplines={setSelectedDisciplines}
                    onClose={() => setModalDiscipline(null)}
                />
            )}
        </div>
    );
}

function DisciplineModal({
    discipline,
    disciplinePowers,
    selectedDisciplines,
    setSelectedDisciplines,
    onClose
}: {
    discipline: Discipline;
    disciplinePowers: DisciplinePower[];
    selectedDisciplines: DisciplinePower[];
    setSelectedDisciplines: (data: DisciplinePower[]) => void;
    onClose: () => void;
}) {
    return (
        <div className="fixed inset-0 flex items-center justify-center backdrop-blur-md" onClick={onClose}>
            <div
                className="modal-enter bg-[var(--color-background)] p-6 rounded-lg shadow-lg max-w-lg w-full overflow-hidden flex flex-col"
                onClick={e => e.stopPropagation()}
            >
                <h2 className="text-lg font-bold text-center pb-2 border-b border-[var(--color-border)]">
                    {discipline.Name}
                </h2>
                <div className="mt-4 overflow-y-auto flex-grow no-scrollbar space-y-3 max-h-72">
                    {disciplinePowers.map(power => (
                        <div key={power.ID} className="p-3 rounded-lg bg-[var(--color-background-soft)] hover:bg-[var(--color-background-hover)] flex items-center gap-2">
                            <input
                                type="checkbox"
                                checked={selectedDisciplines.some(d => d.ID === power.ID)}
                                onChange={() => toggleDiscipline(power, selectedDisciplines, setSelectedDisciplines)}
                                disabled={!hasLowerLevel(power, selectedDisciplines)}
                                className="h-4 w-4 text-[var(--color-primary)] cursor-pointer"
                            />
                            <span className="flex-grow text-[var(--color-foreground)]">[{power.Level}] {power.Name}</span>
                        </div>
                    ))}
                </div>
                <button
                    className="btn btn-primary mt-4 w-full border-t border-[var(--color-border)]"
                    onClick={onClose}
                >
                    Close
                </button>
            </div>
        </div>
    );
}

function hasLowerLevel(power: DisciplinePower, selectedDisciplines: DisciplinePower[]) {
    if (power.Level === 1) return true;
    return selectedDisciplines.some(d => d.DisciplineGroup === power.DisciplineGroup && d.Level === power.Level - 1);
}

function toggleDiscipline(
    power: DisciplinePower,
    selectedDisciplines: DisciplinePower[],
    setSelectedDisciplines: (data: DisciplinePower[]) => void
) {
    if (!hasLowerLevel(power, selectedDisciplines)) return;
    setSelectedDisciplines(prev =>
        prev.some(d => d.ID === power.ID)
            ? prev.filter(d => d.ID !== power.ID)
            : [...prev, power]
    );
}