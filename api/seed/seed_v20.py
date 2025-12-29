from app import db
from models import V20_Clans, V20_Backgrounds, V20_Nature, V20_Discipline_Powers, V20_Merits, V20_Flaws, V20_Disciplines, V20_Magic_Types, V20_Sorcery_Paths


def seed_v20_clan():
    clans_data = [
        {
            "name": "Caitiff",
            "weakness": "Because of their social stigma, they cannot take Status at character creation. Until they establish themselves in a domain or group, they suffer +2 difficulty on all Social rolls with non-Caitiff. Their childer are also Caitiff.",
            "information": "Clanless vampires shunned and distrusted by most of Kindred society.",
            "reference": "Vampire The Masquerade 20th Anniversary Edition, Core Rulebook",
        },
        {
            "name": "Assamite",
            "weakness": "When they taste Kindred vitae, they must roll Self-Control or Instincts (difficulty 3 + blood points taken). Failure causes addiction, and future failures when exposed to vitae trigger frenzy to drink more.",
            "information": "Judgment-focused warriors whose blood resonates dangerously with vampiric vitae.",
            "reference": "Vampire The Masquerade 20th Anniversary Edition, Core Rulebook, p428",
        },
        {
            "name": "Brujah",
            "weakness": "All rolls to resist or guide frenzy are at +2 difficulty, and they may not spend Willpower to avoid frenzy (only to end it once begun).",
            "information": "Passionate warriors and philosophers whose tempers are infamously volatile.",
            "reference": "Vampire The Masquerade 20th Anniversary Edition, Core Rulebook, p50",
        },
        {
            "name": "Followers of Set",
            "weakness": "Suffer two additional health levels of damage from sunlight and lose one die from dice pools for actions taken in bright light.",
            "information": "Serpentine corrupters bound to darkness and spiritually harmed by illumination.",
            "reference": "Vampire The Masquerade 20th Anniversary Edition, Core Rulebook, p52",
        },
        {
            "name": "Gangrel",
            "weakness": "Each time they frenzy, they gain a temporary animalistic trait, which may eventually become permanent.",
            "information": "Bestial nomads whose inner Beast steadily marks their bodies and behavior.",
            "reference": "Vampire The Masquerade 20th Anniversary Edition, Core Rulebook, p54",
        },
        {
            "name": "Giovanni",
            "weakness": "Their Kiss causes excruciating pain and inflicts double the usual damage on mortal vessels when feeding.",
            "information": "Necromantic clan whose feeding is agonizing and often fatal if not carefully managed.",
            "reference": "Vampire The Masquerade 20th Anniversary Edition, Core Rulebook, p56",
        },
        {
            "name": "Lasombra",
            "weakness": "They cast no reflection in mirrors, water, or any reflective surface.",
            "information": "Shadow-wielding nobles whose lack of reflection marks their alien nature.",
            "reference": "Vampire The Masquerade 20th Anniversary Edition, Core Rulebook, p58",
        },
        {
            "name": "Malkavian",
            "weakness": "Each has a single permanent, incurable derangement, though they may gain and lose additional ones.",
            "information": "Mad seers whose fractured minds conceal terrifying insight.",
            "reference": "Vampire The Masquerade 20th Anniversary Edition, Core Rulebook, p60",
        },
        {
            "name": "Nosferatu",
            "weakness": "Their Appearance is always 0 and may never be increased; they automatically fail Appearance-based rolls.",
            "information": "Hideous but resourceful vampires who lurk in society’s forgotten places.",
            "reference": "Vampire The Masquerade 20th Anniversary Edition, Core Rulebook, p62",
        },
        {
            "name": "Ravnos",
            "weakness": "Each has a personal vice. When given a chance to indulge it, they must succeed on a Self-Control or Instincts roll (difficulty 6) or succumb.",
            "information": "Tricksters driven by compulsive vices such as theft, lies, or cruelty.",
            "reference": "Vampire The Masquerade 20th Anniversary Edition, Core Rulebook, p64",
        },
        {
            "name": "Toreador",
            "weakness": "When faced with something truly beautiful or inspiring, they must roll Self-Control or Instincts (difficulty 6) or become entranced and unable to act except to remain involved with the source of fascination.",
            "information": "Aesthetic-obsessed vampires who can be rendered helpless by beauty.",
            "reference": "Vampire The Masquerade 20th Anniversary Edition, Core Rulebook, p66",
        },
        {
            "name": "Tremere",
            "weakness": "They become blood bound after only two drinks from another vampire; the first drink counts as if they had taken two.",
            "information": "Hierarchical blood sorcerers whose weakness enforces loyalty through the blood bond.",
            "reference": "Vampire The Masquerade 20th Anniversary Edition, Core Rulebook, p68",
        },
        {
            "name": "Tzimisce",
            "weakness": "Must rest near at least two handfuls of native soil. Each night without it halves all dice pools cumulatively until only one die remains, persisting until they rest a full day in their soil.",
            "information": "Territorial flesh-shapers mystically bound to the land of their origin.",
            "reference": "Vampire The Masquerade 20th Anniversary Edition, Core Rulebook, p70",
        },
        {
            "name": "Ventrue",
            "weakness": "Can feed only on a specific, chosen type of mortal blood. Other blood provides no sustenance and is vomited up.",
            "information": "Patrician clan whose refined tastes severely restrict their feeding options.",
            "reference": "Vampire The Masquerade 20th Anniversary Edition, Core Rulebook, p72",
        },
        {
            "name": "Ahrimanes",
            "weakness": "Their blood is inert: they cannot Embrace, create blood bonds, or make ghouls.",
            "information": "Spirit-bound outcasts whose vitae no longer functions like normal vampiric blood.",
            "reference": "Vampire The Masquerade 20th Anniversary Edition, Core Rulebook, p414",
        },
        {
            "name": "Anda",
            "weakness": "Gain animal features from frenzy once every other frenzy and suffer halved dice pools for each day after the third spent sleeping within the same one-mile area.",
            "information": "Nomadic hunters tied to constant travel, punished for remaining in one place too long.",
            "reference": "Vampire The Masquerade 20th Anniversary Edition, Core Rulebook, p416",
        },
        {
            "name": "Baali",
            "weakness": "Cannot bear to look upon or handle objects of faith; such items burn them, and hindering or damage effects from True Faith are doubled.",
            "information": "Infernalists repulsed and harmed by the trappings of genuine faith.",
            "reference": "Vampire The Masquerade 20th Anniversary Edition, Core Rulebook, p394",
        },
        {
            "name": "Blood Brothers",
            "weakness": "Cannot Embrace. When one suffers a wound penalty, all members of the circle suffer the same penalty for the next turn (only the highest penalty applies).",
            "information": "Circle-based Frankensteins who literally share each others’ pain.",
            "reference": "Vampire The Masquerade 20th Anniversary Edition, Core Rulebook, p396",
        },
        {
            "name": "Cappadocians",
            "weakness": "Exhibit a deathly pallor that worsens with age, eventually resembling withered corpses.",
            "information": "Death-obsessed scholars whose bodies increasingly mimic the grave.",
            "reference": "Vampire The Masquerade 20th Anniversary Edition, Core Rulebook, p418",
        },
        {
            "name": "Children of Osiris",
            "weakness": "They retain the weakness of their original clan.",
            "information": "Redeemed vampires who follow Osirian mysteries and temper their curse through Bardo.",
            "reference": "Vampire The Masquerade 20th Anniversary Edition, Core Rulebook, p420",
        },
        {
            "name": "Daughters of Cacophony",
            "weakness": "Constantly hear music in their minds. All Perception rolls are at +2 difficulty, and they may not have Alertness above 3.",
            "information": "Haunted singers guided and distracted by an unending inner song.",
            "reference": "Vampire The Masquerade 20th Anniversary Edition, Core Rulebook, p398",
        },
        {
            "name": "Gargoyles",
            "weakness": "Hideous appearance results in Appearance 0. They are also highly susceptible to mind control, treating their Willpower as 2 lower when resisting such powers.",
            "information": "Constructed stone-like vampires crafted as slaves and soldiers by the Tremere.",
            "reference": "Vampire The Masquerade 20th Anniversary Edition, Core Rulebook, p400",
        },
        {
            "name": "Harbingers of Skulls",
            "weakness": "Look like shriveled corpses with Appearance 0 and automatically fail Appearance rolls.",
            "information": "Macabre returnees from the Cappadocian line, outwardly corpse-like in all stages.",
            "reference": "Vampire The Masquerade 20th Anniversary Edition, Core Rulebook, p402",
        },
        {
            "name": "Kiasyd",
            "weakness": "Allergic to iron. Touching iron requires an immediate roll to avoid frenzy; weapons of cold iron inflict aggravated damage.",
            "information": "Fae-tainted occultists with an otherworldly fragility to iron.",
            "reference": "Vampire The Masquerade 20th Anniversary Edition, Core Rulebook, p404",
        },
        {
            "name": "Lamia",
            "weakness": "Their bite can transmit a fatal, plague-like disease to mortals who fail a Stamina roll, and vampires drinking their blood become carriers until the Lamia vitae is gone.",
            "information": "Deadly bodyguards of Lilith whose Kiss can spread a virulent pox.",
            "reference": "Vampire The Masquerade 20th Anniversary Edition, Core Rulebook, p423",
        },
        {
            "name": "Lhiannan",
            "weakness": "Easily recognized as inhuman with Auspex (−2 difficulty). When away from their territory, they lose one die from all dice pools per week until returning, where pools recover after a few hours.",
            "information": "Territory-bound nature spirits in vampiric form, unsettled when far from their lands.",
            "reference": "Vampire The Masquerade 20th Anniversary Edition, Core Rulebook, p424",
        },
        {
            "name": "Nagaraja",
            "weakness": "Must consume raw flesh as well as blood. Each night without flesh, they lose one die from all Physical dice pools. Eating flesh restores these dice; taking flesh deals unsoakable lethal damage to victims.",
            "information": "Cannibalistic necromancers sustained by flesh as much as vitae.",
            "reference": "Vampire The Masquerade 20th Anniversary Edition, Core Rulebook, p406",
        },
        {
            "name": "Noiad",
            "weakness": "Cannot drink from animals, only mortals or Cainites.",
            "information": "Tribal protectors mystically restricted to feeding on chosen people and other vampires.",
            "reference": "Vampire The Masquerade 20th Anniversary Edition, Core Rulebook, p426",
        },
        {
            "name": "Salubri",
            "weakness": "Lose one Willpower point when feeding on unwilling vessels.",
            "information": "Reluctant feeders whose ethics and curse both discourage predation on the unwilling.",
            "reference": "Vampire The Masquerade 20th Anniversary Edition, Core Rulebook, p408",
        },
        {
            "name": "Samedi",
            "weakness": "Rotting, corpse-like bodies with Appearance 0; they automatically fail Appearance rolls.",
            "information": "Putrescent vampires whose decayed bodies repel the living.",
            "reference": "Vampire The Masquerade 20th Anniversary Edition, Core Rulebook, p410",
        },
        {
            "name": "True Brujah",
            "weakness": "+2 difficulty on all Conscience and Conviction rolls (max 10), and traits like Conscience, Conviction, Humanity, and Paths of Enlightenment cost double experience.",
            "information": "Emotionally numb temporal scholars whose morality erodes and is hard to maintain.",
            "reference": "Vampire The Masquerade 20th Anniversary Edition, Core Rulebook, p412",
        },
        {
            "name": "Assamite Antitribu",
            "weakness": "Share the pre-curse weakness: when drinking vampire blood, must roll Self-Control or Instincts. Failure causes addiction and can trigger frenzies to drink more when opportunities arise.",
            "information": "Sabbat-aligned judges whose old addiction to Kindred vitae never faded.",
            "reference": "Vampire The Masquerade 20th Anniversary Edition, Core Rulebook, p429",
        },
        {
            "name": "Brujah Antitribu",
            "weakness": "Same as Clan Brujah: all frenzy difficulties are increased by two, to a maximum of 10.",
            "information": "Rage-embracing Sabbat shock troops reveling in their violent tempers.",
            "reference": "Vampire The Masquerade 20th Anniversary Edition, Core Rulebook, p429",
        },
        {
            "name": "City Gangrel",
            "weakness": "Same as Gangrel: each frenzy grants a temporary animal feature, typically resembling urban animals. Mechanical impact is Storyteller’s call.",
            "information": "City-adapted Gangrel whose Beasts echo rats, dogs, pigeons, and other urban fauna.",
            "reference": "Vampire The Masquerade 20th Anniversary Edition, Core Rulebook, p429",
        },
        {
            "name": "Country Gangrel",
            "weakness": "Same as main Gangrel: each frenzy grants a temporary animal feature whose impact is Storyteller-determined.",
            "information": "Rural Sabbat hunters with increasingly feral, animalistic traits.",
            "reference": "Vampire The Masquerade 20th Anniversary Edition, Core Rulebook, p430",
        },
        {
            "name": "Malkavian Antitribu",
            "weakness": "Begin play with a derangement that can never be overcome.",
            "information": "Sabbat lunatics whose incurable insanity often manifests in violent ways.",
            "reference": "Vampire The Masquerade 20th Anniversary Edition, Core Rulebook, p430",
        },
        {
            "name": "Nosferatu Antitribu",
            "weakness": "As with Camarilla Nosferatu, they have Appearance 0 and can never improve it.",
            "information": "Equally hideous Sabbat sewer lords and ambushers.",
            "reference": "Vampire The Masquerade 20th Anniversary Edition, Core Rulebook, p430",
        },
        {
            "name": "Panders",
            "weakness": "No special clan curse, but may not start lower than 9th Generation.",
            "information": "Ambitious, clanless Sabbat vampires striving for recognition and power.",
            "reference": "Vampire The Masquerade 20th Anniversary Edition, Core Rulebook, p431",
        },
        {
            "name": "Ravnos Antitribu",
            "weakness": "Like their parent clan, each has a personal vice and must succeed on a Self-Control or Instincts roll (difficulty 6) to resist indulging it.",
            "information": "Sabbat con artists hard-wired to break taboos and pursue vice.",
            "reference": "Vampire The Masquerade 20th Anniversary Edition, Core Rulebook, p431",
        },
        {
            "name": "Salubri Antitribu",
            "weakness": "Must feed from blood taken by force, preferably in battle; peaceful feeding offers no nourishment. They also have limited starting Generations (10th–12th).",
            "information": "Martial cousins of the Salubri who must drink the blood of defeated foes.",
            "reference": "Vampire The Masquerade 20th Anniversary Edition, Core Rulebook, p431",
        },
        {
            "name": "Serpents of the Light",
            "weakness": "As Followers of Set: suffer two extra health levels of sunlight damage and a one-die penalty to all rolls in bright light.",
            "information": "Caribbean offshoot of the Setites whose curse mirrors their progenitors’ hatred of light.",
            "reference": "Vampire The Masquerade 20th Anniversary Edition, Core Rulebook",
        },
        {
            "name": "Toreador Antitribu",
            "weakness": "When given an opportunity to inflict emotional or physical pain, must roll Self-Control or Instincts (difficulty 6) or spend Willpower; on failure, they must indulge their cruelty.",
            "information": "Perverse aesthetes whose fascination with beauty has twisted into sadism.",
            "reference": "Vampire The Masquerade 20th Anniversary Edition, Core Rulebook",
        },
        {
            "name": "Tremere Antitribu",
            "weakness": "Marked in their very presence as traitors, making them identifiable to Tremere. They also gain +1 to all Vinculum rolls.",
            "information": "Hunted Sabbat sorcerers whose betrayal is mystically obvious to their former clan.",
            "reference": "Vampire The Masquerade 20th Anniversary Edition, Core Rulebook",
        },
        {
            "name": "Ventrue Antitribu",
            "weakness": "Share the same feeding restriction as Ventrue: can only feed from one specific type of mortal blood, with all others providing no nourishment.",
            "information": "Sabbat nobles mirroring the refined but restrictive feeding of their Camarilla kin.",
            "reference": "Vampire The Masquerade 20th Anniversary Edition, Core Rulebook",
        },
        {
            "name": "Assamite Sorcerers",
            "weakness": "Easier to perceive supernaturally: any power used to sense them is at −2 difficulty, and attempts to pierce their concealment operate as if the opposing perception power were one level higher.",
            "information": "Long-practicing mystics whose blood shines like a beacon to supernatural senses.",
            "reference": "Vampire The Masquerade 20th Anniversary Edition, Core Rulebook, p433",
        },
        {
            "name": "Assamite Viziers",
            "weakness": "Each has an Obsessive-Compulsive derangement tied to their highest-rated intellectual or creative Ability, shifting if their focus changes.",
            "information": "Hyper-focused artisans and scholars consumed by their chosen craft or pursuit.",
            "reference": "Vampire The Masquerade 20th Anniversary Edition, Core Rulebook, p434",
        },
        {
            "name": "Daitya",
            "weakness": "Share the Followers of Set weakness: suffer two additional health levels of sunlight damage and a one-die penalty to all rolls in bright light.",
            "information": "Ascetic Setite offshoots embracing a more contemplative, philosophical path.",
            "reference": "Vampire The Masquerade 20th Anniversary Edition, Core Rulebook, p434",
        },
        {
            "name": "Tlacique",
            "weakness": "Like Followers of Set, suffer two additional health levels of damage from sunlight and a one-die penalty to all rolls in bright light.",
            "information": "Predatory jungle Setites whose curse ties them to the same hatred of light.",
            "reference": "Vampire The Masquerade 20th Anniversary Edition, Core Rulebook, p435",
        },
        {
            "name": "Warrior Setites",
            "weakness": "Share the Followers of Set weakness: extra sunlight damage and a one-die penalty to all rolls in bright light.",
            "information": "Militant arm of the Setites, embracing the same vulnerability to light as their kin.",
            "reference": "Vampire The Masquerade 20th Anniversary Edition, Core Rulebook, p435",
        },
        {
            "name": "Mariners",
            "weakness": "Gain animal features with each frenzy, but these resemble aquatic creatures such as fish, cephalopods, or other sea life; their alien nature should influence the mechanical impact.",
            "information": "Sea-bound Gangrel whose Beasts manifest as oceanic mutations.",
            "reference": "Vampire The Masquerade 20th Anniversary Edition, Core Rulebook, p435",
        },
        {
            "name": "Gargoyle Scout",
            "weakness": "All wound penalties from injuries are doubled as their bodies revert toward stone; these penalties remain until they awaken after a day with no health levels marked.",
            "information": "Reconnaissance-focused Gargoyles whose stone bodies hamper them when injured.",
            "reference": "Lore of the Bloodlines, p.36",
        },
        {
            "name": "Gargoyle Sentinel",
            "weakness": "No additional specific clan weakness beyond that of Gargoyles in general.",
            "information": "Guardian Gargoyles designed to watch over chantries and havens, surprisingly sociable despite their appearance.",
            "reference": "Lore of the Bloodlines, p.36",
        },
        {
            "name": "Gargoyle Warrior",
            "weakness": "No additional specific clan weakness beyond that of Gargoyles in general.",
            "information": "Battle-built stone soldiers created to wage war on the Tremere’s enemies.",
            "reference": "Lore of the Bloodlines, p.36",
        },
        {
            "name": "Angelis Ater",
            "weakness": "Share the Lasombra weakness of casting no reflection. House rule: if Obtenebration is taken as a third Discipline, they also gain the Baali curse regarding objects of faith.",
            "information": "Lasombra subsect steeped in deeper darkness, sometimes bearing an infernal taint.",
            "reference": "Vampire The Masquerade 20th Anniversary Edition, Core Rulebook, p436",
        },
        {
            "name": "Lasombra Antitribu",
            "weakness": "Do not cast reflections like all Lasombra and are hunted relentlessly by the Sabbat when discovered.",
            "information": "Defectors of the Lasombra clan forced into constant hiding from their former sect.",
            "reference": "Vampire The Masquerade 20th Anniversary Edition, Core Rulebook, p436",
        },
        {
            "name": "Dominate Malkavians",
            "weakness": "As with all Malkavians, they possess at least one permanent, incurable derangement.",
            "information": "A quieter, more subtle branch of Malkavians whose minds remain irretrievably broken.",
            "reference": "Vampire The Masquerade 20th Anniversary Edition, Core Rulebook, p437",
        },
        {
            "name": "Brahman",
            "weakness": "Share the Ravnos weakness: each has a preferred vice and must succeed on a Self-Control or Instinct roll (difficulty 6) to resist indulging it.",
            "information": "Mystically inclined Ravnos who often express their vice through spiritual scams and séances.",
            "reference": "Vampire The Masquerade 20th Anniversary Edition, Core Rulebook, p437",
        },
        {
            "name": "Wu Zao",
            "weakness": "Each must select an arcane or scholarly focus. When presented with an opportunity to learn more about it, they must roll Willpower (difficulty 6) to avoid obsessively pursuing that lead.",
            "information": "Scholar-sages of the Salubri line whose curiosity borders on compulsion.",
            "reference": "Vampire The Masquerade 20th Anniversary Edition, Core Rulebook, p438",
        },
        {
            "name": "Telyavelic Tremere",
            "weakness": "Weak against Christian symbols and True Faith; difficulties to resist frenzy are +2 when confronted by enemies using True Faith as a defense.",
            "information": "Pagan Tremere whose ties to old faiths leave them vulnerable to Christian holy symbols.",
            "reference": "Vampire The Masquerade 20th Anniversary Edition, Core Rulebook, p438",
        },
        {
            "name": "Koldun",
            "weakness": "As with all Tzimisce, must rest in native soil or suffer cumulative halving of dice pools every 24 hours until resting a full day in their earth.",
            "information": "Elemental sorcerers of the Tzimisce, deeply bound to their ancestral lands.",
            "reference": "Vampire The Masquerade 20th Anniversary Edition, Core Rulebook, p439",
        },
        {
            "name": "Old Clan Tzimisce",
            "weakness": "Share the Tzimisce requirement to sleep with at least two handfuls of soil from their homeland or suffer cumulative halving of dice pools every 24 hours.",
            "information": "Traditionalist Tzimisce predating the modern flesh-crafting practices of the clan.",
            "reference": "Vampire The Masquerade 20th Anniversary Edition, Core Rulebook, p439",
        },
        {
            "name": "Maeghar",
            "weakness": "Easier to recognize as otherworldly (−1 difficulty to notice). Vulnerable to cold iron, which inflicts aggravated damage and triggers checks for frenzy or Rötschreck. Must drain mortal blood into a clean container before drinking directly; this restriction does not apply when feeding from vampires.",
            "information": "Fae-marked Tal'Mahe'Ra who find human blood repulsive unless decanted and are especially vulnerable to cold iron.",
            "reference": "The Black Hand: A Guide To The Tal'Mahe'Ra, p167",
        },
    ]

    for c in clans_data:
        existing = V20_Clans.query.filter_by(name=c["name"]).first()
        if existing:
            continue

        clan = V20_Clans(
            name=c["name"],
            weakness=c["weakness"],
            information=c["information"],
            reference=c["reference"],
        )
        db.session.add(clan)


