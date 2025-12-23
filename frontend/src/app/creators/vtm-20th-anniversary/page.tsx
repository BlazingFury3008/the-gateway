"use client";
import CharactersLibrary from "@/components/components/characterlib/CharacterLibrary";

export default function Page() {
  return (
    <CharactersLibrary
      title={"Vampire: The Masquerade 20th Anniversary"}
      itemLabel="Characters"
      onCreate={(() => alert("Yes"))}
      items={[{ name: "Aristos", subtitle: "Clan Tremere • 13th Generation", id: "1" }]}
      onViewItem={(() => alert("View"))}
      onEditItem={(() => alert("Edit"))}
      onDeleteItem={(() => alert("Delete"))}
      onCopyItem={(() => alert("Copy"))}
    />
  );
}
