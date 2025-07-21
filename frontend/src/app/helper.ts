export const vtm5_getClanSymbol = (clan: string) => {
    const formattedClan = clan.replace(/\s+/g, "");
    return `/Images/vtm5/clan_logos/${formattedClan}_Symbol.png`;
  };

export const DEFAULT_USER_ICON = "https://cdn-icons-png.flaticon.com/512/149/149071.png"