def seed_v20_nature():
    natures_data = [
        {"name": "Architect", "description": "You build something of lasting value."},
        {"name": "Autocrat", "description": "You need control."},
        {"name": "Bon Vivant", "description": "Unlife is for pleasure."},
        {"name": "Bravo", "description": "Might makes right."},
        {
            "name": "Capitalist",
            "description": "Why give it away for free when you can sell it?",
        },
        {"name": "Caregiver", "description": "Everyone needs nurturing."},
        {"name": "Celebrant", "description": "Your cause brings you joy."},
        {"name": "Chameleon", "description": "You manage to blend into any situation."},
        {"name": "Child", "description": "Won’t somebody be there for you?"},
        {"name": "Competitor", "description": "You must be the best."},
        {"name": "Conformist", "description": "You follow and assist."},
        {"name": "Conniver", "description": "Others exist for your benefit."},
        {
            "name": "Creep Show",
            "description": "Disgusting the straights makes you smile.",
        },
        {"name": "Curmudgeon", "description": "Everything has its flaws."},
        {"name": "Dabbler", "description": "It's always about the next big thing."},
        {"name": "Deviant", "description": "The status quo is for sheep."},
        {"name": "Director", "description": "You oversee what must be done."},
        {
            "name": "Enigma",
            "description": "Just when people think they've figured you out, you change the game.",
        },
        {
            "name": "Eye of the Storm",
            "description": "Chaos and havoc follow you, but it never gets to you.",
        },
        {"name": "Fanatic", "description": "The cause is all that matters."},
        {
            "name": "Gallant",
            "description": "You're not the showstopper: you're the show!",
        },
        {"name": "Guru", "description": "People find you spiritually compelling."},
        {"name": "Idealist", "description": "You believe in something greater."},
        {"name": "Judge", "description": "Your judgment will improve things."},
        {"name": "Loner", "description": "You make your own way."},
        {"name": "Martyr", "description": "You suffer for the greater good."},
        {"name": "Masochist", "description": "Pain reminds you that you still exist."},
        {"name": "Monster", "description": "You're Damned, so act like it!"},
        {"name": "Pedagogue", "description": "You save others through knowledge."},
        {
            "name": "Penitent",
            "description": "Unlife is a curse, and you must atone for it.",
        },
        {
            "name": "Perfectionist",
            "description": "You strive for an unattainable goal.",
        },
        {"name": "Rebel", "description": "You follow no one's rules."},
        {"name": "Rogue", "description": "It's all about you."},
        {"name": "Sadist", "description": "You live to cause pain."},
        {"name": "Scientist", "description": "Everything is a puzzle to solve."},
        {"name": "Sociopath", "description": "The inferior must be destroyed."},
        {"name": "Soldier", "description": "You follow orders, but in your own way."},
        {"name": "Survivor", "description": "Nothing can keep you down."},
        {"name": "Thrill-Seeker", "description": "The rush is all that matters."},
        {
            "name": "Traditionalist",
            "description": "As it has always been, so it must be.",
        },
        {"name": "Trickster", "description": "Laughter dims the pain."},
        {"name": "Visionary", "description": "Something exists beyond all this."},
    ]

    for n in natures_data:
        existing = V20_Nature.query.filter_by(name=n["name"]).first()
        if existing:
            continue

        nature = V20_Nature(
            name=n["name"],
            description=n["description"],
        )
        db.session.add(nature)


