export const vtm5_getClanSymbol = (clan: string) => {
    const formattedClan = clan.replace(/\s+/g, "");
    return `/Images/vtm5/clan_logos/${formattedClan}_Symbol.png`;
  };