import { GiClawSlashes, GiFangs, GiTargetArrows } from "react-icons/gi";
import { FaBook, FaTerminal } from "react-icons/fa";

// Define the type for game systems
interface GameSystem {
  title: string;
  description: string;
  icon: React.ReactNode;
  link: string;
  bgColor: string;
  enabled: boolean;
}

export const gameSystems: GameSystem[] = [
  {
    title: "Vampire: The Masquerade 20th Edition",
    description: "Create a character for VTM 20th Anniversary Edition.",
    icon: <GiFangs />,
    link: "/character-creation/vtm20",
    bgColor: "rgba(39, 116, 75, 0.8)",
    enabled: false,
  },
  {
    title: "Werewolf: The Apocalypse 20th Edition",
    description: "Create a character for WTA 20th Anniversary Edition.",
    icon: <GiClawSlashes />,
    link: "/character-creation/wta20",
    bgColor: "rgba(184, 159, 0, 0.8)",
    enabled: false,
  },
  {
    title: "Hunter: The Reckoning 20th Edition",
    description: "Create a character for HTR 20th Anniversary Edition.",
    icon: <GiTargetArrows />,
    link: "/character-creation/htr20",
    bgColor: "rgba(254, 124, 32, 0.8)",
    enabled: false,
  },
  {
    title: "Mage: The Ascension 20th Edition",
    description: "Create a character for MTA 20th Anniversary Edition.",
    icon: <FaBook />,
    link: "/character-creation/mta20",
    bgColor: "rgba(75, 0, 130, 0.8)",
    enabled: false,
  },
  {
    title: "Vampire: The Masquerade 5th Edition",
    description: "Create a character for VTM 5th Edition.",
    icon: <GiFangs />,
    link: "/character-creation/vtm5",
    bgColor: "rgba(130, 0, 0, 0.8)",
    enabled: true,
  },
  {
    title: "Cyberpunk RED",
    description: "Create a character for Cyberpunk RED.",
    icon: <FaTerminal />,
    link: "/character-creation/cyberpunk-red",
    bgColor: "rgba(231, 76, 60, 0.8)",
    enabled: false,

  },
];
