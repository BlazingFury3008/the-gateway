export const characterCreationOptions: { label: string; href: string, exp: number }[] = [
    { label: "Touch Up (+10xp)", href: "&xp_addon=touch-up", exp:10 },
    {
      label: "Established Kindred (+30xp)",
      href: "&xp_addon=established-kindred",
      exp:30
    },
    { label: "Major Player (+50xp)", href: "&xp_addon=major-player", exp:50 },
    { label: "Living Legend (+70xp)", href: "&xp_addon=legend", exp:70 },
  ];

export const optionalRulesSelection:  { label: string; href: string}[] = [
    { label: "Loresheets", href: "loresheet",},
    { label: "Variant Banes", href: "variant-bane",},
    { label: "Ritual Per Level", href: "ritual-level",},
    { label: "Detach Discipline Powers & Level", href: "no-cap",},
    { label: "Remove Pre-Requisite", href: "no-prereq"},
    { label: "Additional Advantages for Flaws", href: "additional-flaw",},
    { label: "In Coterie", href: "in-coterie",},
]

export const character_creation_modes = ["custom", "childe", "neonate", "ancilla"];

export const defaultAttributes = [
  //Physical Attributes
  {attribute:"Strength", value:1},
  {attribute:"Dexterity", value:1},
  {attribute:"Stamina", value:1},

  //Social Attributes
  {attribute:"Charisma", value:1},
  {attribute:"Manipulation", value:1},
  {attribute:"Composure", value:1},

  //Mental Attributes
  {attribute:"Intelligence", value:1},
  {attribute:"Wits", value:1},
  {attribute:"Resolve", value:1},
]

export const defaultSkills =[
  //Physical Skills
  {skill:"Athletics", value:0},
  {skill:"Brawl", value:0},
  {skill:"Craft", value:0},
  {skill:"Drive", value:0},
  {skill:"Firearms", value:0},
  {skill:"Melee", value:0},
  {skill:"Larceny", value:0},
  {skill:"Stealth", value:0},
  {skill:"Survival", value:0},
  
  //Social Skills
  {skill:"Animal Ken", value:0},
  {skill:"Etiquette", value:0},
  {skill:"Insight", value:0},
  {skill:"Intimidation", value:0},
  {skill:"Leadership", value:0},
  {skill:"Performance", value:0},
  {skill:"Persuasion", value:0},
  {skill:"Streetwise", value:0},
  {skill:"Subterfuge", value:0},

  //Mental Skills
  {skill:"Academics", value:0},
  {skill:"Awareness", value:0},
  {skill:"Finance", value:0},
  {skill:"Investigation", value:0},
  {skill:"Medicine", value:0},
  {skill:"Occult", value:0},
  {skill:"Politics", value:0},
  {skill:"Science", value:0},
  {skill:"Technology", value:0},
]

//Data Interfaces
export interface ThinbloodBackground {
  ID: number;
  Name: string;
  Description: string;
  Reference: string;
}

export interface CaitiffBackground {
  ID: number;
  Name: string;
  Values: string;
  Description: string;
}

export interface Clan {
  ID: number;
  Name: string;
  "Clan Bane": string;
  "Variant Bane": string;
  Description: string;
}

export interface Discipline {
  ID: number;
  Name: string;
  Description: string;
}

export interface DisciplineJunction {
  ID: number;
  clanID: number;
  disciplineID: number;
}
