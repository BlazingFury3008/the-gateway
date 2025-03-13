-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Mar 13, 2025 at 03:39 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `the-gateway`
--

-- --------------------------------------------------------

--
-- Table structure for table `api_keys`
--

CREATE TABLE `api_keys` (
  `name` varchar(255) NOT NULL,
  `api_key` varchar(255) NOT NULL,
  `is_active` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci COMMENT='API';

--
-- Dumping data for table `api_keys`
--

INSERT INTO `api_keys` (`name`, `api_key`, `is_active`) VALUES
('the-gateway', '3e34e537-9dd2-4a00-8dbb-62ddf3318e87', 1);

-- --------------------------------------------------------

--
-- Table structure for table `characters`
--

CREATE TABLE `characters` (
  `uuid` varchar(255) NOT NULL,
  `game` enum('vtm_5','vtm_20','cyber_red') NOT NULL,
  `data` longtext NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `uuid` varchar(255) NOT NULL,
  `email` text NOT NULL,
  `username` varchar(255) NOT NULL,
  `hashed_password` varchar(255) NOT NULL,
  `auth_level` int(11) NOT NULL DEFAULT 1,
  `config` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci COMMENT='User';

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`uuid`, `email`, `username`, `hashed_password`, `auth_level`, `config`) VALUES
('03eea24b-f0dd-40e8-bf57-93a7aba76640', 'ataylor3008@gmail.com', 'Blazin3008', '$2b$12$ZynFIHQ/wODZ9aI/EPjfy.ED9W1HrsS0gOrt5PQTAnAAfCNTyGHja', 6, '[\r\n  {\r\n    \"id\": \"vtm_v5\",\r\n    \"options\": {\r\n      \"Loresheets\": {\r\n        \"type\": \"boolean\",\r\n        \"value\": false\r\n      },\r\n      \"Variant Banes\": {\r\n        \"type\": \"boolean\",\r\n        \"value\": false\r\n      },\r\n      \"Ritual Per Level\": {\r\n        \"type\": \"boolean\",\r\n        \"value\": false\r\n      },\r\n      \"Detach Discipline Powers & Level\": {\r\n        \"type\": \"boolean\",\r\n        \"value\": false\r\n      },\r\n      \"Remove Pre-Requisite\": {\r\n        \"type\": \"boolean\",\r\n        \"value\": false\r\n      },\r\n      \"Additional Advantages for Flaws\": {\r\n        \"type\": \"boolean\",\r\n        \"value\": false\r\n      },\r\n      \"In Coterie\": {\r\n        \"type\": \"boolean\",\r\n        \"value\": false\r\n      }\r\n    }\r\n  }\r\n]');

-- --------------------------------------------------------

--
-- Table structure for table `vtm5_caitiffflaws`
--

CREATE TABLE `vtm5_caitiffflaws` (
  `ID` int(2) NOT NULL,
  `Name` tinytext DEFAULT NULL,
  `Values` tinytext DEFAULT NULL,
  `Limits` int(2) DEFAULT NULL,
  `Description` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Dumping data for table `vtm5_caitiffflaws`
--

INSERT INTO `vtm5_caitiffflaws` (`ID`, `Name`, `Values`, `Limits`, `Description`) VALUES
(1, 'Befouling Vitae', '2', 1, ''),
(2, 'Clan Curse', '2', 1, ''),
(3, 'Debt Peon', '2', 1, ''),
(4, 'Liquidator', '1', 1, ''),
(5, 'Muddled Blood', '1', 1, ''),
(6, 'Walking Omen', '2', 1, ''),
(7, 'Word-Scarred', '1', 1, '');

-- --------------------------------------------------------

--
-- Table structure for table `vtm5_caitiffmerits`
--

CREATE TABLE `vtm5_caitiffmerits` (
  `ID` int(11) NOT NULL,
  `Name` tinytext DEFAULT NULL,
  `Values` tinytext DEFAULT NULL,
  `Limits` int(2) DEFAULT NULL,
  `Description` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Dumping data for table `vtm5_caitiffmerits`
--

INSERT INTO `vtm5_caitiffmerits` (`ID`, `Name`, `Values`, `Limits`, `Description`) VALUES
(1, 'Favoured Blood', '4', 1, ''),
(2, 'Mark of Caine', '2', 1, ''),
(3, 'Mockingbird', '3', 1, ''),
(4, 'Sun-Scarred', '5', 1, ''),
(5, 'Uncle Fangs', '3', 1, '');

-- --------------------------------------------------------

--
-- Table structure for table `vtm5_clan`
--

CREATE TABLE `vtm5_clan` (
  `ID` int(2) NOT NULL,
  `Name` tinytext DEFAULT NULL,
  `Reference` tinytext DEFAULT NULL,
  `Clan Bane` text NOT NULL,
  `Variant Bane` text NOT NULL,
  `Description` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Dumping data for table `vtm5_clan`
--

INSERT INTO `vtm5_clan` (`ID`, `Name`, `Reference`, `Clan Bane`, `Variant Bane`, `Description`) VALUES
(1, 'Banu Haqim', 'VtM Player\'s Guide; PG 17', 'Blood Addiction:\nWhen the Banu Haqim slakes at least one Hunger level from another vampire, they must make a Hunger Frenzy test at difficulty (2 + {Bane Severity}). If they fail, they must gorge themselves on vitae, in turn opening the door to possible Diablerie', 'Noxious Blood: The Blood of the Banu Haqim is toxic to mortals, but not to other vampires. Due to this mortals receive ({Bane Severity}) Aggravated Damage for each Rouse Check’s worth of Blood consumed. Their Blood cannot be used to heal mortal injuries. In amounts below the amount needed to Blood Bond, it does not harm them, even if directly injected into them.', 'The Children of Haqim, have joined the Camarilla recently after major internal schisms after one of their Eldest awoke from Torpor and began major shifts to the Clan’s internal structure. Being the Sorcerers and Warriors they were, and still are, many Domains see much use for their particular skills - Especially with the recent fall of Vienna, further weakening the Tremere’s power and influence.'),
(2, 'Brujah', 'VtM Corebook; PG 65', 'Violent Temper:\nA rage is simmering in the back of the mind with a Brujah with the slightest provocation able to send them into a frenzied rage. Subtract ({Bane Severity}) dice against Tests for Fury Frenzy. ', 'Violence: When a messy critical occurs as the result of any Skill test outside of combat, a Brujah vampire causes ({Bane Severity}) damage to the subject of their interaction, in addition to any other result of the Hunger dice. The type of damage is dependent on the situation either physical or mental. The damage is Aggravated unless the player spends a point of Willpower to turn it into Superficial', 'Following the Conclave of 2012, many Brujah left the Camarilla with former Archon Theo Bell. In Glasgow, they make up most of the Anarch Movement. While some Brujah stayed in the Camarilla, they are a minority in the Modern Nights. They are rebels and radicals, usually always pushing for “Improvement”, though what that exactly is is up for debate.'),
(3, 'Gangrel', 'VtM Corebook; PG 69', 'Bestial Features:\nIn Frenzy, Gangrel gains ({Bane Severity}) animalistic features. These features last for one more night afterward, each feature reducing one Attribute by 1 point. The Gangrel may choose to Ride the Wave in order to only have one feature manifest and only lose one Attribute point. ', 'Survival Instincts: Subtract ({Bane Severity}) dice in any roll to resist fear Frenzy. The pool cannot be below one die.', 'No one is quite sure why the Gangrel left the Camarilla, but almost the entire Clan did. Very few Gangrel remain within the Camarilla, but those that do are usually doing so out of loyalty, debt or blood bond. Often being closer to their Beast than other Clans, they are often called the apex predators of Kindred society, as no other Clan can match their ability to endure and survive in any environment.'),
(4, 'Hecata', 'VtM Player\'s Guide; PG 22', 'Painful Kiss:\nHecata may only take harmful drinks from mortals which result in blood loss. Unwilling mortals that are able to escape will make the attempt, even those who are convinced or willing must succeed in a Stamina + Resolve test against Difficulty (2 + {Bane Severity}) in order to not recoil. Vampires who are willingly bit must make a Frenzy test against Difficulty 3 to avoid terror Frenzy. ', 'Decay: Hecata suffer ({Bane Severity}) additional dots in Flaws equal to spread as they see fit across Retainer, Haven, and Resources Flaws. These Flaws can either be taken at Character Creation or removed by paying twice the amount of Background dots. Additionally, any purchase of dots in these Advantages costs an ({Bane Severity}) amount of extra experience points. ', 'The most prominent Bloodline of the Hecata in the UK is the Dunsirn, due to them being the splinter family of the Giovanni based in Scotland, though non-Dunsirns aren’t unheard of. Though, with them being one of the last true Independents, the recent fall of both the Camarilla within Glasgow and rumoured end to the Promise of 1528, many more have turned their attention to the Domain as a potential powerbase.'),
(5, 'Lasombra', 'VtM Player\'s Guide; PG 27', 'Distorted Image:\nIn reflections or recordings (live or not) the Lasombra appear to be distorted, those who know what vampires are know precisely what\'s going on, while others might be confused but know something is wrong. This does not however, hide their identity with any certainty and they are not likely to be caught more often on surveillance than any other Kindred. In addition to this, modern technology which includes making a phone call requires a Technology test at Difficulty (2 + {Bane Severity}) as microphones struggle with them as much as cameras. Avoiding any electronic vampire detection system is also done with a ({Bane Severity}) dice penalty. ', 'Callousness: Whenever making a Remorse test remove ({Bane Severity}) dice. The dice pool cannot be reduced below 1. ', 'Within recent nights, the main body of Clan Lasombra has made their way into the Camarilla, even if many Princes have hefty prices for their admittance into their Domains (Most commonly being the life of an Elder for the admittance of a member). Glasgow’s previous Prince didn’t hold such views, though the suspicions of them being backstabbers and traitors greedy for power are hard to assuage.'),
(6, 'Malkavian', 'VtM Corebook; PG 75', 'Fractured Perspective:\nWhen suffering a Bestial Failure or a Compulsion, their mental derangement comes to the forefront. Suffers a ({Bane Severity}) dice penalty equal to one category of dice pools (Physical, Social or Mental) for the entire scene. The penalty and nature of the affliction are decided between the player and Storyteller during character creation. ', 'Unnatural Manifestations: Using Discipline powers within close proximity of mortals scares them and any social interactions other than Intimidation suffer a ({Bane Severity}) dice penalty. This is not Masquerade-breaking, but the dislike remains for the duration of one scene. Other vampires subject to this recognize the Malkavian as a vampire but suffer no penalty.', 'Clan Malkavian has enjoyed membership in the Camarilla since its founding, though the opinions of the other Clans about them has drastically changed over time. These nights, they are regarded as a Clan of maniacs and madmen and seers and prophets who are often given a wide berth, either to avoid their delusion or keep secrets as far from their ‘eyes’ as possible.'),
(7, 'The Ministry', 'VtM Player\'s Guide; PG 33', 'Abhors the Light:\nWhen a Minister is exposed to direct illumination, be it naturally caused or artificial, they receive a ({Bane Severity}) dice penalty equal  to all dice pools while subject to the light. They also add ({Bane Severity}) to Aggravated damage taken from sunlight. ', 'Cold-Blooded: They can only use Blush of Life if they have recently fed from a living vessel in the same scene or up to roughly an hour ago, Storytellers discretion. When they do so, it requires ({Bane Severity}) Rouse Checks  rather than just one.', 'The Vipers were the first to see the seeds of the end, and when they did, they realised that independence may have killed them. At the same time the Banu Haqim sought admittance to the Camarilla, so too did the Followers of Set, however they were rejected as their past misdeeds held too harsh a stain upon their name. Instead, they changed their name to The Ministry and many joined the Anarchs, plying their trade and influence in the dirtier parts of Kindred and Kine society.'),
(8, 'Nosferatu', 'VtM Corebook; PG 81', 'Repulsiveness: Cursed by their blood, when they are Embraced they are twisted into revolting monsters. They can never raise their rating in the Looks merits and instead must take the Repulsive flaw. Any attempt to disguise themselves incurs a ({Bane Severity}) dice penalty equal. This also includes the use of Disciplines such as Mask of a Thousand Faces. However, most Nosferatu do not breach the Masquerade by being seen, they are instead perceived as gross or terrifying. ', 'Infestation: The Haven of a Nosferatu is always infested with vermin, any attempt to do something that requires concentration takes a (2 + {Bane Severity}) dice penalty, as well as the same penalty to social tests at ST discretion. Additionally, when a Nosferatu spends a scene at an enclosed location, the vermin appears and causes the same penalty though reduced to ({Bane Severity}). Any attempt to control these vermin with Animalism is done at a ({Bane Severity}) dice penalty. ', 'The Nosferatu are a Clan of secrets and spies. With a hunger for secrets, they have garnered a reputation as reliable information gatherers, but one should always be wary in dealings with them; The phrase “Always assume there are 3 Nosferatu in the room” tends to hold some water.'),
(9, 'Ravnos', 'VtM Player\'s Guide; PG 39', 'Doomed: Anytime they daysleep within the same place more than once in seven nights, roll ({Bane Severity}) dice. If they receive any 10\'s they then take 1 Aggravated damage for each as they are scorched from within. What constitutes as the same place is defined by the chronicle, but generally will need a mile distance between the two resting places before the bane is triggered. Mobile havens do work as long as the haven is moved a mile away. Due to this, the Ravnos may not take the No Haven Flaw. ', 'Unbirth Name: If a Ravnos’ unbirth name is used against them, the name-wielding opponent receives a ({Bane Severity}) dice bonus to resist their Discipline powers. Additionally, the Ravnos affected receives the same penalty to resist supernatural powers used by the opponent ', 'Since the Week of Nightmares and their new need to remain nomadic, the Ravnos are likewise, a rare Clan to see, however not nearly as exotic as the childer of Saulot. Many of the Clan have attempted their best to rebuild the Clan and their numbers while maintaining roaming caravans  and acting as messengers and information brokers.'),
(10, 'Salubri', 'VtM Player\'s Guide; PG 45', 'Hunted:\nTheir vitae has a unique trait where when another clan partakes in their Blood they find it difficult to pull away. Once a non-Salubri has consumed at least one Hunger level worth, they must make a Hunger Frenzy test at difficulty (2 + {Bane Severity}), (3 + {Bane Severity}) for Banu Haqim. If they fail, they will continue to consume the Salubri until pried off. Additionally, each Salubri has a third eye and while it\'s not always human-like it\'s always present and cannot be obscured by supernatural powers. In addition to this, whenever they activate a Discipline, the eye weeps vitae with its intensity correlating to the level of the Discipline used. The Blood flowing from the eye can trigger a Hunger Frenzy test from nearby vampires with Hunger 4 or more. ', 'Asceticism: Whenever their Hunger is below three, the Salubri suffer a ({Bane Severity}) dice penalty equal to any Discipline dice pools. The bleeding third eye still remains.', 'Rumoured to be a myth, not much is known of them. In play, this Clan will be heavily limited in numbers.'),
(11, 'Toreador', 'VtM Corebook; PG 87', 'Aesthetic Fixation:\nA desire for beauty takes control over the Toreador and when in lesser surroundings they suffer. When they are within settings they find less than beautiful, they take a ({Bane Severity}) dice penalty equal when using Disciplines. ', 'Agonizing Empathy: Whenever their feeding causes Aggravated damage to a mortal, the vampire suffers the same damage in return but cannot receive more than ({Bane Severity}). This damage is generally Aggravated. The damage itself is reflected as vivid bruising wherever they bit their victim as internal bleeding takes place.', 'The Toreador are known throughout the world as artists and experts on what it means to be part of Humanity. They keep Elysia and the various sects up to date on the mores and customs of human society. Socialites that they are, they also tend to enjoy spreading gossip and news among their networks and cities.'),
(12, 'Tremere', 'VtM Corebook; PG 93', 'Deficient Blood:\nBefore the fall of Vienna, they were defined by their rigid hierarchy of Blood Bonds within the Pyramid. After the fall, their Blood weakened and rejected all prior connections. Tremere are unable to Blood Bond other Kindred, though they can still be Bound by other clans. Tremere can still Blood Bond mortals to do their bidding, but the vitae must be drunk an additional ({Bane Severity}) times', 'Stolen Blood: When performing a Blood Surge they need to make ({Bane Severity}) Rouse Checks. If these Rouse Checks increase their Hunger to 5 or higher, they can choose whether to back off their Blood Surge or perform it to then hit Hunger 5 afterward immediately.', 'The Tremere were a powerhouse of a Clan, backed up by a rigid hierarchy and advanced blood magic. Until 2008, when their headquarters in Vienna was destroyed by Second Inquisition agents. They are now split into several ‘Houses’, each with their own agendas and goals but all, ultimately, wanting to bring the Tremere back into a position of power and prominence.'),
(13, 'Tzimisce', 'VtM Player\'s Guide; PG 51', 'Grounded:\nEach Tzimisce must select a specific charge, be it a physical location, a group of people, or something even more esoteric. Each night they must sleep surrounded by their charge, if they do not, they sustain ({Bane Severity}) aggravated Willpower damage upon waking the following night. ', 'Cursed Courtesy: If they wish to enter a place of residence uninvited they must spend ({Bane Severity}) Willpower, this penalty also applies to their Discipline pools while they are there. The invitation inside can only be made by someone who lives there and this does not occur in uninhabited homes or public places. Tzimisce with this Bane cannot take the uninvited Folkloric Block.[3] ', 'While most Tzimisce joined the Sabbat, several stayed Independent or paid lip service to the Camarilla. Most Scottish Dragons live further up in the Highlands, where their castles and havens can be hidden and protected by vast wilderness and loyal ghouls, however some younger Dragons made their way to the cities to fight for their own share of the spoils of modernity, often putting them in direct competition with the Ventrue and Lasombra.'),
(14, 'Ventrue', 'VtM Corebook; PG 99', 'Rarefied Tastes:\nWhen the Ventrue drinks the blood of a mortal who does not fall within their preference, they must spend ({Bane Severity})  Willpower else they will vomit the blood from their bodies unable to slake their hunger. Their preferences range within the clan, some looking for descendants of a certain nationality to soldiers suffering from PTSD. With a Resolve + Awareness test, they can sense if a mortal they seek to feed from fits within their preference. At character creation, their preference should be selected', 'Hierarchy: The Ventrue suffer a ({Bane Severity}) penalty to their Discipline dice pools when using them against a vampire of a lower generation. They must also spend ({Bane Severity}) Willpower if they wish to directly attack other vampires of a lower generation.', 'The Ventrue, another of the founding Camarilla Clans, see themselves as the only Clan fit to lead any sect to greatness. Some call it arrogance, they call it confidence. Tracing their lineages all the way to the Founder of the Clan, they take great pride in each member of their Clan being great from the moment of Embrace, as is fitting for a Clan of Kings.'),
(15, 'Caitiff', 'VtM Corebook; PG 105', 'Outcast:\nUntouched by their ancestors, the Caitiff do not share a common Bane. The character begins with the Flaw Suspect and they may not purchase positive status during Character Creation. The Storyteller may impose a 1-2 dice penalty to social tests against Kindred who know they are Caitiff. To improve a Discipline, the cost is 6 times the level of experience points. ', '', 'The Clanless are split into two main branches - The Caitiff and The Thinblooded. Caitiffs are Kindred who, for whatever reason, have not manifested the traits of a Clan, and are thus often ostracised.'),
(16, 'Thinblood', 'VtM Corebook; PG 109', 'Uncursed:\nThin-bloods do not suffer from a Bane unless the thin-blood Flaw Clan Curse is taken. ', '', 'The Clanless are split into two main branches - The Caitiff and The Thinblooded. Thinblooded are Kindred whose Blood is so diluted, they also do not manifest traits typical of other Kindred, though they have other unique traits, such as being able to walk in sunlight or appearing more like a Mortal.');

-- --------------------------------------------------------

--
-- Table structure for table `vtm5_clandisciplinejunction`
--

CREATE TABLE `vtm5_clandisciplinejunction` (
  `ID` int(11) NOT NULL,
  `clanID` int(2) DEFAULT NULL,
  `disciplineID` int(2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Dumping data for table `vtm5_clandisciplinejunction`
--

INSERT INTO `vtm5_clandisciplinejunction` (`ID`, `clanID`, `disciplineID`) VALUES
(1, 1, 6),
(2, 1, 11),
(3, 1, 3),
(4, 2, 8),
(5, 2, 3),
(6, 2, 7),
(7, 3, 1),
(8, 3, 5),
(9, 3, 9),
(10, 4, 2),
(11, 4, 5),
(12, 4, 10),
(13, 5, 4),
(14, 5, 10),
(15, 5, 7),
(16, 6, 4),
(17, 6, 2),
(18, 6, 6),
(19, 8, 1),
(20, 8, 6),
(21, 8, 7),
(22, 9, 1),
(23, 9, 6),
(24, 9, 8),
(25, 10, 5),
(26, 10, 2),
(27, 10, 4),
(28, 7, 9),
(29, 7, 6),
(30, 7, 8),
(31, 11, 8),
(32, 11, 3),
(33, 11, 2),
(34, 12, 4),
(35, 12, 2),
(36, 12, 11),
(37, 13, 4),
(38, 13, 1),
(39, 13, 9),
(40, 14, 4),
(41, 14, 8),
(42, 14, 5),
(43, 15, 1),
(44, 15, 2),
(45, 15, 3),
(46, 15, 4),
(47, 15, 5),
(48, 15, 6),
(49, 15, 7),
(50, 15, 8),
(51, 15, 9),
(52, 15, 10),
(53, 15, 11),
(54, 16, 12);

-- --------------------------------------------------------

--
-- Table structure for table `vtm5_disciplinegroups`
--

CREATE TABLE `vtm5_disciplinegroups` (
  `ID` int(2) NOT NULL,
  `Name` varchar(18) DEFAULT NULL,
  `Reference` varchar(25) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Dumping data for table `vtm5_disciplinegroups`
--

INSERT INTO `vtm5_disciplinegroups` (`ID`, `Name`, `Reference`) VALUES
(1, 'Animalism', 'VtM Corebook; PG 244'),
(2, 'Auspex', 'VtM Corebook; PG 248'),
(3, 'Celerity', 'VtM Corebook; PG 252'),
(4, 'Dominate', 'VtM Corebook; PG 254'),
(5, 'Fortitude', 'VtM Corebook; PG 258'),
(6, 'Obfuscate', 'VtM Corebook; PG 260'),
(7, 'Potence', 'VtM Corebook; PG 263'),
(8, 'Presence', 'VtM Corebook; PG 266'),
(9, 'Protean', 'VtM Corebook; PG 269'),
(10, 'Oblivion', 'VtM Player\'s Guide; PG 84'),
(11, 'Blood Sorcery', 'VtM Corebook; PG 271'),
(12, 'Thin-blood Alchemy', 'VtM Corebook; PG 282');

-- --------------------------------------------------------

--
-- Table structure for table `vtm5_disciplinepowers`
--

CREATE TABLE `vtm5_disciplinepowers` (
  `ID` int(3) NOT NULL,
  `Name` tinytext DEFAULT NULL,
  `Description` text NOT NULL,
  `Reference` tinytext DEFAULT NULL,
  `Level` int(1) DEFAULT 1,
  `Prerequisite` tinytext DEFAULT NULL,
  `DisciplineGroup` int(2) DEFAULT 1
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Dumping data for table `vtm5_disciplinepowers`
--

INSERT INTO `vtm5_disciplinepowers` (`ID`, `Name`, `Description`, `Reference`, `Level`, `Prerequisite`, `DisciplineGroup`) VALUES
(1, 'Bond Famulus', '', 'VtM Corebook; PG245', 1, '', 1),
(2, 'Sense the Beast', '', 'V5 245', 1, '', 1),
(3, 'Animal Messenger', '', 'PG 69', 2, 'Auspex 1', 1),
(4, 'Atavism', '', 'Teeth 3', 2, '', 1),
(5, 'Feral Whispers', '', 'V5 246', 2, '', 1),
(6, 'Animal Succulence', '', 'V5 246', 3, '', 1),
(7, 'Messenger\'s Command', '', 'PG 69', 3, 'Dominate 1, Animal Messenger, Compel or Mesmerize', 1),
(8, 'Scent of Prey', '', 'Sabbat 47', 3, '', 1),
(9, 'Plague of Beasts', '', 'PG 69', 3, '', 1),
(10, 'Quell the Beast', '', 'V5 246', 3, '', 1),
(11, 'Unliving Hive', '', 'V5 246', 3, 'Obfuscate 2', 1),
(12, 'Subsume the Spirit', '', 'V5 247', 4, '', 1),
(13, 'Sway the Flock', '', 'PG 69', 4, '', 1),
(14, 'Animal Dominion', '', 'V5 247', 5, '', 1),
(15, 'Coax the Bestial Temper', '', 'PG 70', 5, '', 1),
(16, 'Drawing Out the Beast', '', 'V5 247', 5, '', 1),
(17, 'Heightened Senses', '', 'V5 249', 1, '', 2),
(18, 'Sense the Unseen', '', 'V5 249', 1, '', 2),
(19, 'Panacea', '', 'Comp 24, PG 70', 2, 'Fortitude 1', 2),
(20, 'Premonition', '', 'V5 249', 2, '', 2),
(21, 'Reveal Temperament', '', 'PG 70', 2, '', 2),
(22, 'Unerring Pursuit', '', 'Sabbat 46', 2, 'Dominate 1', 2),
(23, 'Eyes of Beasts', '', 'FoL 148', 3, 'Animalism 2', 2),
(24, 'Fatal Flaw', '', 'PG 71', 3, 'Oblivion 1', 2),
(25, 'Scry the Soul', '', 'V5 250', 3, '', 2),
(26, 'Share the Senses', '', 'V5 250', 3, '', 2),
(27, 'Spirit\'s Touch', '', 'V5 250', 4, '', 2),
(28, 'Clairvoyance', '', 'V5 251', 5, '', 2),
(29, 'Possession', '', 'V5 251', 5, 'Dominate 3', 2),
(30, 'Telepathy', '', 'V5 252', 5, '', 2),
(31, 'Unburdening the Bestial Soul', '', 'Comp 24, PG 71', 5, 'Dominate 3, Panacea', 2),
(32, 'Cat\'s Grace', '', 'V5 252', 1, '', 3),
(33, 'Rapid Reflexes', '', 'V5 253', 1, '', 3),
(34, 'Fleetness', '', 'V5 253', 2, '', 3),
(35, 'Rush Job', '', 'PG 72', 2, '', 3),
(36, 'Blink', '', 'V5 253', 3, '', 3),
(37, 'Traversal', '', 'V5 253', 3, '', 3),
(38, 'Weaving', '', 'PG 72', 3, 'Rapid Reflexes', 3),
(39, 'Blurred Momentum', '', 'PG 72', 4, '', 3),
(40, 'Draught of Elegance', '', 'V5 254', 4, '', 3),
(41, 'Unerring Aim', '', 'V5 254', 4, 'Auspex 2', 3),
(42, 'Unseen Strike', '', 'PG 73', 4, 'Obfuscate 4, Blink', 3),
(43, 'Lightning Strike', '', 'V5 254', 5, '', 3),
(44, 'Split Second', '', 'V5 254', 5, '', 3),
(45, 'Cloud Memory', '', 'V5 255', 1, '', 4),
(46, 'Compel', '', 'V5 255', 1, '', 4),
(47, 'Slavish Devotion', '', 'Cults 104, PG 73', 1, 'Fortitude 1', 4),
(48, 'Mesmerize', '', 'V5 255', 2, '', 4),
(49, 'Dementation', '', 'V5 255', 2, 'Obfuscate 2', 4),
(50, 'Domitor\'s Favor', '', 'Comp 25, PG 74', 2, '', 4),
(51, 'The Forgetful Mind', '', 'V5 257', 3, '', 4),
(52, 'Submerged Directive', '', 'V5 257', 3, 'Mesmerize', 4),
(53, 'Ancestral Dominion', '', 'Cults 104, PG 74', 4, 'Blood Sorcery 3, Mesmerize', 4),
(54, 'Implant Suggestion', '', 'PG 74', 4, 'Presence 1', 4),
(55, 'Rationalize', '', 'V5 257', 4, '', 4),
(56, 'Tabula Rasa', '', 'Sabbat 47', 4, '', 4),
(57, 'Mass Manipulation', '', 'V5 257', 5, '', 4),
(58, 'Terminal Decree', '', 'V5 257', 5, '', 4),
(59, 'Resilience', '', 'V5 258', 1, '', 5),
(60, 'Unswayable Mind', '', 'V5 258', 1, '', 5),
(61, 'Earth\'s Perseverance', '', 'PG 75', 2, '', 5),
(62, 'Enduring Beasts', '', 'V5 259', 2, 'Animalism 1', 5),
(63, 'Obdurate', '', 'Teeth 3', 2, 'Potence 2', 5),
(64, 'Invigorating Vitae', '', 'PG 75', 2, 'Auspex 1', 5),
(65, 'Toughness', '', 'V5 258', 2, '', 5),
(66, 'Defy Bane', '', 'V5 259', 3, '', 5),
(67, 'Fortify the Inner Façade', '', 'V5 259', 3, '', 5),
(68, 'Seal the Beast\'s Maw', '', 'FR 44', 3, '', 5),
(69, 'Valeren', '', 'Comp 25, PG 75', 3, 'Auspex 1', 5),
(70, 'Gorgon\'s Scales', '', 'PG 75', 4, '', 5),
(71, 'Draught of Endurance', '', 'V5 259', 4, '', 5),
(72, 'Shatter', '', 'Cults 104', 4, 'Toughness', 5),
(73, 'Flesh of Marble', '', 'V5 259', 5, '', 5),
(74, 'Prowess from Pain', '', 'V5 260', 5, '', 5),
(75, 'Cloak of Shadows', '', 'V5 261', 1, '', 6),
(76, 'Silence of Death', '', 'V5 261', 1, '', 6),
(77, 'Chimerstry', '', 'Comp 25, PG 76', 2, 'Presence 1', 6),
(78, 'Ghost\'s Passing', '', 'FR 18', 2, 'Animalism 1', 6),
(79, 'Unseen Passage', '', 'V5 261', 2, '', 6),
(80, 'Ventriloquism', '', 'FoL 148', 2, 'Auspex 2', 6),
(81, 'Fata Morgana', '', 'Comp 26, PG 77', 3, 'Presence 2', 6),
(82, 'Ghost in the Machine', '', 'V5 262', 3, '', 6),
(83, 'Mask of a Thousand Faces', '', 'V5 262', 3, '', 6),
(84, 'Mask of Isolation', '', 'Sabbat 48', 3, 'Dominate 1, Mask of a Thousand Faces', 6),
(85, 'Mental Maze', '', 'Cults 85, PG 77', 3, 'Dominate 1', 6),
(86, 'Mind Masque', '', 'PG 78', 3, 'Dominate 2', 6),
(87, 'Conceal', '', 'V5 262', 4, 'Auspex 3', 6),
(88, 'Vanish', '', 'V5 262', 4, 'Cloak of Shadows', 6),
(89, 'Cloak the Gathering', '', 'V5 263', 5, '', 6),
(90, 'Imposter\'s Guise', '', 'V5 263', 5, 'Mask of a Thousand Faces', 6),
(91, 'Ashes to Ashes', '', 'Cults 204, PG 85', 1, '', 10),
(92, 'Binding Fetter', '', 'Cults 204, PG 85', 1, '', 10),
(93, 'Shadow Cloak', '', 'Chicago 293, PG 85', 1, '', 10),
(94, 'Oblivion\'s Sight', '', 'Chicago 293, PG 85', 1, '', 10),
(95, 'Arms of Ahriman', '', 'Chicago 294, PG 86', 2, 'Potence 2', 10),
(96, 'Fatal Prediction', '', 'Cults 204, PG 87', 2, 'Auspex 2', 10),
(97, 'Shadow Cast', '', 'Chicago 293, PG 87', 2, '', 10),
(98, 'Where the Veil Thins', '', 'Cults 205, PG 87', 2, '', 10),
(99, 'Aura of Decay', '', 'Cults 205, PG 88', 3, '', 10),
(100, 'Passion Feast', '', 'Cults 206, PG 88', 3, 'Fortitude 2', 10),
(101, 'Shadow Perspective', '', 'Chicago 294, PG 89', 3, '', 10),
(102, 'Touch of Oblivion', '', 'Chicago 294, PG 89', 3, '', 10),
(103, 'Necrotic Plague', '', 'Cults 206, PG 89', 4, '', 10),
(104, 'Stygian Shroud', '', 'Chicago 295, PG 90', 4, '', 10),
(105, 'Umbrous Clutch', '', 'Sabbat 49', 4, '', 10),
(106, 'Shadow Step', '', 'Chicago 295, PG 90', 5, '', 10),
(107, 'Skuld Fulfilled', '', 'Cults 207, PG 91', 5, '', 10),
(108, 'Tenebrous Avatar', '', 'Chicago 295, PG 91', 5, '', 10),
(109, 'Withering Spirit', '', 'Cults 208', 5, '', 10),
(110, 'Lethal Body', '', 'V5 264', 1, '', 7),
(111, 'Soaring Leap', '', 'V5 264', 1, '', 7),
(112, 'Prowess', '', 'V5 264', 2, '', 7),
(113, 'Relentless Grasp', '', 'PG 79', 2, '', 7),
(114, 'Brutal Feed', '', 'V5 264', 3, '', 7),
(115, 'Spark of Rage', '', 'V5 265', 3, 'Presence 3', 7),
(116, 'Uncanny Grip', '', 'V5 265', 3, '', 7),
(117, 'Wrecker', '', 'PG 79', 3, 'Prowess', 7),
(118, 'Crash Down', '', 'PG 79', 4, 'Soaring Leap', 7),
(119, 'Draught of Might', '', 'V5 265', 4, '', 7),
(120, 'Earthshock', '', 'V5 265', 5, '', 7),
(121, 'Fist of Caine', '', 'V5 266', 5, '', 7),
(122, 'Subtle Hammer', '', 'PG 79', 5, '', 7),
(123, 'Awe', '', 'V5 267', 1, '', 8),
(124, 'Daunt', '', 'V5 267', 1, '', 8),
(125, 'Eyes of the Serpent', '', 'Anarch 185, PG 80', 1, 'Protean 1', 8),
(126, 'Lingering Kiss', '', 'V5 267', 2, '', 8),
(127, 'Melpominee', '', 'PG 80', 2, '', 8),
(128, 'Clear the Field', '', 'FoL 177', 3, 'Dominate 3', 8),
(129, 'Dread Gaze', '', 'V5 267', 3, '', 8),
(130, 'Entrancement', '', 'V5 268', 3, '', 8),
(131, 'Thrown Voice', '', 'PG 80', 3, 'Auspex 1', 8),
(132, 'True Love\'s Face', '', 'Cults 85', 3, 'Obfuscate 3', 8),
(133, 'Irresistable Voice', '', 'V5 268', 4, 'Dominate 1', 8),
(134, 'Magnum Opus', '', 'Teeth 3', 4, 'Auspex 3', 8),
(135, 'Suffuse the Edifice', '', 'PG 80', 4, '', 8),
(136, 'Summon', '', 'V5 268', 4, '', 8),
(137, 'Majesty', '', 'V5 268', 5, '', 8),
(138, 'Star Magnetism', '', 'V5 269', 5, '', 8),
(139, 'Eyes of the Beast', '', 'V5 269', 1, '', 9),
(140, 'Weight of the Feather', '', 'V5 269', 1, '', 9),
(141, 'Feral Weapons', '', 'V5 270', 2, '', 9),
(142, 'Vicissitude', '', 'Comp 27, PG 81', 2, 'Dominate 2', 9),
(143, 'Earth Meld', '', 'V5 270', 3, '', 9),
(144, 'Fleshcrafting', '', 'Comp 27, PG 82', 3, 'Dominate 2, Vicissitude', 9),
(145, 'Shapechange', '', 'V5 270', 3, '', 9),
(146, 'Visceral Absorption', '', 'Sabbat 49', 3, 'Blood Sorcery 2', 9),
(147, 'Horrid Form', '', 'Comp 28, PG 83', 4, 'Dominate 2, Vicissitude', 9),
(148, 'Metamorphosis', '', 'V5 271', 4, 'Shapechange', 9),
(149, 'Heart of Darkness', '', 'Cults 85', 5, 'Fortitude 2', 9),
(150, 'Mist Form', '', 'V5 271', 5, '', 9),
(151, 'One with the Land', '', 'Comp 28, PG 83', 5, 'Animalism 2, Earth Meld', 9),
(152, 'The Unfettered Heart', '', 'V5 271', 5, '', 9),
(153, 'Corrosive Vitae', '', 'V5 272', 1, '', 11),
(154, 'Shape the Sanguine Sacrament', '', 'Teeth 3', 1, '', 11),
(155, 'A Taste for Blood', '', 'V5 272', 1, '', 11),
(156, 'Extinguish Vitae', '', 'V5 273', 2, '', 11),
(157, 'Scour Secrets', '', 'PG 98', 2, '', 11),
(158, 'Blood of Potency', '', 'V5 273', 3, '', 11),
(159, 'Scorpion\'s Touch', '', 'V5 273', 3, '', 11),
(160, 'Transitive Bond', '', 'Sabbat 49', 3, '', 11),
(161, 'Blood Aegis', '', 'PG 98', 4, '', 11),
(162, 'Theft of Vitae', '', 'V5 274', 4, '', 11),
(163, 'Baal\'s Caress', '', 'V5 274', 5, '', 11),
(164, 'Cauldron of Blood', '', 'V5 274', 5, '', 11),
(165, 'Reclamation of Vitae', '', 'Sabbat 50', 5, '', 11),
(166, 'Body Paint', '', 'VtM Blood Sigils; PG73', 1, '', 12),
(167, 'Checkout Time', '', 'VtM Blood Sigils; PG73', 1, '', 12),
(168, 'Elevate', '', 'VtM Blood Sigils; PG73', 1, '', 12),
(169, 'Far Reach', '', 'VtM Corebook; PG284', 1, '', 12),
(170, 'Food Stain', '', 'VtM Blood Sigils; PG74', 1, '', 12),
(171, 'Gaoler\'s Bane', '', 'Unknown', 1, '', 12),
(172, 'Haze', '', 'VtM Corebook; PG285', 1, '', 12),
(173, 'Mercurian Tongue', '', 'VtM Corebook; PG102', 1, '', 12),
(174, 'Plug-In', '', 'VtM Corebook; PG102', 1, '', 12),
(175, 'Portable Shade', '', 'VtM Sabbat The Black Hand; PG53', 1, '', 12),
(176, 'Speak from the Heart', '', 'VtM Blood Sigils; PG75', 1, '', 12),
(177, 'Advanced Torpor', '', 'VtM Blood Sigils; PG75', 2, '', 12),
(178, 'Blacklight Surprise', '', 'VtM Blood Sigils; PG75', 2, '', 12),
(179, 'Blood of Mandagloire', '', 'VtM Second Inquisition; PG46', 2, '', 12),
(180, 'Blue State', '', 'VtM Blood Sigils; PG76', 2, '', 12),
(181, 'Envelop', '', 'VtM Corebook; PG 285', 2, '', 12),
(182, 'Friends List', '', 'VtM Corebook; PG104', 2, '', 12),
(183, 'Mirror of Trust', '', 'VtM Second Inquisition; PG46', 2, '', 12),
(184, 'Red\'s Flamin\' Hot Sauce', '', 'Unknown', 2, '', 12),
(185, 'Chemically-Induced Flashback', '', 'VtM Cults of The Blood Gods; PG 45', 3, '', 12),
(186, 'Concoct Ashe', '', 'VtM Cults of The Blood Gods; PG 45', 3, '', 12),
(187, 'Defractionate', '', 'VtM Corebook; PG 286', 3, '', 12),
(188, 'Diamond Skin', '', 'VtM Blood Sigils; PG76', 3, '', 12),
(189, 'Fang-Stinger', '', 'VtM Second Inquisition; PG47', 3, '', 12),
(190, 'Fireskin', '', 'VtM Blood Sigils; PG76', 3, '', 12),
(191, 'Freezer Fluid', '', 'VtM Second Inquisition; PG47', 3, '', 12),
(192, 'Hospital Chains', '', 'VtM Blood Sigils; PG76', 3, '', 12),
(193, 'Mandagloire', '', 'VtM Corebook; PG104', 3, '', 12),
(194, 'Martian Purity', '', 'VtM Blood Sigils; PG77', 3, '', 12),
(195, 'Mask Off', '', 'VtM Blood Sigils; PG77', 3, '', 12),
(196, 'On-Demand Sunburn', '', 'VtM Sabbat The Black Hand; PG53', 3, '', 12),
(197, 'Profane Hieros Gamos', '', 'VtM Corebook  Errata', 3, '', 12),
(198, 'Rumor', '', 'VtM Corebook; PG105', 3, '', 12),
(199, 'Stay the Falling Sand', '', 'Unknown', 3, '', 12),
(200, 'Tank', '', 'VtM Corebook; PG105', 3, '', 12),
(201, 'TLC', '', 'VtM Blood Sigils; PG77', 3, '', 12),
(202, 'Troll the Pious', '', 'VtM Blood Sigils; PG78', 3, '', 12),
(203, 'Airborne Momentum', '', 'VtM Corebook; PG 287', 4, '', 12),
(204, 'Copycat', '', 'VtM Blood Sigils; PG78', 4, '', 12),
(205, 'Discipline Channelling', '', 'VtM Cults of The Blood Gods; PG 46', 4, '', 12),
(206, 'Half-Living Conductor', '', 'VtM Blood Sigils; PG79', 4, '', 12),
(207, 'Hollow Leg', '', 'Unknown', 4, '', 12),
(208, 'Red State', '', 'VtM Blood Sigils; PG79', 4, '', 12),
(209, 'Short Circuit', '', 'VtM Corebook; PG105', 4, '', 12),
(210, 'Toxic Personality', '', 'VtM Corebook; PG106', 4, '', 12),
(211, 'Vitae MSG', '', 'VtM Blood Sigils; PG79', 4, '', 12),
(212, 'Awaken the Sleeper', '', 'VtM Corebook; PG 287', 5, '', 12),
(213, 'Flowering Amaranth', '', 'VtM Corebook; PG106', 5, '', 12),
(214, 'Moment of Clarity', '', 'VtM Corebook; PG106', 5, '', 12),
(215, 'Saturn\'s Flux', '', 'VtM Blood Sigils; PG80', 5, '', 12);

-- --------------------------------------------------------

--
-- Table structure for table `vtm5_extradisciplinegroups`
--

CREATE TABLE `vtm5_extradisciplinegroups` (
  `ID` int(11) NOT NULL,
  `Name` varchar(21) DEFAULT NULL,
  `Reference` varchar(25) DEFAULT NULL,
  `ConnectedDiscipline` int(2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Dumping data for table `vtm5_extradisciplinegroups`
--

INSERT INTO `vtm5_extradisciplinegroups` (`ID`, `Name`, `Reference`, `ConnectedDiscipline`) VALUES
(1, 'Blood Sorcery Rituals', 'VtM Corebook; PG 274', 11),
(2, 'Oblivion Ceremonies', 'VtM Player\'s Guide; PG 91', 10);

-- --------------------------------------------------------

--
-- Table structure for table `vtm5_extradisciplinepowers`
--

CREATE TABLE `vtm5_extradisciplinepowers` (
  `ID` int(11) NOT NULL,
  `Name` tinytext DEFAULT NULL,
  `Description` text NOT NULL,
  `Reference` tinytext DEFAULT NULL,
  `Level` int(1) DEFAULT NULL,
  `Prerequisite` tinytext DEFAULT NULL,
  `ExtraDisciplineGroup` int(1) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Dumping data for table `vtm5_extradisciplinepowers`
--

INSERT INTO `vtm5_extradisciplinepowers` (`ID`, `Name`, `Description`, `Reference`, `Level`, `Prerequisite`, `ExtraDisciplineGroup`) VALUES
(1, 'Gift of False Life', '', 'VtM Player\'s Guide; PG 92', 1, 'Necromancer', 2),
(2, 'Knowing Stone', '', 'VtM Fall of London; 259', 1, 'Necromancer', 2),
(3, 'Summon Spirit', '', 'VtM Player\'s Guide; PG 92', 1, 'Necromancer', 2),
(4, 'Ashen Relic', '', 'VtM Book of Nod; PG 35', 2, 'Necromancer', 2),
(5, 'Awaken the Homuncular Servant', '', 'VtM Player\'s Guide; PG 93', 2, 'Necromancer', 2),
(6, 'Blinding the Alloy Eye', '', 'VtM Sabbat the Black Hand; PG 52', 2, 'Abyss Mysticism', 2),
(7, 'Compel Spirit', '', 'VtM Player\'s Guide; PG 94', 2, 'Necromancer', 2),
(8, 'Maw of Ahriman', '', 'VtM Blood Stained Love; PG 152', 2, 'Necromancer Or Abyss Mysticism', 2),
(9, 'Fortezza Sindonica', '', 'VtM Trails of Ash and Bone; PG 173', 3, 'Necromancer', 2),
(10, 'Harrowhaunt', '', 'VtM Sabbat the Black Hand; PG 51', 3, 'Necromancer', 2),
(11, 'Host Spirit', '', 'VtM Player\'s Guide; PG 94', 3, 'Necromancer', 2),
(12, 'Knit the Veil', '', 'VtM Trails of Ash and Bone; PG 174', 3, 'Necromancer', 2),
(13, 'Shambling Hordes', '', 'VtM Player\'s Guide; PG 95', 3, 'Necromancer', 2),
(14, 'Wisdom of the Dead', '', 'VtM Book of Nod; PG 35', 3, 'Necromancer', 2),
(15, 'Befoul Vessel', '', 'VtM Sabbat the Black Hand; PG 52', 4, 'Necromancer', 2),
(16, 'Bind the Spirit', '', 'VtM Player\'s Guide; PG 96', 4, 'Necromancer', 2),
(17, 'Death Rattle', '', 'VtM Trails of Ash and Bone; PG 174', 4, 'Necromancer', 2),
(18, 'Split the Veil', '', 'VtM Player\'s Guide; PG 96', 4, 'Necromancer', 2),
(19, 'Ex Nihilo', '', 'VtM Cult of the Blood God; PG 213', 5, 'Necromancer', 2),
(20, 'Lazarene Blessing', '', 'VtM Player\'s Guide; PG 97', 5, 'Necromancer', 2),
(21, 'Pit of Contemplation', '', 'VtM Cult of the Blood God; PG 94', 5, 'Abyss Mysticism', 2),
(22, 'Astromancy', '', 'VtM Blood Sigils; PG 59', 1, '', 1),
(23, 'Beelzebeatit', '', 'VtM Sabbat the Black Hand; PG 50', 1, '', 1),
(24, 'Bind the Accusing Tongue', '', 'VtM Blood Sigils; PG 60', 1, '', 1),
(25, 'Blood Apocrypha', '', 'VtM Book of Nod; PG 34', 1, '', 1),
(26, 'Blood Walk', '', 'VtM Corebook; PG 276', 1, '', 1),
(27, 'Bloody Message', '', 'VtM Let the Streets Run Red; PG 77', 1, '', 1),
(28, 'Clinging of the Insect', '', 'VtM Corebook; PG 276', 1, '', 1),
(29, 'Coax the Garden', '', 'VtM Cults of the Blood Gods; PG 55', 1, 'Bahari', 1),
(30, 'Craft Bloodstone', '', 'VtM Corebook; PG 276', 1, '', 1),
(31, 'Douse the Fear', '', 'VtM Player\'s Guide; PG 99', 1, 'Church of Caine', 1),
(32, 'Enrich the Blood', '', 'VtM Forbidden Religions; PG 76', 1, '', 1),
(33, 'Herd Ward (Minor)', '', 'VtM Let the Streets Run Red; PG 77', 1, '', 1),
(34, 'Letter Ward', '', 'VtM Let the Streets Run Red; PG 77', 1, '', 1),
(35, 'Seal the Brand', '', 'VtM Player\'s Guide; PG 99', 1, '', 1),
(36, 'Wake with Evening\'s Freshness', '', 'VtM Corebook; PG 276', 1, '', 1),
(37, 'Ward against Ghouls', '', 'VtM Corebook; PG 277', 1, '', 1),
(38, 'As Fog On Water', '', 'VtM Player\'s Guide; PG 100', 2, '', 1),
(39, 'Calix Secretus', '', 'VtM Player\'s Guide; PG 100', 2, '', 1),
(40, 'Calling the Aura\'s Remnants', '', 'VtM Chicago Folio\'s; PG 171', 2, 'Speak With ST', 1),
(41, 'Communicate with Kindred Sire', '', 'VtM Corebook; PG 277', 2, '', 1),
(42, 'Craftmaster', '', 'VtM Blood Sigils; PG 62', 2, '', 1),
(43, 'Depths of Nightmare', '', 'VtM Blood Sigils; PG 62', 2, '', 1),
(44, 'Elemental Grasp', '', 'VtM Blood Sigils; PG 62', 2, 'Koldunic Sorcery', 1),
(45, 'Enhance Dyscrasia', '', 'VtM Forbidden Religions; PG 77', 2, 'Speak With ST', 1),
(46, 'Eyes of Babel', '', 'VtM Corebook; PG 277', 2, '', 1),
(47, 'Illuminate the Trail of Prey', '', 'VtM Corebook; PG 277', 2, '', 1),
(48, 'Le Sang de l\'Amour', '', 'VtM Blood Sigils; PG 63', 2, 'Speak With ST', 1),
(49, 'Soporific Touch', '', 'VtM Player\'s Guide; PG 100', 2, '', 1),
(50, 'Shroud of Silence', '', 'VtM Forbidden Religions; PG 23', 2, 'Banu Haqim', 1),
(51, 'Silentia Mortis', '', 'VtM Blood Sigils; PG 64', 2, 'Banu Haqim', 1),
(52, 'Tiamat Glistens', '', 'VtM Blood Sigils; PG 64', 2, 'Speak With ST', 1),
(53, 'Truth of Blood', '', 'VtM Corebook; PG 277', 2, '', 1),
(54, 'Unseen Underground', '', 'VtM Fall of London; PG 128', 2, '', 1),
(55, 'Viscera Garden', '', 'VtM Blood Sigils; PG 65', 2, 'Bahari', 1),
(56, 'Ward against Spirits', '', 'VtM Corebook; PG 277', 2, '', 1),
(57, 'Warding Circle against Ghouls', '', 'VtM Corebook; PG 278', 2, 'Ward Against Ghouls', 1),
(58, 'Bladed Hands', '', 'VtM Chicago Folios; PG 174', 3, '', 1),
(59, 'Blood Sigil', '', 'VtM Blood Sigils; PG 66', 3, '', 1),
(60, 'Communal Vigor', '', 'VtM Sabbat the Black Hand; PG 50', 3, 'Speak With ST', 1),
(61, 'Dagon\'s Call', '', 'VtM Corebook; PG 278', 3, 'Banu Haqim', 1),
(62, 'Deflection of the Wooden Doom', '', 'VtM Corebook; PG 278', 3, '', 1),
(63, 'Elemental Shelter', '', 'VtM Blood Sigils; PG 66', 3, 'Koldunic Sorcery', 1),
(64, 'Essence of Air', '', 'VtM Corebook; PG 278', 3, '', 1),
(65, 'Eyes of the Past', '', 'VtM Chicago Folio\'s; PG 172', 3, 'Speak With ST', 1),
(66, 'Fire in the Blood', '', 'VtM Player\'s Guide; PG 100', 3, '', 1),
(67, 'Firewalker', '', 'VtM Corebook; PG 279', 3, '', 1),
(68, 'Galvanic Ruination', '', 'VtM Sabbat the Black Hand; PG 51', 3, '', 1),
(69, 'Gentle Mind', '', 'VtM Chicago Folio\'s; PG 172', 3, '', 1),
(70, 'Haunted House', '', 'VtM Chicago Folio\'s; PG 175', 3, 'Speak With ST', 1),
(71, 'Herd Ward (Major)', '', 'VtM Let the Streets Run Red; PG 77', 3, '', 1),
(72, 'Illusion of Peaceful Death', '', 'VtM Chicago Folio\'s; PG 172', 3, '', 1),
(73, 'Illusion of Perfection', '', 'VtM Chicago Folio\'s; PG 174', 3, '', 1),
(74, 'Nepenthe', '', 'VtM Blood Sigils; PG 66', 3, 'Speak With ST', 1),
(75, 'One with the Blade', '', 'VtM Player\'s Guide; PG 101', 3, 'Banu Haqim', 1),
(76, 'Sanguine Watcher', '', 'VtM Chicago Folio\'s; 174', 3, '', 1),
(77, 'Seeing with the Sky\'s Eyes', '', 'VtM Blood Sigils; PG 67', 3, 'Banu Haqim', 1),
(78, 'Seeking Tiamat', '', 'VtM Blood Sigils; PG 68', 3, 'Speak With ST', 1),
(79, 'Soul of the Hemonculus', '', 'VtM Blood Sigils; PG 68', 3, 'Speak With ST', 1),
(80, 'Stone of the True Form', '', 'VtM Blood Sigils; PG 68', 3, '', 1),
(81, 'Trespass', '', 'VtM Blood Sigils; PG 69', 3, 'Speak With ST', 1),
(82, 'The Unseen Change', '', 'VtM Chicago Folio\'s; PG 172', 3, 'Ward against Lupines', 1),
(83, 'Viral Haruspex', '', 'VtM Blood Sigils; PG 69', 3, 'Speak With ST', 1),
(84, 'Ward against Lupines', '', 'VtM Corebook; PG 279', 3, '', 1),
(85, 'Warding Circle against Spirits', '', 'VtM Corebook; PG 279', 3, 'Ward Against Spirits', 1),
(86, 'Compel the Inanimate', '', 'VtM Blood Sigils; PG 70', 4, '', 1),
(87, 'Defense of the Sacred Haven', '', 'VtM Corebook; PG 279', 4, '', 1),
(88, 'Egregore Consultation', '', 'VtM Blood Sigils; PG 70', 4, 'Speak With ST', 1),
(89, 'Eyes of the Nighthawk', '', 'VtM Corebook; PG 279', 4, '', 1),
(90, 'Feast of Ashes', '', 'VtM Player\'s Guide; PG 101', 4, '', 1),
(91, 'Guided Memory', '', 'VtM Player\'s Guide; PG 101', 4, 'Speak With ST', 1),
(92, 'Incorporeal Passage', '', 'VtM Corebook; PG 280', 4, '', 1),
(93, 'Invisible Chains of Binding', '', 'VtM Player\'s Guide; PG 102', 4, '', 1),
(94, 'Land\'s Sustenance', '', 'VtM Blood Sigils; PG 70', 4, 'Speak With ST', 1),
(95, 'Protean Curse', '', 'VtM Chicago Folio\'s; PG 173', 4, '', 1),
(96, 'Rending the Sweet Earth', '', 'VtM Chicago Folio\'s; PG 173', 4, '', 1),
(97, 'Riding the Earth\'s Veins', '', 'VtM Blood Sigils; PG 71', 4, 'Speak With ST', 1),
(98, 'Ward against Kindred (Cainite)', '', 'VtM Corebook; PG 280', 4, '', 1),
(99, 'Warding Circle against Lupines', '', 'VtM Corebook; PG 280', 4, 'Ward against Lupines', 1),
(100, 'Antebrachia Ignium', '', 'VtM Player\'s Guide; PG 102', 5, '', 1),
(101, 'Dominion', '', 'VtM Player\'s Guide; PG 103', 5, '', 1),
(102, 'Eden\'s Bounty', '', 'VtM Cults of the Blood Gods; PG 56', 5, 'Bahari', 1),
(103, 'Elemental Attack', '', 'VtM Blood Sigils; PG 71', 5, 'Koldunic Sorcery', 1),
(104, 'Escape to True Sanctuary', '', 'VtM Corebook; PG 280', 5, '', 1),
(105, 'Fisher King', '', 'VtM Blood Sigils; PG 72', 5, 'Speak With ST', 1),
(106, 'Heart of Stone', '', 'VtM Corebook; PG 281', 5, '', 1),
(107, 'Shaft of Belated Dissolution', '', 'VtM Corebook; PG 281', 5, '', 1),
(108, 'Simulacrum Gate', '', 'VtM Sabbat the Black Hand; PG 51', 5, 'Speak With ST', 1),
(109, 'Warding Circle against Kindred (Cainite)', '', 'VtM Corebook; PG 282', 5, 'Ward against Kindred (Cainite)', 1);

-- --------------------------------------------------------

--
-- Table structure for table `vtm5_flaws`
--

CREATE TABLE `vtm5_flaws` (
  `ID` int(2) NOT NULL,
  `Name` tinytext DEFAULT NULL,
  `Values` tinytext DEFAULT NULL,
  `Limits` int(2) DEFAULT NULL,
  `Description` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Dumping data for table `vtm5_flaws`
--

INSERT INTO `vtm5_flaws` (`ID`, `Name`, `Values`, `Limits`, `Description`) VALUES
(1, 'Illiterate', '2', 1, ''),
(2, 'Looks', '1,2', 1, ''),
(3, 'Stench', '1', 1, ''),
(4, 'Transparent', '1', 1, ''),
(5, 'Addiction', '1,2', -1, ''),
(6, 'Bond Junkie', '1', 1, ''),
(7, 'Long Bond', '1', 1, ''),
(8, 'Bond Slave', '2', 1, ''),
(9, 'Two Masters', '1', 1, ''),
(10, 'Prey Exclusion', '1,2', 1, ''),
(11, 'Methuselah\'s Thirst', '1', 1, ''),
(12, 'Farmer', '2', 1, ''),
(13, 'Organovore', '2', 1, ''),
(14, 'Vein Tapper', '1', 1, ''),
(15, 'Folkloric Bane', '1', -1, ''),
(16, 'Folkloric Block', '1', -1, ''),
(17, 'Stigmata', '1', 1, ''),
(18, 'Stake Bait', '2', 1, ''),
(19, 'Starving Decay', '2', 1, ''),
(20, 'Twice Cursed', '2', 1, ''),
(21, 'Beacon of Profanity', '1', 1, ''),
(22, 'Crisis of Faith', '1', 1, ''),
(23, 'Horrible Scars of Penitence', '1', 1, ''),
(24, 'Grovelling Worm', '2', 1, ''),
(25, 'Disease Vector', '1', 1, ''),
(26, 'Plaguebringer', '1,2', 1, ''),
(27, 'Knowledge Hungry', '1', -1, ''),
(28, 'Prestation Debts', '1', 1, ''),
(29, 'Risk-Taker', '1', 1, ''),
(30, 'Weak-Willed', '2', 1, ''),
(31, 'Excommunicated', '1,2', 1, ''),
(32, 'Faithless', '2', 1, ''),
(33, 'Ashe Addiction', '2', 1, ''),
(34, 'Schism (Lasombra)', '1', 1, ''),
(35, 'False Alarm', '1', 1, ''),
(36, 'Empty', '1', 1, ''),
(37, 'Failed Initiate', '1', 1, ''),
(38, 'Yearning', '1', 1, ''),
(39, 'Enemy', '1,2', -1, ''),
(40, 'Dark Secret', '1,2', -1, ''),
(41, 'Infamy', '1,2', -1, ''),
(42, 'Disliked', '1', 1, ''),
(43, 'Dispised', '2', 1, ''),
(44, 'No Haven', '1', 1, ''),
(45, 'Obvious Predator', '2', 1, ''),
(46, 'Known Corpse/Blankbody', '1,2', 1, ''),
(47, 'Adversary', '1,2,3', -1, ''),
(48, 'Destitute', '1', 1, ''),
(49, 'Stalkers', '1', -1, ''),
(50, 'Suspect', '1', 1, '');

-- --------------------------------------------------------

--
-- Table structure for table `vtm5_havenflaws`
--

CREATE TABLE `vtm5_havenflaws` (
  `ID` int(11) NOT NULL,
  `Name` tinytext DEFAULT NULL,
  `Values` tinytext DEFAULT NULL,
  `Limits` int(2) DEFAULT NULL,
  `Description` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Dumping data for table `vtm5_havenflaws`
--

INSERT INTO `vtm5_havenflaws` (`ID`, `Name`, `Values`, `Limits`, `Description`) VALUES
(1, 'Haven - Creepy', '1', 1, ''),
(2, 'Haven - Haunted', '1,2,3,4,5', -1, ''),
(3, 'Haven - Compromised', '2', 1, ''),
(4, 'Haven - Shared', '1,2', 1, '');

-- --------------------------------------------------------

--
-- Table structure for table `vtm5_havenmerits`
--

CREATE TABLE `vtm5_havenmerits` (
  `ID` int(11) NOT NULL,
  `Name` tinytext DEFAULT NULL,
  `Values` tinytext DEFAULT NULL,
  `Limits` int(2) DEFAULT NULL,
  `Description` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Dumping data for table `vtm5_havenmerits`
--

INSERT INTO `vtm5_havenmerits` (`ID`, `Name`, `Values`, `Limits`, `Description`) VALUES
(1, 'Haven - Hidden Armoury', '1,2,3,4,5', -1, ''),
(2, 'Haven - Cell', '1,2,3,4,5', -1, ''),
(3, 'Haven - Watchmen', '1,2,3,4,5', -1, ''),
(4, 'Haven - Laboratory', '1,2,3,4,5', -1, ''),
(5, 'Haven - Library', '1,2,3,4,5', -1, ''),
(6, 'Haven - Location', '1', 1, ''),
(7, 'Haven - Luxury', '1', 1, ''),
(8, 'Haven - Postern', '1,2,3,4,5', -1, ''),
(9, 'Haven - Security System', '1,2,3,4,5', -1, ''),
(10, 'Haven - Surgery', '1', 1, ''),
(11, 'Haven - Warding', '1,2,3,4,5', 1, ''),
(12, 'Haven - Holy Ground', '1', 1, ''),
(13, 'Haven - Shrine', '1,2,3', 1, ''),
(14, 'Haven - Business Establishment', '2,3', 1, ''),
(15, 'Haven - Furcus', '1,2,3', 1, ''),
(16, 'Haven - Machine Shop', '1,2,3,4,5', 1, '');

-- --------------------------------------------------------

--
-- Table structure for table `vtm5_merits`
--

CREATE TABLE `vtm5_merits` (
  `ID` int(11) NOT NULL,
  `Name` tinytext DEFAULT NULL,
  `Values` tinytext DEFAULT NULL,
  `Limits` int(2) DEFAULT NULL,
  `Description` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Dumping data for table `vtm5_merits`
--

INSERT INTO `vtm5_merits` (`ID`, `Name`, `Values`, `Limits`, `Description`) VALUES
(1, 'Linguistics', '1', -1, 'Each dot of Linguistics allows the character to read, write and speak fluently in another language outside of the default two they already know, which is their native language and the language of the Domain.'),
(2, 'Looks', '2,4', 1, 'Beautiful (2 dot version): Gain 1 additional dice on all social tests\nStunning (4 dot version): Gain 2 additional dice on all social tests'),
(3, 'Semblance of the Methuselah', '1,2', 1, 'With an appearance strikingly similar to a methuselah, gain one die on rolls to impress, intimidate or attract the attention who recognize your face. As well as gain other bonuses such as status or additional die when meeting the methuselah they resemble'),
(4, 'Famous Face', '1', 1, 'Appear as someone famous and gain two dice in social tests where this works to their benefit. Take a two-dice penalty whenever they attempt to hide in a crowd or avoid recognition'),
(5, 'Ingénue', '1', 1, 'They appear innocent and blameless, add two dice to any rolls related to avoiding suspicion or deflecting blame at the Storytellers’ discretion'),
(6, 'Remarkable Feature', '1', 1, 'Possessing a rare, memorable feature such as eye color or unusual complexion. Add two-dice to social interactions with strangers and take a one-die penalty to disguise yourself'),
(7, 'Up All Night', '2,3', 1, 'Treat Humanity as one higher (Max 10), or two dots higher if taken at four dots when using Blush of Life, eating, drinking, or sexual intercourse'),
(8, 'High Functioning Addict', '1', 1, 'Add one die to either Physical, Social, or Mental pool when the last feeding had the drug of their desire. '),
(9, 'Bond Resistance', '1,2,3', 1, 'Add one die to resist Blood Bonds per level of this merit'),
(10, 'Short Bond', '2', 1, 'Bonds decrease by two levels each month if not reinforced.'),
(11, 'Unbondable', '5', 1, 'A Vampire with this merit cannot become under the effects of a bloodbond. This Merit is not available for Tremere Characters unless otherwise specified by an ST'),
(12, 'Bloodhound', '1', 1, 'Able to sniff out resonances without tasting them. '),
(13, 'Iron Gullet', '3', 1, 'Able to consume rancid, defractionated, or otherwise unedible blood to other vampires'),
(14, 'Vessel Recognition', '1', 1, 'With a Resolve + Awareness test at Difficulty 2 they can tell if a mortal has been fed on recently. A critical win lets them sense if the feed is recurring, meaning there is a chance it’s a herd member'),
(15, 'Eat Food', '2', 1, 'Can consume food but still with no nourishment'),
(16, 'Cold Dead Hunger', '3', 1, 'Add two dice to resist Hunger frenzy'),
(17, 'Pack Diablerie', '2', 1, 'The character will always be the one to take the soul unless they otherwise choose during Diablerie. Additionally, if they help another consume the soul, they gain 5 experience points to spend in the same manner as if they\'d committed the Diablerie themselves'),
(18, 'Luck of the Devil', '4', 1, 'Once per session when misfortune occurs it can be redirected towards someone close to them for the victim to take the fall'),
(19, 'Nuit Mode', '2', 1, 'The Kindred’s body does not revert to it’s death-state each night, enabling them to keep new haircuts and body modifications. They can mend these changes anytime as if they were Aggravated damage. This does not work for characters with BP higher than 1'),
(20, 'Unholy Will', '2,4', 1, 'With two dots, add one die to any pool when resisting or contesting against an individual with True Faith when related to their faith. The character also suffers one less point of damage from holy sources. At four dots, add two dice and suffer two fewer points of damage'),
(21, 'Zealotry', '1,2,3', 1, 'For each dot in this merit, once per session when succeeding with a normal roll that relates or aligns to the character\'s Conviction, turn it into a messy critical. '),
(22, 'Penitence', '1,2,3,4', 1, 'Once per session, take one point of self-inflicted Superficial Health Damage in exchange for one point of Superficial Willpower damage. '),
(23, 'Soothed Beast', '1', 1, 'With a SPC as an obsession, once per session they can ignore one Bestial or Messy Critical. Gain three Stains if they die'),
(24, 'False Love', '1', 1, 'With a SPC as an obsession, when in their presence treat the character\'s treat Humanity as one higher (Max 10) for purposes of using Blush of Life, eating, drinking, or sexual intercourse. Gain three Stains if they die'),
(25, 'Check the Trunk', '1', 1, ''),
(26, 'Side Hustler', '2', 1, ''),
(27, 'Tempered Will', '3', 1, ''),
(28, 'Untouchable', '5', 1, ''),
(29, 'Apocryphal Texts', '1', 1, ''),
(30, 'Inspired Artist', '2', 1, ''),
(31, 'Traveling Preacher', '2', 1, ''),
(32, 'Memories of the Fallen (Thinblood Only)', '2', 1, ''),
(33, 'Streamer', '2', 1, ''),
(34, 'Gardener', '1,2,3,4,5', 1, ''),
(35, 'Dark Mother\'s Song', '2', 1, ''),
(36, 'Fire Resistant', '1', 1, ''),
(37, 'Vigilant', '2', 1, ''),
(38, 'Fixer', '2', 1, ''),
(39, 'Go to Ground', '1', 1, ''),
(40, 'Insidious Whispers', '2', 1, ''),
(41, 'Gematria', '1', 1, ''),
(42, 'Bull-Slayer', '3', 1, ''),
(43, 'Bargainer', '1', 1, ''),
(44, 'Archangel\'s Grace', '3', 1, ''),
(45, 'Allies', '1,2,3,4,5,6', -1, ''),
(46, 'Contacts', '1,2,3', -1, ''),
(47, 'Fame', '1,2,3,4,5', -1, ''),
(48, 'Influence', '1,2,3,4,5', -1, ''),
(49, 'Herd', '1,2,3,4,5', -1, ''),
(50, 'Mask', '1,2', 1, ''),
(51, 'Mask - Zeroed', '1', 1, ''),
(52, 'Mask - Cobbler', '1', 1, ''),
(53, 'Mawla', '1,2,3,4,5', -1, ''),
(54, 'Resources', '1,2,3,4,5', 1, ''),
(55, 'Retainer', '1,2,3', -1, ''),
(56, 'Status', '1,2,3,4,5', -1, ''),
(57, 'City Secrets', '1', 1, ''),
(63, 'LS - Carna [Embrace the Vision]', '1', 1, ''),
(64, 'LS - Carna [The Rebel Trait]', '2', 1, ''),
(65, 'LS - Carna [Unorthodox Rituals]', '3', 1, ''),
(66, 'LS - Carna [Reimagined Bond]', '4', 1, ''),
(67, 'LS - Carna [Book of the Grave-War]', '5', 1, ''),
(68, 'LS - The Circulatory System [Tap into the System]', '1', 1, ''),
(69, 'LS - The Circulatory System [Little Black Book]', '2', 1, ''),
(70, 'LS - The Circulatory System [Farm Upstate]', '3', 1, ''),
(71, 'LS - The Circulatory System [Secure Transit]', '4', 1, ''),
(72, 'LS - The Circulatory System [Blood Sommelier]', '5', 1, ''),
(73, 'LS - Descendant of Hardestadt [Voice of Hardestadt]', '1', 1, ''),
(74, 'LS - Descendant of Hardestadt [Supreme Leader]', '2', 1, ''),
(75, 'LS - Descendant of Hardestadt [Ventrue Pillar]', '3', 1, ''),
(76, 'LS - Descendant of Hardestadt [Line to the Founders]', '4', 1, ''),
(77, 'LS - Descendant of Hardestadt [Hardestadt\'s Heir]', '5', 1, ''),
(78, 'LS - Descendant of Helena [Skin Deep]', '1', 1, ''),
(79, 'LS - Descendant of Helena [Real Talent]', '2', 1, ''),
(80, 'LS - Descendant of Helena [Embrace the Stereotype]', '3', 1, ''),
(81, 'LS - Descendant of Helena [Divine Purity]', '4', 1, ''),
(82, 'LS - Descendant of Helena [Succubus Club Franchise]', '5', 1, ''),
(83, 'LS - Descendant of Tyler [Instigator]', '1', 1, ''),
(84, 'LS - Descendant of Tyler [Champion of the Cause]', '2', 1, ''),
(85, 'LS - Descendant of Tyler [Tyler\'s Mercy]', '3', 1, ''),
(86, 'LS - Descendant of Tyler [The Furores]', '4', 1, ''),
(87, 'LS - Descendant of Tyler [Permanent Revolution]', '5', 1, ''),
(88, 'LS - Descendant of Zelios [Sanctuary]', '1', 1, ''),
(89, 'LS - Descendant of Zelios [Saboteur]', '2', 1, ''),
(90, 'LS - Descendant of Zelios [On Commission]', '3', 1, ''),
(91, 'LS - Descendant of Zelios [The Laburinth]', '4', 1, ''),
(92, 'LS - Descendant of Zelios [Sense the Lay Lines]', '5', 1, ''),
(93, 'LS - Descendant of Vasantasena [Agent of Chaos]', '1', 1, ''),
(94, 'LS - Descendant of Vasantasena [Hear My Words]', '2', 1, ''),
(95, 'LS - Descendant of Vasantasena [Scent the Bond]', '3', 1, ''),
(96, 'LS - Descendant of Vasantasena [Destroy the Bond]', '4', 1, ''),
(97, 'LS - Descendant of Vasantasena [Sabbat Become Camarilla]', '5', 1, ''),
(98, 'LS - Descendant of Karl Schrekt [Remember the House]', '1', 1, ''),
(99, 'LS - Descendant of Karl Schrekt [Hardliner]', '2', 1, ''),
(100, 'LS - Descendant of Karl Schrekt [Ritual Preparedness]', '3', 1, ''),
(101, 'LS - Descendant of Karl Schrekt [Archon\'s Bane]', '4', 1, ''),
(102, 'LS - Descendant of Karl Schrekt [Know the World]', '5', 1, ''),
(103, 'LS - Descendant of Xaviar [Martyred Ancestor]', '1', 1, ''),
(104, 'LS - Descendant of Xaviar [Where the Bodies are Buried]', '2', 1, ''),
(105, 'LS - Descendant of Xaviar [Loyal Hound]', '3', 1, ''),
(106, 'LS - Descendant of Xaviar [Monstrous Bat]', '4', 1, ''),
(107, 'LS - Descendant of Xaviar [Experienced the Antedeluvian]', '5', 1, ''),
(108, 'LS - Bankers of Dunsirn [Money Obfuscates]', '1', 1, ''),
(109, 'LS - Bankers of Dunsirn [Money Talks]', '2', 1, ''),
(110, 'LS - Bankers of Dunsirn [Money Enhances]', '3', 1, ''),
(111, 'LS - Bankers of Dunsirn [Money Multiplies]', '4', 1, ''),
(112, 'LS - Bankers of Dunsirn [Money Dictates]', '5', 1, ''),
(113, 'LS - Children of Tenochtitlan [Hiding from the Wolf]', '1', 1, ''),
(114, 'LS - Children of Tenochtitlan [Ghostly Instincts]', '2', 1, ''),
(115, 'LS - Children of Tenochtitlan [Forward Thinking]', '3', 1, ''),
(116, 'LS - Children of Tenochtitlan [Necromantic Prodigy]', '4', 1, ''),
(117, 'LS - Children of Tenochtitlan [Next in Line]', '5', 1, ''),
(118, 'LS - Flesh Eaters [Viscus]', '1', 1, ''),
(119, 'LS - Flesh Eaters [Unseen Spirit]', '2', 1, ''),
(120, 'LS - Flesh Eaters [The Perfect Murder]', '3', 1, ''),
(121, 'LS - Flesh Eaters [Send a Murderer]', '4', 1, ''),
(122, 'LS - Flesh Eaters [Monstrous Bite]', '5', 1, ''),
(123, 'LS - Harbingers of Ashur [The Ashen Mask]', '1', 1, ''),
(124, 'LS - Harbingers of Ashur [The Gold Mask]', '2', 1, ''),
(125, 'LS - Harbingers of Ashur [The White Mask]', '3', 1, ''),
(126, 'LS - Harbingers of Ashur [The Obsidian Mask]', '4', 1, ''),
(127, 'LS - Harbingers of Ashur [The Lazarene Mask]', '5', 1, ''),
(128, 'LS - La Famiglia Giovanni [A Cousin\'s Ear]', '1', 1, ''),
(129, 'LS - La Famiglia Giovanni [Faded Glamor]', '2', 1, ''),
(130, 'LS - La Famiglia Giovanni [Petty Cash]', '3', 1, ''),
(131, 'LS - La Famiglia Giovanni [Spectre Servant]', '4', 1, ''),
(132, 'LS - La Famiglia Giovanni [Aspiring Anziano]', '5', 1, ''),
(133, 'LS - The Gorgons [The Serpent\'s Kiss]', '1', 1, ''),
(134, 'LS - The Gorgons [Protection]', '2', 1, ''),
(135, 'LS - The Gorgons [Four Humours]', '3', 1, ''),
(136, 'LS - The Gorgons [Controling the Beast]', '4', 1, ''),
(137, 'LS - The Gorgons [Medusa\'s Gaze]', '5', 1, ''),
(138, 'LS - Nasyon San An [CSI Shit]', '1', 1, ''),
(139, 'LS - Nasyon San An [Pound of Flesh]', '2', 1, ''),
(140, 'LS - Nasyon San An [Treat Yourself]', '3', 1, ''),
(141, 'LS - Nasyon San An [My Setite Friends]', '4', 1, ''),
(142, 'LS - Nasyon San An [The Silk Hat]', '5', 1, ''),
(143, 'LS - Descendant of de Camden [Proud Childe]', '1', 1, ''),
(144, 'LS - Descendant of de Camden [Corpsense]', '2', 1, ''),
(145, 'LS - Descendant of de Camden [Eye to Eye]', '3', 1, ''),
(146, 'LS - Descendant of de Camden [The Way of all Flesh]', '4', 1, ''),
(147, 'LS - Descendant of de Camden [Perchance to Dream]', '5', 1, ''),
(148, 'LS - Descendant of Menele [Symposium]', '1', 1, ''),
(149, 'LS - Descendant of Menele [Carthage Delenda Est]', '2', 1, ''),
(150, 'LS - Descendant of Menele [Know Thyself]', '3', 1, ''),
(151, 'LS - Descendant of Menele [Knowledge is Power]', '4', 1, ''),
(152, 'LS - Descendant of Menele [The Greater Mysteries]', '5', 1, ''),
(153, 'LS - Descendant of Montano [The Shadow of Yesterday]', '1', 1, ''),
(154, 'LS - Descendant of Montano [Sibling in Darkness]', '2', 1, ''),
(155, 'LS - Descendant of Montano [Abyssal Apprentice]', '3', 1, ''),
(156, 'LS - Descendant of Montano [Word of Mouth]', '4', 1, ''),
(157, 'LS - Descendant of Montano [Purity of Remorse]', '5', 1, ''),
(158, 'LS - Descendant of Lodin [Baby of the Family]', '1', 1, ''),
(159, 'LS - Descendant of Lodin [Responsible Middle Childe]', '2', 1, ''),
(160, 'LS - Descendant of Lodin [Black Sheep of the Family]', '3', 1, ''),
(161, 'LS - Descendant of Lodin [Like Sire, Like Childe]', '4', 1, ''),
(162, 'LS - Descendant of Lodin [Long-Lost Relative]', '5', 1, ''),
(163, 'LS - Descendant of Al-Ashrad [Stories of Old]', '1', 1, ''),
(164, 'LS - Descendant of Al-Ashrad [Sight Beyond Sight]', '2', 1, ''),
(165, 'LS - Descendant of Al-Ashrad [Vengeful Sorcery]', '3', 1, ''),
(166, 'LS - Descendant of Al-Ashrad [Banish the Intangible]', '4', 1, ''),
(167, 'LS - Descendant of Al-Ashrad [Amr-in-Waiting]', '5', 1, ''),
(175, 'LS - Kindred Iconography [Iconographer]', '1', 1, ''),
(176, 'LS - Kindred Iconography [The Writing on the Wall]', '2', 1, ''),
(177, 'LS - Kindred Iconography [Trendsetter]', '3', 1, ''),
(178, 'LS - Kindred Iconography [Graffiti Artist]', '4', 1, ''),
(179, 'LS - Kindred Iconography [Giorgio Who?]', '5', 1, '');

-- --------------------------------------------------------

--
-- Table structure for table `vtm5_predatortype`
--

CREATE TABLE `vtm5_predatortype` (
  `ID` int(2) NOT NULL,
  `Name` tinytext DEFAULT NULL,
  `Description` text NOT NULL,
  `Specialisations` text DEFAULT NULL,
  `Disciplines` tinytext DEFAULT NULL,
  `Humanity` int(2) DEFAULT NULL,
  `Blood Potency` int(1) DEFAULT NULL,
  `Merits` text DEFAULT NULL,
  `Flaws` text DEFAULT NULL,
  `Reference` tinytext DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Dumping data for table `vtm5_predatortype`
--

INSERT INTO `vtm5_predatortype` (`ID`, `Name`, `Description`, `Specialisations`, `Disciplines`, `Humanity`, `Blood Potency`, `Merits`, `Flaws`, `Reference`) VALUES
(1, 'Alleycat', 'Those who find violence to be the quickest way to get what they want might gravitate towards this hunting style. Alleycats are a vampire who feeds by brute force and outright attack and feeds from whomever they can when they can. Intimidation is a route easily taken to make their victims cower or even Dominating the victims to not report the attack or mask it as something else entirely.\r\nStrength + Brawl is to take blood by force or threat. Wits + Streetwise can be used to find criminals as if a vigilante figure.', '[{\"Skill\": \"Intimidation\", \"Spec\":\"Stickups\"}, {\"Skill\":\"Brawl\", \"Spec\":\"Grappling\"}]', '[\"Celerity\", \"Potence\"]', -1, 0, '[{\"Name\": \"Contacts\", \"Value\":3, \"Extra\": \"Criminal\"}]', '[]', 'VtM Corebook; PG 175'),
(2, 'Bagger', 'Sometimes the best blood doesn\'t come from a live body. Baggers are kindred who take an approach most are unable to with their ability to consume preserved, defractionated or rancid blood through (•••) Iron Gullet, allowing them to feed from unusual sources such as blood bags or corpses. Perhaps they work in a hospital or blood bank or they might even have enough knowledge about the black market to obtain their blood. Ventrue are unable to pick this Predator type.\nIntelligence + Streetwise can be used to find, gain access and purchase the goods.', '[{\"Skill\": \"Larceny\", \"Spec\":\"Lock-Picking\"}, {\"Skill\":\"Streetwise\", \"Spec\":\"Black-market\"}]', '[\"Blood Sorcery\", \"Obfuscate\"]', 0, 0, '[{\"Name\": \"Iron Gullet\", \"Value\":3, \"Extra\": \"\"}]', '[{\"Name\": \"Enemy\", \"Value\":2, \"Extra\": \"\"}]', 'VtM Corebook; PG 176'),
(3, 'Blood Leech (Diablerist)', 'Some Kindred might see feeding from mortals as inherently wrong or disgusting regardless of others\' rationale. Blood Leech is a feeding style that is not looked upon kindly by many vampires making it risky unless the Kindred has a position of power and can keep their little secret secure. Regardless, with their rejection of mortal blood, they instead feed upon the vitae of other vampires through hunting those weaker than them, coercion, or taking Blood as payment', '[{\"Skill\": \"Brawl\", \"Spec\":\"Kindred\"}, {\"Skill\":\"Stealth\", \"Spec\":\"Against Kindred\"}]', '[\"Celerity\", \"Protean\"]', -1, 1, '[]', '[{\"Name\": \"Prey Exclusion\", \"Value\":2, \"Extra\": \"Mortals\"}, {\"Name\": \"Dark Secret\", \"Value\": 2, \"Extra\": \"Diablorist\"}]', 'VtM Corebook; PG 176'),
(4, 'Blood Leech (Shunned)', 'Some Kindred might see feeding from mortals as inherently wrong or disgusting regardless of others\' rationale. Blood Leech is a feeding style that is not looked upon kindly by many vampires making it risky unless the Kindred has a position of power and can keep their little secret secure. Regardless, with their rejection of mortal blood, they instead feed upon the vitae of other vampires through hunting those weaker than them, coercion, or taking Blood as payment', '[{\"Skill\": \"Brawl\", \"Spec\":\"Kindred\"}, {\"Skill\":\"Stealth\", \"Spec\":\"Against Kindred\"}]', '[\"Celerity\", \"Protean\"]', -1, 1, '[]', '[{\"Name\": \"Prey Exclusion\", \"Value\":2, \"Extra\": \"Mortals\"}, {\"Name\": \"Shunned\", \"Value\": 2, \"Extra\": \"\"}]', 'VtM Corebook; PG 176'),
(5, 'Cleaver', 'The sweetest blood might be from those closest to them, the Cleaver takes advantage of that idea while taking blood from either their own close family and friends or even those close to someone else. Covertly stealing the blood from their victims while still maintaining ties to them. Cleavers will go to extreme lengths to keep their condition a secret from their victims but some may instead take a less than pleasant route. The Camarilla forbids the practice of taking a human family in this fashion, as it\'s a breach waiting to happen', '[{\"Skill\": \"Persuasion\", \"Spec\":\"Gaslighting\"}, {\"Skill\":\"Subterfuge\", \"Spec\":\"Coverups\"}]', '[\"Dominate\", \"Animalism\"]', 0, 0, '[{\"Name\": \"Herd\", \"Value\":2, \"Extra\": \"\"}]', '[{\"Name\": \"Dark Secret\", \"Value\": 1, \"Extra\": \"Cleaver\"}]', 'VtM Corebook; PG 176'),
(6, 'Consensualist', '', '[{\"Skill\": \"Medicine\", \"Spec\":\"Phlegbotomy\"}, {\"Skill\":\"Persuasion\", \"Spec\":\"Victims\"}]', '[\"Auspex\", \"Fortitude\"]', 1, 0, '[]', '[{\"Name\": \"Dark Secret\", \"Value\": 1, \"Extra\": \"Masquarade Breacher\"}, {\"Name\": \"Prey Exclusion\", \"Value\":1, \"Extra\": \"Non-consenting\"}]', 'VtM Corebook; PG 177'),
(7, 'Farmer', '', '[{\"Skill\": \"Animal Ken\", \"Spec\":\"An Animal Type - Speak to ST\"}, {\"Skill\":\"Survival\", \"Spec\":\"Hunting\"}]', '[\"Animalism\", \"Protean\"]', 1, 0, '[]', '[{\"Name\": \"Vegan\", \"Value\":2, \"Extra\": \"\"}]', 'VtM Corebook; PG 177'),
(8, 'Osiris (Fame)', '', '[{\"Skill\": \"Occult\", \"Spec\":\"Specific Tradition - Speak To ST\"}, {\"Skill\":\"Performance\", \"Spec\":\"Specific Entertainment Field\"}]', '[\"Blood Sorcery\", \"Presence\"]', 0, 0, '[{\"Name\": \"Fame\", \"Value\":3, \"Extra\": \"\"}]', '[{\"Name\": \"Enemy\", \"Value\":2, \"Extra\": \"\"}]', 'VtM Corebook; PG 177'),
(9, 'Osiris (Herd)', '', '[{\"Skill\": \"Occult\", \"Spec\":\"Specific Tradition - Speak To ST\"}, {\"Skill\":\"Performance\", \"Spec\":\"Specific Entertainment Field\"}]', '[\"Blood Sorcery\", \"Presence\"]', 0, 0, '[{\"Name\": \"Herd\", \"Value\":3, \"Extra\": \"\"}]', '[{\"Name\": \"Enemy\", \"Value\":2, \"Extra\": \"\"}]', 'VtM Corebook; PG 177'),
(10, 'Sandman', '', '[{\"Skill\": \"Medicine\", \"Spec\":\"Anesthetics\"}, {\"Skill\":\"Stealth\", \"Spec\":\"Break-Ins\"}]', '[\"Auspex\", \"Obfuscate\"]', 0, 0, '[{\"Name\": \"Resources\", \"Value\":1, \"Extra\": \"\"}]', '[]', 'VtM Corebook; PG 177'),
(11, 'Scene Queen (Disliked)', '', '[{\"Skill\": \"Etiquette\", \"Spec\":\"Specific Scene - Speak to ST\"}, {\"Skill\": \"Leadership\", \"Spec\":\"Specific Scene - Speak to ST\"}]', '[\"Dominate\", \"Potence\"]', 0, 0, '[{\"Name\": \"Fame\", \"Value\":1, \"Extra\": \"\"},{\"Name\": \"Contacts\", \"Value\":1, \"Extra\": \"\"}]', '[{\"Name\": \"Disliked\", \"Value\":1, \"Extra\": \"Outside your sub-culture\"}]', 'VtM Corebook; PG 178'),
(12, 'Scene Queen (Prey Exclusion)', '', '[{\"Skill\": \"Etiquette\", \"Spec\":\"Specific Scene - Speak to ST\"}, {\"Skill\": \"Leadership\", \"Spec\":\"Specific Scene - Speak to ST\"}]', '[\"Dominate\", \"Potence\"]', 0, 0, '[{\"Name\": \"Fame\", \"Value\":1, \"Extra\": \"\"},{\"Name\": \"Contacts\", \"Value\":1, \"Extra\": \"\"}]', '[{\"Name\": \"Prey Exclusion\", \"Value\":1, \"Extra\": \"A different sub-culture to yours\"}]', 'VtM Corebook; PG 178'),
(13, 'Siren', '', '[{\"Skill\": \"Persuasion\", \"Spec\":\"Seduction\"},{\"Skill\": \"Subterfuge\", \"Spec\":\"Seduction\"}]', '[\"Fortitude\", \"Presence\"]', 0, 0, '[{\"Name\": \"Looks\", \"Value\":2, \"Extra\": \"\"}]', '[{\"Name\": \"Enemy\", \"Value\":1, \"Extra\": \"A spurned lover or jealous partner\"}]', 'VtM Corebook; PG 178'),
(14, 'Extortionist (Contacts)', '', '[{\"Skill\": \"Intimidation\", \"Spec\":\"Coercion\"},{\"Skill\": \"Larceny\", \"Spec\":\"Security\"}]', '[\"Dominate\", \"Potence\"]', 0, 0, '[{\"Name\": \"Contacts\", \"Value\":3, \"Extra\": \"\"}]', '[{\"Name\": \"Enemy\", \"Value\":2, \"Extra\": \"The police or a victim who wants revenge\"}]', 'VtM Player\'s Guide; PG 107'),
(15, 'Extortionist (Resources)', '', '[{\"Skill\": \"Intimidation\", \"Spec\":\"Coercion\"},{\"Skill\": \"Larceny\", \"Spec\":\"Security\"}]', '[\"Dominate\", \"Potence\"]', 0, 0, '[{\"Name\": \"Resources\", \"Value\":3, \"Extra\": \"\"}]', '[{\"Name\": \"Enemy\", \"Value\":2, \"Extra\": \"The police or a victim who wants revenge\"}]', 'VtM Player\'s Guide; PG 108'),
(16, 'Graverobber', '', '[{\"Skill\": \"Occult\", \"Spec\":\"Grave Rituals\"},{\"Skill\": \"Medicine\", \"Spec\":\"Cadavers\"}]', '[\"Fortitude\", \"Oblivion\"]', 0, 0, '[{\"Name\": \"Iron Gullet\", \"Value\":3, \"Extra\": \"\"},{\"Name\": \"Haven\", \"Value\":1, \"Extra\": \"\"}]', '[{\"Name\": \"Obvious Predator\", \"Value\":2, \"Extra\": \"\"}]', 'VtM Player\'s Guide; PG 108'),
(17, 'Grim Reaper (Allies)', '', '[{\"Skill\": \"Awareness\", \"Spec\":\"Death\"},{\"Skill\": \"Larceny\", \"Spec\":\"Forgery\"}]', '[\"Auspex\", \"Oblivion\"]', 1, 0, '[{\"Name\": \"Allies\", \"Value\":1, \"Extra\": \"Medical Community\"}]', '[{\"Name\": \"Prey Exclusion\", \"Value\":1, \"Extra\": \"Healthy Mortals\"}]', 'VtM Player\'s Guide; PG 108'),
(18, 'Grim Reaper (Influence)', '', '[{\"Skill\": \"Awareness\", \"Spec\":\"Death\"},{\"Skill\": \"Larceny\", \"Spec\":\"Forgery\"}]', '[\"Auspex\", \"Oblivion\"]', 1, 0, '[{\"Name\": \"Influence\", \"Value\":1, \"Extra\": \"Medical Community\"}]', '[{\"Name\": \"Prey Exclusion\", \"Value\":1, \"Extra\": \"Healthy Mortals\"}]', 'VtM Player\'s Guide; PG 108'),
(19, 'Montero', '', '[{\"Skill\": \"Leadership\", \"Spec\":\"Hunting Pack\"},{\"Skill\": \"Stealth\", \"Spec\":\"Stakeout\"}]', '[\"Dominate\", \"Obfuscate\"]', -1, 0, '[{\"Name\": \"Retainer\", \"Value\":2, \"Extra\": \"\"}]', '[]', 'VtM Player\'s Guide; PG 108'),
(20, 'Pursuer', '', '[{\"Skill\": \"Investigation\", \"Spec\":\"Profiling\"},{\"Skill\": \"Stealth\", \"Spec\":\"Shadowing\"}]', '[\"Auspex\", \"Animalism\"]', -1, 0, '[{\"Name\": \"Bloodhound\", \"Value\":1, \"Extra\": \"\"}, {\"Name\": \"Contacts\", \"Value\":1, \"Extra\": \"An individual amongst the morally flexible habitates of your hunting ground\"}]', '[]', 'VtM Player\'s Guide; PG 108'),
(21, 'Trapdoor (Retainer)', '', '[{\"Skill\": \"Persuasion\", \"Spec\":\"Marketing\"},{\"Skill\": \"Stealth\", \"Spec\":\"Ambushes or Traps\"}]', '[\"Protean\", \"Obfuscate\"]', 0, 0, '[{\"Name\": \"Haven\", \"Value\":1, \"Extra\": \"Trapdoor Haven - Retainer\"},{\"Name\": \"Retainer\", \"Value\":1, \"Extra\": \"\"}]', '[{\"Name\": \"Haven - Creepy\", \"Value\":1, \"Extra\": \"Trapdoor Haven - Retainer\"}]', 'VtM Player\'s Guide; PG 109'),
(22, 'Trapdoor (Herd)', '', '[{\"Skill\": \"Persuasion\", \"Spec\":\"Marketing\"},{\"Skill\": \"Stealth\", \"Spec\":\"Ambushes or Traps\"}]', '[\"Protean\", \"Obfuscate\"]', 0, 0, '[{\"Name\": \"Haven\", \"Value\":1, \"Extra\": \"Trapdoor Haven - Herd\"},{\"Name\": \"Herd\", \"Value\":1, \"Extra\": \"\"}]', '[{\"Name\": \"Haven - Creepy\", \"Value\":1, \"Extra\": \"Trapdoor Haven - Herd\"}]', 'VtM Player\'s Guide; PG 109'),
(23, 'Trapdoor (Haven)', '', '[{\"Skill\": \"Persuasion\", \"Spec\":\"Marketing\"},{\"Skill\": \"Stealth\", \"Spec\":\"Ambushes or Traps\"}]', '[\"Protean\", \"Obfuscate\"]', 0, 0, '[{\"Name\": \"Haven\", \"Value\":2, \"Extra\": \"Trapdoor Haven - Haven\"}]', '[{\"Name\": \"Haven - Creepy\", \"Value\":1, \"Extra\": \"Trapdoor Haven - Haven\"}]', 'VtM Player\'s Guide; PG 109'),
(24, 'Roadside Killer', '', '[{\"Skill\": \"Survival\", \"Spec\":\"The Road\"},{\"Skill\": \"Investigation\", \"Spec\":\"Vampire Cant\"}]', '[\"Protean\", \"Fortitude\"]', 0, 0, '[{\"Name\": \"Herd\", \"Value\":2, \"Extra\": \"Migrating\"}]', '[{\"Name\": \"Prey Exclusion\", \"Value\":1, \"Extra\": \"Locals\"}]', 'VtM Streets; PG 76');

-- --------------------------------------------------------

--
-- Table structure for table `vtm5_thinbloodflaws`
--

CREATE TABLE `vtm5_thinbloodflaws` (
  `ID` int(2) NOT NULL,
  `Name` tinytext DEFAULT NULL,
  `Description` text NOT NULL,
  `Reference` tinytext DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Dumping data for table `vtm5_thinbloodflaws`
--

INSERT INTO `vtm5_thinbloodflaws` (`ID`, `Name`, `Description`, `Reference`) VALUES
(1, 'Baby Teeth', 'Never developed fangs, or grew ones that were not sharp enough to break the skin. ', 'VtM Corebook; PG 182'),
(2, 'Bestial Temper', 'Frenzy test as normal vampire rules ', 'VtM Corebook; PG 182'),
(3, 'Branded by the Camarilla', 'An unhealable and painful brand given by the Camarilla to know what they are. Can take Camarilla Contact with this Flaw. ', 'VtM Corebook; PG 182'),
(4, 'Clan Curse', 'Cursed by the bane of a clan. Bane Severity becomes 1. Can only take Banu Haqim, Gangrel, or Brujah Bane if they have Bestial Temper and the Tremere Bane if they have Catenating Blood ', 'VtM Corebook; PG 183'),
(5, 'Dead Flesh', 'Medical inspections will report them as deceased and take a one-die penalty to face-to-face Social tests with a mortal. Cannot take Lifelike with this Flaw. ', 'VtM Corebook; PG 183'),
(6, 'Mortal Frailty', 'Mend like a mortal, unable to rouse the blood. Cannot take Vampiric Resilience with this Flaw. ', 'VtM Corebook; PG 183'),
(7, 'Shunned by the Anarchs', 'They\'ve done something and the Anarch shun them, more likely to throw them to the Camarilla than help. Cannot take Anarch Comrades with this Flaw. ', 'VtM Corebook; PG 183'),
(8, 'Vitae Dependancy', 'Must slake one hunger of vampire vitae each week else they\'ll lose access to all their vampiric powers. ', 'VtM Corebook; PG 183'),
(9, 'Heliophobia', 'Fear sunlight as if a full vampire, terror Frenzy from sunlight', 'VtM Player\'s Guide; PG 135'),
(10, 'Night Terrors', 'Once per session suffer from night terrors and receive a one-die penalty for all actions for the rest of the scene', 'VtM Player\'s Guide; PG 135'),
(11, 'Plague Bearers', 'Still susceptible to mortal illnesses, whenever they feed they have a chance to catch a sickness by rolling a die and it lands on \"1\". Mortal medicine does not heal you, only slaking from a healthy immune system to Hunger 0 does', 'VtM Player\'s Guide; PG 135'),
(12, 'Sloppy Drinker', 'When feeding make a Dex + Medicine test against a Difficulty equal to the amount of Hunger slaked. On a failure, the wound is too ragged to close and the victim may bleed out from the Masquerade-threatening wound', 'VtM Player\'s Guide; PG 135'),
(14, 'Supernatural Tell', 'Something about them makes them easy to spot as supernatural creatures. Lose two dice from Stealth pools and similar against other supernatural creatures', 'VtM Player\'s Guide; PG 135'),
(15, 'Twilight Presence', 'Mortals don\'t want to be around them and even other Kindred find them more unpleasant than other thin-bloods. Lose one die from Social pools involving others except for other thin-bloods who can adjust to their strange demeanor', 'VtM Player\'s Guide; PG 135'),
(16, 'Unending Hunger', 'When feeding in a scene, slake one Hunger less, this only applies once per scene', 'VtM Player\'s Guide; PG 135');

-- --------------------------------------------------------

--
-- Table structure for table `vtm5_thinbloodmerits`
--

CREATE TABLE `vtm5_thinbloodmerits` (
  `ID` int(2) NOT NULL,
  `Name` tinytext DEFAULT NULL,
  `Description` text NOT NULL,
  `Reference` tinytext DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Dumping data for table `vtm5_thinbloodmerits`
--

INSERT INTO `vtm5_thinbloodmerits` (`ID`, `Name`, `Description`, `Reference`) VALUES
(1, 'Anarch Comrades', 'Befriended an Anarch group, and act as a one-dot Anarch Mawla. ', 'VtM Corebook; PG 183'),
(2, 'Camarilla Contacts', 'Caught the attention of someone within the Camarilla, acts as a one-dot Camarilla Mawla. ', 'VtM Corebook; PG 183'),
(3, 'Catenating Blood', 'Can create Blood Bonds and embrace other thin-bloods. ', 'VtM Corebook; PG 183'),
(4, 'Day Drinker', 'Able to walk in the sun. Sunlight halves their Health Tracker (rounded up) and removes all vampiric abilities. ', 'VtM Corebook; PG 183'),
(5, 'Discipline Affinity', 'Natural ability for one Discipline. Gain one dot and can retain additional levels at the experience cost of out-of-clan. Consuming matching resonance does not reward them with extra temporary dots. ', 'VtM Corebook; PG 184'),
(6, 'Lifelike', 'Has a heartbeat, can eat food, and enjoy sexual activities. Most medical checks reveal nothing, as long as it\'s during the night. ', 'VtM Corebook; PG 184'),
(7, 'Thinblood Alchemist', 'Gain one dot and one formula of Thin-blood Alchemy. ', 'VtM Corebook; PG 184'),
(8, 'Vampiric Resilience', 'Take damage like a regular vampire', 'VtM Corebook; PG 184'),
(9, 'Abhorrent Blood', 'With Blood so disgusting any vampire who attempts to drink from them must spend two points of Willpower each turn. Mortals and Thin-blood Alchemy are not affected by this.', 'VtM Player\'s Guide; PG 135'),
(10, 'Faith Proof', 'They are too close to mortality for True Faith to affect them', 'VtM Player\'s Guide; PG 136'),
(11, 'Low Appetite', 'When waking up at sunset with Hunger 0 or 1, roll two dice on the Rouse Check and take the highest between the two', 'VtM Player\'s Guide; PG 136'),
(12, 'Lucid Dreamer', 'Once per session, they can receive a clue from the previous night\'s memories or a hint about the story', 'VtM Player\'s Guide; PG 136'),
(13, 'Mortality\'s Mein', 'Appearing more mortal than most vampires their vampiric nature cannot be detected through auras. In addition, receive two dice in any attempt to make yourself appear mortal in other methods such as makeup', 'VtM Player\'s Guide; PG 136'),
(14, 'Swift Feeder', 'Able to slake one Hunger in one turn as well as lick the wound closed. This can only be used once per scene.', 'VtM Player\'s Guide; PG 136');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `api_keys`
--
ALTER TABLE `api_keys`
  ADD PRIMARY KEY (`api_key`);

--
-- Indexes for table `characters`
--
ALTER TABLE `characters`
  ADD PRIMARY KEY (`uuid`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`uuid`);

--
-- Indexes for table `vtm5_caitiffflaws`
--
ALTER TABLE `vtm5_caitiffflaws`
  ADD PRIMARY KEY (`ID`),
  ADD KEY `vfID` (`ID`);

--
-- Indexes for table `vtm5_caitiffmerits`
--
ALTER TABLE `vtm5_caitiffmerits`
  ADD PRIMARY KEY (`ID`),
  ADD KEY `vmID` (`ID`);

--
-- Indexes for table `vtm5_clan`
--
ALTER TABLE `vtm5_clan`
  ADD PRIMARY KEY (`ID`),
  ADD KEY `clanID` (`ID`);

--
-- Indexes for table `vtm5_clandisciplinejunction`
--
ALTER TABLE `vtm5_clandisciplinejunction`
  ADD PRIMARY KEY (`ID`),
  ADD KEY `disciplineJunctionID` (`ID`),
  ADD KEY `disciplineID` (`disciplineID`),
  ADD KEY `clanID` (`clanID`);

--
-- Indexes for table `vtm5_disciplinegroups`
--
ALTER TABLE `vtm5_disciplinegroups`
  ADD PRIMARY KEY (`ID`),
  ADD KEY `dgID` (`ID`);

--
-- Indexes for table `vtm5_disciplinepowers`
--
ALTER TABLE `vtm5_disciplinepowers`
  ADD PRIMARY KEY (`ID`),
  ADD KEY `dpID` (`ID`),
  ADD KEY `DisciplineGroup` (`DisciplineGroup`);

--
-- Indexes for table `vtm5_extradisciplinegroups`
--
ALTER TABLE `vtm5_extradisciplinegroups`
  ADD PRIMARY KEY (`ID`),
  ADD KEY `edgID` (`ID`),
  ADD KEY `ConnectedDiscipline` (`ConnectedDiscipline`);

--
-- Indexes for table `vtm5_extradisciplinepowers`
--
ALTER TABLE `vtm5_extradisciplinepowers`
  ADD PRIMARY KEY (`ID`),
  ADD KEY `edpID` (`ID`),
  ADD KEY `ExtraDisciplineGroup` (`ExtraDisciplineGroup`);

--
-- Indexes for table `vtm5_flaws`
--
ALTER TABLE `vtm5_flaws`
  ADD PRIMARY KEY (`ID`),
  ADD KEY `vfID` (`ID`);

--
-- Indexes for table `vtm5_havenflaws`
--
ALTER TABLE `vtm5_havenflaws`
  ADD PRIMARY KEY (`ID`),
  ADD KEY `hfID` (`ID`);

--
-- Indexes for table `vtm5_havenmerits`
--
ALTER TABLE `vtm5_havenmerits`
  ADD PRIMARY KEY (`ID`),
  ADD KEY `hmID` (`ID`);

--
-- Indexes for table `vtm5_merits`
--
ALTER TABLE `vtm5_merits`
  ADD PRIMARY KEY (`ID`),
  ADD KEY `vmID` (`ID`);

--
-- Indexes for table `vtm5_predatortype`
--
ALTER TABLE `vtm5_predatortype`
  ADD PRIMARY KEY (`ID`),
  ADD KEY `id` (`ID`);

--
-- Indexes for table `vtm5_thinbloodflaws`
--
ALTER TABLE `vtm5_thinbloodflaws`
  ADD PRIMARY KEY (`ID`),
  ADD KEY `tbfID` (`ID`);

--
-- Indexes for table `vtm5_thinbloodmerits`
--
ALTER TABLE `vtm5_thinbloodmerits`
  ADD PRIMARY KEY (`ID`),
  ADD KEY `tbmID` (`ID`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `vtm5_caitiffflaws`
--
ALTER TABLE `vtm5_caitiffflaws`
  MODIFY `ID` int(2) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=58;

--
-- AUTO_INCREMENT for table `vtm5_caitiffmerits`
--
ALTER TABLE `vtm5_caitiffmerits`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=180;

--
-- AUTO_INCREMENT for table `vtm5_clan`
--
ALTER TABLE `vtm5_clan`
  MODIFY `ID` int(2) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;

--
-- AUTO_INCREMENT for table `vtm5_clandisciplinejunction`
--
ALTER TABLE `vtm5_clandisciplinejunction`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=55;

--
-- AUTO_INCREMENT for table `vtm5_disciplinepowers`
--
ALTER TABLE `vtm5_disciplinepowers`
  MODIFY `ID` int(3) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=217;

--
-- AUTO_INCREMENT for table `vtm5_flaws`
--
ALTER TABLE `vtm5_flaws`
  MODIFY `ID` int(2) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=58;

--
-- AUTO_INCREMENT for table `vtm5_havenflaws`
--
ALTER TABLE `vtm5_havenflaws`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `vtm5_havenmerits`
--
ALTER TABLE `vtm5_havenmerits`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;

--
-- AUTO_INCREMENT for table `vtm5_merits`
--
ALTER TABLE `vtm5_merits`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=181;

--
-- AUTO_INCREMENT for table `vtm5_predatortype`
--
ALTER TABLE `vtm5_predatortype`
  MODIFY `ID` int(2) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=25;

--
-- AUTO_INCREMENT for table `vtm5_thinbloodflaws`
--
ALTER TABLE `vtm5_thinbloodflaws`
  MODIFY `ID` int(2) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;

--
-- AUTO_INCREMENT for table `vtm5_thinbloodmerits`
--
ALTER TABLE `vtm5_thinbloodmerits`
  MODIFY `ID` int(2) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `vtm5_clandisciplinejunction`
--
ALTER TABLE `vtm5_clandisciplinejunction`
  ADD CONSTRAINT `clanDisciplineJunction_ibfk_1` FOREIGN KEY (`clanID`) REFERENCES `vtm5_clan` (`ID`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `clanDisciplineJunction_ibfk_2` FOREIGN KEY (`disciplineID`) REFERENCES `vtm5_disciplinegroups` (`ID`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `vtm5_disciplinepowers`
--
ALTER TABLE `vtm5_disciplinepowers`
  ADD CONSTRAINT `disciplinePowers_ibfk_1` FOREIGN KEY (`DisciplineGroup`) REFERENCES `vtm5_disciplinegroups` (`ID`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `vtm5_extradisciplinegroups`
--
ALTER TABLE `vtm5_extradisciplinegroups`
  ADD CONSTRAINT `extraDisciplineGroups_ibfk_1` FOREIGN KEY (`ConnectedDiscipline`) REFERENCES `vtm5_disciplinegroups` (`ID`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `vtm5_extradisciplinepowers`
--
ALTER TABLE `vtm5_extradisciplinepowers`
  ADD CONSTRAINT `extraDisciplinePowers_ibfk_1` FOREIGN KEY (`ExtraDisciplineGroup`) REFERENCES `vtm5_extradisciplinegroups` (`ID`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
