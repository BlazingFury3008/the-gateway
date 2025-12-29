
export interface V20Nature {
  id: number;
  name: string;
  desc: string;
}

export interface V20Clan{
    id: number;
    name: string;
    weakness: string;
    information: string;
    reference: string;
}

export interface V20BasicStats {
  name?: string;
  concept?: string;
  nature?: V20Nature | null;
  demeanor?: V20Nature | null;
  clan?: V20Clan | null;
  starting_generation?: number;
}

export interface V20_Character {
  basic_stats?: V20BasicStats;
}

export interface V20_Data {
  nature: V20Nature[];
  clan: V20Clan[];
}