def seed_v20_backgrounds():
    backgrounds_data = [
        {
            "name": "Allies",
            "increments": 1,
            "maximum_value": 5,
            "cost_mult": 1,
            "description": "Mortal confederates, usually family or friends",
        },
        {
            "name": "Alternate Identity",
            "increments": 1,
            "maximum_value": 5,
            "cost_mult": 1,
            "description": "A false identity, complete with documentation",
        },
        {
            "name": "Black Hand Membership (Sabbat)",
            "increments": 1,
            "maximum_value": 5,
            "cost_mult": 1,
            "description": "The number of Black Hand members you can call on",
        },
        {
            "name": "Contacts",
            "increments": 1,
            "maximum_value": 5,
            "cost_mult": 1,
            "description": "The information sources the character possesses",
        },
        {
            "name": "Domain",
            "increments": 1,
            "maximum_value": 5,
            "cost_mult": 1,
            "description": "Feeding grounds acknowledged by Kindred society",
        },
        {
            "name": "Fame",
            "increments": 1,
            "maximum_value": 5,
            "cost_mult": 1,
            "description": "How well-known the character is among mortals",
        },
        {
            "name": "Generation",
            "increments": 1,
            "maximum_value": 5,
            "cost_mult": 1,
            "description": "How far removed from Caine the character is",
        },
        {
            "name": "Herd",
            "increments": 1,
            "maximum_value": 5,
            "cost_mult": 1,
            "description": "The vessels to which the character has free and safe access",
        },
        {
            "name": "Influence",
            "increments": 1,
            "maximum_value": 5,
            "cost_mult": 1,
            "description": "The character's political power within mortal society",
        },
        {
            "name": "Mentor",
            "increments": 1,
            "maximum_value": 5,
            "cost_mult": 1,
            "description": "The Kindred patron who advises and supports the character",
        },
        {
            "name": "Resources",
            "increments": 1,
            "maximum_value": 5,
            "cost_mult": 1,
            "description": "Wealth, belongings, and income",
        },
        {
            "name": "Retainers",
            "increments": 1,
            "maximum_value": 5,
            "cost_mult": 1,
            "description": "Followers, guards, and servants",
        },
        {
            "name": "Rituals (Sabbat)",
            "increments": 1,
            "maximum_value": 5,
            "cost_mult": 1,
            "description": "How many ritae the Cainite knows and can perform",
        },
        {
            "name": "Status",
            "increments": 1,
            "maximum_value": 5,
            "cost_mult": 1,
            "description": "The character's standing in undead society",
        },
    ]

    for b in backgrounds_data:
        existing = V20_Backgrounds.query.filter_by(name=b["name"]).first()
        if existing:
            continue

        background = V20_Backgrounds(
            name=b["name"],
            increments=b["increments"],
            max_value=b["maximum_value"],
            cost=b["cost_mult"],
            description=b["description"],
        )
        db.session.add(background)


