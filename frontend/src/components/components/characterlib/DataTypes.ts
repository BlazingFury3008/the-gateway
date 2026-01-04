// datatypes.ts
// Types that match your current Flask payloads (to_dict / route payloads)

export type ID = number;

// ------------------------------------
// V20: Nature
// GET /v20/nature -> [{ id, name, description }]
// ------------------------------------
export interface V20Nature {
  id: ID;
  name: string;
  description: string;
}

// ------------------------------------
// V20: Disciplines
// GET /v20/discipline -> [{ id, name, description }]
// ------------------------------------
export interface V20Discipline {
  id: ID;
  name: string;
  description: string;
}

// ------------------------------------
// V20: Clans
// GET /v20/clan -> [{ id, name, weakness, information, reference, discipline_1..4 }]
// discipline_1..4 are discipline objects or null
// ------------------------------------
export interface V20Clan {
  id: ID;
  name: string;
  weakness: string;
  information: string;
  reference: string | null;

  discipline_1: V20Discipline | null;
  discipline_2: V20Discipline | null;
  discipline_3: V20Discipline | null;
  discipline_4: V20Discipline | null;
}

// ------------------------------------
// V20: Advantages (Merits / Flaws)
// GET /v20/merit, /v20/flaw, /v20/advantage
// -> [{ id, name, rating, description, clan, reference, category }]
//
// NOTE: rating is stored as JSON w/ MutableList, but your model default is `1`
// so the runtime can be number OR number[] until you normalize it.
// ------------------------------------
export type MeritFlawCategory = "Merit" | "Flaw";
export type V20Rating = number | number[];

export interface V20Advantage {
  id: ID;
  name: string;
  rating: V20Rating;
  description: string;
  clan: string | null;
  reference: string;
  category: MeritFlawCategory;
}

// ------------------------------------
// V20: Backgrounds
// GET /v20/backgrounds
// -> [{ id, name, increments, maximum_value, cost_mult, description }]
// ------------------------------------
export interface V20Background {
  id: ID;
  name: string;
  increments: number;
  maximum_value: number;
  cost_mult: number;
  description: string | null;
}

// ------------------------------------
// V20: Sorcery Paths
// GET /v20/sorcery
// -> [{ id, name, category, reference, powers }]
//
// powers is JSON; structure depends on what you stored.
// Tighten this once you standardize the payload.
// ------------------------------------
export type V20SorceryPower = unknown;

export interface V20SorceryPath {
  id: ID;
  name: string;
  category: string; // magic type name
  reference: string | null;
  powers: V20SorceryPower[];
}

// ------------------------------------
// V20: Magic Types
// GET /v20/m_type -> [{ name }]
// ------------------------------------
export interface V20MagicType {
  name: string;
}

// ------------------------------------
// Character creation / app state types
// ------------------------------------
export interface V20BasicStats {
  name?: string;
  concept?: string;
  nature?: V20Nature | null;
  demeanor?: V20Nature | null;
  clan?: V20Clan | null;
  starting_generation?: number;
}

export interface V20Character {
  basic_stats?: V20BasicStats;
}

// ------------------------------------
// Constants payload you build on the frontend
// ------------------------------------
export interface V20Data {
  nature: V20Nature[];
  clan: V20Clan[];
  merits: V20Advantage[];
  flaws: V20Advantage[];
  backgrounds: V20Background[];
  disciplines: V20Discipline[];
  sorcery_paths: V20SorceryPath[];
  magic_types?: V20MagicType[];
}