def seed_magic_types():
    magic_types_data = [
        {
            "name": "Thaumaturgy",
            "description": "Blood magic practiced by the Tremere and their offshoots.",
        },
        {
            "name": "Necromancy",
            "description": "The dark art of communing with and commanding the dead.",
        },

    ]

    for mt in magic_types_data:
        existing = V20_Magic_Types.query.filter_by(name=mt["name"]).first()
        if existing:
            continue

        magic_type = V20_Magic_Types(
            name=mt["name"],
            description=mt["description"],
        )
        db.session.add(magic_type)


def seed_v20_disciplines():
    discipline_data = [
        {
            "name": "Animalism",
            "description": "Supernatural affinity with and control of animals.",
        },
        {
            "name": "Auspex",
            "description": "Heightened senses and psychic abilities.",
        },
        {
            "name": "Celerity",
            "description": "Supernatural speed and reflexes.",
        },
        {
            "name": "Chimerstry",
            "description": "Illusions and sensory manipulation.",
        },
        {
            "name": "Dementation",
            "description": "Inducing madness and manipulating minds.",
        },
        {
            "name": "Dominate",
            "description": "Mind control practiced through the piercing gaze",
        },
        {
            "name": "Fortitude",
            "description": "Supernatural resilience and toughness.",
        },
        {
            "name": "Necromancy",
            "description": "The dark art of communing with and commanding the dead.",
        },
        {
            "name": "Obfuscate",
            "description": "Stealth and concealment abilities.",
        },
        {
            "name": "Obtenebration",
            "description": "Manipulation of shadows and darkness.",
        },
        {
            "name": "Potence",
            "description": "Supernatural strength and power.",
        },
        {
            "name": "Presence",
            "description": "Supernatural charisma and influence over others.",
        },
        {
            "name": "Protean",
            "description": "Shapeshifting and transformation abilities.",
        },
        {
            "name": "Quietus",
            "description": "The art of silent death.",
        },
        {
            "name": "Serpentis",
            "description": "the Disciline of reptilian powers"
        },
        {
            "name": "Thaumaturgy",
            "description": "The study and practice of blood sorcery.",
        },
        {
            "name": "Vicissitude",
            "description": "The gruesome art of fleshcrafting.",
        },
        {
            "name": "Dur-An-Ki",
            "description": "Blood magic practiced by the Ashirra/Assamites.",
        },
        {
            "name": "Daimonion",
            "description": "Infernal powers granted by pacts with demonic entities.",
        },
        {
            "name": "Obeah",
            "description": "Healing powers of the Salubri"
        },
        {
            "name": "Valeran",
            "description": "The powers of the Warrior Salubri",
        },
        {
            "name": "Koldunic Sorcery",
            "description": "Elemental magic practiced by the Kolduns.",
        },
        {
            "name": "Bardo",
            "description": "Mystical practices of the Children of Osiris.",
        },
        {
            "name": "Flight",
            "description": "The power of supernatural flight by the Gargoyals.",
        },
        {
            "name": "Melpominee",
            "description": "The power of song and sound by the Daughters of Cacophony.",
        },
        {
            "name": "Mythercaria",
            "description": "The powers of the Kiasyd.",
        },
        {
            "name": "Ogham",
            "description": "The nature-based magic of the Lhiannan.",
        },
        {
            "name": "Sanguinus",
            "description": "The blood powers of the Blood Brothers.",
        },
        {
            "name": "Spiritus",
            "description": "The spirit powers of the Ahrimanes.",
        },
        {
            "name": "Temporis",
            "description": "The manipulation of time by the True Brujah.",
        },
        {
            "name": "Thanatosis",
            "description": "The power over death by the Samedi.",
        },
        {
            "name": "Visceratika",
            "description": "The signiture powers of the Gargoyals.",
        }
    ]

    for d in discipline_data:
        existing = V20_Disciplines.query.filter_by(name=d["name"]).first()
        if existing:
            continue

        discipline = V20_Disciplines(
            name=d["name"],
            description=d["description"],
        )
        db.session.add(discipline)


def seed_v20():
    seed_v20_disciplines()
    seed_v20_clan()
    seed_v20_nature()
    seed_v20_backgrounds()
    seed_magic_types()
    db.session.commit()
