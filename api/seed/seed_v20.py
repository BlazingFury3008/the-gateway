from app import db
from models import (
    V20_Clans,
    V20_Backgrounds,
    V20_Nature,
    V20_Discipline_Powers,
    V20_Advantage,
    V20_Disciplines,
    V20_Magic_Types,
    V20_Sorcery_Paths,
)
from typing import TypedDict, List, Optional


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


def seed_v20_disciplines():
    discipline_data = [
        {
            "name": "Animalism",
            "description": "Supernatural affinity with and control of animals.",
        },
        {"name": "Auspex", "description": "Heightened senses and psychic abilities."},
        {
            "name": "Bardo",
            "description": "Mystical practices of the Children of Osiris.",
        },
        {"name": "Celerity", "description": "Supernatural speed and reflexes."},
        {"name": "Chimerstry", "description": "Illusions and sensory manipulation."},
        # FIX: spelling to match your provided set ("Daimoinon")
        {
            "name": "Daimoinon",
            "description": "Infernal powers granted by pacts with demonic entities.",
        },
        {
            "name": "Dark Thaumaturgy",
            "description": "Corrupt blood sorcery steeped in darker practices.",
        },
        {
            "name": "Dementation",
            "description": "Inducing madness and manipulating minds.",
        },
        {
            "name": "Dominate",
            "description": "Mind control practiced through the piercing gaze.",
        },
        {
            "name": "Dur-An-Ki",
            "description": "Blood magic practiced by the Assamites/Ashirra.",
        },
        {"name": "Flight", "description": "The power of supernatural flight."},
        {"name": "Fortitude", "description": "Supernatural resilience and toughness."},
        {
            "name": "Koldunic Sorcery",
            "description": "Elemental magic practiced by the Kolduns.",
        },
        {"name": "Melpominee", "description": "The power of song and sound."},
        # FIX: spelling to match your provided set ("Mytherceria")
        {
            "name": "Mytherceria",
            "description": "Eldritch fae sorcery practiced by the Kiasyd.",
        },
        {
            "name": "Necromancy",
            "description": "The dark art of communing with and commanding the dead.",
        },
        {
            "name": "Obeah",
            "description": "Healing and restorative powers associated with the Salubri.",
        },
        {"name": "Obfuscate", "description": "Stealth and concealment abilities."},
        {
            "name": "Obtenebration",
            "description": "Manipulation of shadows and darkness.",
        },
        {
            "name": "Ogham",
            "description": "Nature-based magic associated with the Lhiannan.",
        },
        {"name": "Potence", "description": "Supernatural strength and power."},
        {
            "name": "Presence",
            "description": "Supernatural charisma and influence over others.",
        },
        # Added because it's in your set as a distinct entry
        {
            "name": "Presence (Setite Elder Discipline)",
            "description": "An elder Setite expression of Presence.",
        },
        {
            "name": "Protean",
            "description": "Shapeshifting and transformation abilities.",
        },
        {"name": "Quietus", "description": "The art of silent death."},
        # Added because they exist as distinct entries in your set
        {
            "name": "Quietus (Sorcerer)",
            "description": "A sorcerous expression of Quietus.",
        },
        {"name": "Quietus (Vizier)", "description": "A Vizier expression of Quietus."},
        {"name": "Sanguinus", "description": "The blood powers of the Blood Brothers."},
        {
            "name": "Serpentis",
            "description": "The Discipline of serpentine and reptilian powers.",
        },
        {
            "name": "Setite Sorcery",
            "description": "Blood sorcery traditions associated with the Followers of Set.",
        },
        {"name": "Spiritus", "description": "The spirit powers of the Ahrimanes."},
        {
            "name": "Temporis",
            "description": "The manipulation of time by the True Brujah.",
        },
        {
            "name": "Thanatosis",
            "description": "The power over death practiced by the Samedi.",
        },
        # Added because it's in your set as its own entry
        {
            "name": "Thaum. Counter.",
            "description": "Countermagic techniques used against blood sorcery.",
        },
        {
            "name": "Thaumaturgy",
            "description": "The study and practice of blood sorcery.",
        },
        # Added because it's in your set (and wasn't in your original seed list)
        {"name": "Valeren", "description": "The powers of the Warrior Salubri."},
        {"name": "Vicissitude", "description": "The gruesome art of fleshcrafting."},
        {
            "name": "Visceratika",
            "description": "The signature powers of the Gargoyles.",
        },
    ]

    for d in discipline_data:
        existing = V20_Disciplines.query.filter_by(name=d["name"]).first()
        if existing:
            # Optional: keep descriptions up to date if the seed changes over time
            if existing.description != d["description"]:
                existing.description = d["description"]
            continue

        discipline = V20_Disciplines(
            name=d["name"],
            description=d["description"],
        )
        db.session.add(discipline)

    db.session.commit()


def seed_v20_clan():
    # Old discipline order -> name mapping (1-based):
    #  1 Animalism, 2 Auspex, 3 Celerity, 4 Chimerstry, 5 Dementation, 6 Dominate,
    #  7 Fortitude, 8 Necromancy, 9 Obfuscate, 10 Obtenebration, 11 Potence, 12 Presence,
    #  13 Protean, 14 Quietus, 15 Serpentis, 16 Thaumaturgy, 17 Vicissitude, 18 Dur-An-Ki,
    #  19 Daimoinon (fixed spelling), 20 Obeah, 21 Valeren (fixed spelling),
    #  22 Koldunic Sorcery, 23 Bardo, 24 Flight, 25 Melpominee, 26 Mytherceria (fixed),
    #  27 Ogham, 28 Sanguinus, 29 Spiritus, 30 Temporis, 31 Thanatosis, 32 Visceratika

    discipline_map = {
        d.name: d.id
        for d in V20_Disciplines.query.with_entities(
            V20_Disciplines.id, V20_Disciplines.name
        ).all()
    }

    def did(name: str | None) -> int | None:
        if not name:
            return None
        _id = discipline_map.get(name)
        if _id is None:
            raise ValueError(
                f"Discipline '{name}' not found in V20_Disciplines. Seed disciplines first."
            )
        return _id

    clans_data = [
        {
            "name": "Caitiff",
            "weakness": "Because of their social stigma, Caitiff are unable to take the Status Background at character creation. In addition to being a “clan,” Caitiff is also a negative title (Titles). Until the Caitiff establishes herself in a domain or social group, she is at +2 difficulty on all Social rolls with non-Caitiff vampires. When Caitiff Embrace, their childer are also Caitiff.",
            "information": "Clanless vampires shunned and distrusted by most of Kindred society.",
            "reference": "Vampire The Masquerade 20th Anniversary Edition, Core Rulebook",
            "discipline_1": None,
            "discipline_2": None,
            "discipline_3": None,
            "discipline_4": None,
        },
        {
            "name": "Assamite",
            "weakness": "(Post Tremere Blood Curse, Warrior Caste) Whenever an Assamite so much as tastes Kindred vitae, the player must make a Self-Control or Instincts roll (difficulty equal to the number of blood points ingested +3). If this roll fails, the addiction rises to the fore, and she must make another Self-Control or Instincts roll the next time she comes in contact with Kindred vitae. If this roll fails, the Banu Haqim frenzies, doing whatever she can to partake of more vampiric blood.",
            "information": "Judgment-focused warriors whose blood resonates dangerously with vampiric vitae.",
            "reference": "Vampire The Masquerade 20th Anniversary Edition, Core Rulebook, p428",
            "discipline_1": "Celerity",
            "discipline_2": "Obfuscate",
            "discipline_3": "Quietus",
            "discipline_4": None,
        },
        {
            "name": "Brujah",
            "weakness": "The same passions that inspire Brujah to greatness or depravity, left unchecked, can send them into incandescent rages: The difficulties of rolls to resist or guide frenzy (p. 298) are two higher than normal. Additionally, a Brujah may never spend Willpower to avoid frenzy, though he may spend a point of Willpower to end a frenzy that has already begun.",
            "information": "Passionate warriors and philosophers whose tempers are infamously volatile.",
            "reference": "Vampire The Masquerade 20th Anniversary Edition, Core Rulebook, p50",
            "discipline_1": "Celerity",
            "discipline_2": "Potence",
            "discipline_3": "Presence",
            "discipline_4": None,
        },
        {
            "name": "Followers of Set",
            # FIXED: key was "weakeness"
            "weakness": "Given their origins in darkness, the Serpents react negatively to bright light: Add two health levels to damage caused by exposure to sunlight. Setites also lose one die from dice pools for actions taken in bright light (police spotlights, stage lights, flares, etc.)",
            "information": "Serpentine corrupters bound to darkness and spiritually harmed by illumination.",
            "reference": "Vampire The Masquerade 20th Anniversary Edition, Core Rulebook, p52",
            "discipline_1": "Obfuscate",
            "discipline_2": "Presence",
            "discipline_3": "Serpentis",
            "discipline_4": None,
        },
        {
            "name": "Gangrel",
            "weakness": "Every time a Gangrel frenzies, she acquires a temporary animal characteristic (which may replace an existing temporary one). A patch of fur, a brief torpor after feeding, or skittishness around crowds — all of these may mar an Outlander after frenzy. Characteristics acquired in Gangrel frenzies need not only be physical – they can be behavioral as well. Players should work with the Storyteller to determine what new animal trait is acquired (whether the frenzy involved the fight-or-flight impulse may be relevant). Over time, or in an exceptional situation, a particular animal feature may become permanent, with the next frenzy adding a new feature. A good guideline is to require each frenzy-gained trait to have some effect grounded in system terms (such as the temporary reduction of Social Attribute dots or a permanent loss of Humanity), though some Storytellers may allow narrative- only traits that can shape the story.",
            "information": "Bestial nomads whose inner Beast steadily marks their bodies and behavior.",
            "reference": "Vampire The Masquerade 20th Anniversary Edition, Core Rulebook, p54",
            "discipline_1": "Animalism",
            "discipline_2": "Fortitude",
            "discipline_3": "Protean",
            "discipline_4": None,
        },
        {
            "name": "Giovanni",
            "weakness": "The Kiss of a Giovanni vampire causes excruciating pain in mortal vessels who receive it. If the Giovanni isn’t careful, her vessel may die of shock and agony before being wholly exsanguinated. When a Giovanni feeds upon a mortal, she does twice as much damage as the Kiss of another vampire would inflict. For example, if a Giovanni takes one point of blood from a mortal vessel, that victim would suffer two health levels of damage. As a result, they tend to use blood banks and other means of feeding that don’t fight as much.",
            "information": "Necromantic clan whose feeding is agonizing and often fatal if not carefully managed.",
            "reference": "Vampire The Masquerade 20th Anniversary Edition, Core Rulebook, p56",
            "discipline_1": "Dominate",
            "discipline_2": "Necromancy",
            "discipline_3": "Potence",
            "discipline_4": None,
        },
        {
            "name": "Lasombra",
            "weakness": "Lasombra vampires cast no reflections. Whether in a mirror, in a body of water, on a polished surface, or in the rear-view of a taxicab, the image of the Keeper does not reflect.",
            "information": "Shadow-wielding nobles whose lack of reflection marks their alien nature.",
            "reference": "Vampire The Masquerade 20th Anniversary Edition, Core Rulebook, p58",
            "discipline_1": "Dominate",
            "discipline_2": "Obtenebration",
            "discipline_3": "Potence",
            "discipline_4": None,
        },
        {
            "name": "Malkavian",
            "weakness": "All members of Clan Malkavian suffer from a permanent, incurable derangement. They may acquire and recover from other derangements, and may spend Willpower to ameliorate the effects of the derangement for a scene, but they can never recover from their original derangement.",
            "information": "Mad seers whose fractured minds conceal terrifying insight.",
            "reference": "Vampire The Masquerade 20th Anniversary Edition, Core Rulebook, p60",
            "discipline_1": "Auspex",
            "discipline_2": "Dementation",
            "discipline_3": "Obfuscate",
            "discipline_4": None,
        },
        {
            "name": "Nosferatu",
            "weakness": "All Nosferatu have an Appearance score of zero, and they may never improve it. Cross it off the character sheet. Dice pools that use the Appearance Trait are inherently difficult for these hideous Kindred.",
            "information": "Hideous but resourceful vampires who lurk in society’s forgotten places.",
            "reference": "Vampire The Masquerade 20th Anniversary Edition, Core Rulebook, p62",
            "discipline_1": "Animalism",
            "discipline_2": "Obfuscate",
            "discipline_3": "Potence",
            "discipline_4": None,
        },
        {
            "name": "Ravnos",
            "weakness": "A turbulent history makes the Ravnos slaves to their vices. Each Ravnos has a penchant for some sort of vice — lying, cruelty, or theft, for example. When presented with the opportunity to engage in that vice, the Ravnos must indulge it unless her player succeeds on a Self-Control or Instincts roll (difficulty 6).",
            "information": "Tricksters driven by compulsive vices such as theft, lies, or cruelty.",
            "reference": "Vampire The Masquerade 20th Anniversary Edition, Core Rulebook, p64",
            "discipline_1": "Chimerstry",
            "discipline_2": "Fortitude",
            "discipline_3": "Animalism",
            "discipline_4": None,
        },
        {
            "name": "Toreador",
            "weakness": "When a Toreador experiences something truly remarkable — a person, an objet d’art, a lovely sunrise — the player must make a Self-Control or Instincts roll (difficulty 6). Failure means that the Kindred finds herself enthralled by the experience. The dazzled Toreador cannot act for the duration of the scene aside from commenting on or continuing their involvement with whatever has captured their attention. If the experience no longer affects her (whether by moving, being destroyed, or whatever is appropriate to the situation), the captivation ends. Enraptured Toreador may not even defend themselves if attacked, though being wounded allows them to make another Self-Control or Instincts roll.",
            "information": "Aesthetic-obsessed vampires who can be rendered helpless by beauty.",
            "reference": "Vampire The Masquerade 20th Anniversary Edition, Core Rulebook, p66",
            "discipline_1": "Auspex",
            "discipline_2": "Celerity",
            "discipline_3": "Presence",
            "discipline_4": None,
        },
        {
            "name": "Tremere",
            "weakness": "Tremere dependency on blood is even more pronounced than that of other Kindred. It takes only two draughts of another vampire’s blood for a Tremere to become blood bound instead of the normal three — the first drink counts as if the Tremere had taken two drinks. (For more information on the blood bond, see p. 286). The elders of the Clan are well aware of this, and seek to impart loyalty to the Clan by forcing all neonate Warlocks to drink of the (transubstantiated) blood of the seven Tremere elders soon after their Embrace.",
            "information": "Hierarchical blood sorcerers whose weakness enforces loyalty through the blood bond.",
            "reference": "Vampire The Masquerade 20th Anniversary Edition, Core Rulebook, p68",
            "discipline_1": "Auspex",
            "discipline_2": "Dominate",
            "discipline_3": "Thaumaturgy",
            "discipline_4": None,
        },
        {
            "name": "Tzimisce",
            "weakness": "The Tzimisce are inextricably tied to their domains of origin, and must rest in the proximity of at least two handfuls of “native soil” — earth from a place important to her as a mortal, such as the soil from her birthplace or the graveyard where she underwent her Embrace. Each night spent without this physical connection to her land limits all of the Tzimisce’s dice pools to one-half, cumulatively, until she has only a single die in her pool. The penalty remains until she rests for a full day amid her earth once more.",
            "information": "Territorial flesh-shapers mystically bound to the land of their origin.",
            "reference": "Vampire The Masquerade 20th Anniversary Edition, Core Rulebook, p70",
            "discipline_1": "Auspex",
            "discipline_2": "Animalism",
            "discipline_3": "Vicissitude",
            "discipline_4": None,  # FIX: missing in your input
        },
        {
            "name": "Ventrue",
            "weakness": "The Ventrue have rarified tastes, and they find only one specific type of mortal blood palatable and vital for them. When a player creates a Ventrue character, he should decide with the Storyteller what specific type of blood suits the character, and this choice is permanent. Blood of other types (even animals) simply offers the vampire no blood pool increase, no matter how much he consumes — he simply vomits it back up. This refined palate may be very narrow or very broad — say, the blood of younger sisters, or the blood of nude children. Vampiric blood is exempt from this restriction.",
            "information": "Patrician clan whose refined tastes severely restrict their feeding options.",
            "reference": "Vampire The Masquerade 20th Anniversary Edition, Core Rulebook, p72",
            "discipline_1": "Dominate",
            "discipline_2": "Fortitude",
            "discipline_3": "Presence",
            "discipline_4": None,
        },
        {
            "name": "Ahrimanes",
            "weakness": "An Ahrimanes’ blood was inert. They were unable to create childer or blood bonds, and a person consuming Ahrimane blood did not become a ghoul.",
            "information": "Spirit-bound outcasts whose vitae no longer functions like normal vampiric blood.",
            "reference": "Vampire The Masquerade 20th Anniversary Edition, Core Rulebook, p414",
            "discipline_1": "Animalism",
            "discipline_2": "Presence",
            "discipline_3": "Spiritus",
            "discipline_4": None,
        },
        {
            "name": "Anda",
            "weakness": "Like the Gangrel from which they were descended, Anda gained animal features from frenzying. Unlike the Gangrel, though, Anda gained such a feature once every other frenzy. However, the Anda suffered a further weakness — for each day after the third that an Anda slept within the same one-mile area, all dice pools were halved (to a minimum pool of one).",
            "information": "Nomadic hunters tied to constant travel, punished for remaining in one place too long.",
            "reference": "Vampire The Masquerade 20th Anniversary Edition, Core Rulebook, p416",
            "discipline_1": "Animalism",
            "discipline_2": "Fortitude",
            "discipline_3": "Protean",
            "discipline_4": None,
        },
        {
            "name": "Baali",
            "weakness": "Baali cannot bear to look upon or handle objects of any faith. Demons must avert their gazes from such objects, and touching them burns their flesh. In addition, should a Baali run afoul of True Faith, any hindering or damage effects are doubled.",
            "information": "Infernalists repulsed and harmed by the trappings of genuine faith.",
            "reference": "Vampire The Masquerade 20th Anniversary Edition, Core Rulebook, p394",
            "discipline_1": "Daimoinon",  # FIX: spelling
            "discipline_2": "Obfuscate",
            "discipline_3": "Presence",
            "discipline_4": None,
        },
        {
            "name": "Blood Brothers",
            "weakness": "Blood Brothers cannot Embrace. If they attempt it, the mortal simply dies. In addition, the Frankensteins literally feel each other’s pain. When a Blood Brother suffers a wound penalty, all members of the circle suffer the same penalty for the next turn. If two Blood Brothers are wounded, only the greater wound penalty applies. Blood Brothers do not continually suffer these penalties unless one of them suffers a new wound.",
            "information": "Circle-based Frankensteins who literally share each others’ pain.",
            "reference": "Vampire The Masquerade 20th Anniversary Edition, Core Rulebook, p396",
            "discipline_1": "Fortitude",
            "discipline_2": "Potence",
            "discipline_3": "Sanguinus",
            "discipline_4": None,
        },
        {
            "name": "Cappadocians",
            "weakness": "As mentioned, the Cappadocians exhibited a deathly pallor, and this only worsened as the vampire grew older. Young Cappadocians were able to pass for human (though mortals that knew what to look for could pick them out easily), but elder Cappadocians showed shriveled skin and a much more withered countenance.",
            "information": "Death-obsessed scholars whose bodies increasingly mimic the grave.",
            "reference": "Vampire The Masquerade 20th Anniversary Edition, Core Rulebook, p418",
            "discipline_1": "Auspex",
            "discipline_2": "Fortitude",
            "discipline_3": "Necromancy",
            "discipline_4": None,
        },
        {
            "name": "Children of Osiris",
            "weakness": "As appropriate for the character’s original Clan.",
            "information": "Redeemed vampires who follow Osirian mysteries and temper their curse through Bardo.",
            "reference": "Vampire The Masquerade 20th Anniversary Edition, Core Rulebook, p420",
            "discipline_1": None,
            "discipline_2": None,
            "discipline_3": None,
            "discipline_4": "Bardo",
        },
        {
            "name": "Daughters of Cacophony",
            "weakness": "The Daughters of Cacophony hear music constantly. This might be a form of synesthesia, or it might be a hallucination. This constant song distracts the Daughters as much as it guides them. The difficulties of all their Perception rolls increase by two. No Daughter of Cacophony may have Alertness above 3 dots.",
            "information": "Haunted singers guided and distracted by an unending inner song.",
            "reference": "Vampire The Masquerade 20th Anniversary Edition, Core Rulebook, p398",
            "discipline_1": "Fortitude",
            "discipline_2": "Melpominee",
            "discipline_3": "Presence",
            "discipline_4": None,
        },
        {
            "name": "Gargoyles",
            "weakness": "The Slaves are hideous. That grotesquery takes different forms, but always results in an Appearance of zero. They are also highly susceptible to mind control from any source. A Gargoyle’s Willpower score (current or permanent) is considered two points lower when used to resist such powers.",
            "information": "Constructed stone-like vampires crafted as slaves and soldiers by the Tremere.",
            "reference": "Vampire The Masquerade 20th Anniversary Edition, Core Rulebook, p400",
            "discipline_1": "Flight",
            "discipline_2": "Fortitude",
            "discipline_3": "Potence",
            "discipline_4": "Visceratika",
        },
        {
            "name": "Harbingers of Skulls",
            "weakness": "No matter how much blood a Harbinger consumes, her skin remains deathly pale. Moreover, all Harbingers look like shriveled corpses. They have Appearance ratings of 0 and automatically fail Appearance rolls.",
            "information": "Macabre returnees from the Cappadocian line, outwardly corpse-like in all stages.",
            "reference": "Vampire The Masquerade 20th Anniversary Edition, Core Rulebook, p402",
            "discipline_1": "Auspex",
            "discipline_2": "Fortitude",
            "discipline_3": "Necromancy",
            "discipline_4": None,
        },
        {
            "name": "Kiasyd",
            "weakness": "Besides their somewhat freakish appearance, Kiasyd also have an allergy to iron. Touching iron requires an immediate roll to avoid frenzy, and any weapons made from cold iron inflict aggravated damage to Kiasyd.",
            "information": "Fae-tainted occultists with an otherworldly fragility to iron.",
            "reference": "Vampire The Masquerade 20th Anniversary Edition, Core Rulebook, p404",
            "discipline_1": "Dominate",
            "discipline_2": "Mytherceria",  # FIX: spelling
            "discipline_3": "Obtenebration",
            "discipline_4": None,
        },
        {
            "name": "Lamia",
            "weakness": "The Lamia carried the “Seed of Lilith,” a wasting disease spread by their bite. Anyone the Lamia fed upon was required to make a Stamina roll (difficulty 6 for women, 8 for men). If the roll failed, the victim contracted a Black Plague-like pox that was fatal within several days. Any vampire that consumed Lamia blood became a carrier of the disease until all of the Lamia vitae had been purged from his body.",
            "information": "Deadly bodyguards of Lilith whose Kiss can spread a virulent pox.",
            "reference": "Vampire The Masquerade 20th Anniversary Edition, Core Rulebook, p423",
            "discipline_1": "Fortitude",
            "discipline_2": "Necromancy",
            "discipline_3": "Potence",
            "discipline_4": None,
        },
        {
            "name": "Lhiannan",
            "weakness": "The Lhiannan were part nature spirit, and the mark of their inhumanity ran strong within them. All difficulties to detect their nature via Auspex were reduced by two, and even normal humans felt vaguely uncomfortable in their presence. Additionally, any Lhiannan who left her territory became agitated — all dice pools were reduced by one die per week (to a minimum of the character’s Stamina) that she was gone. Once she re-entered her territory, her dice pools returned to normal within a few hours.",
            "information": "Territory-bound nature spirits in vampiric form, unsettled when far from their lands.",
            "reference": "Vampire The Masquerade 20th Anniversary Edition, Core Rulebook, p424",
            "discipline_1": "Animalism",
            "discipline_2": "Ogham",
            "discipline_3": "Presence",
            "discipline_4": None,
        },
        {
            "name": "Nagaraja",
            "weakness": "The Nagaraja require raw flesh in addition to blood to survive. For every night a Nagaraja goes without consuming flesh, he loses one cumulative die from all his Physical dice pools. Eating one point worth of flesh restores one die to these pools until the vampire has “caught up.” A human body has 10 “flesh points,” which work just like blood points: A Nagaraja consuming one flesh point increases his blood pool by one. Unlike blood points, however, taking a “flesh point” from a vessel does one health level of unsoakable lethal damage to that vessel. The flesh the Nagaraja consume must be relatively fresh, though not necessarily “alive.” Indeed, some Nagaraja keep stores of ritually preserved corpses in their havens. This weakness does not allow them to eat food or consume other liquids.",
            "information": "Cannibalistic necromancers sustained by flesh as much as vitae.",
            "reference": "Vampire The Masquerade 20th Anniversary Edition, Core Rulebook, p406",
            "discipline_1": "Auspex",
            "discipline_2": "Dominate",
            "discipline_3": "Necromancy",
            "discipline_4": None,
        },
        {
            "name": "Noiad",
            "weakness": "The Noiad were so intrinsically tied to the Samí and to their role as the divine protectors of the tribe that one of the legends about them came true. The Samí’s protectors, it was said, could not sup from animals, but could only take sustenance from the blood of the chosen (that is, the Samí). The Noiad, in fact, could not drink from animals, though they were capable of drinking from any mortal or Cainite, regardless of nationality or ethnicity.",
            "information": "Tribal protectors mystically restricted to feeding on chosen people and other vampires.",
            "reference": "Vampire The Masquerade 20th Anniversary Edition, Core Rulebook, p426",
            "discipline_1": "Animalism",
            "discipline_2": "Auspex",
            "discipline_3": "Protean",
            "discipline_4": None,
        },
        {
            "name": "Salubri",
            "weakness": "Salubri have difficulty feeding on unwilling vessels. If a Cyclops attempts it, she loses a point of Willpower.",
            "information": "Reluctant feeders whose ethics and curse both discourage predation on the unwilling.",
            "reference": "Vampire The Masquerade 20th Anniversary Edition, Core Rulebook, p408",
            "discipline_1": "Auspex",
            "discipline_2": "Fortitude",
            "discipline_3": "Obeah",
            "discipline_4": None,
        },
        {
            "name": "Samedi",
            "weakness": "The Samedi, as mentioned, are putrid beyond words. Samedi characters have Appearance ratings of 0, and automatically fail Appearance rolls.",
            "information": "Putrescent vampires whose decayed bodies repel the living.",
            "reference": "Vampire The Masquerade 20th Anniversary Edition, Core Rulebook, p410",
            "discipline_1": "Fortitude",
            "discipline_2": "Obfuscate",
            "discipline_3": "Thanatosis",
            "discipline_4": None,
        },
        {
            "name": "True Brujah",
            "weakness": "True Brujah lose much of their emotional capacity when they are Embraced, and their ability for sympathy continues to deteriorate as they grow older. All Conscience and Conviction rolls are made at +2 difficulty (maximum 10), and ratings in Conscience, Conviction, Humanity, and Paths of Enlightenment cost double the normal experience costs.",
            "information": "Emotionally numb temporal scholars whose morality erodes and is hard to maintain.",
            "reference": "Vampire The Masquerade 20th Anniversary Edition, Core Rulebook, p412",
            "discipline_1": "Potence",
            "discipline_2": "Presence",
            "discipline_3": "Temporis",
            "discipline_4": None,
        },
        {
            "name": "Assamite Antitribu",
            "weakness": "Assamite antitribu have the post-curse weakness mentioned in the sidebar on the previous page. In fact, their weakness never changed, while the rest of the Clan shackled with the blood curse of the Tremere. Whenever an Banu Haqim antitribu drinks vampire blood, the player must roll Self-Control or Instincts (difficulty 3 + the number of blood points consumed). If this roll fails, the character is addicted. Once addicted, the character will indulge in drinking Kindred blood whenever possible. When she is given the opportunity to do so, the player must roll Self-Control or Instincts (difficulty 6). If this roll fails, the character frenzies, attacks the target and drinks as much blood as she can. ",
            "information": "Sabbat-aligned judges whose old addiction to Kindred vitae never faded.",
            "reference": "Vampire The Masquerade 20th Anniversary Edition, Core Rulebook, p429",
            "discipline_1": "Celerity",
            "discipline_2": "Obfuscate",
            "discipline_3": "Quietus",
            "discipline_4": None,
        },
        {
            "name": "Brujah Antitribu",
            "weakness": "The bloodline has the same weakness as the main body of the Clan (p. 51): All frenzy difficulties are increased by two, to a maximum of 10. Unlike Camarilla Brujah, though, the Brutes aren’t in the least bit sensitive about their tempers. Indeed, they revel in their rage.",
            "information": "Rage-embracing Sabbat shock troops reveling in their violent tempers.",
            "reference": "Vampire The Masquerade 20th Anniversary Edition, Core Rulebook, p429",
            "discipline_1": "Celerity",
            "discipline_2": "Potence",
            "discipline_3": "Presence",
            "discipline_4": None,
        },
        {
            "name": "City Gangrel",
            "weakness": "City Gangrel suffer the same weakness as the main line of the Clan. Whenever a City Gangrel frenzies, he gains a temporary animalistic feature of some kind (which may replace an existing temporary one). The mechanical impact of such a feature is up to Storyteller discretion. City Gangrel tend to develop features reminiscent of the animals commonly found in urban environments — rats, dogs, cats, pigeons, and even insects.",
            "information": "City-adapted Gangrel whose Beasts echo rats, dogs, pigeons, and other urban fauna.",
            "reference": "Vampire The Masquerade 20th Anniversary Edition, Core Rulebook, p429",
            "discipline_1": "Celerity",
            "discipline_2": "Obfuscate",
            "discipline_3": "Protean",
            "discipline_4": None,
        },
        {
            "name": "Country Gangrel",
            "weakness": "The Hunters have the same weakness as their non-Sabbat counterparts. Each time a Country Gangrel frenzies, he gains a temporary animalistic feature, which may replace an existing temporary one. The mechanical impact of such a feature is up to Storyteller discretion.",
            "information": "Rural Sabbat hunters with increasingly feral, animalistic traits.",
            "reference": "Vampire The Masquerade 20th Anniversary Edition, Core Rulebook, p430",
            "discipline_1": "Animalism",
            "discipline_2": "Fortitude",
            "discipline_3": "Protean",
            "discipline_4": None,
        },
        {
            "name": "Malkavian Antitribu",
            "weakness": "Like all Malkavians, the Freaks are completely insane. At character creation, the player must choose a derangement that the character can never overcome.",
            "information": "Sabbat lunatics whose incurable insanity often manifests in violent ways.",
            "reference": "Vampire The Masquerade 20th Anniversary Edition, Core Rulebook, p430",
            "discipline_1": "Auspex",
            "discipline_2": "Dementation",
            "discipline_3": "Obfuscate",
            "discipline_4": None,
        },
        {
            "name": "Nosferatu Antitribu",
            "weakness": "Sabbat Nosferatu are just as hideous as their Camarilla counterparts, and suffer the same weakness: they all have an Appearance score of zero, and they may never improve it",
            "information": "Equally hideous Sabbat sewer lords and ambushers.",
            "reference": "Vampire The Masquerade 20th Anniversary Edition, Core Rulebook, p430",
            "discipline_1": "Animalism",
            "discipline_2": "Obfuscate",
            "discipline_3": "Potence",
            "discipline_4": None,
        },
        {
            "name": "Panders",
            "weakness": "Panders do not have a specific weakness. Pander characters cannot start lower than Ninth Generation, though they can subsequently lower their Generation via diablerie.",
            "information": "Ambitious, clanless Sabbat vampires striving for recognition and power.",
            "reference": "Vampire The Masquerade 20th Anniversary Edition, Core Rulebook, p431",
            "discipline_1": None,
            "discipline_2": None,
            "discipline_3": None,
            "discipline_4": None,
        },
        {
            "name": "Ravnos Antitribu",
            "weakness": "Each Ravnos antitribu, just like their parent Clan, has a penchant for some sort of vice — breaking taboos is hard-wired into the Rogues just as it is into the Ravnos proper. When presented with the opportunity to engage in that vice, the Rogue must indulge it unless her player succeeds on a Self-Control or Instincts roll (difficulty 6).",
            "information": "Sabbat con artists hard-wired to break taboos and pursue vice.",
            "reference": "Vampire The Masquerade 20th Anniversary Edition, Core Rulebook, p431",
            "discipline_1": "Animalism",
            "discipline_2": "Chimerstry",
            "discipline_3": "Fortitude",
            "discipline_4": None,
        },
        {
            "name": "Salubri Antitribu",
            "weakness": "Unlike their nonviolent brethren, Sabbat Salubri must consume blood taken by force, preferably in the heat of battle. Unless the vampire feeds on blood from a fallen foe or fights his target before feeding, the Vitae offers no nourishment. In addition, Salubri antitribu cannot start lower than Tenth Generation or higher than Twelfth, as their blood has yet to spread across a wider spectrum than that.",
            "information": "Martial cousins of the Salubri who must drink the blood of defeated foes.",
            "reference": "Vampire The Masquerade 20th Anniversary Edition, Core Rulebook, p431",
            "discipline_1": "Auspex",
            "discipline_2": "Fortitude",
            "discipline_3": "Valeren",  # FIX: spelling
            "discipline_4": None,
        },
        {
            "name": "Serpents of the Light",
            "weakness": "The Serpents of the Light, despite the name, are just as vulnerable to bright illumination as their parent Clan. They suffer two additional health levels of damage from sunlight, and a one-die penalty to all rolls when subject to bright light of any kind.",
            "information": "Caribbean offshoot of the Setites whose curse mirrors their progenitors’ hatred of light.",
            "reference": "Vampire The Masquerade 20th Anniversary Edition, Core Rulebook",
            "discipline_1": "Presence",
            "discipline_2": "Obfuscate",
            "discipline_3": "Serpentis",
            "discipline_4": None,
        },
        {
            "name": "Toreador Antitribu",
            "weakness": "Over time, the propensity for the Toreador to become fascinated by beauty has twisted itself into a perverse need for cruelty. When faced with an opportunity to inflict emotional or physical pain — a captive that might be tortured, or a protégé whose ambitions might be squashed — the Toreador antitribu’s player must make a Self-Control or Instinct roll (difficulty 6), or spend a Willpower point. If the roll fails, the character must indulge in her savage desires.",
            "information": "Perverse aesthetes whose fascination with beauty has twisted into sadism.",
            "reference": "Vampire The Masquerade 20th Anniversary Edition, Core Rulebook",
            "discipline_1": "Auspex",
            "discipline_2": "Celerity",
            "discipline_3": "Presence",
            "discipline_4": None,
        },
        {
            "name": "Tremere Antitribu",
            "weakness": "The Tremere antitribu were all immediately recognizable as traitors to Camarilla Warlocks. The mark wasn’t a physical disfigurement, but a change to the character’s very presence. This wasn’t a weakness that carries an immediate mechanical disadvantage, but once identified, the Tremere antitribu could expect to be hunted down and burned as soon as the Tremere can possibly manage it. They were also still susceptible to the power of the blood, gaining a +1 to all Vinculum rolls.",
            "information": "Hunted Sabbat sorcerers whose betrayal is mystically obvious to their former clan.",
            "reference": "Vampire The Masquerade 20th Anniversary Edition, Core Rulebook",
            "discipline_1": "Auspex",
            "discipline_2": "Dominate",
            "discipline_3": "Thaumaturgy",
            "discipline_4": None,
        },
        {
            "name": "Ventrue Antitribu (Auspex)",
            "weakness": "Sabbat Ventrue have the same weakness as their Camarilla brethren. The player decides with the Storyteller what specific type of blood suits the Crusader, and this choice is permanent. Blood of other types (even animals) simply offers the vampire no blood pool increase, no matter how much he consumes",
            "information": "Sabbat nobles mirroring the refined but restrictive feeding of their Camarilla kin.",
            "reference": "Vampire The Masquerade 20th Anniversary Edition, Core Rulebook",
            "discipline_1": "Dominate",
            "discipline_2": "Fortitude",
            "discipline_3": "Auspex",
            "discipline_4": None,
        },
        {
            "name": "Ventrue Antitribu (Presence)",
            "weakness": "Sabbat Ventrue have the same weakness as their Camarilla brethren. The player decides with the Storyteller what specific type of blood suits the Crusader, and this choice is permanent. Blood of other types (even animals) simply offers the vampire no blood pool increase, no matter how much he consumes",
            "information": "Sabbat nobles mirroring the refined but restrictive feeding of their Camarilla kin.",
            "reference": "Vampire The Masquerade 20th Anniversary Edition, Core Rulebook",
            "discipline_1": "Dominate",
            "discipline_2": "Fortitude",
            "discipline_3": "Presence",
            "discipline_4": None,
        },
        {
            "name": "Assamite Sorcerers",
            "weakness": "The line as a whole has practiced the art for so long that it permeates their blood, making each individual sorcerer stand out like a beacon to anyone with supernatural perception. Any use of a supernatural power on a sorcerer for purposes of perception enjoys a -2 difficulty. Additionally, attempts to penetrate a sorcerer’s supernatural concealment using an opposed power are considered to operate one level higher than normal (so a character with Auspex 2 trying to penetrate a sorcerer’s Obfuscate has an effective Auspex of 3).",
            "information": "Long-practicing mystics whose blood shines like a beacon to supernatural senses.",
            "reference": "Vampire The Masquerade 20th Anniversary Edition, Core Rulebook, p433",
            "discipline_1": "Dur-An-Ki",
            "discipline_2": "Obfuscate",
            "discipline_3": "Quietus",
            "discipline_4": None,
        },
        {
            "name": "Assamite Viziers",
            "weakness": "The viziers are mad. Every vizier finds himself caught up in the continuance of his chosen pursuits to the exclusion of trivial concerns such as daily shelter or nightly nourishment. Each vizier has an Obsessive-Compulsive derangement associated with his highest-rated intellectual or creative Ability. If the character’s focus of effort shifts, so does the focus of the derangement.",
            "information": "Hyper-focused artisans and scholars consumed by their chosen craft or pursuit.",
            "reference": "Vampire The Masquerade 20th Anniversary Edition, Core Rulebook, p434",
            "discipline_1": "Auspex",
            "discipline_2": "Celerity",
            "discipline_3": "Quietus",
            "discipline_4": None,
        },
        {
            "name": "Daitya",
            "weakness": "The Daitya suffer the same weakness as the Followers of Set (p. 53): They suffer two additional health levels of damage from sunlight, and a one-die penalty to all rolls when subject to bright light of any kind.",
            "information": "Ascetic Setite offshoots embracing a more contemplative, philosophical path.",
            "reference": "Vampire The Masquerade 20th Anniversary Edition, Core Rulebook, p434",
            "discipline_1": "Presence",
            "discipline_2": "Obfuscate",
            "discipline_3": "Serpentis",
            "discipline_4": None,
        },
        {
            "name": "Tlacique",
            "weakness": "The Tlacique’s weakness is one of the only ways to trace the line’s lineage to the Setites. They, like the Followers of Set, suffer two additional health levels of damage from sunlight, and a one-die penalty to all rolls when subjected to bright light of any kind.",
            "information": "Predatory jungle Setites whose curse ties them to the same hatred of light.",
            "reference": "Vampire The Masquerade 20th Anniversary Edition, Core Rulebook, p435",
            "discipline_1": "Presence",
            "discipline_2": "Obfuscate",
            "discipline_3": "Protean",
            "discipline_4": None,
        },
        {
            "name": "Warrior Setites",
            "weakness": "The warriors suffer same weakness as the Followers of Set: They suffer two additional health levels of damage from sunlight, and a one-die penalty to all rolls when subjected to bright light of any kind.",
            "information": "Militant arm of the Setites, embracing the same vulnerability to light as their kin.",
            "reference": "Vampire The Masquerade 20th Anniversary Edition, Core Rulebook, p435",
            "discipline_1": "Potence",
            "discipline_2": "Obfuscate",
            "discipline_3": "Serpentis",
            "discipline_4": None,
        },
        {
            "name": "Mariners",
            "weakness": "As with most Gangrel, the Mariners gain an animalistic feature each time they frenzy. These features, though, resemble fish, aquatic worms, cephalopods, and other sea creatures (the rare Gangrel develops a cetacean or seal-like feature). The alien nature of these features should be taken into consideration by Storytellers determining the mechanical impact of such features.",
            "information": "Sea-bound Gangrel whose Beasts manifest as oceanic mutations.",
            "reference": "Vampire The Masquerade 20th Anniversary Edition, Core Rulebook, p435",
            "discipline_1": "Animalism",
            "discipline_2": "Fortitude",
            "discipline_3": "Protean",
            "discipline_4": None,
        },
        {
            "name": "Gargoyle Scout",
            "weakness": "All Health penalties from injures double as the Gargoyle’s damaged body turns back to stone. These penalties only go away when the Gargoyle awakens in an evening with no health boxes crossed off.",
            "information": "Reconnaissance-focused Gargoyles whose stone bodies hamper them when injured.",
            "reference": "Lore of the Bloodlines, p.36",
            "discipline_1": "Auspex",
            "discipline_2": "Obfuscate",
            "discipline_3": "Flight",
            "discipline_4": None,
        },
        {
            "name": "Gargoyle Sentinel",
            "weakness": "These Gargoyles were created to watch over the chantries, havens, and other important locations of the early Tremere. They are quite sociable and friendly, despite appearances to the contrary; They suffer the same weakness as their normal Gargoyle counterparts.",
            "information": "Guardian Gargoyles designed to watch over chantries and havens, surprisingly sociable despite their appearance.",
            "reference": "Lore of the Bloodlines, p.36",
            "discipline_1": "Fortitude",
            "discipline_2": "Potence",
            "discipline_3": "Flight",
            "discipline_4": None,
        },
        {
            "name": "Gargoyle Warrior",
            "weakness": "These Gargoyles were built to wage war on the enemies of House and Clan Tremere. The Tremere did not want to waste their small number on fighting their battles, so they created these stone soldiers instead; They suffer the same weakness as their normal Gargoyle counterparts.",
            "information": "Battle-built stone soldiers created to wage war on the Tremere’s enemies.",
            "reference": "Lore of the Bloodlines, p.36",
            "discipline_1": "Fortitude",
            "discipline_2": "Protean",
            "discipline_3": "Flight",
            "discipline_4": None,
        },
        {
            "name": "Angelis Ater (Potence)",
            "weakness": "The Angellis Ater have the same weakness as other Lasombra — they do not cast reflections. ",
            "information": "Lasombra subsect steeped in deeper darkness, sometimes bearing an infernal taint.",
            "reference": "Vampire The Masquerade 20th Anniversary Edition, Core Rulebook, p436",
            "discipline_1": "Daimoinon",
            "discipline_2": "Dominate",
            "discipline_3": "Potence",
            "discipline_4": None,
        },
        {
            "name": "Angelis Ater (Presence)",
            "weakness": "The Angellis Ater have the same weakness as other Lasombra — they do not cast reflections. ",
            "information": "Lasombra subsect steeped in deeper darkness, sometimes bearing an infernal taint.",
            "reference": "Vampire The Masquerade 20th Anniversary Edition, Core Rulebook, p436",
            "discipline_1": "Daimoinon",
            "discipline_2": "Dominate",
            "discipline_3": "Presence",
            "discipline_4": None,
        },
        {
            "name": "Angelis Ater (Obtenebration)",
            "weakness": "The Angellis Ater have the same weakness as other Lasombra — they do not cast reflections. ",
            "information": "Lasombra subsect steeped in deeper darkness, sometimes bearing an infernal taint.",
            "reference": "Vampire The Masquerade 20th Anniversary Edition, Core Rulebook, p436",
            "discipline_1": "Daimoinon",
            "discipline_2": "Dominate",
            "discipline_3": "Obtenebration",
            "discipline_4": None,
        },
        {
            "name": "Lasombra Antitribu",
            "weakness": "In addition to the Clan’s usual problem with reflections (p. 59), Lasombra antitribu also have the “weakness” of being hunted relentlessly by the Sabbat, and targeted for destruction whenever their existence is made public.",
            "information": "Defectors of the Lasombra clan forced into constant hiding from their former sect.",
            "reference": "Vampire The Masquerade 20th Anniversary Edition, Core Rulebook, p436",
            "discipline_1": "Dominate",
            "discipline_2": "Obtenebration",
            "discipline_3": "Potence",
            "discipline_4": None,
        },
        {
            "name": "Dominate Malkavians",
            "weakness": "Like all Malkavians, the Carriers are irretrievably insane. As a rule, their insanity tends to be “quieter” than the average Lunatic’s, but the Dominate Malkavians still have at least one derangement that cannot be cured.",
            "information": "A quieter, more subtle branch of Malkavians whose minds remain irretrievably broken.",
            "reference": "Vampire The Masquerade 20th Anniversary Edition, Core Rulebook, p437",
            "discipline_1": "Auspex",
            "discipline_2": "Dominate",
            "discipline_3": "Obfuscate",
            "discipline_4": None,
        },
        {
            "name": "Brahman",
            "weakness": "The Brahman suffer the same weakness as the main body of Clan Ravnos. Each one has a preferred form of vice (though the Brahman have a special love for swindling through psychic readings and séances). Whenever the Brahman is given the chance to indulge in his favorite vice, the player must roll Self-Control or Instinct (difficulty 6) to resist the temptation.",
            "information": "Mystically inclined Ravnos who often express their vice through spiritual scams and séances.",
            "reference": "Vampire The Masquerade 20th Anniversary Edition, Core Rulebook, p437",
            "discipline_1": "Animalism",
            "discipline_2": "Auspex",
            "discipline_3": "Chimerstry",
            "discipline_4": None,
        },
        {
            "name": "Wu Zao (Obeah)",
            "weakness": "The Wu Zao are scholars by nature, and each of them has a special focus. At character creation, the player must select an area of arcane study — the Wan Kuei, the culture of a specific mortal group, a group of mystical tomes lost to the ages, etc. Whenever the opportunity arises to learn something about this subject, the player must make a Willpower roll (difficulty 6) to avoid pursuing that lead to the exclusion of all else.",
            "information": "Scholar-sages of the Salubri line whose curiosity borders on compulsion.",
            "reference": "Vampire The Masquerade 20th Anniversary Edition, Core Rulebook, p438",
            "discipline_1": "Auspex",
            "discipline_2": "Fortitude",
            "discipline_3": "Obeah",
            "discipline_4": None,
        },
        {
            "name": "Wu Zao (Valeren)",
            "weakness": "The Wu Zao are scholars by nature, and each of them has a special focus. At character creation, the player must select an area of arcane study — the Wan Kuei, the culture of a specific mortal group, a group of mystical tomes lost to the ages, etc. Whenever the opportunity arises to learn something about this subject, the player must make a Willpower roll (difficulty 6) to avoid pursuing that lead to the exclusion of all else.",
            "information": "Scholar-sages of the Salubri line whose curiosity borders on compulsion.",
            "reference": "Vampire The Masquerade 20th Anniversary Edition, Core Rulebook, p438",
            "discipline_1": "Auspex",
            "discipline_2": "Fortitude",
            "discipline_3": "Valeren",  # FIX: spelling
            "discipline_4": None,
        },
        {
            "name": "Telyavelic Tremere",
            "weakness": "The Telyavs bound their fates so tightly to their pagan herds that they took on some of the same fears and enemies. They are weak against Christian symbols and faith. Difficulties to resist frenzy are two higher than normal when confronted by an enemy using True Faith as a defense. They recoil from the sight of the cross or other symbols of the Christian faith.",
            "information": "Pagan Tremere whose ties to old faiths leave them vulnerable to Christian holy symbols.",
            "reference": "Vampire The Masquerade 20th Anniversary Edition, Core Rulebook, p438",
            "discipline_1": "Auspex",
            "discipline_2": "Presence",
            "discipline_3": "Thaumaturgy",
            "discipline_4": None,
        },
        {
            "name": "Koldun (Dominate)",
            "weakness": "As with the rest of the Clan (p. 71): The koldun must rest in the proximity of at least two handfuls of native soil. Failure to meet this requirement halves the koldun’s dice pools every 24 hours, until all pools fall to one die. This penalty remains until they are able to rest for a full day in their earth.",
            "information": "Elemental sorcerers of the Tzimisce, deeply bound to their ancestral lands.",
            "reference": "Vampire The Masquerade 20th Anniversary Edition, Core Rulebook, p439",
            "discipline_1": "Auspex",
            "discipline_2": "Animalism",
            "discipline_3": "Dominate",
            "discipline_4": None,
        },
        {
            "name": "Koldun (Vicissitude)",
            "weakness": "As with the rest of the Clan (p. 71): The koldun must rest in the proximity of at least two handfuls of native soil. Failure to meet this requirement halves the koldun’s dice pools every 24 hours, until all pools fall to one die. This penalty remains until they are able to rest for a full day in their earth.",
            "information": "Elemental sorcerers of the Tzimisce, deeply bound to their ancestral lands.",
            "reference": "Vampire The Masquerade 20th Anniversary Edition, Core Rulebook, p439",
            "discipline_1": "Auspex",
            "discipline_2": "Animalism",
            "discipline_3": "Vicissitude",
            "discipline_4": None,
        },
        {
            "name": "Old Clan Tzimisce",
            "weakness": "As with the rest of the Clan (p. 71), the Old Clan Tzimisce must sleep in at least two handfuls of soil from their homeland. Failure to meet this requirement halves the Tzimisce’s dice pools every 24 hours, until all pools fall to one die. This penalty remains until they are able to rest for a full day in their earth.",
            "information": "Traditionalist Tzimisce predating the modern flesh-crafting practices of the clan.",
            "reference": "Vampire The Masquerade 20th Anniversary Edition, Core Rulebook, p439",
            "discipline_1": "Auspex",
            "discipline_2": "Animalism",
            "discipline_3": "Dominate",
            "discipline_4": None,
        },
        {
            "name": "Maeghar (Mytherceria)",
            "weakness": "Due to her fae-marked physique, rolls to recognize the Maeghar as otherworldly are at -1 difficulty. Secondly, her fae heritage makes her vulnerable to cold iron: not only do weapons made from cold iron inflict aggravated damage to her, but such damage triggers an immediate roll to avoid either frenzy or Rötschreck as befitting the context. Lastly, a Maeghar feels such revulsion at feeding from a warm, smelly, and sweaty human that she must drain her victim’s blood in a clean container before consuming it. This restriction does not apply when feeding from vampires.",
            "information": "Fae-marked Tal'Mahe'Ra who find human blood repulsive unless decanted and are especially vulnerable to cold iron.",
            "reference": "The Black Hand: A Guide To The Tal'Mahe'Ra, p167",
            "discipline_1": "Mytherceria",  # FIX: spelling
            "discipline_2": None,
            "discipline_3": None,
            "discipline_4": None,
        },
        {
            "name": "Maeghar (Necromancy)",
            "weakness": "Due to her fae-marked physique, rolls to recognize the Maeghar as otherworldly are at -1 difficulty. Secondly, her fae heritage makes her vulnerable to cold iron: not only do weapons made from cold iron inflict aggravated damage to her, but such damage triggers an immediate roll to avoid either frenzy or Rötschreck as befitting the context. Lastly, a Maeghar feels such revulsion at feeding from a warm, smelly, and sweaty human that she must drain her victim’s blood in a clean container before consuming it. This restriction does not apply when feeding from vampires.",
            "information": "Fae-marked Tal'Mahe'Ra who find human blood repulsive unless decanted and are especially vulnerable to cold iron.",
            "reference": "The Black Hand: A Guide To The Tal'Mahe'Ra, p167",
            "discipline_1": "Necromancy",
            "discipline_2": None,
            "discipline_3": None,
            "discipline_4": None,
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
            reference=c.get("reference"),
            discipline_1=did(c.get("discipline_1")),
            discipline_2=did(c.get("discipline_2")),
            discipline_3=did(c.get("discipline_3")),
            discipline_4=did(c.get("discipline_4")),
        )
        db.session.add(clan)

    db.session.commit()


class SorceryPower(TypedDict):
    name: str
    description: str
    system: str


class SorceryPath(TypedDict):
    name: str
    reference: str
    powers: List[SorceryPower]
    type: str


def seed_v20_sorcery():
    path_data: List[SorceryPath] = [
        {
            "name": "Fires of the Inferno",
            "reference": "Rites of the Blood; PG 168",
            "type": "Dark Thaumaturgy",
            "powers": [
                {
                    "name": "Lighter",
                    "description": "Practitioners of the Fires of the Inferno may summon forth balefire that springs forth from her hands in jets orglobes. Many believe that this malignant green flame is conjured from the very depths of Hades. Being burned by these fires is to taste the agonies that await them in Hell. Witnessing the conjuring of the Fires of Inferno allows anyone with mystical senses to know the source is infernal. Balefire is greatly feared, as fire is one of the surest ways to bring Final Death to a vampire.",
                    "system": "The number of successes determines how accurately the vampire places the flame in his desired location (declared before the roll is made). Individual descriptions are not provided for each level of this path — fire is fire, after all (and can potentially cause frenzy in other vampires witnessing it). The chart below describes the path level required to generate a specific amount of flame. To soak the damage at all, a vampire must have the Fortitude Discipline.",
                },
                {
                    "name": "Stovetop",
                    "description": "Practitioners of the Fires of the Inferno may summon forth balefire that springs forth from her hands in jets orglobes. Many believe that this malignant green flame is conjured from the very depths of Hades. Being burned by these fires is to taste the agonies that await them in Hell. Witnessing the conjuring of the Fires of Inferno allows anyone with mystical senses to know the source is infernal. Balefire is greatly feared, as fire is one of the surest ways to bring Final Death to a vampire.",
                    "system": "The number of successes determines how accurately the vampire places the flame in his desired location (declared before the roll is made). Individual descriptions are not provided for each level of this path — fire is fire, after all (and can potentially cause frenzy in other vampires witnessing it). The chart below describes the path level required to generate a specific amount of flame. To soak the damage at all, a vampire must have the Fortitude Discipline.",
                },
                {
                    "name": "Blowtorch",
                    "description": "Practitioners of the Fires of the Inferno may summon forth balefire that springs forth from her hands in jets orglobes. Many believe that this malignant green flame is conjured from the very depths of Hades. Being burned by these fires is to taste the agonies that await them in Hell. Witnessing the conjuring of the Fires of Inferno allows anyone with mystical senses to know the source is infernal. Balefire is greatly feared, as fire is one of the surest ways to bring Final Death to a vampire.",
                    "system": "The number of successes determines how accurately the vampire places the flame in his desired location (declared before the roll is made). Individual descriptions are not provided for each level of this path — fire is fire, after all (and can potentially cause frenzy in other vampires witnessing it). The chart below describes the path level required to generate a specific amount of flame. To soak the damage at all, a vampire must have the Fortitude Discipline.",
                },
                {
                    "name": "Flamethrower",
                    "description": "Practitioners of the Fires of the Inferno may summon forth balefire that springs forth from her hands in jets orglobes. Many believe that this malignant green flame is conjured from the very depths of Hades. Being burned by these fires is to taste the agonies that await them in Hell. Witnessing the conjuring of the Fires of Inferno allows anyone with mystical senses to know the source is infernal. Balefire is greatly feared, as fire is one of the surest ways to bring Final Death to a vampire.",
                    "system": "The number of successes determines how accurately the vampire places the flame in his desired location (declared before the roll is made). Individual descriptions are not provided for each level of this path — fire is fire, after all (and can potentially cause frenzy in other vampires witnessing it). The chart below describes the path level required to generate a specific amount of flame. To soak the damage at all, a vampire must have the Fortitude Discipline.",
                },
                {
                    "name": "Confligeration",
                    "description": "Practitioners of the Fires of the Inferno may summon forth balefire that springs forth from her hands in jets orglobes. Many believe that this malignant green flame is conjured from the very depths of Hades. Being burned by these fires is to taste the agonies that await them in Hell. Witnessing the conjuring of the Fires of Inferno allows anyone with mystical senses to know the source is infernal. Balefire is greatly feared, as fire is one of the surest ways to bring Final Death to a vampire.",
                    "system": "The number of successes determines how accurately the vampire places the flame in his desired location (declared before the roll is made). Individual descriptions are not provided for each level of this path — fire is fire, after all (and can potentially cause frenzy in other vampires witnessing it). The chart below describes the path level required to generate a specific amount of flame. To soak the damage at all, a vampire must have the Fortitude Discipline.",
                },
            ],
        },
        {
            "name": "Path of Phobos",
            "reference": "Rites of the Blood; PG 168",
            "type": "Dark Thaumaturgy",
            "powers": [
                {
                    "name": "Induce Fear",
                    "description": "The infernalist harnesses the power of Hell to twist\r\nthe mind of her victim, leaving her to feel paranoid.\r\nSubtle shapes and shadows shimmer at the edge of the\r\nvictim’s vision, tormenting her by lurking just beyond\r\nher range of sight.",
                    "system": "The infernalist may target any subject within\r\nher line of sight. She must concentrate, gesture towards\r\nthe victim, and chant the proper invocation to Hell.\r\nShould she succeed, the victim becomes noticeably upset\r\nand preoccupied, which should be role-played. To resist,\r\nthe victim must make a Courage roll (difficulty 4 + the\r\nnumber of successes achieved on the activation roll, to\r\na maximum of 9) to take any action other than looking\r\nfor the imagined stalker.\r\nAll of the victim’s dice pools for the duration of this\r\npower are automatically reduced by one. The duration of\r\nthis power is limited by the number of successes achieved\r\non the activation role:\r\n1 Success One Turn\r\n2 Successes Five Turns\r\n3 Successes One Hour\r\n4 Successes One Night\r\n5 Successes Two Nights",
                },
                {
                    "name": "Spook",
                    "description": "This power transforms suspicion to dread, as the flitting\r\nshadows become frightening threats. The victim senses\r\nsomething terrible is about to happen to him unless he\r\nimmediately flees the area. He might imagine she sees the\r\nflash of a gun barrel or hears the clicking of hard-soled\r\nshoes on the pavement just behind her. He might even\r\nbelieve she smells her pursuer’s sweat or feels his damp\r\nbreath on the back of her neck.",
                    "system": "The infernalist must see her victim and whisper\r\na prayer to Hell for this power to work. The nagging\r\nsense of discomfort in the back of the character’s mind\r\nbecomes more tangible. Mortals must make a successful\r\nCourage roll (difficulty 7) to keep from fleeing the area\r\nin terror. Vampires must make the same roll, but if they\r\nfail they enter Rötschreck.",
                },
                {
                    "name": "Terrorise",
                    "description": "The infernalist can draw out his victim’s fear and present\r\nher with it. The victim sees that which terrifies her the\r\nmost. If she fears spiders, she may imagine spider webs\r\nbrushing her face and hands as thousands of illusory\r\narachnids scuttle across her flesh. She may hear them\r\nskittering across the floor or clicking their horrid chelicerae.\r\nTo the victim, the effects seem very real, though they are\r\nsimply illusions and invisible to onlookers.",
                    "system": "The infernalist must concentrate for a\r\nmoment and then gesture towards her victim. Should\r\nshe succeed, the terrorized subject must succeed in a\r\nCourage roll (difficulty 7) to shake off her fear in order\r\nto act. Otherwise she simply cowers, feebly hiding from\r\nher imagined object of terror. Botching this Courage\r\nroll results in a derangement, preferably suited to the\r\nfear visiting the victim.\r\nThe duration of this power is limited by the number\r\nof successes achieved on the activation role:\r\n1 Success One Turn\r\n2 Successes Five Turns\r\n3 Successes 30 Minutes\r\n4 Successes One Hour\r\n5 Successes One Night",
                },
                {
                    "name": "Fear Plague",
                    "description": "The infernalist can now taste her victim’s most deeprooted\r\nfear. She can force her subject to plunge deep\r\ninto this phobia every waking moment. A person afraid\r\nof drowning would feel the air thicken and coagulate in\r\nhis throat and lungs until he cannot take a breath, while\r\na person afraid of vampires may see fanged nemeses in\r\nhis coworkers or lurking behind every corner. Eventually,\r\nthe victim becomes so exhausted that he is unable rise\r\nand face a new night of swarming horrors.",
                    "system": "The infernalist must see and then loudly\r\ncurse her victim for this terrible power to take effect.\r\nOnce cursed, this power lasts for a week. The victim is\r\nconstantly harassed by his fear every moment. For the\r\nduration of this power, all Willpower rolls are made as\r\nthough the character’s permanent rating is three lower\r\nthan normal (to a minimum of 1).",
                },
                {
                    "name": "Leech Fear",
                    "description": "This power enables the infernalist to temporarily feed\r\non fear as though it was blood. This experience gives a\r\neuphoric high stronger than conventional feeding, but\r\nit is a dangerous practice if used too frequently. The\r\ninfernalist converts the pure emotional charge drawn\r\nfrom the victim’s terror into a mystical substitute for vitae.",
                    "system": "As long as she has her subject in sight, the\r\ninfernalist may attempt to gain sustenance from any fear\r\nthat the victim might be currently suffering. Naturally,\r\nthe victim must have cause to be afraid of something or\r\nsomeone while the infernalist practices this power. These\r\nfears may not be caused by other applications of this path.\r\nThe number of successes achieved on the activation roll\r\ndetermines the number of points transmuted into the\r\ninfernalist’s “fear pool.” Each point in this “fear pool”\r\nmay be spent exactly like a blood point, beyond normal\r\nGeneration limits. However, this extra source of power\r\nmust be utilized before sunrise or it will disappear.\r\nIn addition to the lost Willpower point, a botch means\r\nthat the infernalist gets no “fear pool” from the victim, and\r\ncannot use the power on that victim again for 24 hours.",
                },
            ],
        },
        {
            "name": "Taking of the Spirit",
            "reference": "Rites of the Blood; PG 170",
            "type": "Dark Thaumaturgy",
            "powers": [
                {
                    "name": "The Taking of the Spirit",
                    "description": "By calling upon the power of Hell, this path allows\r\nthe infernalist to strip away the temporary Willpower\r\nof her victim, leaving an almost soulless automaton\r\nready to serve the infernalist without question. Some\r\nfiendish vampires have built entire legions of servants\r\nfor themselves with this power. This fearsome path works\r\non vampires and kine alike.",
                    "system": "The infernalist loudly calls forth the legions of\r\nHell to steal away the spirit of her target and then touches her\r\ntarget. Depending upon the circumstances, the Storyteller\r\nmay require a successful Dexterity + Brawl roll for the\r\nthaumaturge to make contact with the intended victim.\r\nOnce contact is made, the infernalist must engage in a\r\ncontested Willpower roll against the subject (difficulty 8).\r\nIf the victim accumulates more successes on this\r\ncontested Willpower roll before being reduced to zero\r\nWillpower, he resists the powers of Hell. In addition, the\r\nsuffering he endured hardens his mind, and this infernal\r\npath may not be used against him again a full year.\r\nIf the victim is reduced to zero Willpower, he must\r\ndo the vampire’s bidding, not speaking, staring blankly\r\nforward, in a state much like a zombie until he has\r\nregained one dot of Willpower, as per the chart below.\r\nIf the infernalist is killed, the victim regains all of his\r\nlost Willpower immediately.\r\nA botch on the part of the infernalist has unique\r\nresults: He loses a number of temporary Willpower\r\npoints that corresponds with his mastery of said path.\r\nThese Willpower points return at a rate of one per night.\r\nIf all points are lost, he may come under the control of\r\notherworldly forces.\r\nThe Willpower siphoned by this power returns at a\r\nrate determined by the infernalist’s rating in the path:\r\n• Return of 3 Willpower points per day’s rest\r\n•• Return of 2 Willpower points per day’s rest\r\n••• Return of 1 Willpower point per day’s rest\r\n•••• Return of 1 Willpower point per week’s rest\r\n••••• Return of 1 Willpower point per two week’s rest",
                },
                {
                    "name": "The Taking of the Spirit",
                    "description": "By calling upon the power of Hell, this path allows\r\nthe infernalist to strip away the temporary Willpower\r\nof her victim, leaving an almost soulless automaton\r\nready to serve the infernalist without question. Some\r\nfiendish vampires have built entire legions of servants\r\nfor themselves with this power. This fearsome path works\r\non vampires and kine alike.",
                    "system": "The infernalist loudly calls forth the legions of\r\nHell to steal away the spirit of her target and then touches her\r\ntarget. Depending upon the circumstances, the Storyteller\r\nmay require a successful Dexterity + Brawl roll for the\r\nthaumaturge to make contact with the intended victim.\r\nOnce contact is made, the infernalist must engage in a\r\ncontested Willpower roll against the subject (difficulty 8).\r\nIf the victim accumulates more successes on this\r\ncontested Willpower roll before being reduced to zero\r\nWillpower, he resists the powers of Hell. In addition, the\r\nsuffering he endured hardens his mind, and this infernal\r\npath may not be used against him again a full year.\r\nIf the victim is reduced to zero Willpower, he must\r\ndo the vampire’s bidding, not speaking, staring blankly\r\nforward, in a state much like a zombie until he has\r\nregained one dot of Willpower, as per the chart below.\r\nIf the infernalist is killed, the victim regains all of his\r\nlost Willpower immediately.\r\nA botch on the part of the infernalist has unique\r\nresults: He loses a number of temporary Willpower\r\npoints that corresponds with his mastery of said path.\r\nThese Willpower points return at a rate of one per night.\r\nIf all points are lost, he may come under the control of\r\notherworldly forces.\r\nThe Willpower siphoned by this power returns at a\r\nrate determined by the infernalist’s rating in the path:\r\n• Return of 3 Willpower points per day’s rest\r\n•• Return of 2 Willpower points per day’s rest\r\n••• Return of 1 Willpower point per day’s rest\r\n•••• Return of 1 Willpower point per week’s rest\r\n••••• Return of 1 Willpower point per two week’s rest",
                },
                {
                    "name": "The Taking of the Spirit",
                    "description": "By calling upon the power of Hell, this path allows\r\nthe infernalist to strip away the temporary Willpower\r\nof her victim, leaving an almost soulless automaton\r\nready to serve the infernalist without question. Some\r\nfiendish vampires have built entire legions of servants\r\nfor themselves with this power. This fearsome path works\r\non vampires and kine alike.",
                    "system": "The infernalist loudly calls forth the legions of\r\nHell to steal away the spirit of her target and then touches her\r\ntarget. Depending upon the circumstances, the Storyteller\r\nmay require a successful Dexterity + Brawl roll for the\r\nthaumaturge to make contact with the intended victim.\r\nOnce contact is made, the infernalist must engage in a\r\ncontested Willpower roll against the subject (difficulty 8).\r\nIf the victim accumulates more successes on this\r\ncontested Willpower roll before being reduced to zero\r\nWillpower, he resists the powers of Hell. In addition, the\r\nsuffering he endured hardens his mind, and this infernal\r\npath may not be used against him again a full year.\r\nIf the victim is reduced to zero Willpower, he must\r\ndo the vampire’s bidding, not speaking, staring blankly\r\nforward, in a state much like a zombie until he has\r\nregained one dot of Willpower, as per the chart below.\r\nIf the infernalist is killed, the victim regains all of his\r\nlost Willpower immediately.\r\nA botch on the part of the infernalist has unique\r\nresults: He loses a number of temporary Willpower\r\npoints that corresponds with his mastery of said path.\r\nThese Willpower points return at a rate of one per night.\r\nIf all points are lost, he may come under the control of\r\notherworldly forces.\r\nThe Willpower siphoned by this power returns at a\r\nrate determined by the infernalist’s rating in the path:\r\n• Return of 3 Willpower points per day’s rest\r\n•• Return of 2 Willpower points per day’s rest\r\n••• Return of 1 Willpower point per day’s rest\r\n•••• Return of 1 Willpower point per week’s rest\r\n••••• Return of 1 Willpower point per two week’s rest",
                },
                {
                    "name": "The Taking of the Spirit",
                    "description": "By calling upon the power of Hell, this path allows\r\nthe infernalist to strip away the temporary Willpower\r\nof her victim, leaving an almost soulless automaton\r\nready to serve the infernalist without question. Some\r\nfiendish vampires have built entire legions of servants\r\nfor themselves with this power. This fearsome path works\r\non vampires and kine alike.",
                    "system": "The infernalist loudly calls forth the legions of\r\nHell to steal away the spirit of her target and then touches her\r\ntarget. Depending upon the circumstances, the Storyteller\r\nmay require a successful Dexterity + Brawl roll for the\r\nthaumaturge to make contact with the intended victim.\r\nOnce contact is made, the infernalist must engage in a\r\ncontested Willpower roll against the subject (difficulty 8).\r\nIf the victim accumulates more successes on this\r\ncontested Willpower roll before being reduced to zero\r\nWillpower, he resists the powers of Hell. In addition, the\r\nsuffering he endured hardens his mind, and this infernal\r\npath may not be used against him again a full year.\r\nIf the victim is reduced to zero Willpower, he must\r\ndo the vampire’s bidding, not speaking, staring blankly\r\nforward, in a state much like a zombie until he has\r\nregained one dot of Willpower, as per the chart below.\r\nIf the infernalist is killed, the victim regains all of his\r\nlost Willpower immediately.\r\nA botch on the part of the infernalist has unique\r\nresults: He loses a number of temporary Willpower\r\npoints that corresponds with his mastery of said path.\r\nThese Willpower points return at a rate of one per night.\r\nIf all points are lost, he may come under the control of\r\notherworldly forces.\r\nThe Willpower siphoned by this power returns at a\r\nrate determined by the infernalist’s rating in the path:\r\n• Return of 3 Willpower points per day’s rest\r\n•• Return of 2 Willpower points per day’s rest\r\n••• Return of 1 Willpower point per day’s rest\r\n•••• Return of 1 Willpower point per week’s rest\r\n••••• Return of 1 Willpower point per two week’s rest",
                },
                {
                    "name": "The Taking of the Spirit",
                    "description": "By calling upon the power of Hell, this path allows\r\nthe infernalist to strip away the temporary Willpower\r\nof her victim, leaving an almost soulless automaton\r\nready to serve the infernalist without question. Some\r\nfiendish vampires have built entire legions of servants\r\nfor themselves with this power. This fearsome path works\r\non vampires and kine alike.",
                    "system": "The infernalist loudly calls forth the legions of\r\nHell to steal away the spirit of her target and then touches her\r\ntarget. Depending upon the circumstances, the Storyteller\r\nmay require a successful Dexterity + Brawl roll for the\r\nthaumaturge to make contact with the intended victim.\r\nOnce contact is made, the infernalist must engage in a\r\ncontested Willpower roll against the subject (difficulty 8).\r\nIf the victim accumulates more successes on this\r\ncontested Willpower roll before being reduced to zero\r\nWillpower, he resists the powers of Hell. In addition, the\r\nsuffering he endured hardens his mind, and this infernal\r\npath may not be used against him again a full year.\r\nIf the victim is reduced to zero Willpower, he must\r\ndo the vampire’s bidding, not speaking, staring blankly\r\nforward, in a state much like a zombie until he has\r\nregained one dot of Willpower, as per the chart below.\r\nIf the infernalist is killed, the victim regains all of his\r\nlost Willpower immediately.\r\nA botch on the part of the infernalist has unique\r\nresults: He loses a number of temporary Willpower\r\npoints that corresponds with his mastery of said path.\r\nThese Willpower points return at a rate of one per night.\r\nIf all points are lost, he may come under the control of\r\notherworldly forces.\r\nThe Willpower siphoned by this power returns at a\r\nrate determined by the infernalist’s rating in the path:\r\n• Return of 3 Willpower points per day’s rest\r\n•• Return of 2 Willpower points per day’s rest\r\n••• Return of 1 Willpower point per day’s rest\r\n•••• Return of 1 Willpower point per week’s rest\r\n••••• Return of 1 Willpower point per two week’s rest",
                },
            ],
        },
        {
            "name": "Awakening of the Steel",
            "reference": "V20 Core; PG 441",
            "type": "Dur-An-Ki",
            "powers": [
                {
                    "name": "Confer with the Blade",
                    "description": "Although few Banu Haqim claim to have actually spoken to a weapon’s soul, blacksmiths and warriors alike have ascribed spiritual qualities to hand-forged blades for centuries. Practitioners of Auspex are familiar with the manner in which inanimate objects can bear impressions of their own history. Confer with the Blade allows a weapon’s wielder to delve into the events that have occurred around his weapon. Some practitioners of this power claim this makes the weapon feel more “comfortable” in their hands, while others speak of the sense of history that an ancient blade bears. The actual impressions only take an instant to gain, though many prefer to spend much longer in contemplation if time permits.",
                    "system": "The number of successes determines the amount of information the sorcerer gains regarding the blade’s history and its present state, as well as all information yielded by a lesser number of successes. With three or more successes, the sorcerer may lower the difficulty on his next attempt to apply a blood-magic ritual to the weapon by one.",
                },
                {
                    "name": "Grasp of the Mountain",
                    "description": "The best scimitar in all creation does its owner no good if it’s lying five yards away from him. Grasp of the Mountain strengthens the spiritual bond between the sword and the swordsman in order to reinforce the wielder’s physical grip on his weapon. A blade that is under the effect of this art never leaves its master’s hand unless he so wills it.",
                    "system": "For the rest of the scene, the character has a number of automatic successes to resist all attempts to disarm him, equal to the number of successes rolled. He cannot accidentally drop the blade (which means his botches are likely to result in self-mutilation in-stead of an empty hand). If the character is somehow disarmed in spite of Grasp of the Mountain, he may call the blade back to his hand by successfully invoking this power again, assuming he has a clear line of sight to the weapon.",
                },
                {
                    "name": "Pierce Steel’s Skin",
                    "description": "At this level of understanding, the sorcerer can com-mand his blade with such precision that he can strike at an opponent’s physical protection rather than his body. The sword transfers its full fury to the intended target, shredding even the toughest chain or plate. This strips away the victim’s defenses, leaving him vulner-  \n\nSuccesses  Result\nOne success  Physical information only: precise length and weight (to the micrometer and milligram), chemical composition (assuming the character understands metallurgy), number of damage dice and type of damage (lethal or aggravated).\nTwo successes Historical overview: when and where the blade was forged, the name and face of its smith, brief glimpses of significant events in its existence.\nThree successes Sorcerous understanding: the type and relative level of power of any enchantments or supernatural enhancements that the blade possesses as well as the name and face of the individual who laid them.\nFour successes Subliminal synthesis: comprehensive knowledge of the sword’s history. For the next seven nights, the character recognizes the taste of any blood that has ever stained the blade if she tastes it herself.\nFive successes Total communion: The sword and the wielder become linked at a level deeper than the physical and more enduring than the immediate. The Storyteller determines  what information the sword holds for the character, but it may include any event in the blade’s history or any aspect of its present existence and condition.able to the next attack. While this power is of limited utility in modern nights, as traditional armor has fallen by the wayside, it remains in the path’s progression of lessons due to its utility in destroying other obstacles.",
                    "system": "While Pierce Steel’s Skin is in effect, an at-tack against an unarmored target inflicts half damage (rounded down). However, for a number of turns equal to the number of successes rolled, each successful at-tack the character makes against an armored foe in-flicts damage on the target’s body armor rather than in-juring him directly. Only metal armor can be damaged by this power. When the character makes a successful attack against an armored target, the player does not roll damage. Instead, he rolls a number of dice equal to the sword’s damage bonus (the number of dice that it adds to his Strength) against a difficulty of 7. Each success reduces the armor’s soak bonus by one die. Ar-mor that is reduced to zero soak dice in this manner is completely destroyed and unsalvageable. Additional successes beyond those needed to destroy a piece of ar-mor have no effect. At the Storyteller’s discretion, Pierce Steel’s Skin may destroy other inanimate objects (walls, doors, cars, dramatically appropriate obstacles) without significant damage to the sword. For the purposes of this power, Fortitude counts as part of the target’s Stamina, not external armor.",
                },
                {
                    "name": "Razor’s Shield",
                    "description": "Many swordsmen hold that the duel is the ultimate test of the warrior because it places all opponents on an equal footing: Death is only three feet of steel away, and only the skill of the combatants determines who walks away. However, observers who are more pragmatic than romantic note that an enemy with a ranged weapon (be it bow, sling, or gun) has the advantage of strik-ing from much farther away than arm’s length. While Awakening of the Steel cannot completely counteract this advantage, this power allows the skilled sorcerer some measure of defense as the sword interposes itself between its master and attacks from afar.",
                    "system": "For a number of turns equal to the number of successes rolled, the character may attempt to parry projectiles. This requires one action for each projectile that the player wishes to block, and the character must be able to see the shot coming (Heightened Senses al-lows visual tracking of bullets). Each parrying attempt requires a Dexterity + Melee roll, with a difficulty de-termined by the speed of the projectile. Thrown ob-jects have a difficulty of 6, arrows and crossbow bolts a difficulty of 7, and bullets a difficulty of 9. Each success subtracts one success from the attacker’s attack roll.Razor’s Shield does not allow the character to parry ranged attacks that do not incorporate solid projectiles, such as flame, lightning, or spat blood.",
                },
                {
                    "name": "Strike at the True Flesh",
                    "description": "Although pacifists may find other uses for blades, a warrior knows that swords were created for one pur-pose: to carve an enemy’s flesh into bloody ruin. Strike at the True Flesh invokes the very essence of the sor-cerer’s weapon, reducing it to the embodiment of its very definition (or, as the more classically minded would put it, invoking the Platonic form) while sim-plifying its target to a similarly basic level. The results of such an invocation are usually devastating on both a philosophical and practical level as weapon and victim momentarily lose all supernatural attributes.",
                    "system": "The effects of Strike at the True Flesh last for a number of turns equal to the number of successes rolled, and they end with the first successful attack that the character makes within this time period. The sword inflicts only the base amount of lethal damage that a weapon of its size and type would normally cause, dis-regarding all enhancements that it may have received (though augmentations to the wielder’s strength or speed, such as Potence and Celerity, still have their nor-mal effects, as do extra successes on the attack roll).However, all the target’s supernatural defenses (in-cluding Fortitude) are likewise negated — he soaks the attack only with his base Stamina. If the negation of his powers and defenses renders the target unable to soak lethal damage, he cannot soak the attack at all. Body armor does protect against this attack, as it is a mundane form of defense.",
                },
            ],
        },
        {
            "name": "Blessings of the Great Dark Mother",
            "reference": "The Black Hand: A Guide to the Tal'Mahe'Ra; PG 86",
            "type": "Dur-An-Ki",
            "powers": [
                {
                    "name": "Cradlesong",
                    "description": "The ashipu utters an incantation that reveals to her the \nnature of any pacts, bonds, or spiritual ties to other beings \nwithin audible range of her voice. These bonds appear differ-\nently to each ashipu who employs the cradlesong, depending \nstrongly on her preferred sensory stimulus. Some see the \nbonds as threads of light wrapped around others, pulsing \nwith colors that define their nature; others hear them as a \nrich and complex song whose internal melodies, harmonies, \ntemp, and beat contain the information they require. Most \nproperly sung, the incantation can also be simply spoken, \nwhistled using the appropriate notes, or plays wordlessly on \na musical instrument as a tone poem; electronic amplification \ncan and does increase its effective range.",
                    "system": 'The ashipu sings her cradlesong, spends on blood \npoint, and rolls Perception+Occult (difficulty equal to the \nhighest current Willpower rating of the individuals in the \ngroup, or the current Willpower rating of the individual \nif attempting to affect a singular target). If succesful, the \nsong causes any and all infernal pacts, spiritual pacts, and \nvoluntary or involuntary bonds of any kind (Including the \nblood bond) to become "visible" in some way to the caster.',
                },
                {
                    "name": "Kessep",
                    "description": 'The firstborn son of Lilith and Lucifer was named \n"Silver" for the light of the Moon, a hue reflected in the \nbright silver scales of the serpent that serves the Great \nDark Mother. The serpent sometimes functions as one of \nher many forms, symbolic of purity and purification. The \nAshipu who calls upon the argent serpent sings, speaks, or \nplays an invocation that allows her to select one infernal \nor spiritual bond and purify the owner of it - severing the \nties of bound spirits or demons. This invocation cannot \nsever the blood bond (no matter how involuntarily it might \nhave been entered into), nor can it undo an infernal pact.',
                    "system": "The ashipu invokes the gift of the argent ser- \npent, spending one blood point and rolling Manipulation \n+ Occult, wih a difficuly equal to the target's curren \nWillpower. If succesful, the invocation causes a single \nselected bond bettween the target and an enthralled spirit \nor bound demon to be broken. This, of course, frees the \npreviously bound spirits or demon to flee, take vengeance, \nor visit whatever consequences of bondage they prefer \nupon their former owner.",
                },
                {
                    "name": "Sotheq",
                    "description": "The second-born son of Lilith and Lucifer was named \n\"Silence\", for the peace and stillness of D'hainu, the Great \nDark Mother's garden of renewal, and is also an attribute \nof the watchful, night-hunting owl that both serves and \nembodies her. The ashipu who calls upon the owl with \nwings of Twilight sings, speaks, or plays an invocation that \nallows her to silence all of the infernal or spiritual ties of \nher target, pacts and bonds alike.",
                    "system": "The ashipu invokes the gift of the twilight owl, \nspending one blood point and rolling Manipulation \n+ Occult, with a difficulty equal to the target's current \nWillpower. If succesful, the invocation causes a psychic \nor spiritual silence to fall across all bonds and pacts in \nwhich the target is involves - he can no longer issue \ncommands to his bound spirits or servitor demons, nor \ncan he receive communication or commands from any \nspirit or demon that hols him in thrall. Exceptional \nsuccess (four successes or more) extends this effect to the \nCainite at the other end of any blood bond in which the \ntarget is engaged.",
                },
                {
                    "name": "Allah",
                    "description": 'The youngest daughter of Lilith and Lucifer was named \n"Night", for the realm that would have been hers had she \nlived to maturity. Such darkness is also an attribute of the \nsoft-pawed, sharp-clawed cat that warded the borders of \nD\'hainu and protected those who dwelt within the Garden \nof Renewal. The ashipu who calls upon the cat with the \npelt of shadow sings, speaks, or plays an invocation that \nallows her to directly assault all of the lesser infernal or \nspiritual tties of their target, parting the bonds as with a \nswipe of deadly claws and disarming the target of their \nspiritual weapons.',
                    "system": "The ashipu invokes the gift of the night-shadow \ncat, spending one blood point and rolling Manipulation \n+ Occult, with a difficulty equal to the target's current \nWillpower, for each spirit or demon that the target holds \nenthralled as a servitor. Success frees the bound spirit or \ndemon to do as it wills. Failure not only fails to free the \nspirit or demon, but also allows those entities to know \nprecisely who attempted to sever those ties.",
                },
                {
                    "name": "Memo",
                    "description": 'The firstborn and eldest child of Lilith and Lucifer was \ntheir daughter, named "Water" after her motther\'s fond \nmemory of both crystal streams of lost Eden and the \nvast oceanic depths in which she took shelter after her \nexpulsion. In the oceans, she bore the first of her many \nbroods and emerged from her exile more powerful than \nbefore. Mighty and deep are tthe powers of htat great pri- \nmordial realm, and might was the form that the Great \nDark Mother took there. She lent the secrets and gifts of \nthat form to her first child and eldest daughter, the drag- \non whose wings blotted out the moon and the sun \nand the stars, and whose scales shone with all the hues of \nthe sea, greatest of all the purifiers. The ashipu who calls \nupon the dragon who weeps tears of salt sings, speaks, or \nplays an invocation that allows her to directly attack the \nprincipal infernal or spiritual pact of her target.',
                    "system": "The ashipu invokes the gift of the great serpent of \nthe ocean, spending one blood point and rolling Perception \n+ Occult, with a difficulty equal to the current Willpower \nof the target. By so doing, she gains the knowledge of \nwhat impelled the target to enter into a bargain in which \nhis soul would be forefeit. Each success rolled yields more \nof the pact, and any infernal investments or gifts that the \ntarget possesses. Spectacular success yields the True Name \nof the target's demonic patron and the opportunity to \ndirectly engage in a contested Manipulation + Occult \n(difficulty equal to it's permanent Willpower) roll. Success \non the part of the ashipu severs the bond between the \ninfernalist and their patron; success on the part of the \npatron allows hte bond ot remain intact. Failure of any \nroll in this sequence allows the infernality's patron to \nperceive the ashipu and derive substantial information \nabout her through the contact.",
                },
            ],
        },
        {
            "name": "Hunter's Winds",
            "reference": "Rites of the Blood; PG 159",
            "type": "Dur-An-Ki",
            "powers": [
                {
                    "name": "Scent of Deception",
                    "description": "The target of this power gains the ability to alter\r\nher scent or eliminate it completely.",
                    "system": "A successful roll means that the target either\r\nleaves no scent that can be detected or tracked, or\r\nshe leaves the scent of someone else known to her.\r\nA failure means nothing happens. A botch means\r\nthat her scent is more easily identifiable to others\r\n(in addition to the other penalties for botching a\r\nblood magic roll).",
                },
                {
                    "name": "Chameleon's Skin",
                    "description": "The target’s skin and clothing automatically assume\r\nthe coloring and texture of whatever he stands near.",
                    "system": "For the duration of the scene following\r\nthe activation scene, the difficulty of all Perception\r\nrolls to detect the target increase by +4 so long as he\r\nremains stationary. While he is in motion, the effect\r\nis negated, but once he comes to rest again against\r\na different surface, he can reassert the camouflage\r\nwith a successful Perception + Stealth roll (difficulty\r\n6, or 9 if someone is actively searching for him at the\r\ntime). Any texture changes are illusory; the target\r\ndoes not gain the durability of a brick wall just by\r\nstanding near it.",
                },
                {
                    "name": "Unassuming Pose",
                    "description": "The target effortlessly blends into any crowd of people.\r\nEveryone present will assume the target belongs there,\r\nincluding any pursuers.",
                    "system": "If the roll succeeds, any observer will\r\nautomatically assume that the target belongs in whatever\r\nlocation he is found. Those searching for him are incapable\r\nof perceiving that he is an intruder. However, this effect\r\ncannot fool technology, and anyone observing through\r\nCCTV, for example, can spot him as an interloper.",
                },
                {
                    "name": "Whiff of Kalif",
                    "description": "The target of this effect generates an aura which is\r\nphysically intoxicating to anyone who directly observes\r\nher. Those affected may experience a pleasant daydream,\r\nor may just be left standing slack-jawed as the target goes\r\non his way.",
                    "system": "If the effect is successfully activated, anyone\r\nwho observes the target during the rest of the scene must\r\nreflexively roll Wits + Alertness (difficulty 7) or become\r\nintoxicated for a number of hours equal to the ashipu’s\r\nsuccesses in triggering the effect. Affected individuals are\r\nincapable of taking any action beyond staring vacantly\r\nat visions only they can see or perhaps giggling from\r\ntime to time. However, any direct threat to an affected\r\nindividual immediately causes the intoxication to fade.",
                },
                {
                    "name": "Ghost Body",
                    "description": "As a particularly powerful effect, Ghost Body requires the\r\nashipu to expend three points of blood instead of the normal\r\none. When the effect is activated, the target becomes completely\r\ninvisible, inaudible, and intangible, and she can move freely\r\nthrough any barriers other than wards against vampires.",
                    "system": "If activated successfully, the target becomes\r\nimmaterial in nearly every sense. The effect does not make\r\nher into a true ghost, and she is incapable of interacting\r\nwith wraiths or spirits while in this form. She is also\r\nincapable of using any Disciplines while in this form.\r\nThe effect ends as soon as the target makes the conscious\r\ndecision to affect the physical world in any way.",
                },
            ],
        },
        {
            "name": "Path of the Evil Eye",
            "reference": "Rites of the Blood; PG 161",
            "type": "Dur-An-Ki",
            "powers": [
                {
                    "name": "Humiliation",
                    "description": "The simplest application of the Evil Eye causes the target \nto embarrass himself in some public way. Possible results \ninclude saying something embarrassing in front of one’s \npeers, failing disastrously at a feeding attempt, or simply \nripping the seat out of one’s pants while in a crowded bar.",
                    "system": "Each success represents one night during which \nthe target is affected by the curse. The curse triggers \nonce per night at a time of the Storyteller’s choosing, \nusually the scene during which the character is in front \nof the largest number of individuals or in which he is in \nfront of the largest number of socially important people. \nThat is, it may trigger while the character is in a crowded \nrestaurant or when he is alone with the Prince, whichever \nhas the greatest potential for personal embarrassment. \nThe Storyteller determines when the curse triggers, but \nit should do so at least once per night. \nDuring the trigger scene, on every Social roll made for \nthe character, the player must add a number of automatic \n1s equal to the sorcerer’s rating in the Path of the Evil Eye, \nthereby increasing the likelihood of a botch on a Social \nroll. In addition, during the trigger scene, the Storyteller \nshould roll a number of dice equal to the sorcerer’s rating \nin this path (difficulty 5). Successes mean that some \nexternal event happens that causes embarrassment to \nthe character, such as a waiter spilling drinks on him or \na car splashing him with mud.",
                },
                {
                    "name": "Loss",
                    "description": "This curse affects the target’s material worth. It most \ncommonly causes the target to be stripped of money, but it \nmay also cause her Herd to diminish, or destroy a Haven. \nThe curse can target any tangible asset represented as a \nBackground. If the character has no suitable Backgrounds, \nit targets personal items of emotional significance.",
                    "system": "Within one week, the target loses one dot \nfrom an appropriate Background. Generally, the curse \npreferentially attacks Resources over other backgrounds, but theoretically any form of tangible Background representing a personal asset can be a valid target. The sorcerer has no control over how the Background point is lost or even which Background point is lost. The Storyteller may even choose to decide randomly.",
                },
                {
                    "name": "Peril",
                    "description": "At this level of mastery, the ashipu may finally endanger \nher enemy rather than merely inconvenience her. The \ncurse cannot directly harm the target, but it can create \na situation in which it is possible for her to be harmed, \nwhether at the hands of a drunken lout who takes offense \nto the target’s manner at a bar or a pack of werewolves \nwho, by happenstance, choose to board the same lonely \nsubway car as the victim.",
                    "system": "The number of successes determines how many nights the character is at risk. At the start of each night, the Storyteller must roll a die and, depending on the results, fashion an encounter for the targeted character. \nDice Result Nature of Peril\n 1-3  None. The curse does not trigger during this \n      night.\n 4-6  Minor: An encounter which is not likely to \n    harm the character but which has a chance \n    to do so. A mortal tries to mug the character \n    while she is in front of mortals, or simply \n    tries to hold up a convenience store while \n    the character is in line paying for gas. A \n    bar patron takes offense to something the \n    character does or says and tries to pick a \n    fight.\n 7-8  Moderate: An encounter with a significant \n    likelihood of at least some harm to the \n    character. The character is involved in a \n    car wreck or struck by a hit-and-run driver. \n    Stairs give way while the character is \n     climbing them.\n 9  Severe: An encounter in which the \n    character is almost certain to suffer some \n    lethal damage. The character inadvertently \n    says something offensive that provokes \n    frenzy rolls in nearby vampires. The \n    building collapses while the character is in \n    it or a fire breaks out.\n 10  Catastrophic: An encounter that is potentially deadly.    The character’s is locked out of his haven during the    day. The character unwittingly says something that    offends a pack of nearby Lupines.\n\n Nights on which there is no peril do not count against \nthe ashipu’s successes; the curse will continue until the \ntarget has suffered a number of dangerous encounters \nequal to the successes or the curse is lifted. During any \ndangerous encounter, a targeted character has a chance \nto realize she is under a curse (if she didn’t already know \nit). The roll is Intelligence + Occult. The default difficulty is 9, but it drops to 8 if the character has Auspex or to 6 if the character has any knowledge of this Path.",
                },
                {
                    "name": "Enemy",
                    "description": "This potent curse causes the target’s friends and allies \nto turn against him, even as it causes the numbers of his \nenemies to grow.",
                    "system": "For each success on the Willpower roll, the \ntarget loses one dot of Allies, Contacts, Influence, or \nRetainers. This may reflect friends and allies who have \nbecome angry with the character and turn their back on \nhim, it may reflect contacts and allies who are simply \nunavailable for a time, or it may actually result in such \ncharacters being injured or even dying due to ill fortune. \nAlternatively, the player may choose to spend some or all of the successes to give the target a new Enemy (as per the Enemy Flaw) who arrives to pursue a vendetta against the character. Regardless, the effects manifest within a week, and the player of the targeted character may neither regain lost Backgrounds nor remove the Enemy Flaw without learning about and neutralizing the curse.",
                },
                {
                    "name": "The Eye that Wounds",
                    "description": "The ultimate expression of this malefic path, the \nEye That Wounds does not require time to establish a \nchain of ill fortune. It strikes immediately. The ashipu \nmust make eye contact with her target and utter some \nexclamation pertaining to a characteristic of his. It can \nbe praise or insult, sarcasm or fury, but whatever form it \ntakes, the target is immediately struck with an agonizing \ninjury that damages that characteristic.",
                    "system": "While the curse allows for flexibility, the default \nassumption is that for every two successes (rounded up), the target (or object, if the curse is directed towards a possession of the target) suffers one level of aggravated damage. Generally, even a single level of damage is sufficient to slay an animal or destroy most objects. If used against a mortal, this power will permanently maim him. If used against a Kindred, the curse will inflict damage shaped by the ashipu’s words. If she compliments his beautiful eyes, they will be burned and he might be rendered blind until he can heal. If she mocks his honeyed words, the curse might burn out his tongue and leave him unable to speak. This curse may be transmitted through an effigy, but the normal difficulty penalty imposed for using an effigy increases by +2 (see Principles of Contagion and Sympathy on pp. 133-135).",
                },
            ],
        },
        {
            "name": "Kraina of Enoch",
            "reference": "The Black Hand: A Guide to the Tal'Mahe'Ra; PG 170",
            "type": "Koldunic Sorcery",
            "powers": [
                {
                    "name": "Shroud of Oblivion",
                    "description": "Existence in the Underworld grants Cainites certain\r\nadvantages not available on the Earth; the koldun tears\r\nout a piece of the Underworld’s fabric to saturate the area\r\naround him with its attributes.",
                    "system": "The koldun spends a Willpower point, then\r\nmakes the activation roll (Attribute: Stamina). With a\r\nsuccess, the koldun’s skin turns to ash and crumbles to\r\nnothing, exposing his meat to the elements. He plunges his\r\nhands into the earth, parting any impediment as if it were\r\nfresh tilled soil, and wrenches forth an insubstantial sheet\r\nof inky night, yanking out a piece of the Underworld with\r\nwhich to wrap himself. Once donned, the appearance of\r\nanything blanketed by the shroud becomes visibly muted;\r\nin the physical world, all beneath its shield resembles\r\nblack-and-white television images in a full color world,\r\nwhile in the Underworld, things take on a more ghastly\r\nhue of deeper darkness and decay.\r\nShroud of Oblivion centers on and follows the koldun.\r\nThe power has a radius of five feet/two meters per success\r\nscored on the activation roll, and a duration (in turns)\r\nequal to the successes. All those within the radius benefit\r\nfrom the shroud’s effects. The effects of this power differ\r\naccording to what land the koldun is currently located\r\n(see the sidebar “Vampires in the Underworld” on p. 119):\r\nwhile in the mortal world, damage from sunlight lessens\r\nto bashing. If anywhere in the Underworld, the faint sun\r\ndeals no damage.\r\nWhen the duration of the power expires, the koldun\r\nbleeds out, losing one point of blood each turn until\r\nhe expends a blood point to rejuvenate his skin (unless\r\nin the Underworld, in which case no blood is lost).\r\nPenalties sustained to activate this power are tallied after\r\nthe duration ends. Healing prior to that time suspends\r\nthe power’s effects.",
                },
                {
                    "name": "Spectral Cloak",
                    "description": "By harnessing the sight of the dead, the koldun aggrieves\r\nthose in the vicinity with a glimpse of the world\r\nbeyond that of the living. Spectral Cloak conceals the\r\nkoldun from unfriendly eyes and drives away unwanted\r\nobservers in terror.",
                    "system": "The koldun plucks out her eyes, crushes them\r\nin her hands, and extends her palms to the sky, then\r\nmakes the activation roll (Attribute: Perception). With\r\na success, the pulp turns to dust and takes flight on an\r\neerie howl of wind that pours from a fathomless darkness\r\nwithin her empty sockets. Shadows drawn from the surroundings\r\nengulf the koldun who vanishes, rendering her\r\ninvisible to standard vision (for those with Auspex, see\r\nthe sidebar “Seeing the Unseen” on p. 142 of V20, using\r\nthe koldun’s rating in this kraina). Though the koldun\r\nsees normally inside the radius of the power’s effect, she\r\nis blind to anything outside of this area. Others within\r\nthe radius must succeed on a Willpower roll (difficulty\r\nequal to the koldun’s rating in the kraina plus successes\r\nscored on the activation roll, maximum 9), or be afflicted\r\nwith the Deathsight Flaw (V20, p. 494) and attempt to\r\nflee in fright for a number of turns equal to the successes\r\nscored on the activation roll.\r\nThe power’s radius centers on and follows the koldun,\r\nallowing her to move about and act on others, even\r\nviolently, without being revealed. Spectral Cloak has a\r\nradius of ten feet/three meters per success scored on\r\nthe activation roll and a duration (in turns) equal to the\r\nsuccesses. When the duration of the power expires, the\r\nkoldun is abandoned to blindness until she expends one\r\nblood point to heal (unless in the Underworld, where the\r\nkoldun may continue to see indefinitely, despite the loss\r\nof her eyes). Penalties sustained to activate this power are\r\ntallied after the duration ends. Healing prior to that time\r\nsuspends the power’s effects.",
                },
                {
                    "name": "Pond of Malevolent Dread",
                    "description": "Nestled just above the abyss in the Underworld, no place\r\nis more frigid, devoid of light, tenebrous, or bleak than\r\nthe Sea of Shadows, an ocean of souls on the precipice of\r\ntotal annihilation. The koldun forms a shaft to sup from\r\nthe doom of this sea and release its flow.",
                    "system": "The koldun spends a turn eviscerating himself,\r\nthrusting his hands deep in his abdomen to expel his\r\nentrails onto the ground, then makes the activation roll\r\n(Attribute: Stamina). With a success, his bowels bore\r\nthrough the earth past any obstruction blocking their path,\r\nthen cross over the threshold which separates the vibrant\r\nlands of the living from the desiccated lands of the dead.\r\nHis entrails touch the very depths of the Underworld’s\r\nbottom layer, taking root in the Sea of Shadows. The\r\nvampire drains its essence into himself and discharges\r\nit outward in pulsating waves of despair that bubble up\r\nTHE BLACK HAND: A GUIDE TO THE TAL’MAHE’RA 171\r\nthrough the earth to ring him in a liquid pool of\r\nseething, writhing spectres. Ghostly arms stretch out\r\nto clutch and feast upon those walking through the\r\ncircle’s radius. The rippling pool centers below the\r\nkoldun, who remains locked in place from the waist\r\ndown until the power ends.\r\nThe power has a radius of fifteen feet/five meters per\r\nsuccess scored on the activation roll and a duration (in\r\nturns) equal to the successes. All those within the radius\r\nhave their speed slowed to ¼ and must succeed at a\r\nWillpower roll each turn (difficulty equal to the koldun’s\r\nrating in the kraina plus successes scored on the activation\r\nroll, maximum 9) or lose 1 point of permanent Willpower.\r\nWhen the duration of the power expires, the koldun\r\nsevers his viscera buried in the earth and incurs two\r\nlevels of unsoakable lethal damage. This damage cannot\r\nbe healed by any other means other than by spending\r\nblood. Additionally, the koldun loses an amount of\r\nblood points equal to half the successes scored on the\r\nactivation roll, rounded up (unless in the Underworld,\r\nin which case no blood is lost). Wounds sustained to\r\nactivate this power are tallied after the duration ends.\r\nHealing prior to that time suspends the power’s effects.",
                },
                {
                    "name": "Wrath of the Tempst",
                    "description": "roiling, limitless typhoon made of fractured memories,\r\nbroken dreams, nightmares, fear, and misery.\r\nThe koldun summons the death rattles of all whom\r\nshe has vanquished, pricking a hole in the barrier\r\nbetween worlds to let bleed the metaphysical storm.",
                    "system": "The koldun spends one Willpower point\r\nand lifts her head to the sky, then makes the activation\r\nroll (Attribute: Strength). With a success, she opens\r\nher mouth and a choir of voices not her own issue a\r\ndeafening cry that blends into thunder as storm clouds\r\ngather above her for the remainder of the turn. A\r\nstill silence follows as the koldun stands frozen, her\r\nexpression transfixed, echoing the call. Moments later,\r\na roaring hurricane explodes around her, breaching\r\nforth from the land of the dead with all the fury of\r\nthe Underworld. Its eye, a focused funnel, descends\r\ninto the koldun’s mouth, causing her to convulse and\r\nwrithe as she rises thirty feet into the air.\r\nThe tempest has a radius of twenty feet/seven meters\r\nper success scored on the activation roll and a duration\r\n(in turns) equal to the successes. All those within the\r\nradius must succeed on a Willpower roll (difficulty 8)\r\neach turn or gain a derangement and enter a strange\r\nfugue state (described on p. 291 of V20) called a\r\n172 CHAPTER FOUR: DIRTY SECRETS\r\n“Harrowing” as the storm warps memories, trapping those\r\nwithin in an internal labyrinth of regret, depression, and\r\nhopelessness for the rest of the scene. While the storm\r\nrages, the koldun is mindless and completely unaware of\r\nher surroundings; she sustains one level of unsoakable\r\nbashing damage each turn as the tempest pounds her from\r\nwithin (unless in the Underworld, in which case the bashing\r\ndamage may be soaked normally). Penalties sustained\r\nto activate this power are tallied after the duration ends.\r\nHealing prior to that time suspends the power’s effects.",
                },
                {
                    "name": "Hunger of the Void",
                    "description": "The koldun embodies the distortions of the Tempest,\r\ntorturing his soul to cleave a pit of perfect destruction\r\ninto reality.",
                    "system": "The koldun spends a Willpower point, reaches\r\ndown his throat, and pulls out his own soul. He spends\r\na turn tormenting and stretching the spirit’s mouth ever\r\nwider as it mutely protests, clawing impotently at its violator\r\nin shocked disbelief. He tosses the contorted soul to the\r\nearth at his feet, then makes the activation roll (Attribute:\r\nStrength) before diving into it. With a success, the giant\r\nmaw transforms into a cavity five feet in circumference that\r\nbegins sucking in all it can to appease its insatiable appetite.\r\nThe power has a radius of twenty five feet/eight meters\r\nper success scored on the activation roll and a duration\r\n(in turns) equal to the successes. All those within the\r\nradius are dragged ten feet/three meters per turn toward\r\nthe Nihil, and have their speed slowed by half every five\r\nfeet/two meters nearer they are to it. If consumed by the\r\nmaw, they disappear and must make a Willpower roll\r\n(difficulty 9). After the power ends, the Nihil implodes,\r\nleaving an enormous crater in its wake. At the base of\r\nthe crater lies the koldun with all the maw has consumed\r\nresting on top of him. Characters who have failed the\r\nroll are turned into mindless creatures, their virtues and\r\nmorality stripped from them completely and reduced to\r\nzero. Vampires succeeding on the roll enter a Harrowing\r\n(see Wrath of the Tempest) for the rest of the scene and\r\ngain a derangement. Regardless of success or failure, any\r\nmortal consumed by the pit has its soul obliterated and\r\nenters a permanent coma.\r\nA vampire’s undead stasis cannot incarnate this otherworldly\r\nenergy. Upon the power’s conclusion, fissures\r\nof unfiltered nothingness shred the koldun’s soul from\r\nwithin as searing chars erupt to split the flesh across his\r\nentire frame (inflicting two levels of aggravated damage).",
                },
            ],
        },
        {
            "name": "Kraina of the Well",
            "reference": "The Black Hand: A Guide to the Tal'Mahe'Ra; PG 172-173",
            "type": "Koldunic Sorcery",
            "powers": [
                {
                    "name": "Call the Children",
                    "description": "In order to command a thing, one should venture to\r\nknow it. Demons, much like dogs, always endeavor to\r\ncome when called by their masters. The technique of\r\nconjuring forth Hell’s dwellers has ever been a staple at\r\nthe table of infernal practice.",
                    "system": "Necessitating a full scene of uninterrupted focus\r\nand the expenditure of one blood point to enact, the\r\nkoldun performs a long series of incantations while tracing\r\nglyphs surrounding a circle in his own blood around the\r\nentrance to his Well of Sacrifice. The power and strength\r\nof a demon the koldun is capable of summoning rises proportionate\r\nto the level of his advancement in the kraina.\r\nAs the koldun’s skill in the kraina rises, so, too, does his\r\nability to invoke demons of increasing power. Over the\r\ncourse of the scene he makes an extended invocation roll\r\n(Attribute: Wits), requiring an amount of successes equal\r\nto the difficulty level of the demon summoned.\r\nMaximum\r\nPower\r\nDifficulty\r\nLevel\r\nType/\r\nFreebie Points\r\nKraina Level 1 5 Successes Fallen Tempter\r\nKraina Level 2 6 Successes Fallen Tempter:\r\n+30\r\nKraina Level 3 7 Successes Fallen Tempter:\r\n+55\r\nKraina Level 4 8 Successes Earthbound Defiler\r\nin Darkness\r\nKraina Level 5 9 Successes Earthbound Defiler\r\nin Darkness: +30\r\nDemons use the statistics presented on pp. 386-387 of\r\nV20. Storytellers should freely exchange specific Abilities\r\nand Disciplines for others and vary Attribute scores to\r\nsuit the needs of their game. Demons invoked through\r\nCall the Children are not in possession of a mortal host,\r\nretaining the countenance of their Apocalyptic Form\r\ndescribed under Powers and Weaknesses. Without being\r\nbound, a demon cannot exit the confines of the summoning\r\ncircle within and will be ripped back into Hell\r\nafter a number of turns equal to the difficulty level of its\r\nconjuration have expired. The demon can communicate,\r\nbut generally demand an exchange of goods or services\r\n(sometimes even a contract) for any information asked\r\nof them, and even then, there’s no guarantee they need\r\nanswer truthfully. The player may choose to summon the\r\nsame demon again at a later date if a bargain was struck but\r\nunfulfilled before the conclusion of the power’s duration.\r\nTwo or more koldun with this power may elect a primary\r\nsummoner and work in concert to invoke an entity. The\r\ndifficulty level is reduced by one (minimum 4) for each\r\nkoldun assisting in the invocation.",
                },
                {
                    "name": "Heed the Hell-bound Heart",
                    "description": "Whether by blessing or familiarity, a koldun who drinks\r\nfrom her Well gains a supernatural sense that alerts her\r\nwhen demonic influence is near, wielding the ability to\r\nscan places, objects, or beings corrupted by the stamp of\r\ninfernal company.",
                    "system": "By sipping a blood point directly from her\r\nWell, the koldun adds her levels attained in Kraina of\r\nthe Well to her Awareness Ability for detecting demonic\r\ninfluence in areas tainted by its presence or souls stained\r\nby its touch. This effect last for as long as the blood point\r\nremains in her system. Blood is always consumed in the\r\norder it was ingested.",
                },
                {
                    "name": "Aegis Alighieri",
                    "description": "Named in the modern nights for the famed Venetian\r\npoet, Aegis Alighieri shields the koldun from violating\r\nonslaughts, predations, and defilement by demonic forces.",
                    "system": "The koldun lacerates a vein, spending one turn\r\nand a blood point to coat an amulet in her blood, then\r\nmakes the activation roll (Attribute: Charisma). For the\r\nremainder of the scene, the koldun adds successes scored\r\non the activation roll to the difficulty rating for supernatural\r\nattacks and influences of infernal origin used to\r\ntarget her (such as infernally blessed objects, Investments\r\nand Gifts, or any Disciplines and blood sorcery powers\r\nwielded by infernalists and demons). She also gains an\r\namount of extra dice on rolls to resist those same effects\r\nequal to the amount of successes scored. Any mundane or\r\nmystical object may be consecrated as an amulet; popular\r\nchoices include ceremonial daggers, shamed crucifixes,\r\nor decapitated heads that animate to scream endlessly\r\nin silence. However, only the koldun benefits from the\r\nprotection granted through Aegis Alighieri and must have\r\nthe amulet on her person for this power to function. Prior\r\nto activating this power, the koldun is required to have\r\ndipped the amulet in her Well, letting it soak therein for\r\none full night. Two or more koldun working together\r\nin close proximity (within 50 feet/15 meters) grant each\r\nother one extra success on resistance rolls and increase\r\nthe difficulty to target by one (maximum 9) for all koldun\r\npresent with this power activated.",
                },
                {
                    "name": "Heave the Host of Hell",
                    "description": "After learning to call, to sense, and then to defend\r\nagainst infernal marring, the koldun now may erase its\r\nscars entirely.",
                    "system": "The koldun creates a link to his Well by molding\r\nor digging a bowl-shaped impression (minimum one\r\nfoot/30 cm in diameter) into the earth and christening\r\nit with one blood point. He chants a litany of admonishments\r\nand curses while sprinkling the blood on the area\r\nor baptizing the subject he intends to exorcize, then makes\r\nthe activation roll (Attribute: Manipulation).\r\nTo cleanse an area, being, or thing of infernal imprint or\r\nevict a demonic entity, an amount of successes are required\r\nrelative to the degree of corruption infused (1 to 2 for minor\r\nblemishes, 3 for subtle infections of noticeable evil, 4 or\r\nmore for objects and spaces radiating a palpably potent\r\nmalevolence). Infernalists imbued with the diabolical and\r\ndemonic spirits disgracing an area with their presence\r\n(or directly in possession of beings, locations, or things)\r\n174 CHAPTER FOUR: DIRTY SECRETS\r\nmay resist by spending a Willpower point, then rolling\r\nWillpower (difficulty equal to the koldun’s permanent\r\nWillpower rating). Demons failing the roll are dismissed\r\nand banished back to Hell. Cleansed infernalists do not\r\nregain their damned souls, but any infernal mark that once\r\npermeated there being is permanently expelled.\r\nOne or more koldun with Heave the Host of Hell may\r\nassist a primary exorcist to negate an infernal blight. The\r\ndifficulty level to cleanse or evict is reduced by one (minimum\r\n4) for each koldun aiding in the exorcism.",
                },
                {
                    "name": "Reap the Well",
                    "description": "Kolduns who attain full mastery in Kraina of the Well\r\nearn the sobriquet of “Hellreaper” by their peers, and\r\nfor good reason.",
                    "system": "Upon summoning a demon or discovering an\r\nescapee unfettered and loose outside the prison of Hell,\r\nthe koldun may attempt to bind and enslave the creature\r\nto her will. The koldun cuts her wrists, taking a turn to\r\npool one blood point in her cupped hands in order to\r\nfabricate a connection to her Well. When ready, she spends\r\na Willpower point and makes the activation roll (Attribute:\r\nStrength). The blood leaps from her hands in the form\r\nof six interlocking hooked chains anchored beneath her\r\nslit wrists which lunge toward the target with unerring\r\nprecision (maximum 100 feet/30 meters). If the roll is a\r\nsuccess, the blood-hooks painfully latch into the entity,\r\ncreating gory wounds (no damage) regardless of whether the\r\ncreature possesses a physical form. An ensnared creature\r\nmay struggle to break one chain per turn by spending a\r\nWillpower point, then rolling Willpower (difficulty equal\r\nto the koldun’s permanent Willpower rating).\r\nFor as long as the hooks penetrate the entity’s body,\r\nonce per turn the koldun may demand its True Name, tormenting\r\nthe demon by rolling Intelligence + Intimidation\r\nagainst the target’s current Willpower points to wrack its\r\nsoul with excruciating pain. With a success, the victim\r\ncries out the answer in supplication. The koldun has\r\ntwo choices: she may unshackle and dismiss the demon\r\nthrough Heave the Host of Hell, or absorb it into herself.\r\nA koldun that has acquired a demon’s True Name\r\nreduces the difficulty level by two when evoking it at a\r\nlater date through Call the Children. Demons bound by\r\ntheir True Name may exit the confines of a circle they’ve\r\nbeen invoked within, and can be commanded by a koldun\r\nto complete a number of tasks for a number of days\r\nequal to the successes scored on the in vocation roll. The\r\ndemon will answer any of the koldun’s questions, and the\r\nkoldun does not need to offer an exchange of services for\r\nquestions or tasks.\r\nIf choosing to absorb a chained demon, the koldun\r\nmay spend a blood point to instantly call it forth again.\r\nChained demons are wholly compliant and serve the will\r\nof the koldun in whatever capacity she demands, but must\r\nremain in bondage (maximum 100 feet/30 meters) to the\r\nkoldun. A koldun can control up to six chained demonic\r\nthralls; each chain divided decreases the amount of chains\r\navailable for future binding and increases the difficulty to\r\ntorment untamed demons by one.\r\nA demon who disobeys or lies to a summoner who\r\nknows its True Name when conjuring it causes a demon\r\ncrippling agony. Should Reap the Well be used to perform\r\na violent exorcism on a living host possessed by a demon,\r\nthe host rolls Stamina against a difficulty equal to the\r\namount of turns taken to tame the demon into revealing\r\nits True Name. A failure results in the host dying of shock.\r\nMultiple koldun may Reap the Well together, collectively\r\ndecreasing the difficulty to torment a demon by one per\r\nchain (minimum 4). The Hellreaper who successfully extracts\r\nthe demon’s True Name on their turn may choose\r\nto bind it or dismiss it. All koldun present hear the demon\r\nhowl its True Name, and if dismissed, may individually\r\nconjure it. A demon in thrall to a Hellreaper cannot be\r\nevoked until released from service.",
                },
            ],
        },
        {
            "name": "Way of Earth",
            "reference": "V20 Core; PG 448",
            "type": "Koldunic Sorcery",
            "powers": [
                {
                    "name": "Grasping Soil",
                    "description": "A kolduninvoking this power may command earth to rise in a spray of dirt and crawl up a victim’s legs. This power can only command soil, not stone, and may only target victims standing on the earth.",
                    "system": "The koldun may direct any patch of earth within a 100-foot/30-meter radius to ensnare a target for two turns per success rolled. Animated dirt ascends and constricts midway between the victim’s knees and hips, holding her fast unless her player scores five suc-cesses on Strength + Survival roll (difficulty 6). It is also possible to use this power as an attack, in which case the grasping earth crushes once and then releases. Used in this manner, each success on the casting in-flicts one level of lethal damage. Such damage mani-fests as broken legs and crushed feet.",
                },
                {
                    "name": "Endurance of Stone",
                    "description": "Drawing the essence of earth into himself, a koldun may gain a measure of its preternatural resilience. Un-der the effects of this power, a vampire’s skin resembles a horrid fusion of flesh and stone that cracks and flows impossibly with every movement.",
                    "system": "A successful activation roll grants the kol-dun two extra dots of Stamina for the rest of the scene. These dots are considered part of the character’s natu-ral Stamina and may aid in any uses of that Attribute, including soak.",
                },
                {
                    "name": "Hungry Earth",
                    "description": "Expanding on the power of Grasping Soil, a koldun may use this power to drag a victim into the earth. He need only gesture and the soil beneath his victim opens like the maw of a great beast. This power may ensnare any victim who stands upon the earth within 100 feet/30 meters of the koldun.",
                    "system": "Like Grasping Soil, every success on the ac-tivation roll leaves the victim immobile for one turn. However, the difficulty of the Strength + Survival roll to break free increases to 8 and doing so still requires five successes. As the earth continues to shift and grasp while the power remains active, this roll must be made as a single (though repeatable) attempt rather than an extended test. In addition, beings trapped in the crush-ing pit suffer one level of lethal damage each turn. Be-ings capable of soaking this damage may do so, but at difficulty 7. At the end of the power’s duration, the earth yawns once more to release the victim.",
                },
                {
                    "name": "Root of Vitality",
                    "description": "As with Hungry Earth, the koldun may direct the land to bury any target standing on the earth within a 100-foot/30-meter radius. Yet this power is far more benevolent in its intent, if no less disturbing in its manifestation. The soil ripples, parting and closing like some obscene womb as it draws the target a full yard beneath the surface. Living beings entombed in this fashion do not suffocate, as the enchanted soil pumps air from above in undulating breaths. Better still, the fertile essence of the earth presses upon her flesh and restores it to new health. Still, the process is highly disturbing and unnatural, especially as targets remain wholly aware in silent, helpless immobility for the full duration. It is possible for a koldun to heal himself with this power.",
                    "system": "The player spends as many blood points as desired (which may require multiple turns depending on Generation) and makes the activation roll. Each success permits the earth to heal two levels of bash-ing damage or one level of lethal damage. Healing ag-gravated damage requires two successes per level. The total number of health levels that may be restored with each use of this power is the number of blood points invested or the number of successes on the activation roll, whichever is lower. Any blood points spent be-yond the number of successes drain away to no effect. The actual healing process takes one turn per bashing level, one minute per lethal level, and one hour per aggravated level. Once the healing is complete or the power is interrupted through determined excavation, the earth expels the target back to the surface.",
                },
                {
                    "name": "Kupala’s Fury",
                    "description": "Mortals pray in fear when the mountains shake. They fear the wrath of the Old Gods, and rightfully so. This is not a power used lightly or capriciously, because it represents one of the greatest weapons available to Koldunic Sorcery.",
                    "system": "This power requires a Willpower point in addition to the usual cost and activation roll. The kol-dun smites the earth with his fist, and his anger flows through the soil to any target in his line of sight. The quake erupts outward from that point, inflicting 10 dice of lethal damage on everything and everyone in the area of effect. Most wooden structures collapse entirely and even buildings of concrete and steel may grow cracked and pitted with superficial damage from the shaking earth. This tremor lasts one turn and af-fects an area determined by the number of successes rolled. It is not possible to apply fewer successes than those rolled.  Successes Area1 success One house or single storefront2 successes Five lesser structures or a small city block3 successes An entire side street or a large  city block4 successes Multiple square blocks or a large structure (like a stadium)5 successes An entire neighborhood or massive industrial complex",
                },
            ],
        },
        {
            "name": "Way of Fire",
            "reference": "V20 Core; PG 452",
            "type": "Koldunic Sorcery",
            "powers": [
                {
                    "name": "Fiery Courage",
                    "description": "No vampire can master an element he fears, so this power\r\ndims that fear to a mere ember of its former intensity.",
                    "system": "Once learned, this power is permanent and\r\nrequires no activation roll or blood. The koldun subtracts\r\nhis rating in the Way of Fire from the difficulty\r\nof Courage rolls to resist Rötschreck from exposure or\r\nproximity to flame. This power does not aid in resisting\r\nthe panic that accompanies sunlight or any other\r\ncauses apart from actual fire. If this reduces the difficulty\r\nof a Courage roll below two, the koldun simply\r\ndoes not succumb to the Red Fear. Koldun never risk\r\nRötschrek from fire and magma they conjure.",
                },
                {
                    "name": "Combust",
                    "description": "The Cainite’s eyes flash vivid orange with sorcerous\r\npower as superheated air coils around the target. In\r\nmoments, the target bursts into spontaneous flame.",
                    "system": "For every success on the activation roll, the\r\ntarget suffers one level of aggravated damage. This attack\r\nmay be dodged, but not blocked, and can affect\r\nliving (or unliving) beings at +2 difficulty. It is only\r\npossible to make one fiery attack per turn.",
                },
                {
                    "name": "Wall of Magma",
                    "description": "The koldun raises his hand and the earth splits,\r\nspraying a wall of glowing magma 10 feet/3 meters\r\nhigh. Normally, this wall forms a 10-foot/3-meter radius\r\ncircle around the vampire, although the sorcerer\r\ncan raise other shapes with practice and skill.",
                    "system": "The wall of magma summoned with this\r\npower has a lifespan of two turns per success rolled. If\r\nthe koldun wishes to release the magma along a shape\r\nother than a protective circle, increase the base difficulty\r\nby one. Characters cannot approach a wall of\r\nmolten rock without a Courage roll (difficulty 8), and\r\neven then, the close blistering heat inflicts a level of\r\naggravated damage. Actual contact with the lava increases\r\nthe damage to three levels and raises the soak\r\ndifficulty to 9, assuming any sort of soak is possible. The\r\nkoldun takes no damage from his proximity to the summoned\r\nmagma (although contact with it still damages\r\nhim as normal).",
                },
                {
                    "name": "Heat Wave",
                    "description": "The koldun acts as a conduit for steam geysers and\r\nchannels a blast of desiccating air at a victim within\r\nline of sight. This fiery wind appears as a rippling heat\r\nwave enveloping the victim. Individuals slain with\r\nthis gruesome power appear as withered, mummified\r\nhusks.",
                    "system": "On a successful activation roll, the victim\r\nsuffers five levels of lethal damage that may be soaked\r\nby beings capable of such. Vampire targets also lose five\r\nblood points, regardless of the damage inflicted.",
                },
                {
                    "name": "Volcanic Blast",
                    "description": "At the final mastery of Way of Fire, a koldun commands\r\nlava to explode from the ground in a huge geyser.\r\nThe molten rock spews across a wide swath before\r\ncrashing to earth and flowing in all directions. Anything\r\nin the path of the molten rock burns, melts, or\r\nvaporizes within moments. The caster may direct the\r\nlava to erupt anywhere in his line of sight.",
                    "system": "This power costs one Willpower point in addition\r\nto a blood point. For every success on the activation\r\nroll, the initial lava burst lasts one turn. The rivers\r\nof burning liquid rock then flow sluggishly for twice\r\nthis duration before suddenly cooling and hardening.\r\nEven if an object survives the heat, it now lies trapped\r\nbeneath the rock. Anything that makes contact with\r\nlava (including the koldun) suffers a minimum of three\r\nlevels of aggravated damage. For objects that don’t\r\nhave health levels, the Storyteller must decide how\r\nmany turns they last before melting or erupting into\r\ntheir own inferno. A botch on this power opens the\r\nlava geyser under an unintended target, possibly the\r\nkoldun himself.",
                },
            ],
        },
        {
            "name": "Way of Sorrows",
            "reference": "Rites of the Blood; PG 157",
            "type": "Koldunic Sorcery",
            "powers": [
                {
                    "name": "The Frustrations of Nestrecha",
                    "description": "The koldun may destroy her enemy’s resolve, instilling\r\nfeelings of pessimism and hopelessness.",
                    "system": "For one turn per success, the target may not\r\nspend Willpower for any purpose.",
                },
                {
                    "name": "The Insults of Krivda",
                    "description": "The koldun unleashes a hateful insult towards his foe,\r\nthereby provoking her to mindless anger.",
                    "system": "In response to the insult, the target must\r\nimmediately roll Self-Control to resist frenzy against a\r\ndifficulty of 5 + the number of successes on the activation\r\nroll, maximum difficulty 9.",
                },
                {
                    "name": "The Weein of Kruchina",
                    "description": "The koldun may instill a crushing despair or nighsuicidal\r\ndepression in her enemy.",
                    "system": "For one turn per success, the target is\r\noverwhelmed by intense misery and weeps uncontrollably.\r\nShe cannot engage in any action that requires\r\nconcentration, and a Kindred loses one blood point\r\neach turn as vitae streams from her eyes.",
                },
                {
                    "name": "The Misfortune of Chernogolov",
                    "description": "The koldun taunts his enemy with a prediction of\r\ncertain doom, which then comes to pass.",
                    "system": "The target automatically loses two successes\r\non every roll she attempts. The effect lasts for a number\r\nof consecutive rolls equal to the successes rolled.",
                },
                {
                    "name": "The Starvation of Marena",
                    "description": "The koldun may now inflict direct damage on her\r\nenemy in the form of bitter cold and starving hunger.",
                    "system": "For each success, the target suffers two levels\r\nof bashing damage that can be soaked normally. In\r\naddition, a vampire targeted with this power loses one\r\nblood point per success.",
                },
            ],
        },
        {
            "name": "Way of Spirit",
            "reference": "Rites of the Blood; PG 156",
            "type": "Koldunic Sorcery",
            "powers": [
                {
                    "name": "The Way of Spirit",
                    "description": "This Path is rarely found outside of Old Clan Tzimisce,\nwhose members still stalk the same ancestral lands as\ntheir sires and their sires’ sires. But it has utility even\nfor Sabbat Tzimisce, and so its knowledge spreads even\nto more cosmopolitan Clan-mates. The path allows the\nkoldun to diffuse his perceptions across an increasingly\nlarge area. If the magic is performed correctly, the koldun\nwill be able to perceive potentially everything that takes\nplace in the affected area (which might be many square\nmiles), though opening one’s self up fully to such\nawareness is dangerous for all but the most strong-willed\nkolduns. Instead, most reflexively limit their perceptions\nto “all intruders” or “all potential feeding vessels” as they desire, and even the most perceptive koldun might miss\nsomething important if she has inadvertently excluded it\nfrom her gaze. While the power is active, the koldun may\nalso target any location or person he can perceive with\nany other Koldunic Path power or ritual, provided that\nthe rating of the Path power or ritual does not exceed\nthat of the koldun’s rating in The Way of the Spirit. This\npower also defeats the use of Obfuscate by any Kindred\nwithin the area of effect.\n• The koldun can perceive everything within a\n50-foot/20-meter radius.\n•• ... within a 100-yard/meter radius.\n••• ... within a quarter-mile/half-kilometer radius.\n•••• ... within a mile/1.5 kilometer radius.\n••••• ... within a five mile/eight kilometer radius.\n\nThe number of successes on the activation roll\r\ndetermines how many successive scenes the effect lasts.\r\nIf activated before the sun rises, the koldun’s awareness\r\ncan extend into the daylight hours, and the koldun suffers\r\nno negative effects from monitoring his lands during\r\nthe day. He does still suffer the usual dice penalties for\r\ntaking any other actions during the day.",
                    "system": "",
                },
                {
                    "name": "The Way of Spirit",
                    "description": "This Path is rarely found outside of Old Clan Tzimisce,\nwhose members still stalk the same ancestral lands as\ntheir sires and their sires’ sires. But it has utility even\nfor Sabbat Tzimisce, and so its knowledge spreads even\nto more cosmopolitan Clan-mates. The path allows the\nkoldun to diffuse his perceptions across an increasingly\nlarge area. If the magic is performed correctly, the koldun\nwill be able to perceive potentially everything that takes\nplace in the affected area (which might be many square\nmiles), though opening one’s self up fully to such\nawareness is dangerous for all but the most strong-willed\nkolduns. Instead, most reflexively limit their perceptions\nto “all intruders” or “all potential feeding vessels” as they desire, and even the most perceptive koldun might miss\nsomething important if she has inadvertently excluded it\nfrom her gaze. While the power is active, the koldun may\nalso target any location or person he can perceive with\nany other Koldunic Path power or ritual, provided that\nthe rating of the Path power or ritual does not exceed\nthat of the koldun’s rating in The Way of the Spirit. This\npower also defeats the use of Obfuscate by any Kindred\nwithin the area of effect.\n• The koldun can perceive everything within a\n50-foot/20-meter radius.\n•• ... within a 100-yard/meter radius.\n••• ... within a quarter-mile/half-kilometer radius.\n•••• ... within a mile/1.5 kilometer radius.\n••••• ... within a five mile/eight kilometer radius.\n\nThe number of successes on the activation roll\ndetermines how many successive scenes the effect lasts.\nIf activated before the sun rises, the koldun’s awareness\ncan extend into the daylight hours, and the koldun suffers\nno negative effects from monitoring his lands during\nthe day. He does still suffer the usual dice penalties for\ntaking any other actions during the day.",
                    "system": "",
                },
                {
                    "name": "The Way of Spirit",
                    "description": "This Path is rarely found outside of Old Clan Tzimisce,\nwhose members still stalk the same ancestral lands as\ntheir sires and their sires’ sires. But it has utility even\nfor Sabbat Tzimisce, and so its knowledge spreads even\nto more cosmopolitan Clan-mates. The path allows the\nkoldun to diffuse his perceptions across an increasingly\nlarge area. If the magic is performed correctly, the koldun\nwill be able to perceive potentially everything that takes\nplace in the affected area (which might be many square\nmiles), though opening one’s self up fully to such\nawareness is dangerous for all but the most strong-willed\nkolduns. Instead, most reflexively limit their perceptions\nto “all intruders” or “all potential feeding vessels” as they desire, and even the most perceptive koldun might miss\nsomething important if she has inadvertently excluded it\nfrom her gaze. While the power is active, the koldun may\nalso target any location or person he can perceive with\nany other Koldunic Path power or ritual, provided that\nthe rating of the Path power or ritual does not exceed\nthat of the koldun’s rating in The Way of the Spirit. This\npower also defeats the use of Obfuscate by any Kindred\nwithin the area of effect.\n• The koldun can perceive everything within a\n50-foot/20-meter radius.\n•• ... within a 100-yard/meter radius.\n••• ... within a quarter-mile/half-kilometer radius.\n•••• ... within a mile/1.5 kilometer radius.\n••••• ... within a five mile/eight kilometer radius.\n\nThe number of successes on the activation roll\r\ndetermines how many successive scenes the effect lasts.\r\nIf activated before the sun rises, the koldun’s awareness\r\ncan extend into the daylight hours, and the koldun suffers\r\nno negative effects from monitoring his lands during\r\nthe day. He does still suffer the usual dice penalties for\r\ntaking any other actions during the day.",
                    "system": "",
                },
                {
                    "name": "The Way of Spirit",
                    "description": "This Path is rarely found outside of Old Clan Tzimisce,\nwhose members still stalk the same ancestral lands as\ntheir sires and their sires’ sires. But it has utility even\nfor Sabbat Tzimisce, and so its knowledge spreads even\nto more cosmopolitan Clan-mates. The path allows the\nkoldun to diffuse his perceptions across an increasingly\nlarge area. If the magic is performed correctly, the koldun\nwill be able to perceive potentially everything that takes\nplace in the affected area (which might be many square\nmiles), though opening one’s self up fully to such\nawareness is dangerous for all but the most strong-willed\nkolduns. Instead, most reflexively limit their perceptions\nto “all intruders” or “all potential feeding vessels” as they desire, and even the most perceptive koldun might miss\nsomething important if she has inadvertently excluded it\nfrom her gaze. While the power is active, the koldun may\nalso target any location or person he can perceive with\nany other Koldunic Path power or ritual, provided that\nthe rating of the Path power or ritual does not exceed\nthat of the koldun’s rating in The Way of the Spirit. This\npower also defeats the use of Obfuscate by any Kindred\nwithin the area of effect.\n• The koldun can perceive everything within a\n50-foot/20-meter radius.\n•• ... within a 100-yard/meter radius.\n••• ... within a quarter-mile/half-kilometer radius.\n•••• ... within a mile/1.5 kilometer radius.\n••••• ... within a five mile/eight kilometer radius.\n\nThe number of successes on the activation roll\r\ndetermines how many successive scenes the effect lasts.\r\nIf activated before the sun rises, the koldun’s awareness\r\ncan extend into the daylight hours, and the koldun suffers\r\nno negative effects from monitoring his lands during\r\nthe day. He does still suffer the usual dice penalties for\r\ntaking any other actions during the day.",
                    "system": "",
                },
                {
                    "name": "The Way of Spirit",
                    "description": "This Path is rarely found outside of Old Clan Tzimisce,\nwhose members still stalk the same ancestral lands as\ntheir sires and their sires’ sires. But it has utility even\nfor Sabbat Tzimisce, and so its knowledge spreads even\nto more cosmopolitan Clan-mates. The path allows the\nkoldun to diffuse his perceptions across an increasingly\nlarge area. If the magic is performed correctly, the koldun\nwill be able to perceive potentially everything that takes\nplace in the affected area (which might be many square\nmiles), though opening one’s self up fully to such\nawareness is dangerous for all but the most strong-willed\nkolduns. Instead, most reflexively limit their perceptions\nto “all intruders” or “all potential feeding vessels” as they desire, and even the most perceptive koldun might miss\nsomething important if she has inadvertently excluded it\nfrom her gaze. While the power is active, the koldun may\nalso target any location or person he can perceive with\nany other Koldunic Path power or ritual, provided that\nthe rating of the Path power or ritual does not exceed\nthat of the koldun’s rating in The Way of the Spirit. This\npower also defeats the use of Obfuscate by any Kindred\nwithin the area of effect.\n• The koldun can perceive everything within a\n50-foot/20-meter radius.\n•• ... within a 100-yard/meter radius.\n••• ... within a quarter-mile/half-kilometer radius.\n•••• ... within a mile/1.5 kilometer radius.\n••••• ... within a five mile/eight kilometer radius.\n\nThe number of successes on the activation roll\r\ndetermines how many successive scenes the effect lasts.\r\nIf activated before the sun rises, the koldun’s awareness\r\ncan extend into the daylight hours, and the koldun suffers\r\nno negative effects from monitoring his lands during\r\nthe day. He does still suffer the usual dice penalties for\r\ntaking any other actions during the day.",
                    "system": "",
                },
            ],
        },
        {
            "name": "Way of Water",
            "reference": "V20 Core; PG 450",
            "type": "Koldunic Sorcery",
            "powers": [
                {
                    "name": "Pool of Lies",
                    "description": "This versatile power creates three-dimensional illusions\r\nalong the surface of a water source. How a koldun\r\nuses such illusions depends on his temperament and\r\nwill. It is just as easy to feign a divine visitation as a\r\ncunning seduction.",
                    "system": "With a successful activation roll, the koldun\r\nmay project an illusion on any water surface in line\r\nof sight. The illusion may speak and move however the\r\nvampire wishes, though it has no substance and cannot\r\nstep beyond the bounds of the water. The phantom\r\nlasts one turn per success rolled, after which it slowly\r\ndissipates into fine mist. It is possible to extend this\r\nlifespan with subsequent activations of the power, each\r\nof which stack in determining final duration. Rolls to\r\nextend an illusion’s duration add one to the base difficulty,\r\nbut require no blood. Once an illusion fades\r\naway, it must be cast anew.",
                },
                {
                    "name": "Watery Haven",
                    "description": "Just as the Gangrel meld with the earth, so may a\r\nkoldun with this power sink beneath the water to escape\r\nthe sun. The vampire does not so much submerge\r\nas merge with the water. Though his slumbering form\r\nmay be visible at odd angles from above, only the most\r\ndetermined splashing can disturb his rest.",
                    "system": "This power requires no blood. If the player gains\r\ntwo or more successes on the activation roll, the vampire\r\nsinks into the water as per the Protean power Earth Meld.\r\nA body of water must be at least two feet deep and as large\r\nin other dimensions as the vampire’s body to contain him.\r\nCatching a glimpse of a hidden koldun in the water requires\r\na successful Perception + Alertness roll (difficulty 8).",
                },
                {
                    "name": "Fog Over Sea",
                    "description": "Moving with the unnatural grace of a ghost, a koldun\r\nemploying this power may stride across water as readily\r\nas land, leaving nary a ripple to mark his passing. Some\r\nvampires delight in using this power in conjunction\r\nwith Pool of Lies to conjure phantasms to attend them.",
                    "system": "For every success on the activation roll, the\r\nkoldun may walk on water for one scene or one hour,\r\nwhichever is longer. A koldun may choose to drop\r\nthe effects of this power in order to submerge or swim;\r\nhowever, the vampire may not walk on water again unless\r\nhe reactivates the power.",
                },
                {
                    "name": "Minions of the Deep",
                    "description": "By dripping his blood into a body of water, a koldun\r\nmay summon or rouse embodied water elementals to\r\nserve him for a night. Such minions are infallibly loyal,\r\nif not especially clever. Despite their liquid form, they\r\nare solid enough to grab a man and drag him to a watery\r\ngrave or pummel him like the crashing surf.",
                    "system": "The player spends one Willpower point and\r\nmakes the standard activation roll. With success, the\r\nplayer may spend blood to summon elemental minions.\r\nThis blood must be dripped or flung into a body of water,\r\nwhich may require multiple turns depending on\r\ngenerational limits for blood expenditure.\r\nOnce the last drop of blood falls, the water rises into\r\nwhatever form the koldun desires. The caster may create\r\nas many minions as blood points spent, though not\r\nmore than the total number of successes rolled. Regardless\r\nof their form, the spirits have a rating equal to\r\nthe vampire’s Wits in all Traits. These beings have no\r\nKnowledges and no Skills apart from Stealth. Further more, their Mental and Social Attributes are considered\r\nto have a rating of 1 except in passive or defensive situations\r\n(such as to resist persuasion or mind-control).\r\nWater elementals soak and otherwise suffer damage as\r\nvampires, including from sunlight. Fire harms them less,\r\ninflicting bashing damage only. Moreover, the watery\r\ncreatures may extinguish flames with their liquid bodies,\r\nthough not without suffering injury. An elemental\r\nwho leaves the body of water that spawned it suffers\r\none level of aggravated damage per hour. Minions regenerate\r\none level of damage of any kind (including\r\naggravated) each turn they remain in contact with a\r\nlarge body of water, but do not otherwise heal. Unless\r\ndestroyed, summoned minions last until the next dawn\r\nbefore collapsing into inanimate puddles.",
                },
                {
                    "name": "Doom Tide",
                    "description": "Many ships lie at the bottom of the Black Sea, shattered\r\nby the whirlpools of the koldun. Victims of this\r\npower must fight with every ounce of their strength or\r\nfall into the whirling, airless depths below.",
                    "system": "The player spends a Willpower point in addition\r\nto the usual blood. For every success on the activation\r\nroll, the resulting whirlpool has a radius of five\r\nfeet/1.5 meters, centered anywhere in the vampire’s line\r\nof sight. Whirlpools have a base Strength of 15, increasing\r\nby 5 dots per success after the first. Victims must successfully\r\noppose this Strength with their own Strength +\r\nSurvival (difficulty 8) in order to break free. Those who\r\nfail are sucked into the depths and pounded with crushing\r\ncurrents. Living beings drown normally, while vampires\r\nand other non-breathing creatures simply remain trapped\r\nhelplessly in the vortex. This power lasts for one scene.",
                },
            ],
        },
        {
            "name": "Way of Wind",
            "reference": "V20 Core; PG 449",
            "type": "Koldunic Sorcery",
            "powers": [
                {
                    "name": "Breath of Whispers",
                    "description": "Even in their absence, koldun instill deep fear in\r\ntheir servants. This power carries the vampire’s words\r\non a light breeze and returns with the target’s reply.\r\nThe vampire need only address the target by name and\r\nforcibly mimic a deep exhalation of breath as he speaks\r\nhis message.",
                    "system": "Every time the koldun wishes to send a\r\nnew message via this power, his player makes the usual\r\nactivation roll. However, the player need only spend\r\nblood the first time the power is used during a given\r\nscene. Each success permits one turn of speech. After\r\nthe vampire concludes the message, swift winds carry\r\nit to its destination. Within a minute, the target hears\r\nthe koldun as if the vampire whispered in his ear. He\r\nmay reply or remain silent, but anything he says within\r\na number of turns equal to the koldun’s successes flies\r\nback to the koldun. This power may bring words to\r\nanyone within a mile (one and a half kilometers) who\r\nis not in a sealed room. While using this power, a koldun\r\nmust concentrate fully. Any disturbance breaks\r\nthe communication.",
                },
                {
                    "name": "Biting Gale",
                    "description": "Vengeful koldun sought to invoke a wind as chill\r\nas air atop the Carpathian Mountains. This power\r\nachieves that end, unleashing a cutting wind that can\r\nfreeze a man’s blood in his veins as it swirls through an area of his choosing. Besides its obvious combat applications,\r\nthis power also facilitates a dramatic entrance\r\nfor those so inclined.",
                    "system": "With a successful activation roll, the koldun\r\nsummons a freezing wind within a maximum of\r\na 100-yard/meter radius. Anyone caught in this frigid\r\nblast suffers one die of bashing damage each turn\r\n(which may be soaked normally), loses two dice from\r\nall Dexterity pools, and moves at half normal speed.\r\nThe winds last as long as the koldun wills, provided he\r\nmaintains concentration. Any non-reflexive actions\r\non the part of the vampire cause the winds to still and\r\ndissipate. This includes any movement.",
                },
                {
                    "name": "Breeze of Lethargy",
                    "description": "Although they cannot induce immediate sleep, the\r\nwinds evoked by this power bring growing exhaustion\r\nand numbing weariness through every muscle. Victims\r\nof this power often smell a hint of bittersweet smoke\r\nbefore they fall entranced.",
                    "system": "For two turns per success, the koldun creates\r\na wind inflicting extreme lethargy within a 200-\r\nfoot/60-meter radius. Players of characters caught in\r\nthis wind must roll Stamina + Survival (difficulty 8).\r\nThis roll is made once every ten minutes of exposure.\r\nFailure means the character halves all dice pools involving\r\nphysical actions for the remaining duration of\r\nthe wind and halves all movement rates for the scene.\r\nA botch puts the character to sleep (or a state of light\r\ntorpor for vampires) for the scene. Sleeping characters\r\nawaken if prodded, shaken, or otherwise manhandled,\r\nthough they move slowly and may suffer halved dice\r\npools if the wind persists.",
                },
                {
                    "name": "Ride the Tempst",
                    "description": "A koldun employing this power moves at incredible\r\nspeeds as he rides along the winds. While traveling\r\nwith this power, a vampire assumes a blurred form that\r\ncoalesces as he reaches his destination.",
                    "system": "With a successful activation roll, the koldun\r\nfades into the wind and flies at 250 mph/400 kph to his\r\ndestination. This power cannot effectively function in\r\ncaves, buildings, or other enclosed areas. Outside, the\r\nvampire’s flight navigates all obstacles. Once the koldun\r\narrives at his destination or the scene ends, the\r\nvampire descends to earth and solidifies.",
                },
                {
                    "name": "Tempst",
                    "description": "Applying fury magnified by blood and will, a koldun\r\nmay project the full measure of his anger into the night\r\nsky. Churning gray clouds blot out stars and moon,\r\nunleashing spiraling gusts and a driving downpour of\r\nfreezing rain. Lightning arcs overhead, with each thunderous\r\nflash casting jagged shadows.",
                    "system": "With a successful activation roll and a point\r\nof Willpower (in addition to the usual blood), a koldun\r\nmay conjure a terrible storm. It takes six hours for the\r\nclouds to gather and thicken overhead, minus one hour\r\nfor every success rolled. If this results in a duration of\r\nless than one hour, the clouds blossom outward from\r\ndirectly overhead like a black canopy, filling the sky in\r\nmere minutes. Once the clouds form, the rain begins\r\nto fall in torrents and the lightning begins. The storm\r\npersists at full strength for one hour per success rolled. It\r\ngradually dissipates over the hour following that. During\r\nthe peak of its fury, the storm may cause flooding and\r\ncertainly chills any exposed mortal to the bone (1 die\r\nof unsoakable bashing damage every five minutes of full\r\nexposure). Lightning strikes regularly, far more than a\r\nusual storm. Indeed, for a cost of one Willpower point,\r\na koldun may direct lightning at a foe using his Perception\r\n+ Occult (difficulty 6). A successful strike inflicts\r\n10 dice of lethal damage (which can be soaked normally).\r\nOnly one such attack may be made each turn.",
                },
            ],
        },
        {
            "name": "Ash Path",
            "reference": "V20 Core; PG 163",
            "type": "Necromancy",
            "powers": [
                {
                    "name": "Shroudsight",
                    "description": "Shroudsight allows a necromancer to see through the\r\nShroud, the mystical barrier that separates the living\r\nworld from the Underworld. By using this power, the\r\nvampire can spot ghostly buildings and items, the landscape\r\nof the so-called Shadowlands, and even wraiths\r\nthemselves. However, an observant wraith may notice\r\nwhen a vampire suddenly starts staring at him, which\r\ncan lead to unpleasant consequences.",
                    "system": "A simple roll of Perception + Awareness\r\n(difficulty 7) allows a necromancer to utilize Shroudsight.\r\nThe effects last for a scene.",
                },
                {
                    "name": "Lifeless Tongues",
                    "description": "Where Shroudsight allows a necromancer to see\r\nghosts, Lifeless Tongues allows her to converse with\r\nthem effortlessly. Once Lifeless Tongues is employed,\r\nthe vampire can carry on a conversation with the denizens\r\nof the ghostly Underworld without spending blood\r\nor causing the wraiths to expend any effort.",
                    "system": "To use Lifeless Tongues requires a roll of\r\nPerception + Occult (difficulty 6) and the expenditure\r\nof a Willpower point.",
                },
                {
                    "name": "Dead Hand",
                    "description": "Similar to the Sepulchre Path power Torment, Dead\r\nHand allows a necromancer to reach across the Shroud\r\nand affect a ghostly object as if it were in the real world.\r\nGhosts are solid to necromancers using this power,\r\nand can be attacked. Furthermore, the necromancer\r\ncan pick up ghostly items, scale ghostly architecture\r\n(giving real-world bystanders the impression that he’s\r\nclimbing on air!), and generally exist in two worlds.\r\nOn the other hand, a necromancer using Dead Hand is\r\nquite solid to the residents of the Underworld — and\r\nto whatever hostilities they might have.",
                    "system": "The player spends a point of Willpower and\r\nmakes a successful Wits + Occult roll (difficulty 7) to\r\nactivate Dead Hand for one scene. For each additional\r\nscene the vampire wishes to remain in contact with\r\nthe Underworld, he must spend a point of blood.",
                },
                {
                    "name": "Ex Nihilo",
                    "description": "Ex Nihilo allows a necromancer to enter the Underworld\r\nphysically. While in the lands of the dead,\r\nthe vampire is essentially a particularly solid ghost. He\r\nmaintains his normal number of health levels, but can\r\nbe hurt only by things that inflict aggravated damage\r\non ghosts (weapons forged from souls, certain ghostly\r\npowers, etc.). A vampire physically in the Underworld\r\ncan pass through solid objects in the real world (at the\r\ncost of one health level) and remain “incorporeal” for\r\na number of turns equal to her Stamina rating. On the\r\nother hand, vampires present in the Underworld are\r\nsubject to all of the Underworld’s perils, including ultimate\r\ndestruction. A vampire killed in the realm of the\r\ndead is gone forever, beyond even the reach of other\r\nnecromancers.",
                    "system": "Using Ex Nihilo takes a tremendous toll on\r\nthe necromancer. To activate this power, the vampire\r\nmust first draw a doorway with chalk or blood on any\r\navailable surface. (The vampire may draw doors ahead\r\nof time for exactly this purpose.) The player must then\r\nexpend two points of Willpower and two points of\r\nblood before making a Stamina + Occult roll (difficulty\r\n8) as the vampire attempts to open the chalk door\r\nphysically. If the roll succeeds, the door opens and the\r\nvampire steps through into the Underworld.\r\nWhen the vampire wishes to return to the real world,\r\nhe merely needs to concentrate (and the player spends\r\nanother Willpower point and rolls Stamina + Occult,\r\ndifficulty 6). At Storyteller discretion, a vampire who\r\nis too deeply immersed in the Underworld may need\r\nto journey to a place close to the lands of the living in\r\norder to cross over. Vampires who wander too far into\r\nthe lands of the dead may be trapped there forever.\r\nVampires in the Underworld cannot feed upon\r\nghosts without the use of another power; their only\r\nsustenance is the blood they bring with them.",
                },
                {
                    "name": "Shroud Mastery",
                    "description": "Shroud Mastery offers the Kindred the ability to\r\nmanipulate the veil between the worlds of the living\r\nand the dead. By doing so, a necromancer can make\r\nit easier for bound wraiths in his service to function,\r\nor make it nearly impossible for ghosts to contact the\r\nmaterial world.",
                    "system": "To exercise Shroud Mastery, the necromancer\r\nexpends two points of Willpower, then states\r\nwhether he is attempting to raise or lower the Shroud.\r\nThe player then makes a Willpower roll (difficulty 9).\r\nEach success on the roll raises or lowers the difficulties\r\nof all nearby wraiths’ attempts to cross the Shroud in\r\nany way by one, to a maximum of 10 or a minimum of\r\n3. The Shroud reverts to its normal strength at a rate of\r\none point per hour thereafter.",
                },
            ],
        },
        {
            "name": "Bone Path",
            "reference": "V20 Core; PG 164",
            "type": "Necromancy",
            "powers": [
                {
                    "name": "Tremens",
                    "description": "Tremens allows a necromancer to make the flesh of a \ncorpse shift once. An arm might suddenly flop forward, \na cadaver might sit up, or dead eyes might abruptly \nopen. This sort of thing tends to have an impressive \nimpact on people who aren’t expecting a departed rela\ntive to roll over in his coffin.",
                    "system": "To use Tremens, the necromancer spends \na single blood point, and the player must succeed on \na Dexterity + Occult roll (difficulty 6). The more suc\ncesses that are achieved, the more complicated an ac\ntion can be effected in the corpse. One success allows \nfor an instantaneous movement, such as a twitch, while \nfive allow the vampire to set up specific conditions un\nder which the body animates (“The next time someone \nenters the room, I want the corpse to sit up and open \nits eyes.”). Under no circumstances can Tremens cause \na dead body to attack or cause damage.",
                },
                {
                    "name": "Apprentice's Brooms",
                    "description": "With Apprentice’s Brooms, the necromancer can \nmake a dead body rise and perform a simple function. \nFor example, the corpse could be set to carrying heavy \nobjects, digging, or just shambling from place to place. \nThe cadavers thus animated do not attack or defend \nthemselves if interfered with, but instead attempt to \ncarry out their given instructions until such time as \nthey’ve been rendered inanimate. Generally it takes dismemberment, flame, or something similar to destroy \na corpse animated in this way.",
                    "system": "A roll of Wits + Occult (difficulty 7) and \nthe expenditure of a point of both blood and Will\npower are all that is necessary to animate corpses with \nApprentice’s Brooms. The number of corpses animated \nis equal to the number of successes achieved. The nec\nromancer must then state the task to which he is set\nting his zombies. The cadavers turn themselves to their \nwork until they finish the job (at which point they col\nlapse) or something (including time) destroys them.\n Corpses animated in this way have no initiative of \ntheir own, and are unable to make value judgments. \nThey respond to very literal instruction. Thus, a zom\nbie could be told “sweep this room every day until all \nthe dust and cobwebs are gone” or “transcribe this \nmanuscript” with an expectation of reasonable results, \nwhile a more open-ended command such as “fix this \nmotorcycle” or “research this Necromantic ritual and \nwrite down the results” would be doomed to failure. \nBodies energized by this power continue to decay, al\nbeit at a much slower rate than normal.",
                },
                {
                    "name": "Shambling Hordes",
                    "description": "Shambling Hordes creates obvious results: reanimat\ned corpses with the ability to attack, albeit neither very \nwell nor very quickly. Once primed by this power, the \ncorpses wait — for years, if necessary — to fulfill the \ncommand given them. The orders might be to protect \na certain site or simply to attack immediately, but they \nwill be carried out until every last one of the decom\nposing monsters is destroyed.",
                    "system": "The player spends a point of Willpower. \nThe player then must succeed on a Wits + Occult roll \n(difficulty 8). Each success allows the vampire to raise \nanother corpse from the grave, and costs one blood \npoint. If the player cannot or chooses not to pay the \nblood point cost of additional zombies past a certain \nnumber, the extra successes are simply lost. Each zom\nbie can follow one simple instruction, such as “Stay \nhere and guard this graveyard against any intruders,” \nor “Kill them!” \nNote: Zombies created by Shambling Hordes will \nwait forever if need be to fulfill their functions. Long \nafter the flesh has rotted off their mystically animated \nbones, the zombies will wait and wait and wait, still \nable to perform their duties.",
                },
                {
                    "name": "Soul Stealing",
                    "description": "This power affects the living, not the dead. It does, \nhowever, temporarily turn a living soul into a sort of \nwraith, as it allows a necromancer to strip a soul from \na living body. A mortal exiled from his body by this \npower becomes a wraith with a single tie to the real \nworld: his now-empty body.",
                    "system": "The player spends a point of Willpower \nand then makes a contested Willpower roll against \nthe intended victim (difficulty 6). Successes indicate \nthe number of hours during which the original soul is \nforced out of its housing. The body itself remains auto\nnomically alive but catatonic.\n This power can be used to create suitable hosts for \nDaemonic Possession. It has no effect on Kindred or \nother supernatural creatures (except ghouls) until such \ncreatures are dead – in the case of vampires, this means \nFinal Death.",
                },
                {
                    "name": "Daemonic Possession",
                    "description": "Daemonic Possession lets a vampire insert a soul into \na freshly dead body. This does not turn the reanimated \ncorpse into anything other than a reanimated corpse, \none that will irrevocably decay after a week, but it does give either a wraith or a free-floating soul (say, that of \na vampire using Psychic Projection) a temporary home \nin the physical world.",
                    "system": "The body in question must be no more than \n30 minutes dead, and the new tenant must agree to in\nhabit it — a ghost or astral form cannot be forced into a \nnew shell. However, most ghosts would gladly seize the \nopportunity. Should the vampire, for whatever reason, \nwish to insert a soul into another vampire’s corpse (be\nfore it crumbles to ash), the necromancer must achieve \nfive successes on a resisted Willpower roll against the \noriginal owner of the body. Otherwise, the interloper \nis denied entrance.\n Note: The soul can use whatever physical abilities \n(Athletics, Brawl, Potence) his new fleshy home pos\nsesses, and whatever mental abilities (Computer, Law, \nPresence) he already possessed. He cannot use the \nphysical abilities of his old form, or the mental abilities \nof his new one.",
                },
            ],
        },
        {
            "name": "Cenotaph Path",
            "reference": "V20 Core; PG 166",
            "type": "Necromancy",
            "powers": [
                {
                    "name": "A Touch of Death",
                    "description": "Just as a necromancer may exert mastery over the \nShadowlands, so too can some ghosts exert them\nselves in the mortal world. Whereas obvious displays \nof ghostly power such as bleeding walls or disembodied \nmoans certainly won’t be mistaken, some ghostly abili\nties exert subtle effects that aren’t easily recognized. \nA necromancer sensitized to the residue of the dead, \nthough, can feel whether an object has been touched \nby a ghost or sense the recent passage of a wraith.",
                    "system": "The necromancer simply touches a person or \nobject that he suspects is a victim of ghostly influence. \nThe player rolls Perception + Awareness (difficulty 6). \nIf successful, the necromancer can determine whether a ghost has exerted any sort of power on the subject, or \neven crossed nearby, to the duration detailed below.\n\n  Successes   Result\n 1 success    Last turn; detect use of ghostly powers\n2 successes   Last three turns; detect use of ghostly \n          powers\n3 successes   Last hour; detect ghost’s touch and \n         use of ghostly powers\n4 successes   Last day; detect ghost’s touch and use \n          of ghostly powers\n5 successes   Last week; detect nearby passage of \n          ghost, ghost’s touch, and use of  \n          ghostly powers\n\n On a failure, the necromancer receives no impres\nsions. A botch reveals a misleading answer (an object \nmay seem tinged with ghostly power when it’s not, or \nvice versa). Should the necromancer succeed in detec\ntion while touching an object or person that a ghost \nis possessing, he immediately becomes aware that the \nghost is still inside. The impression gained in such a \ncase is sufficient to count as an image of the spirit for \npurposes of the Sepulchre Path’s powers, so the Kin\ndred may be able to (for example) immediately com\nmand a ghost to exit a person whom it possesses.",
                },
                {
                    "name": "Reveal the Catene",
                    "description": "Necromantic compulsions function much more ef\nfectively when the caster uses an object of significance \nto the ghost in question. Such fetters tie the dead to \nthe living lands through their remembered importance \n— a favored recliner for relaxing, a reviled piece of art \nfoisted off by hated relatives, or some object of similarly \nintense emotion. Many necromancers can detect such \ncatene through the use of rituals (see Ritual of the Un\nearthed Fetter, p. 181). With this power, though, the \nnecromancer can determine a fetter with just a few mo\nments of handling. The Kindred simply runs his hands \nover the object and concentrates on it. He quickly \nreceives an impression of the item’s (or person’s) im\nportance to wraiths, if any; should the wraith be one \nknown to the necromancer, he immediately recognizes \nthe object as a fetter to that (or those) ghost(s). Suc\ncessful identification of a connected ghost is not exclu\nsive; that is, if the vampire determines that the object \nis important to a given wraith, he can also determine if \nthere are other ghosts tied to the item, though he must \nuse the power again to gain their identities.\n Many necromancers use this power on objects al\nready identified with A Touch of Death, in order to \ndetermine whether the ghost is trying to attune a given \nfetter or simply toying with the world of the living.",
                    "system": "The necromancer holds and examines the object for at least three turns — if it’s an item, this means turning it over in his hands, running his fingers along it, or otherwise giving it a critical eye; with a person, this may require a more… invasive… examination. The player then spends a blood point and rolls Perception + Occult (difficulty 7). If successful, \nthe Kindred determines whether the object holds any significance to any ghost and, with three or more successes, the identity of at least one such ghost (which allows the Kindred to use the Sepulchre Path on that wraith, if desired). If the necromancer already knows any of the ghosts involved, their ties are revealed with their identity — so, if the necromancer already knows a wraith well enough to summon and compel it with other powers, successful identification of a fetter tells whether the object is tied to that ghost, in addition to any other impressions gained.\n If a botch is scored, the necromancer can never successfully use this power on the item being examined.",
                },
                {
                    "name": "Tread upon the Grave",
                    "description": "The extended awareness granted with the Cenotaph \nPath allows the necromancer to find locations where \nthe Shadowlands and the living world come close. \nOften, the necromancer experiences a chill or shiver \nwhen stepping into an area where the Underworld lies \nnear the living one. With practice, the vampire can \ntell exactly where such locations are.\n Experienced necromancers learn that certain loca\ntions are susceptible to ghostly influence; these haunt\ned areas often become homes of a sort for ghosts. A \nknowledgeable vampire can thus discover places where \nthe dead are likely to congregate, the better to snare \nthem with other Necromancy powers.",
                    "system": "The player simply declares intent to sense \nthe Shroud in an area and makes a Willpower roll \n(difficulty 8). Success reveals whether the location is \nhighly attuned to the Shadowlands, about average (not \nparticularly close to the world of the dead), or far re\nmoved from the realm of death. A failing attempt at \nusing the power has no adverse effect, though it may \nbe attempted only once per scene (so the necromancer \nmust either wait for a time or move to a different area \nbefore attempting Tread Upon the Grave once more).\n A botch stuns the necromancer into inaction for a full \nturn and costs him a temporary Willpower point, as he \nis overcome by shivers and a sense of overwhelming \ndespair.\n With three or more successes, the necromancer can \ndetermine whether the Shroud’s strength has been ar\ntificially altered in the area.",
                },
                {
                    "name": "Death Knell",
                    "description": "Not all who die go on to become ghosts — many \nlack the drive to hang on after death or simply have no \noverwhelming needs that compel them to stick around. \nNormally, even necromancers have no way to sort \nthose who might become ghosts from the masses who \ngo on to whatever rewards await. Over time, though, a \nnecromancer can become sensitized to the pull that oc\ncurs when a soul escapes from a body only to hover in \nwait, enslaved by its desires. The weight of desperation \nbecomes like a tangible tug, and some necromancers \nsavor this emotion even as they follow the sensation to \nfind the new ghost.\n Of course, actually discovering the new ghost can be \nproblematic. The Kindred may need some means to see \nthrough the Shroud or may have to send other wraiths \nto look for the new unfortunate, especially if a large \naccident or massacre leaves too many corpses for the \nnecromancer to easily discern and test names.",
                    "system": "Whenever someone dies and becomes a \nghost within a half-mile or kilometer of the necroman\ncer, she automatically senses the demise (though many \nchoose to ignore this “always-on” power unless actively \nseeking someone). This power does not automatically \npinpoint the location of the new ghost or identify it, \nbut the player may spend one Willpower point and roll \nPerception + Occult (difficulty 7) for the necromancer \nto gain a vague sense of the distance and direction to \nthe new wraith. With one success, the Kindred may \nsense a vague pull in a general direction; with three \nsuccesses, the necromancer can sense the direction and \nguess distance to within a quarter-mile or half a kilo\nmeter. With five successes, the necromancer immedi\nately senses the location of the new ghost to within \none foot or 30 cm. A failure carries no penalty but a \nbotched attempt sends the necromancer scurrying off \nin the wrong direction.\n The Storyteller may rule that disturbances in the \nUnderworld, intervening magic, or other similar phe\nnomena cloud this sensation, simply to prevent over\nburdening a chronicle with constant ghost-hunting \nand dice rolling.",
                },
                {
                    "name": "Ephemeral Binding",
                    "description": "The most puissant necromancers learn not only to \nsense the ties between living and dead, but to forge \nsuch ties themselves. The master of Ephemeral Bind\ning turns an otherwise mundane object or person into a \ndepository for his own necromantic energy. The undy\ning Curse transforms the subject into a sort of linkage \nbetween the living and dead. The necromancer smears \nhis blood on the item in question, which mystically ab\nsorbs the vitae and, in doing so, becomes a vessel to \nanchor a spirit.",
                    "system": "The necromancer must coat an object with \nhis blood (a full blood point’s worth); if the subject is \na person, then that individual must ingest the vitae. \nThe player marks off the blood point, spends a point \nof Willpower, and rolls Manipulation + Occult (difficulty 8). If successful, the item temporarily becomes \na fetter to one wraith. If the Kindred already knows \nthe name of the wraith or has a strong psychic impres\nsion, then the object can become a fetter at any range, \neven to a ghost who normally does not come near the \nliving world (so long as the ghost still exists). Other\nwise, the necromancer must be able to see or sense the \nghost (with Witness of Death, Shroudsight, or other \nsuch means).\n A fetter artificially created in this fashion functions \nfor all necromantic and ghostly purposes as a normal \nfetter: It can be detected with other Necromancy pow\ners, the vampire gains a bonus to Necromancy against \nthe wraith attuned to it, and the ghost similarly finds \nexertion of its powers easier upon the subject (so the \nvampire might turn an unwitting ghoul into a consort \nfor a wraith familiar with possession…). The ghost can \nsink into the fetter to heal; conversely, if the fetter is \ndestroyed, the wraith is banished to some inaccessible \nregion of the Underworld, perhaps never to return.\n A fetter created with Ephemeral Binding lasts for \none night per success scored. The expenditure of an ad\nditional point of Willpower increases this duration to \na week per success, whereas spending a permanent dot \nof Willpower extends the duration to a year and a day.\n Botching with this power not only causes failure but \nalso makes the ghost immediately aware of what the \nnecromancer was trying to do. Most ghosts do not take \nkindly to meddling Kindred trying to make artificial \nchains for them.",
                },
            ],
        },
        {
            "name": "Corpse in the Monster",
            "reference": "V20 Core; PG 168-169",
            "type": "Necromancy",
            "powers": [
                {
                    "name": "Masque of Death",
                    "description": "The character with this ability can assume a visage \nof death or inflict that shape on another vampire. The \nvictim’s flesh becomes pallid and thin (if it is not al\nready), and skin pulls tight against bone. This ability \ncan be very useful, as it allows one to hide in plain sight \nin a tomb or crypt at any time (though the character \nremains as vulnerable to sunlight and fire as ever). \nWhen a necromancer uses this power on another Kin\ndred, the victim gains the same corpselike demeanor. \nIn this sense, the ability works as something of a minor \ncurse.",
                    "system": "The player spends one blood point for the \ncharacter to gain the form described. Those afflicted \nwith the Masque of Death lose two points of Dexter\nity and Appearance (minimum of 1 in Dexterity and \n0 in Appearance) for the duration of the power. The \nplayer also gets two extra dice to his Intimidation dice \npool, should he wish to terrify any onlookers. Further, \nif the character remains perfectly still, observers must \nroll five successes on a Perception + Medicine roll (difficulty 7) to distinguish the character from a normal \ncorpse. The player doesn’t need to roll anything to \nhave the character stop moving — vampires have no \nautonomic functions. \nIf the user inflicts Masque of Death on another vam\npire, he must spend a blood point, touch the target, and \nthen make a Stamina + Medicine roll (difficulty equal \nto the target’s Stamina + 3). The Masque of Death lasts \nuntil the next sunset, unless the character who created \nthe masque wishes to extinguish its effects earlier.",
                },
                {
                    "name": "Cold of the Grave",
                    "description": "The dead feel no pain, though most undead do. With \nthis ability, the character can temporarily take on the \nunfeeling semblance of the dead, in order to protect \nherself from physical and emotional harm. When as\nsuming the Cold of the Grave, the vampire’s skin be\ncomes unusually cold. When she speaks, her breath \nmists even in warm air — those with exceptional sens\nes might even see a slight red tinge to the breath.\n The power brings a sense of lethargy over the char\nacter, as a mortal might feel under the influence of a \nmildly unpleasant disease. It becomes difficult to rouse \noneself to action, and very little seems important \nenough to really worry about. A corpse has no worries, \nafter all.",
                    "system": "The player spends one Willpower point. \nFor the remainder of the scene, the character takes no \nwound penalties, and the player gains an additional die \nto all dice pools that involve resisting emotional ma\nnipulation, such as Intimidation or Empathy. However, \nthe player also loses a die from dice pools to emotion\nally manipulate others. The character is a cold fish to \nthose she interacts with, and they do not respond read\nily to her. The Cold of the Grave does not protect the \ncharacter against the depredations of the Beast. She \nmay be emotionally cold on the surface, but if others \ntaunt and anger her sufficiently, she is still subject to \nfrenzy as normal.",
                },
                {
                    "name": "Curse of Life",
                    "description": "The Curse of Life inflicts some of the undesirable \ntraits of the living upon the undead, removing their corpselike nature and creating a false life to remind \nthem of the worst things about being alive. Targets of \nthis power regain only the unpleasant aspects of life, as \nculled from the memory of the Discipline’s user. This \nmay include mundane hunger and thirst, sweat and \nother excretions, the need to urinate and defecate, a \ndecrease in sensory acuity, and a particular vulnerabil\nity to attacks that the character might normally shrug \noff.",
                    "system": "The player spends one Willpower and rolls \nIntelligence + Medicine (difficulty 8) to affect a target \nwithin line of sight and no farther than 20 yards or me\nters from the character. If the roll succeeds, the target \nsuffers the weaknesses of the living without gaining any \nbenefit from that state. He does not become immune \nto sunlight or holy artifacts, for instance. However, he \ndoes become badly distracted by mundane needs, with \nthe net result that his player suffers a +2 difficulty pen\nalty to all rolls. He can ignore these distractions at the \ncost of one Willpower point per scene. Additionally, \nthe victim cannot use blood to raise his Physical At\ntributes while this power is in effect, and Willpower \ncannot eliminate this penalty. The power remains in \neffect until the next sunset.",
                },
                {
                    "name": "Gift of the Corpse",
                    "description": "This power, one of the most potent on the Corpse \nin the Monster path, enables a necromancer to ignore \nmost of her race’s inherent weaknesses for a short time. \nA dead body is not particularly vulnerable to sunlight, \nholy artifacts, frenzy, or being staked through the heart, \nafter all, and so it is with a vampire using the Gift of \nthe Corpse. As with the Cold of the Grave, above, \nthe character using this power takes on an even more \ndeathlike mien. It lasts for less than a minute, typical\nly, but that time may be enough to enable a character \nto charge through a burning building without fearing \nfrenzy or instant death.",
                    "system": "The player spends one Willpower and rolls \nStamina + Occult (difficulty 8). For every success, the \ncharacter can spend one turn in a state in which he is \nmore akin to an animated corpse than a vampire. Holy \nartifacts and sanctified ground have no effect, and the \ncharacter is immune to frenzy and Rötschreck. Sun\nlight does only bashing damage, and then only if bare \nskin is exposed on a clear day. Being staked through \nthe heart is only as much of a danger as getting stabbed \nthrough his dead spleen would be. Fire harms him only \nas it would a mortal — causing lethal damage instead \nof aggravated. \nShould the character end the power’s duration while \nexposed to any of the aforementioned harmful things, \nhe immediately takes their full effect. If he is staked, he \nbecome immobilized; if he is on or near fire, he begins \nto take the damage a Cainite should take, and he must \nimmediately roll against Rötschreck.",
                },
                {
                    "name": "Gift of Life",
                    "description": "With the Gift of Life, the character can experience \nthe best and most positive things about being alive. The \noverwhelming hunger for blood temporarily abates, al\nlowing the character to consume and enjoy food and \ndrink. She can also enjoy sex as she wishes, and the sun \ndoes not burn her. The Gift of Life comes with a dark, \nterrible cost, however. Its use is almost sure to result in \nthe death of a mortal, as the vampire must expend an \nenormous quantity of vitae in order to initiate it. The \nDiscipline’s effects last until the midnight after the \ncharacter uses the power, so it is in her best interests to \nuse it just after midnight.",
                    "system": "The player spends 12 blood points, burning \nas much blood as possible each turn until she meets \nthat level. She then rolls Stamina + Occult (difficulty \n6) and needs only one success for the power to work. \nA botch has catastrophic effects. The character might \nbe instantly killed or might inadvertently Embrace her \nvictim, for example. If it takes longer than one turn \nto spend the necessary blood to enact this ability, it \ndoes not take effect until all 12 points have been spent. \nHowever, the blood must be spent continuously — the \nvampire cannot burn five, run off and feed, then burn \nseven more an hour later. On the other hand, she may \nfeed as she activates the power — in one turn she might \nburn one blood point while drinking three. Since few \nKindred above the Seventh Generation can easily ex\npend such an amount of blood, the most efficient way \nto activate this power is to have a human nearby who \ncan be sacrificed to power the transformation.\n After her transformation, the character gains many \ntraits of an ordinary human. She is largely immune to \nthe scorching effects of the sun (Fortitude difficulties \nto soak damage from direct sunlight are halved, and \nshe takes no damage if she is sufficiently covered), and \nshe can experience and enjoy many of the fine things \nabout human life. She retains a few of her vampiric \nbenefits, however. Fortitude and Auspex abilities re\nmain in place if she has either of those Disciplines, and \nthe Storyteller may allow her to retain other Disciplines \nas well if he deems them dramatically appropriate. She \nalso retains a vampire’s benefits when it comes to han\ndling bashing damage. However, she is still vulnerable \nto holy artifacts, human faith, and being staked. Her \nblood remains vitae, not human blood. Use of this abil\nity — which creates a mockery of human life — may \ninterfere with a character’s Path advancement, at the \nStoryteller’s discretion.\n The vampire is no more vulnerable to fire than any \nother mortal while in this half-alive state, but she still \nsuffers somewhat from the Beast. Frenzy and Rötschreck \ndifficulties are halved (round up). She can remain ac\ntive during the day without Humanity or Path-based \ndice pool caps, although she is certainly tired during \nthe day, since that is not her usual time of activity.\n Her Beast exacts a dangerous retribution when her \nday of “life” is done. Although its influence is greatly \nsuppressed during this power’s duration, the Beast has \nits way with the vampire for the next six nights, as all \ndifficulties to resist frenzy increase by three. The wise \nnecromancer hides herself away somewhere during \nthat period, but, depending on morality and tempera\nment, enforced isolation might drive her to frenzy on \nits own.",
                },
            ],
        },
        {
            "name": "Grave's Decay",
            "reference": "V20 Core; PG 171",
            "type": "Necromancy",
            "powers": [
                {
                    "name": "Destroy the Husk",
                    "description": "Cainites who kill their victims, rather than just feed\ning upon them, frequently find themselves in need of a \nquick way to dispose of a corpse. While there are many \nways to make sure that a corpse is not found — feed it \nto a pack of hounds or weigh it down and throw it in a \nriver — many of these methods do involve risk to the \nvampire and are not guaranteed to succeed. Destroy \nthe Husk, by contrast, is foolproof. Use of this power \nsimply turns one human corpse to a pile of about 30 \npounds (13 kilograms) of unremarkable dust, roughly \nthe size and shape of that body.",
                    "system": "The player spends one blood point as the \nvampire drips her vitae onto the corpse. The player \nthen rolls Intelligence + Medicine (difficulty 6). One \nsuccess is all that is needed to render the corpse into \ndust, although the process takes a number of turns \nequal to five minus the successes.",
                },
                {
                    "name": "Rigor Mortis",
                    "description": "One of the first changes that comes over a dead body \nis rigidity; the corpse becomes stiff as a board, frozen \nin a single pose. The Cainite who wields Rigor Mortis \nis able to push a living or undead body to that frozen \npoint using only his will and understanding of the forc\nes of decay. She forces her target to become rigid and \nunable to move without enormous effort of will, as his \nvery muscles betray him.",
                    "system": "The player spends a point of Willpower and \nrolls Intelligence + Medicine (difficulty 7). Each suc\ncess freezes the target in place for one turn. A failure \nsimply indicates the loss of the Willpower point, while \na botch renders the target immune to powers in the \nGrave’s Decay path for the next 24 hours. The target \nmust be visible and within about 25 yards or meters for \nthis ability to take effect. A frozen target is treated as \nthough he has been staked (see p. 280). With a Will\npower roll (difficulty 7) and two successes, the target \ncan break out of the rigor on her turn. Failure causes \nher a level of bashing damage and means another turn \nwasted and frozen.",
                },
                {
                    "name": "Wither",
                    "description": "Reminiscent of some of the powers of Vicissitude, \nWither allows a vampire to cripple an opponent’s limb. \nWhether the foe is living or undead, muscle shrivels \naway, skin peels, and bone becomes brittle. The tar\nget is unable to exert any noteworthy strength in the \ncrippled limb. This injury lasts for far longer than most \ninjuries trouble vampires, and in mortals it simply does \nnot heal.\nWither doesn’t have to be used on a limb, although \nthat is its usual purpose. It can also be used simply to \naffect the target’s face and hair, making him appear far \nolder than his years. It could also be applied to a tar\nget’s eye or ear, killing the sense in that organ (and \nthus requiring two uses to permanently blind or deaf\nen). Wither cannot be used as an “instant-kill” power \n— necromancers cannot wither internal organs — but \nit can inflict a wide variety of injuries on a foe.",
                    "system": "The player spends a Willpower point. The \ncharacter chooses a limb on the target and then touch\nes that limb. If the target is trying to avoid contact, the \ninvoker’s player rolls Dexterity + Brawl to hit as nor\nmal. If the character succeeds in touching the intended \nlimb, the target suffers two aggravated wounds. Unless \nthe target soaks both wounds (such as with Fortitude), \nthe struck limb is crippled and unusable until both of \nthose wounds have healed. Kindred heal the wounds as they would any other aggravated wound (see p. 285). \nMortals are incapable of healing aggravated wounds, so \nthey suffer throughout their lives unless they are healed \nthrough supernatural means. A withered limb does not \ndegenerate further, even on a mortal. The character \nmay be crippled for life, but the limb won’t become \ninfected or gangrenous.\n The effects of the withering depend on the affected \nlimb. A crippled arm has a Strength of 0, cannot ben\nefit from Potence, and cannot carry anything heavier \nthan about half a pound (200 grams). A crippled leg \nprevents the character from moving faster than a stut\ntering hop or dragging limp. The character suffers the \neffects of the Lame Flaw (see p. 482). A single withered \neye or ear imposes a +1 difficulty to relevant Perception \nrolls. Losing both eyes or both ears imposes the effects \nof the Blind or Deaf Flaws (see pp. 484 and 483). A \nwithered tongue imposes the effects of the Mute Flaw \n(p. 483), while a withered face reduces the target’s Appearance by one for each aggravated wound suffered.",
                },
                {
                    "name": "Corrupt the Undead Flesh",
                    "description": "Corrupt the Undead Flesh blurs the line between life \nand undeath, turning an undead creature into some\nthing just living enough to carry and suffer from dis\nease. The disease inflicts the target, causing lethargy, \ndizziness, loss of strength, clumsiness, and the inabil\nity to keep blood in his system. This pernicious influ\nence is extremely virulent among mortals. They pick \nthe disease up simply by spending a few hours near the \nvictim. Other vampires have a harder time acquiring \nthe disease. They must consume the victim’s blood to \ndo so, but afterward, they suffer just as much as the \noriginal target — including passing the affliction on \nto others.\n The disease fades after roughly a week.",
                    "system": "The player chooses a target within her \ncharacter’s line of sight and no more than 20 yards or \nmeters away. She rolls Intelligence + Medicine (diffi\nculty 6) and spends a point of Willpower. The victim’s \nplayer must roll Stamina (+ Fortitude, if appropriate) \nagainst a difficulty equal to the attacker’s Willpower. If \nthe player scores more successes than the victim, he ac\nquires a virulent disease immediately. The disease has \nthe following effects: \n• The victim’s Strength and Wits are halved (round \ndown).\n • The victim loses one point of Dexterity.\n • The victim’s player must spend one additional \nblood point every evening for the vampire to rouse \nhimself to consciousness. Mortals lose one health level \nper day instead.\n • The victim’s player must roll Self-Control or In\nstinct each time the character feeds (difficulty 8). On \na failure, the vampire cannot keep the blood he just \ningested inside his body, and he vomits it up in great \nhorrifying gouts of gore, losing any benefit the blood \nmight have provided. Humans vomit up food.\n Every evening at sunset, the victim has a chance to \nthrow off the plague. The victim’s player rolls Stamina, \nwith a difficulty equal to 10 minus the number of sun\nsets since acquiring the plague. On a successful roll, the \ncharacter fights the disease to a standstill and begins \nto recover. He instantly regains his ability to manage \nblood, and he heals back one lost Attribute point per \nhour until all have returned.",
                },
                {
                    "name": "Dissolve the Flesh",
                    "description": "This ability brings the Grave’s Decay path full circle, \nas it causes Destroy the Husk to apply to vampires. Dis\nsolve the Flesh allows a necromancer to attempt to \nturn vampiric flesh to dust or ash, as though the target \nhad been burned or left out in the sun.",
                    "system": "The player spends two blood points and a \nWillpower point as the vampire extracts a quantity of \nher vitae charged with the power of the grave. If she \ndrips it onto a single Kindred victim anytime within \nthe next few turns (most of the blood must reach the \nvictim, so flinging a few drops is ineffective), it causes \nwhole chunks of the victim’s body to crumble to ash. \nThe player rolls Willpower against a difficulty of the \nvictim’s Stamina + 3. For every success, the target \ntakes one aggravated wound. \nThe undead flesh damaged by this power turns to \ndust (gone for the time being), and it must be regen\nerated painstakingly by the victim, should he survive. \nThat dust doubtlessly has mystical properties that vari\nous sorcerers might be able to take advantage of. Every \nwound inflicted by this ability represents the loss of \nabout one-eighth of the target’s weight; the Storyteller \nchooses where the loss comes from. (It might also be \nshed from all over, leaving the victim a bit gaunter or \nmissing chunks of flesh.)\n Regenerating body parts occurs naturally while heal\ning aggravated wounds at the normal rate (see p. 285).",
                },
            ],
        },
        {
            "name": "Nightshade Path",
            "reference": "The Black Hand: A Guide to the Tal'Mahe'Ra; PG 70-71",
            "type": "Necromancy",
            "powers": [
                {
                    "name": "Tend the Body Garden",
                    "description": "Modern forensics makes it possible to determine time of\ndeath with remarkable accuracy — a frightening prospect\nfor Kindred with bodies to hide. On the other hand,\nsometimes it’s better for people to find corpses before rot\ntakes them. Presenting evidence that elder Kindred have\nsuffered the Final Death is sometimes difficult to come\nby, as their bodies rapidly molder into nondescript ash. A necromancer with this power overcomes these difficulties.\nShe can speed up or slow the process of decay, turning\na dead mortal into a bloated host for flies in seconds or\nnullifying the decay of Final Death.",
                    "system": "The player spends one blood point as the vampire\nlets some of her blood drip on to a corpse, and rolls\nWits + Occult (difficulty 6). Successes allow the vampire\nto accelerate or arrest decomposition as follows:\nSuccesses Delay or Accelerate Rot by:\n1 Up to one day\n2 Up to one week\n3 Up to one month\n4 Up to one year\n5+ Storyteller’s discretion\nThe vampire may use this power on mortals and animals\nas long as the remains have not been substantially scattered.\nIt may be used on Kindred no longer than one turn after\nthey’ve met Final Death. Corpses that recently belonged\nto the living change according to local conditions, so that\none stored in a dry place might mummify, while another\nthat rests on soil quickly sprouts plants and maggots. Living\nthings that feed from the dead are quickened or held in\nstasis as the corpse is, provided they’re plants, fungi, or\nno larger than a scarab beetle. Kindred under Final Death\nwither and fall to dust without attracting such organisms.",
                },
                {
                    "name": "Witch's Fruit",
                    "description": "Every plant relies on death to grow. Rotting things\r\nenrich the soil, and the trees, vines, and grasses drink up\r\nnecrotic echoes along with vital nutrients. A necromancer\r\ncan awaken this death aura by exposing their fruits to her\r\nblood. She awakens and concentrates their trace necrotic\r\nenergies so that anyone who consumes them can sense\r\nand touch the Shadowlands.",
                    "system": "The player spends a blood point while the\nvampire touches edible plant matter. No roll is required.\nThe first living creature to eat this tainted meal falls into\na waking, ambulatory trance for a scene, during which\nshe may see into the Shadowlands, hear its denizens, and\neven touch and be touched by ghosts. The target may not\nmake physical contact with buildings and other objects\nthat were never alive, and may not be dragged into the\nTempest or any other place that has no corresponding\nlocation in the living world. Tainted plant matter rots by\nthe next sunrise and loses the ability to impart this state. Witches’ fruits are mild hallucinogens. Twisted visions\nof ghosts and long-fallen buildings disorient mortals under\ntheir influence. This normally imposes +2 to difficulties\nto perform any actions except for Willpower rolls while\naffected. Creatures who are familiar with supernatural\nphenomena don’t suffer this penalty.",
                },
                {
                    "name": "Raise the Green One",
                    "description": "Tales of Kid, Osiris, and the Green Man all describe\r\nbeings who were brought back from death and clothed\r\nin verdant color. Isis raised Osiris to become a symbol of\r\nrebirth and growth, and neopagans say Green Man iconography\r\nremembers the god who is slain by Winter and\r\nreborn in the Goddess’ womb. Nightshade necromancers\r\nchannel these legends into the act of raising a corpse bound\r\nand strengthened by plant matter. Leaves cover its skin\r\nand strong vines supplement its rotted sinews. The living\r\nshell grants speed and self-preservation instincts not seen\r\nin other animated dead.",
                    "system": "The player rolls Wits + Occult (difficulty 8). He\nspends one Willpower point and one blood point while\nconcentrating on a corpse that lays upon or within fertile\nsoil. If the roll succeeds, red-tinged vines, branches, and\nleaves envelop the corpse, and it rises to do the necromancer’s\nbidding. The necromancer may only raise the\nGreen Ones one at a time, and may never have multiple\nGreen Ones active at the same time.\nGreen Ones are stronger, faster, and possess better\ninstincts than most zombies. Their traits are Strength\n4, Dexterity 4, Stamina 4, Athletics 2, Brawl 3, and the\nequivalent of 2 dots of Fortitude, as their damp bodies\nresist injuries. Bashing damage inflicts half damage to a\nGreen One. Like vampires, they suffer bashing damage\nfrom gunfire. Unlike ordinary zombies, they act in standard\ninitiative order.",
                },
                {
                    "name": "Wails and Whispers",
                    "description": "As the necromancer’s understanding deepens, she\r\nexplores the wavering barrier between life and death.\r\nWhen she screams like a banshee, she can lure a soul to\r\nits demise, increasing the chance of a fatal injury. When\r\nshe whispers like a mother to her child, she can fix a soul\r\nin the lands of the living, even when it occupies a body\r\nthat should be dead.",
                    "system": "The vampire concentrates on a target, screaming\nor whispering as her intentions dictate. (The target does not\nneed to be able to hear the vampire.) The player spends one\npoint of Willpower and rolls Wits + Occult (difficulty 8). If\nshe wishes to lure her target closer to death, each success adds\none level of lethal damage to the total inflicted by the next\ninjury he suffers in that scene. If she wishes to prevent the\ntarget from dying, each success sets aside one level of damage\n(of any kind) from the next injury the target suffers during the\nscene, but this benefit only lasts until the end of the scene,\nafter which the set aside damage returns. The target suffers\ninjury but doesn’t feel its effects, up to and including death,\nuntil the scene ends and the damage returns. Note that the\nStoryteller can rule that very large amounts of damage may\ncause death due to total or near-total destruction of the body,\nregardless of this power’s effects.",
                },
                {
                    "name": "Chthonic Womb",
                    "description": "At the apex of this Path, a necromancer combines murder\r\nand fertility to give birth to the ghost of a mortal she has\r\nslain. She drinks the victim’s blood to grab hold of his\r\nsoul, and after dispatching him, traps it within her. At a\r\nlater time, she may call it forth as a ghost to do her bidding.",
                    "system": "The vampire must drink at least one point of\na mortal victim’s blood, but may kill him using another\nmethod. Another person or incident may cause the mortal’s\ndemise, but the necromancer must make physical\ncontact with him at the moment of death. At that point\nthe player spends one point of Willpower and rolls Wits\n+ Occult (difficulty 8). If the player succeeds, the soul\noccupies the vampire’s body in a dormant state for up to\none month per success. (Aura Perception or similar powers\nwill reveal the presence of the dormant soul, which might\nbe mistaken for a form of possession.) The necromancer\nmay store multiple souls this way, but “twins,” “triplets,”\nand more tax the “mother’s” energy. Each soul stored\nbeyond the first drains one additional blood point when\nthe vampire awakens each night.\nAt any point before the soul leaves her body, the vampire\nmay summon it forth to manifest with either the traits\nof a recently deceased ghost (see V20, p. 385) or those it\npossessed in life, along with a recently deceased ghost’s\nsupernatural abilities. It must perform three services for\nits “mother.” After that, the soul is free to move on to its\nultimate destiny. If the ghost is commanded to perform\nany task that would traumatize a mortal (typically, those\nwhich would risk a Humanity check in a vampire with\nthat trait at 7) it may, at the Storyteller’s discretion, treat\nthe necromancer as a “fetter,” an object that the ghost\nfixates upon and uses as a tie to the living world. This gives\nthe ghost the ability to haunt the necromancer until it is\nbanished. The necromancer may always simply dismiss\nthe soul when it appears, or even command it to leave\nher body while the soul still slumbers.",
                },
            ],
        },
        {
            "name": "Path of Haunting",
            "reference": "The Black Hand: A Guide to the Tal'Mahe'Ra; PG 174-175",
            "type": "Necromancy",
            "powers": [
                {
                    "name": "Song of the Dead",
                    "description": "The necromancer weaves death and silence into a \nhaunting song that instills an obsession with death in \nher listener. The victim becomes sure that death stalks \nhim and sees ill omens everywhere. The constant threat \ncan eventually lead a mortal to suicide or drive a vampire \ninto torpor.",
                    "system": "The vampire chants to the victim while her \nplayer spends one blood point and rolls Manipulation \n+ Occult (difficulty of the target's current Willpower). A \nbotch indicates the vampire affects herself as though she \nhad gained successes equal to the number of 1s rolled.\nFor a number of nights equal to the successes rolled, the \ntarget suffers depression and morbid anxiety. This fixation \nadds +2 to the difficulty of Social rolls (except those involving \nIntimidation) and +1 to the difficulty of all other non-reflex-\nive rolls. If a target suffers the effects of this power for more \ncontinuous nights than his permanent Willpower, he loses \na dot of permanent Willpower. This cycle continues after \nan interval of the new rating in days, with the victim losing \na dot of permanent Willpower after each such iteration. \nOnce a character drops to zero permanent Willpower, he \ncommits suicide (If living) or falls into torpor (If a vampire). \nIf the power is interrupted for at least one night, the victim \nrecovers his permanent Willpower at the rate of one dot \nper week. A vampire who falls into otrpoer from reaching \nzero Willpower awakens with his original rating.",
                },
                {
                    "name": "Summon Wisp",
                    "description": "Straddling two worlds, the necromancer does not truly \nexist. She is here, yet she is not. Reaching into herself, she \ninfuses a spark of her own ephemeral nature with dark, \nnecromantic energy. The result is a dancing light, which \nis as hypnotic as it is treacherous.",
                    "system": "The player spends one blood point and rolls \nCharisma + Occult (difficulty 5) to conjure an orb of pale \nlight that lasts one scene. The wisp can take any color the \nvampire chooses and has no substance or weight. It may \nfly as fast as the vampire can run, casting cold illumination \nas bright as a candle. Mortals who behold the wisp must \nroll Willpower (difficulty 4) and achieve more successes \nthan the caster or fall into a mild trance, which adds +1 \nto the difficulty of all actions due to distraction. If the \nvampire's successes are double the mortal's, he follow \nthe light without regard for any but the most obvious \nobstacles. He walks around trees and rocks, but falls prey \nto quicksand or a high parapet. Any loud noise or other \ndistraction immediately breaks the reverie.\nIf the vampire's player botches the conjuration roll, the \nwisp appears and acts with its own malevolent agenda. \nSuch a creature is only a nuisance,, but can display remark- \nabl cunning in luring enemies to the vampire's haven or \ngiving away her position.",
                },
                {
                    "name": "Harrowing",
                    "description": "Even dreams offer no respite to the enemies of the necr- \nmancer. Restful sleep becomes pure terror as Song of the \nDead continues to haunt the sleeper through nightmares.",
                    "system": "The vampire makes eye contactt with the vic- \ntim, while her player spends one blood point and rolls \nManipulation + Occult (difficulty of the target's permanent \nWillpower). If successful, the victim feels a slight sense of \nunease. When he next sleeps, he suffers horrible night- \nmares about his own demise. Even though he cannot fully \nremember the content of his visions after he wakes, the \nemotional trauma prevens him from regaining Willpower. \nIn addition, his twisted deja vu and unnatural parranoia \ngive him the Nightmares and Eerie Presence Flaws (V20, P. \n495) for the day. A botch in castting his power inflicts the \nsame terrible dreams on the vampire when she slumbers.",
                },
                {
                    "name": "Phantasms",
                    "description": "The necromancer recognizes the passion of the dead \nas an illusion. Drawing upon her insight, she may turn \nthese illusions to haunt the living.",
                    "system": "The vampire envisions the desired appari- \ntion, while the player spends one blood point and roll \nManipulation + Occult (Difficulty 7). These creations have \nno substance and cannot speak or perform complicated \nactions, though hey emit a surreal cold. Each success \nallows the vampire to create one phenomenon, or add \none characteristic or condition to another phantom. For \nexample, three successes could animate shadows to shuffle \nand writhe (one success) and create an illusion of dripping \ngore that bursts into a spray of flies when someone draw \nclose (one success for the gore and one success for the \ncondition). This power may create apparitions anywhere \nin the caster's line of sight. The Storyteller remains the \nfinal arbiter of what is or is not possible with this power. \nA botch calls the attention of a malefic ghost, giving the \nvampire the Haunted Flaw (V20, p495) for a number of \nnights equal to the 1s rolled.",
                },
                {
                    "name": "Torment",
                    "description": "The distinction between life and death means nothing \nto the necromancer - it is another illusion, created for \nthe comfort of the living. She may rend this veil and call \nupon malicious apparitions to haunt her victim.",
                    "system": "The player spends one blood point and rolls \nManipulation + Occult (Difficulty 8). On a botch, the \nvampire permanently gains the Haunted Flaw (V20, \nP. 495), attracting the vilest and most hateful ghosts. If \nsuccesful, the victim feels a sudden chill. The difficulty \nfor ghosts to affect the target with any power decreases by \none for every success rolled, or a minimum of difficulty \n4. Malicious ghosts flock to the target, eagerly inflicting \nevery horror at their disposal. The difficulty reduction \ndiminishes by one every day at dawn until the victim \nreturns to normal and the spectres lose interest. Multiple \napplications of this power may not be stacked to increase \nduration or intensity of effect. The statistics and powers \nof spectres are left to the Storyteller, but the experience \nshould terrify the character utterly and may well result in \nderangements at the least.",
                },
            ],
        },
        {
            "name": "Path of the Four Humors",
            "reference": "V20 Core; PG 173",
            "type": "Necromancy",
            "powers": [
                {
                    "name": "Whisper's to the Soul",
                    "description": "The necromancer with this ability can let slip a little \nof her own undead bilious humor as she speaks to an\nother being (whether mortal or Kindred). The wicked \nvapor slips into the target’s ear and whispers night\nmares to the target throughout the day and night. The \ntarget has a harder time sleeping, and becomes irritable \nand distracted during his waking hours.",
                    "system": "The character must whisper the target’s \nname (as she knows it) into his ear. The victim rolls \nWillpower (difficulty 8). If the roll fails, the victim suf\nfers from nightmares and hears mad, wicked mutter\nings while awake, for a number of full days equal to the \nnecromancer’s Manipulation. The victim loses one die \nfrom all dice pools while thus afflicted, and at the Sto\nryteller’s discretion, the difficulty to resist Rötschreck \nmay be increased by one at the same time.",
                },
                {
                    "name": "Kiss of the Dark Mother",
                    "description": "Kiss of the Dark Mother allows the necromancer \nwho uses it to mix her vitae with black bile, turning it \ninto a noxious poison. The necromancer forces it into \nher mouth as saliva might once have come; the vitae \ntastes acrid and bitter, as though it had been scorched. \nOnce the necromancer coats her teeth and lips with it, \nshe can inflict terrible damage with her bite.",
                    "system": "The player spends one blood point; activat\ning this power is a reflexive action, but it must be done \nbefore making a bite attack. If the bite hits, the aggra\nvated damage inflicted by a single bite is doubled before soak is calculated. This power does not affect the \ncharacter’s ability to drain blood from the target, nor \ndoes it increase the amount of damage done by blood \nloss. The necromancer’s bite remains potent until this \nability is discharged by a successful hit or she spends \none turn cleansing the dark blood from her mouth.",
                },
                {
                    "name": "Dark Humors",
                    "description": "The vampire can exude a coat of a particular humor \nonto her skin, causing all that touch it to experience \nthe most intense form of that humor. After a necro\nmancer has used this power, she generally feels the \nopposite of the sensation the humor usually conveys: \nUsing blood leaves her depressed and pessimistic; using \nyellow bile renders her calm and placid; using black \nbile leaves her optimistic; and using phlegm makes her \naroused and angry.",
                    "system": "The player spends two blood points. The \nnecromancer chooses which humor she wishes to ex\ncrete. The humor can simply coat the skin — in which \ncase touching the victim’s skin lets the humor take ef\nfect — or it can act as a poison if placed in a bever\nage (or in vitae). The victim must make a Stamina roll \n(difficulty 8) to resist the effects of the humor:\n • Phlegm: Target becomes lethargic; all dice pools \nare reduced by two for the remainder of the scene.\n • Blood (vitae): Target becomes prone to excessive \nbleeding, and any lethal or aggravated wounds he suf\nfers deal an additional health level of damage on the \nturn after they originally occur. Vitae altered by Dark \nHumors will not turn a human into a ghoul if ingested, \nnor will it initiate a blood bond.\n • Black Bile: Target suffers a number of health levels \nof damage equal to the necromancer’s Stamina. This \ndamage is considered lethal and can be soaked (if the \nvictim is normally capable of soaking such damage), \nthough armor does not protect against it.\n • Yellow Bile: Target becomes melancholic and is \nplagued with visions of death. He cannot spend Will\npower for the remainder of the scene, and all Willpow\ner rolls receive a +2 difficulty.",
                },
                {
                    "name": "Clutching the Shroud",
                    "description": "Blood, the sanguine humor, was regarded by philoso\nphers as being both hot and wet. Blood from a cold \ncorpse has been transubstantiated into a dead form — \na cold incarnation of a hot, wet element. This trans\nformation of the living into death holds great power; \nthe necromancer knows how to infuse her own being \nwith the blood of a cold corpse and transform herself \ninto something not wholly vampiric. Instead, the nec\nromancer edges closer to being an animated corpse in \nfact as well as name. She grows distant and chill, as \nthough possessed by the spirit of Death itself; she has to \nwork to push her attention into the physical world.",
                    "system": "The character must drink, and then spend, \nfive blood points from a cold corpse (one dead for 24 \nhours or more, but generally less than three days). It \nwill generally take at least two turns to consume that \nblood, and the power is not activated until the char\nacter can spend all of it. For example, if the character \nis Twelfth Generation, Clutching the Shroud takes at \nleast seven turns total to activate (two to consume the \nblood and five to spend it). \nAfter the power is active and for the rest of the scene, \nthe necromancer gains several benefits. First, she re\nceives two additional soak dice, which may be used to \nsoak any sort of damage, even if the character does not \npossess Fortitude. Second, she gains a mystic sense of \nhow far those in the area are from death — whether \nthey are healthy or infirm, suffer from diseases, or are \nundead, ghouls, or mortals. Finally, a Manipulation + \nOccult roll lets her speak with ghosts freely. The difficulty for this roll depends on how attuned to death a \nlocale is; a cemetery would be difficulty 5, while a cozy \napartment might be difficulty 7. However, this ability \nmakes the necromancer much more susceptible to the \neffects of powers used by ghosts, which means that she \nmust act carefully.",
                },
                {
                    "name": "Black Breath",
                    "description": "A necromancer who has mastered this path can har\nness the undead black bile that festers at the core of her \nbeing; she pulls that melancholy to her lungs and lets it \nmingle with her outgoing breath. She then exhales the \ndark mist, letting it engulf those nearby. The necro\nmancer feels curiously lightheaded and optimistic after \nusing this power, as she has forced some of her most \ndepressed nature out into the world; those caught in \nthe black vapors grow despairing and hopeless.",
                    "system": "The player spends one Willpower and one \nblood point, and rolls Stamina + Athletics (difficulty \n7). Black Breath allows the character to exhale a dark \ncloud of vapor that is five yards or meters in diameter per \nsuccess rolled. Those caught in the mists may attempt \na Dexterity + Athletics roll to escape it if they have an \navailable action; otherwise, they may be overwhelmed \nby depression to the point of suicide. Those who can\nnot escape the mists must immediately roll Willpower (difficulty 8 for mortals, 7 for supernatural beings) and \nachieve more successes than the invoker did. Mortals \nwho fail in this actively attempt to kill themselves on \ntheir next turn. They do not attempt such ludicrous \nsuicides as praying for a lightning bolt or holding their \nbreath; they use the most effective means at hand to \nend their own lives. If prevented from suicide, they at\ntempt it again as soon as an opportunity presents itself. \nThis impulse lasts for the rest of the scene, and the Sto\nryteller may impose flare-ups over the next day or so at \nhis discretion. Those who succeed on the Willpower \nroll still become enchanted with the prospect of death, \nwhether mortal or Kindred, and lose two dice from all \ndice pools for the rest of the scene.\n Kindred who fail the Willpower roll do not attempt \nsuicide; as they are already dead, the malign influences \nof undead humors do not have as strong an effect on \nthem. Instead, the affected vampire sinks into torpor. \nThe duration of this torpor is based on the vampire’s \nHumanity or Path rating, just as if lethal wounds had \nforced him into it.",
                },
            ],
        },
        {
            "name": "Sepulchre Path",
            "reference": "V20 Core; PG 160",
            "type": "Necromancy",
            "powers": [
                {
                    "name": "Witness of Death",
                    "description": "Before it is possible to control the dead, one must perceive them. This power allows just that, attuning a vampire’s unliving senses to the presence of the in-corporeal. Under its effects, a necromancer sees ghosts as trans-lucent phantoms gliding among the living and hears their whispers and moans. She feels the spectral cold of their touch and smells their musty hint of decay. Yet one cannot mistake the dead for the living, as they lack true substance, and appear dimmer and less real than creatures of flesh and blood. When a vampire uses this power, her eyes flicker with pale blue fire that only the dead can see.Ghosts resent being spied upon, and more powerful shades may use their own powers to inflict their dis-pleasure on the incautious.",
                    "system": "The player rolls Perception + Awareness (difficulty 5). Success allows the vampire to perceive ghosts as described for the rest of the scene (in the mortal world — seeing ghosts in the land of the dead requires Shroudsight, on p. 163). Failure has no special effect, but a botch means the vampire can see only the dead for the scene; everything else appears as shapeless, dim shadows. While the vampire’s other senses remain attuned to the living, he is all but blind in this state and suffers a +3 difficulty to most vision-based Percep-tion rolls and attacks. Ghosts notice the glowing eyes of a vampire using this power only with a successful Perception + Alertness roll (difficulty 7)",
                },
                {
                    "name": "Summon Soul",
                    "description": "The power of Summon Soul allows a necromancer to call a ghost back from the Underworld, for conversa-tional purposes only. In order to perform this feat (and indeed, most of the feats in this path), the vampire must meet certain conditions: \n• The necromancer must know the name of the wraith in question, though an image of the wraith ob-tained via Witness of Death (see above), Shroudsight (see p. 163), Auspex, or other supernatural perception will suffice.\n• An object with which the wraith had some contact in life must be in the vicinity, though it need not be something of significant importance to the ghost’s liv-ing consciousness. A piece of the ghost’s corpse works well for this purpose (and even provides a -1 difficulty modifier).Certain types of ghosts cannot be summoned with this power. Vampires who achieved Golconda before their Final Deaths, or who were diablerized, are beyond the reach of this summons. Likewise, many ghosts of the dead cannot be called — they are destroyed, un-able to return to the mortal plane, or lost in the eternal storm of the Underworld",
                    "system": "The player spends one blood point and rolls Manipulation + Occult (difficulty equal to 7 or the ghost’s Willpower, whichever is higher). The vampire must know the name of the ghost and have on hand an object the ghost had contact with in life. Provided that the target has died and become a ghost, success means the shade appears before the necromancer as described above. Not everyone becomes a ghost — it requires a strong will to persevere in the face of death, and souls that have found peace pass on to their eternal rewards. Moreover, it is possible for the dead to suffer spiritual dissolution and destruction after they become ghosts. The Storyteller should consider all these factors when deciding whether a particular ghost exists for a vampire to summon.Vampires know if their summons should have suc-ceeded by a feeling of sudden, terrifying descent as they reach too far into the great Beyond, so this power can be used to determine whether a soul has endured be-yond death. While a failure means the vampire wastes blood, a botch calls a spirit other than the one sought — usually a malevolent ghost known as a Spectre (see p. 385). Such a fiend torments the one who summoned it with every wicked power at its disposal. Once a ghost is summoned, it may not deliberately move out of sight of the vampire, though it can take any other actions, including direct attack. The vam-pire’s player may spend a Willpower point to dismiss the ghost at any time (unless he rolled a botch). Other-wise, at the end of the scene, shadows engulf the spirit once more and return it to its original location.",
                },
                {
                    "name": "Compel Soul",
                    "description": "With this power, a vampire can command a ghost to do his bidding for a while. Compulsion of the soul is a perilous undertaking and, when used improperly, can endanger vampire and wraith alike.",
                    "system": "The vampire locates and approaches the in-tended ghost or calls it to his presence with Summon Soul. As with the previous power, he must have the ghost’s name and an object it handled in life. His player then spends one blood point and rolls Manipulation + Occult in a resisted roll against the ghost’s Willpower (difficulty 6 for both rolls). If the vampire wins, the number of net successes de-termines the degree of control he has over the ghost (as described below). Moreover, the vampire’s control keeps ghosts that have been called with Summon Soul from returning to their original locations at the end of the scene. If the ghost wins, the vampire loses a number of Willpower points equal to the ghost’s net successes. On a tie, the roll becomes an extended contest that continues each turn until one side wins. If the vampire botches at any point, the ghost is immune to any use of the vampire’s Necromancy for the rest of the scene. If the ghost botches, it must obey as if the vampire’s player had rolled five net successes.  Successes   Result1 success The ghost must perform one simple task for the vampire that does not place it in certain danger. It must attend to this task immediately,  although it can delay the compulsion and pursue its own  business at a cost of one Willpower point per scene. The ghost may not attack the vampire until this task is complete. It is possible to issue the task of answering one question, in which case the ghost must answer truthfully and to the best of its knowledge.2 successes The vampire may issue two orders or ask two questions as outlined for one success. Alternatively, the  vampire may demand a simple task with a real possibility of danger, as long as the danger is not certain. The ghost may delay this compulsion with Willpower.3 successes The vampire may issue three orders as outlined for one success. Alternatively, he may demand the ghost fulfill one difficult and dangerous task or a simple assignment that has an extended duration of up to one month. The ghost may delay such orders with Willpower.4 successes The vampire may issue four orders, as outlined for one success, or   assign two tasks, as for two successes. Alternatively, the vampire may  command the ghost to perform one complex assignment that puts the ghost at extreme risk, or perform any number of non-threatening tasks as the vampire’s slave for up to one month (or, if the necromancer spends a permanent point of Willpower, for a year and a day). It is possible for ghosts to delay individual tasks, but not put off enslavement.5+ successes The vampire may issue multiple orders that have a sum complexity or danger of five successes’ worth. Instead, the vampire may order the ghost to perform any one action that it is capable of executing within one month. Such a task can place the ghost in immediate peril of destruction, or even force it to betray and assault loved ones. It is not  possible for ghosts to delay a task of this magnitude with Willpower — they must obey.",
                },
                {
                    "name": "Haunting",
                    "description": "Haunting binds a summoned ghost to a particular location or, in extreme cases, an object. The wraith cannot leave the area to which the necromancer binds it without risking destruction.",
                    "system": "The player spends one blood point while standing at the location for the haunting or touching the intended prison. She then has the ghost brought to her by whatever means she desires, though Summon Soul is quickest and most reliable. Her player then rolls Manipulation + Occult (difficulty is equal to the target’s current Willpower points if resisted, to a mini-mum of 4; otherwise it is 4). The difficulty rises by one if the vampire wishes to place the ghost in an object. As usual, the difficulty decreases by one if the necro-mancer has a part of the spirit’s corpse in addition to knowing its name (minimum difficulty 3). Each success binds the ghost within the location or object for one night. This duration extends to one week if the player spends a Willpower point or a year and a day for a dot of permanent Willpower. A wraith at-tempting to leave the area of a haunting must make an extended Willpower roll (difficulty 9, four cumulative successes necessary in a single scene) or take a level of aggravated damage for each roll. If the wraith runs out of health levels, it is hurled deep into the Underworld to face destruction.",
                },
                {
                    "name": "Torment",
                    "description": "It is through the use of this power that powerful nec-romancers convince bound ghosts to behave — or else. Torment allows the vampire to strike a wraith as if he himself were in the lands of the dead, inflicting dam-age on the wraith’s ectoplasmic form. The vampire remains in the real world, however, so he cannot be struck in return. Torment allows the vampire to strike a wraith as if he himself were in the lands of the dead, inflicting dam-age on the wraith’s ectoplasmic form. The vampire remains in the real world, however, so he cannot be struck in return.",
                    "system": "The player rolls Stamina + Empathy (dif-ficulty equal to the wraith’s current Willpower points), and the vampire reaches out to strike the wraith. Each success inflicts a level of lethal damage on the wraith. Should the wraith lose all health levels, it immediately vanishes into what appears to be a doorway to some hideous nightmare realm. Ghosts “destroyed” thus can-not reappear in or near the real world for a month.",
                },
            ],
        },
        {
            "name": "Vitreous Path",
            "reference": "V20 Core; PG 174",
            "type": "Necromancy",
            "powers": [
                {
                    "name": "Eyes of the Dead",
                    "description": "The necromancer employing the Eyes of the Dead \ncan see with the perceptions of the Restless Dead \n(called Deathsight). To such a manipulator of ghostly \nenergies, the auras of surrounding beings give off tell\ntale hints as to their health and even their ultimate \nfate; the necromancer can see the energies of death flowing through everyone, just as ghosts can. By look\ning at the entropic markings on a person’s body, the \nnecromancer can gain rough knowledge of how far that \nperson is from death, how soon that person is likely to \ndie, and even what the cause of her death is likely to be. The information thus gained is not exact by any \nmeans, but it gives the necromancer an edge over those \nshe scrutinizes.",
                    "system": "The player rolls Perception + Occult, difficulty 6. One success lets a necromancer determine whether someone is injured, diseased, or dying, as well as whether the individual labors under any sort of curse or baleful magic. \nFurther, the vampire can divine the target’s eventual \ndemise, depending on the successes scored. One suc\ncess means the character can guess how long the tar\nget has to live to within a few weeks. Three successes \nmeans the character can estimate how long the target \nhas to live and what the probable source of death will \nbe, as the entropic markings show the wounds that will \nsomeday exist on that person. Five successes means the character can actually see where and when the event will occur by interpreting the black marks on the target’s soul. \nThis ability lasts for one scene, though the necro\nmancer may choose to end the power early. It can be \nused to read the fate of only one target at a time. Story\ntellers should exercise judgment with this power, since \nthe markings of death are typically unavoidable. He \nmay decide to roll the dice himself, so that the player \nhas no way of knowing whether her insight is correct.",
                },
                {
                    "name": "Aura of Decay",
                    "description": "The necromancer can strengthen the feeling of en\ntropy around her to the point where it breaks down \nnonliving objects and machines. It can gnarl wood, \nrust metal, crack silicon chips, and erode plastic, glass, \nand dead organic material. This power has a range of \none yard or meter from the necromancer’s body, but all \nthose in the presence of the vampire can feel her cor\nruption as an icy wind.",
                    "system": "No roll is required, but this power does cost \nat least one blood point. Objects subjected to this Aura \nof Decay break down and become useless after being \ntargeted. How the object gives out, as well as the exact \nmechanism of failure, is up to the Storyteller. Corro\nsion, metal fatigue, or sheer brittleness are all suitably \nlikely for any given item’s demise, but the in-game ef\nfect of using a doomed item is as if the owning charac\nter rolled a botch. The speed at which an item breaks \ndown depends on how many blood points are spent.\n \n Blood Spent Time to Breakdown\n One       One week\n Two       One day\nThree       End of scene\nFour       Five turns  \nFive       One turn\n\n Note that since this power requires the expenditure \nof blood points, a character cannot cause an Aura of \nDecay while staked.",
                },
                {
                    "name": "Soul Feast",
                    "description": "Just as the necromancer can release entropic ener\ngies from within, she may also pull them into herself \nas a source of power. Soul Feasting allows the caster \nto either draw on the ambient death energies around \nher or to actively feed on a ghost, stealing the wraith’s \nsubstance and mystically transforming that energy into \nsustenance.",
                    "system": "The player spends one Willpower point to allow the vampire to feed on the negative energies of the dead. If the character is drawing the energies from the atmosphere, she must be in a place where death has occurred within the hour or in a place where death is common, such as a cemetery, a morgue, or the scene of a recent murder. Generally, the necromancer can draw anywhere from one to four points of entropy from such a location, although the difficulty in using all Necromancy and similar deathly powers within the area increases by an equal amount for a number of nights \nequal to the points taken. The energies of such an area \nmay only be drained once until the area’s entropy re\nplenishes.\nIn cases when the necromancer feeds on a ghost, the \nvampire must actually attack the wraith as if feeding \nnormally. Wraiths have up to 10 “blood points” that \nmay be taken from them, and they become less and \nless substantial as their spirit essence drains away. The \ncharacter is vulnerable to any attack the ghost might \nmake, even those that do not normally affect the phys\nical world; while feeding, the vampire is essentially in \na half-state, existing in both the living lands and the \nUnderworld simultaneously. The wraith so attacked is \nconsidered immobilized and cannot run or escape un\nless it can defeat the vampire in a resisted Willpower \nroll (difficulty 6 for both sides). This power may also \nbe used in conjunction with Ash Path Necromancy, \nallowing the vampire to drain power (though not sus\ntenance) from ghosts while traveling in the lands of \nthe dead.\n This soul energy may be used just like blood in every respect except for when the vampire rises for the \nnight. It can activate Disciplines, heal wounds, boost \nAttributes, etc. Botching this power renders the vam\npire unable to feed through the Shroud for the rest of \nthe night. However, she remains susceptible to the as\nsaults of ghosts and spirits for several turns (generally, \na number of turns equal to the amount of energy that \ncould have been drawn from the area, or one turn if at\ntacking a ghost) as she hovers between worlds, unable \nto function effectively in either.",
                },
                {
                    "name": "Breath of Thanatos",
                    "description": "The Breath of Thanatos allows the necromancer to \ndraw out entropic energy and focus it upon an area \nor person by taking a deep breath and then forcefully \nexhaling a fog of necromantic energy. This cloud of \nvirulence is completely invisible to anyone without the \nability to see the passing of entropy. The energy of this \ncloud is like a beacon for Spectres, and they are drawn \nto the entropic force like moths to a flame.\n Once the energy is pulled from the necromancer’s \nbody, she can either disperse it over a large area as a \nlure for Spectres, or use the mist for more sinister pur\nposes. Channeled into an object or person, the death\nmist inflicts the subject with a debilitating, wasting ill\nness. Furthermore, the focused energies are tainted and \neerie, and though generally invisible (except to powers \nsuch as Aura Perception), they tend to cause people \nand animals to feel uncomfortable around the victim.",
                    "system": "The player spends one blood point and rolls \nWillpower (difficulty 8). Only one success is needed to \ndraw out the Breath of Thanatos. If dispersed to sum\nmon Spectres, the energies cover roughly one-quarter \nof a mile (400 meters) in radius, centered around the \nnecromancer. The range increases by an additional \none-quarter mile or 400 meters for every additional \nblood point expended. \nSpectres summoned with this power will ignore the \nsummoning necromancer for the duration of the pow\ner unless provoked, but may well go out of their way \nto wreak havoc on anyone else in the vicinity. The \nnecromancer can then use other Necromancy powers \n(such as those in the Sepulchre Path) to manipulate \nand affect these Spectres. Ghosts so targeted may then \ninteract with the necromancer as normal, although the \nother Spectres in the area will continue to ignore both \nthe vampire and the targeted ghost. This energy dis\nperses after a scene, after which the Spectres leave to \nfind new prey. Mechanics for Spectres can be found on \np. 385.\nIf the cloud is directed toward a particular target, the \nnecromancer must either touch the target or direct the \nstream of entropy using Dexterity + Occult (difficulty \n7). A target laden with entropy suffers one (and only \none) level of aggravated damage; this generally mani\nfests as sudden illness or decay. The target’s social difficulties while interacting with those unfamiliar with \nthe touch of death — most normal humans, as well as \nsome supernatural creatures — increase by 2. Further\nmore, supernatural perceptions indicate the target is \ntainted with decay, which can be dangerous. This form \nof taint lasts until sunrise; a victim already plagued by \nthis power cannot be affected again until the previous \nfog of entropy has dispersed.\n A botch on the roll to control this power indicates \nthat the vampire has turned the energy upon himself, \nand suffers all the effects of the vitriolic breath. This \ninflicts the usual injury and may subject the necroman\ncer to the possibly dangerous attention of provoked \nSpectres and other creatures from beyond the grave.",
                },
                {
                    "name": "Night Cry",
                    "description": "The breath of entropic energy becomes a scream of \npure chaos. The necromancer can issue an unearthly cry \n(heard both in the living world and in the Shadowlands). \nThe howl pours icy oblivion into a target or group of \ntargets — either sweeping away the inherent entropy or \ncollecting that destruction and unleashing it.",
                    "system": "The vampire chooses a number of targets \nwithin one yard or meter per dot of Necromancy and \ninvokes Night Cry with a terrible scream. The player \nspends a Willpower point and a blood point for each \ntarget beyond the first. (In other words, she spends \nno blood if only going after one target, or one blood \nfor two targets. Generational blood limits apply, and \nthe vampire may not “pre-spend” blood prior to using \nNight Cry.) \nThe player then chooses whether the vampire will aid \nor harm the targets, and rolls Manipulation + Occult \n(difficulty 6). If she chooses to aid the target or targets, \neach success gives each affected target a -2 difficulty \nmodifier to all of his actions for one turn per success. If \nshe instead chooses harm, each success causes an aggra\nvated wound to each target. Targets may be any kind of \nliving creature, including supernatural ones.\n No matter the result, the Night Cry is heard on both \nsides of the Shroud, attracting the attention of anyone \nnearby. On a botch, the necromancy may summon un\nruly ghosts or Spectres, similar to Breath of Thanatos \n(although the ghosts are under no compulsion to ig\nnore the necromancer…).",
                },
            ],
        },
        {
            "name": "Flow of Ashe (Wanga)",
            "reference": "Rites of the Blood; PG 166",
            "type": "Setite Sorcery",
            "powers": [
                {
                    "name": "Touch of Life",
                    "description": "The wangateur may ingest a special mixture of herbs\r\nand powders in lieu of expending blood when trying to\r\nimitate the characteristics of the living. The effect lasts\r\nfor one scene. The wangateur may ingest this mixture\r\nfor himself or provide it to another Kindred (but not a\r\nmortal) who must swallow the mixture during that scene.\r\nIn the latter case, the wangateur decides which aspect of\r\nthe living the other Kindred will imitated.",
                    "system": "",
                },
                {
                    "name": "Strength of Root and Stone",
                    "description": "The wangateur may inhale a mixture of herbs and\r\npowders through the nose instead of expending blood\r\nwhen trying to augment a Physical Attribute. The effect is\r\nthe same as if the vampire had spent one point of blood\r\nto improve a Physical Attribute. The effect lasts for one\r\nscene. The wangateur may use this mixture himself or\r\nprovide it for another (including a mortal). If it is to be\r\nused by another, the wangateur decides which Attribute\r\nis to be augmented when the mixture is prepared.",
                    "system": "",
                },
                {
                    "name": "Breath of Life",
                    "description": "The wangateur may use a mixture of herbs and powders\r\nin place of blood when trying to heal herself. The specific\r\nmixture produces a paste which the wangateur must physically\r\nsmear on the area to be healed. The effect is the same as if\r\nthe vampire had spent one point of blood to repair physical\r\ndamage. This power cannot be used to heal aggravated damage,\r\nonly bashing or lethal. The wangateur may use this mixture\r\nfor himself or for another (including a mortal).",
                    "system": "",
                },
                {
                    "name": "Favor of the Orishas",
                    "description": "The wangateur may use a mixture of herbs and powders\r\nin order to fuel any Discipline (including blood magic)\r\nthat requires exactly one point of blood to function.\r\nThis formula also requires a small quantity of blood to\r\nfunction, but it need not come from the wangateur and,\r\nin fact, can come from an enemy (human or Kindred) who\r\nhas shed blood nearby. The wangateur may only use this\r\nmixture on herself and must make a superficial cut on\r\nher arm and then rub the mixture into the open wound.",
                    "system": "",
                },
                {
                    "name": "Gift of Ashe",
                    "description": "The wangateur may now create mixtures using the first\r\nthree levels of this path which will maintain their efficacy\r\nfor an entire night rather than just one turn or scene.\r\nFurthermore, the wangateur can maintain a number of\r\nmixtures up to his Intelligence simultaneously. Thus, he\r\ncan provide the mixtures to allies and no longer needs to be\r\nnearby in order to provide the appropriate benefits — he can\r\nsimply give the mixture to an ally and send her on her way.",
                    "system": "",
                },
            ],
        },
        {
            "name": "Path of Praapti (Sadhana)",
            "reference": "Rites of the Blood; PG 165",
            "type": "Setite Sorcery",
            "powers": [
                {
                    "name": "10 yards/meters",
                    "description": "Praapti is the power of instantaneous travel. Indian Sadhana practitioners developed this Path to match their mysterious Asian rivals, who have the power to travel instantly along lines of mystical force. Later, turncoat sadhus sold the secret of this Path to the Tremere, who reverse-engineered it into what they call the Path of Mercury. A handful of New Age Anarchs have also stumbled onto the secret of this path, which they simply call Teleportation. Individual levels of this Path do not have distinct effects; instead, higher mastery simply indicates a farther distance that can be traveled. Ideally, the sorcerer must be able to see the target location or know it intimately. Teleportation is inherently risky and rarely exact, especially when used without clear knowledge of the destination.",
                    "system": "Teleport up to 10 yards/meters. Activating Praapti allows the sorcerer to instantly relocate to a point within short range. The destination should ideally be within sight or intimately known. Failure results in no effect. If the destination is nearby or visible, a botch causes standard blood magic backlash. Blind teleports risk materializing partially inside solid matter, causing aggravated damage per “1” rolled. One success transports only the sorcerer’s nude body, with additional successes allowing twenty extra pounds each. Minor inaccuracies may occur, with each “1” shifting the arrival point by 10% of the total distance.",
                },
                {
                    "name": "50 yards/meters",
                    "description": "Praapti is the power of instantaneous travel. Indian Sadhana practitioners developed this Path to match their mysterious Asian rivals, who have the power to travel instantly along lines of mystical force. Later, turncoat sadhus sold the secret of this Path to the Tremere, who reverse-engineered it into what they call the Path of Mercury. A handful of New Age Anarchs have also stumbled onto the secret of this path, which they simply call Teleportation. Individual levels of this Path do not have distinct effects; instead, higher mastery simply indicates a farther distance that can be traveled. Ideally, the sorcerer must be able to see the target location or know it intimately. Teleportation is inherently risky and rarely exact, especially when used without clear knowledge of the destination.",
                    "system": "Teleport up to 50 yards/meters. The sorcerer may now cross streets, courtyards, or small buildings in an instant. Familiarity with the destination becomes increasingly important, especially when teleporting without line of sight. Failure has no effect, while botches follow the same dangers as lesser uses, potentially resulting in aggravated damage or becoming embedded in solid objects during blind teleports. Each “1” rolled on a successful activation displaces the sorcerer by 10% of the distance traveled. Successes determine carried mass as normal.",
                },
                {
                    "name": "500 yards/meters",
                    "description": "Praapti is the power of instantaneous travel. Indian Sadhana practitioners developed this Path to match their mysterious Asian rivals, who have the power to travel instantly along lines of mystical force. Later, turncoat sadhus sold the secret of this Path to the Tremere, who reverse-engineered it into what they call the Path of Mercury. A handful of New Age Anarchs have also stumbled onto the secret of this path, which they simply call Teleportation. Individual levels of this Path do not have distinct effects; instead, higher mastery simply indicates a farther distance that can be traveled. Ideally, the sorcerer must be able to see the target location or know it intimately. Teleportation is inherently risky and rarely exact, especially when used without clear knowledge of the destination.",
                    "system": "Teleport up to 500 yards/meters. At this level, Praapti allows traversal across neighborhoods or large structures. Blind teleportation grows significantly more dangerous due to the increased distance involved. Botches may leave the sorcerer grievously wounded or trapped inside walls, floors, or other solid matter, with Fortitude only mitigating damage, not entrapment. Imprecision becomes more noticeable, as small percentage deviations can result in substantial displacement. Successes determine how much additional weight may be carried.",
                },
                {
                    "name": "5 miles/8 kilometers",
                    "description": "Praapti is the power of instantaneous travel. Indian Sadhana practitioners developed this Path to match their mysterious Asian rivals, who have the power to travel instantly along lines of mystical force. Later, turncoat sadhus sold the secret of this Path to the Tremere, who reverse-engineered it into what they call the Path of Mercury. A handful of New Age Anarchs have also stumbled onto the secret of this path, which they simply call Teleportation. Individual levels of this Path do not have distinct effects; instead, higher mastery simply indicates a farther distance that can be traveled. Ideally, the sorcerer must be able to see the target location or know it intimately. Teleportation is inherently risky and rarely exact, especially when used without clear knowledge of the destination.",
                    "system": "Teleport up to 5 miles/8 kilometers. The sorcerer may now cross entire districts or cities in a single instant. Accurate knowledge of the destination is critical; blind teleportation at this range is extremely hazardous. A botch may result in severe aggravated damage or complete entombment within large structures or underground spaces. Even on success, errors in arrival location can be dramatic due to distance scaling. One success transports the sorcerer alone, with each additional success allowing twenty more pounds to accompany them.",
                },
                {
                    "name": "500 miles/800 kilometers",
                    "description": "Praapti is the power of instantaneous travel. Indian Sadhana practitioners developed this Path to match their mysterious Asian rivals, who have the power to travel instantly along lines of mystical force. Later, turncoat sadhus sold the secret of this Path to the Tremere, who reverse-engineered it into what they call the Path of Mercury. A handful of New Age Anarchs have also stumbled onto the secret of this path, which they simply call Teleportation. Individual levels of this Path do not have distinct effects; instead, higher mastery simply indicates a farther distance that can be traveled. Ideally, the sorcerer must be able to see the target location or know it intimately. Teleportation is inherently risky and rarely exact, especially when used without clear knowledge of the destination.",
                    "system": "Teleport up to 500 miles/800 kilometers. Mastery of Praapti permits continental-scale instantaneous travel. Such feats demand precise understanding or absolute familiarity with the destination, as blind teleports are almost suicidal. Botches at this level frequently result in catastrophic outcomes, including lethal damage or permanent entrapment. Even successful teleportation is rarely exact, with each “1” rolled potentially displacing the sorcerer by vast distances. The number of successes strictly limits what may be carried, and insufficient successes may leave possessions—or companions—behind at the Storyteller’s discretion.",
                },
            ],
        },
        {
            "name": "Ushabti (Akhu)",
            "reference": "Rites of the Blood; PG 163",
            "type": "Setite Sorcery",
            "powers": [
                {
                    "name": "Laborer",
                    "description": "The ushabti can be a human or an animal. It is mindless and obeys all orders from its master. It has two dots in each Physical Attribute, one dot in each Mental Attribute, and no dots in any Social Attribute. It has no Abilities.",
                    "system": "Activated ushabti have Attributes and Abilities determined by the level of the path used to create them. The sorcerer may not grant an ushabti Abilities she does not have nor Ability ratings higher than her own. The successes on the Willpower roll determine how realistic the activated ushabti is. However, the successes applied to “realism” can never exceed the path rating used. Thus, only an ushabti created with Gift of Khnum (Ushabti •••••) can be indistinguishable from a living creature.SuccessesResults1A crude thing obviously made of wax.2As realistic as a well-made waxwork or a china doll.3Lifelike enough to fool a casual viewer (difficulty 6 to detect as fake)4Extremely lifelike (difficulty 8 to detect as unreal)5Indistinguishable from a living creatureOnce activated, the ushabti endures for one lunar month, but this can be extended indefinitely at a cost of one point of blood per additional month. However, this assumes that the ushabti remains within its master’s haven and does not interact with mortals. If those conditions are broken, the ushabti will degrade into nothingness within an hour. A sorcerer can craft an ushabti for use by another, but doing so costs him one Willpower.",
                },
                {
                    "name": "Servitor",
                    "description": "To the Laborer, add three additional Attribute dots. None can be applied to any Social Attribute, and no Mental Attribute can rise above 2. Add two dots of non-combat Abilities",
                    "system": "Activated ushabti have Attributes and Abilities determined by the level of the path used to create them. The sorcerer may not grant an ushabti Abilities she does not have nor Ability ratings higher than her own. The successes on the Willpower roll determine how realistic the activated ushabti is. However, the successes applied to “realism” can never exceed the path rating used. Thus, only an ushabti created with Gift of Khnum (Ushabti •••••) can be indistinguishable from a living creature.SuccessesResults1A crude thing obviously made of wax.2As realistic as a well-made waxwork or a china doll.3Lifelike enough to fool a casual viewer (difficulty 6 to detect as fake)4Extremely lifelike (difficulty 8 to detect as unreal)5Indistinguishable from a living creatureOnce activated, the ushabti endures for one lunar month, but this can be extended indefinitely at a cost of one point of blood per additional month. However, this assumes that the ushabti remains within its master’s haven and does not interact with mortals. If those conditions are broken, the ushabti will degrade into nothingness within an hour. A sorcerer can craft an ushabti for use by another, but doing so costs him one Willpower.",
                },
                {
                    "name": "Guard",
                    "description": "To the Laborer, add six dots of Attributes and four dots of Abilities. Guards may have Social Attributes, but no Social or Mental Attribute may exceed 2, nor can any Ability.",
                    "system": "Activated ushabti have Attributes and Abilities determined by the level of the path used to create them. The sorcerer may not grant an ushabti Abilities she does not have nor Ability ratings higher than her own. The successes on the Willpower roll determine how realistic the activated ushabti is. However, the successes applied to “realism” can never exceed the path rating used. Thus, only an ushabti created with Gift of Khnum (Ushabti •••••) can be indistinguishable from a living creature.SuccessesResults1A crude thing obviously made of wax.2As realistic as a well-made waxwork or a china doll.3Lifelike enough to fool a casual viewer (difficulty 6 to detect as fake)4Extremely lifelike (difficulty 8 to detect as unreal)5Indistinguishable from a living creatureOnce activated, the ushabti endures for one lunar month, but this can be extended indefinitely at a cost of one point of blood per additional month. However, this assumes that the ushabti remains within its master’s haven and does not interact with mortals. If those conditions are broken, the ushabti will degrade into nothingness within an hour. A sorcerer can craft an ushabti for use by another, but doing so costs him one Willpower.",
                },
                {
                    "name": "Overseer",
                    "description": "To the Laborer, add nine dots of Attributes and six dots of Abilities; no Social or Mental Attribute may exceed 3, nor can any Ability.",
                    "system": "Activated ushabti have Attributes and Abilities determined by the level of the path used to create them. The sorcerer may not grant an ushabti Abilities she does not have nor Ability ratings higher than her own. The successes on the Willpower roll determine how realistic the activated ushabti is. However, the successes applied to “realism” can never exceed the path rating used. Thus, only an ushabti created with Gift of Khnum (Ushabti •••••) can be indistinguishable from a living creature.SuccessesResults1A crude thing obviously made of wax.2As realistic as a well-made waxwork or a china doll.3Lifelike enough to fool a casual viewer (difficulty 6 to detect as fake)4Extremely lifelike (difficulty 8 to detect as unreal)5Indistinguishable from a living creatureOnce activated, the ushabti endures for one lunar month, but this can be extended indefinitely at a cost of one point of blood per additional month. However, this assumes that the ushabti remains within its master’s haven and does not interact with mortals. If those conditions are broken, the ushabti will degrade into nothingness within an hour. A sorcerer can craft an ushabti for use by another, but doing so costs him one Willpower.",
                },
                {
                    "name": "Gift of Khnum",
                    "description": "The ultimate expression of this art, the Gift of Khnum (the legendary creator of humanity according to Egyptian lore) allows the sorcerer to create what is effectively a living body, either as an obedient slave or as a ready-made vessel for a wraith or a spirit. The character who activates the ushabti decides which, although the latter option requires her to have a compliant wraith or spirit handy.To the basic Laborer, add 12 dots of Attributes and eight dots of Abilities. The ushabti gains the Virtues, Humanity, and Willpower of a starting vampire. It is sentient but emotionally bound to the one who activates it as if by a blood bond. This is true even if a spirit or wraith possesses it. Each use of Gift of Khnum costs two Willpower points at the time of activation, and the player may spend additional Willpower points to gain automatic successes on the activation roll. An ushabti created with this Path does not degrade unless someone actively challenges its identity and persuades it that it is not real. Absent proof of its own unreality, the ushabti is effectively immortal.",
                    "system": "Activated ushabti have Attributes and Abilities determined by the level of the path used to create them. The sorcerer may not grant an ushabti Abilities she does not have nor Ability ratings higher than her own. The successes on the Willpower roll determine how realistic the activated ushabti is. However, the successes applied to “realism” can never exceed the path rating used. Thus, only an ushabti created with Gift of Khnum (Ushabti •••••) can be indistinguishable from a living creature.SuccessesResults1A crude thing obviously made of wax.2As realistic as a well-made waxwork or a china doll.3Lifelike enough to fool a casual viewer (difficulty 6 to detect as fake)4Extremely lifelike (difficulty 8 to detect as unreal)5Indistinguishable from a living creatureOnce activated, the ushabti endures for one lunar month, but this can be extended indefinitely at a cost of one point of blood per additional month. However, this assumes that the ushabti remains within its master’s haven and does not interact with mortals. If those conditions are broken, the ushabti will degrade into nothingness within an hour. A sorcerer can craft an ushabti for use by another, but doing so costs him one Willpower.",
                },
            ],
        },
        {
            "name": "Elemental Mastery",
            "reference": "V20 Core; PG 214",
            "type": "Thaumaturgy",
            "powers": [
                {
                    "name": "Elemental Strength",
                    "description": "The vampire can draw upon the strength and resilience\r\nof the earth, or of the objects around him, to increase\r\nhis physical prowess without the need for large\r\namounts of blood.",
                    "system": "The player allocates a total of three temporary\r\nbonus dots between the character’s Strength\r\nand Stamina. The number of successes on the roll to\r\nactivate the power is the number of turns these dots\r\nremain. The player may spend a Willpower point to\r\nincrease this duration by one turn. This power cannot\r\nbe “stacked” — one application must expire before the\r\nnext can be made.",
                },
                {
                    "name": "Wooden Tongues",
                    "description": "A vampire may speak, albeit in limited fashion, with\r\nthe spirit of any inanimate object. The conversation\r\nmay not be incredibly interesting, as most rocks and\r\nchairs have limited concern for what occurs around\r\nthem, but the vampire can get at least a general impression\r\nof what the subject has “experienced.” Note\r\nthat events which are significant to a vampire may not\r\nbe the same events that interest a lawn gnome.",
                    "system": "The number of successes dictates the amount\r\nand relevance of the information that the character receives.\r\nOne success may yield a boulder’s memory of a\r\nforest fire, while three may indicate that it remembers\r\na shadowy figure running past, and five will cause the\r\nrock to relate a precise description of a local Gangrel.",
                },
                {
                    "name": "Animate the Unmoving",
                    "description": "Objects affected by this power move as the vampire\r\nusing it dictates. An object cannot take an action that\r\nwould be completely inconceivable for something with\r\nits form — for instance, a door could not leap from\r\nits hinges and carry someone across a street. However,\r\nseemingly solid objects can become flexible within reason:\r\nBarstools can run with their legs, guns can twist\r\nout of their owners’ hands or fire while holstered, and\r\nhumanoid statues can move like normal humans.",
                    "system": "This power requires the expenditure of a\r\nWillpower point with less than four successes on the\r\nroll. Each use of this power animates one object no\r\nlarger than human-sized; the caster may simultaneously\r\ncontrol a number of animate objects equal to his Intelligence\r\nrating. Objects animated by this power stay\r\nanimated as long as they are within the caster’s line of\r\nsight or up to an hour, although the thaumaturge can\r\ntake other actions during that time.",
                },
                {
                    "name": "Elemental Form",
                    "description": "The vampire can take the shape of any inanimate\r\nobject of a mass roughly equal to her own. A desk, a\r\nstatue, or a bicycle would be feasible, but a house or a\r\npen would be beyond this power’s capacity.",
                    "system": "The number of successes determines how\ncompletely the character takes the shape she wishes\nto counterfeit. At least three successes are required for the character to use her senses or Disciplines while in\r\nher altered form. This power lasts for the remainder of\r\nthe night, although the character may return to her\r\nnormal form at will.",
                },
                {
                    "name": "Summon Elemental",
                    "description": "A vampire may summon one of the traditional spirits\r\nof the elements: a salamander (fire), a sylph (air),\r\na gnome (earth), or an undine (water). Some thaumaturges\r\nclaim to have contacted elemental spirits of\r\nglass, electricity, blood, and even atomic energy, but\r\nsuch reports remain unconfirmed (even as their authors\r\nare summoned to Vienna for questioning). The\r\ncaster may choose what type of elemental he wishes to\r\nsummon and command.",
                    "system": "The character must be near some quantity\nof the classical element corresponding to the spirit\nhe wishes to invoke. The spirit invoked may or may\nnot actually follow the caster’s instructions once summoned,\nbut generally will at least pay rough attention\nto what it’s being told to do. The number of successes\ngained on the Willpower roll determines the power\nlevel of the elemental.\nThe elemental has three dots in all Physical and\nMental Attributes. One dot may be added to one of\nthe elemental’s Physical Attributes for each success\ngained by the caster on the initial roll. The Storyteller\nshould determine the elemental’s Abilities, attacks,\nand damage, and any special powers it has related to\nits element.\nOnce the elemental has been summoned, the thaumaturge\nmust exert control over it. The more powerful\nthe elemental, the more difficult a task this is. The\nplayer rolls Manipulation + Occult (difficulty of the\nnumber of successes scored on the casting roll + 4),\nand the number of successes determines the degree of\ncontrol:\nSuccesses Result\nBotch The elemental immediately attacks\nthe thaumaturge.\nFailure The elemental goes free and may\nattack anyone or leave the scene\nat the Storyteller’s discretion.\n1 success The elemental does not attack its\nsummoner.\n2 successes The elemental behaves favorably\ntoward the summoner and may\nperform a service in exchange forpayment (determined by the\r\nStoryteller).\r\n3 successes The elemental performs one service,\r\nwithin reason.\r\n4 successes The elemental performs any one task\r\nfor the caster that does not jeopardize\r\nits own existence.\r\n5 successes The elemental performs any task that\r\nthe caster sets for it, even one that\r\nmay take several nights to complete\r\nor that places its existence at risk. payment (determined by the\r\nStoryteller).\r\n3 successes The elemental performs one service,\r\nwithin reason.\r\n4 successes The elemental performs any one task\r\nfor the caster that does not jeopardize\r\nits own existence.\r\n5 successes The elemental performs any task that\r\nthe caster sets for it, even one that\r\nmay take several nights to complete\r\nor that places its existence at risk.",
                },
            ],
        },
        {
            "name": "Green Path",
            "reference": "V20 Core; PG 215",
            "type": "Thaumaturgy",
            "powers": [
                {
                    "name": "Herbal Wisdom",
                    "description": "With a touch, a vampire can commune with the\r\nspirit of a plant. Conversations held in this manner are\r\noften cryptic but rewarding — the wisdom and experience\r\nof the spirits of some trees surpasses that of the\r\noracles of legend. Crabgrass, on the other hand, rarely\r\nhas much insight to offer, but might reveal the appearance\r\nof the last person who trod upon it.",
                    "system": "The number of successes rolled determines\r\nthe amount of information that can be gained from the\r\ncontact. Depending on the precise information that\r\nthe vampire seeks, the Storyteller might require the\r\nplayer to roll Intelligence + Occult in order to interpret\r\nthe results of the communication.\r\nSuccesses Result\r\n1 success Fleeting cryptic impressions\r\n2 successes One or two clear images\r\n3 successes A concise answer to a simple query\r\n4 successes A detailed response to one or more\r\ncomplex questions\r\n5 successes The sum total of the plant-spirit’s\r\nknowledge on a given subject",
                },
                {
                    "name": "Speed the Seasons Passing",
                    "description": "This power allows a thaumaturge to accelerate a plant’s\r\ngrowth, causing roses to bloom in a matter of minutes or\r\ntrees to shoot up from saplings overnight. Alternately,\r\nshe can speed a plant’s death and decay, withering grass\r\nand crumbling wooden stakes with but a touch.",
                    "system": "The character touches the target plant. The\r\nplayer rolls normally, and the number of successes determines\r\nthe amount of growth or decay. One success\r\ngives the plant a brief growth spurt or simulates the effects\r\nof harsh weather, while three noticeably enlarge\r\nor wither it. With five successes, a full-grown plant\r\nsprings from a seed or crumbles to dust in a few minutes,\r\nand a tree sprouts fruit or begins decaying almost\r\ninstantaneously. If this power is used in combat, three\r\nsuccesses are needed to render a wooden weapon completely\r\nuseless. Two successes suffice to weaken it, while\r\nfive cause it to disintegrate in the wielder’s hand.",
                },
                {
                    "name": "Dance of Vines",
                    "description": "The thaumaturge can animate a mass of vegetation\r\nup to his own size, using it for utilitarian or combat purposes\r\nwith equal ease. Leaves can walk along a desktop,\r\nivy can act as a scribe, and jungle creepers can strangle\r\nopponents. Intruders should beware of Tremere workshops\r\nthat harbor potted rowan saplings.",
                    "system": "Any total amount of vegetation with a mass\r\nless than or equal to the character’s own may be animated\r\nthrough this power. The plants stay active for one turn\r\nper success scored on the roll, and are under the complete\r\ncontrol of the character. If used for combat purposes, the\r\nplants have Strength and Dexterity ratings each equal\r\nto half the character’s Willpower (rounded down) and\r\nBrawl ratings one lower than that of the character.\r\nDance of Vines cannot make plants uproot themselves\r\nand go stomping about. Even the most energetic\r\nvegetation is incapable of pulling out of the soil and\r\nwalking under the effect of this power. However, 200\r\npounds (100 kilograms) of kudzu can cover a considerable\r\narea all by itself….",
                },
                {
                    "name": "Verdant Haven",
                    "description": "This power weaves a temporary shelter out of a sufficient\r\namount of plant matter. In addition to providing physical\r\nprotection from the elements (and even sunlight), the\r\nVerdant Haven also establishes a mystical barrier which\r\nis nearly impassable to anyone the caster wishes to exclude.\r\nA Verdant Haven appears as a six-foot-tall (twometer-\r\ntall) hemisphere of interlocked branches, leaves, and vines with no discernible opening, and even to the\r\ncasual observer it appears to be an unnatural construction.\r\nVerdant Havens are rumored to have supernatural\r\nhealing properties, hut no Kindred have reported experiencing\r\nsuch benefits from a stay in one.",
                    "system": "A character must be standing in a heavily\r\nvegetated area to use this power. The Verdant Haven\r\nsprings up around the character over the course of three\r\nturns. Once the haven is established, anyone wishing\r\nto enter the haven without the caster’s permission\r\nmust achieve more than the caster’s original number of\r\nsuccesses on a single roll of Wits + Survival (difficulty\r\nequal to the caster’s Willpower). The haven lasts until\r\nthe next sunset, or until the caster dispels or leaves it.\r\nIf the caster scored four or more successes, the haven is\r\nimpenetrable to sunlight unless physically breached.",
                },
                {
                    "name": "Awaken the Forest Giants",
                    "description": "Entire trees can be animated by a master of the\r\nGreen Path. Ancient oaks can be temporarily given\r\nthe gift of movement, pulling their roots from the soil\r\nand shaking the ground with their steps. While not as\r\nversatile as elementals or other summoned spirits, trees\r\nbrought to ponderous life via this power display awesome\r\nstrength and resilience.",
                    "system": "The character touches the tree to be animated.\r\nThe player spends a blood point and rolls normally.\r\nIf the roll succeeds, the player must spend a blood\r\npoint for every success. The tree stays animated for one\r\nturn per success rolled; once this time expires, the tree\r\nputs its roots down wherever it stands and cannot be\r\nanimated again until the next night. While animated,\r\nthe tree follows the character’s verbal commands to\r\nthe best of its ability. An animated tree has Strength\r\nand Stamina equal to the caster’s Thaumaturgy rating,\r\nDexterity 2, and a Brawl rating equal to the caster’s\r\nown. It is immune to bashing damage, and all lethal\r\ndamage dice pools are halved due to its size.\r\nOnce the animating energy leaves a tree, it puts\r\ndown roots immediately, regardless of what it is currently\r\nstanding on. A tree re-establishing itself in the\r\nsoil can punch through concrete and asphalt to find\r\nnourishing dirt and water underneath, meaning that it\r\nis entirely possible for a sycamore to root itself in the\r\nmiddle of a road without any warning.",
                },
            ],
        },
        {
            "name": "Hands of Destruction",
            "reference": "V20 Core; PG 217",
            "type": "Thaumaturgy",
            "powers": [
                {
                    "name": "Decay",
                    "description": "This power accelerates the decrepitude of its target,\r\ncausing it to wither, rot, or otherwise break down. The\r\ntarget must be inanimate, though dead organic matter\r\ncan be affected.",
                    "system": "If the roll is successful, the inanimate object\r\ntouched by the thaumaturge ages 10 years for every\r\nminute the Kindred touches it. If the vampire breaks\r\nphysical contact and wishes to age the object again,\r\nanother blood point must be spent and another roll\r\nmust be made. This power does not affect vampires.",
                },
                {
                    "name": "Gnarl Wood",
                    "description": "This power warps and bends wooden objects.\r\nThough the wood is otherwise undamaged, this power\r\noften leaves the objects completely useless. This power\r\nmay also be used to swell or contract wood, in addition\r\nto bending it into unwholesome shapes. Unlike\r\nother powers of this path, Gnarl Wood requires merely\r\na glance rather than physical contact.",
                    "system": "Fifty pounds or twenty-five kilograms of visible\r\nwood may be gnarled for each blood point spent\r\non this power (the thaumaturge may expend as much\r\nblood as she likes on this power, up to her per-turn\r\ngenerational maximum). It is also possible to warp\r\nmultiple visible objects — like all the stakes a team of\r\nvampire-hunters wields.",
                },
                {
                    "name": "Acidic Touch",
                    "description": "The vampire secretes a bilious, acidic fluid from any\r\nportion of his body. The viscous acid corrodes metal,\r\ndestroys wood, and causes horrendous chemical burns\r\nto living tissue.",
                    "system": "The player spends one blood point to create\r\nthe acid — the blood literally transmutes into the volatile\r\nsecretion. One blood point creates enough acid to\r\nburn through a quarter-inch or half a centimeter of steel\r\nplate or three inches (seven centimeters) of wood. The\r\ndamage from an acid-augmented hand-to-hand attack\r\nis aggravated and costs one blood point per turn to use.\r\nA thaumaturge is immune to her own acidic touch.",
                },
                {
                    "name": "Atrophy",
                    "description": "This power withers a victim’s limb, leaving only a desiccated,\r\nalmost mummified husk of bone and skin. The effects\r\nare instantaneous; in mortals, they are also irreversible.",
                    "system": "The victim may resist the effects of Atrophy\r\nby scoring three or more successes on a Stamina + Athletics\r\nroll (difficulty 8). Failure means the limb is permanently\r\nand completely crippled. Partial resistance\r\nis possible: One success indicates that the difficulty of\r\nany roll involving the use of the arm increases by two,\r\nthough these effects are still permanent with regard to\r\nmortals. Two successes signify that difficulties increase\r\nby one. Vampires afflicted by this power may spend five\r\nblood points to rejuvenate atrophied limbs. Mortals are\r\npermanently crippled. This power affects only limbs or\r\nparts of limbs (arms, legs, hands); it does not work on\r\nvictims’ heads, torsos, etc.",
                },
                {
                    "name": "Turn to Dust",
                    "description": "This fearsome power accelerates decrepitude in its\r\nvictims. Mortals literally age at the mere touch of a\r\nskilled thaumaturge, gaining decades in moments.",
                    "system": "Each success on the roll ages the victim by\r\n10 years. A potential victim may resist with a Stamina\r\n+ Courage roll (difficulty 8), but must accumulate\r\nmore successes than the caster’s activation roll — it’s\r\nan all-or-nothing affair. If the victim succeeds, he does\r\nnot age at all. If he does not acquire more successes\r\nthan the thaumaturge, he ages the full amount. Obviously,\r\nthis power, while it affects vampires, has no detrimental\r\neffect on them (they’re immortal). At most, a\r\nKindred victim grows paler and withers slightly (-1 to\r\nAppearance) for one night.",
                },
            ],
        },
        {
            "name": "Lure of Flames",
            "reference": "V20 Core; PG 218",
            "type": "Thaumaturgy",
            "powers": [
                {
                    "name": "Candle",
                    "description": "This path grants the thaumaturge the ability to conjure forth mystical flames — small fires at first, but skilled magicians may create great conflagrations. Fire created by this path is not “natural.” In fact, many vampires believe the flames to be conjured from Hell itself. The Lure of Flames is greatly feared, as fire is one of the surest ways to bring Final Death upon a vampire. See “Fire” (p. 297) for more information on how vampires suffer from flame.\n\nFire conjured by The Lure of Flames must be released for it to have any effect. Thus, a “palm of flame” does not burn the vampire’s hand and cause an aggravated wound (nor does it cause the caster to frenzy) — it merely produces light. Once the flame has been released, however, it burns normally and the character has no control over it.",
                    "system": "The number of successes determines how accurately the vampire places the flame in his desired location (declared before the roll is made). One success is all that is necessary to conjure a flame in one’s hand, while five successes place a flame anywhere in the Kindred’s line of sight. Less successes mean that the flame appears somewhere at the Storyteller’s discretion — as a rough rule of thumb, the thaumaturge can accurately place a flame within 10 yards or meters of themselves per success. Individual descriptions are not provided for each level of this path — fire is fire, after all (including potentially causing frenzy in other vampires witnessing it). The chart below describes the path level required to generate a specific amount of flame. To soak the damage at all, a vampire must have the Fortitude Discipline. Fire under the caster’s control does not harm the vampire or cause him to frenzy, but fires started as a result of the unnatural flame affect the thaumaturge normally.\nCandle (difficulty 3 to soak, one health level of aggravated damage/ turn)",
                },
                {
                    "name": "Palm of Flame",
                    "description": "This path grants the thaumaturge the ability to conjure forth mystical flames — small fires at first, but skilled magicians may create great conflagrations. Fire created by this path is not “natural.” In fact, many vampires believe the flames to be conjured from Hell itself. The Lure of Flames is greatly feared, as fire is one of the surest ways to bring Final Death upon a vampire. See “Fire” (p. 297) for more information on how vampires suffer from flame.\n\nFire conjured by The Lure of Flames must be released for it to have any effect. Thus, a “palm of flame” does not burn the vampire’s hand and cause an aggravated wound (nor does it cause the caster to frenzy) — it merely produces light. Once the flame has been released, however, it burns normally and the character has no control over it.",
                    "system": "The number of successes determines how accurately the vampire places the flame in his desired location (declared before the roll is made). One success is all that is necessary to conjure a flame in one’s hand, while five successes place a flame anywhere in the Kindred’s line of sight. Less successes mean that the flame appears somewhere at the Storyteller’s discretion — as a rough rule of thumb, the thaumaturge can accurately place a flame within 10 yards or meters of themselves per success. Individual descriptions are not provided for each level of this path — fire is fire, after all (including potentially causing frenzy in other vampires witnessing it). The chart below describes the path level required to generate a specific amount of flame. To soak the damage at all, a vampire must have the Fortitude Discipline. Fire under the caster’s control does not harm the vampire or cause him to frenzy, but fires started as a result of the unnatural flame affect the thaumaturge normally. \nPalm of flame (difficulty 4 to soak, one health level of aggravated damage/turn)",
                },
                {
                    "name": "Campfire",
                    "description": "This path grants the thaumaturge the ability to conjure forth mystical flames — small fires at first, but skilled magicians may create great conflagrations. Fire created by this path is not “natural.” In fact, many vampires believe the flames to be conjured from Hell itself. The Lure of Flames is greatly feared, as fire is one of the surest ways to bring Final Death upon a vampire. See “Fire” (p. 297) for more information on how vampires suffer from flame.\n\nFire conjured by The Lure of Flames must be released for it to have any effect. Thus, a “palm of flame” does not burn the vampire’s hand and cause an aggravated wound (nor does it cause the caster to frenzy) — it merely produces light. Once the flame has been released, however, it burns normally and the character has no control over it.",
                    "system": "The number of successes determines how accurately the vampire places the flame in his desired location (declared before the roll is made). One success is all that is necessary to conjure a flame in one’s hand, while five successes place a flame anywhere in the Kindred’s line of sight. Less successes mean that the flame appears somewhere at the Storyteller’s discretion — as a rough rule of thumb, the thaumaturge can accurately place a flame within 10 yards or meters of themselves per success. Individual descriptions are not provided for each level of this path — fire is fire, after all (including potentially causing frenzy in other vampires witnessing it). The chart below describes the path level required to generate a specific amount of flame. To soak the damage at all, a vampire must have the Fortitude Discipline. Fire under the caster’s control does not harm the vampire or cause him to frenzy, but fires started as a result of the unnatural flame affect the thaumaturge normally. \nCampfire (difficulty 5 to soak, two health levels of aggravated damage/turn)",
                },
                {
                    "name": "Bonfire",
                    "description": "This path grants the thaumaturge the ability to conjure forth mystical flames — small fires at first, but skilled magicians may create great conflagrations. Fire created by this path is not “natural.” In fact, many vampires believe the flames to be conjured from Hell itself. The Lure of Flames is greatly feared, as fire is one of the surest ways to bring Final Death upon a vampire. See “Fire” (p. 297) for more information on how vampires suffer from flame.\n\nFire conjured by The Lure of Flames must be released for it to have any effect. Thus, a “palm of flame” does not burn the vampire’s hand and cause an aggravated wound (nor does it cause the caster to frenzy) — it merely produces light. Once the flame has been released, however, it burns normally and the character has no control over it.",
                    "system": "The number of successes determines how accurately the vampire places the flame in his desired location (declared before the roll is made). One success is all that is necessary to conjure a flame in one’s hand, while five successes place a flame anywhere in the Kindred’s line of sight. Less successes mean that the flame appears somewhere at the Storyteller’s discretion — as a rough rule of thumb, the thaumaturge can accurately place a flame within 10 yards or meters of themselves per success. Individual descriptions are not provided for each level of this path — fire is fire, after all (including potentially causing frenzy in other vampires witnessing it). The chart below describes the path level required to generate a specific amount of flame. To soak the damage at all, a vampire must have the Fortitude Discipline. Fire under the caster’s control does not harm the vampire or cause him to frenzy, but fires started as a result of the unnatural flame affect the thaumaturge normally. \nBonfire (difficulty 7 to soak, two health levels of aggravated damage/turn)",
                },
                {
                    "name": "Inferno",
                    "description": "This path grants the thaumaturge the ability to conjure forth mystical flames — small fires at first, but skilled magicians may create great conflagrations. Fire created by this path is not “natural.” In fact, many vampires believe the flames to be conjured from Hell itself. The Lure of Flames is greatly feared, as fire is one of the surest ways to bring Final Death upon a vampire. See “Fire” (p. 297) for more information on how vampires suffer from flame.\n\nFire conjured by The Lure of Flames must be released for it to have any effect. Thus, a “palm of flame” does not burn the vampire’s hand and cause an aggravated wound (nor does it cause the caster to frenzy) — it merely produces light. Once the flame has been released, however, it burns normally and the character has no control over it.",
                    "system": "The number of successes determines how accurately the vampire places the flame in his desired location (declared before the roll is made). One success is all that is necessary to conjure a flame in one’s hand, while five successes place a flame anywhere in the Kindred’s line of sight. Less successes mean that the flame appears somewhere at the Storyteller’s discretion — as a rough rule of thumb, the thaumaturge can accurately place a flame within 10 yards or meters of themselves per success. Individual descriptions are not provided for each level of this path — fire is fire, after all (including potentially causing frenzy in other vampires witnessing it). The chart below describes the path level required to generate a specific amount of flame. To soak the damage at all, a vampire must have the Fortitude Discipline. Fire under the caster’s control does not harm the vampire or cause him to frenzy, but fires started as a result of the unnatural flame affect the thaumaturge normally. \nInferno (difficulty 9 to soak, three health levels of aggravated damage/turn)",
                },
            ],
        },
        {
            "name": "Mastery of the Mortal Shell",
            "reference": "Rites of the Blood; PG 138",
            "type": "Thaumaturgy",
            "powers": [
                {
                    "name": "Vertigo",
                    "description": "The thaumaturge induces minor disorientation\nand dizziness through subtle manipulations in the\nsubject's body. The physical discomfort is temporary\nand minor, but a clever thaumaturge can use it on rivals\nat the most inopportune times, causing them to\nlose their aplomb.",
                    "system": "A touch from the thaumaurge invokes\ndisorientation in he vicim. If successful,\nall of he victim's physical actions are at\n+1 difficulty for he duration of the power.\nSubsequent uses of this Patth may extend\nthe duration, though the difficulty will not \nincrease further.",
                },
                {
                    "name": "Contortion",
                    "description": "With a touch, the thaumaturge causes a group\nof her opponent's muscles to contract involuntarily,\nreducing it to twitching fits. This effect is extremely\ndisconcerting to the subject, rendering the limb\nor muscle group unusable.",
                    "system": "By making physical contact with one of\nthe limbs of the target, the thaumaturge\nrenders it useless for the duration of Contortion.\nA leg rendered useless makes standing difficult,\nand the victim suffers from increased difficulty \n(+1 to +3, depending on circumstances) to\nappropriate dexterity challenges related to her leg,\nsuch as dancing or balancing on ledges. A contorted arm\n hangs lifeless at the subject's side. A useless head causes\nspeech and increases the difficulty of all Social rolls by 2 as\nthe facial muscles spasm out of control.",
                },
                {
                    "name": "Seizure",
                    "description": "Seizure causes the body to erupt into a fit\nof convulsions. All the muscles throughout\nthe body tighten uncontrollably, while the\nvictim foams at the mouth and spasms rack\nhim with agony. A mortal may even choke to\ndeath as her tongue cuts off her air supply.",
                    "system": "A light touch from the thaumaturge forces the very\nunpleasant effects of this power upon the target.\nFor the duration of the seizure, a target's body writhes,\ntormenting her to the point of incapacitation. Victims\nsuffer a +2 difficulty penalty to all physical actions. The\nvictim also suffers one level of bashing damage every \nturn, as her body helplessly twists itself. At the Storyteller \ndiscretion, the effects of this power may even cause \ndeatth in extremely ill or wounded mortals.\nDamage may be reduced as normal (alhough levels from\narmor do not apply.)",
                },
                {
                    "name": "Body Failure",
                    "description": "Thaumaturges wielding this frightful power gain\ndevastating insights into the workings of the body, \nallowing a complete shutdown of its system. This \nsudden biological overload often proves fatal to \nmorttals and damaging to other supernatural beings. \nBody Failure has been used throughout the ages to \nafflict horrific ailments in inconspicuous ways that \nsuggest a stroke or heart attack.",
                    "system": "The thaumaturge no longer needs to touch\nher victim to strike out with this level of mastery of the\nPath. She may affect any target wihin her line of sight, \nbut she must keep visual contactt with the victim at all \ntimes to maintain this effect. A succesful activation of \nthis power grants effects similar to Seizure, except that \ndamage is lethal (and thus not soakable by mortals) due \nto complete mass tissue and organ failure. Additionally, \ntthe victim suffers a +2 difficulty penalty to all actions. \nThe subject may resist the effects of Body Failure via a\nStamina + Fortitude roll when the thaumaturge attempts\nto strike the target (difficulty equals the thaumaturge's\ncurrent Willpower). Each success the victim gains on this \nroll reduces the duration of Body Failure by one turn.",
                },
                {
                    "name": "Marionette",
                    "description": "The thaumaturge invoking Marionette gains such \nmastery over the body of others that she can magically \nseize control of another being and force her victim to act \naccording to her own whims. This control is not as fine as \nthe direct and personal command of the Dominate Power \nof Possession, but the thaumaturge's true body is not as \nvulnerable during the manipulation. Once established, \nthe Marionette victim is under the complete sway of the \nthaumaturge, forced to perform as the thaumaturge's \nmacabre pawn.",
                    "system": "The thaumaturge may affect any target within \nher line of sight, but must keep visual contact with \nthe victim at all times to maintain this effect. A subject \nmay resist the effects of Marionette on a Stamina + \nFortitude roll (difficulty equal to the thaumaturge's \ncurrent Willpower) when the thaumaturge attempts to \ntake control. Each success the victim gains on this roll \nreduces the duration of Marionette by one turn. Victims \nlacking Fortitude do not have the physical resistance to \ndefy this effect. \nFor the duration of this power, thte thaumaturge \ncan cause the victim to perform any physical action, \nusing the target's pools with a penalty of +2 difficulty \nto all rolls. The concentration this power requires also \nincreases the thaumaurge's own difficulties by two for all other personal actions undertaken while manipulating the victim. To extend the duration of this control, \nthe thaumaturge must make a second activation roll. \nMarionette does not rob the victim of her cognizance, \nonly physical control over her body. During this time \nof thaumaturge's mastery, the target remains aware \nthat some outside force is manipulating her physical actions, \nconscious that they are not her own. The victim may \nspend a point of Willpower to attempt to take a mental \nor social action, such as activating a Discipline or \nspeaking.",
                },
            ],
        },
        {
            "name": "Movement of the Mind",
            "reference": "V20 Core; PG 220",
            "type": "Thaumaturgy",
            "powers": [
                {
                    "name": "1 pound/ .5 kilogram",
                    "description": "This path gives the thaumaturge the ability to move\nobjects telekinetically through the mystic power of\nblood. At higher levels, even flight is possible (but be\ncareful who sees you…). Objects under the character’s\ncontrol may be manipulated as if she held them — they\nmay be lifted, spun, juggled, or even “thrown,” though\ncreating enough force to inflict actual damage requires\nmastery of at least the fourth level of this path. Some\ncasters skilled in this path even use it to guard their\nhavens, animating swords, axes, and firearms to ward\noff intruders. This path may frighten and disconcert\nonlookers.",
                    "system": "The number of successes indicates the duration of the caster’s control over the object (or subject). Each success allows one turn of manipulation, though the Kindred may attempt to maintain control after this time by making a new roll (she need not spend additional blood to maintain control). If the roll is successful,\ncontrol is maintained. If a thaumaturge loses or relaxes control over an object and later manipulates it again, her player must spend another blood point, as a new attempt is being made. Five or more successes on the initial roll means the vampire can control the object for duration of the scene. If this power is used to manipulate a living being, the subject may attempt to resist. In this case, the caster and the subject make opposed Willpower rolls each turn the control is \nOnce a Kindred reaches a rating of 3, she may levitate herself and “fly” at approximately running speed, no matter how much she weighs, though the weight restrictions apply if she manipulates other objects or subjects. Once a Kindred achieves 4, she may “throw” objects at a Strength equal to her level of mastery of\nthis path.",
                },
                {
                    "name": "20 pounds/10 kilograms",
                    "description": "This path gives the thaumaturge the ability to move\nobjects telekinetically through the mystic power of\nblood. At higher levels, even flight is possible (but be\ncareful who sees you…). Objects under the character’s\ncontrol may be manipulated as if she held them — they\nmay be lifted, spun, juggled, or even “thrown,” though\ncreating enough force to inflict actual damage requires\nmastery of at least the fourth level of this path. Some\ncasters skilled in this path even use it to guard their\nhavens, animating swords, axes, and firearms to ward\noff intruders. This path may frighten and disconcert\nonlookers.",
                    "system": "The number of successes indicates the duration of the caster’s control over the object (or subject). Each success allows one turn of manipulation, though the Kindred may attempt to maintain control after this time by making a new roll (she need not spend additional blood to maintain control). If the roll is successful,\ncontrol is maintained. If a thaumaturge loses or relaxes control over an object and later manipulates it again, her player must spend another blood point, as a new attempt is being made. Five or more successes on the initial roll means the vampire can control the object for duration of the scene. If this power is used to manipulate a living being, the subject may attempt to resist. In this case, the caster and the subject make opposed Willpower rolls each turn the control is \nOnce a Kindred reaches a rating of 3, she may levitate herself and “fly” at approximately running speed, no matter how much she weighs, though the weight restrictions apply if she manipulates other objects or subjects. Once a Kindred achieves 4, she may “throw” objects at a Strength equal to her level of mastery of\nthis path.",
                },
                {
                    "name": "200 pounds/100 kilograms",
                    "description": "This path gives the thaumaturge the ability to move\nobjects telekinetically through the mystic power of\nblood. At higher levels, even flight is possible (but be\ncareful who sees you…). Objects under the character’s\ncontrol may be manipulated as if she held them — they\nmay be lifted, spun, juggled, or even “thrown,” though\ncreating enough force to inflict actual damage requires\nmastery of at least the fourth level of this path. Some\ncasters skilled in this path even use it to guard their\nhavens, animating swords, axes, and firearms to ward\noff intruders. This path may frighten and disconcert\nonlookers.",
                    "system": "The number of successes indicates the duration of the caster’s control over the object (or subject). Each success allows one turn of manipulation, though the Kindred may attempt to maintain control after this time by making a new roll (she need not spend additional blood to maintain control). If the roll is successful,\ncontrol is maintained. If a thaumaturge loses or relaxes control over an object and later manipulates it again, her player must spend another blood point, as a new attempt is being made. Five or more successes on the initial roll means the vampire can control the object for duration of the scene. If this power is used to manipulate a living being, the subject may attempt to resist. In this case, the caster and the subject make opposed Willpower rolls each turn the control is \nOnce a Kindred reaches a rating of 3, she may levitate herself and “fly” at approximately running speed, no matter how much she weighs, though the weight restrictions apply if she manipulates other objects or subjects. Once a Kindred achieves 4, she may “throw” objects at a Strength equal to her level of mastery of\nthis path.",
                },
                {
                    "name": "500 pounds/250 kilograms",
                    "description": "This path gives the thaumaturge the ability to move\nobjects telekinetically through the mystic power of\nblood. At higher levels, even flight is possible (but be\ncareful who sees you…). Objects under the character’s\ncontrol may be manipulated as if she held them — they\nmay be lifted, spun, juggled, or even “thrown,” though\ncreating enough force to inflict actual damage requires\nmastery of at least the fourth level of this path. Some\ncasters skilled in this path even use it to guard their\nhavens, animating swords, axes, and firearms to ward\noff intruders. This path may frighten and disconcert\nonlookers.",
                    "system": "The number of successes indicates the duration of the caster’s control over the object (or subject). Each success allows one turn of manipulation, though the Kindred may attempt to maintain control after this time by making a new roll (she need not spend additional blood to maintain control). If the roll is successful,\ncontrol is maintained. If a thaumaturge loses or relaxes control over an object and later manipulates it again, her player must spend another blood point, as a new attempt is being made. Five or more successes on the initial roll means the vampire can control the object for duration of the scene. If this power is used to manipulate a living being, the subject may attempt to resist. In this case, the caster and the subject make opposed Willpower rolls each turn the control is \nOnce a Kindred reaches a rating of 3, she may levitate herself and “fly” at approximately running speed, no matter how much she weighs, though the weight restrictions apply if she manipulates other objects or subjects. Once a Kindred achieves 4, she may “throw” objects at a Strength equal to her level of mastery of\nthis path.",
                },
                {
                    "name": "1000 pounds/500 kilograms",
                    "description": "This path gives the thaumaturge the ability to move\nobjects telekinetically through the mystic power of\nblood. At higher levels, even flight is possible (but be\ncareful who sees you…). Objects under the character’s\ncontrol may be manipulated as if she held them — they\nmay be lifted, spun, juggled, or even “thrown,” though\ncreating enough force to inflict actual damage requires\nmastery of at least the fourth level of this path. Some\ncasters skilled in this path even use it to guard their\nhavens, animating swords, axes, and firearms to ward\noff intruders. This path may frighten and disconcert\nonlookers.",
                    "system": "The number of successes indicates the duration of the caster’s control over the object (or subject). Each success allows one turn of manipulation, though the Kindred may attempt to maintain control after this time by making a new roll (she need not spend additional blood to maintain control). If the roll is successful,\ncontrol is maintained. If a thaumaturge loses or relaxes control over an object and later manipulates it again, her player must spend another blood point, as a new attempt is being made. Five or more successes on the initial roll means the vampire can control the object for duration of the scene. If this power is used to manipulate a living being, the subject may attempt to resist. In this case, the caster and the subject make opposed Willpower rolls each turn the control is \nOnce a Kindred reaches a rating of 3, she may levitate herself and “fly” at approximately running speed, no matter how much she weighs, though the weight restrictions apply if she manipulates other objects or subjects. Once a Kindred achieves 4, she may “throw” objects at a Strength equal to her level of mastery of\nthis path.",
                },
            ],
        },
        {
            "name": "Neptune's Might",
            "reference": "V20 Core; PG 219",
            "type": "Thaumaturgy",
            "powers": [
                {
                    "name": "Eyes of the Sea",
                    "description": "The thaumaturge may peer into a body of water and\r\nview events that have transpired on, in, or around it\r\nfrom the water’s perspective. Some older practitioners\r\nof this art claim that the vampire communes with the\r\nspirits of the waters when using this power; younger\r\nKindred scoff at such claims.",
                    "system": "The number of successes rolled determines\r\nhow far into the past the character can look.\r\nSuccesses Result\r\n1 success One day\r\n2 successes One week\r\n3 successes One month\r\n4 successes One year\r\n5 successes 10 years\r\nThe Storyteller may require a Perception + Occult\r\nroll for the character to discern very small details in the\r\ntransmitted images. This power can only he used on\r\nstanding water; lakes and puddles qualify, but oceans,\r\nrivers, sewers, and wine glasses do not.",
                },
                {
                    "name": "Prison of Water",
                    "description": "The thaumaturge can command a sufficiently large\r\nquantity of water to animate itself and imprison a subject.\r\nThis power requires a significant amount of fluid\r\nto be fully effective, although even a few gallons can be\r\nused to shape chains of animated water.",
                    "system": "The number of successes scored on the roll\r\nis the number of successes the victim must score on a\r\nStrength roll (difficulty 8; Potence can add to this roll)\r\nto break free. A subject may be held in only one prison\r\nat a time, although the caster is free to invoke multiple\r\nuses of this power upon separate victims and may dissolve\r\nthese prisons at will. If a sufficient quantity of\r\nwater (at least a bathtub’s worth) is not present, the\r\ndifficulty of the Willpower roll to activate this power\r\nis raised by one.",
                },
                {
                    "name": "Blood to Water",
                    "description": "The thaumaturge has now attained enough power\r\nover water that she can transmute other liquids to this\r\nbasic element. The most commonly seen use of this\r\npower is as an assault; with but a touch, the victim’s\r\nblood transforms to water, weakening vampires and\r\nkilling mortals in moments.",
                    "system": "The character must touch her intended victim.\r\nThe player rolls Willpower normally. Each success\r\nconverts one of the victim’s blood points to water. One\r\nsuccess kills a mortal within minutes. Vampires who\r\nlose blood points to this power also suffer dice pool\r\npenalties as if they had received an equivalent number\r\nof health levels of injury. The water left in the target’s\r\nsystem by this attack evaporates out at a rate of one\r\nblood point’s worth per hour, but the lost blood does\r\nnot return.\r\nAt the Storyteller’s discretion, other liquids may be\r\nturned to water with this power (the difficulty for such\r\nan action is reduced by one unless the substance is particularly\r\ndangerous or magical in nature). The character\r\nmust still touch the substance or its container to use\r\nthis power.",
                },
                {
                    "name": "Flowing Wall",
                    "description": "Tales of vampires’ inability to cross running water\r\nmay have derived in part from garbled accounts of this\r\npower in action. The thaumaturge can animate water\r\nto an even greater degree than is possible with the use\r\nof Prison of Water, commanding it to rise up to form a\r\nbarrier impassable to almost any being.",
                    "system": "The character touches the surface of a\r\nstanding body of water; the player spends three Willpower\r\npoints and the normal required blood point and\r\nrolls normally. Successes are applied to both width and\r\nheight of the wall; each success “buys” 10 feet/three\r\nmeters in one dimension. The wall may be placed anywhere\r\nwithin the character’s line of sight, and must be\r\nformed in a straight line. The wall lasts until the next\r\nsunrise. It cannot be climbed, though it can be flown\r\nover. To pass through the barrier, any supernatural being\r\n(including beings trying to pass the wall on other\r\nlevels of existence, such as ghosts) must score at least\r\nthree successes on a single Willpower roll (difficulty\r\n9).",
                },
                {
                    "name": "Dehydrate",
                    "description": "At this level of mastery, the thaumaturge can directly\nattack living and unliving targets by removing the\nwater from their bodies. Victims killed by this power\nleave behind hideous mummified corpses. This power\ncan also be used for less aggressive purposes, such as\ndrying out wet clothes — or evaporating puddles to\nkeep other practitioners of this path from using them.",
                    "system": "This power can be used on any target in the\r\ncharacter’s line of sight. The player rolls normally; the\r\nvictim resists with a roll of Stamina + Fortitude (difficulty\r\n9). Each success gained by the caster translates\r\ninto one health level of lethal damage inflicted on the\r\nvictim. This injury cannot be soaked (the resistance\r\nroll replaces soak for this attack) but can be healed\r\nnormally. Vampires lose blood points instead of health\r\nlevels, though if a vampire has no blood points this attack\r\ninflicts health level loss as it would against a mortal.\r\nThe victim of this attack must also roll Courage\r\n(difficulty equal to the number of successes scored by\r\nthe caster + 3) to be able to act on the turn following\r\nthe attack; failure means he is overcome with agony\r\nand can do nothing.",
                },
            ],
        },
        {
            "name": "Path of Blood",
            "reference": "V20 Core; PG 212",
            "type": "Thaumaturgy",
            "powers": [
                {
                    "name": "A Taste for Blood",
                    "description": "This power was developed as a means of testing a foe’s might — an extremely important ability in the tumultuous early nights of Clan Tremere. By merely touching the blood of his subject, the caster may de-termine how much vitae remains in the subject and, if the subject is a vampire, how recently he has fed, his approximate Generation and, with three or more suc-cesses, whether he has ever committed diablerie.",
                    "system": "The number of successes achieved on the roll determines how much information the thauma-turge gleans and how accurate it is.",
                },
                {
                    "name": "Blood Rage",
                    "description": "This power allows a vampire to force another Kin-dred to expend blood against his will. The caster must touch her subject for this power to work, though only the lightest contact is necessary. A vampire affected by this power might feel a physical rush as the thau-maturge heightens his Physical Attributes, might find himself suddenly looking more human, or may even find himself on the brink of frenzy as his stores of vitae are mystically depleted.",
                    "system": "Each success forces the subject to spend one blood point immediately in the way the caster desires (which must go towards some logical expenditure the target vampire could make, such as increasing Physical Attributes or powering Disciplines). Note that blood points forcibly spent in this manner may exceed the normal “per turn” maximum indicated by the victim’s Generation. Each success gained also increases the subject’s difficulty to resist frenzy by one. The thauma-turge may not use Blood Rage on herself to circumvent generational limits.",
                },
                {
                    "name": "Blood of Potency",
                    "description": "The thaumaturge gains such control over his own blood that he may effectively “concentrate” it, mak-ing it more powerful for a short time. In effect, he may temporarily lower his own Generation with this power. This power may be used only once per night.",
                    "system": "One success on the Willpower roll allows the character to lower his Generation by one step for one hour. Each additional success grants the Kindred either one step down in Generation or one hour of ef-fect. Successes earned must be spent both to decrease the vampire’s Generation and to maintain the change (this power cannot be activated again until the origi-nal application wears off). If the vampire is diablerized while this power is in effect, it wears off immediately and the diablerist gains power appropriate to the cast-er’s actual Generation. Furthermore, any mortals Em-braced by the thaumaturge are born to the Generation appropriate to their sire’s original Generation (e.g., a Tenth-Generation Tremere who has reduced his ef-fective Generation to Eighth still produces Eleventh-Generation childer).Once the effect wears off, any blood over the char-acter’s blood pool maximum dilutes, leaving the char-acter at his regular blood pool maximum. Thus, if a Twelfth-Generation Tremere (maximum blood pool of 11) decreased his Generation to Ninth (maximum blood pool 14), ingested 14 blood points, and had this much vitae in his system when the power wore off, his blood pool would immediately drop to 11.",
                },
                {
                    "name": "Theft of Vitae",
                    "description": "A thaumaturge using this power siphons vitae from her subject. She need never come in contact with the subject — blood literally streams out in a physical tor-rent from the subject to the Kindred (though it is often mystically absorbed and need not enter through the mouth).",
                    "system": "The number of successes determines how many blood points the caster transfers from the sub-ject. The subject must be visible to the thaumaturge and within 50 feet (15 meters). Using this power pre-vents the caster from being blood-bound, but other-wise counts as if the vampire ingested the blood her-self. This power is spectacularly obvious, and Camarilla princes justifiably consider its public use a breach of the Masquerade.",
                },
                {
                    "name": "Cauldron of Blood",
                    "description": "A thaumaturge using this power boils her subject’s blood in his veins like water on a stove. The Kindred must touch her subject, and it is this contact that sim-mers the subject’s blood. This power is always fatal to mortals, and causes great damage to even the mightiest vampires.",
                    "system": "The number of successes gained determines how many blood points are brought to boil. The sub-ject suffers one health level of aggravated damage for each point boiled (individuals with Fortitude may soak this damage using only their Fortitude dice). A single success kills any mortal, though some ghouls with ac-cess to Fortitude are said to have survived after soaking all of the aggravated damage.",
                },
            ],
        },
        {
            "name": "Path of Conjuring",
            "reference": "V20 Core; PG 221",
            "type": "Thaumaturgy",
            "powers": [
                {
                    "name": "Summon the Simple Form",
                    "description": "At this level of mastery, the conjurer may create\nsimple, inanimate objects. The object cannot have any\nmoving parts and may not be made of multiple materials.\nFor example, the conjurer may summon a steel\nbaton, a lead pipe, a wooden stake, or a chunk of granite.",
                    "system": "Each turn the conjurer wishes to keep the\r\nobject in existence, another Willpower point must be\r\nspent or the object vanishes.",
                },
                {
                    "name": "Permanency",
                    "description": "At this level, the conjurer no longer needs to pay\r\nWillpower costs to keep an object in existence. The\r\nobject is permanent, though simple objects are still all\r\nthat may be created.",
                    "system": "The player must invest three blood points\r\nin an object to make it real.",
                },
                {
                    "name": "Magic of the Smith",
                    "description": "The Kindred may now conjure complex objects of\r\nmultiple components and with moving parts. For example,\r\nthe thaumaturge can create guns, bicycles,\r\nchainsaws, or cellphones.",
                    "system": "Objects created via Magic of the Smith are\r\nautomatically permanent and cost five blood points\r\nto conjure. Particularly complex items often require a\r\nKnowledge roll (Crafts, Science, Technology, etc.) in\r\naddition to the basic roll.",
                },
                {
                    "name": "Reverse Conjuration",
                    "description": "This power allows the conjurer to “banish” into nonexistence\r\nany object previously called forth via this\r\npath.",
                    "system": "This is an extended success roll. The conjurer\r\nmust accumulate as many successes as the original\r\ncaster received when creating the object in question.\r\nThis can also be used by the thaumaturge to banish\r\nobject she created herself with this Path.",
                },
                {
                    "name": "Power Over Life",
                    "description": "This power cannot create true life, though it can\r\nsummon forth impressive simulacra. Creatures (and\r\npeople) summoned with this power lack the free will\r\nto act on their own, mindlessly following the simple\r\ninstructions of their conjurer instead. People created\r\nin this way can be subject to the use of the Dominate\r\npower Possession (p. 155), if desired.",
                    "system": "The player spends 10 blood points. Imperfect\r\nand impermanent, creatures summoned via this\r\npath are too complex to exist for long. Within a week\r\nafter their conjuration, the simulacra vanish into insubstantiality.",
                },
            ],
        },
        {
            "name": "Path of Corruption",
            "reference": "V20 Core; PG 221",
            "type": "Thaumaturgy",
            "powers": [
                {
                    "name": "Contradict",
                    "description": "The vampire can interrupt a subject’s thought processes,\r\nforcing the victim to reverse his current course\r\nof action. An Archon may be caused to execute a prisoner\r\nshe was about to exonerate and release; a mortal\r\nlover might switch from gentle and caring to sadistic\r\nand demanding in the middle of an encounter. The results\r\nof Contradict are never precisely known to the\r\nthaumaturge in advance, but they always take the form\r\nof a more negative action than the subject had originally\r\nintended to perform.",
                    "system": "This power may be used on any subject\r\nwithin the character’s line of sight. The player rolls as\r\nper normal. The target rolls Perception + Subterfuge\r\n(difficulty equal to the number of successes scored by\r\nthe caster + 2). Two successes allow the subject to realize that she is being influenced by some outside source.\r\nThree successes let her pinpoint the source of the effect.\r\nFour successes give her a moment of hesitation,\r\nneither performing her original action nor its inverse,\r\nwhile five allow her to carry through with the original\r\naction.\r\nThe Storyteller dictates what the subject’s precise\r\nreaction to this power is. Contradict cannot be used in\r\ncombat or to affect other actions (at the Storyteller’s\r\ndiscretion) that are mainly physical and reflexive.",
                },
                {
                    "name": "Subvert",
                    "description": "This power follows the same principle as does Contradict,\r\nthe release of a subject’s dark, self-destructive\r\nside. However, Subvert’s effects are longer-lasting than\r\nthe momentary flare of Contradiction. Under the influence\r\nof this power, victims act on their own suppressed\r\ntemptations, pursuing agendas that their morals\r\nor self-control would forbid them to follow under\r\nnormal circumstances.",
                    "system": "This power requires the character to make\r\neye contact (see p. 152) with the intended victim. The\r\nplayer rolls normally. The target resists with a roll of\r\nPerception + Subterfuge (difficulty equal to the target’s\r\nManipulation + Subterfuge). If the thaumaturge scores\r\nmore successes, the victim becomes inclined to follow\r\na repressed, shameful desire for the length of time described\r\nbelow.\r\nSuccesses Result\r\n1 success Five minutes\r\n2 successes One hour\r\n3 successes One night\r\n4 successes Three nights\r\n5 successes One week\r\nThe Storyteller determines the precise desire or\r\nagenda that the victim follows. It should be in keeping\r\nwith the Psychological Flaws that she possesses or\r\nwith the negative aspects of her Nature (for example,\r\na Loner desiring isolation to such an extent that she\r\nbecomes violent if forced to attend a social function).\r\nThe subject should not become fixated on following\r\nthis new agenda at all times, but should occasionally be\r\nforced to spend a Willpower point if the opportunity to\r\nsuccumb arises and she wishes to resist the impulse.",
                },
                {
                    "name": "Dissociate",
                    "description": "“Divide and conquer” is a maxim that is well-understood\r\nby the Tremere, and Dissociate is a powerful tool\r\nwith which to divide the Clan’s enemies. This power\r\nis used to break the social ties of interpersonal relationships.\r\nEven the most passionate affair or the oldest\r\nfriendship can be cooled through use of Dissociate, and\r\nweaker personal ties can be destroyed altogether.",
                    "system": "The character must touch the target. The\r\nplayer rolls normally. The target resists with a Willpower\r\nroll (difficulty of the thaumaturge’s Manipulation\r\n+ Empathy). The victim loses three dice from\r\nall Social rolls for a period of time determined by the\r\nnumber of successes gained by the caster:\r\nSuccesses Result\r\n1 success Five minutes\r\n2 successes One hour\r\n3 successes One night\r\n4 successes Three nights\r\n5 successes One week\r\nThis penalty applies to all rolls that rely on Social\r\nAttributes, even those required for the use of Disciplines.\r\nIf this power is used on a character who has\r\nparticipated in the Vaulderie or a similar ritual, that\r\ncharacter’s Vinculum ratings are reduced by three for\r\nthe duration of Dissociate’s effect.\r\nDissociate’s primary effect falls under roleplaying\r\nrather than game mechanics. Victims of this power\r\nshould be played as withdrawn, suspicious, and emotionally\r\ndistant. The Storyteller should feel free to require\r\na Willpower point expenditure for a player who\r\ndoes not follow these guidelines.",
                },
                {
                    "name": "Addiction",
                    "description": "This power is a much stronger and more potentially\r\ndamaging form of Subvert. Addiction creates just that\r\nin the victim. By simply exposing the target to a particular\r\nsensation, substance, or action, the caster creates\r\na powerful psychological dependence. Many thaumaturges\r\nensure that their victims become addicted to\r\nsubstances or thrills that only the mystic can provide,\r\nthus creating both a source of income and potential\r\nblackmail material.",
                    "system": "The subject must encounter or be exposed\r\nto the sensation, substance, or action to which the\r\ncharacter wants to addict him. The thaumaturge then\r\ntouches his target. The player rolls normally; the victim\r\nresists with a Self-Control/Instinct roll (difficulty\r\nequal to the number of successes scored by the caster\r\n+ 3). Failure gives the subject an instant addiction to\r\nthat object.\r\nAn addicted character must get his fix at least once\r\na night. Every night that he goes without satisfying his\r\ndesire imposes a cumulative penalty of one die on all of\r\nhis dice pools (to a minimum pool of one die). The victim\r\nmust roll Self-Control/Instinct (difficulty 8) every\r\ntime he is confronted with the object of his addiction\r\nand wishes to keep from indulging. Addiction lasts for\r\na number of weeks equal to the thaumaturge’s Manipulation\r\nscore.\r\nAn individual may try to break the effects of Addiction.\r\nThis requires an extended Self-Control/Instinct\r\nroll (difficulty of the caster’s Manipulation + Subterfuge),\r\nwith one roll made per night. The addict must\r\naccumulate a number of successes equal to three times\r\nthe number of successes scored by the caster. The victim\r\nmay not indulge in his addiction over the time\r\nneeded to accumulate these successes. If he does so, all\r\naccumulated successes are lost and he must begin anew\r\non the next night. Note that the Self-Control/Instinct\r\ndice pool is reduced every night that the victim goes\r\nwithout feeding his addiction.",
                },
                {
                    "name": "Dependence",
                    "description": "Many former pawns of Clan Tremere claim to have\r\nfelt a strange sensation similar to depression when not\r\nin the presence of their masters. This is usually attributed\r\nto the blood bond, but is sometimes the result of\r\nthe vampire’s mastery of Dependence. The final power\r\nof the Path of Corruption enables the vampire to tie\r\nher victim’s soul to her own, engendering feelings of\r\nlethargy and helplessness when the victim is not in her\r\npresence or acting to further her desires.",
                    "system": "The character engages the target in conversation.\nThe player rolls normally. The victim rolls\nSelf-Control/Instinct (difficulty equals the number of\nsuccesses scored by the caster + 3). Failure means that\nthe victim’s psyche has been subtly bonded to that of\nthe thaumaturge for one night per success rolled by the\ncaster.\nA bonded victim is no less likely to attack his controller,\nand feels no particular positive emotions toward\nher. However, he is psychologically addicted to\nher presence, and suffers a one-die penalty to all rolls\nwhen he is not around her or performing tasks for her. Additionally, he is much less resistant to her commands,\r\nand his dice pools are halved when he attempts\r\nto resist her Dominate, Presence (or other mental or\r\nemotional control powers), or mundane Social rolls.\r\nFinally, he is unable to regain Willpower when he is\r\nnot in the thaumaturge’s presence.",
                },
            ],
        },
        {
            "name": "Path of Levinbolt",
            "reference": "Rites of the Blood; PG 141",
            "type": "Thaumaturgy",
            "powers": [
                {
                    "name": "Flicker",
                    "description": "Novice Thaumaturges learn to freely absorb power\naround them through electrical outlets, circuits, or \nbatteries. A user of this power can sense the current \nfeeding into a specific electrical system and then draw\nit to her, effectively turning it off.",
                    "system": "The thaumaturge simply glances at a target \npowered by electricity. Upon a succesful activation \nroll, she can shut down an electrical device for ten \nminutes per success on the activation roll. The spark \nof electricity arcs from the device directly into the \nthaumaturge in a frightening display of mystical power. \nThe source of this power is immediately known.",
                },
                {
                    "name": "Spark",
                    "description": "Novice thaumaturges can build up a tiny static \ncharge, enough to make a noticeable snap with a \ntouch. Such a discharge poses little threat to healthy \ntargets, though the energy can ruin delicae electronics \nor stun an unlucky victim.",
                    "system": "The thaumaturge simply touches a target \n(after the requisite blood expenditure and activation \nroll by the player) and releases the spark. The \nelectricity can snap from any part of the caster's body, \nso a thaumaturge might give an unpleasant surprise\nto someone touching her. The resulting electrical \ndischarge inflicts four dice of lethal damage to targets\n(difficulty 7 to soak), and short-circuits electronic \nequipment and devices not specifically grounded \nagainst lightning strike.",
                },
                {
                    "name": "Illuminate",
                    "description": 'Neonates sometimes derogatively refer to this effect\nas the "40-watt Tremere," right up until they\'ve felt its\nsting. The thaumaturge summons enough electricity \nto cover her hand or arm in arcing bolts. This power \ncan charge a battery, briefly run a small device, or \neven leave a nasty burn on a touched subject.',
                    "system": "Each success scored on the player's \nactivation roll translates to approximately one turn of \npower sufficient to run a handful of lights or a small \nelectrical device. Alternately, the thaumaturge can \nshock someone by touch, as with the Spark power, \nbut for eight dice of lethal electricity damage (difficulty \n8 to soak). \nThe current created with this power is not strong \nenough to force its way through less-than-ideal \nconductors, and thus simply inflicts electrical damage \nraw metals, woods, or other matter in the form of a burn \nand discoloration. The thaumaturge can alternately allow \nthe electricity to spark around her hand, eyes, or head; \nthis creates illumination about equal to a dim light bulb,\nand lowers the difficulty of any Intimidation rolls by 2.",
                },
                {
                    "name": "Thor's Fury",
                    "description": "The thaumaturge may strike her enemies from afar as \nthough she were a god. She may direct an arc of lightning \nfrom her body to nearby targets.",
                    "system": "The thaumaturge focuses her concentration \nupon her target and then directs hurled bolts via a \nPerception + Science roll (difficulty 6 plus the range \nin yard/meters, maximum 4 yards/meters). Each success \ninflicts a level of lethal damage (difficulty 8 to soak). The \nsource of this power is immediately known.",
                },
                {
                    "name": "Eye of the Storm",
                    "description": "The thaumaturge becomes a shifting, sparkling pillar of \nelectrical power. The energy channeled in the Eye of the \nStorm shields her body from virtually any direct harm.",
                    "system": "When a thaumaturge spends a Willpower point \nto invoke this power, she solidifies the stored electricity \ninside of her into a mystical barrier that completely \nsorrounds her. The caster becomes immune to any ranged \nattacks. Metal weapons such as swords inflict injury as \nnormal for the first sttrike, but are then melted from \ncontact with the barrier, and the wielder takes a level \nof lethal damage. Enemies that dare to touch the caster \nsuffer two points of aggravated damage (difficulty 8 to \nsoak.) Non-mettal weapons, such as wooden stakes, are not \naffected by Eye of the Storm. This power lasts for a single \nturn, with each additional success on the activattion roll \nextending tthis duration by one turn. Mental and social \nattacks may pass through this barrier.",
                },
            ],
        },
        {
            "name": "Path of Mars",
            "reference": "V20 Core; PG 224",
            "type": "Thaumaturgy",
            "powers": [
                {
                    "name": "War Cry",
                    "description": "A vampire on the attack can focus his will, making\nhim less susceptible to battle fear or the powers of the\nundead. The vampire shouts a primal scream to start the\neffect, though some thaumaturges have been known to\npaint their faces or cut themselves open instead.",
                    "system": "For the duration of one scene, the vampire\nadds one to his Courage Trait. Additionally, for the\npurposes of hostile effects, his Willpower is considered\nto be one higher (though this bonus applies only to the\nTrait itself, not the Willpower pool). A character may\nonly gain the benefits of War Cry once per scene.",
                },
                {
                    "name": "Strike True",
                    "description": "The vampire makes a single attack, guided by the\nunholy power of her Blood. This attack strikes its foe\ninfallibly.",
                    "system": "By invoking this power, the player need\nnot roll to see if the vampire’s attack hits — it does,\nautomatically. Only Melee or Brawl attacks may be\nmade in this manner. These attacks are considered to\nbe one-success attacks; they offer no additional damage\ndice. Also, they may be dodged, blocked, or parried\nnormally, and the defender needs only one success (as\nthe attacks’ number of success is assumed to be one).\nStrike True has no effect if attempted on multiple attacks\n(dice pool splits) in a single turn from one character.",
                },
                {
                    "name": "Wind Dance",
                    "description": "The thaumaturge invokes the power of the winds,\nmoving in a blur. She gains a preternatural edge in\navoiding her enemies’ blows, moving out of their way\nbefore the enemy has a chance to throw them.",
                    "system": "The player can dodge any number of attacks\nwith her full dice pool in a single turn. This advantage\napplies only to dodges — if the character wishes to attack\nand dodge, the player must still split her dice pool.\nThis power lasts for one scene.",
                },
                {
                    "name": "Fearless Heart",
                    "description": "The vampire temporarily augments his abilities as a\nwarrior. Through the mystical powers of blood magic,\nthe character becomes a potent fighting force.",
                    "system": "Fearless Heart grants the vampire an extra\npoint in each of the Physical Attributes (Strength,\nDexterity, and Stamina). These Traits may not exceed\ntheir generational maximums, though the player may\nuse blood points to push the character’s Traits even\nhigher. The effects last for one scene, and a character\nmay gain its benefits only once per scene. The vampire\nmust spend two hours in a calm and restful state following\nthe use of Fearless Heart, or lose a blood point\nevery 15 minutes until he rests.",
                },
                {
                    "name": "Comrades at Arms",
                    "description": "This ability extends the power of the previous abilities\nin the path. It allows any of the earlier effects to be\napplied to a group such as a pack or War Party.",
                    "system": "The player chooses one of the lower-level\npowers in the path, invoking it as normal. Afterward,\nhe touches another character and (if the roll for Comrades\nat Arms is successful) bestows the benefit on her\nas well. The same power may be delivered to any number\nof packmates, as long as the rolls for Comrades at\nArms are successful and the thaumaturge pays the appropriate\nblood costs.",
                },
            ],
        },
        {
            "name": "Path of Spirit Manipulation",
            "reference": "Rites of the Blood; PG 142-143",
            "type": "Thaumaturgy",
            "powers": [
                {
                    "name": "Hermetic Sightt",
                    "description": "The vampire can percieve the spirit world, either by \ngazing deeply into it or by seeing the presence of nearby \nspirits as a hazy overlay on the material world.",
                    "system": "Hermetic Sight allows the thaumaturge to \npercieve the spirit realm interlaid over the material \nworld for one hour. Each additional level of success on \nthe activation roll increases the duration of this power \nby an additional thirty minutes.",
                },
                {
                    "name": "Astral Cant",
                    "description": "The languages of the spirit world are infinitely \nvaried and mainly incomprehensible to mortal (and \nimmortal) minds. Astral Cant does not teach the \nthaumaturge the tongues of the spirits, but it does \nallow him to understand them as they speak to him \nand to reply in their own languages. The use of this \npower is not always necessary; many spirits speak \nhuman tongues, but choose to feign ignorance when \ndealing with vampires. Spirits are not affected by \nDominate, buttt may be manipulated by Presence. Some \nthaumaturges theorize that this is because spirits are \nnot actually sentient as a vampire would understand \nthe concept, but are manifestations based on the \nperception of those that are self-aware.",
                    "system": "Astral Cant allows the thaumaturge to speak to \nany spirit visible via Hermetic Sight for fifteen minutes. \nEach additional level of success on the activation roll \nincreases the duration of this power by an additional \nfifteen minutes to the duration.",
                },
                {
                    "name": "Voice of Command",
                    "description": "This is perhaps the most dangerous power in the \nSpirit Manipulation arsenal, for the consequences \nof failure can be particularly unpleasant. Voice of \nCommand allows the thaumaturge to issue orders to \na spirit, compelling it to heed her bidding whether or \nnot it desires to do so. \nSpirits compelled by this power are fully aware that \nthey are being forced into these actions, and may well \nseek revenge on their erstwhile masters at a later time. \nThaumaturges who issue commands above and beyond \nwhat their spirit servants are compelled to perform may \nfind themselves ignored or mocked. A trickster spirit \nmay agree to a situation to follow orders only to betray \nits master, leaving the thaumaturge in a situation of \npotentially fatal embarressment.",
                    "system": "The thaumaturge makes the normal opposed \nWillpower roll against the spirit. The target spirit \nresists with Willpower (difficulty of the thaumaturge's \nManipulation + Occult). The degree of success the \nthaumaturge attains determines the complexity and \nseverity of the command that she can issue.",
                },
                {
                    "name": "Entrap Ephemera",
                    "description": "This power allows a thaumaturge to bind a spirit into \na physical object. This can be done to imprison the \ntarget, but is more often performed to create a fettish - an \nartifact that grants mystical benefits powered by the spirit. \nFetishes created by this power are often unreliable and \nunderstandably displeased with their situation and will \ntake any opportunity to escape or thwartt their captors. \nLupines find it offensive f or vampires to possess a fetish, \nand often will frenzy simply at the sight of a vampire \nwielding one.",
                    "system": "The thaumaturge must first locate a vessel \nsymbolically aligned with the targeted spirit that will \neventually become the fetish. Then she must command \nthe targeted spirit to enter the vessel via an opposed \nWillpower roll. The target spirit resists with Willpower \n(difficulty equals the thaumaturge's Manipulation + \nOccult).\nShould the thaumaturge succeed, she can create a fetish \nof a power level based on the number of successes achieved \nover the spirit, up to a level five fetish. For example, if the \nthaumaturge wins the opposed Willpower roll against the \nspirit by three successes, she creates a level three fetish.\n\nCreating and maintaining a fetish is difficult; because of \nthis, the number of fetishes a thaumaturge may creatte is \nlimited by her Willpower. If the thaumaturge gives away \nsaid fetish, it still counts against her total available slots. \nShe may only create an additional fetish when one of \nher previous fetishes has been destroyed. \nA fetish grants a number of bonus dice to a specific \nskill comparable to the level of the fetish. For example, \na healing spirit trapped inside a scalpel would grant \nexttra dice (the level of the fetish) for any Medicine roll. \nThe Storyteller always has final authority on what sort \nof fetish can be made. \nA fettish is activatted by rolling the user's Willpower \n(difficulty equals the Fetish's power level + 3). A botch \non this roll destroys the physical component of the fetish \nand frees the spirit that was trapped within.",
                },
                {
                    "name": "Duality",
                    "description": "The thaumaturge can now fully interact with the spirit \nworld - a strange place that only sometimes resembles \nthe real world. While using this power, she exists on \nboth planes of existence at once. She is able to pick up \nobjects in the physical world and place them in the spirit \nworld and vice versa. Beings and landscape features in \nboth realms are solid to her, and she can engage in any \nmanner of interaction. She can even use Thaumaturgy \nand other Disciplines in either world. This is not without \nits dangers. With a single misstep, the vampire can find \nhimself trapped in the spirit realm with no way to return \nhome. Several incautious thaumaturges have starved into \ntorpor while trapped on the other side of the barrier that \nseperates the physical and spirit realms.",
                    "system": "The thaumaturge may interact with the spirit \nworld for fifteen minutes. Each additional level of \nsuccess on the activation roll increases the duration of \nthis power by an additional fifteen minutes. Duality can \nonly be enacted while the character begins the process in \nthe physical world. While in this state, the thaumaturge \nbecomes susceptible to attacks from both realms and \nsuffers a +1 difficulty to all Perception rolls. The \ncharacter is still considered to be in the physical world \nfor purposes of basic physics (and common sense).\nSpirits who have been previously angered will seek \nphysical revenge on unwary thaumaturges using this power. \nA botch on the roll to activate this power tears the \nvampire out of the physical world and traps him in the \nspirit realm. The way back to the physical realm, if there is \none, is left to the Storyteller's discretion, and may spark \nan entirely new story.",
                },
            ],
        },
        {
            "name": "Path of Technomancy",
            "reference": "V20 Core; PG 225",
            "type": "Thaumaturgy",
            "powers": [
                {
                    "name": "Analyze",
                    "description": "Mortals are constantly developing new innovations,\nand any vampire who would work Technomancy must\nbe able to understand that upon which he practices his\nmagic. The most basic power of this path allows the\nthaumaturge to project his perceptions into a device,\ngranting him a temporary understanding of its purpose,\nthe principles of its functioning, and its means of operation.\nThis does not grant permanent knowledge,\nonly a momentary flash of insight which fades within\nminutes.",
                    "system": "A character must touch the device in order\nto apply this power. The number of successes rolled determines\nhow well the character understands this particular\npiece of equipment. One success allows a basic\nknowledge (on/off and simple functions), while three\nsuccesses grant competence in operating the device,\nand five successes show the character the full range of\nthe device’s potential. The knowledge lasts for a number\nof minutes equal to the character’s Intelligence.\nThis power can also be used to understand a nonphysical\ntechnological innovation — generally a piece\nof software — at +2 difficulty. The character must\ntouch the computer on which the software is installed\n— simply holding the flash drive or CD-ROM is not\nenough. Software applied remotely to a device (such\nas through an app store) also cannot be analyzed until\nit is installed.",
                },
                {
                    "name": "Burnout",
                    "description": "It is usually easier to destroy than to create, and sensitive\nelectronics are no exception to this rule. Burnout\nis used to cause a device’s power supply (either internal\nor external) to surge, damaging or destroying the\ntarget. Burnout cannot be used to directly injure another\nindividual, although the sudden destruction of\na pacemaker or a car’s fuel injection control chip can\ncertainly create a health hazard.",
                    "system": "A character can use this power at a range\nof up to 10 times her Willpower in yards or meters,\nalthough a +1 difficulty is applied if she is not touching\nthe target item. The number of successes determines\nthe extent of the damage:\n\nSuccesses    Result\n1 success     Momentary interruption of operation (one turn), but no permanent damage.\n2 successes  Significant loss of function; +1 difficulty to use using the device for the rest of the scene.\n3 successes  The device breaks and is inoperable until repaired.\n4 successes  Even after repairs, the device’s capabilities are diminished (permanent +1 difficulty to use).\n5 successes  The equipment is a total write-off; completely unsalvageable.\n\nLarge enough systems, such as a server cluster or\na passenger aircraft, impose a +2 to +4 difficulty (at\nStoryteller discretion) to affect with this power. Additionally,\nsome systems, such as military and banking\nnetworks, may be protected against power surges and\nspikes, and thus possess one to five dice (Storyteller\ndiscretion again) to roll to resist this power. Each success\non this roll (difficulty 6) takes away one success\nfrom the Thaumaturgy roll.\nBurnout may be used to destroy electronic data storage,\nin which case three successes destroy all information\non the target item, and five erase it beyond any\nhope of non-magical recovery.",
                },
                {
                    "name": "Encrypt/Decrypt",
                    "description": "Electronic security is a paramount concern of governments\nand corporations alike. Those thaumaturges\nwho are techno-savvy enough to understand the issues\nat stake have become quite enamored of this power,\nwhich allows them to scramble a device’s controls mystically,\nmaking it inaccessible to anyone else. Encrypt/\nDecrypt also works on electronic media; a DVD under\nthe influence of this power displays just snow and static\nif played back without the owner’s approval. Some neonates\nhave taken to calling this power “DRM.”",
                    "system": "The character touches the device or data\ncontainer that he wishes to encrypt. The player rolls\nnormally. The number of successes scored is applied as\na difficulty modifier for anyone who attempts to use the\nprotected equipment or access the scrambled information\nwithout the assistance of the character. The caster\ncan dispel the effect at any time by touching the target\nitem and spending a point of Willpower.\n\nThis power may also be used to counter another\nthaumaturge’s use of Encrypt/Decrypt. The player rolls\nat +1 difficulty; each success negates one of the “owner’s.”\nThe effects of Encrypt/Decrypt last for a number of\nweeks equal to the character’s permanent Willpower\nrating.",
                },
                {
                    "name": "Remote Access",
                    "description": "With this power, a skilled thaumaturge can bypass\nthe need for physical contact to operate a device. This\nis not a form of telekinesis; the vampire does not manipulate\nthe item’s controls, but rather touches it directly\nwith the power of his mind.",
                    "system": "This power may be used on any electronic\ndevice within the character’s line of sight. The number\nof successes rolled is the maximum number of dice\nfrom any relevant Ability that the character may use\nwhile remotely controlling the device. (For instance, if\nFritz has Technology 5 and scores three successes while\nusing Remote Access on a keypad lock, he can only\napply three dots of his Technology rating to any rolls\nthat he makes through any use of the power.) Remote\nAccess lasts for a number of turns equal to the number\nof successes rolled, and can only be used on one item\nat a time.\nIf an item is destroyed while under the effects of Remote\nAccess, the character takes five dice of bashing\ndamage due to the shock of having his perceptions\nrudely shunted back into his own body.",
                },
                {
                    "name": "Telecommute",
                    "description": "A progressive derivation of Remote Access, Telecommute\nallows a thaumaturge to project her consciousness\ninto the Internet, sending her mind through\nnetwork connections as fast as they can transfer her.\nWhile immersed in the network, she can use any other\nTechnomancy power on the devices with which she\nmakes contact.",
                    "system": "The character touches any form of communications\ndevice: a cellphone, 3G-equipped netbook,\nWi-Fi tablet, or anything else that is connected directly\nor indirectly to the Internet. The player rolls normally\nand spends a Willpower point. Telecommute lasts for\nfive minutes per success rolled, and may be extended by\n10 minutes with the expenditure of another Willpower\npoint. The number of successes indicates the maximum\nrange that the character can project her consciousness\naway from her body:\n\nSuccesses    Result\n1 success     25 miles/40 kilometers\n2 successes  250 miles/400 kilometers\n3 successes  1000 miles/1500 kilometers\n4 successes  5000 miles/8000 kilometers\n5 successes  Anywhere in the world\n\nWhile in the network, the character can apply any\nother Path of Technomancy power to any device or\ndata with which she comes in contact. A loss of connection,\neither through the destruction of a part of the\nnetwork or simply a loss of cell signal, hurls her consciousness\nback to her body and inflicts eight dice of\nbashing damage.\nA character traveling through the Internet by means\nof this power can use her Path of Technomancy powers\nat a normal difficulty. Using any other abilities or powers\nwhile engaged thus is done at a +2 difficulty.",
                },
            ],
        },
        {
            "name": "Path of the Father's Vengeance",
            "reference": "V20 Core; PG 226",
            "type": "Thaumaturgy",
            "powers": [
                {
                    "name": "Zillah’s Litany",
                    "description": "Zillah, the wife of Caine, unknowingly drank from\nher husband and sire three times, thus becoming bond\ned to him. This power reveals existing blood bonds and\nVinculi to the thaumaturge.",
                    "system": "If the subject has any blood bonds or Vinculi\nto other vampires, this power reveals them to the\ncaster. Although the caster may not know the vampires\nin question, this power does reveal the names and\ngives rough psychic impressions of the individuals in\nquestion.",
                },
                {
                    "name": "The Crone’s Pride",
                    "description": "This power inflicts the curse of the crone, who bound\nCaine to her as he fled his wife’s spurning. Hideously\nugly, the crone had to resort to trickery to get others to\nhelp or serve her.",
                    "system": "This power reduces the target’s Appearance\nto zero. All Social rolls during this time generally fail,\nunless the character attempts to intimidate or browbeat\nthe subject. This power lasts for one night.",
                },
                {
                    "name": "Feast of Ashes",
                    "description": "Primarily used against wanton or excessive vampires,\nthis power temporarily removes a vampire’s dependency\non blood. While some would say this negates the\nCurse of Caine, it reduces the vampire to little more\nthan a wretched scavenger, as he must consume literal\nashes, though he gains little sustenance from them.",
                    "system": "The victim of this power can no longer consume\nblood, vomiting it up as he would mortal food or\ndrink. Instead, the victim can eat only ashes, and the\n“blood points” he gains from this may be used only to\nrise each night. Ashen “blood points” may not be used\nto power Disciplines, raise Attributes, or feed ghouls\n(though actual blood points in the character’s body at\nthe time this power is invoked may still be used for\nsuch). One blood point’s worth of ash is roughly one\npint or half-liter, and any ash will do — cigarette ash,\ncampfire leftovers, or vampire corpses destroyed by fire\nor sunlight. This power lasts for one week.",
                },
                {
                    "name": "Uriel’s Disfavor",
                    "description": "This power invokes the darkness of the Angel of\nDeath. All but the dimmest of light causes the subject\nexcruciating pain, and some artificial forms of bright\nlight may even damage the vampire. Uriel delivered\nGod’s curse on Caine, shielding him in the blackness\nof his wings.",
                    "system": "The presence of any light makes the subject\nuncomfortable, and bright light of any kind — flashlights, \nheadlights, etc. — inflict one health level of aggravated\ndamage on the character for every turn he remains\nunder its direct focus. Most vampires who suffer\nthis curse elect to sleep for the duration, hiding away in\nthe darkness of their havens until they can walk again\namong the living without pain. This power lasts for\none week.",
                },
                {
                    "name": "Valediction",
                    "description": "Many Sabbat rightfully fear this power, though very\nfew have ever seen it used. It levies a punishment for\nbreaking one of Caine’s greatest commandments —\nthe ban against diablerie. As most Sabbat attain their\npower and station through some measure of diablerie,\nthey must reconcile their beliefs with the admonitions\nof Caine, and this power engenders a great sense of humility.",
                    "system": "When this power takes effect, the subject\nimmediately reverts to her original Generation. This\nchange may entail losing points in certain Traits due to\ngenerational maximums. This power lasts for one week,\nafter which any Traits reduced to higher-Generation\nmaximums return to normal. It takes three turns to spea",
                },
            ],
        },
        {
            "name": "Path of the Focused Mind",
            "reference": "Rites of the Blood; PG 139",
            "type": "Thaumaturgy",
            "powers": [
                {
                    "name": "Readiness",
                    "description": "Using Readiness makes the caster able to gain a quicker \nunderstanding of a predicament. Enhanced lucidity \nenlightens the caster, allowing increased cleverness and \nbetter reactions to changing situations.",
                    "system": "This power is only usable on the thaumaturge \nherself. Every success on the activation roll adds on die \nto a special dice pool for the remainder of the turn. These \ndice may be used on any Wits-related rolls or actions that \nthe thaumaturge performs during this turn. Alternatively, \neach die removed from the dice pool adds one to the \ncaster's initiative rating.",
                },
                {
                    "name": "Centering",
                    "description": "By invoking this power, the thaumaturge causes a \nsudden, intense calmness in the subject by whispering \nsoothing words to her. While under this serenity, the \ntarget is better able to focus on tasks at hand, ignoring \ndistractions and annoyances, including grave bodily harm. \nThaumaturges in fear of frenzy often use this power on \nthemselves to stifle their own emotions and achieve a \nstate of tranquility.",
                    "system": "This power is usable on any one subject within \nearshot of the thaumaturge and lasts for one turn per \nsuccess on the activation roll. During this period, the \ntarget is unaffected by any power or effect (with the \nnotable exception of Elder disciplines) that reduces her \ndice pools. This includes wound penalties, situational \nmodifiers, and Disciplines. Modifications to difficulty \nnumbers still apply during this time, however. In addition, \ndue to the unnatural serenity that this power bestows, \nthe target receives two additional dice in all attempts to \navoid or break frenzy.",
                },
                {
                    "name": "One-Tracked Mind",
                    "description": 'By extending her powers to other individuals, the \nthaumaturge is able to fixate the subject on one action. \nThis single-mindedness of the target is so complete \nthat they ignore everything else that occurs around \nthem. Guards are easily distracted with this power, as \ntheir attention becomes fixated elsewhere, and research \nbecomes a dedicated, focused task. Use of this power \nis sometimes colloquially referred tto as "railroading \nsomeone."',
                    "system": "This power may affect anyone who can hear \nthe thaumaturge. Succesful invocation makes the target \nunable to split any dice pools for multiple actions and \nunable to change tactics after actions have been declared. \nAs a side benefit, the target reduces tthe difficulty of the \ndeclared action by one. Additional actions that the victim \ntakes (from Celeritty, for example) during the duration \nof this power must follow up upon their initial action, \nas they concentrate wholly upon this one idea. If the \ntarget wishes to attempt a different course of action, \nshe must spend a point of Willpower per scene (or per \nturn in combat.) The duration of One-Tracked Mind is \none scene, or one turn per success on the activation roll.",
                },
                {
                    "name": "Dual Thought",
                    "description": "The rigors of learning Thaumaturgy strengthen the \nmind and the will of a thaumaturge. As a result, those \nskilled with Thaumaturgy often have the ability to quickly \nassess a situation and calculate the options available to \nthem. At this level of mastery of the Focused Mind, \nthe thaumaturge is able to divide her attention to two \ncompletely seperate tasks without penalty or distraction. \nAs One-Tracked Mind forces the subject's attenttion into a \nsingle objecttive, Dual Thought expands the thaumaturge's \nconcentration to the point that focus upon two goals is possible.",
                    "system": "Succesful use of Dual Thought allow the \ncaster to take two actions without penalty during her turn. \n(Note that this power specifically lifts the restrictions of \nmultiple actions detailed in V20, P. 248). The extra action \ngranted by this power must be a mental action, whether \nit's the use of Disciplines such as the use of Auspex or \nThaumaturgy, or the contemplation of some problem.\nIf the character is using both actions to solve a problem, \nshe has two seperate dice pools to draw from. These two \nactions happen at the same time, as determined by the \ninitiative rating of the character. You may not use the \nextra action to re-cast Dual Thought.",
                },
                {
                    "name": "Perfect Clarity",
                    "description": "Perfect Clarity brings about a Zen-like moment of \nfocused insight for the thaumaturge as she gains a brief, \nperfect understanding of herself, the universe, and her \nplace within it. This lucidity protects the thaumaturge \nfrom influences both internal and external; even the\nBeast within is unable to rage forth. Thought and action \nbecome one as a complete serenity of the mind descends \nupon the thaumaturge.",
                    "system": "Perfect Clarity lasts for the duration of one \nscene, (or one turn plus an additional turn for every \nsuccess on the activation roll if used while in combat). \nFor this period, the thaumaturge has the difficulties of \nall actions reduced by two. The Kindred is immune to \nfrenzy and Rotschreck from all sources, even supernatural \ntriggers. Finally, any means to control or influence the \nthaumaturge suffer a +2 difficulty, including powers such \nas Presence, Dominate, and Dementation.",
                },
            ],
        },
        {
            "name": "Thaumaturgical Countermagic",
            "reference": "V20 Core; PG 228",
            "type": "Thaumaturgy",
            "powers": [
                {
                    "name": "Thaumaturgical Countermagic (1-5)",
                    "description": "This is less of a path than it is a separate Discipline, as the power to resist Thaumaturgy can be taught independently of Thaumaturgy, even to those Kindred who are incapable of mastering the simplest ritual. Though the techniques of Thaumaturgical Countermagic are\nnot officially taught outside Clan Tremere, unofficial methods are likely to exist. Any non-Tremere who displays the ability to resist Thaumaturgy quickly becomes the subject of potentially fatal scrutiny from the entirety of Clan Tremere.",
                    "system": "Thaumaturgical Countermagic is treated as a separate Discipline, although it uses the usual rules for Thaumaturgy (including experience costs and the fact that it is limited to only five levels). It cannot be taken as a character’s primary path, and a rating in it does not allow the character to perform rituals. The use of Thaumaturgical Countermagic is treated as a free action in combat and does not require a split dice pool. To oppose a Thaumaturgy power or ritual, a character must have a Thaumaturgical Countermagic rating equal to or greater than the rating of that power or ritual. The player spends a blood point and rolls the number of dice indicated by the character’s Thaumaturgical Countermagic rating (difficulty equal to the difficulty of the power in use). Each success cancels one of the opposing thaumaturge’s successes. Thaumaturgical Countermagic is only at full effectiveness when used against Thaumaturgy. It works with halved dice pools against Necromancy and other mystical Disciplines, and is completely ineffective against non-vampiric magics and powers.\nThaumaturgical Countermagic can be learned by characters who are unable to learn Thaumaturgy (e.g., those with the Merit Magic Resistance). Any non-Tremere character with a rating in this power automatically gains the Flaw Clan Enmity (Tremere), receiving no freebie points for it. This power cannot be taken during character creation and cannot be spontaneously developed. Whether the character has Thaumaturgy as an in-Clan power or not, it costs the same as any other non-Clan Discipline to learn.\nTwo dice of countermagic. The character can attempt to cancel only those powers and rituals that directly affect him, his garments, and objects on his person.",
                },
                {
                    "name": "Thaumaturgical Countermagic (1-5)",
                    "description": "This is less of a path than it is a separate Discipline, as the power to resist Thaumaturgy can be taught independently of Thaumaturgy, even to those Kindred who are incapable of mastering the simplest ritual. Though the techniques of Thaumaturgical Countermagic are\nnot officially taught outside Clan Tremere, unofficial methods are likely to exist. Any non-Tremere who displays the ability to resist Thaumaturgy quickly becomes the subject of potentially fatal scrutiny from the entirety of Clan Tremere.",
                    "system": "Thaumaturgical Countermagic is treated as a separate Discipline, although it uses the usual rules for Thaumaturgy (including experience costs and the fact that it is limited to only five levels). It cannot be taken as a character’s primary path, and a rating in it does not allow the character to perform rituals. The use of Thaumaturgical Countermagic is treated as a free action in combat and does not require a split dice pool. To oppose a Thaumaturgy power or ritual, a character must have a Thaumaturgical Countermagic rating equal to or greater than the rating of that power or ritual. The player spends a blood point and rolls the number of dice indicated by the character’s Thaumaturgical Countermagic rating (difficulty equal to the difficulty of the power in use). Each success cancels one of the opposing thaumaturge’s successes. Thaumaturgical Countermagic is only at full effectiveness when used against Thaumaturgy. It works with halved dice pools against Necromancy and other mystical Disciplines, and is completely ineffective against non-vampiric magics and powers.\nThaumaturgical Countermagic can be learned by characters who are unable to learn Thaumaturgy (e.g., those with the Merit Magic Resistance). Any non-Tremere character with a rating in this power automatically gains the Flaw Clan Enmity (Tremere), receiving no freebie points for it. This power cannot be taken during character creation and cannot be spontaneously developed. Whether the character has Thaumaturgy as an in-Clan power or not, it costs the same as any other non-Clan Discipline to learn.\nFour dice of countermagic. The character can attempt to cancel only those powers and rituals that directly affect him, his garments, and objects on his person.",
                },
                {
                    "name": "Thaumaturgical Countermagic (1-5)",
                    "description": "This is less of a path than it is a separate Discipline, as the power to resist Thaumaturgy can be taught independently of Thaumaturgy, even to those Kindred who are incapable of mastering the simplest ritual. Though the techniques of Thaumaturgical Countermagic are\nnot officially taught outside Clan Tremere, unofficial methods are likely to exist. Any non-Tremere who displays the ability to resist Thaumaturgy quickly becomes the subject of potentially fatal scrutiny from the entirety of Clan Tremere.",
                    "system": "Thaumaturgical Countermagic is treated as a separate Discipline, although it uses the usual rules for Thaumaturgy (including experience costs and the fact that it is limited to only five levels). It cannot be taken as a character’s primary path, and a rating in it does not allow the character to perform rituals. The use of Thaumaturgical Countermagic is treated as a free action in combat and does not require a split dice pool. To oppose a Thaumaturgy power or ritual, a character must have a Thaumaturgical Countermagic rating equal to or greater than the rating of that power or ritual. The player spends a blood point and rolls the number of dice indicated by the character’s Thaumaturgical Countermagic rating (difficulty equal to the difficulty of the power in use). Each success cancels one of the opposing thaumaturge’s successes. Thaumaturgical Countermagic is only at full effectiveness when used against Thaumaturgy. It works with halved dice pools against Necromancy and other mystical Disciplines, and is completely ineffective against non-vampiric magics and powers.\nThaumaturgical Countermagic can be learned by characters who are unable to learn Thaumaturgy (e.g., those with the Merit Magic Resistance). Any non-Tremere character with a rating in this power automatically gains the Flaw Clan Enmity (Tremere), receiving no freebie points for it. This power cannot be taken during character creation and cannot be spontaneously developed. Whether the character has Thaumaturgy as an in-Clan power or not, it costs the same as any other non-Clan Discipline to learn.\nSix dice of countermagic. The character can attempt to cancel a Thaumaturgy power that affects anyone or anything in physical contact with him.",
                },
                {
                    "name": "Thaumaturgical Countermagic (1-5)",
                    "description": "This is less of a path than it is a separate Discipline, as the power to resist Thaumaturgy can be taught independently of Thaumaturgy, even to those Kindred who are incapable of mastering the simplest ritual. Though the techniques of Thaumaturgical Countermagic are\nnot officially taught outside Clan Tremere, unofficial methods are likely to exist. Any non-Tremere who displays the ability to resist Thaumaturgy quickly becomes the subject of potentially fatal scrutiny from the entirety of Clan Tremere.",
                    "system": "Thaumaturgical Countermagic is treated as a separate Discipline, although it uses the usual rules for Thaumaturgy (including experience costs and the fact that it is limited to only five levels). It cannot be taken as a character’s primary path, and a rating in it does not allow the character to perform rituals. The use of Thaumaturgical Countermagic is treated as a free action in combat and does not require a split dice pool. To oppose a Thaumaturgy power or ritual, a character must have a Thaumaturgical Countermagic rating equal to or greater than the rating of that power or ritual. The player spends a blood point and rolls the number of dice indicated by the character’s Thaumaturgical Countermagic rating (difficulty equal to the difficulty of the power in use). Each success cancels one of the opposing thaumaturge’s successes. Thaumaturgical Countermagic is only at full effectiveness when used against Thaumaturgy. It works with halved dice pools against Necromancy and other mystical Disciplines, and is completely ineffective against non-vampiric magics and powers.\nThaumaturgical Countermagic can be learned by characters who are unable to learn Thaumaturgy (e.g., those with the Merit Magic Resistance). Any non-Tremere character with a rating in this power automatically gains the Flaw Clan Enmity (Tremere), receiving no freebie points for it. This power cannot be taken during character creation and cannot be spontaneously developed. Whether the character has Thaumaturgy as an in-Clan power or not, it costs the same as any other non-Clan Discipline to learn.\nEight dice of countermagic. The character can attempt to cancel a Thaumaturgy power that affects anyone or anything in physical contact with him.",
                },
                {
                    "name": "Thaumaturgical Countermagic (1-5)",
                    "description": "This is less of a path than it is a separate Discipline, as the power to resist Thaumaturgy can be taught independently of Thaumaturgy, even to those Kindred who are incapable of mastering the simplest ritual. Though the techniques of Thaumaturgical Countermagic are\nnot officially taught outside Clan Tremere, unofficial methods are likely to exist. Any non-Tremere who displays the ability to resist Thaumaturgy quickly becomes the subject of potentially fatal scrutiny from the entirety of Clan Tremere.",
                    "system": "Thaumaturgical Countermagic is treated as a separate Discipline, although it uses the usual rules for Thaumaturgy (including experience costs and the fact that it is limited to only five levels). It cannot be taken as a character’s primary path, and a rating in it does not allow the character to perform rituals. The use of Thaumaturgical Countermagic is treated as a free action in combat and does not require a split dice pool. To oppose a Thaumaturgy power or ritual, a character must have a Thaumaturgical Countermagic rating equal to or greater than the rating of that power or ritual. The player spends a blood point and rolls the number of dice indicated by the character’s Thaumaturgical Countermagic rating (difficulty equal to the difficulty of the power in use). Each success cancels one of the opposing thaumaturge’s successes. Thaumaturgical Countermagic is only at full effectiveness when used against Thaumaturgy. It works with halved dice pools against Necromancy and other mystical Disciplines, and is completely ineffective against non-vampiric magics and powers.\nThaumaturgical Countermagic can be learned by characters who are unable to learn Thaumaturgy (e.g., those with the Merit Magic Resistance). Any non-Tremere character with a rating in this power automatically gains the Flaw Clan Enmity (Tremere), receiving no freebie points for it. This power cannot be taken during character creation and cannot be spontaneously developed. Whether the character has Thaumaturgy as an in-Clan power or not, it costs the same as any other non-Clan Discipline to learn.\nTen dice of countermagic. The character can now attempt to cancel a power or ritual that targets anything within a radius equal to his Willpower in yards or meters, or one that is being used or performed within that same radius.",
                },
            ],
        },
        {
            "name": "Weather Control",
            "reference": "V20 Core; PG 228",
            "type": "Thaumaturgy",
            "powers": [
                {
                    "name": "Fog & Minor Temperature Change",
                    "description": "Command over the weather has long been a staple\npower of wizards both mortal and immortal, and this\npath is said to predate the Tremere by millennia. The\nproliferation of usage of this path outside the Clan tends\nto confirm this theory; Weather Control is quite common\noutside the Tremere, and even outside the Camarilla.\nLower levels of this path allow subtle manipulations,\nwhile higher stages of mastery allow a vampire to\ncall up raging storms. The area affected by this power is\nusually rather small, no more than three or four miles\n(five to six kilometers) in diameter, and the changes\nthe power wreaks are not always immediate.",
                    "system": "The number of successes rolled indicates how long it takes the weather magic to take effect. One success indicates an entire day may pass before the weather changes to the thaumaturge’s liking, while a roll with five successes brings an almost instant effect. The difficulty of the Willpower roll necessary to invoke\nthis power may change depending on the current local weather conditions and the weather the character is attempting to create. The Storyteller should impose a bonus (-1 or -2 difficulty) for relatively minor shifts, such as clearing away a light drizzle or calling lightning when a severe thunderstorm is already raging.\nConversely, a penalty (+1 or +2 difficulty) should be applied when the desired change is at odds with the current conditions, such as summoning the same light drizzle in the middle of the Sahara Desert or calling down lightning from a cloudless sky. If the character tries to strike a specific target with lightning, the player must roll Perception + Occult (difficulty 6 if the target is standing in open terrain, 8 if he is under shelter, or 10 if he is inside but near a window) in addition to the base roll to use Thaumaturgy. \nOtherwise the bolt goes astray, with the relative degree of failure of the roll determining where exactly the lightning strikes. Effects of the power default to the maximum area available unless the caster states that he’s attempting to affect a smaller area. At Storyteller discretion, an additional Willpower roll (difficulty 6) may be required to keep the change in the weather under control. Weather Control is not the sort of power that lends itself well to indoor application. While certain of the path’s uses (changes of temperature, high winds, and possibly even fog) do make a certain amount of sense in interior settings, others (precipitation of any sort, lightning) don’t. The difficulty for all rolls to use Weather Control indoors is at +2, and the Storyteller should feel free to disallow any proposed uses that don’t make sense.\nIndividual power descriptions are not provided for this path, as the general principle is fairly consistent. Instead, the strongest weather phenomenon possible at\neach level is listed. \n• Fog: Vision is slightly impaired and sounds are muffled; a +1 difficulty is imposed on all Perception rolls that involve sight and hearing, and the effective range of all ranged attacks are halved. Light breeze: A +1 difficulty is\nimposed on all Perception rolls that involve smell.\nMinor temperature change: It is possible to raise or lower the local temperature by up to 10 degrees Fahrenheit or 5 degrees Celsius.\n•• Rain or snow: As Fog, but Perception rolls are impaired to a much greater extent; the difficulty modifier for all such rolls rises to +2. In addition, the difficulty on all Drive rolls increases by two.\n••• High Winds: The wind speed rises to around 30 miles per hour or 50 kilometers per hour, with gusts of up to twice that. Ranged attacks are much more difficult: + 1 to firearm attacks and +2 to thrown weapons and archery. In addition, during fierce gusts, Dexterity rolls (difficulty 6) may be required to keep characters from being knocked over by the winds. When gale-force winds are in effect, papers go flying, objects get picked up by the winds and hurled with abandon, and other suitably cinematic effects are likely. \nModerate temperature change: The local temperature can be raised or lowered by up to 20 degrees Fahrenheit or 10 degrees Celsius.\n•••• Storm: This has the effects of both Rain and High Winds.\n••••• Lightning Strike: This attack inflicts 10 dice of lethal damage. Body armor does not add to the target’s dice pool to soak this attack.",
                },
                {
                    "name": "Rain or Snow",
                    "description": "Command over the weather has long been a staple\npower of wizards both mortal and immortal, and this\npath is said to predate the Tremere by millennia. The\nproliferation of usage of this path outside the Clan tends\nto confirm this theory; Weather Control is quite common\noutside the Tremere, and even outside the Camarilla.\nLower levels of this path allow subtle manipulations,\nwhile higher stages of mastery allow a vampire to\ncall up raging storms. The area affected by this power is\nusually rather small, no more than three or four miles\n(five to six kilometers) in diameter, and the changes\nthe power wreaks are not always immediate.",
                    "system": "The number of successes rolled indicates how long it takes the weather magic to take effect. One success indicates an entire day may pass before the weather changes to the thaumaturge’s liking, while a roll with five successes brings an almost instant effect. The difficulty of the Willpower roll necessary to invoke\nthis power may change depending on the current local weather conditions and the weather the character is attempting to create. The Storyteller should impose a bonus (-1 or -2 difficulty) for relatively minor shifts, such as clearing away a light drizzle or calling lightning when a severe thunderstorm is already raging.\nConversely, a penalty (+1 or +2 difficulty) should be applied when the desired change is at odds with the current conditions, such as summoning the same light drizzle in the middle of the Sahara Desert or calling down lightning from a cloudless sky. If the character tries to strike a specific target with lightning, the player must roll Perception + Occult (difficulty 6 if the target is standing in open terrain, 8 if he is under shelter, or 10 if he is inside but near a window) in addition to the base roll to use Thaumaturgy. \nOtherwise the bolt goes astray, with the relative degree of failure of the roll determining where exactly the lightning strikes. Effects of the power default to the maximum area available unless the caster states that he’s attempting to affect a smaller area. At Storyteller discretion, an additional Willpower roll (difficulty 6) may be required to keep the change in the weather under control. Weather Control is not the sort of power that lends itself well to indoor application. While certain of the path’s uses (changes of temperature, high winds, and possibly even fog) do make a certain amount of sense in interior settings, others (precipitation of any sort, lightning) don’t. The difficulty for all rolls to use Weather Control indoors is at +2, and the Storyteller should feel free to disallow any proposed uses that don’t make sense.\nIndividual power descriptions are not provided for this path, as the general principle is fairly consistent. Instead, the strongest weather phenomenon possible at\neach level is listed. \n• Fog: Vision is slightly impaired and sounds are muffled; a +1 difficulty is imposed on all Perception rolls that involve sight and hearing, and the effective range of all ranged attacks are halved. Light breeze: A +1 difficulty is\nimposed on all Perception rolls that involve smell.\nMinor temperature change: It is possible to raise or lower the local temperature by up to 10 degrees Fahrenheit or 5 degrees Celsius.\n•• Rain or snow: As Fog, but Perception rolls are impaired to a much greater extent; the difficulty modifier for all such rolls rises to +2. In addition, the difficulty on all Drive rolls increases by two.\n••• High Winds: The wind speed rises to around 30 miles per hour or 50 kilometers per hour, with gusts of up to twice that. Ranged attacks are much more difficult: + 1 to firearm attacks and +2 to thrown weapons and archery. In addition, during fierce gusts, Dexterity rolls (difficulty 6) may be required to keep characters from being knocked over by the winds. When gale-force winds are in effect, papers go flying, objects get picked up by the winds and hurled with abandon, and other suitably cinematic effects are likely. \nModerate temperature change: The local temperature can be raised or lowered by up to 20 degrees Fahrenheit or 10 degrees Celsius.\n•••• Storm: This has the effects of both Rain and High Winds.\n••••• Lightning Strike: This attack inflicts 10 dice of lethal damage. Body armor does not add to the target’s dice pool to soak this attack.",
                },
                {
                    "name": "High Winds & Moderate Temperature Change",
                    "description": "Command over the weather has long been a staple\npower of wizards both mortal and immortal, and this\npath is said to predate the Tremere by millennia. The\nproliferation of usage of this path outside the Clan tends\nto confirm this theory; Weather Control is quite common\noutside the Tremere, and even outside the Camarilla.\nLower levels of this path allow subtle manipulations,\nwhile higher stages of mastery allow a vampire to\ncall up raging storms. The area affected by this power is\nusually rather small, no more than three or four miles\n(five to six kilometers) in diameter, and the changes\nthe power wreaks are not always immediate.",
                    "system": "The number of successes rolled indicates how long it takes the weather magic to take effect. One success indicates an entire day may pass before the weather changes to the thaumaturge’s liking, while a roll with five successes brings an almost instant effect. The difficulty of the Willpower roll necessary to invoke\nthis power may change depending on the current local weather conditions and the weather the character is attempting to create. The Storyteller should impose a bonus (-1 or -2 difficulty) for relatively minor shifts, such as clearing away a light drizzle or calling lightning when a severe thunderstorm is already raging.\nConversely, a penalty (+1 or +2 difficulty) should be applied when the desired change is at odds with the current conditions, such as summoning the same light drizzle in the middle of the Sahara Desert or calling down lightning from a cloudless sky. If the character tries to strike a specific target with lightning, the player must roll Perception + Occult (difficulty 6 if the target is standing in open terrain, 8 if he is under shelter, or 10 if he is inside but near a window) in addition to the base roll to use Thaumaturgy. \nOtherwise the bolt goes astray, with the relative degree of failure of the roll determining where exactly the lightning strikes. Effects of the power default to the maximum area available unless the caster states that he’s attempting to affect a smaller area. At Storyteller discretion, an additional Willpower roll (difficulty 6) may be required to keep the change in the weather under control. Weather Control is not the sort of power that lends itself well to indoor application. While certain of the path’s uses (changes of temperature, high winds, and possibly even fog) do make a certain amount of sense in interior settings, others (precipitation of any sort, lightning) don’t. The difficulty for all rolls to use Weather Control indoors is at +2, and the Storyteller should feel free to disallow any proposed uses that don’t make sense.\nIndividual power descriptions are not provided for this path, as the general principle is fairly consistent. Instead, the strongest weather phenomenon possible at\neach level is listed. \n• Fog: Vision is slightly impaired and sounds are muffled; a +1 difficulty is imposed on all Perception rolls that involve sight and hearing, and the effective range of all ranged attacks are halved. Light breeze: A +1 difficulty is\nimposed on all Perception rolls that involve smell.\nMinor temperature change: It is possible to raise or lower the local temperature by up to 10 degrees Fahrenheit or 5 degrees Celsius.\n•• Rain or snow: As Fog, but Perception rolls are impaired to a much greater extent; the difficulty modifier for all such rolls rises to +2. In addition, the difficulty on all Drive rolls increases by two.\n••• High Winds: The wind speed rises to around 30 miles per hour or 50 kilometers per hour, with gusts of up to twice that. Ranged attacks are much more difficult: + 1 to firearm attacks and +2 to thrown weapons and archery. In addition, during fierce gusts, Dexterity rolls (difficulty 6) may be required to keep characters from being knocked over by the winds. When gale-force winds are in effect, papers go flying, objects get picked up by the winds and hurled with abandon, and other suitably cinematic effects are likely. \nModerate temperature change: The local temperature can be raised or lowered by up to 20 degrees Fahrenheit or 10 degrees Celsius.\n•••• Storm: This has the effects of both Rain and High Winds.\n••••• Lightning Strike: This attack inflicts 10 dice of lethal damage. Body armor does not add to the target’s dice pool to soak this attack.",
                },
                {
                    "name": "Storm",
                    "description": "Command over the weather has long been a staple\npower of wizards both mortal and immortal, and this\npath is said to predate the Tremere by millennia. The\nproliferation of usage of this path outside the Clan tends\nto confirm this theory; Weather Control is quite common\noutside the Tremere, and even outside the Camarilla.\nLower levels of this path allow subtle manipulations,\nwhile higher stages of mastery allow a vampire to\ncall up raging storms. The area affected by this power is\nusually rather small, no more than three or four miles\n(five to six kilometers) in diameter, and the changes\nthe power wreaks are not always immediate.",
                    "system": "The number of successes rolled indicates how long it takes the weather magic to take effect. One success indicates an entire day may pass before the weather changes to the thaumaturge’s liking, while a roll with five successes brings an almost instant effect. The difficulty of the Willpower roll necessary to invoke\nthis power may change depending on the current local weather conditions and the weather the character is attempting to create. The Storyteller should impose a bonus (-1 or -2 difficulty) for relatively minor shifts, such as clearing away a light drizzle or calling lightning when a severe thunderstorm is already raging.\nConversely, a penalty (+1 or +2 difficulty) should be applied when the desired change is at odds with the current conditions, such as summoning the same light drizzle in the middle of the Sahara Desert or calling down lightning from a cloudless sky. If the character tries to strike a specific target with lightning, the player must roll Perception + Occult (difficulty 6 if the target is standing in open terrain, 8 if he is under shelter, or 10 if he is inside but near a window) in addition to the base roll to use Thaumaturgy. \nOtherwise the bolt goes astray, with the relative degree of failure of the roll determining where exactly the lightning strikes. Effects of the power default to the maximum area available unless the caster states that he’s attempting to affect a smaller area. At Storyteller discretion, an additional Willpower roll (difficulty 6) may be required to keep the change in the weather under control. Weather Control is not the sort of power that lends itself well to indoor application. While certain of the path’s uses (changes of temperature, high winds, and possibly even fog) do make a certain amount of sense in interior settings, others (precipitation of any sort, lightning) don’t. The difficulty for all rolls to use Weather Control indoors is at +2, and the Storyteller should feel free to disallow any proposed uses that don’t make sense.\nIndividual power descriptions are not provided for this path, as the general principle is fairly consistent. Instead, the strongest weather phenomenon possible at\neach level is listed. \n• Fog: Vision is slightly impaired and sounds are muffled; a +1 difficulty is imposed on all Perception rolls that involve sight and hearing, and the effective range of all ranged attacks are halved. Light breeze: A +1 difficulty is\nimposed on all Perception rolls that involve smell.\nMinor temperature change: It is possible to raise or lower the local temperature by up to 10 degrees Fahrenheit or 5 degrees Celsius.\n•• Rain or snow: As Fog, but Perception rolls are impaired to a much greater extent; the difficulty modifier for all such rolls rises to +2. In addition, the difficulty on all Drive rolls increases by two.\n••• High Winds: The wind speed rises to around 30 miles per hour or 50 kilometers per hour, with gusts of up to twice that. Ranged attacks are much more difficult: + 1 to firearm attacks and +2 to thrown weapons and archery. In addition, during fierce gusts, Dexterity rolls (difficulty 6) may be required to keep characters from being knocked over by the winds. When gale-force winds are in effect, papers go flying, objects get picked up by the winds and hurled with abandon, and other suitably cinematic effects are likely. \nModerate temperature change: The local temperature can be raised or lowered by up to 20 degrees Fahrenheit or 10 degrees Celsius.\n•••• Storm: This has the effects of both Rain and High Winds.\n••••• Lightning Strike: This attack inflicts 10 dice of lethal damage. Body armor does not add to the target’s dice pool to soak this attack.",
                },
                {
                    "name": "Lightning Strike",
                    "description": "Command over the weather has long been a staple\npower of wizards both mortal and immortal, and this\npath is said to predate the Tremere by millennia. The\nproliferation of usage of this path outside the Clan tends\nto confirm this theory; Weather Control is quite common\noutside the Tremere, and even outside the Camarilla.\nLower levels of this path allow subtle manipulations,\nwhile higher stages of mastery allow a vampire to\ncall up raging storms. The area affected by this power is\nusually rather small, no more than three or four miles\n(five to six kilometers) in diameter, and the changes\nthe power wreaks are not always immediate.",
                    "system": "The number of successes rolled indicates how long it takes the weather magic to take effect. One success indicates an entire day may pass before the weather changes to the thaumaturge’s liking, while a roll with five successes brings an almost instant effect. The difficulty of the Willpower roll necessary to invoke\nthis power may change depending on the current local weather conditions and the weather the character is attempting to create. The Storyteller should impose a bonus (-1 or -2 difficulty) for relatively minor shifts, such as clearing away a light drizzle or calling lightning when a severe thunderstorm is already raging.\nConversely, a penalty (+1 or +2 difficulty) should be applied when the desired change is at odds with the current conditions, such as summoning the same light drizzle in the middle of the Sahara Desert or calling down lightning from a cloudless sky. If the character tries to strike a specific target with lightning, the player must roll Perception + Occult (difficulty 6 if the target is standing in open terrain, 8 if he is under shelter, or 10 if he is inside but near a window) in addition to the base roll to use Thaumaturgy. \nOtherwise the bolt goes astray, with the relative degree of failure of the roll determining where exactly the lightning strikes. Effects of the power default to the maximum area available unless the caster states that he’s attempting to affect a smaller area. At Storyteller discretion, an additional Willpower roll (difficulty 6) may be required to keep the change in the weather under control. Weather Control is not the sort of power that lends itself well to indoor application. While certain of the path’s uses (changes of temperature, high winds, and possibly even fog) do make a certain amount of sense in interior settings, others (precipitation of any sort, lightning) don’t. The difficulty for all rolls to use Weather Control indoors is at +2, and the Storyteller should feel free to disallow any proposed uses that don’t make sense.\nIndividual power descriptions are not provided for this path, as the general principle is fairly consistent. Instead, the strongest weather phenomenon possible at\neach level is listed. \n• Fog: Vision is slightly impaired and sounds are muffled; a +1 difficulty is imposed on all Perception rolls that involve sight and hearing, and the effective range of all ranged attacks are halved. Light breeze: A +1 difficulty is\nimposed on all Perception rolls that involve smell.\nMinor temperature change: It is possible to raise or lower the local temperature by up to 10 degrees Fahrenheit or 5 degrees Celsius.\n•• Rain or snow: As Fog, but Perception rolls are impaired to a much greater extent; the difficulty modifier for all such rolls rises to +2. In addition, the difficulty on all Drive rolls increases by two.\n••• High Winds: The wind speed rises to around 30 miles per hour or 50 kilometers per hour, with gusts of up to twice that. Ranged attacks are much more difficult: + 1 to firearm attacks and +2 to thrown weapons and archery. In addition, during fierce gusts, Dexterity rolls (difficulty 6) may be required to keep characters from being knocked over by the winds. When gale-force winds are in effect, papers go flying, objects get picked up by the winds and hurled with abandon, and other suitably cinematic effects are likely. \nModerate temperature change: The local temperature can be raised or lowered by up to 20 degrees Fahrenheit or 10 degrees Celsius.\n•••• Storm: This has the effects of both Rain and High Winds.\n••••• Lightning Strike: This attack inflicts 10 dice of lethal damage. Body armor does not add to the target’s dice pool to soak this attack.",
                },
            ],
        },
        {
            "name": "Movement of the Mind (Anarch, Hacktivist)",
            "reference": "Rites of the Blood; PG 58 (V20 Core; PG 220)",
            "type": "Thaumaturgy (Anarch, Hacktivist)",
            "powers": [
                {
                    "name": "1 pound/ .5 kilogram",
                    "description": "This path gives the thaumaturge the ability to move\nobjects telekinetically through the mystic power of\nblood. At higher levels, even flight is possible (but be\ncareful who sees you…). Objects under the character’s\ncontrol may be manipulated as if she held them — they\nmay be lifted, spun, juggled, or even “thrown,” though\ncreating enough force to inflict actual damage requires\nmastery of at least the fourth level of this path. Some\ncasters skilled in this path even use it to guard their\nhavens, animating swords, axes, and firearms to ward\noff intruders. This path may frighten and disconcert\nonlookers.",
                    "system": "The number of successes indicates the duration of the caster’s control over the object (or subject). Each success allows one turn of manipulation, though the Kindred may attempt to maintain control after this time by making a new roll (she need not spend additional blood to maintain control). If the roll is successful,\ncontrol is maintained. If a thaumaturge loses or relaxes control over an object and later manipulates it again, her player must spend another blood point, as a new attempt is being made. Five or more successes on the initial roll means the vampire can control the object for duration of the scene. If this power is used to manipulate a living being, the subject may attempt to resist. In this case, the caster and the subject make opposed Willpower rolls each turn the control is \nOnce a Kindred reaches a rating of 3, she may levitate herself and “fly” at approximately running speed, no matter how much she weighs, though the weight restrictions apply if she manipulates other objects or subjects. Once a Kindred achieves 4, she may “throw” objects at a Strength equal to her level of mastery of\nthis path.",
                },
                {
                    "name": "20 pounds/10 kilograms",
                    "description": "This path gives the thaumaturge the ability to move\nobjects telekinetically through the mystic power of\nblood. At higher levels, even flight is possible (but be\ncareful who sees you…). Objects under the character’s\ncontrol may be manipulated as if she held them — they\nmay be lifted, spun, juggled, or even “thrown,” though\ncreating enough force to inflict actual damage requires\nmastery of at least the fourth level of this path. Some\ncasters skilled in this path even use it to guard their\nhavens, animating swords, axes, and firearms to ward\noff intruders. This path may frighten and disconcert\nonlookers.",
                    "system": "The number of successes indicates the duration of the caster’s control over the object (or subject). Each success allows one turn of manipulation, though the Kindred may attempt to maintain control after this time by making a new roll (she need not spend additional blood to maintain control). If the roll is successful,\ncontrol is maintained. If a thaumaturge loses or relaxes control over an object and later manipulates it again, her player must spend another blood point, as a new attempt is being made. Five or more successes on the initial roll means the vampire can control the object for duration of the scene. If this power is used to manipulate a living being, the subject may attempt to resist. In this case, the caster and the subject make opposed Willpower rolls each turn the control is \nOnce a Kindred reaches a rating of 3, she may levitate herself and “fly” at approximately running speed, no matter how much she weighs, though the weight restrictions apply if she manipulates other objects or subjects. Once a Kindred achieves 4, she may “throw” objects at a Strength equal to her level of mastery of\nthis path.",
                },
                {
                    "name": "200 pounds/100 kilograms",
                    "description": "This path gives the thaumaturge the ability to move\nobjects telekinetically through the mystic power of\nblood. At higher levels, even flight is possible (but be\ncareful who sees you…). Objects under the character’s\ncontrol may be manipulated as if she held them — they\nmay be lifted, spun, juggled, or even “thrown,” though\ncreating enough force to inflict actual damage requires\nmastery of at least the fourth level of this path. Some\ncasters skilled in this path even use it to guard their\nhavens, animating swords, axes, and firearms to ward\noff intruders. This path may frighten and disconcert\nonlookers.",
                    "system": "The number of successes indicates the duration of the caster’s control over the object (or subject). Each success allows one turn of manipulation, though the Kindred may attempt to maintain control after this time by making a new roll (she need not spend additional blood to maintain control). If the roll is successful,\ncontrol is maintained. If a thaumaturge loses or relaxes control over an object and later manipulates it again, her player must spend another blood point, as a new attempt is being made. Five or more successes on the initial roll means the vampire can control the object for duration of the scene. If this power is used to manipulate a living being, the subject may attempt to resist. In this case, the caster and the subject make opposed Willpower rolls each turn the control is \nOnce a Kindred reaches a rating of 3, she may levitate herself and “fly” at approximately running speed, no matter how much she weighs, though the weight restrictions apply if she manipulates other objects or subjects. Once a Kindred achieves 4, she may “throw” objects at a Strength equal to her level of mastery of\nthis path.",
                },
                {
                    "name": "500 pounds/250 kilograms",
                    "description": "This path gives the thaumaturge the ability to move\nobjects telekinetically through the mystic power of\nblood. At higher levels, even flight is possible (but be\ncareful who sees you…). Objects under the character’s\ncontrol may be manipulated as if she held them — they\nmay be lifted, spun, juggled, or even “thrown,” though\ncreating enough force to inflict actual damage requires\nmastery of at least the fourth level of this path. Some\ncasters skilled in this path even use it to guard their\nhavens, animating swords, axes, and firearms to ward\noff intruders. This path may frighten and disconcert\nonlookers.",
                    "system": "The number of successes indicates the duration of the caster’s control over the object (or subject). Each success allows one turn of manipulation, though the Kindred may attempt to maintain control after this time by making a new roll (she need not spend additional blood to maintain control). If the roll is successful,\ncontrol is maintained. If a thaumaturge loses or relaxes control over an object and later manipulates it again, her player must spend another blood point, as a new attempt is being made. Five or more successes on the initial roll means the vampire can control the object for duration of the scene. If this power is used to manipulate a living being, the subject may attempt to resist. In this case, the caster and the subject make opposed Willpower rolls each turn the control is \nOnce a Kindred reaches a rating of 3, she may levitate herself and “fly” at approximately running speed, no matter how much she weighs, though the weight restrictions apply if she manipulates other objects or subjects. Once a Kindred achieves 4, she may “throw” objects at a Strength equal to her level of mastery of\nthis path.",
                },
                {
                    "name": "1000 pounds/500 kilograms",
                    "description": "This path gives the thaumaturge the ability to move\nobjects telekinetically through the mystic power of\nblood. At higher levels, even flight is possible (but be\ncareful who sees you…). Objects under the character’s\ncontrol may be manipulated as if she held them — they\nmay be lifted, spun, juggled, or even “thrown,” though\ncreating enough force to inflict actual damage requires\nmastery of at least the fourth level of this path. Some\ncasters skilled in this path even use it to guard their\nhavens, animating swords, axes, and firearms to ward\noff intruders. This path may frighten and disconcert\nonlookers.",
                    "system": "The number of successes indicates the duration of the caster’s control over the object (or subject). Each success allows one turn of manipulation, though the Kindred may attempt to maintain control after this time by making a new roll (she need not spend additional blood to maintain control). If the roll is successful,\ncontrol is maintained. If a thaumaturge loses or relaxes control over an object and later manipulates it again, her player must spend another blood point, as a new attempt is being made. Five or more successes on the initial roll means the vampire can control the object for duration of the scene. If this power is used to manipulate a living being, the subject may attempt to resist. In this case, the caster and the subject make opposed Willpower rolls each turn the control is \nOnce a Kindred reaches a rating of 3, she may levitate herself and “fly” at approximately running speed, no matter how much she weighs, though the weight restrictions apply if she manipulates other objects or subjects. Once a Kindred achieves 4, she may “throw” objects at a Strength equal to her level of mastery of\nthis path.",
                },
            ],
        },
        {
            "name": "Path of Blood (Anarch, Hacktivist)",
            "reference": "Rites of the Blood; PG 58 (V20 Core; PG 212)",
            "type": "Thaumaturgy (Anarch, Hacktivist)",
            "powers": [
                {
                    "name": "A Taste for Blood",
                    "description": "This power was developed as a means of testing a foe’s might — an extremely important ability in the tumultuous early nights of Clan Tremere. By merely touching the blood of his subject, the caster may de-termine how much vitae remains in the subject and, if the subject is a vampire, how recently he has fed, his approximate Generation and, with three or more suc-cesses, whether he has ever committed diablerie.",
                    "system": "The number of successes achieved on the roll determines how much information the thauma-turge gleans and how accurate it is.",
                },
                {
                    "name": "Blood Rage",
                    "description": "This power allows a vampire to force another Kin-dred to expend blood against his will. The caster must touch her subject for this power to work, though only the lightest contact is necessary. A vampire affected by this power might feel a physical rush as the thau-maturge heightens his Physical Attributes, might find himself suddenly looking more human, or may even find himself on the brink of frenzy as his stores of vitae are mystically depleted.",
                    "system": "Each success forces the subject to spend one blood point immediately in the way the caster desires (which must go towards some logical expenditure the target vampire could make, such as increasing Physical Attributes or powering Disciplines). Note that blood points forcibly spent in this manner may exceed the normal “per turn” maximum indicated by the victim’s Generation. Each success gained also increases the subject’s difficulty to resist frenzy by one. The thauma-turge may not use Blood Rage on herself to circumvent generational limits.",
                },
                {
                    "name": "Blood of Potency",
                    "description": "The thaumaturge gains such control over his own blood that he may effectively “concentrate” it, mak-ing it more powerful for a short time. In effect, he may temporarily lower his own Generation with this power. This power may be used only once per night.",
                    "system": "One success on the Willpower roll allows the character to lower his Generation by one step for one hour. Each additional success grants the Kindred either one step down in Generation or one hour of ef-fect. Successes earned must be spent both to decrease the vampire’s Generation and to maintain the change (this power cannot be activated again until the origi-nal application wears off). If the vampire is diablerized while this power is in effect, it wears off immediately and the diablerist gains power appropriate to the cast-er’s actual Generation. Furthermore, any mortals Em-braced by the thaumaturge are born to the Generation appropriate to their sire’s original Generation (e.g., a Tenth-Generation Tremere who has reduced his ef-fective Generation to Eighth still produces Eleventh-Generation childer).Once the effect wears off, any blood over the char-acter’s blood pool maximum dilutes, leaving the char-acter at his regular blood pool maximum. Thus, if a Twelfth-Generation Tremere (maximum blood pool of 11) decreased his Generation to Ninth (maximum blood pool 14), ingested 14 blood points, and had this much vitae in his system when the power wore off, his blood pool would immediately drop to 11.",
                },
                {
                    "name": "Theft of Vitae",
                    "description": "A thaumaturge using this power siphons vitae from her subject. She need never come in contact with the subject — blood literally streams out in a physical tor-rent from the subject to the Kindred (though it is often mystically absorbed and need not enter through the mouth).",
                    "system": "The number of successes determines how many blood points the caster transfers from the sub-ject. The subject must be visible to the thaumaturge and within 50 feet (15 meters). Using this power pre-vents the caster from being blood-bound, but other-wise counts as if the vampire ingested the blood her-self. This power is spectacularly obvious, and Camarilla princes justifiably consider its public use a breach of the Masquerade.",
                },
                {
                    "name": "Cauldron of Blood",
                    "description": "A thaumaturge using this power boils her subject’s blood in his veins like water on a stove. The Kindred must touch her subject, and it is this contact that sim-mers the subject’s blood. This power is always fatal to mortals, and causes great damage to even the mightiest vampires.",
                    "system": "The number of successes gained determines how many blood points are brought to boil. The sub-ject suffers one health level of aggravated damage for each point boiled (individuals with Fortitude may soak this damage using only their Fortitude dice). A single success kills any mortal, though some ghouls with ac-cess to Fortitude are said to have survived after soaking all of the aggravated damage.",
                },
            ],
        },
        {
            "name": "Path of Conjuring (Anarch, Hacktivist)",
            "reference": "Rites of the Blood; PG 58 (V20 Core; PG 221)",
            "type": "Thaumaturgy (Anarch, Hacktivist)",
            "powers": [
                {
                    "name": "Summon the Simple Form",
                    "description": "At this level of mastery, the conjurer may create\nsimple, inanimate objects. The object cannot have any\nmoving parts and may not be made of multiple materials.\nFor example, the conjurer may summon a steel\nbaton, a lead pipe, a wooden stake, or a chunk of granite.",
                    "system": "Each turn the conjurer wishes to keep the\r\nobject in existence, another Willpower point must be\r\nspent or the object vanishes.",
                },
                {
                    "name": "Permanency",
                    "description": "At this level, the conjurer no longer needs to pay\r\nWillpower costs to keep an object in existence. The\r\nobject is permanent, though simple objects are still all\r\nthat may be created.",
                    "system": "The player must invest three blood points\r\nin an object to make it real.",
                },
                {
                    "name": "Magic of the Smith",
                    "description": "The Kindred may now conjure complex objects of\r\nmultiple components and with moving parts. For example,\r\nthe thaumaturge can create guns, bicycles,\r\nchainsaws, or cellphones.",
                    "system": "Objects created via Magic of the Smith are\r\nautomatically permanent and cost five blood points\r\nto conjure. Particularly complex items often require a\r\nKnowledge roll (Crafts, Science, Technology, etc.) in\r\naddition to the basic roll.",
                },
                {
                    "name": "Reverse Conjuration",
                    "description": "This power allows the conjurer to “banish” into nonexistence\r\nany object previously called forth via this\r\npath.",
                    "system": "This is an extended success roll. The conjurer\r\nmust accumulate as many successes as the original\r\ncaster received when creating the object in question.\r\nThis can also be used by the thaumaturge to banish\r\nobject she created herself with this Path.",
                },
                {
                    "name": "Power Over Life",
                    "description": "This power cannot create true life, though it can\r\nsummon forth impressive simulacra. Creatures (and\r\npeople) summoned with this power lack the free will\r\nto act on their own, mindlessly following the simple\r\ninstructions of their conjurer instead. People created\r\nin this way can be subject to the use of the Dominate\r\npower Possession (p. 155), if desired.",
                    "system": "The player spends 10 blood points. Imperfect\r\nand impermanent, creatures summoned via this\r\npath are too complex to exist for long. Within a week\r\nafter their conjuration, the simulacra vanish into insubstantiality.",
                },
            ],
        },
        {
            "name": "Path of Technomancy (Anarch, Hacktivist)",
            "reference": "Rites of the Blood; PG 58 (V20 Core; PG 225)",
            "type": "Thaumaturgy (Anarch, Hacktivist)",
            "powers": [
                {
                    "name": "Analyze",
                    "description": "Mortals are constantly developing new innovations,\nand any vampire who would work Technomancy must\nbe able to understand that upon which he practices his\nmagic. The most basic power of this path allows the\nthaumaturge to project his perceptions into a device,\ngranting him a temporary understanding of its purpose,\nthe principles of its functioning, and its means of operation.\nThis does not grant permanent knowledge,\nonly a momentary flash of insight which fades within\nminutes.",
                    "system": "A character must touch the device in order\nto apply this power. The number of successes rolled determines\nhow well the character understands this particular\npiece of equipment. One success allows a basic\nknowledge (on/off and simple functions), while three\nsuccesses grant competence in operating the device,\nand five successes show the character the full range of\nthe device’s potential. The knowledge lasts for a number\nof minutes equal to the character’s Intelligence.\nThis power can also be used to understand a nonphysical\ntechnological innovation — generally a piece\nof software — at +2 difficulty. The character must\ntouch the computer on which the software is installed\n— simply holding the flash drive or CD-ROM is not\nenough. Software applied remotely to a device (such\nas through an app store) also cannot be analyzed until\nit is installed.",
                },
                {
                    "name": "Burnout",
                    "description": "It is usually easier to destroy than to create, and sensitive\nelectronics are no exception to this rule. Burnout\nis used to cause a device’s power supply (either internal\nor external) to surge, damaging or destroying the\ntarget. Burnout cannot be used to directly injure another\nindividual, although the sudden destruction of\na pacemaker or a car’s fuel injection control chip can\ncertainly create a health hazard.",
                    "system": "A character can use this power at a range\nof up to 10 times her Willpower in yards or meters,\nalthough a +1 difficulty is applied if she is not touching\nthe target item. The number of successes determines\nthe extent of the damage:\n\nSuccesses    Result\n1 success     Momentary interruption of operation (one turn), but no permanent damage.\n2 successes  Significant loss of function; +1 difficulty to use using the device for the rest of the scene.\n3 successes  The device breaks and is inoperable until repaired.\n4 successes  Even after repairs, the device’s capabilities are diminished (permanent +1 difficulty to use).\n5 successes  The equipment is a total write-off; completely unsalvageable.\n\nLarge enough systems, such as a server cluster or\na passenger aircraft, impose a +2 to +4 difficulty (at\nStoryteller discretion) to affect with this power. Additionally,\nsome systems, such as military and banking\nnetworks, may be protected against power surges and\nspikes, and thus possess one to five dice (Storyteller\ndiscretion again) to roll to resist this power. Each success\non this roll (difficulty 6) takes away one success\nfrom the Thaumaturgy roll.\nBurnout may be used to destroy electronic data storage,\nin which case three successes destroy all information\non the target item, and five erase it beyond any\nhope of non-magical recovery.",
                },
                {
                    "name": "Encrypt/Decrypt",
                    "description": "Electronic security is a paramount concern of governments\nand corporations alike. Those thaumaturges\nwho are techno-savvy enough to understand the issues\nat stake have become quite enamored of this power,\nwhich allows them to scramble a device’s controls mystically,\nmaking it inaccessible to anyone else. Encrypt/\nDecrypt also works on electronic media; a DVD under\nthe influence of this power displays just snow and static\nif played back without the owner’s approval. Some neonates\nhave taken to calling this power “DRM.”",
                    "system": "The character touches the device or data\ncontainer that he wishes to encrypt. The player rolls\nnormally. The number of successes scored is applied as\na difficulty modifier for anyone who attempts to use the\nprotected equipment or access the scrambled information\nwithout the assistance of the character. The caster\ncan dispel the effect at any time by touching the target\nitem and spending a point of Willpower.\n\nThis power may also be used to counter another\nthaumaturge’s use of Encrypt/Decrypt. The player rolls\nat +1 difficulty; each success negates one of the “owner’s.”\nThe effects of Encrypt/Decrypt last for a number of\nweeks equal to the character’s permanent Willpower\nrating.",
                },
                {
                    "name": "Remote Access",
                    "description": "With this power, a skilled thaumaturge can bypass\nthe need for physical contact to operate a device. This\nis not a form of telekinesis; the vampire does not manipulate\nthe item’s controls, but rather touches it directly\nwith the power of his mind.",
                    "system": "This power may be used on any electronic\ndevice within the character’s line of sight. The number\nof successes rolled is the maximum number of dice\nfrom any relevant Ability that the character may use\nwhile remotely controlling the device. (For instance, if\nFritz has Technology 5 and scores three successes while\nusing Remote Access on a keypad lock, he can only\napply three dots of his Technology rating to any rolls\nthat he makes through any use of the power.) Remote\nAccess lasts for a number of turns equal to the number\nof successes rolled, and can only be used on one item\nat a time.\nIf an item is destroyed while under the effects of Remote\nAccess, the character takes five dice of bashing\ndamage due to the shock of having his perceptions\nrudely shunted back into his own body.",
                },
                {
                    "name": "Telecommute",
                    "description": "A progressive derivation of Remote Access, Telecommute\nallows a thaumaturge to project her consciousness\ninto the Internet, sending her mind through\nnetwork connections as fast as they can transfer her.\nWhile immersed in the network, she can use any other\nTechnomancy power on the devices with which she\nmakes contact.",
                    "system": "The character touches any form of communications\ndevice: a cellphone, 3G-equipped netbook,\nWi-Fi tablet, or anything else that is connected directly\nor indirectly to the Internet. The player rolls normally\nand spends a Willpower point. Telecommute lasts for\nfive minutes per success rolled, and may be extended by\n10 minutes with the expenditure of another Willpower\npoint. The number of successes indicates the maximum\nrange that the character can project her consciousness\naway from her body:\n\nSuccesses    Result\n1 success     25 miles/40 kilometers\n2 successes  250 miles/400 kilometers\n3 successes  1000 miles/1500 kilometers\n4 successes  5000 miles/8000 kilometers\n5 successes  Anywhere in the world\n\nWhile in the network, the character can apply any\nother Path of Technomancy power to any device or\ndata with which she comes in contact. A loss of connection,\neither through the destruction of a part of the\nnetwork or simply a loss of cell signal, hurls her consciousness\nback to her body and inflicts eight dice of\nbashing damage.\nA character traveling through the Internet by means\nof this power can use her Path of Technomancy powers\nat a normal difficulty. Using any other abilities or powers\nwhile engaged thus is done at a +2 difficulty.",
                },
            ],
        },
        {
            "name": "Path of the Levinbolt",
            "reference": "Rites of the Blood; PG 58",
            "type": "Thaumaturgy (Anarch, Hacktivist)",
            "powers": [
                {
                    "name": "Flicker",
                    "description": "Novice Thaumaturges learn to freely absorb power\naround them through electrical outlets, circuits, or \nbatteries. A user of this power can sense the current \nfeeding into a specific electrical system and then draw\nit to her, effectively turning it off.",
                    "system": "The thaumaturge simply glances at a target \npowered by electricity. Upon a succesful activation \nroll, she can shut down an electrical device for ten \nminutes per success on the activation roll. The spark \nof electricity arcs from the device directly into the \nthaumaturge in a frightening display of mystical power. \nThe source of this power is immediately known.",
                },
                {
                    "name": "Spark",
                    "description": "Novice thaumaturges can build up a tiny static \ncharge, enough to make a noticeable snap with a \ntouch. Such a discharge poses little threat to healthy \ntargets, though the energy can ruin delicae electronics \nor stun an unlucky victim.",
                    "system": "The thaumaturge simply touches a target \n(after the requisite blood expenditure and activation \nroll by the player) and releases the spark. The \nelectricity can snap from any part of the caster's body, \nso a thaumaturge might give an unpleasant surprise\nto someone touching her. The resulting electrical \ndischarge inflicts four dice of lethal damage to targets\n(difficulty 7 to soak), and short-circuits electronic \nequipment and devices not specifically grounded \nagainst lightning strike.",
                },
                {
                    "name": "Illuminate",
                    "description": 'Neonates sometimes derogatively refer to this effect\nas the "40-watt Tremere," right up until they\'ve felt its\nsting. The thaumaturge summons enough electricity \nto cover her hand or arm in arcing bolts. This power \ncan charge a battery, briefly run a small device, or \neven leave a nasty burn on a touched subject.',
                    "system": "Each success scored on the player's \nactivation roll translates to approximately one turn of \npower sufficient to run a handful of lights or a small \nelectrical device. Alternately, the thaumaturge can \nshock someone by touch, as with the Spark power, \nbut for eight dice of lethal electricity damage (difficulty \n8 to soak). \nThe current created with this power is not strong \nenough to force its way through less-than-ideal \nconductors, and thus simply inflicts electrical damage \nraw metals, woods, or other matter in the form of a burn \nand discoloration. The thaumaturge can alternately allow \nthe electricity to spark around her hand, eyes, or head; \nthis creates illumination about equal to a dim light bulb,\nand lowers the difficulty of any Intimidation rolls by 2.",
                },
                {
                    "name": "Thor's Fury",
                    "description": "The thaumaturge may strike her enemies from afar as \nthough she were a god. She may direct an arc of lightning \nfrom her body to nearby targets.",
                    "system": "The thaumaturge focuses her concentration \nupon her target and then directs hurled bolts via a \nPerception + Science roll (difficulty 6 plus the range \nin yard/meters, maximum 4 yards/meters). Each success \ninflicts a level of lethal damage (difficulty 8 to soak). The \nsource of this power is immediately known.",
                },
                {
                    "name": "Eye of the Storm",
                    "description": "The thaumaturge becomes a shifting, sparkling pillar of \nelectrical power. The energy channeled in the Eye of the \nStorm shields her body from virtually any direct harm.",
                    "system": "When a thaumaturge spends a Willpower point \nto invoke this power, she solidifies the stored electricity \ninside of her into a mystical barrier that completely \nsorrounds her. The caster becomes immune to any ranged \nattacks. Metal weapons such as swords inflict injury as \nnormal for the first sttrike, but are then melted from \ncontact with the barrier, and the wielder takes a level \nof lethal damage. Enemies that dare to touch the caster \nsuffer two points of aggravated damage (difficulty 8 to \nsoak.) Non-mettal weapons, such as wooden stakes, are not \naffected by Eye of the Storm. This power lasts for a single \nturn, with each additional success on the activattion roll \nextending tthis duration by one turn. Mental and social \nattacks may pass through this barrier.",
                },
            ],
        },
        {
            "name": "Thaumaturgical Countermagic (Anarch, Hacktivist)",
            "reference": "Rites of the Blood; PG 58 (V20 Core; PG 228)",
            "type": "Thaumaturgy (Anarch, Hacktivist)",
            "powers": [
                {
                    "name": "Thaumaturgical Countermagic (1-5)",
                    "description": "This is less of a path than it is a separate Discipline, as the power to resist Thaumaturgy can be taught independently of Thaumaturgy, even to those Kindred who are incapable of mastering the simplest ritual. Though the techniques of Thaumaturgical Countermagic are\nnot officially taught outside Clan Tremere, unofficial methods are likely to exist. Any non-Tremere who displays the ability to resist Thaumaturgy quickly becomes the subject of potentially fatal scrutiny from the entirety of Clan Tremere.",
                    "system": "Thaumaturgical Countermagic is treated as a separate Discipline, although it uses the usual rules for Thaumaturgy (including experience costs and the fact that it is limited to only five levels). It cannot be taken as a character’s primary path, and a rating in it does not allow the character to perform rituals. The use of Thaumaturgical Countermagic is treated as a free action in combat and does not require a split dice pool. To oppose a Thaumaturgy power or ritual, a character must have a Thaumaturgical Countermagic rating equal to or greater than the rating of that power or ritual. The player spends a blood point and rolls the number of dice indicated by the character’s Thaumaturgical Countermagic rating (difficulty equal to the difficulty of the power in use). Each success cancels one of the opposing thaumaturge’s successes. Thaumaturgical Countermagic is only at full effectiveness when used against Thaumaturgy. It works with halved dice pools against Necromancy and other mystical Disciplines, and is completely ineffective against non-vampiric magics and powers.\nThaumaturgical Countermagic can be learned by characters who are unable to learn Thaumaturgy (e.g., those with the Merit Magic Resistance). Any non-Tremere character with a rating in this power automatically gains the Flaw Clan Enmity (Tremere), receiving no freebie points for it. This power cannot be taken during character creation and cannot be spontaneously developed. Whether the character has Thaumaturgy as an in-Clan power or not, it costs the same as any other non-Clan Discipline to learn.\nTwo dice of countermagic. The character can attempt to cancel only those powers and rituals that directly affect him, his garments, and objects on his person.",
                },
                {
                    "name": "Thaumaturgical Countermagic (1-5)",
                    "description": "This is less of a path than it is a separate Discipline, as the power to resist Thaumaturgy can be taught independently of Thaumaturgy, even to those Kindred who are incapable of mastering the simplest ritual. Though the techniques of Thaumaturgical Countermagic are\nnot officially taught outside Clan Tremere, unofficial methods are likely to exist. Any non-Tremere who displays the ability to resist Thaumaturgy quickly becomes the subject of potentially fatal scrutiny from the entirety of Clan Tremere.",
                    "system": "Thaumaturgical Countermagic is treated as a separate Discipline, although it uses the usual rules for Thaumaturgy (including experience costs and the fact that it is limited to only five levels). It cannot be taken as a character’s primary path, and a rating in it does not allow the character to perform rituals. The use of Thaumaturgical Countermagic is treated as a free action in combat and does not require a split dice pool. To oppose a Thaumaturgy power or ritual, a character must have a Thaumaturgical Countermagic rating equal to or greater than the rating of that power or ritual. The player spends a blood point and rolls the number of dice indicated by the character’s Thaumaturgical Countermagic rating (difficulty equal to the difficulty of the power in use). Each success cancels one of the opposing thaumaturge’s successes. Thaumaturgical Countermagic is only at full effectiveness when used against Thaumaturgy. It works with halved dice pools against Necromancy and other mystical Disciplines, and is completely ineffective against non-vampiric magics and powers.\nThaumaturgical Countermagic can be learned by characters who are unable to learn Thaumaturgy (e.g., those with the Merit Magic Resistance). Any non-Tremere character with a rating in this power automatically gains the Flaw Clan Enmity (Tremere), receiving no freebie points for it. This power cannot be taken during character creation and cannot be spontaneously developed. Whether the character has Thaumaturgy as an in-Clan power or not, it costs the same as any other non-Clan Discipline to learn.\nFour dice of countermagic. The character can attempt to cancel only those powers and rituals that directly affect him, his garments, and objects on his person.",
                },
                {
                    "name": "Thaumaturgical Countermagic (1-5)",
                    "description": "This is less of a path than it is a separate Discipline, as the power to resist Thaumaturgy can be taught independently of Thaumaturgy, even to those Kindred who are incapable of mastering the simplest ritual. Though the techniques of Thaumaturgical Countermagic are\nnot officially taught outside Clan Tremere, unofficial methods are likely to exist. Any non-Tremere who displays the ability to resist Thaumaturgy quickly becomes the subject of potentially fatal scrutiny from the entirety of Clan Tremere.",
                    "system": "Thaumaturgical Countermagic is treated as a separate Discipline, although it uses the usual rules for Thaumaturgy (including experience costs and the fact that it is limited to only five levels). It cannot be taken as a character’s primary path, and a rating in it does not allow the character to perform rituals. The use of Thaumaturgical Countermagic is treated as a free action in combat and does not require a split dice pool. To oppose a Thaumaturgy power or ritual, a character must have a Thaumaturgical Countermagic rating equal to or greater than the rating of that power or ritual. The player spends a blood point and rolls the number of dice indicated by the character’s Thaumaturgical Countermagic rating (difficulty equal to the difficulty of the power in use). Each success cancels one of the opposing thaumaturge’s successes. Thaumaturgical Countermagic is only at full effectiveness when used against Thaumaturgy. It works with halved dice pools against Necromancy and other mystical Disciplines, and is completely ineffective against non-vampiric magics and powers.\nThaumaturgical Countermagic can be learned by characters who are unable to learn Thaumaturgy (e.g., those with the Merit Magic Resistance). Any non-Tremere character with a rating in this power automatically gains the Flaw Clan Enmity (Tremere), receiving no freebie points for it. This power cannot be taken during character creation and cannot be spontaneously developed. Whether the character has Thaumaturgy as an in-Clan power or not, it costs the same as any other non-Clan Discipline to learn.\nSix dice of countermagic. The character can attempt to cancel a Thaumaturgy power that affects anyone or anything in physical contact with him.",
                },
                {
                    "name": "Thaumaturgical Countermagic (1-5)",
                    "description": "This is less of a path than it is a separate Discipline, as the power to resist Thaumaturgy can be taught independently of Thaumaturgy, even to those Kindred who are incapable of mastering the simplest ritual. Though the techniques of Thaumaturgical Countermagic are\nnot officially taught outside Clan Tremere, unofficial methods are likely to exist. Any non-Tremere who displays the ability to resist Thaumaturgy quickly becomes the subject of potentially fatal scrutiny from the entirety of Clan Tremere.",
                    "system": "Thaumaturgical Countermagic is treated as a separate Discipline, although it uses the usual rules for Thaumaturgy (including experience costs and the fact that it is limited to only five levels). It cannot be taken as a character’s primary path, and a rating in it does not allow the character to perform rituals. The use of Thaumaturgical Countermagic is treated as a free action in combat and does not require a split dice pool. To oppose a Thaumaturgy power or ritual, a character must have a Thaumaturgical Countermagic rating equal to or greater than the rating of that power or ritual. The player spends a blood point and rolls the number of dice indicated by the character’s Thaumaturgical Countermagic rating (difficulty equal to the difficulty of the power in use). Each success cancels one of the opposing thaumaturge’s successes. Thaumaturgical Countermagic is only at full effectiveness when used against Thaumaturgy. It works with halved dice pools against Necromancy and other mystical Disciplines, and is completely ineffective against non-vampiric magics and powers.\nThaumaturgical Countermagic can be learned by characters who are unable to learn Thaumaturgy (e.g., those with the Merit Magic Resistance). Any non-Tremere character with a rating in this power automatically gains the Flaw Clan Enmity (Tremere), receiving no freebie points for it. This power cannot be taken during character creation and cannot be spontaneously developed. Whether the character has Thaumaturgy as an in-Clan power or not, it costs the same as any other non-Clan Discipline to learn.\nEight dice of countermagic. The character can attempt to cancel a Thaumaturgy power that affects anyone or anything in physical contact with him.",
                },
                {
                    "name": "Thaumaturgical Countermagic (1-5)",
                    "description": "This is less of a path than it is a separate Discipline, as the power to resist Thaumaturgy can be taught independently of Thaumaturgy, even to those Kindred who are incapable of mastering the simplest ritual. Though the techniques of Thaumaturgical Countermagic are\nnot officially taught outside Clan Tremere, unofficial methods are likely to exist. Any non-Tremere who displays the ability to resist Thaumaturgy quickly becomes the subject of potentially fatal scrutiny from the entirety of Clan Tremere.",
                    "system": "Thaumaturgical Countermagic is treated as a separate Discipline, although it uses the usual rules for Thaumaturgy (including experience costs and the fact that it is limited to only five levels). It cannot be taken as a character’s primary path, and a rating in it does not allow the character to perform rituals. The use of Thaumaturgical Countermagic is treated as a free action in combat and does not require a split dice pool. To oppose a Thaumaturgy power or ritual, a character must have a Thaumaturgical Countermagic rating equal to or greater than the rating of that power or ritual. The player spends a blood point and rolls the number of dice indicated by the character’s Thaumaturgical Countermagic rating (difficulty equal to the difficulty of the power in use). Each success cancels one of the opposing thaumaturge’s successes. Thaumaturgical Countermagic is only at full effectiveness when used against Thaumaturgy. It works with halved dice pools against Necromancy and other mystical Disciplines, and is completely ineffective against non-vampiric magics and powers.\nThaumaturgical Countermagic can be learned by characters who are unable to learn Thaumaturgy (e.g., those with the Merit Magic Resistance). Any non-Tremere character with a rating in this power automatically gains the Flaw Clan Enmity (Tremere), receiving no freebie points for it. This power cannot be taken during character creation and cannot be spontaneously developed. Whether the character has Thaumaturgy as an in-Clan power or not, it costs the same as any other non-Clan Discipline to learn.\nTen dice of countermagic. The character can now attempt to cancel a power or ritual that targets anything within a radius equal to his Willpower in yards or meters, or one that is being used or performed within that same radius.",
                },
            ],
        },
        {
            "name": "Green Path (Anarch, New Age)",
            "reference": "Rites of the Blood; PG 55 (V20 Core; PG 215)",
            "type": "Thaumaturgy (Anarch, New Age)",
            "powers": [
                {
                    "name": "Herbal Wisdom",
                    "description": "With a touch, a vampire can commune with the\r\nspirit of a plant. Conversations held in this manner are\r\noften cryptic but rewarding — the wisdom and experience\r\nof the spirits of some trees surpasses that of the\r\noracles of legend. Crabgrass, on the other hand, rarely\r\nhas much insight to offer, but might reveal the appearance\r\nof the last person who trod upon it.",
                    "system": "The number of successes rolled determines\r\nthe amount of information that can be gained from the\r\ncontact. Depending on the precise information that\r\nthe vampire seeks, the Storyteller might require the\r\nplayer to roll Intelligence + Occult in order to interpret\r\nthe results of the communication.\r\nSuccesses Result\r\n1 success Fleeting cryptic impressions\r\n2 successes One or two clear images\r\n3 successes A concise answer to a simple query\r\n4 successes A detailed response to one or more\r\ncomplex questions\r\n5 successes The sum total of the plant-spirit’s\r\nknowledge on a given subject",
                },
                {
                    "name": "Speed the Seasons Passing",
                    "description": "This power allows a thaumaturge to accelerate a plant’s\r\ngrowth, causing roses to bloom in a matter of minutes or\r\ntrees to shoot up from saplings overnight. Alternately,\r\nshe can speed a plant’s death and decay, withering grass\r\nand crumbling wooden stakes with but a touch.",
                    "system": "The character touches the target plant. The\r\nplayer rolls normally, and the number of successes determines\r\nthe amount of growth or decay. One success\r\ngives the plant a brief growth spurt or simulates the effects\r\nof harsh weather, while three noticeably enlarge\r\nor wither it. With five successes, a full-grown plant\r\nsprings from a seed or crumbles to dust in a few minutes,\r\nand a tree sprouts fruit or begins decaying almost\r\ninstantaneously. If this power is used in combat, three\r\nsuccesses are needed to render a wooden weapon completely\r\nuseless. Two successes suffice to weaken it, while\r\nfive cause it to disintegrate in the wielder’s hand.",
                },
                {
                    "name": "Dance of Vines",
                    "description": "The thaumaturge can animate a mass of vegetation\r\nup to his own size, using it for utilitarian or combat purposes\r\nwith equal ease. Leaves can walk along a desktop,\r\nivy can act as a scribe, and jungle creepers can strangle\r\nopponents. Intruders should beware of Tremere workshops\r\nthat harbor potted rowan saplings.",
                    "system": "Any total amount of vegetation with a mass\r\nless than or equal to the character’s own may be animated\r\nthrough this power. The plants stay active for one turn\r\nper success scored on the roll, and are under the complete\r\ncontrol of the character. If used for combat purposes, the\r\nplants have Strength and Dexterity ratings each equal\r\nto half the character’s Willpower (rounded down) and\r\nBrawl ratings one lower than that of the character.\r\nDance of Vines cannot make plants uproot themselves\r\nand go stomping about. Even the most energetic\r\nvegetation is incapable of pulling out of the soil and\r\nwalking under the effect of this power. However, 200\r\npounds (100 kilograms) of kudzu can cover a considerable\r\narea all by itself….",
                },
                {
                    "name": "Verdant Haven",
                    "description": "This power weaves a temporary shelter out of a sufficient\r\namount of plant matter. In addition to providing physical\r\nprotection from the elements (and even sunlight), the\r\nVerdant Haven also establishes a mystical barrier which\r\nis nearly impassable to anyone the caster wishes to exclude.\r\nA Verdant Haven appears as a six-foot-tall (twometer-\r\ntall) hemisphere of interlocked branches, leaves, and vines with no discernible opening, and even to the\r\ncasual observer it appears to be an unnatural construction.\r\nVerdant Havens are rumored to have supernatural\r\nhealing properties, hut no Kindred have reported experiencing\r\nsuch benefits from a stay in one.",
                    "system": "A character must be standing in a heavily\r\nvegetated area to use this power. The Verdant Haven\r\nsprings up around the character over the course of three\r\nturns. Once the haven is established, anyone wishing\r\nto enter the haven without the caster’s permission\r\nmust achieve more than the caster’s original number of\r\nsuccesses on a single roll of Wits + Survival (difficulty\r\nequal to the caster’s Willpower). The haven lasts until\r\nthe next sunset, or until the caster dispels or leaves it.\r\nIf the caster scored four or more successes, the haven is\r\nimpenetrable to sunlight unless physically breached.",
                },
                {
                    "name": "Awaken the Forest Giants",
                    "description": "Entire trees can be animated by a master of the\r\nGreen Path. Ancient oaks can be temporarily given\r\nthe gift of movement, pulling their roots from the soil\r\nand shaking the ground with their steps. While not as\r\nversatile as elementals or other summoned spirits, trees\r\nbrought to ponderous life via this power display awesome\r\nstrength and resilience.",
                    "system": "The character touches the tree to be animated.\r\nThe player spends a blood point and rolls normally.\r\nIf the roll succeeds, the player must spend a blood\r\npoint for every success. The tree stays animated for one\r\nturn per success rolled; once this time expires, the tree\r\nputs its roots down wherever it stands and cannot be\r\nanimated again until the next night. While animated,\r\nthe tree follows the character’s verbal commands to\r\nthe best of its ability. An animated tree has Strength\r\nand Stamina equal to the caster’s Thaumaturgy rating,\r\nDexterity 2, and a Brawl rating equal to the caster’s\r\nown. It is immune to bashing damage, and all lethal\r\ndamage dice pools are halved due to its size.\r\nOnce the animating energy leaves a tree, it puts\r\ndown roots immediately, regardless of what it is currently\r\nstanding on. A tree re-establishing itself in the\r\nsoil can punch through concrete and asphalt to find\r\nnourishing dirt and water underneath, meaning that it\r\nis entirely possible for a sycamore to root itself in the\r\nmiddle of a road without any warning.",
                },
            ],
        },
        {
            "name": "Lure of Flames (Anarch, New Age)",
            "reference": "Rites of the Blood; PG 55 (V20 Core; PG 218)",
            "type": "Thaumaturgy (Anarch, New Age)",
            "powers": [
                {
                    "name": "Candle",
                    "description": "This path grants the thaumaturge the ability to conjure forth mystical flames — small fires at first, but skilled magicians may create great conflagrations. Fire created by this path is not “natural.” In fact, many vampires believe the flames to be conjured from Hell itself. The Lure of Flames is greatly feared, as fire is one of the surest ways to bring Final Death upon a vampire. See “Fire” (p. 297) for more information on how vampires suffer from flame.\n\nFire conjured by The Lure of Flames must be released for it to have any effect. Thus, a “palm of flame” does not burn the vampire’s hand and cause an aggravated wound (nor does it cause the caster to frenzy) — it merely produces light. Once the flame has been released, however, it burns normally and the character has no control over it.",
                    "system": "The number of successes determines how accurately the vampire places the flame in his desired location (declared before the roll is made). One success is all that is necessary to conjure a flame in one’s hand, while five successes place a flame anywhere in the Kindred’s line of sight. Less successes mean that the flame appears somewhere at the Storyteller’s discretion — as a rough rule of thumb, the thaumaturge can accurately place a flame within 10 yards or meters of themselves per success. Individual descriptions are not provided for each level of this path — fire is fire, after all (including potentially causing frenzy in other vampires witnessing it). The chart below describes the path level required to generate a specific amount of flame. To soak the damage at all, a vampire must have the Fortitude Discipline. Fire under the caster’s control does not harm the vampire or cause him to frenzy, but fires started as a result of the unnatural flame affect the thaumaturge normally.\nCandle (difficulty 3 to soak, one health level of aggravated damage/ turn)",
                },
                {
                    "name": "Palm of Flame",
                    "description": "This path grants the thaumaturge the ability to conjure forth mystical flames — small fires at first, but skilled magicians may create great conflagrations. Fire created by this path is not “natural.” In fact, many vampires believe the flames to be conjured from Hell itself. The Lure of Flames is greatly feared, as fire is one of the surest ways to bring Final Death upon a vampire. See “Fire” (p. 297) for more information on how vampires suffer from flame.\n\nFire conjured by The Lure of Flames must be released for it to have any effect. Thus, a “palm of flame” does not burn the vampire’s hand and cause an aggravated wound (nor does it cause the caster to frenzy) — it merely produces light. Once the flame has been released, however, it burns normally and the character has no control over it.",
                    "system": "The number of successes determines how accurately the vampire places the flame in his desired location (declared before the roll is made). One success is all that is necessary to conjure a flame in one’s hand, while five successes place a flame anywhere in the Kindred’s line of sight. Less successes mean that the flame appears somewhere at the Storyteller’s discretion — as a rough rule of thumb, the thaumaturge can accurately place a flame within 10 yards or meters of themselves per success. Individual descriptions are not provided for each level of this path — fire is fire, after all (including potentially causing frenzy in other vampires witnessing it). The chart below describes the path level required to generate a specific amount of flame. To soak the damage at all, a vampire must have the Fortitude Discipline. Fire under the caster’s control does not harm the vampire or cause him to frenzy, but fires started as a result of the unnatural flame affect the thaumaturge normally. \nPalm of flame (difficulty 4 to soak, one health level of aggravated damage/turn)",
                },
                {
                    "name": "Campfire",
                    "description": "This path grants the thaumaturge the ability to conjure forth mystical flames — small fires at first, but skilled magicians may create great conflagrations. Fire created by this path is not “natural.” In fact, many vampires believe the flames to be conjured from Hell itself. The Lure of Flames is greatly feared, as fire is one of the surest ways to bring Final Death upon a vampire. See “Fire” (p. 297) for more information on how vampires suffer from flame.\n\nFire conjured by The Lure of Flames must be released for it to have any effect. Thus, a “palm of flame” does not burn the vampire’s hand and cause an aggravated wound (nor does it cause the caster to frenzy) — it merely produces light. Once the flame has been released, however, it burns normally and the character has no control over it.",
                    "system": "The number of successes determines how accurately the vampire places the flame in his desired location (declared before the roll is made). One success is all that is necessary to conjure a flame in one’s hand, while five successes place a flame anywhere in the Kindred’s line of sight. Less successes mean that the flame appears somewhere at the Storyteller’s discretion — as a rough rule of thumb, the thaumaturge can accurately place a flame within 10 yards or meters of themselves per success. Individual descriptions are not provided for each level of this path — fire is fire, after all (including potentially causing frenzy in other vampires witnessing it). The chart below describes the path level required to generate a specific amount of flame. To soak the damage at all, a vampire must have the Fortitude Discipline. Fire under the caster’s control does not harm the vampire or cause him to frenzy, but fires started as a result of the unnatural flame affect the thaumaturge normally. \nCampfire (difficulty 5 to soak, two health levels of aggravated damage/turn)",
                },
                {
                    "name": "Bonfire",
                    "description": "This path grants the thaumaturge the ability to conjure forth mystical flames — small fires at first, but skilled magicians may create great conflagrations. Fire created by this path is not “natural.” In fact, many vampires believe the flames to be conjured from Hell itself. The Lure of Flames is greatly feared, as fire is one of the surest ways to bring Final Death upon a vampire. See “Fire” (p. 297) for more information on how vampires suffer from flame.\n\nFire conjured by The Lure of Flames must be released for it to have any effect. Thus, a “palm of flame” does not burn the vampire’s hand and cause an aggravated wound (nor does it cause the caster to frenzy) — it merely produces light. Once the flame has been released, however, it burns normally and the character has no control over it.",
                    "system": "The number of successes determines how accurately the vampire places the flame in his desired location (declared before the roll is made). One success is all that is necessary to conjure a flame in one’s hand, while five successes place a flame anywhere in the Kindred’s line of sight. Less successes mean that the flame appears somewhere at the Storyteller’s discretion — as a rough rule of thumb, the thaumaturge can accurately place a flame within 10 yards or meters of themselves per success. Individual descriptions are not provided for each level of this path — fire is fire, after all (including potentially causing frenzy in other vampires witnessing it). The chart below describes the path level required to generate a specific amount of flame. To soak the damage at all, a vampire must have the Fortitude Discipline. Fire under the caster’s control does not harm the vampire or cause him to frenzy, but fires started as a result of the unnatural flame affect the thaumaturge normally. \nBonfire (difficulty 7 to soak, two health levels of aggravated damage/turn)",
                },
                {
                    "name": "Inferno",
                    "description": "This path grants the thaumaturge the ability to conjure forth mystical flames — small fires at first, but skilled magicians may create great conflagrations. Fire created by this path is not “natural.” In fact, many vampires believe the flames to be conjured from Hell itself. The Lure of Flames is greatly feared, as fire is one of the surest ways to bring Final Death upon a vampire. See “Fire” (p. 297) for more information on how vampires suffer from flame.\n\nFire conjured by The Lure of Flames must be released for it to have any effect. Thus, a “palm of flame” does not burn the vampire’s hand and cause an aggravated wound (nor does it cause the caster to frenzy) — it merely produces light. Once the flame has been released, however, it burns normally and the character has no control over it.",
                    "system": "The number of successes determines how accurately the vampire places the flame in his desired location (declared before the roll is made). One success is all that is necessary to conjure a flame in one’s hand, while five successes place a flame anywhere in the Kindred’s line of sight. Less successes mean that the flame appears somewhere at the Storyteller’s discretion — as a rough rule of thumb, the thaumaturge can accurately place a flame within 10 yards or meters of themselves per success. Individual descriptions are not provided for each level of this path — fire is fire, after all (including potentially causing frenzy in other vampires witnessing it). The chart below describes the path level required to generate a specific amount of flame. To soak the damage at all, a vampire must have the Fortitude Discipline. Fire under the caster’s control does not harm the vampire or cause him to frenzy, but fires started as a result of the unnatural flame affect the thaumaturge normally. \nInferno (difficulty 9 to soak, three health levels of aggravated damage/turn)",
                },
            ],
        },
        {
            "name": "Movement of the Mind (Anarch, New Age)",
            "reference": "Rites of the Blood; PG 55 (V20 Core; PG 220)",
            "type": "Thaumaturgy (Anarch, New Age)",
            "powers": [
                {
                    "name": "1 pound/ .5 kilogram",
                    "description": "This path gives the thaumaturge the ability to move\nobjects telekinetically through the mystic power of\nblood. At higher levels, even flight is possible (but be\ncareful who sees you…). Objects under the character’s\ncontrol may be manipulated as if she held them — they\nmay be lifted, spun, juggled, or even “thrown,” though\ncreating enough force to inflict actual damage requires\nmastery of at least the fourth level of this path. Some\ncasters skilled in this path even use it to guard their\nhavens, animating swords, axes, and firearms to ward\noff intruders. This path may frighten and disconcert\nonlookers.",
                    "system": "The number of successes indicates the duration of the caster’s control over the object (or subject). Each success allows one turn of manipulation, though the Kindred may attempt to maintain control after this time by making a new roll (she need not spend additional blood to maintain control). If the roll is successful,\ncontrol is maintained. If a thaumaturge loses or relaxes control over an object and later manipulates it again, her player must spend another blood point, as a new attempt is being made. Five or more successes on the initial roll means the vampire can control the object for duration of the scene. If this power is used to manipulate a living being, the subject may attempt to resist. In this case, the caster and the subject make opposed Willpower rolls each turn the control is \nOnce a Kindred reaches a rating of 3, she may levitate herself and “fly” at approximately running speed, no matter how much she weighs, though the weight restrictions apply if she manipulates other objects or subjects. Once a Kindred achieves 4, she may “throw” objects at a Strength equal to her level of mastery of\nthis path.",
                },
                {
                    "name": "20 pounds/10 kilograms",
                    "description": "This path gives the thaumaturge the ability to move\nobjects telekinetically through the mystic power of\nblood. At higher levels, even flight is possible (but be\ncareful who sees you…). Objects under the character’s\ncontrol may be manipulated as if she held them — they\nmay be lifted, spun, juggled, or even “thrown,” though\ncreating enough force to inflict actual damage requires\nmastery of at least the fourth level of this path. Some\ncasters skilled in this path even use it to guard their\nhavens, animating swords, axes, and firearms to ward\noff intruders. This path may frighten and disconcert\nonlookers.",
                    "system": "The number of successes indicates the duration of the caster’s control over the object (or subject). Each success allows one turn of manipulation, though the Kindred may attempt to maintain control after this time by making a new roll (she need not spend additional blood to maintain control). If the roll is successful,\ncontrol is maintained. If a thaumaturge loses or relaxes control over an object and later manipulates it again, her player must spend another blood point, as a new attempt is being made. Five or more successes on the initial roll means the vampire can control the object for duration of the scene. If this power is used to manipulate a living being, the subject may attempt to resist. In this case, the caster and the subject make opposed Willpower rolls each turn the control is \nOnce a Kindred reaches a rating of 3, she may levitate herself and “fly” at approximately running speed, no matter how much she weighs, though the weight restrictions apply if she manipulates other objects or subjects. Once a Kindred achieves 4, she may “throw” objects at a Strength equal to her level of mastery of\nthis path.",
                },
                {
                    "name": "200 pounds/100 kilograms",
                    "description": "This path gives the thaumaturge the ability to move\nobjects telekinetically through the mystic power of\nblood. At higher levels, even flight is possible (but be\ncareful who sees you…). Objects under the character’s\ncontrol may be manipulated as if she held them — they\nmay be lifted, spun, juggled, or even “thrown,” though\ncreating enough force to inflict actual damage requires\nmastery of at least the fourth level of this path. Some\ncasters skilled in this path even use it to guard their\nhavens, animating swords, axes, and firearms to ward\noff intruders. This path may frighten and disconcert\nonlookers.",
                    "system": "The number of successes indicates the duration of the caster’s control over the object (or subject). Each success allows one turn of manipulation, though the Kindred may attempt to maintain control after this time by making a new roll (she need not spend additional blood to maintain control). If the roll is successful,\ncontrol is maintained. If a thaumaturge loses or relaxes control over an object and later manipulates it again, her player must spend another blood point, as a new attempt is being made. Five or more successes on the initial roll means the vampire can control the object for duration of the scene. If this power is used to manipulate a living being, the subject may attempt to resist. In this case, the caster and the subject make opposed Willpower rolls each turn the control is \nOnce a Kindred reaches a rating of 3, she may levitate herself and “fly” at approximately running speed, no matter how much she weighs, though the weight restrictions apply if she manipulates other objects or subjects. Once a Kindred achieves 4, she may “throw” objects at a Strength equal to her level of mastery of\nthis path.",
                },
                {
                    "name": "500 pounds/250 kilograms",
                    "description": "This path gives the thaumaturge the ability to move\nobjects telekinetically through the mystic power of\nblood. At higher levels, even flight is possible (but be\ncareful who sees you…). Objects under the character’s\ncontrol may be manipulated as if she held them — they\nmay be lifted, spun, juggled, or even “thrown,” though\ncreating enough force to inflict actual damage requires\nmastery of at least the fourth level of this path. Some\ncasters skilled in this path even use it to guard their\nhavens, animating swords, axes, and firearms to ward\noff intruders. This path may frighten and disconcert\nonlookers.",
                    "system": "The number of successes indicates the duration of the caster’s control over the object (or subject). Each success allows one turn of manipulation, though the Kindred may attempt to maintain control after this time by making a new roll (she need not spend additional blood to maintain control). If the roll is successful,\ncontrol is maintained. If a thaumaturge loses or relaxes control over an object and later manipulates it again, her player must spend another blood point, as a new attempt is being made. Five or more successes on the initial roll means the vampire can control the object for duration of the scene. If this power is used to manipulate a living being, the subject may attempt to resist. In this case, the caster and the subject make opposed Willpower rolls each turn the control is \nOnce a Kindred reaches a rating of 3, she may levitate herself and “fly” at approximately running speed, no matter how much she weighs, though the weight restrictions apply if she manipulates other objects or subjects. Once a Kindred achieves 4, she may “throw” objects at a Strength equal to her level of mastery of\nthis path.",
                },
                {
                    "name": "1000 pounds/500 kilograms",
                    "description": "This path gives the thaumaturge the ability to move\nobjects telekinetically through the mystic power of\nblood. At higher levels, even flight is possible (but be\ncareful who sees you…). Objects under the character’s\ncontrol may be manipulated as if she held them — they\nmay be lifted, spun, juggled, or even “thrown,” though\ncreating enough force to inflict actual damage requires\nmastery of at least the fourth level of this path. Some\ncasters skilled in this path even use it to guard their\nhavens, animating swords, axes, and firearms to ward\noff intruders. This path may frighten and disconcert\nonlookers.",
                    "system": "The number of successes indicates the duration of the caster’s control over the object (or subject). Each success allows one turn of manipulation, though the Kindred may attempt to maintain control after this time by making a new roll (she need not spend additional blood to maintain control). If the roll is successful,\ncontrol is maintained. If a thaumaturge loses or relaxes control over an object and later manipulates it again, her player must spend another blood point, as a new attempt is being made. Five or more successes on the initial roll means the vampire can control the object for duration of the scene. If this power is used to manipulate a living being, the subject may attempt to resist. In this case, the caster and the subject make opposed Willpower rolls each turn the control is \nOnce a Kindred reaches a rating of 3, she may levitate herself and “fly” at approximately running speed, no matter how much she weighs, though the weight restrictions apply if she manipulates other objects or subjects. Once a Kindred achieves 4, she may “throw” objects at a Strength equal to her level of mastery of\nthis path.",
                },
            ],
        },
        {
            "name": "Path of Blood (Anarch, New Age)",
            "reference": "Rites of the Blood; PG 55 (V20 Core; PG 212)",
            "type": "Thaumaturgy (Anarch, New Age)",
            "powers": [
                {
                    "name": "A Taste for Blood",
                    "description": "This power was developed as a means of testing a foe’s might — an extremely important ability in the tumultuous early nights of Clan Tremere. By merely touching the blood of his subject, the caster may de-termine how much vitae remains in the subject and, if the subject is a vampire, how recently he has fed, his approximate Generation and, with three or more suc-cesses, whether he has ever committed diablerie.",
                    "system": "The number of successes achieved on the roll determines how much information the thauma-turge gleans and how accurate it is.",
                },
                {
                    "name": "Blood Rage",
                    "description": "This power allows a vampire to force another Kin-dred to expend blood against his will. The caster must touch her subject for this power to work, though only the lightest contact is necessary. A vampire affected by this power might feel a physical rush as the thau-maturge heightens his Physical Attributes, might find himself suddenly looking more human, or may even find himself on the brink of frenzy as his stores of vitae are mystically depleted.",
                    "system": "Each success forces the subject to spend one blood point immediately in the way the caster desires (which must go towards some logical expenditure the target vampire could make, such as increasing Physical Attributes or powering Disciplines). Note that blood points forcibly spent in this manner may exceed the normal “per turn” maximum indicated by the victim’s Generation. Each success gained also increases the subject’s difficulty to resist frenzy by one. The thauma-turge may not use Blood Rage on herself to circumvent generational limits.",
                },
                {
                    "name": "Blood of Potency",
                    "description": "The thaumaturge gains such control over his own blood that he may effectively “concentrate” it, mak-ing it more powerful for a short time. In effect, he may temporarily lower his own Generation with this power. This power may be used only once per night.",
                    "system": "One success on the Willpower roll allows the character to lower his Generation by one step for one hour. Each additional success grants the Kindred either one step down in Generation or one hour of ef-fect. Successes earned must be spent both to decrease the vampire’s Generation and to maintain the change (this power cannot be activated again until the origi-nal application wears off). If the vampire is diablerized while this power is in effect, it wears off immediately and the diablerist gains power appropriate to the cast-er’s actual Generation. Furthermore, any mortals Em-braced by the thaumaturge are born to the Generation appropriate to their sire’s original Generation (e.g., a Tenth-Generation Tremere who has reduced his ef-fective Generation to Eighth still produces Eleventh-Generation childer).Once the effect wears off, any blood over the char-acter’s blood pool maximum dilutes, leaving the char-acter at his regular blood pool maximum. Thus, if a Twelfth-Generation Tremere (maximum blood pool of 11) decreased his Generation to Ninth (maximum blood pool 14), ingested 14 blood points, and had this much vitae in his system when the power wore off, his blood pool would immediately drop to 11.",
                },
                {
                    "name": "Theft of Vitae",
                    "description": "A thaumaturge using this power siphons vitae from her subject. She need never come in contact with the subject — blood literally streams out in a physical tor-rent from the subject to the Kindred (though it is often mystically absorbed and need not enter through the mouth).",
                    "system": "The number of successes determines how many blood points the caster transfers from the sub-ject. The subject must be visible to the thaumaturge and within 50 feet (15 meters). Using this power pre-vents the caster from being blood-bound, but other-wise counts as if the vampire ingested the blood her-self. This power is spectacularly obvious, and Camarilla princes justifiably consider its public use a breach of the Masquerade.",
                },
                {
                    "name": "Cauldron of Blood",
                    "description": "A thaumaturge using this power boils her subject’s blood in his veins like water on a stove. The Kindred must touch her subject, and it is this contact that sim-mers the subject’s blood. This power is always fatal to mortals, and causes great damage to even the mightiest vampires.",
                    "system": "The number of successes gained determines how many blood points are brought to boil. The sub-ject suffers one health level of aggravated damage for each point boiled (individuals with Fortitude may soak this damage using only their Fortitude dice). A single success kills any mortal, though some ghouls with ac-cess to Fortitude are said to have survived after soaking all of the aggravated damage.",
                },
            ],
        },
        {
            "name": "Path of Corruption (Anarch, New Age)",
            "reference": "Rites of the Blood; PG 55 (V20 Core; PG 221)",
            "type": "Thaumaturgy (Anarch, New Age)",
            "powers": [
                {
                    "name": "Contradict",
                    "description": "The vampire can interrupt a subject’s thought processes,\r\nforcing the victim to reverse his current course\r\nof action. An Archon may be caused to execute a prisoner\r\nshe was about to exonerate and release; a mortal\r\nlover might switch from gentle and caring to sadistic\r\nand demanding in the middle of an encounter. The results\r\nof Contradict are never precisely known to the\r\nthaumaturge in advance, but they always take the form\r\nof a more negative action than the subject had originally\r\nintended to perform.",
                    "system": "This power may be used on any subject\r\nwithin the character’s line of sight. The player rolls as\r\nper normal. The target rolls Perception + Subterfuge\r\n(difficulty equal to the number of successes scored by\r\nthe caster + 2). Two successes allow the subject to realize that she is being influenced by some outside source.\r\nThree successes let her pinpoint the source of the effect.\r\nFour successes give her a moment of hesitation,\r\nneither performing her original action nor its inverse,\r\nwhile five allow her to carry through with the original\r\naction.\r\nThe Storyteller dictates what the subject’s precise\r\nreaction to this power is. Contradict cannot be used in\r\ncombat or to affect other actions (at the Storyteller’s\r\ndiscretion) that are mainly physical and reflexive.",
                },
                {
                    "name": "Subvert",
                    "description": "This power follows the same principle as does Contradict,\r\nthe release of a subject’s dark, self-destructive\r\nside. However, Subvert’s effects are longer-lasting than\r\nthe momentary flare of Contradiction. Under the influence\r\nof this power, victims act on their own suppressed\r\ntemptations, pursuing agendas that their morals\r\nor self-control would forbid them to follow under\r\nnormal circumstances.",
                    "system": "This power requires the character to make\r\neye contact (see p. 152) with the intended victim. The\r\nplayer rolls normally. The target resists with a roll of\r\nPerception + Subterfuge (difficulty equal to the target’s\r\nManipulation + Subterfuge). If the thaumaturge scores\r\nmore successes, the victim becomes inclined to follow\r\na repressed, shameful desire for the length of time described\r\nbelow.\r\nSuccesses Result\r\n1 success Five minutes\r\n2 successes One hour\r\n3 successes One night\r\n4 successes Three nights\r\n5 successes One week\r\nThe Storyteller determines the precise desire or\r\nagenda that the victim follows. It should be in keeping\r\nwith the Psychological Flaws that she possesses or\r\nwith the negative aspects of her Nature (for example,\r\na Loner desiring isolation to such an extent that she\r\nbecomes violent if forced to attend a social function).\r\nThe subject should not become fixated on following\r\nthis new agenda at all times, but should occasionally be\r\nforced to spend a Willpower point if the opportunity to\r\nsuccumb arises and she wishes to resist the impulse.",
                },
                {
                    "name": "Dissociate",
                    "description": "“Divide and conquer” is a maxim that is well-understood\r\nby the Tremere, and Dissociate is a powerful tool\r\nwith which to divide the Clan’s enemies. This power\r\nis used to break the social ties of interpersonal relationships.\r\nEven the most passionate affair or the oldest\r\nfriendship can be cooled through use of Dissociate, and\r\nweaker personal ties can be destroyed altogether.",
                    "system": "The character must touch the target. The\r\nplayer rolls normally. The target resists with a Willpower\r\nroll (difficulty of the thaumaturge’s Manipulation\r\n+ Empathy). The victim loses three dice from\r\nall Social rolls for a period of time determined by the\r\nnumber of successes gained by the caster:\r\nSuccesses Result\r\n1 success Five minutes\r\n2 successes One hour\r\n3 successes One night\r\n4 successes Three nights\r\n5 successes One week\r\nThis penalty applies to all rolls that rely on Social\r\nAttributes, even those required for the use of Disciplines.\r\nIf this power is used on a character who has\r\nparticipated in the Vaulderie or a similar ritual, that\r\ncharacter’s Vinculum ratings are reduced by three for\r\nthe duration of Dissociate’s effect.\r\nDissociate’s primary effect falls under roleplaying\r\nrather than game mechanics. Victims of this power\r\nshould be played as withdrawn, suspicious, and emotionally\r\ndistant. The Storyteller should feel free to require\r\na Willpower point expenditure for a player who\r\ndoes not follow these guidelines.",
                },
                {
                    "name": "Addiction",
                    "description": "This power is a much stronger and more potentially\r\ndamaging form of Subvert. Addiction creates just that\r\nin the victim. By simply exposing the target to a particular\r\nsensation, substance, or action, the caster creates\r\na powerful psychological dependence. Many thaumaturges\r\nensure that their victims become addicted to\r\nsubstances or thrills that only the mystic can provide,\r\nthus creating both a source of income and potential\r\nblackmail material.",
                    "system": "The subject must encounter or be exposed\r\nto the sensation, substance, or action to which the\r\ncharacter wants to addict him. The thaumaturge then\r\ntouches his target. The player rolls normally; the victim\r\nresists with a Self-Control/Instinct roll (difficulty\r\nequal to the number of successes scored by the caster\r\n+ 3). Failure gives the subject an instant addiction to\r\nthat object.\r\nAn addicted character must get his fix at least once\r\na night. Every night that he goes without satisfying his\r\ndesire imposes a cumulative penalty of one die on all of\r\nhis dice pools (to a minimum pool of one die). The victim\r\nmust roll Self-Control/Instinct (difficulty 8) every\r\ntime he is confronted with the object of his addiction\r\nand wishes to keep from indulging. Addiction lasts for\r\na number of weeks equal to the thaumaturge’s Manipulation\r\nscore.\r\nAn individual may try to break the effects of Addiction.\r\nThis requires an extended Self-Control/Instinct\r\nroll (difficulty of the caster’s Manipulation + Subterfuge),\r\nwith one roll made per night. The addict must\r\naccumulate a number of successes equal to three times\r\nthe number of successes scored by the caster. The victim\r\nmay not indulge in his addiction over the time\r\nneeded to accumulate these successes. If he does so, all\r\naccumulated successes are lost and he must begin anew\r\non the next night. Note that the Self-Control/Instinct\r\ndice pool is reduced every night that the victim goes\r\nwithout feeding his addiction.",
                },
                {
                    "name": "Dependence",
                    "description": "Many former pawns of Clan Tremere claim to have\r\nfelt a strange sensation similar to depression when not\r\nin the presence of their masters. This is usually attributed\r\nto the blood bond, but is sometimes the result of\r\nthe vampire’s mastery of Dependence. The final power\r\nof the Path of Corruption enables the vampire to tie\r\nher victim’s soul to her own, engendering feelings of\r\nlethargy and helplessness when the victim is not in her\r\npresence or acting to further her desires.",
                    "system": "The character engages the target in conversation.\nThe player rolls normally. The victim rolls\nSelf-Control/Instinct (difficulty equals the number of\nsuccesses scored by the caster + 3). Failure means that\nthe victim’s psyche has been subtly bonded to that of\nthe thaumaturge for one night per success rolled by the\ncaster.\nA bonded victim is no less likely to attack his controller,\nand feels no particular positive emotions toward\nher. However, he is psychologically addicted to\nher presence, and suffers a one-die penalty to all rolls\nwhen he is not around her or performing tasks for her. Additionally, he is much less resistant to her commands,\r\nand his dice pools are halved when he attempts\r\nto resist her Dominate, Presence (or other mental or\r\nemotional control powers), or mundane Social rolls.\r\nFinally, he is unable to regain Willpower when he is\r\nnot in the thaumaturge’s presence.",
                },
            ],
        },
        {
            "name": "Path of Teleportation (Anarch, New Age)",
            "reference": "Rites of the Blood; PG 55",
            "type": "Thaumaturgy (Anarch, New Age)",
            "powers": [
                {
                    "name": "10 yards/meters",
                    "description": "Praapti is the power of instantaneous travel. Indian Sadhana practitioners developed this Path to match their mysterious Asian rivals, who have the power to travel instantly along lines of mystical force. Later, turncoat sadhus sold the secret of this Path to the Tremere, who reverse-engineered it into what they call the Path of Mercury. A handful of New Age Anarchs have also stumbled onto the secret of this path, which they simply call Teleportation. Individual levels of this Path do not have distinct effects; instead, higher mastery simply indicates a farther distance that can be traveled. Ideally, the sorcerer must be able to see the target location or know it intimately. Teleportation is inherently risky and rarely exact, especially when used without clear knowledge of the destination.",
                    "system": "Teleport up to 10 yards/meters. Activating Praapti allows the sorcerer to instantly relocate to a point within short range. The destination should ideally be within sight or intimately known. Failure results in no effect. If the destination is nearby or visible, a botch causes standard blood magic backlash. Blind teleports risk materializing partially inside solid matter, causing aggravated damage per “1” rolled. One success transports only the sorcerer’s nude body, with additional successes allowing twenty extra pounds each. Minor inaccuracies may occur, with each “1” shifting the arrival point by 10% of the total distance.",
                },
                {
                    "name": "50 yards/meters",
                    "description": "Praapti is the power of instantaneous travel. Indian Sadhana practitioners developed this Path to match their mysterious Asian rivals, who have the power to travel instantly along lines of mystical force. Later, turncoat sadhus sold the secret of this Path to the Tremere, who reverse-engineered it into what they call the Path of Mercury. A handful of New Age Anarchs have also stumbled onto the secret of this path, which they simply call Teleportation. Individual levels of this Path do not have distinct effects; instead, higher mastery simply indicates a farther distance that can be traveled. Ideally, the sorcerer must be able to see the target location or know it intimately. Teleportation is inherently risky and rarely exact, especially when used without clear knowledge of the destination.",
                    "system": "Teleport up to 50 yards/meters. The sorcerer may now cross streets, courtyards, or small buildings in an instant. Familiarity with the destination becomes increasingly important, especially when teleporting without line of sight. Failure has no effect, while botches follow the same dangers as lesser uses, potentially resulting in aggravated damage or becoming embedded in solid objects during blind teleports. Each “1” rolled on a successful activation displaces the sorcerer by 10% of the distance traveled. Successes determine carried mass as normal.",
                },
                {
                    "name": "500 yards/meters",
                    "description": "Praapti is the power of instantaneous travel. Indian Sadhana practitioners developed this Path to match their mysterious Asian rivals, who have the power to travel instantly along lines of mystical force. Later, turncoat sadhus sold the secret of this Path to the Tremere, who reverse-engineered it into what they call the Path of Mercury. A handful of New Age Anarchs have also stumbled onto the secret of this path, which they simply call Teleportation. Individual levels of this Path do not have distinct effects; instead, higher mastery simply indicates a farther distance that can be traveled. Ideally, the sorcerer must be able to see the target location or know it intimately. Teleportation is inherently risky and rarely exact, especially when used without clear knowledge of the destination.",
                    "system": "Teleport up to 500 yards/meters. At this level, Praapti allows traversal across neighborhoods or large structures. Blind teleportation grows significantly more dangerous due to the increased distance involved. Botches may leave the sorcerer grievously wounded or trapped inside walls, floors, or other solid matter, with Fortitude only mitigating damage, not entrapment. Imprecision becomes more noticeable, as small percentage deviations can result in substantial displacement. Successes determine how much additional weight may be carried.",
                },
                {
                    "name": "5 miles/8 kilometers",
                    "description": "Praapti is the power of instantaneous travel. Indian Sadhana practitioners developed this Path to match their mysterious Asian rivals, who have the power to travel instantly along lines of mystical force. Later, turncoat sadhus sold the secret of this Path to the Tremere, who reverse-engineered it into what they call the Path of Mercury. A handful of New Age Anarchs have also stumbled onto the secret of this path, which they simply call Teleportation. Individual levels of this Path do not have distinct effects; instead, higher mastery simply indicates a farther distance that can be traveled. Ideally, the sorcerer must be able to see the target location or know it intimately. Teleportation is inherently risky and rarely exact, especially when used without clear knowledge of the destination.",
                    "system": "Teleport up to 5 miles/8 kilometers. The sorcerer may now cross entire districts or cities in a single instant. Accurate knowledge of the destination is critical; blind teleportation at this range is extremely hazardous. A botch may result in severe aggravated damage or complete entombment within large structures or underground spaces. Even on success, errors in arrival location can be dramatic due to distance scaling. One success transports the sorcerer alone, with each additional success allowing twenty more pounds to accompany them.",
                },
                {
                    "name": "500 miles/800 kilometers",
                    "description": "Praapti is the power of instantaneous travel. Indian Sadhana practitioners developed this Path to match their mysterious Asian rivals, who have the power to travel instantly along lines of mystical force. Later, turncoat sadhus sold the secret of this Path to the Tremere, who reverse-engineered it into what they call the Path of Mercury. A handful of New Age Anarchs have also stumbled onto the secret of this path, which they simply call Teleportation. Individual levels of this Path do not have distinct effects; instead, higher mastery simply indicates a farther distance that can be traveled. Ideally, the sorcerer must be able to see the target location or know it intimately. Teleportation is inherently risky and rarely exact, especially when used without clear knowledge of the destination.",
                    "system": "Teleport up to 500 miles/800 kilometers. Mastery of Praapti permits continental-scale instantaneous travel. Such feats demand precise understanding or absolute familiarity with the destination, as blind teleports are almost suicidal. Botches at this level frequently result in catastrophic outcomes, including lethal damage or permanent entrapment. Even successful teleportation is rarely exact, with each “1” rolled potentially displacing the sorcerer by vast distances. The number of successes strictly limits what may be carried, and insufficient successes may leave possessions—or companions—behind at the Storyteller’s discretion.",
                },
            ],
        },
        {
            "name": "Path of the Focused Mind (Anarch, New Age)",
            "reference": "Rites of the Blood; PG 55 (Rites of the Blood; PG 139)",
            "type": "Thaumaturgy (Anarch, New Age)",
            "powers": [
                {
                    "name": "Readiness",
                    "description": "Using Readiness makes the caster able to gain a quicker \nunderstanding of a predicament. Enhanced lucidity \nenlightens the caster, allowing increased cleverness and \nbetter reactions to changing situations.",
                    "system": "This power is only usable on the thaumaturge \nherself. Every success on the activation roll adds on die \nto a special dice pool for the remainder of the turn. These \ndice may be used on any Wits-related rolls or actions that \nthe thaumaturge performs during this turn. Alternatively, \neach die removed from the dice pool adds one to the \ncaster's initiative rating.",
                },
                {
                    "name": "Centering",
                    "description": "By invoking this power, the thaumaturge causes a \nsudden, intense calmness in the subject by whispering \nsoothing words to her. While under this serenity, the \ntarget is better able to focus on tasks at hand, ignoring \ndistractions and annoyances, including grave bodily harm. \nThaumaturges in fear of frenzy often use this power on \nthemselves to stifle their own emotions and achieve a \nstate of tranquility.",
                    "system": "This power is usable on any one subject within \nearshot of the thaumaturge and lasts for one turn per \nsuccess on the activation roll. During this period, the \ntarget is unaffected by any power or effect (with the \nnotable exception of Elder disciplines) that reduces her \ndice pools. This includes wound penalties, situational \nmodifiers, and Disciplines. Modifications to difficulty \nnumbers still apply during this time, however. In addition, \ndue to the unnatural serenity that this power bestows, \nthe target receives two additional dice in all attempts to \navoid or break frenzy.",
                },
                {
                    "name": "One-Tracked Mind",
                    "description": 'By extending her powers to other individuals, the \nthaumaturge is able to fixate the subject on one action. \nThis single-mindedness of the target is so complete \nthat they ignore everything else that occurs around \nthem. Guards are easily distracted with this power, as \ntheir attention becomes fixated elsewhere, and research \nbecomes a dedicated, focused task. Use of this power \nis sometimes colloquially referred tto as "railroading \nsomeone."',
                    "system": "This power may affect anyone who can hear \nthe thaumaturge. Succesful invocation makes the target \nunable to split any dice pools for multiple actions and \nunable to change tactics after actions have been declared. \nAs a side benefit, the target reduces tthe difficulty of the \ndeclared action by one. Additional actions that the victim \ntakes (from Celeritty, for example) during the duration \nof this power must follow up upon their initial action, \nas they concentrate wholly upon this one idea. If the \ntarget wishes to attempt a different course of action, \nshe must spend a point of Willpower per scene (or per \nturn in combat.) The duration of One-Tracked Mind is \none scene, or one turn per success on the activation roll.",
                },
                {
                    "name": "Dual Thought",
                    "description": "The rigors of learning Thaumaturgy strengthen the \nmind and the will of a thaumaturge. As a result, those \nskilled with Thaumaturgy often have the ability to quickly \nassess a situation and calculate the options available to \nthem. At this level of mastery of the Focused Mind, \nthe thaumaturge is able to divide her attention to two \ncompletely seperate tasks without penalty or distraction. \nAs One-Tracked Mind forces the subject's attenttion into a \nsingle objecttive, Dual Thought expands the thaumaturge's \nconcentration to the point that focus upon two goals is possible.",
                    "system": "Succesful use of Dual Thought allow the \ncaster to take two actions without penalty during her turn. \n(Note that this power specifically lifts the restrictions of \nmultiple actions detailed in V20, P. 248). The extra action \ngranted by this power must be a mental action, whether \nit's the use of Disciplines such as the use of Auspex or \nThaumaturgy, or the contemplation of some problem.\nIf the character is using both actions to solve a problem, \nshe has two seperate dice pools to draw from. These two \nactions happen at the same time, as determined by the \ninitiative rating of the character. You may not use the \nextra action to re-cast Dual Thought.",
                },
                {
                    "name": "Perfect Clarity",
                    "description": "Perfect Clarity brings about a Zen-like moment of \nfocused insight for the thaumaturge as she gains a brief, \nperfect understanding of herself, the universe, and her \nplace within it. This lucidity protects the thaumaturge \nfrom influences both internal and external; even the\nBeast within is unable to rage forth. Thought and action \nbecome one as a complete serenity of the mind descends \nupon the thaumaturge.",
                    "system": "Perfect Clarity lasts for the duration of one \nscene, (or one turn plus an additional turn for every \nsuccess on the activation roll if used while in combat). \nFor this period, the thaumaturge has the difficulties of \nall actions reduced by two. The Kindred is immune to \nfrenzy and Rotschreck from all sources, even supernatural \ntriggers. Finally, any means to control or influence the \nthaumaturge suffer a +2 difficulty, including powers such \nas Presence, Dominate, and Dementation.",
                },
            ],
        },
        {
            "name": "Elemental Mastery (Anarch, Old Skool)",
            "reference": "Rites of the Blood; PG 54 (V20 Core; PG 214)",
            "type": "Thaumaturgy (Anarch, Old Skool)",
            "powers": [
                {
                    "name": "Elemental Strength",
                    "description": "The vampire can draw upon the strength and resilience\r\nof the earth, or of the objects around him, to increase\r\nhis physical prowess without the need for large\r\namounts of blood.",
                    "system": "The player allocates a total of three temporary\r\nbonus dots between the character’s Strength\r\nand Stamina. The number of successes on the roll to\r\nactivate the power is the number of turns these dots\r\nremain. The player may spend a Willpower point to\r\nincrease this duration by one turn. This power cannot\r\nbe “stacked” — one application must expire before the\r\nnext can be made.",
                },
                {
                    "name": "Wooden Tongues",
                    "description": "A vampire may speak, albeit in limited fashion, with\r\nthe spirit of any inanimate object. The conversation\r\nmay not be incredibly interesting, as most rocks and\r\nchairs have limited concern for what occurs around\r\nthem, but the vampire can get at least a general impression\r\nof what the subject has “experienced.” Note\r\nthat events which are significant to a vampire may not\r\nbe the same events that interest a lawn gnome.",
                    "system": "The number of successes dictates the amount\r\nand relevance of the information that the character receives.\r\nOne success may yield a boulder’s memory of a\r\nforest fire, while three may indicate that it remembers\r\na shadowy figure running past, and five will cause the\r\nrock to relate a precise description of a local Gangrel.",
                },
                {
                    "name": "Animate the Unmoving",
                    "description": "Objects affected by this power move as the vampire\r\nusing it dictates. An object cannot take an action that\r\nwould be completely inconceivable for something with\r\nits form — for instance, a door could not leap from\r\nits hinges and carry someone across a street. However,\r\nseemingly solid objects can become flexible within reason:\r\nBarstools can run with their legs, guns can twist\r\nout of their owners’ hands or fire while holstered, and\r\nhumanoid statues can move like normal humans.",
                    "system": "This power requires the expenditure of a\r\nWillpower point with less than four successes on the\r\nroll. Each use of this power animates one object no\r\nlarger than human-sized; the caster may simultaneously\r\ncontrol a number of animate objects equal to his Intelligence\r\nrating. Objects animated by this power stay\r\nanimated as long as they are within the caster’s line of\r\nsight or up to an hour, although the thaumaturge can\r\ntake other actions during that time.",
                },
                {
                    "name": "Elemental Form",
                    "description": "The vampire can take the shape of any inanimate\r\nobject of a mass roughly equal to her own. A desk, a\r\nstatue, or a bicycle would be feasible, but a house or a\r\npen would be beyond this power’s capacity.",
                    "system": "The number of successes determines how\ncompletely the character takes the shape she wishes\nto counterfeit. At least three successes are required for the character to use her senses or Disciplines while in\r\nher altered form. This power lasts for the remainder of\r\nthe night, although the character may return to her\r\nnormal form at will.",
                },
                {
                    "name": "Summon Elemental",
                    "description": "A vampire may summon one of the traditional spirits\r\nof the elements: a salamander (fire), a sylph (air),\r\na gnome (earth), or an undine (water). Some thaumaturges\r\nclaim to have contacted elemental spirits of\r\nglass, electricity, blood, and even atomic energy, but\r\nsuch reports remain unconfirmed (even as their authors\r\nare summoned to Vienna for questioning). The\r\ncaster may choose what type of elemental he wishes to\r\nsummon and command.",
                    "system": "The character must be near some quantity\nof the classical element corresponding to the spirit\nhe wishes to invoke. The spirit invoked may or may\nnot actually follow the caster’s instructions once summoned,\nbut generally will at least pay rough attention\nto what it’s being told to do. The number of successes\ngained on the Willpower roll determines the power\nlevel of the elemental.\nThe elemental has three dots in all Physical and\nMental Attributes. One dot may be added to one of\nthe elemental’s Physical Attributes for each success\ngained by the caster on the initial roll. The Storyteller\nshould determine the elemental’s Abilities, attacks,\nand damage, and any special powers it has related to\nits element.\nOnce the elemental has been summoned, the thaumaturge\nmust exert control over it. The more powerful\nthe elemental, the more difficult a task this is. The\nplayer rolls Manipulation + Occult (difficulty of the\nnumber of successes scored on the casting roll + 4),\nand the number of successes determines the degree of\ncontrol:\nSuccesses Result\nBotch The elemental immediately attacks\nthe thaumaturge.\nFailure The elemental goes free and may\nattack anyone or leave the scene\nat the Storyteller’s discretion.\n1 success The elemental does not attack its\nsummoner.\n2 successes The elemental behaves favorably\ntoward the summoner and may\nperform a service in exchange forpayment (determined by the\r\nStoryteller).\r\n3 successes The elemental performs one service,\r\nwithin reason.\r\n4 successes The elemental performs any one task\r\nfor the caster that does not jeopardize\r\nits own existence.\r\n5 successes The elemental performs any task that\r\nthe caster sets for it, even one that\r\nmay take several nights to complete\r\nor that places its existence at risk. payment (determined by the\r\nStoryteller).\r\n3 successes The elemental performs one service,\r\nwithin reason.\r\n4 successes The elemental performs any one task\r\nfor the caster that does not jeopardize\r\nits own existence.\r\n5 successes The elemental performs any task that\r\nthe caster sets for it, even one that\r\nmay take several nights to complete\r\nor that places its existence at risk.",
                },
            ],
        },
        {
            "name": "Green Path (Anarch, Old Skool)",
            "reference": "Rites of the Blood; PG 54 (V20 Core; PG 215)",
            "type": "Thaumaturgy (Anarch, Old Skool)",
            "powers": [
                {
                    "name": "Herbal Wisdom",
                    "description": "With a touch, a vampire can commune with the\r\nspirit of a plant. Conversations held in this manner are\r\noften cryptic but rewarding — the wisdom and experience\r\nof the spirits of some trees surpasses that of the\r\noracles of legend. Crabgrass, on the other hand, rarely\r\nhas much insight to offer, but might reveal the appearance\r\nof the last person who trod upon it.",
                    "system": "The number of successes rolled determines\r\nthe amount of information that can be gained from the\r\ncontact. Depending on the precise information that\r\nthe vampire seeks, the Storyteller might require the\r\nplayer to roll Intelligence + Occult in order to interpret\r\nthe results of the communication.\r\nSuccesses Result\r\n1 success Fleeting cryptic impressions\r\n2 successes One or two clear images\r\n3 successes A concise answer to a simple query\r\n4 successes A detailed response to one or more\r\ncomplex questions\r\n5 successes The sum total of the plant-spirit’s\r\nknowledge on a given subject",
                },
                {
                    "name": "Speed the Seasons Passing",
                    "description": "This power allows a thaumaturge to accelerate a plant’s\r\ngrowth, causing roses to bloom in a matter of minutes or\r\ntrees to shoot up from saplings overnight. Alternately,\r\nshe can speed a plant’s death and decay, withering grass\r\nand crumbling wooden stakes with but a touch.",
                    "system": "The character touches the target plant. The\r\nplayer rolls normally, and the number of successes determines\r\nthe amount of growth or decay. One success\r\ngives the plant a brief growth spurt or simulates the effects\r\nof harsh weather, while three noticeably enlarge\r\nor wither it. With five successes, a full-grown plant\r\nsprings from a seed or crumbles to dust in a few minutes,\r\nand a tree sprouts fruit or begins decaying almost\r\ninstantaneously. If this power is used in combat, three\r\nsuccesses are needed to render a wooden weapon completely\r\nuseless. Two successes suffice to weaken it, while\r\nfive cause it to disintegrate in the wielder’s hand.",
                },
                {
                    "name": "Dance of Vines",
                    "description": "The thaumaturge can animate a mass of vegetation\r\nup to his own size, using it for utilitarian or combat purposes\r\nwith equal ease. Leaves can walk along a desktop,\r\nivy can act as a scribe, and jungle creepers can strangle\r\nopponents. Intruders should beware of Tremere workshops\r\nthat harbor potted rowan saplings.",
                    "system": "Any total amount of vegetation with a mass\r\nless than or equal to the character’s own may be animated\r\nthrough this power. The plants stay active for one turn\r\nper success scored on the roll, and are under the complete\r\ncontrol of the character. If used for combat purposes, the\r\nplants have Strength and Dexterity ratings each equal\r\nto half the character’s Willpower (rounded down) and\r\nBrawl ratings one lower than that of the character.\r\nDance of Vines cannot make plants uproot themselves\r\nand go stomping about. Even the most energetic\r\nvegetation is incapable of pulling out of the soil and\r\nwalking under the effect of this power. However, 200\r\npounds (100 kilograms) of kudzu can cover a considerable\r\narea all by itself….",
                },
                {
                    "name": "Verdant Haven",
                    "description": "This power weaves a temporary shelter out of a sufficient\r\namount of plant matter. In addition to providing physical\r\nprotection from the elements (and even sunlight), the\r\nVerdant Haven also establishes a mystical barrier which\r\nis nearly impassable to anyone the caster wishes to exclude.\r\nA Verdant Haven appears as a six-foot-tall (twometer-\r\ntall) hemisphere of interlocked branches, leaves, and vines with no discernible opening, and even to the\r\ncasual observer it appears to be an unnatural construction.\r\nVerdant Havens are rumored to have supernatural\r\nhealing properties, hut no Kindred have reported experiencing\r\nsuch benefits from a stay in one.",
                    "system": "A character must be standing in a heavily\r\nvegetated area to use this power. The Verdant Haven\r\nsprings up around the character over the course of three\r\nturns. Once the haven is established, anyone wishing\r\nto enter the haven without the caster’s permission\r\nmust achieve more than the caster’s original number of\r\nsuccesses on a single roll of Wits + Survival (difficulty\r\nequal to the caster’s Willpower). The haven lasts until\r\nthe next sunset, or until the caster dispels or leaves it.\r\nIf the caster scored four or more successes, the haven is\r\nimpenetrable to sunlight unless physically breached.",
                },
                {
                    "name": "Awaken the Forest Giants",
                    "description": "Entire trees can be animated by a master of the\r\nGreen Path. Ancient oaks can be temporarily given\r\nthe gift of movement, pulling their roots from the soil\r\nand shaking the ground with their steps. While not as\r\nversatile as elementals or other summoned spirits, trees\r\nbrought to ponderous life via this power display awesome\r\nstrength and resilience.",
                    "system": "The character touches the tree to be animated.\r\nThe player spends a blood point and rolls normally.\r\nIf the roll succeeds, the player must spend a blood\r\npoint for every success. The tree stays animated for one\r\nturn per success rolled; once this time expires, the tree\r\nputs its roots down wherever it stands and cannot be\r\nanimated again until the next night. While animated,\r\nthe tree follows the character’s verbal commands to\r\nthe best of its ability. An animated tree has Strength\r\nand Stamina equal to the caster’s Thaumaturgy rating,\r\nDexterity 2, and a Brawl rating equal to the caster’s\r\nown. It is immune to bashing damage, and all lethal\r\ndamage dice pools are halved due to its size.\r\nOnce the animating energy leaves a tree, it puts\r\ndown roots immediately, regardless of what it is currently\r\nstanding on. A tree re-establishing itself in the\r\nsoil can punch through concrete and asphalt to find\r\nnourishing dirt and water underneath, meaning that it\r\nis entirely possible for a sycamore to root itself in the\r\nmiddle of a road without any warning.",
                },
            ],
        },
        {
            "name": "Path of Mars (Anarch, Old Skool)",
            "reference": "Rites of the Blood; PG 54 (V20 Core; PG 224)",
            "type": "Thaumaturgy (Anarch, Old Skool)",
            "powers": [
                {
                    "name": "War Cry",
                    "description": "A vampire on the attack can focus his will, making\nhim less susceptible to battle fear or the powers of the\nundead. The vampire shouts a primal scream to start the\neffect, though some thaumaturges have been known to\npaint their faces or cut themselves open instead.",
                    "system": "For the duration of one scene, the vampire\nadds one to his Courage Trait. Additionally, for the\npurposes of hostile effects, his Willpower is considered\nto be one higher (though this bonus applies only to the\nTrait itself, not the Willpower pool). A character may\nonly gain the benefits of War Cry once per scene.",
                },
                {
                    "name": "Strike True",
                    "description": "The vampire makes a single attack, guided by the\nunholy power of her Blood. This attack strikes its foe\ninfallibly.",
                    "system": "By invoking this power, the player need\nnot roll to see if the vampire’s attack hits — it does,\nautomatically. Only Melee or Brawl attacks may be\nmade in this manner. These attacks are considered to\nbe one-success attacks; they offer no additional damage\ndice. Also, they may be dodged, blocked, or parried\nnormally, and the defender needs only one success (as\nthe attacks’ number of success is assumed to be one).\nStrike True has no effect if attempted on multiple attacks\n(dice pool splits) in a single turn from one character.",
                },
                {
                    "name": "Wind Dance",
                    "description": "The thaumaturge invokes the power of the winds,\nmoving in a blur. She gains a preternatural edge in\navoiding her enemies’ blows, moving out of their way\nbefore the enemy has a chance to throw them.",
                    "system": "The player can dodge any number of attacks\nwith her full dice pool in a single turn. This advantage\napplies only to dodges — if the character wishes to attack\nand dodge, the player must still split her dice pool.\nThis power lasts for one scene.",
                },
                {
                    "name": "Fearless Heart",
                    "description": "The vampire temporarily augments his abilities as a\nwarrior. Through the mystical powers of blood magic,\nthe character becomes a potent fighting force.",
                    "system": "Fearless Heart grants the vampire an extra\npoint in each of the Physical Attributes (Strength,\nDexterity, and Stamina). These Traits may not exceed\ntheir generational maximums, though the player may\nuse blood points to push the character’s Traits even\nhigher. The effects last for one scene, and a character\nmay gain its benefits only once per scene. The vampire\nmust spend two hours in a calm and restful state following\nthe use of Fearless Heart, or lose a blood point\nevery 15 minutes until he rests.",
                },
                {
                    "name": "Comrades at Arms",
                    "description": "This ability extends the power of the previous abilities\nin the path. It allows any of the earlier effects to be\napplied to a group such as a pack or War Party.",
                    "system": "The player chooses one of the lower-level\npowers in the path, invoking it as normal. Afterward,\nhe touches another character and (if the roll for Comrades\nat Arms is successful) bestows the benefit on her\nas well. The same power may be delivered to any number\nof packmates, as long as the rolls for Comrades at\nArms are successful and the thaumaturge pays the appropriate\nblood costs.",
                },
            ],
        },
        {
            "name": "Path of Spirit Manipulation (Anarch, Old Skool)",
            "reference": "Rites of the Blood; PG 54 (Rites of the Blood; PG 142-143)",
            "type": "Thaumaturgy (Anarch, Old Skool)",
            "powers": [
                {
                    "name": "Hermetic Sightt",
                    "description": "The vampire can percieve the spirit world, either by \ngazing deeply into it or by seeing the presence of nearby \nspirits as a hazy overlay on the material world.",
                    "system": "Hermetic Sight allows the thaumaturge to \npercieve the spirit realm interlaid over the material \nworld for one hour. Each additional level of success on \nthe activation roll increases the duration of this power \nby an additional thirty minutes.",
                },
                {
                    "name": "Astral Cant",
                    "description": "The languages of the spirit world are infinitely \nvaried and mainly incomprehensible to mortal (and \nimmortal) minds. Astral Cant does not teach the \nthaumaturge the tongues of the spirits, but it does \nallow him to understand them as they speak to him \nand to reply in their own languages. The use of this \npower is not always necessary; many spirits speak \nhuman tongues, but choose to feign ignorance when \ndealing with vampires. Spirits are not affected by \nDominate, buttt may be manipulated by Presence. Some \nthaumaturges theorize that this is because spirits are \nnot actually sentient as a vampire would understand \nthe concept, but are manifestations based on the \nperception of those that are self-aware.",
                    "system": "Astral Cant allows the thaumaturge to speak to \nany spirit visible via Hermetic Sight for fifteen minutes. \nEach additional level of success on the activation roll \nincreases the duration of this power by an additional \nfifteen minutes to the duration.",
                },
                {
                    "name": "Voice of Command",
                    "description": "This is perhaps the most dangerous power in the \nSpirit Manipulation arsenal, for the consequences \nof failure can be particularly unpleasant. Voice of \nCommand allows the thaumaturge to issue orders to \na spirit, compelling it to heed her bidding whether or \nnot it desires to do so. \nSpirits compelled by this power are fully aware that \nthey are being forced into these actions, and may well \nseek revenge on their erstwhile masters at a later time. \nThaumaturges who issue commands above and beyond \nwhat their spirit servants are compelled to perform may \nfind themselves ignored or mocked. A trickster spirit \nmay agree to a situation to follow orders only to betray \nits master, leaving the thaumaturge in a situation of \npotentially fatal embarressment.",
                    "system": "The thaumaturge makes the normal opposed \nWillpower roll against the spirit. The target spirit \nresists with Willpower (difficulty of the thaumaturge's \nManipulation + Occult). The degree of success the \nthaumaturge attains determines the complexity and \nseverity of the command that she can issue.",
                },
                {
                    "name": "Entrap Ephemera",
                    "description": "This power allows a thaumaturge to bind a spirit into \na physical object. This can be done to imprison the \ntarget, but is more often performed to create a fettish - an \nartifact that grants mystical benefits powered by the spirit. \nFetishes created by this power are often unreliable and \nunderstandably displeased with their situation and will \ntake any opportunity to escape or thwartt their captors. \nLupines find it offensive f or vampires to possess a fetish, \nand often will frenzy simply at the sight of a vampire \nwielding one.",
                    "system": "The thaumaturge must first locate a vessel \nsymbolically aligned with the targeted spirit that will \neventually become the fetish. Then she must command \nthe targeted spirit to enter the vessel via an opposed \nWillpower roll. The target spirit resists with Willpower \n(difficulty equals the thaumaturge's Manipulation + \nOccult).\nShould the thaumaturge succeed, she can create a fetish \nof a power level based on the number of successes achieved \nover the spirit, up to a level five fetish. For example, if the \nthaumaturge wins the opposed Willpower roll against the \nspirit by three successes, she creates a level three fetish.\n\nCreating and maintaining a fetish is difficult; because of \nthis, the number of fetishes a thaumaturge may creatte is \nlimited by her Willpower. If the thaumaturge gives away \nsaid fetish, it still counts against her total available slots. \nShe may only create an additional fetish when one of \nher previous fetishes has been destroyed. \nA fetish grants a number of bonus dice to a specific \nskill comparable to the level of the fetish. For example, \na healing spirit trapped inside a scalpel would grant \nexttra dice (the level of the fetish) for any Medicine roll. \nThe Storyteller always has final authority on what sort \nof fetish can be made. \nA fettish is activatted by rolling the user's Willpower \n(difficulty equals the Fetish's power level + 3). A botch \non this roll destroys the physical component of the fetish \nand frees the spirit that was trapped within.",
                },
                {
                    "name": "Duality",
                    "description": "The thaumaturge can now fully interact with the spirit \nworld - a strange place that only sometimes resembles \nthe real world. While using this power, she exists on \nboth planes of existence at once. She is able to pick up \nobjects in the physical world and place them in the spirit \nworld and vice versa. Beings and landscape features in \nboth realms are solid to her, and she can engage in any \nmanner of interaction. She can even use Thaumaturgy \nand other Disciplines in either world. This is not without \nits dangers. With a single misstep, the vampire can find \nhimself trapped in the spirit realm with no way to return \nhome. Several incautious thaumaturges have starved into \ntorpor while trapped on the other side of the barrier that \nseperates the physical and spirit realms.",
                    "system": "The thaumaturge may interact with the spirit \nworld for fifteen minutes. Each additional level of \nsuccess on the activation roll increases the duration of \nthis power by an additional fifteen minutes. Duality can \nonly be enacted while the character begins the process in \nthe physical world. While in this state, the thaumaturge \nbecomes susceptible to attacks from both realms and \nsuffers a +1 difficulty to all Perception rolls. The \ncharacter is still considered to be in the physical world \nfor purposes of basic physics (and common sense).\nSpirits who have been previously angered will seek \nphysical revenge on unwary thaumaturges using this power. \nA botch on the roll to activate this power tears the \nvampire out of the physical world and traps him in the \nspirit realm. The way back to the physical realm, if there is \none, is left to the Storyteller's discretion, and may spark \nan entirely new story.",
                },
            ],
        },
        {
            "name": "Path of the Evil Eye (Anarch, Old Skool)",
            "reference": "Rites of the Blood; PG 54",
            "type": "Thaumaturgy (Anarch, Old Skool)",
            "powers": [
                {
                    "name": "Humiliation",
                    "description": "The simplest application of the Evil Eye causes the target \nto embarrass himself in some public way. Possible results \ninclude saying something embarrassing in front of one’s \npeers, failing disastrously at a feeding attempt, or simply \nripping the seat out of one’s pants while in a crowded bar.",
                    "system": "Each success represents one night during which \nthe target is affected by the curse. The curse triggers \nonce per night at a time of the Storyteller’s choosing, \nusually the scene during which the character is in front \nof the largest number of individuals or in which he is in \nfront of the largest number of socially important people. \nThat is, it may trigger while the character is in a crowded \nrestaurant or when he is alone with the Prince, whichever \nhas the greatest potential for personal embarrassment. \nThe Storyteller determines when the curse triggers, but \nit should do so at least once per night. \nDuring the trigger scene, on every Social roll made for \nthe character, the player must add a number of automatic \n1s equal to the sorcerer’s rating in the Path of the Evil Eye, \nthereby increasing the likelihood of a botch on a Social \nroll. In addition, during the trigger scene, the Storyteller \nshould roll a number of dice equal to the sorcerer’s rating \nin this path (difficulty 5). Successes mean that some \nexternal event happens that causes embarrassment to \nthe character, such as a waiter spilling drinks on him or \na car splashing him with mud.",
                },
                {
                    "name": "Loss",
                    "description": "This curse affects the target’s material worth. It most \ncommonly causes the target to be stripped of money, but it \nmay also cause her Herd to diminish, or destroy a Haven. \nThe curse can target any tangible asset represented as a \nBackground. If the character has no suitable Backgrounds, \nit targets personal items of emotional significance.",
                    "system": "Within one week, the target loses one dot \nfrom an appropriate Background. Generally, the curse \npreferentially attacks Resources over other backgrounds, but theoretically any form of tangible Background representing a personal asset can be a valid target. The sorcerer has no control over how the Background point is lost or even which Background point is lost. The Storyteller may even choose to decide randomly.",
                },
                {
                    "name": "Peril",
                    "description": "At this level of mastery, the ashipu may finally endanger \nher enemy rather than merely inconvenience her. The \ncurse cannot directly harm the target, but it can create \na situation in which it is possible for her to be harmed, \nwhether at the hands of a drunken lout who takes offense \nto the target’s manner at a bar or a pack of werewolves \nwho, by happenstance, choose to board the same lonely \nsubway car as the victim.",
                    "system": "The number of successes determines how many nights the character is at risk. At the start of each night, the Storyteller must roll a die and, depending on the results, fashion an encounter for the targeted character. \nDice Result Nature of Peril\n 1-3  None. The curse does not trigger during this \n      night.\n 4-6  Minor: An encounter which is not likely to \n    harm the character but which has a chance \n    to do so. A mortal tries to mug the character \n    while she is in front of mortals, or simply \n    tries to hold up a convenience store while \n    the character is in line paying for gas. A \n    bar patron takes offense to something the \n    character does or says and tries to pick a \n    fight.\n 7-8  Moderate: An encounter with a significant \n    likelihood of at least some harm to the \n    character. The character is involved in a \n    car wreck or struck by a hit-and-run driver. \n    Stairs give way while the character is \n     climbing them.\n 9  Severe: An encounter in which the \n    character is almost certain to suffer some \n    lethal damage. The character inadvertently \n    says something offensive that provokes \n    frenzy rolls in nearby vampires. The \n    building collapses while the character is in \n    it or a fire breaks out.\n 10  Catastrophic: An encounter that is potentially deadly.    The character’s is locked out of his haven during the    day. The character unwittingly says something that    offends a pack of nearby Lupines.\n\n Nights on which there is no peril do not count against \nthe ashipu’s successes; the curse will continue until the \ntarget has suffered a number of dangerous encounters \nequal to the successes or the curse is lifted. During any \ndangerous encounter, a targeted character has a chance \nto realize she is under a curse (if she didn’t already know \nit). The roll is Intelligence + Occult. The default difficulty is 9, but it drops to 8 if the character has Auspex or to 6 if the character has any knowledge of this Path.",
                },
                {
                    "name": "Enemy",
                    "description": "This potent curse causes the target’s friends and allies \nto turn against him, even as it causes the numbers of his \nenemies to grow.",
                    "system": "For each success on the Willpower roll, the \ntarget loses one dot of Allies, Contacts, Influence, or \nRetainers. This may reflect friends and allies who have \nbecome angry with the character and turn their back on \nhim, it may reflect contacts and allies who are simply \nunavailable for a time, or it may actually result in such \ncharacters being injured or even dying due to ill fortune. \nAlternatively, the player may choose to spend some or all of the successes to give the target a new Enemy (as per the Enemy Flaw) who arrives to pursue a vendetta against the character. Regardless, the effects manifest within a week, and the player of the targeted character may neither regain lost Backgrounds nor remove the Enemy Flaw without learning about and neutralizing the curse.",
                },
                {
                    "name": "The Eye that Wounds",
                    "description": "The ultimate expression of this malefic path, the \nEye That Wounds does not require time to establish a \nchain of ill fortune. It strikes immediately. The ashipu \nmust make eye contact with her target and utter some \nexclamation pertaining to a characteristic of his. It can \nbe praise or insult, sarcasm or fury, but whatever form it \ntakes, the target is immediately struck with an agonizing \ninjury that damages that characteristic.",
                    "system": "While the curse allows for flexibility, the default \nassumption is that for every two successes (rounded up), the target (or object, if the curse is directed towards a possession of the target) suffers one level of aggravated damage. Generally, even a single level of damage is sufficient to slay an animal or destroy most objects. If used against a mortal, this power will permanently maim him. If used against a Kindred, the curse will inflict damage shaped by the ashipu’s words. If she compliments his beautiful eyes, they will be burned and he might be rendered blind until he can heal. If she mocks his honeyed words, the curse might burn out his tongue and leave him unable to speak. This curse may be transmitted through an effigy, but the normal difficulty penalty imposed for using an effigy increases by +2 (see Principles of Contagion and Sympathy on pp. 133-135).",
                },
            ],
        },
        {
            "name": "Vodoun Necromancy (Anarch, Old Skool)",
            "reference": "Rites of the Blood; PG 54 (Rites of the Blood; PG 166)",
            "type": "Thaumaturgy (Anarch, Old Skool)",
            "powers": [
                {
                    "name": "Touch of Life",
                    "description": "The wangateur may ingest a special mixture of herbs\r\nand powders in lieu of expending blood when trying to\r\nimitate the characteristics of the living. The effect lasts\r\nfor one scene. The wangateur may ingest this mixture\r\nfor himself or provide it to another Kindred (but not a\r\nmortal) who must swallow the mixture during that scene.\r\nIn the latter case, the wangateur decides which aspect of\r\nthe living the other Kindred will imitated.",
                    "system": "",
                },
                {
                    "name": "Strength of Root and Stone",
                    "description": "The wangateur may inhale a mixture of herbs and\r\npowders through the nose instead of expending blood\r\nwhen trying to augment a Physical Attribute. The effect is\r\nthe same as if the vampire had spent one point of blood\r\nto improve a Physical Attribute. The effect lasts for one\r\nscene. The wangateur may use this mixture himself or\r\nprovide it for another (including a mortal). If it is to be\r\nused by another, the wangateur decides which Attribute\r\nis to be augmented when the mixture is prepared.",
                    "system": "",
                },
                {
                    "name": "Breath of Life",
                    "description": "The wangateur may use a mixture of herbs and powders\r\nin place of blood when trying to heal herself. The specific\r\nmixture produces a paste which the wangateur must physically\r\nsmear on the area to be healed. The effect is the same as if\r\nthe vampire had spent one point of blood to repair physical\r\ndamage. This power cannot be used to heal aggravated damage,\r\nonly bashing or lethal. The wangateur may use this mixture\r\nfor himself or for another (including a mortal).",
                    "system": "",
                },
                {
                    "name": "Favor of the Orishas",
                    "description": "The wangateur may use a mixture of herbs and powders\r\nin order to fuel any Discipline (including blood magic)\r\nthat requires exactly one point of blood to function.\r\nThis formula also requires a small quantity of blood to\r\nfunction, but it need not come from the wangateur and,\r\nin fact, can come from an enemy (human or Kindred) who\r\nhas shed blood nearby. The wangateur may only use this\r\nmixture on herself and must make a superficial cut on\r\nher arm and then rub the mixture into the open wound.",
                    "system": "",
                },
                {
                    "name": "Gift of Ashe",
                    "description": "The wangateur may now create mixtures using the first\r\nthree levels of this path which will maintain their efficacy\r\nfor an entire night rather than just one turn or scene.\r\nFurthermore, the wangateur can maintain a number of\r\nmixtures up to his Intelligence simultaneously. Thus, he\r\ncan provide the mixtures to allies and no longer needs to be\r\nnearby in order to provide the appropriate benefits — he can\r\nsimply give the mixture to an ally and send her on her way.",
                    "system": "",
                },
            ],
        },
        {
            "name": "Weather Control (Anarch, Old Skool)",
            "reference": "Rites of the Blood; PG 54 (V20 Core; PG 228)",
            "type": "Thaumaturgy (Anarch, Old Skool)",
            "powers": [
                {
                    "name": "Fog & Minor Temperature Change",
                    "description": "Command over the weather has long been a staple\npower of wizards both mortal and immortal, and this\npath is said to predate the Tremere by millennia. The\nproliferation of usage of this path outside the Clan tends\nto confirm this theory; Weather Control is quite common\noutside the Tremere, and even outside the Camarilla.\nLower levels of this path allow subtle manipulations,\nwhile higher stages of mastery allow a vampire to\ncall up raging storms. The area affected by this power is\nusually rather small, no more than three or four miles\n(five to six kilometers) in diameter, and the changes\nthe power wreaks are not always immediate.",
                    "system": "The number of successes rolled indicates how long it takes the weather magic to take effect. One success indicates an entire day may pass before the weather changes to the thaumaturge’s liking, while a roll with five successes brings an almost instant effect. The difficulty of the Willpower roll necessary to invoke\nthis power may change depending on the current local weather conditions and the weather the character is attempting to create. The Storyteller should impose a bonus (-1 or -2 difficulty) for relatively minor shifts, such as clearing away a light drizzle or calling lightning when a severe thunderstorm is already raging.\nConversely, a penalty (+1 or +2 difficulty) should be applied when the desired change is at odds with the current conditions, such as summoning the same light drizzle in the middle of the Sahara Desert or calling down lightning from a cloudless sky. If the character tries to strike a specific target with lightning, the player must roll Perception + Occult (difficulty 6 if the target is standing in open terrain, 8 if he is under shelter, or 10 if he is inside but near a window) in addition to the base roll to use Thaumaturgy. \nOtherwise the bolt goes astray, with the relative degree of failure of the roll determining where exactly the lightning strikes. Effects of the power default to the maximum area available unless the caster states that he’s attempting to affect a smaller area. At Storyteller discretion, an additional Willpower roll (difficulty 6) may be required to keep the change in the weather under control. Weather Control is not the sort of power that lends itself well to indoor application. While certain of the path’s uses (changes of temperature, high winds, and possibly even fog) do make a certain amount of sense in interior settings, others (precipitation of any sort, lightning) don’t. The difficulty for all rolls to use Weather Control indoors is at +2, and the Storyteller should feel free to disallow any proposed uses that don’t make sense.\nIndividual power descriptions are not provided for this path, as the general principle is fairly consistent. Instead, the strongest weather phenomenon possible at\neach level is listed. \n• Fog: Vision is slightly impaired and sounds are muffled; a +1 difficulty is imposed on all Perception rolls that involve sight and hearing, and the effective range of all ranged attacks are halved. Light breeze: A +1 difficulty is\nimposed on all Perception rolls that involve smell.\nMinor temperature change: It is possible to raise or lower the local temperature by up to 10 degrees Fahrenheit or 5 degrees Celsius.\n•• Rain or snow: As Fog, but Perception rolls are impaired to a much greater extent; the difficulty modifier for all such rolls rises to +2. In addition, the difficulty on all Drive rolls increases by two.\n••• High Winds: The wind speed rises to around 30 miles per hour or 50 kilometers per hour, with gusts of up to twice that. Ranged attacks are much more difficult: + 1 to firearm attacks and +2 to thrown weapons and archery. In addition, during fierce gusts, Dexterity rolls (difficulty 6) may be required to keep characters from being knocked over by the winds. When gale-force winds are in effect, papers go flying, objects get picked up by the winds and hurled with abandon, and other suitably cinematic effects are likely. \nModerate temperature change: The local temperature can be raised or lowered by up to 20 degrees Fahrenheit or 10 degrees Celsius.\n•••• Storm: This has the effects of both Rain and High Winds.\n••••• Lightning Strike: This attack inflicts 10 dice of lethal damage. Body armor does not add to the target’s dice pool to soak this attack.",
                },
                {
                    "name": "Rain or Snow",
                    "description": "Command over the weather has long been a staple\npower of wizards both mortal and immortal, and this\npath is said to predate the Tremere by millennia. The\nproliferation of usage of this path outside the Clan tends\nto confirm this theory; Weather Control is quite common\noutside the Tremere, and even outside the Camarilla.\nLower levels of this path allow subtle manipulations,\nwhile higher stages of mastery allow a vampire to\ncall up raging storms. The area affected by this power is\nusually rather small, no more than three or four miles\n(five to six kilometers) in diameter, and the changes\nthe power wreaks are not always immediate.",
                    "system": "The number of successes rolled indicates how long it takes the weather magic to take effect. One success indicates an entire day may pass before the weather changes to the thaumaturge’s liking, while a roll with five successes brings an almost instant effect. The difficulty of the Willpower roll necessary to invoke\nthis power may change depending on the current local weather conditions and the weather the character is attempting to create. The Storyteller should impose a bonus (-1 or -2 difficulty) for relatively minor shifts, such as clearing away a light drizzle or calling lightning when a severe thunderstorm is already raging.\nConversely, a penalty (+1 or +2 difficulty) should be applied when the desired change is at odds with the current conditions, such as summoning the same light drizzle in the middle of the Sahara Desert or calling down lightning from a cloudless sky. If the character tries to strike a specific target with lightning, the player must roll Perception + Occult (difficulty 6 if the target is standing in open terrain, 8 if he is under shelter, or 10 if he is inside but near a window) in addition to the base roll to use Thaumaturgy. \nOtherwise the bolt goes astray, with the relative degree of failure of the roll determining where exactly the lightning strikes. Effects of the power default to the maximum area available unless the caster states that he’s attempting to affect a smaller area. At Storyteller discretion, an additional Willpower roll (difficulty 6) may be required to keep the change in the weather under control. Weather Control is not the sort of power that lends itself well to indoor application. While certain of the path’s uses (changes of temperature, high winds, and possibly even fog) do make a certain amount of sense in interior settings, others (precipitation of any sort, lightning) don’t. The difficulty for all rolls to use Weather Control indoors is at +2, and the Storyteller should feel free to disallow any proposed uses that don’t make sense.\nIndividual power descriptions are not provided for this path, as the general principle is fairly consistent. Instead, the strongest weather phenomenon possible at\neach level is listed. \n• Fog: Vision is slightly impaired and sounds are muffled; a +1 difficulty is imposed on all Perception rolls that involve sight and hearing, and the effective range of all ranged attacks are halved. Light breeze: A +1 difficulty is\nimposed on all Perception rolls that involve smell.\nMinor temperature change: It is possible to raise or lower the local temperature by up to 10 degrees Fahrenheit or 5 degrees Celsius.\n•• Rain or snow: As Fog, but Perception rolls are impaired to a much greater extent; the difficulty modifier for all such rolls rises to +2. In addition, the difficulty on all Drive rolls increases by two.\n••• High Winds: The wind speed rises to around 30 miles per hour or 50 kilometers per hour, with gusts of up to twice that. Ranged attacks are much more difficult: + 1 to firearm attacks and +2 to thrown weapons and archery. In addition, during fierce gusts, Dexterity rolls (difficulty 6) may be required to keep characters from being knocked over by the winds. When gale-force winds are in effect, papers go flying, objects get picked up by the winds and hurled with abandon, and other suitably cinematic effects are likely. \nModerate temperature change: The local temperature can be raised or lowered by up to 20 degrees Fahrenheit or 10 degrees Celsius.\n•••• Storm: This has the effects of both Rain and High Winds.\n••••• Lightning Strike: This attack inflicts 10 dice of lethal damage. Body armor does not add to the target’s dice pool to soak this attack.",
                },
                {
                    "name": "High Winds & Moderate Temperature Change",
                    "description": "Command over the weather has long been a staple\npower of wizards both mortal and immortal, and this\npath is said to predate the Tremere by millennia. The\nproliferation of usage of this path outside the Clan tends\nto confirm this theory; Weather Control is quite common\noutside the Tremere, and even outside the Camarilla.\nLower levels of this path allow subtle manipulations,\nwhile higher stages of mastery allow a vampire to\ncall up raging storms. The area affected by this power is\nusually rather small, no more than three or four miles\n(five to six kilometers) in diameter, and the changes\nthe power wreaks are not always immediate.",
                    "system": "The number of successes rolled indicates how long it takes the weather magic to take effect. One success indicates an entire day may pass before the weather changes to the thaumaturge’s liking, while a roll with five successes brings an almost instant effect. The difficulty of the Willpower roll necessary to invoke\nthis power may change depending on the current local weather conditions and the weather the character is attempting to create. The Storyteller should impose a bonus (-1 or -2 difficulty) for relatively minor shifts, such as clearing away a light drizzle or calling lightning when a severe thunderstorm is already raging.\nConversely, a penalty (+1 or +2 difficulty) should be applied when the desired change is at odds with the current conditions, such as summoning the same light drizzle in the middle of the Sahara Desert or calling down lightning from a cloudless sky. If the character tries to strike a specific target with lightning, the player must roll Perception + Occult (difficulty 6 if the target is standing in open terrain, 8 if he is under shelter, or 10 if he is inside but near a window) in addition to the base roll to use Thaumaturgy. \nOtherwise the bolt goes astray, with the relative degree of failure of the roll determining where exactly the lightning strikes. Effects of the power default to the maximum area available unless the caster states that he’s attempting to affect a smaller area. At Storyteller discretion, an additional Willpower roll (difficulty 6) may be required to keep the change in the weather under control. Weather Control is not the sort of power that lends itself well to indoor application. While certain of the path’s uses (changes of temperature, high winds, and possibly even fog) do make a certain amount of sense in interior settings, others (precipitation of any sort, lightning) don’t. The difficulty for all rolls to use Weather Control indoors is at +2, and the Storyteller should feel free to disallow any proposed uses that don’t make sense.\nIndividual power descriptions are not provided for this path, as the general principle is fairly consistent. Instead, the strongest weather phenomenon possible at\neach level is listed. \n• Fog: Vision is slightly impaired and sounds are muffled; a +1 difficulty is imposed on all Perception rolls that involve sight and hearing, and the effective range of all ranged attacks are halved. Light breeze: A +1 difficulty is\nimposed on all Perception rolls that involve smell.\nMinor temperature change: It is possible to raise or lower the local temperature by up to 10 degrees Fahrenheit or 5 degrees Celsius.\n•• Rain or snow: As Fog, but Perception rolls are impaired to a much greater extent; the difficulty modifier for all such rolls rises to +2. In addition, the difficulty on all Drive rolls increases by two.\n••• High Winds: The wind speed rises to around 30 miles per hour or 50 kilometers per hour, with gusts of up to twice that. Ranged attacks are much more difficult: + 1 to firearm attacks and +2 to thrown weapons and archery. In addition, during fierce gusts, Dexterity rolls (difficulty 6) may be required to keep characters from being knocked over by the winds. When gale-force winds are in effect, papers go flying, objects get picked up by the winds and hurled with abandon, and other suitably cinematic effects are likely. \nModerate temperature change: The local temperature can be raised or lowered by up to 20 degrees Fahrenheit or 10 degrees Celsius.\n•••• Storm: This has the effects of both Rain and High Winds.\n••••• Lightning Strike: This attack inflicts 10 dice of lethal damage. Body armor does not add to the target’s dice pool to soak this attack.",
                },
                {
                    "name": "Storm",
                    "description": "Command over the weather has long been a staple\npower of wizards both mortal and immortal, and this\npath is said to predate the Tremere by millennia. The\nproliferation of usage of this path outside the Clan tends\nto confirm this theory; Weather Control is quite common\noutside the Tremere, and even outside the Camarilla.\nLower levels of this path allow subtle manipulations,\nwhile higher stages of mastery allow a vampire to\ncall up raging storms. The area affected by this power is\nusually rather small, no more than three or four miles\n(five to six kilometers) in diameter, and the changes\nthe power wreaks are not always immediate.",
                    "system": "The number of successes rolled indicates how long it takes the weather magic to take effect. One success indicates an entire day may pass before the weather changes to the thaumaturge’s liking, while a roll with five successes brings an almost instant effect. The difficulty of the Willpower roll necessary to invoke\nthis power may change depending on the current local weather conditions and the weather the character is attempting to create. The Storyteller should impose a bonus (-1 or -2 difficulty) for relatively minor shifts, such as clearing away a light drizzle or calling lightning when a severe thunderstorm is already raging.\nConversely, a penalty (+1 or +2 difficulty) should be applied when the desired change is at odds with the current conditions, such as summoning the same light drizzle in the middle of the Sahara Desert or calling down lightning from a cloudless sky. If the character tries to strike a specific target with lightning, the player must roll Perception + Occult (difficulty 6 if the target is standing in open terrain, 8 if he is under shelter, or 10 if he is inside but near a window) in addition to the base roll to use Thaumaturgy. \nOtherwise the bolt goes astray, with the relative degree of failure of the roll determining where exactly the lightning strikes. Effects of the power default to the maximum area available unless the caster states that he’s attempting to affect a smaller area. At Storyteller discretion, an additional Willpower roll (difficulty 6) may be required to keep the change in the weather under control. Weather Control is not the sort of power that lends itself well to indoor application. While certain of the path’s uses (changes of temperature, high winds, and possibly even fog) do make a certain amount of sense in interior settings, others (precipitation of any sort, lightning) don’t. The difficulty for all rolls to use Weather Control indoors is at +2, and the Storyteller should feel free to disallow any proposed uses that don’t make sense.\nIndividual power descriptions are not provided for this path, as the general principle is fairly consistent. Instead, the strongest weather phenomenon possible at\neach level is listed. \n• Fog: Vision is slightly impaired and sounds are muffled; a +1 difficulty is imposed on all Perception rolls that involve sight and hearing, and the effective range of all ranged attacks are halved. Light breeze: A +1 difficulty is\nimposed on all Perception rolls that involve smell.\nMinor temperature change: It is possible to raise or lower the local temperature by up to 10 degrees Fahrenheit or 5 degrees Celsius.\n•• Rain or snow: As Fog, but Perception rolls are impaired to a much greater extent; the difficulty modifier for all such rolls rises to +2. In addition, the difficulty on all Drive rolls increases by two.\n••• High Winds: The wind speed rises to around 30 miles per hour or 50 kilometers per hour, with gusts of up to twice that. Ranged attacks are much more difficult: + 1 to firearm attacks and +2 to thrown weapons and archery. In addition, during fierce gusts, Dexterity rolls (difficulty 6) may be required to keep characters from being knocked over by the winds. When gale-force winds are in effect, papers go flying, objects get picked up by the winds and hurled with abandon, and other suitably cinematic effects are likely. \nModerate temperature change: The local temperature can be raised or lowered by up to 20 degrees Fahrenheit or 10 degrees Celsius.\n•••• Storm: This has the effects of both Rain and High Winds.\n••••• Lightning Strike: This attack inflicts 10 dice of lethal damage. Body armor does not add to the target’s dice pool to soak this attack.",
                },
                {
                    "name": "Lightning Strike",
                    "description": "Command over the weather has long been a staple\npower of wizards both mortal and immortal, and this\npath is said to predate the Tremere by millennia. The\nproliferation of usage of this path outside the Clan tends\nto confirm this theory; Weather Control is quite common\noutside the Tremere, and even outside the Camarilla.\nLower levels of this path allow subtle manipulations,\nwhile higher stages of mastery allow a vampire to\ncall up raging storms. The area affected by this power is\nusually rather small, no more than three or four miles\n(five to six kilometers) in diameter, and the changes\nthe power wreaks are not always immediate.",
                    "system": "The number of successes rolled indicates how long it takes the weather magic to take effect. One success indicates an entire day may pass before the weather changes to the thaumaturge’s liking, while a roll with five successes brings an almost instant effect. The difficulty of the Willpower roll necessary to invoke\nthis power may change depending on the current local weather conditions and the weather the character is attempting to create. The Storyteller should impose a bonus (-1 or -2 difficulty) for relatively minor shifts, such as clearing away a light drizzle or calling lightning when a severe thunderstorm is already raging.\nConversely, a penalty (+1 or +2 difficulty) should be applied when the desired change is at odds with the current conditions, such as summoning the same light drizzle in the middle of the Sahara Desert or calling down lightning from a cloudless sky. If the character tries to strike a specific target with lightning, the player must roll Perception + Occult (difficulty 6 if the target is standing in open terrain, 8 if he is under shelter, or 10 if he is inside but near a window) in addition to the base roll to use Thaumaturgy. \nOtherwise the bolt goes astray, with the relative degree of failure of the roll determining where exactly the lightning strikes. Effects of the power default to the maximum area available unless the caster states that he’s attempting to affect a smaller area. At Storyteller discretion, an additional Willpower roll (difficulty 6) may be required to keep the change in the weather under control. Weather Control is not the sort of power that lends itself well to indoor application. While certain of the path’s uses (changes of temperature, high winds, and possibly even fog) do make a certain amount of sense in interior settings, others (precipitation of any sort, lightning) don’t. The difficulty for all rolls to use Weather Control indoors is at +2, and the Storyteller should feel free to disallow any proposed uses that don’t make sense.\nIndividual power descriptions are not provided for this path, as the general principle is fairly consistent. Instead, the strongest weather phenomenon possible at\neach level is listed. \n• Fog: Vision is slightly impaired and sounds are muffled; a +1 difficulty is imposed on all Perception rolls that involve sight and hearing, and the effective range of all ranged attacks are halved. Light breeze: A +1 difficulty is\nimposed on all Perception rolls that involve smell.\nMinor temperature change: It is possible to raise or lower the local temperature by up to 10 degrees Fahrenheit or 5 degrees Celsius.\n•• Rain or snow: As Fog, but Perception rolls are impaired to a much greater extent; the difficulty modifier for all such rolls rises to +2. In addition, the difficulty on all Drive rolls increases by two.\n••• High Winds: The wind speed rises to around 30 miles per hour or 50 kilometers per hour, with gusts of up to twice that. Ranged attacks are much more difficult: + 1 to firearm attacks and +2 to thrown weapons and archery. In addition, during fierce gusts, Dexterity rolls (difficulty 6) may be required to keep characters from being knocked over by the winds. When gale-force winds are in effect, papers go flying, objects get picked up by the winds and hurled with abandon, and other suitably cinematic effects are likely. \nModerate temperature change: The local temperature can be raised or lowered by up to 20 degrees Fahrenheit or 10 degrees Celsius.\n•••• Storm: This has the effects of both Rain and High Winds.\n••••• Lightning Strike: This attack inflicts 10 dice of lethal damage. Body armor does not add to the target’s dice pool to soak this attack.",
                },
            ],
        },
        {
            "name": "Hands of Destruction (Anarch, Punk Sorcery)",
            "reference": "Rites of the Blood; PG 57 (V20 Core; PG 215)",
            "type": "Thaumaturgy (Anarch, Punk Sorcery)",
            "powers": [
                {
                    "name": "Herbal Wisdom",
                    "description": "With a touch, a vampire can commune with the\r\nspirit of a plant. Conversations held in this manner are\r\noften cryptic but rewarding — the wisdom and experience\r\nof the spirits of some trees surpasses that of the\r\noracles of legend. Crabgrass, on the other hand, rarely\r\nhas much insight to offer, but might reveal the appearance\r\nof the last person who trod upon it.",
                    "system": "The number of successes rolled determines\r\nthe amount of information that can be gained from the\r\ncontact. Depending on the precise information that\r\nthe vampire seeks, the Storyteller might require the\r\nplayer to roll Intelligence + Occult in order to interpret\r\nthe results of the communication.\r\nSuccesses Result\r\n1 success Fleeting cryptic impressions\r\n2 successes One or two clear images\r\n3 successes A concise answer to a simple query\r\n4 successes A detailed response to one or more\r\ncomplex questions\r\n5 successes The sum total of the plant-spirit’s\r\nknowledge on a given subject",
                },
                {
                    "name": "Speed the Seasons Passing",
                    "description": "This power allows a thaumaturge to accelerate a plant’s\r\ngrowth, causing roses to bloom in a matter of minutes or\r\ntrees to shoot up from saplings overnight. Alternately,\r\nshe can speed a plant’s death and decay, withering grass\r\nand crumbling wooden stakes with but a touch.",
                    "system": "The character touches the target plant. The\r\nplayer rolls normally, and the number of successes determines\r\nthe amount of growth or decay. One success\r\ngives the plant a brief growth spurt or simulates the effects\r\nof harsh weather, while three noticeably enlarge\r\nor wither it. With five successes, a full-grown plant\r\nsprings from a seed or crumbles to dust in a few minutes,\r\nand a tree sprouts fruit or begins decaying almost\r\ninstantaneously. If this power is used in combat, three\r\nsuccesses are needed to render a wooden weapon completely\r\nuseless. Two successes suffice to weaken it, while\r\nfive cause it to disintegrate in the wielder’s hand.",
                },
                {
                    "name": "Dance of Vines",
                    "description": "The thaumaturge can animate a mass of vegetation\r\nup to his own size, using it for utilitarian or combat purposes\r\nwith equal ease. Leaves can walk along a desktop,\r\nivy can act as a scribe, and jungle creepers can strangle\r\nopponents. Intruders should beware of Tremere workshops\r\nthat harbor potted rowan saplings.",
                    "system": "Any total amount of vegetation with a mass\r\nless than or equal to the character’s own may be animated\r\nthrough this power. The plants stay active for one turn\r\nper success scored on the roll, and are under the complete\r\ncontrol of the character. If used for combat purposes, the\r\nplants have Strength and Dexterity ratings each equal\r\nto half the character’s Willpower (rounded down) and\r\nBrawl ratings one lower than that of the character.\r\nDance of Vines cannot make plants uproot themselves\r\nand go stomping about. Even the most energetic\r\nvegetation is incapable of pulling out of the soil and\r\nwalking under the effect of this power. However, 200\r\npounds (100 kilograms) of kudzu can cover a considerable\r\narea all by itself….",
                },
                {
                    "name": "Verdant Haven",
                    "description": "This power weaves a temporary shelter out of a sufficient\r\namount of plant matter. In addition to providing physical\r\nprotection from the elements (and even sunlight), the\r\nVerdant Haven also establishes a mystical barrier which\r\nis nearly impassable to anyone the caster wishes to exclude.\r\nA Verdant Haven appears as a six-foot-tall (twometer-\r\ntall) hemisphere of interlocked branches, leaves, and vines with no discernible opening, and even to the\r\ncasual observer it appears to be an unnatural construction.\r\nVerdant Havens are rumored to have supernatural\r\nhealing properties, hut no Kindred have reported experiencing\r\nsuch benefits from a stay in one.",
                    "system": "A character must be standing in a heavily\r\nvegetated area to use this power. The Verdant Haven\r\nsprings up around the character over the course of three\r\nturns. Once the haven is established, anyone wishing\r\nto enter the haven without the caster’s permission\r\nmust achieve more than the caster’s original number of\r\nsuccesses on a single roll of Wits + Survival (difficulty\r\nequal to the caster’s Willpower). The haven lasts until\r\nthe next sunset, or until the caster dispels or leaves it.\r\nIf the caster scored four or more successes, the haven is\r\nimpenetrable to sunlight unless physically breached.",
                },
                {
                    "name": "Awaken the Forest Giants",
                    "description": "Entire trees can be animated by a master of the\r\nGreen Path. Ancient oaks can be temporarily given\r\nthe gift of movement, pulling their roots from the soil\r\nand shaking the ground with their steps. While not as\r\nversatile as elementals or other summoned spirits, trees\r\nbrought to ponderous life via this power display awesome\r\nstrength and resilience.",
                    "system": "The character touches the tree to be animated.\r\nThe player spends a blood point and rolls normally.\r\nIf the roll succeeds, the player must spend a blood\r\npoint for every success. The tree stays animated for one\r\nturn per success rolled; once this time expires, the tree\r\nputs its roots down wherever it stands and cannot be\r\nanimated again until the next night. While animated,\r\nthe tree follows the character’s verbal commands to\r\nthe best of its ability. An animated tree has Strength\r\nand Stamina equal to the caster’s Thaumaturgy rating,\r\nDexterity 2, and a Brawl rating equal to the caster’s\r\nown. It is immune to bashing damage, and all lethal\r\ndamage dice pools are halved due to its size.\r\nOnce the animating energy leaves a tree, it puts\r\ndown roots immediately, regardless of what it is currently\r\nstanding on. A tree re-establishing itself in the\r\nsoil can punch through concrete and asphalt to find\r\nnourishing dirt and water underneath, meaning that it\r\nis entirely possible for a sycamore to root itself in the\r\nmiddle of a road without any warning.",
                },
            ],
        },
        {
            "name": "Lure of Flames (Anarch, Punk Sorcery)",
            "reference": "Rites of the Blood; PG 57 (V20 Core; PG 218)",
            "type": "Thaumaturgy (Anarch, Punk Sorcery)",
            "powers": [
                {
                    "name": "Candle",
                    "description": "This path grants the thaumaturge the ability to conjure forth mystical flames — small fires at first, but skilled magicians may create great conflagrations. Fire created by this path is not “natural.” In fact, many vampires believe the flames to be conjured from Hell itself. The Lure of Flames is greatly feared, as fire is one of the surest ways to bring Final Death upon a vampire. See “Fire” (p. 297) for more information on how vampires suffer from flame.\n\nFire conjured by The Lure of Flames must be released for it to have any effect. Thus, a “palm of flame” does not burn the vampire’s hand and cause an aggravated wound (nor does it cause the caster to frenzy) — it merely produces light. Once the flame has been released, however, it burns normally and the character has no control over it.",
                    "system": "The number of successes determines how accurately the vampire places the flame in his desired location (declared before the roll is made). One success is all that is necessary to conjure a flame in one’s hand, while five successes place a flame anywhere in the Kindred’s line of sight. Less successes mean that the flame appears somewhere at the Storyteller’s discretion — as a rough rule of thumb, the thaumaturge can accurately place a flame within 10 yards or meters of themselves per success. Individual descriptions are not provided for each level of this path — fire is fire, after all (including potentially causing frenzy in other vampires witnessing it). The chart below describes the path level required to generate a specific amount of flame. To soak the damage at all, a vampire must have the Fortitude Discipline. Fire under the caster’s control does not harm the vampire or cause him to frenzy, but fires started as a result of the unnatural flame affect the thaumaturge normally.\nCandle (difficulty 3 to soak, one health level of aggravated damage/ turn)",
                },
                {
                    "name": "Palm of Flame",
                    "description": "This path grants the thaumaturge the ability to conjure forth mystical flames — small fires at first, but skilled magicians may create great conflagrations. Fire created by this path is not “natural.” In fact, many vampires believe the flames to be conjured from Hell itself. The Lure of Flames is greatly feared, as fire is one of the surest ways to bring Final Death upon a vampire. See “Fire” (p. 297) for more information on how vampires suffer from flame.\n\nFire conjured by The Lure of Flames must be released for it to have any effect. Thus, a “palm of flame” does not burn the vampire’s hand and cause an aggravated wound (nor does it cause the caster to frenzy) — it merely produces light. Once the flame has been released, however, it burns normally and the character has no control over it.",
                    "system": "The number of successes determines how accurately the vampire places the flame in his desired location (declared before the roll is made). One success is all that is necessary to conjure a flame in one’s hand, while five successes place a flame anywhere in the Kindred’s line of sight. Less successes mean that the flame appears somewhere at the Storyteller’s discretion — as a rough rule of thumb, the thaumaturge can accurately place a flame within 10 yards or meters of themselves per success. Individual descriptions are not provided for each level of this path — fire is fire, after all (including potentially causing frenzy in other vampires witnessing it). The chart below describes the path level required to generate a specific amount of flame. To soak the damage at all, a vampire must have the Fortitude Discipline. Fire under the caster’s control does not harm the vampire or cause him to frenzy, but fires started as a result of the unnatural flame affect the thaumaturge normally. \nPalm of flame (difficulty 4 to soak, one health level of aggravated damage/turn)",
                },
                {
                    "name": "Campfire",
                    "description": "This path grants the thaumaturge the ability to conjure forth mystical flames — small fires at first, but skilled magicians may create great conflagrations. Fire created by this path is not “natural.” In fact, many vampires believe the flames to be conjured from Hell itself. The Lure of Flames is greatly feared, as fire is one of the surest ways to bring Final Death upon a vampire. See “Fire” (p. 297) for more information on how vampires suffer from flame.\n\nFire conjured by The Lure of Flames must be released for it to have any effect. Thus, a “palm of flame” does not burn the vampire’s hand and cause an aggravated wound (nor does it cause the caster to frenzy) — it merely produces light. Once the flame has been released, however, it burns normally and the character has no control over it.",
                    "system": "The number of successes determines how accurately the vampire places the flame in his desired location (declared before the roll is made). One success is all that is necessary to conjure a flame in one’s hand, while five successes place a flame anywhere in the Kindred’s line of sight. Less successes mean that the flame appears somewhere at the Storyteller’s discretion — as a rough rule of thumb, the thaumaturge can accurately place a flame within 10 yards or meters of themselves per success. Individual descriptions are not provided for each level of this path — fire is fire, after all (including potentially causing frenzy in other vampires witnessing it). The chart below describes the path level required to generate a specific amount of flame. To soak the damage at all, a vampire must have the Fortitude Discipline. Fire under the caster’s control does not harm the vampire or cause him to frenzy, but fires started as a result of the unnatural flame affect the thaumaturge normally. \nCampfire (difficulty 5 to soak, two health levels of aggravated damage/turn)",
                },
                {
                    "name": "Bonfire",
                    "description": "This path grants the thaumaturge the ability to conjure forth mystical flames — small fires at first, but skilled magicians may create great conflagrations. Fire created by this path is not “natural.” In fact, many vampires believe the flames to be conjured from Hell itself. The Lure of Flames is greatly feared, as fire is one of the surest ways to bring Final Death upon a vampire. See “Fire” (p. 297) for more information on how vampires suffer from flame.\n\nFire conjured by The Lure of Flames must be released for it to have any effect. Thus, a “palm of flame” does not burn the vampire’s hand and cause an aggravated wound (nor does it cause the caster to frenzy) — it merely produces light. Once the flame has been released, however, it burns normally and the character has no control over it.",
                    "system": "The number of successes determines how accurately the vampire places the flame in his desired location (declared before the roll is made). One success is all that is necessary to conjure a flame in one’s hand, while five successes place a flame anywhere in the Kindred’s line of sight. Less successes mean that the flame appears somewhere at the Storyteller’s discretion — as a rough rule of thumb, the thaumaturge can accurately place a flame within 10 yards or meters of themselves per success. Individual descriptions are not provided for each level of this path — fire is fire, after all (including potentially causing frenzy in other vampires witnessing it). The chart below describes the path level required to generate a specific amount of flame. To soak the damage at all, a vampire must have the Fortitude Discipline. Fire under the caster’s control does not harm the vampire or cause him to frenzy, but fires started as a result of the unnatural flame affect the thaumaturge normally. \nBonfire (difficulty 7 to soak, two health levels of aggravated damage/turn)",
                },
                {
                    "name": "Inferno",
                    "description": "This path grants the thaumaturge the ability to conjure forth mystical flames — small fires at first, but skilled magicians may create great conflagrations. Fire created by this path is not “natural.” In fact, many vampires believe the flames to be conjured from Hell itself. The Lure of Flames is greatly feared, as fire is one of the surest ways to bring Final Death upon a vampire. See “Fire” (p. 297) for more information on how vampires suffer from flame.\n\nFire conjured by The Lure of Flames must be released for it to have any effect. Thus, a “palm of flame” does not burn the vampire’s hand and cause an aggravated wound (nor does it cause the caster to frenzy) — it merely produces light. Once the flame has been released, however, it burns normally and the character has no control over it.",
                    "system": "The number of successes determines how accurately the vampire places the flame in his desired location (declared before the roll is made). One success is all that is necessary to conjure a flame in one’s hand, while five successes place a flame anywhere in the Kindred’s line of sight. Less successes mean that the flame appears somewhere at the Storyteller’s discretion — as a rough rule of thumb, the thaumaturge can accurately place a flame within 10 yards or meters of themselves per success. Individual descriptions are not provided for each level of this path — fire is fire, after all (including potentially causing frenzy in other vampires witnessing it). The chart below describes the path level required to generate a specific amount of flame. To soak the damage at all, a vampire must have the Fortitude Discipline. Fire under the caster’s control does not harm the vampire or cause him to frenzy, but fires started as a result of the unnatural flame affect the thaumaturge normally. \nInferno (difficulty 9 to soak, three health levels of aggravated damage/turn)",
                },
            ],
        },
        {
            "name": "Path of Blood (Anarch, Punk Sorcery)",
            "reference": "Rites of the Blood; PG 57 (V20 Core; PG 212)",
            "type": "Thaumaturgy (Anarch, Punk Sorcery)",
            "powers": [
                {
                    "name": "A Taste for Blood",
                    "description": "This power was developed as a means of testing a foe’s might — an extremely important ability in the tumultuous early nights of Clan Tremere. By merely touching the blood of his subject, the caster may de-termine how much vitae remains in the subject and, if the subject is a vampire, how recently he has fed, his approximate Generation and, with three or more suc-cesses, whether he has ever committed diablerie.",
                    "system": "The number of successes achieved on the roll determines how much information the thauma-turge gleans and how accurate it is.",
                },
                {
                    "name": "Blood Rage",
                    "description": "This power allows a vampire to force another Kin-dred to expend blood against his will. The caster must touch her subject for this power to work, though only the lightest contact is necessary. A vampire affected by this power might feel a physical rush as the thau-maturge heightens his Physical Attributes, might find himself suddenly looking more human, or may even find himself on the brink of frenzy as his stores of vitae are mystically depleted.",
                    "system": "Each success forces the subject to spend one blood point immediately in the way the caster desires (which must go towards some logical expenditure the target vampire could make, such as increasing Physical Attributes or powering Disciplines). Note that blood points forcibly spent in this manner may exceed the normal “per turn” maximum indicated by the victim’s Generation. Each success gained also increases the subject’s difficulty to resist frenzy by one. The thauma-turge may not use Blood Rage on herself to circumvent generational limits.",
                },
                {
                    "name": "Blood of Potency",
                    "description": "The thaumaturge gains such control over his own blood that he may effectively “concentrate” it, mak-ing it more powerful for a short time. In effect, he may temporarily lower his own Generation with this power. This power may be used only once per night.",
                    "system": "One success on the Willpower roll allows the character to lower his Generation by one step for one hour. Each additional success grants the Kindred either one step down in Generation or one hour of ef-fect. Successes earned must be spent both to decrease the vampire’s Generation and to maintain the change (this power cannot be activated again until the origi-nal application wears off). If the vampire is diablerized while this power is in effect, it wears off immediately and the diablerist gains power appropriate to the cast-er’s actual Generation. Furthermore, any mortals Em-braced by the thaumaturge are born to the Generation appropriate to their sire’s original Generation (e.g., a Tenth-Generation Tremere who has reduced his ef-fective Generation to Eighth still produces Eleventh-Generation childer).Once the effect wears off, any blood over the char-acter’s blood pool maximum dilutes, leaving the char-acter at his regular blood pool maximum. Thus, if a Twelfth-Generation Tremere (maximum blood pool of 11) decreased his Generation to Ninth (maximum blood pool 14), ingested 14 blood points, and had this much vitae in his system when the power wore off, his blood pool would immediately drop to 11.",
                },
                {
                    "name": "Theft of Vitae",
                    "description": "A thaumaturge using this power siphons vitae from her subject. She need never come in contact with the subject — blood literally streams out in a physical tor-rent from the subject to the Kindred (though it is often mystically absorbed and need not enter through the mouth).",
                    "system": "The number of successes determines how many blood points the caster transfers from the sub-ject. The subject must be visible to the thaumaturge and within 50 feet (15 meters). Using this power pre-vents the caster from being blood-bound, but other-wise counts as if the vampire ingested the blood her-self. This power is spectacularly obvious, and Camarilla princes justifiably consider its public use a breach of the Masquerade.",
                },
                {
                    "name": "Cauldron of Blood",
                    "description": "A thaumaturge using this power boils her subject’s blood in his veins like water on a stove. The Kindred must touch her subject, and it is this contact that sim-mers the subject’s blood. This power is always fatal to mortals, and causes great damage to even the mightiest vampires.",
                    "system": "The number of successes gained determines how many blood points are brought to boil. The sub-ject suffers one health level of aggravated damage for each point boiled (individuals with Fortitude may soak this damage using only their Fortitude dice). A single success kills any mortal, though some ghouls with ac-cess to Fortitude are said to have survived after soaking all of the aggravated damage.",
                },
            ],
        },
        {
            "name": "Path of Mars (Anarch, Punk Sorcery)",
            "reference": "Rites of the Blood; PG 57 (V20 Core; PG 224)",
            "type": "Thaumaturgy (Anarch, Punk Sorcery)",
            "powers": [
                {
                    "name": "War Cry",
                    "description": "A vampire on the attack can focus his will, making\nhim less susceptible to battle fear or the powers of the\nundead. The vampire shouts a primal scream to start the\neffect, though some thaumaturges have been known to\npaint their faces or cut themselves open instead.",
                    "system": "For the duration of one scene, the vampire\nadds one to his Courage Trait. Additionally, for the\npurposes of hostile effects, his Willpower is considered\nto be one higher (though this bonus applies only to the\nTrait itself, not the Willpower pool). A character may\nonly gain the benefits of War Cry once per scene.",
                },
                {
                    "name": "Strike True",
                    "description": "The vampire makes a single attack, guided by the\nunholy power of her Blood. This attack strikes its foe\ninfallibly.",
                    "system": "By invoking this power, the player need\nnot roll to see if the vampire’s attack hits — it does,\nautomatically. Only Melee or Brawl attacks may be\nmade in this manner. These attacks are considered to\nbe one-success attacks; they offer no additional damage\ndice. Also, they may be dodged, blocked, or parried\nnormally, and the defender needs only one success (as\nthe attacks’ number of success is assumed to be one).\nStrike True has no effect if attempted on multiple attacks\n(dice pool splits) in a single turn from one character.",
                },
                {
                    "name": "Wind Dance",
                    "description": "The thaumaturge invokes the power of the winds,\nmoving in a blur. She gains a preternatural edge in\navoiding her enemies’ blows, moving out of their way\nbefore the enemy has a chance to throw them.",
                    "system": "The player can dodge any number of attacks\nwith her full dice pool in a single turn. This advantage\napplies only to dodges — if the character wishes to attack\nand dodge, the player must still split her dice pool.\nThis power lasts for one scene.",
                },
                {
                    "name": "Fearless Heart",
                    "description": "The vampire temporarily augments his abilities as a\nwarrior. Through the mystical powers of blood magic,\nthe character becomes a potent fighting force.",
                    "system": "Fearless Heart grants the vampire an extra\npoint in each of the Physical Attributes (Strength,\nDexterity, and Stamina). These Traits may not exceed\ntheir generational maximums, though the player may\nuse blood points to push the character’s Traits even\nhigher. The effects last for one scene, and a character\nmay gain its benefits only once per scene. The vampire\nmust spend two hours in a calm and restful state following\nthe use of Fearless Heart, or lose a blood point\nevery 15 minutes until he rests.",
                },
                {
                    "name": "Comrades at Arms",
                    "description": "This ability extends the power of the previous abilities\nin the path. It allows any of the earlier effects to be\napplied to a group such as a pack or War Party.",
                    "system": "The player chooses one of the lower-level\npowers in the path, invoking it as normal. Afterward,\nhe touches another character and (if the roll for Comrades\nat Arms is successful) bestows the benefit on her\nas well. The same power may be delivered to any number\nof packmates, as long as the rolls for Comrades at\nArms are successful and the thaumaturge pays the appropriate\nblood costs.",
                },
            ],
        },
        {
            "name": "Path of the Evil Eye (Anarch, Punk Sorcery)",
            "reference": "Rites of the Blood; PG 57",
            "type": "Thaumaturgy (Anarch, Punk Sorcery)",
            "powers": [
                {
                    "name": "Humiliation",
                    "description": "The simplest application of the Evil Eye causes the target \nto embarrass himself in some public way. Possible results \ninclude saying something embarrassing in front of one’s \npeers, failing disastrously at a feeding attempt, or simply \nripping the seat out of one’s pants while in a crowded bar.",
                    "system": "Each success represents one night during which \nthe target is affected by the curse. The curse triggers \nonce per night at a time of the Storyteller’s choosing, \nusually the scene during which the character is in front \nof the largest number of individuals or in which he is in \nfront of the largest number of socially important people. \nThat is, it may trigger while the character is in a crowded \nrestaurant or when he is alone with the Prince, whichever \nhas the greatest potential for personal embarrassment. \nThe Storyteller determines when the curse triggers, but \nit should do so at least once per night. \nDuring the trigger scene, on every Social roll made for \nthe character, the player must add a number of automatic \n1s equal to the sorcerer’s rating in the Path of the Evil Eye, \nthereby increasing the likelihood of a botch on a Social \nroll. In addition, during the trigger scene, the Storyteller \nshould roll a number of dice equal to the sorcerer’s rating \nin this path (difficulty 5). Successes mean that some \nexternal event happens that causes embarrassment to \nthe character, such as a waiter spilling drinks on him or \na car splashing him with mud.",
                },
                {
                    "name": "Loss",
                    "description": "This curse affects the target’s material worth. It most \ncommonly causes the target to be stripped of money, but it \nmay also cause her Herd to diminish, or destroy a Haven. \nThe curse can target any tangible asset represented as a \nBackground. If the character has no suitable Backgrounds, \nit targets personal items of emotional significance.",
                    "system": "Within one week, the target loses one dot \nfrom an appropriate Background. Generally, the curse \npreferentially attacks Resources over other backgrounds, but theoretically any form of tangible Background representing a personal asset can be a valid target. The sorcerer has no control over how the Background point is lost or even which Background point is lost. The Storyteller may even choose to decide randomly.",
                },
                {
                    "name": "Peril",
                    "description": "At this level of mastery, the ashipu may finally endanger \nher enemy rather than merely inconvenience her. The \ncurse cannot directly harm the target, but it can create \na situation in which it is possible for her to be harmed, \nwhether at the hands of a drunken lout who takes offense \nto the target’s manner at a bar or a pack of werewolves \nwho, by happenstance, choose to board the same lonely \nsubway car as the victim.",
                    "system": "The number of successes determines how many nights the character is at risk. At the start of each night, the Storyteller must roll a die and, depending on the results, fashion an encounter for the targeted character. \nDice Result Nature of Peril\n 1-3  None. The curse does not trigger during this \n      night.\n 4-6  Minor: An encounter which is not likely to \n    harm the character but which has a chance \n    to do so. A mortal tries to mug the character \n    while she is in front of mortals, or simply \n    tries to hold up a convenience store while \n    the character is in line paying for gas. A \n    bar patron takes offense to something the \n    character does or says and tries to pick a \n    fight.\n 7-8  Moderate: An encounter with a significant \n    likelihood of at least some harm to the \n    character. The character is involved in a \n    car wreck or struck by a hit-and-run driver. \n    Stairs give way while the character is \n     climbing them.\n 9  Severe: An encounter in which the \n    character is almost certain to suffer some \n    lethal damage. The character inadvertently \n    says something offensive that provokes \n    frenzy rolls in nearby vampires. The \n    building collapses while the character is in \n    it or a fire breaks out.\n 10  Catastrophic: An encounter that is potentially deadly.    The character’s is locked out of his haven during the    day. The character unwittingly says something that    offends a pack of nearby Lupines.\n\n Nights on which there is no peril do not count against \nthe ashipu’s successes; the curse will continue until the \ntarget has suffered a number of dangerous encounters \nequal to the successes or the curse is lifted. During any \ndangerous encounter, a targeted character has a chance \nto realize she is under a curse (if she didn’t already know \nit). The roll is Intelligence + Occult. The default difficulty is 9, but it drops to 8 if the character has Auspex or to 6 if the character has any knowledge of this Path.",
                },
                {
                    "name": "Enemy",
                    "description": "This potent curse causes the target’s friends and allies \nto turn against him, even as it causes the numbers of his \nenemies to grow.",
                    "system": "For each success on the Willpower roll, the \ntarget loses one dot of Allies, Contacts, Influence, or \nRetainers. This may reflect friends and allies who have \nbecome angry with the character and turn their back on \nhim, it may reflect contacts and allies who are simply \nunavailable for a time, or it may actually result in such \ncharacters being injured or even dying due to ill fortune. \nAlternatively, the player may choose to spend some or all of the successes to give the target a new Enemy (as per the Enemy Flaw) who arrives to pursue a vendetta against the character. Regardless, the effects manifest within a week, and the player of the targeted character may neither regain lost Backgrounds nor remove the Enemy Flaw without learning about and neutralizing the curse.",
                },
                {
                    "name": "The Eye that Wounds",
                    "description": "The ultimate expression of this malefic path, the \nEye That Wounds does not require time to establish a \nchain of ill fortune. It strikes immediately. The ashipu \nmust make eye contact with her target and utter some \nexclamation pertaining to a characteristic of his. It can \nbe praise or insult, sarcasm or fury, but whatever form it \ntakes, the target is immediately struck with an agonizing \ninjury that damages that characteristic.",
                    "system": "While the curse allows for flexibility, the default \nassumption is that for every two successes (rounded up), the target (or object, if the curse is directed towards a possession of the target) suffers one level of aggravated damage. Generally, even a single level of damage is sufficient to slay an animal or destroy most objects. If used against a mortal, this power will permanently maim him. If used against a Kindred, the curse will inflict damage shaped by the ashipu’s words. If she compliments his beautiful eyes, they will be burned and he might be rendered blind until he can heal. If she mocks his honeyed words, the curse might burn out his tongue and leave him unable to speak. This curse may be transmitted through an effigy, but the normal difficulty penalty imposed for using an effigy increases by +2 (see Principles of Contagion and Sympathy on pp. 133-135).",
                },
            ],
        },
        {
            "name": "Path of the Levinbolt (Anarch, Punk Sorcery)",
            "reference": "Rites of the Blood; PG 57",
            "type": "Thaumaturgy (Anarch, Punk Sorcery)",
            "powers": [
                {
                    "name": "Flicker",
                    "description": "Novice Thaumaturges learn to freely absorb power\naround them through electrical outlets, circuits, or \nbatteries. A user of this power can sense the current \nfeeding into a specific electrical system and then draw\nit to her, effectively turning it off.",
                    "system": "The thaumaturge simply glances at a target \npowered by electricity. Upon a succesful activation \nroll, she can shut down an electrical device for ten \nminutes per success on the activation roll. The spark \nof electricity arcs from the device directly into the \nthaumaturge in a frightening display of mystical power. \nThe source of this power is immediately known.",
                },
                {
                    "name": "Spark",
                    "description": "Novice thaumaturges can build up a tiny static \ncharge, enough to make a noticeable snap with a \ntouch. Such a discharge poses little threat to healthy \ntargets, though the energy can ruin delicae electronics \nor stun an unlucky victim.",
                    "system": "The thaumaturge simply touches a target \n(after the requisite blood expenditure and activation \nroll by the player) and releases the spark. The \nelectricity can snap from any part of the caster's body, \nso a thaumaturge might give an unpleasant surprise\nto someone touching her. The resulting electrical \ndischarge inflicts four dice of lethal damage to targets\n(difficulty 7 to soak), and short-circuits electronic \nequipment and devices not specifically grounded \nagainst lightning strike.",
                },
                {
                    "name": "Illuminate",
                    "description": 'Neonates sometimes derogatively refer to this effect\nas the "40-watt Tremere," right up until they\'ve felt its\nsting. The thaumaturge summons enough electricity \nto cover her hand or arm in arcing bolts. This power \ncan charge a battery, briefly run a small device, or \neven leave a nasty burn on a touched subject.',
                    "system": "Each success scored on the player's \nactivation roll translates to approximately one turn of \npower sufficient to run a handful of lights or a small \nelectrical device. Alternately, the thaumaturge can \nshock someone by touch, as with the Spark power, \nbut for eight dice of lethal electricity damage (difficulty \n8 to soak). \nThe current created with this power is not strong \nenough to force its way through less-than-ideal \nconductors, and thus simply inflicts electrical damage \nraw metals, woods, or other matter in the form of a burn \nand discoloration. The thaumaturge can alternately allow \nthe electricity to spark around her hand, eyes, or head; \nthis creates illumination about equal to a dim light bulb,\nand lowers the difficulty of any Intimidation rolls by 2.",
                },
                {
                    "name": "Thor's Fury",
                    "description": "The thaumaturge may strike her enemies from afar as \nthough she were a god. She may direct an arc of lightning \nfrom her body to nearby targets.",
                    "system": "The thaumaturge focuses her concentration \nupon her target and then directs hurled bolts via a \nPerception + Science roll (difficulty 6 plus the range \nin yard/meters, maximum 4 yards/meters). Each success \ninflicts a level of lethal damage (difficulty 8 to soak). The \nsource of this power is immediately known.",
                },
                {
                    "name": "Eye of the Storm",
                    "description": "The thaumaturge becomes a shifting, sparkling pillar of \nelectrical power. The energy channeled in the Eye of the \nStorm shields her body from virtually any direct harm.",
                    "system": "When a thaumaturge spends a Willpower point \nto invoke this power, she solidifies the stored electricity \ninside of her into a mystical barrier that completely \nsorrounds her. The caster becomes immune to any ranged \nattacks. Metal weapons such as swords inflict injury as \nnormal for the first sttrike, but are then melted from \ncontact with the barrier, and the wielder takes a level \nof lethal damage. Enemies that dare to touch the caster \nsuffer two points of aggravated damage (difficulty 8 to \nsoak.) Non-mettal weapons, such as wooden stakes, are not \naffected by Eye of the Storm. This power lasts for a single \nturn, with each additional success on the activattion roll \nextending tthis duration by one turn. Mental and social \nattacks may pass through this barrier.",
                },
            ],
        },
        {
            "name": "Vodoun Necromancy (Anarch, Punk Sorcery)",
            "reference": "Rites of the Blood; PG 57 (Rites of the Blood; PG 166)",
            "type": "Thaumaturgy (Anarch, Punk Sorcery)",
            "powers": [
                {
                    "name": "Touch of Life",
                    "description": "The wangateur may ingest a special mixture of herbs\r\nand powders in lieu of expending blood when trying to\r\nimitate the characteristics of the living. The effect lasts\r\nfor one scene. The wangateur may ingest this mixture\r\nfor himself or provide it to another Kindred (but not a\r\nmortal) who must swallow the mixture during that scene.\r\nIn the latter case, the wangateur decides which aspect of\r\nthe living the other Kindred will imitated.",
                    "system": "",
                },
                {
                    "name": "Strength of Root and Stone",
                    "description": "The wangateur may inhale a mixture of herbs and\r\npowders through the nose instead of expending blood\r\nwhen trying to augment a Physical Attribute. The effect is\r\nthe same as if the vampire had spent one point of blood\r\nto improve a Physical Attribute. The effect lasts for one\r\nscene. The wangateur may use this mixture himself or\r\nprovide it for another (including a mortal). If it is to be\r\nused by another, the wangateur decides which Attribute\r\nis to be augmented when the mixture is prepared.",
                    "system": "",
                },
                {
                    "name": "Breath of Life",
                    "description": "The wangateur may use a mixture of herbs and powders\r\nin place of blood when trying to heal herself. The specific\r\nmixture produces a paste which the wangateur must physically\r\nsmear on the area to be healed. The effect is the same as if\r\nthe vampire had spent one point of blood to repair physical\r\ndamage. This power cannot be used to heal aggravated damage,\r\nonly bashing or lethal. The wangateur may use this mixture\r\nfor himself or for another (including a mortal).",
                    "system": "",
                },
                {
                    "name": "Favor of the Orishas",
                    "description": "The wangateur may use a mixture of herbs and powders\r\nin order to fuel any Discipline (including blood magic)\r\nthat requires exactly one point of blood to function.\r\nThis formula also requires a small quantity of blood to\r\nfunction, but it need not come from the wangateur and,\r\nin fact, can come from an enemy (human or Kindred) who\r\nhas shed blood nearby. The wangateur may only use this\r\nmixture on herself and must make a superficial cut on\r\nher arm and then rub the mixture into the open wound.",
                    "system": "",
                },
                {
                    "name": "Gift of Ashe",
                    "description": "The wangateur may now create mixtures using the first\r\nthree levels of this path which will maintain their efficacy\r\nfor an entire night rather than just one turn or scene.\r\nFurthermore, the wangateur can maintain a number of\r\nmixtures up to his Intelligence simultaneously. Thus, he\r\ncan provide the mixtures to allies and no longer needs to be\r\nnearby in order to provide the appropriate benefits — he can\r\nsimply give the mixture to an ally and send her on her way.",
                    "system": "",
                },
            ],
        },
    ]

    for p in path_data:
        p_type = V20_Magic_Types.query.filter_by(name=p["type"]).first()
        if not p_type:
            magic = V20_Magic_Types(name=p["type"])
            db.session.add(magic)

        existing = V20_Sorcery_Paths.query.filter_by(name=p["name"]).first()
        if existing:
            continue

        path = V20_Sorcery_Paths(
            name=p["name"],
            category=p["type"],
            reference=p["reference"],
            powers=p["powers"],
        )
        db.session.add(path)


def seed_v20_rituals():
    ritual_data = []
    pass


def seed_v20_powers():
    pass


def seed_v20_merits():
    merit_data = [
        {
            "name": "Acute Sense",
            "rating": [1],
            "description": "One of your senses is exceptionally sharp, be it sight, hearing, smell, touch, or taste. The difficulties for all tasks involving the use of this particular sense are reduced by two. This Merit can be combined with the Discipline of Auspex to produce superhuman sensory acuity.",
            "reference": "V20 Corebook; PG 479",
            "clan": None,
        },
        {
            "name": "Ambidextrous",
            "rating": [1],
            "description": "You have a high degree of off-hand dexterity and can perform tasks with the “wrong” hand at no pen-alty. The rules for taking multiple actions still apply, but you do not suffer a difficulty penalty if you use two weapons or are forced to use your off hand.",
            "reference": "V20 Corebook; PG 480",
            "clan": None,
        },
        {
            "name": "Bruiser",
            "rating": [1],
            "description": "Your appearance is sufficiently thug-like to inspire fear (or at least disquiet) in those who see you. While you’re not necessarily ugly, you do radiate a quiet menace, to the point where people cross the street to avoid passing near you. All Intimidation rolls against those who have not demonstrated their physical superiority to you are at -1 difficulty.",
            "reference": "V20 Corebook; PG 480",
            "clan": None,
        },
        {
            "name": "Catlike Balance",
            "rating": [1],
            "description": "You possess an innately perfect sense of balance. Characters with this Merit reduce difficulties of all balance-related rolls (e.g., Dexterity + Athletics to walk along a narrow ledge) by two.",
            "reference": "V20 Corebook; PG 480",
            "clan": None,
        },
        {
            "name": "Early Riser",
            "rating": [1],
            "description": "No one can explain it, but you seem to have the ability to work on less rest than your fellow vampires. You always seem to be the first to rise and the last to go to bed even if you’re been out until dawn. Your Humanity or Path score is considered to be 10 for purposes of deciding when you rise each evening. Vampires with this Merit cannot take the Deep Sleeper Flaw.",
            "reference": "V20 Corebook; PG 480",
            "clan": None,
        },
        {
            "name": "Eat Food",
            "rating": [1],
            "description": "You have the capacity to eat food and even savor its taste. While you cannot derive any nourishment from eating regular foods, this ability will serve you well in pretending to be human. Of course, you can’t digest what you eat, and there will be some point during the evening when you have to heave it back up.",
            "reference": "V20 Corebook; PG 480",
            "clan": None,
        },
        {
            "name": "Friendly Face",
            "rating": [1],
            "description": "You have a face that reminds everyone of someone, to the point where strangers are inclined to be well inclined toward you because of it. The effect doesn’t fade even if you explain the “mistake,” leaving you at -1 difficulty on all appropriate Social-based rolls (yes for Seduction, no for Intimidation, for example) when a stranger is involved. This Merit only functions on a first meeting.",
            "reference": "V20 Corebook; PG 480",
            "clan": None,
        },
        {
            "name": "Blush of Health",
            "rating": [2],
            "description": "You look more hale and healthy in appearance than other vampires, allowing you to blend with human society much more easily. You still retain the color of a living mortal, and your skin feels only slightly cool to the touch.",
            "reference": "V20 Corebook; PG 480",
            "clan": None,
        },
        {
            "name": "Enchanting Voice",
            "rating": [2],
            "description": "There is something about your voice that others cannot ignore. When you command, they are cowed. When you seduce, they swoon. Whether thundering, soothing, persuading, or simply talking, your voice commands attention. The difficulties of all rolls involving the use of the voice to persuade, charm, or command are reduced by two.",
            "reference": "V20 Corebook; PG 480",
            "clan": None,
        },
        {
            "name": "Daredevil",
            "rating": [3],
            "description": "You are good at taking risks, and even better at surviving them. When attempting exceptionally risky non-combat actions (such as leaping from one moving car to another), characters with this Merit add an additional three dice to their rolls, and negate a single botch die that may result from such a roll. Generally, such actions must be at least difficulty 8 and have the potential to inflict at least three health levels of damage if failed.",
            "reference": "V20 Corebook; PG 480",
            "clan": None,
        },
        {
            "name": "Efficient Digestion",
            "rating": [3],
            "description": "You are able to draw more than the usual amount of nourishment from blood. When feeding, you gain an additional point to your blood pool for every two points of blood you consume. This does not allow you to exceed your blood pool maximum.",
            "reference": "V20 Corebook; PG 480",
            "clan": None,
        },
        {
            "name": "Discerning Palate",
            "rating": [4],
            "description": "Your naturally selective palate allows you to discern specific traits inherent to a sample of blood. With but a taste, you can determine potency, freshness, species, or whether a blood sample is contaminated, as well as attempt to identify the Generation, age, and even Clan of other vampires. If you sample even a single drop of blood, roll Perception + Awareness (difficulty 8). • One success allows you to identify the relative potency and freshness of the blood, a species whose blood you have previously tasted and know to be of a specific kind, the Generation of another vampire within two steps of your own, if the blood is either under one hundred or over one hundred years old, and if it is of your same Clan. • Two successes identifies whether the blood is contaminated by disease or poison, the Generations of vampires within four steps of your own, the approximate age within fifty years (if less than three hundred years old), and any Clan whose blood you’ve previously tasted. • With three or more successes, you identify specific contaminates you’ve sampled before, Generations within six steps of your own, the vintage of blood within twenty-five years (if less than six hundred years old), and any Clan as well as family of vampires whose blood you’ve tasted previously.",
            "reference": "The Black Hand: A Guide to The Tal'Mahe'Ra; PG 177",
            "clan": None,
        },
        {
            "name": "Huge Size",
            "rating": [4],
            "description": "You are abnormally large in size, at least 6’10” and 300 pounds in weight (well over two meters tall and over 130 kgs). Aside from making you extremely noticeable in public, this extra mass bestows an additional Bruised health level. Characters with this Merit may also gain bonuses to push objects, open barred doors, avoid being knocked down, etc.",
            "reference": "V20 Corebook; PG 480",
            "clan": None,
        },
        {
            "name": "Coldly Logical",
            "rating": [1],
            "description": "While some might refer to you as a “cold fish,” you have a knack for separating factual reporting from emotional or hysterical coloration. You may or may not be emotional yourself, but you can see clearly when others are clouding the facts with their feelings (-1 difficulty on all related rolls).",
            "reference": "V20 Corebook; PG 484",
            "clan": None,
        },
        {
            "name": "Common Sense",
            "rating": [1],
            "description": "You have a significant amount of practical, everyday wisdom. Whenever you are about to act in a way contrary to common sense, the Storyteller can make suggestions or warnings about the implications of said action. This is a very useful Merit for beginning players unfamiliar with the game.",
            "reference": "V20 Corebook; PG 484",
            "clan": None,
        },
        {
            "name": "Concentration",
            "rating": [1],
            "description": "You have the ability to focus your mind and shut out any distractions or annoyances. Characters with this Merit are unaffected by any penalties stemming from distracting circumstances (e.g., loud noises, strobe lights, or hanging upside down).",
            "reference": "V20 Corebook; PG 484",
            "clan": None,
        },
        {
            "name": "Introspection",
            "rating": [1],
            "description": "You have keen insight into the ulterior motives of all your actions. Through this nightly exercise, you also have incredible insight into the underlying motives of others’ actions. Add two dice to your Perception dice pool when you must take an action against someone with the same Nature or Demeanor as you.",
            "reference": "V20 Corebook; PG 484",
            "clan": None,
        },
        {
            "name": "Kashaph",
            "rating": [1],
            "description": "The term kashaph is of ambiguous meaning, based on a Hebrew root word for “mutter,” and implying spoken sorcery and incantations. The term is used in the Old Testament to condemn the practitioners of witchcraft. True kashaph has long been extinct — save among the Inconnu. Kashaph is an enchanted language, and cannot be “decoded” by modern linguistics or cryptography. The Inconnu use kashaph to communicate secretly, and also as a method of identifying one another. New members of the Inconnu are not taught kashaph by normal means. It cannot be studied, nor learned like a conventional language. Instead, members are indoctrinated into the society through an elaborate ritual during which the language of kashaph is inscribed upon their soul. Once “learned” in this way, the language may be spoken, not written (there is no written form, and the sounds cannot be accurately captured by phonetic scribblings), and only another individual with this merit has the capacity to understand the words said in the language of kashaph.",
            "reference": "Rites of the Blood; PG 100",
            "clan": None,
        },
        {
            "name": "Language",
            "rating": [1],
            "description": "You know a language in addition to your native one. You can take this Merit multiple times, each reflecting a different language.",
            "reference": "V20 Corebook; PG 484",
            "clan": None,
        },
        {
            "name": "Time Sense",
            "rating": [1],
            "description": "You have an innate sense of time and are able to estimate the passage of time accurately without using a watch or other mechanical device.",
            "reference": "V20 Corebook; PG 484",
            "clan": None,
        },
        {
            "name": "Useful Knowledge",
            "rating": [1],
            "description": "You have expertise in a specific field that makes your conversation intriguing to an older Kindred. So long as your knowledge holds the other vampire’s attention, he has a vested interest in keeping you around. Then again, once he’s pumped you for every iota of information you possess, that patronage may suddenly vanish. (Note: This Merit should be played like a 1-dot Mentor with a specific interest. However, unlike a Mentor, Useful Knowledge does not imply a permanent relationship.)",
            "reference": "V20 Corebook; PG 484",
            "clan": None,
        },
        {
            "name": "Code of Honor",
            "rating": [2],
            "description": "You have a personal code of ethics to which you adhere. The specifics of this code must be worked out with the Storyteller prior to play, and the character must follow it strictly. Characters with this Merit gain two additional dice to all Willpower or Virtue rolls when acting in accordance with their code (e.g., defending the helpless) or when attempting to avoid situations that might force them to violate their code.",
            "reference": "V20 Corebook; PG 484",
            "clan": None,
        },
        {
            "name": "Computer Aptitude",
            "rating": [2],
            "description": "You are familiar with and talented in the uses of computer equipment. Other Kindred may not understand computers, but to you they are intuitive. All rolls involving computers are at -2 difficulty for you.",
            "reference": "V20 Corebook; PG 484",
            "clan": None,
        },
        {
            "name": "Eidetic Memory",
            "rating": [2],
            "description": "You remember, with perfect detail, things you see and hear. Documents, photographs, conversations, etc., can be committed to memory with only minor concentration. Under stressful conditions involving numerous distractions, you must make a Perception + Alertness roll (difficulty 6) to summon enough concentration to absorb what your senses detect.",
            "reference": "V20 Corebook; PG 484",
            "clan": None,
        },
        {
            "name": "Light Sleeper",
            "rating": [2],
            "description": "You can awaken instantly at any sign of trouble or danger, and do so without any sleepiness or hesitation. You may ignore rules regarding how Humanity or your morality Path restricts the number of dice available during the day.",
            "reference": "V20 Corebook; PG 485",
            "clan": None,
        },
        {
            "name": "Natural Linguist",
            "rating": [2],
            "description": "You have a flair for languages. You may add three dice to any dice pool involving written or spoken languages, and each purchase of the Language Merit (previous page) gives you two languages instead of just one.",
            "reference": "V20 Corebook; PG 485",
            "clan": None,
        },
        {
            "name": "Calm Heart",
            "rating": [3],
            "description": "You are naturally calm and do not easily fly off the handle. You receive two extra dice when attempting to resist a frenzy. Brujah may not take this Merit.",
            "reference": "V20 Corebook; PG 485",
            "clan": None,
        },
        {
            "name": "Iron Will",
            "rating": [3],
            "description": "When you are determined and your mind is set, nothing can thwart you from your goals. Characters using Dementation, Dominate, or any other mind-altering magic, spell, or Thaumaturgy path against your character are at +3 difficulty. Elder levels of powers like Dementation and Dominate may overwhelm even this resistance. Against Level Six powers, the expenditure of a Willpower point through Iron Will only raises the difficulty of the Discipline roll by two. Against Level Seven powers, the difficulty is increased by only one. Level Eight and higher powers cannot be resisted with Iron Will. This Merit does not affect Presence or other powers dealing with the emotions. Characters will Willpower scores below 8 cannot take this Merit.",
            "reference": "V20 Corebook; PG 485",
            "clan": None,
        },
        {
            "name": "Precocious",
            "rating": [3],
            "description": "You learn quickly. The time for you to pick up a particular Ability (or Abilities, at Storyteller discretion) is cut in half, as is the experience cost.",
            "reference": "V20 Corebook; PG 485",
            "clan": None,
        },
        {
            "name": "Grand Library",
            "rating": [2, 4, 6, 7],
            "description": "Throughout the years, you’ve managed to amass an exquisite collection of books, both common and rare. Choose 3 Knowledge dots for every 2 points taken in this Merit, or 10 Knowledge dots for 7 points. While working in your library, the difficulty rating for any rolls involving those Knowledges is reduced by 2.",
            "reference": "The Black Hand: A Guide to The Tal'Mahe'Ra; PG 177",
            "clan": None,
        },
        {
            "name": "Elysium Regular",
            "rating": [1],
            "description": "You spend an unusual amount of time in Elysium. You see and are seen to such an extent that all of the movers and shakers of Elysium at least know who you are. Extended time spent in Elysium also gives you extended opportunities to interact with the Harpies and other Kindred of that stature — and they’ll know your name when you approach them. This Merit is generally taken by vampires that respect and attend Elysium on a regular basis.",
            "reference": "V20 Corebook; PG 487",
            "clan": None,
        },
        {
            "name": "Former Ghoul",
            "rating": [1],
            "description": "You were introduced to the Blood long before you were made Kindred. Your long experience as a ghoul gives you insight into and comfort with vampiric society. You are at -1 difficulty on all Social rolls when in the presence of other neonates (particularly those who haven’t been educated by their sires), and have a -1 difficulty on all rolls relating to vampiric knowledge.",
            "reference": "V20 Corebook; PG 487",
            "clan": None,
        },
        {
            "name": "Harmless",
            "rating": [1],
            "description": "Everyone in the city knows you, and knows that you’re no threat to their plans. While that sort of estimation may seem insulting, it’s also what’s kept you from being killed. No one considers you worth their time to deal with, and that low opinion keeps you safe. If you start acting in a way that demonstrates that you are no longer harmless, others’ reactions to you will likely change as a result.",
            "reference": "V20 Corebook; PG 487",
            "clan": None,
        },
        {
            "name": "Natural Leader",
            "rating": [1],
            "description": "You are gifted with a certain magnetism to which others naturally defer. You receive two extra dice when making Leadership rolls. You must have a Charisma rating of 3 or greater to purchase this Merit.",
            "reference": "V20 Corebook; PG 487",
            "clan": None,
        },
        {
            "name": "Prestigious Sire",
            "rating": [1],
            "description": "Your sire has or had great status in her Sect or Clan, and this has accorded you a certain amount of prestige. Though your sire may no longer have any dealings with you, the simple fact of your ancestry has marked you forever. This prestige might aid you greatly in dealings with other vampires, or it might engender jealousy or contempt.",
            "reference": "V20 Corebook; PG 488",
            "clan": None,
        },
        {
            "name": "Protégé",
            "rating": [1],
            "description": "Your sire watched you for some time before Embracing you, and spoke glowingly of you to acquaintances. These vampires may be inclined to look favorably on you by dint of your sire’s recommendation; you are at -1 difficulty on Social rolls with all those who’ve heard good things about you.",
            "reference": "V20 Corebook; PG 488",
            "clan": None,
        },
        {
            "name": "Rep",
            "rating": [1],
            "description": "Your fame has exceeded the bounds of your Sect. Everyone knows who you are, what you’ve done and what you’re supposed to have done (which might not be the same thing). The publicity can be good or bad; what matters is that everybody knows your name. Whether individuals outside of your immediate social circle know enough to match your face to your name is a different matter.",
            "reference": "V20 Corebook; PG 488",
            "clan": None,
        },
        {
            "name": "Sabbat Survivor",
            "rating": [1],
            "description": "You’ve lived through at least one Sabbat attack or attempted recruitment. Your experience helps you anticipate situations where you might potentially be endangered by the Sabbat once again. You are at -1 difficulty on all Perception rolls when it comes to Sabbat-based matters. This Merit is generally taken by groups in conflict with the Sabbat, and comes into play most frequently as a means of avoiding ambushes.",
            "reference": "V20 Corebook; PG 488",
            "clan": None,
        },
        {
            "name": "Boon",
            "rating": [1, 6],
            "description": "Someone owes you a favor. The vampire in your debt might be the lowliest neonate in the city or might be the Prince herself; it all depends on how many points the Merit costs. You only have that single favor owed you (unless you take the Merit multiple times), so us-ing it properly is of paramount importance. Depending on status and other factors, the vampire who owes you a favor may well resent his debt, and might go out of his way to “settle” it early — even going so far as to create situations from which he must “rescue” you and thus clear the slate.",
            "reference": "V20 Corebook; PG 488",
            "clan": None,
        },
        {
            "name": "Bullyboy",
            "rating": [2],
            "description": "You’re part of the brute squad the local Sheriff or Bishop calls on when he needs some muscle. As a result, you get in on action that others miss entirely, score points with those in power, and occasionally get a chance to act outside of the law. How far outside the law you can go depends on circumstance and how much the vampire you report to likes you.",
            "reference": "V20 Corebook; PG 488",
            "clan": None,
        },
        {
            "name": "Entrepreneur",
            "rating": [2],
            "description": "Making money comes naturally to you, and you know what it takes to succeed. All rolls involving acquiring money through business dealings have their difficulty reduced by 2.",
            "reference": "The Black Hand: A Guide to The Tal'Mahe'Ra; PG 178",
            "clan": None,
        },
        {
            "name": "Old Pal",
            "rating": [2],
            "description": "An acquaintance from your breathing days was Em-braced at the same time you were. Fortunately, your friendship has endured even death and unlife, and you find a constant source of support and aid in your old friend. She expects the same of you, which isn’t always convenient, but at least you each have someone to hang onto who remembers the good old nights — and days. The Storyteller should play the Old Pal as a very loyal Ally.",
            "reference": "V20 Corebook; PG 488",
            "clan": None,
        },
        {
            "name": "Lawman's Friend",
            "rating": [2],
            "description": "For whatever reason (maybe your winning smile or perhaps just your superb groveling technique), the local Sheriff or Bishop in charge of discipline likes you. He’s inclined to overlook your minor trespasses and let you in on things you’re not supposed to know about. He even gives you warnings about occasional crack-downs and times when the higher-ups aren’t feeling generous. Of course, abusing this connection might well turn a friendly vampire into an enemy — and the change might not be apparent until it’s too late.",
            "reference": "V20 Corebook; PG 488",
            "clan": None,
        },
        {
            "name": "Open Road",
            "rating": [2],
            "description": "Unlike many Kindred, you like to travel. You have a solid knowledge of safe travel routes and methodologies, not to mention haven space available in any number of destinations. Unless someone out there knows your exact route and is specifically looking for you, you can move between cities unimpeded by random encounters with Lupines, overzealous state troopers, and the like.",
            "reference": "V20 Corebook; PG 488",
            "clan": None,
        },
        {
            "name": "Sanctity",
            "rating": [2],
            "description": "This Merit is sometimes called the halo effect; everyone considers you pure and innocent, though not necessarily naïve. You have a saint-like quality that is hard to pinpoint but cannot be denied. You are trusted, even if you are not trustworthy. At the Storyteller’s discretion, you tend to receive lesser punishments for wrongdoing, and you are liked by most.",
            "reference": "V20 Corebook; PG 488",
            "clan": None,
        },
        {
            "name": "Scholar of Enemies",
            "rating": [2],
            "description": "You have taken the time to learn about and specialize in one particular enemy of your Sect. You are aware of at least some of the group’s customs, strategies, abilities, and long-term goals, and can put that knowledge to good use. This Merit is worth a -2 difficulty for all non-combat rolls pertaining specifically to the subject of your specialization. On the other hand, you are at a +1 difficulty when it comes to dealing with other enemies, simply because you’re so thoroughly focused on your field.",
            "reference": "V20 Corebook; PG 488",
            "clan": None,
        },
        {
            "name": "Scholar of Others",
            "rating": [2],
            "description": "This Merit functions identically to Scholar of Ene-mies, except that it applies to a group that is not neces-sarily inimical to your Sect.",
            "reference": "V20 Corebook; PG 488",
            "clan": None,
        },
        {
            "name": "Friend of the Underground",
            "rating": [3],
            "description": "While you’re not a Nosferatu, you know your way around the sewers, tunnels, ducts, subway tubes, and other subterranean passages of your hometown. The local Nosferatu (and any other creatures dwelling down in the muck) may not actually like you, but they’re not inclined to kill you on sight when they see you in their territory. You are at -1 difficulty on any rolls involving the subterranean world (sneaking from place to place underground, finding routes into sub-basements, and so on). Nosferatu cannot purchase this Merit.",
            "reference": "V20 Corebook; PG 488",
            "clan": None,
        },
        {
            "name": "Mole",
            "rating": [3],
            "description": "You have an informer buried in one of your Sect’s enemy organizations who funnels you all sorts of information as to what her peers are up to. What you do with the information is up to you, but abusing the knowledge might be a good way to get your informer killed. The other side has spies too….",
            "reference": "V20 Corebook; PG 488",
            "clan": None,
        },
        {
            "name": "Rising Star",
            "rating": [3],
            "description": "You’re one of the up-and-comers in the city, a rising star in your Sect. Everyone wants to know you and be your friend, even as those in power groom you for positions of greater responsibility. You are at -1 difficulty on all Social rolls against any vampires in your Sect who aren’t actively opposing your ascent.",
            "reference": "V20 Corebook; PG 488",
            "clan": None,
        },
        {
            "name": "Broken Bond",
            "rating": [4],
            "description": "You were once blood-bound but have secretly slipped the leash, and you are free to act as you will once more. Your regnant has no idea that you are not in fact bound, and continues to treat you as if you were. At Storyteller discretion, the experience of having been bound once may render you immune to ever being enthralled again. Sabbat vampires cannot take this Merit.",
            "reference": "V20 Corebook; PG 488",
            "clan": None,
        },
        {
            "name": "Clan Friendship",
            "rating": [4],
            "description": "One particular Clan (not your own) has a special liking for you. You might have done the Clan as a whole a favor at some point, or perhaps you’re just a loud voice in support of their aims. Whatever the case, you’re at -2 difficulty on all friendly Social rolls involving members of the Clan in question. Of course, the reaction your cozy relationship with another Clan is likely to draw from your own Clan leaders is an entirely different can of worms",
            "reference": "V20 Corebook; PG 488",
            "clan": None,
        },
        {
            "name": "Primogen/Bishop Friendship",
            "rating": [4],
            "description": "The ruling vampires of the city value you and your opinions. You are called in to consult on decisions, and your recommendations carry great weight. Your position may not be an official one, but it’s powerful nonetheless.",
            "reference": "V20 Corebook; PG 488",
            "clan": None,
        },
        {
            "name": "Trophy Allegiance",
            "rating": [4],
            "description": "Similar to the Clan Friendship Merit (pg. 489, V20) Trophy Allegiance opens doors and allows the character to be treated favorably by a specific Clan. The character has earned the Trophy from the Clan in question for taking down one of the Anathema. Word has spread throughout that Clan, that members should offer assistance and rewards to the character for their deed.  While the Trophy itself has likely already been covered with specific rewards, this Social Merit reflects more of a general goodwill and offers the character -2 difficulty on all friendly Social rolls involving members of the Trophy Clan who are familiar with the Alastor’s deeds. Additionally, the character’s reputation may earn her the occasional small favor such as the use of a haven, a loaner car, access to information from Trophy Clan members. Note: This Merit is only available to Alastor characters who have killed an Anathema and earned a Trophy.",
            "reference": "Dread Names Red List; PG 100",
            "clan": None,
        },
        {
            "name": "Arcane",
            "rating": [1, 5],
            "description": "Some vampires have a strange ability to slip from notice, which manifests as an aura of forgetfulness. Those trying to remember the vampire experience a sensation of jamais-vu. The ability may be deliberately developed, or the Kindred could simply be too ordinary to pay attention to. Though not similar to Obfuscate, Arcane doesn’t help in combat situations — the vampire can’t literally vanish. However, someone searching for them may well fail, as no one remembers the vampire or can give a reliable description. Each point taken subtracts one die from any dice pools used to actively locate the vampire or recall her from memory. Those with this Merit can choose to “turn off” Arcane if they wish. As a passive trait, it doesn’t help on Stealth rolls or other overt attempts to hide. If you have any dots in Status or Fame, Arcane ceases to function while you possess them.",
            "reference": "The Black Hand: A Guide to The Tal'Mahe'Ra; PG 177",
            "clan": None,
        },
        {
            "name": "Paragon",
            "rating": [7],
            "description": "Others find you particularly compelling. Select one Background from the following group: Allies, Contacts, Domain, Fame, Herd, Influence, Mentor, Resources, Retainers, or Status. You receive one free dot in that Background, and your maximum Trait score in that Background may exceed normal Generational limits by one.",
            "reference": "The Black Hand: A Guide to The Tal'Mahe'Ra; PG 178",
            "clan": None,
        },
        {
            "name": "Deceptive Aura",
            "rating": [1],
            "description": "Your aura is unnaturally bright and colorful for a vampire. You register as a mortal on all attempts to read your aura.",
            "reference": "V20 Corebook; PG 493",
            "clan": None,
        },
        {
            "name": "Healing Touch",
            "rating": [1],
            "description": "Normally vampires can only seal the wounds they inflict from feeding by licking them. With but a touch, you can achieve the same effect, closing the puncture wounds left by drinking blood.",
            "reference": "V20 Corebook; PG 493",
            "clan": None,
        },
        {
            "name": "Inoffensive to Animals",
            "rating": [1],
            "description": "With rare exceptions, animals usually despise the Kindred. Some flee, others attack, but all dislike being in the presence of a vampire. You have no such problem. Animals may not enjoy being in your company, but they don’t actively flee from you.",
            "reference": "V20 Corebook; PG 493",
            "clan": None,
        },
        {
            "name": "Apostate",
            "rating": [2],
            "description": "Since their inception, Nergali Baali have subverted members of other Clans into their own ranks. Known as Apostates, initiates are first drained completely by a Baali nest-master, who then extracts the still-beating heart from a mortal victim, fills it with his own blood, and buries it in a pool of gore within a Well of Sacrifice. The initiate swims through the dismembered bodies and viscous remains to find and consume the heart. In this way, Nergali do not make a victim of those they Embrace; prospective members must claim it through strength of will. Apostates replace any one in-Clan Discipline with Daimoinon, but in turn gain the Baali Clan weakness on top of their standard Clan weakness. Apostates can still pass with relative ease for members of their former Clans, but any childe they Embrace is indistinguishable from a standard Baali. Further, such a childe shares none of the Clan Disciplines or weaknesses of their sire’s former Clan, save those Disciplines that are innate to the Baali. Apostates do not lose levels in the Discipline they choose to exchange for Daimoinon, but further levels in that Discipline are purchased at out-of-Clan costs. Baali may not take this Merit.",
            "reference": "The Black Hand: A Guide To The Tal'Mahe'Ra; PG 178",
            "clan": None,
        },
        {
            "name": "Medium",
            "rating": [2],
            "description": "You possess the natural affinity to sense and hear spirits, ghosts, and shades. Though you cannot see them, you can sense them, speak to them and, through pleading or cajoling, draw them to your presence. You may call upon them for aid or advice, but there will always be a price. Also, your difficulty is reduced by two for all Awareness rolls involving the spirits of the dead.",
            "reference": "V20 Corebook; PG 493",
            "clan": None,
        },
        {
            "name": "Magic Resistance",
            "rating": [2],
            "description": "You have an inherent resistance to the rituals of the Tremere and the spells of the mages of other Clans. The difficulty of all such magic, both malicious and beneficent, is two higher when directed at you. You may never learn magical Disciplines such as Thaumaturgy and Necromancy.",
            "reference": "V20 Corebook; PG 493",
            "clan": None,
        },
        {
            "name": "Without a Trace",
            "rating": [2],
            "description": "When in the wilderness, the earth fills in your footprints. You leave no noticeable traces, not even a scent. Normal attempts at tracking automatically fail. Supernatural attempts are done with a +2 difficulty.",
            "reference": "The Black Hand: A Guide To The Tal'Mahe'Ra; PG 179",
            "clan": None,
        },
        {
            "name": "Hidden Diablerie",
            "rating": [3],
            "description": "The tell-tale black streaks of diablerie do not manifest in your aura.",
            "reference": "V20 Corebook; PG 493",
            "clan": None,
        },
        {
            "name": "Lucky",
            "rating": [3],
            "description": "You were born lucky — or else the Devil looks after his own. Either way, you may repeat any three failed rolls per story, including botches, but you may try only once per failed roll.",
            "reference": "V20 Corebook; PG 493",
            "clan": None,
        },
        {
            "name": "Oracular Ability",
            "rating": [3],
            "description": "You can see and interpret signs and omens. You are able to draw advice from these omens, for they pro-vide hints of the future and warnings of the present. When the Storyteller feels that you are in position to see an omen, you will be required to make a Perception + Awareness roll, with the difficulty relative to how well the omen is concealed. If successful, you may then roll Intelligence + Occult to interpret what you have seen; the difficulty is again relative to the complexity of the omen.",
            "reference": "V20 Corebook; PG 493",
            "clan": None,
        },
        {
            "name": "Spirit Mentor",
            "rating": [3],
            "description": "You have a ghostly companion and guide. The identity and exact powers of this spirit are up to the Story-teller, but it can be called upon in difficult situations for help and guidance.",
            "reference": "V20 Corebook; PG 493",
            "clan": None,
        },
        {
            "name": "Mark of Caine",
            "rating": [4],
            "description": "Over the course of history, some of these rituals have been lost, either due to the death of Sect members, or because the ritus simply was not as integral to the Sect’s survival in the modern world. One of these lost ritae was the Mark of the Father, which offered protection against weapons of faith. As faith has declined in the modern world, the ritus was used less and less, until eventually, priests who know the ritae have become all but extinct. Some vampires who participated in the lost Mark of Caine ritus were especially blessed, and still bear a faint sign of favor. Such vampires are always old, pre-dating the first Sabbat Civil War, and once had this ritual cast upon them by a powerful practitioner. These vampires have a small, faded mark upon their forehead that resembles the Hebraic letter tav. Those who bear the Mark of Caine gain a twisted form of True Faith. They can use the effects of the first dot of True Faith (V20, pp. 372-373) – they must use symbols of Caine as “holy symbols.” Further, they get +2 dice to resist mortal True Faith. Only vampires on spiritual Paths of Enlightenment can use this Merit – if a Cainite reverts to Humanity or succumbs to wassail, all benefit from this Merit is lost forever.",
            "reference": "Rites of the Blood; PG 41",
            "clan": None,
        },
        {
            "name": "True Love",
            "rating": [4],
            "description": "You have discovered, perhaps too late, a true love. He or she is mortal, but is the center of your existence, and inspires you to keep going in a world of darkness and despair. Whenever you suffer, the thought of your true love gives you the strength to persevere. This Merit grants you one automatic success on all Willpower rolls, which can be negated only by a botch die. This can be a great gift but also a hindrance, for your true love may require protection and occasionally rescue.",
            "reference": "V20 Corebook; PG 493",
            "clan": None,
        },
        {
            "name": "Additional Discipline",
            "rating": [5],
            "description": "You can take one additional Discipline (Storyteller discretion) as if it were a Clan Discipline. All costs to learn that Discipline are paid out as if it were native to your Clan. A character cannot take this Merit more than once, and Caitiff vampires cannot take this Merit.",
            "reference": "V20 Corebook; PG 494",
            "clan": None,
        },
        {
            "name": "Psychic Leech",
            "rating": [5],
            "description": "At the cost of one Willpower point, you may feed on the Willpower of your victims from a distance. The consumed Willpower strengthens the potency of your own blood, effectively transforming it into temporary blood that dissipates at the end of the night. These temporary blood points may be spent just like regular blood points, but cannot be lost due to damage or blood drain, do not affect hunger rolls for frenzy, and may not be used to create or sustain blood bonds or ghouls. To activate this ability, the target must have at least one of your blood points in their system, and must be engaged in eye contact with you.",
            "reference": "The Black Hand: A Guide To The Tal'Mahe'Ra; PG 179",
            "clan": None,
        },
        {
            "name": "Unbondable",
            "rating": [5],
            "description": "You are immune to being blood bound. Tremere cannot take this Merit.",
            "reference": "V20 Corebook; PG 494",
            "clan": None,
        },
        {
            "name": "Nine Lives",
            "rating": [6],
            "description": "Fate has granted you the opportunity to come as close to Final Death as anyone can get and still survive. When a roll occurs that would result in your death, the roll is made again. If the next roll succeeds, then you live — and one of your nine lives is used up. If that subsequent roll fails, then another reroll is made, until either a successful roll occurs or your nine lives are used up. The Storyteller should keep careful count of how many lives the character has remaining.",
            "reference": "V20 Corebook; PG 494",
            "clan": None,
        },
        {
            "name": "True Faith",
            "rating": [7],
            "description": "You have a deep-seated faith in and love for God, or whatever name you choose to call the Almighty. You begin the game with one point of True Faith (see the sidebar on p. 372); this Trait adds one die per point to all Willpower and Virtue rolls. You must have a Humanity of 9 or higher to choose this Merit, and if you lose even a single point, all your Faith points are lost and may be regained only when the lost Humanity is recovered. Individuals with True Faith are capable of performing magical acts akin to miracles, but the exact nature of those acts are up to the Storyteller.",
            "reference": "V20 Corebook; PG 494",
            "clan": None,
        },
        {
            "name": "Sectarian Ally",
            "rating": [1],
            "description": "You have a close friend in one of the Kindred sects. Perhaps you are a warrior who is in touch with one of the antitribu, a vizier who shares common business interests with some Camarilla Ventrue, or a sorcerer who corresponds with one of the rare blood magicians of the Anarch Movement. Your ally can help you navigate the currents of their sect, but they might want something in exchange from time to time.",
            "reference": "Lore of the Clans; PG 26",
            "clan": "Assamite",
        },
        {
            "name": "Thousand Meter Killer",
            "rating": [1],
            "description": "You have proven yourself worthy to join the Thousand Meter Club through your remarkable skill with the sniper rifle. The difficulty of all rolls associated with sniping is reduced by -1. You also double the normal range when using a sniper rifle as a weapon.",
            "reference": "Lore of the Clans; PG 26",
            "clan": "Assamite",
        },
        {
            "name": "Fury's Focus (Prerequisite: Path of Entelechy)",
            "rating": [3],
            "description": "Brujah who have devoted themselves to mastering their frenzies through the Path of Entelechy sometimes find tangible benefits resulting from their efforts. A Brujah with this Merit may briefly delay the full onset of frenzy. The player spends a Willpower point at the onset of frenzy and then rolls the Brujah’s Entelechy rating. The difficulty is one higher than the original roll to resist frenzy. The Brujah still frenzies, but the player controls her character’s actions for one turn per success. Furthermore, when the period of partial control ends and the Brujah loses control, the difficulty of any degeneration rolls triggered by sins committed during the frenzy are reduced by the number of successes rolled, to a minimum difficulty of 4.",
            "reference": "Lore of the Clans; PG 48",
            "clan": "Brujah",
        },
        {
            "name": "Dynamic Personality",
            "rating": [5],
            "description": "Your natural charisma draws mortals to you like groupies to a rock star. Consequently, it is easier for you to acquire certain Backgrounds related to mortals. In addition to any Backgrounds acquired at character creation or through roleplay, you can purchase new Backgrounds with experience points at the end of each story. The available Backgrounds are Allies, Contacts, Herd, Retainers, and each new dot costs the current rating in experience points.",
            "reference": "Lore of the Clans; PG 48",
            "clan": "Brujah",
        },
        {
            "name": "Drug Resistance",
            "rating": [2],
            "description": "The Setite religion is one fraught with vices, both to compromise enemies and to enlighten initiates. Cultists tend to build up a tolerance to the substances they take directly (if human or ghoul) or through the blood of prey (if Kindred). You are unusually resistant to alcohol, narcotics, and similar addictive substances. You can pretend to be far more under the influence than you are in order to take advantage of an opponent. All rolls to resist the effects of such substances are at -2 difficulty.",
            "reference": "Lore of the Clans; PG 67",
            "clan": "Followers of Set",
        },
        {
            "name": "Addictive Blood",
            "rating": [3],
            "description": "You don’t just peddle narcotics; through the blessings of the Dark God, you are the perfect drug. Your blood is especially delicious to others, Kindred or kine. Whoever tastes your blood must, during any subsequent scenes that they meet you, drink again or spend a Willpower point to avoid the pangs of craving. These cravings add +2 difficulty to any Mental or Social rolls. Setites with this Merit find it much easier to blood bond an opponent, as once they have tasted the tainted vitae, they will do almost anything to drink it again.",
            "reference": "Lore of the Clans; PG 67",
            "clan": "Followers of Set",
        },
        {
            "name": "Setite Initiate",
            "rating": [5],
            "description": "You were Embraced into a Clan other than the Followers of Set. However, you have accepted the Setite religion, undergone the vetting process and rites, and have been formally inducted into the cult. You have access to Serpentis and Setite Blood Sorcery (though you pay out-of-Clan costs to learn the,). You may even study one of their Paths of Enlightenment. It is important to note that “Setites” from other Clans or bloodlines are not treated as second-class citizens. You are no longer a dupe they can string along. Once you are in, you are a sibling of faith, which is a much more important distinction than blood. An outsider accepting the Dark God is a joyous event, even to the most conservative elder. There are even rumors of non-Kindred supernatural beings joining the cult.",
            "reference": "Lore of the Clans; PG 67",
            "clan": "Followers of Set",
        },
        {
            "name": "Hive-Minded",
            "rating": [1, 2],
            "description": "Your Animalism works on insects and other creepy-crawlies in addition to mammalian animals. If you select the two-point version of this merit, your Protean forms may take the form of an insectoid swarm rather than a single creature (though the swarm must be of a size equivalent to a wolf or a bat, as appropriate).",
            "reference": "Lore of the Clans; PG 86",
            "clan": "Gangrel",
        },
        {
            "name": "Skald",
            "rating": [2],
            "description": "Anytime you make an Occult roll to know a fact about vampiric history, you may add a die to your dice pool. Further, you have exceptional memory for oral histories, and you are a quick study when it comes to memorizing large amounts of rote information. This is not true eidetic memory, but constitutes the ability to memorize poetic eddas, codes, or complex messages with only a few hours of study.",
            "reference": "Lore of the Clans; PG 87",
            "clan": "Gangrel",
        },
        {
            "name": "Lesser Mark of the Beast",
            "rating": [4],
            "description": "Common to the Gangrel known as the Knights of Avalon, you are able to control how your Beast manifests more than others do. Whenever you would gain an animalistic feature (V20, p. 55), roll your current Willpower (difficulty 12 - Humanity rating, maximum 9). If successful, you manage to channel your humanity to avoid gaining an animalistic feature. However, your Beast is further from you, making you at +2 difficulty to rolls involving Animalism or Protean (or combo Disciplines involving those powers) for the rest of the evening. Vampires on a Path of Enlightenment lose all access to this Merit.",
            "reference": "Lore of the Clans; PG 87",
            "clan": "Gangrel",
        },
        {
            "name": "Totemic Change",
            "rating": [5],
            "description": "Your Protean forms are flexible; you may choose a different animal form each time you change shape. The form you choose each time must follow all the conventions and rules of standard Protean animal shapes (see p. 91); you simply may choose to appear as a different animal each time you take Beast Form.",
            "reference": "Lore of the Clans; PG 87",
            "clan": "Gangrel",
        },
        {
            "name": "Cannibal",
            "rating": [1],
            "description": "Most vampires can’t eat food, and even those who can force it down, don’t gain sustenance from it. Like them, you still can’t stomach the crap most mortals eat. Human meat, on the other hand, brings you great joy. It can be baked, fried, or even raw, and you can tuck right in, and even gain sustenance. Even other vampires look askance at Kindred who devour their prey, though the Dunsirn applaud your respect for tradition. In addition to the blood points every human can provide, you can cannibalize a mortal and gain even more. An average human can provide up to seven helpings of meat (one per health level). Each helping provides you with one blood point.",
            "reference": "Lore of the Clans; PG 106",
            "clan": "Giovanni",
        },
        {
            "name": "Consanguineous Resistance",
            "rating": [1],
            "description": "Your character cannot be blood bound by anyone who shares his mortal bloodline. That is, if you were born into the Giovanni family, you cannot be bound by anyone else who was born a Giovanni, though you can still be bound by, say, a Pisanob of the Giovanni Clan, or by Kindred of any other Clan. Similarly, a Dunsirn with Consanguineous Resistance could not be bound by others who were born into the mortal Dunsirn family, but could be bound by a Milliner of the Giovanni Clan. The Giovanni are extremely suspicious of anyone known to manifest this quirk. Although this blood-borne aberration hasn’t been documented, a few savvy Giovanni have a rough idea of what it is and does. It’s generally associated with being a rebellious young smartass who needs to be put down. This is not as unfair as it sounds; by the time a bond resistance is really obvious, it’s likely because a punishment isn’t working. A character who is discovered to have this trait probably earns her sire’s hostility at the very least.",
            "reference": "Lore of the Clans; PG 106",
            "clan": "Giovanni",
        },
        {
            "name": "Mortuario",
            "rating": [2, 4],
            "description": "You died. Perhaps you were murdered, or simply had a car accident. Whatever the cause, you were gone. But your sire found you too useful, or couldn’t let you go. You were Embraced using the Ferryman’s Recall ritual (see p. 109). The Embrace left you with the scars of your death, eternal tracework reminders of your trip to the other side. It also left you with the taut, pallid complexion of the dead. In addition to the traditional weakness of your Clan, you also suffer disfigurement from your time as a true corpse. While you are able to heal yourself just like any other vampire, the wounds do not heal cleanly. You retain the scars of every experience. Depending on the nature of the damage, this can make social dealings exceedingly difficult, and may decrease your Appearance dots over time (even to 0). However, your time across the Shroud also gave you a natural feel for necromantic blood magic. The difficulties of all Necromancy rolls are reduced by two. This trait costs 4 points for characters who already have an appearance of 0 (such as Samedi and the Harbingers of Skulls), or 2 points for any other Kindred. It is an incredibly rare condition even among the Giovanni, and essentially unknown outside the Clan. Giovanni with this Merit generally arouse the superstition of their Clan, and are treated with a definite wariness, particularly by Anziani. Characters with the Mortuario Merit may not also possess the Sanguine Incongruity Merit or similar flaws such as Monstrous.",
            "reference": "Lore of the Clans; PG 106",
            "clan": "Giovanni",
        },
        {
            "name": "Sanguine Incongruity",
            "rating": [5],
            "description": "Giovanni with this atavism are few and far between. Kindred possessing it do not bear the traditional Giovanni Clan weakness, the so-called Curse of Lamia; their Kiss causes no more damage than the blood loss itself. These vampires acquire a peculiar pallor upon their Embrace, however — they look like corpses, and no amount of blood ingestion can flush their features (as other vampires are able to do). Indeed, the bearer of this Merit more closely resembles the Clan’s Cappadocian ancestors, and they have a slightly unnerving air about them. As a result, all rolls involving a Social attribute (Charisma, Manipulation, or Appearance) are at +1 difficulty. Giovanni with this Merit are afforded wide berth, as the Giovanni tend to be quite superstitious about it. Characters with the Sanguine Incongruity Merit may not also possess the Mortuario Merit.",
            "reference": "Lore of the Clans; PG 106",
            "clan": "Giovanni",
        },
        {
            "name": "Court Favorite",
            "rating": [1, 5],
            "description": "While the Courts of Blood are usually difficult to sway, you have become very good at shifting the balance. A mixture of experience and political empathy allow you to know just the right way to nudge the decision in your direction, or perhaps for that of your client. Any roll made that will affect the decision in a Court of Blood is granted a bonus or penalty (whichever is in your favor) in dice equal to the level you have of this Merit.",
            "reference": "Lore of the Clans; PG 121",
            "clan": "Lasombra",
        },
        {
            "name": "Eyes of Shadow",
            "rating": [1, 4],
            "description": "There is something about your eyes that makes you look dark and dangerous. Making eye contact with you is like staring into the Abyss. It may not be obvious why, but anyone you talk to gets a chill when they meet your gaze. The difficulty for any Intimidation roll is reduced by the number of points in this Merit (to a minimum of 2).",
            "reference": "Lore of the Clans; PG 121",
            "clan": "Lasombra",
        },
        {
            "name": "Bigger Boys Came",
            "rating": [2],
            "description": "When someone uses their contacts to their advantage, you can try to use yours to overrule them. You might get an editor to quash a reporter’s story, or get a gang boss to stop his thugs taking down a rival. To do this you must make a roll using Manipulation + Contacts (difficulty 8). If you can get more successes than the Contacts rating of your opponent, their contacts fail to come through for them.",
            "reference": "Lore of the Clans; PG 121",
            "clan": "Lasombra",
        },
        {
            "name": "Call of the Sea",
            "rating": [2],
            "description": "There is something about the sea that makes you feel at home. You are in tune with the tides and rhythm of the ocean. When on a boat in the ocean or on a river, you may add a die to all your dice pools except for Disciplines.",
            "reference": "Lore of the Clans; PG 122",
            "clan": "Lasombra",
        },
        {
            "name": "Controllable Night Sight",
            "rating": [2],
            "description": "Your night vision is extraordinarily good, even for a vampire. The deepest shadows are like looking into a well-lit room for you. However, in normal light or bright conditions, you have to switch back to less-sensitive vision, or the weakest light quickly blinds you. While your night sight is active, you suffer no penalties for the dark and can see perfectly well. Should you use it in well-lit conditions; you suffer a penalty inversely proportional to the usual penalties for darkness.",
            "reference": "Lore of the Clans; PG 122",
            "clan": "Lasombra",
        },
        {
            "name": "Secret Stash",
            "rating": [2, 5],
            "description": "You have several resources, sleeper agents, or followers hidden away for a rainy day. For each level of this Merit you have one unassigned background point “sitting in storage” (2 gives you one point, 3 gives you two points, and so on). At any time, you may spend as many of them as you like to increase your level in Allies, Contacts, Herd, Influence, Mentor, Resources, or Retainers. Once spent, the points remain assigned permanently, but until then they cannot be affected by anything. This allows the vampire to create a new resource in an instant, without requiring the expenditure of experience points or awaiting a downtime. The vampire is not really gaining new levels, but revealing levels he has had all along.",
            "reference": "Lore of the Clans; PG 122",
            "clan": "Lasombra",
        },
        {
            "name": "Aura of Command",
            "rating": [3],
            "description": "Whether you are good at barking orders or simply have a commanding tone, people tend to do what you tell them to do. You are not so much a natural leader as a born commander. When using the Leadership skill to get others to obey you, the difficulty is reduced by two.",
            "reference": "Lore of the Clans; PG 122",
            "clan": "Lasombra",
        },
        {
            "name": "King or Queen of Shadow",
            "rating": [4],
            "description": "It is hard to hold onto your Humanity within the Sabbat, or even simply as a vampire. Your ability to empathize with the kine makes it more difficult. However, you have found a way to draw strength from that empathy. Any degeneration checks you make while on Path of Humanity reduce their difficulty by two.",
            "reference": "Lore of the Clans; PG 122",
            "clan": "Lasombra",
        },
        {
            "name": "Long-Term Planning",
            "rating": [4],
            "description": "You never leave anything to chance; every action is a carefully considered stratagem. Once per session you may declare an action you are about to take is actually “all part of your plan” and reduce its difficulty by two points. The Storyteller may veto the use of this ability on particular rolls. The player and Storyteller should keep a note of each of these occasions and decide how they are linking together into a grand scheme.",
            "reference": "Lore of the Clans; PG 123",
            "clan": "Lasombra",
        },
        {
            "name": "Instrument of God",
            "rating": [5],
            "description": "Your self-confidence comes not from a belief in your own abilities, but due to a direct manifesto from the Lord. You have a divine purpose and He works through you, even though your goals may seem anything but holy. Whether it is because of you powerful will or an actual connection to the divine, you gain three additional dice to resist the powers of True Faith when they are used against you.",
            "reference": "Lore of the Clans; PG 123",
            "clan": "Lasombra",
        },
        {
            "name": "Distracting Aura",
            "rating": [2],
            "description": "Reading an aura using Auspex requires the viewer to focus on recurring patterns and colors to detect a target’s emotional state. Because of the unique state of your psyche, your aura is even harder to read than most. All uses of Aura Perception are at a +2 difficulty against you.",
            "reference": "Lore of the Clans; PG 142",
            "clan": "Malkavian",
        },
        {
            "name": "Prophetic Dreams",
            "rating": [2],
            "description": "You have dreams during your daylight sleep. Dreams you remember. Sometimes, they even come true. Rather than regain a point of Willpower when you rest during the day, you may choose to have the Storyteller give your character a lucid dream featuring foreshadowing about upcoming events, characters, and situations.",
            "reference": "Lore of the Clans; PG 142",
            "clan": "Malkavian",
        },
        {
            "name": "Cold Read",
            "rating": [3],
            "description": "Whenever you meet someone for the first time, you may spend a number of points of Willpower equal to your Perception. For each point spent, you may ask the Storyteller one question about the character. The Storyteller must either answer truthfully or let you take the Willpower point back to you to avoid answering the question.",
            "reference": "Lore of the Clans; PG 142",
            "clan": "Malkavian",
        },
        {
            "name": "Foul Blood",
            "rating": [1],
            "description": "Your blood is vile; in fact, it tastes so disgusting it requires a Willpower roll (difficulty 6) just to avoid gagging and retching after tasting it. If someone is foolish enough to attempt diablerie on you, they need to succeed in three (difficulty 9) Willpower rolls to go through with it. The blood is so disgusting that no one can keep it down long enough to use it to become a ghoul, either.",
            "reference": "Lore of the Clans; PG 160",
            "clan": "Nosferatu",
        },
        {
            "name": "Lizard Limbs",
            "rating": [1],
            "description": "Like a lizard, you are able to actually shed parts of your body. By spending a blood point and a little effort, you can detach a hand or foot, or even an arm or leg. This might be to escape bonds or a grapple. Unfortunately, the appendage will not reattach, and you will have to regrow that over time (usually a couple of days for a hand or foot, and a week for a limb). You also suffer a -3 dice pool penalty to actions that would require the use of more limbs.",
            "reference": "Lore of the Clans; PG 160",
            "clan": "Nosferatu",
        },
        {
            "name": "Long Fingers",
            "rating": [1],
            "description": "You have been blessed with unusually long and graceful fingers. This means you have an easier time with fine manipulation as well as grappling tasks, gaining an extra die when attempting such actions.",
            "reference": "Lore of the Clans; PG 160",
            "clan": "Nosferatu",
        },
        {
            "name": "Monstrous Maw",
            "rating": [1],
            "description": "You have either oversized tusks for fangs, or a huge mouth full of sharp teeth. Whatever form it takes, your mouth is that of a monster. When attacking with a bite you do an additional point of damage. You may also add a die to your Intimidation dice pool when you smile.",
            "reference": "Lore of the Clans; PG 160",
            "clan": "Nosferatu",
        },
        {
            "name": "Piscine",
            "rating": [1],
            "description": "Water is a far more comfortable environment for you, be it the sea or sewer effluent. Rolls involving swimming or underwater movement have their difficulty reduced by 1.",
            "reference": "Lore of the Clans; PG 160",
            "clan": "Nosferatu",
        },
        {
            "name": "Slimy",
            "rating": [1],
            "description": "You secrete an ooze, which is as disgusting as it sounds. The ooze covers your entire body and soaks into your clothes. It makes you slippery and difficult to hold, requiring opponents to gain two more successes to grapple you. The dampness also makes you a little fire resistant, reducing your difficulty to soak fire damage by 1.",
            "reference": "Lore of the Clans; PG 160",
            "clan": "Nosferatu",
        },
        {
            "name": "Spawning Pool",
            "rating": [1, 3],
            "description": "You have a spawning pool of your own (or possibly donate heavily to the Clan’s main pool). Creating such a pool takes time, and requires regular infusions of blood, at least six blood points a week for a year. The Merit grants its level as a dice pool bonus to the Nosferatu’s use of Animalism in their home city, but only with animals considered vermin, such as rats and cockroaches. Essentially the bonus is only available for creatures that might conceivably drink regularly from the tainted blood. Once established, the spawning pool requires twice its level in blood points each week to it. Without proper maintenance, its level will drop by one. It can be rebuilt by maintaining it at the new level and adding four additional blood points each week for six months. The Merit cannot be improved above its initial level, as this also represents the convenience of its location and the variety of creatures that might find it.",
            "reference": "Lore of the Clans; PG 160",
            "clan": "Nosferatu",
        },
        {
            "name": "Tunnel Rat",
            "rating": [1, 5],
            "description": "You are remarkably adept at moving through the underground tunnels that you call your home. When attempting to navigate, escape, or track through sewers and underground places you know, you gain an additional die for every point you have in this Merit.",
            "reference": "Lore of the Clans; PG 160",
            "clan": "Nosferatu",
        },
        {
            "name": "Sleep Unseen",
            "rating": [2],
            "description": "The power of Obfuscate usually requires you to concentrate at least a little. However, you are able to lock the power on, allowing you to sleep while remaining hidden. To do so requires the expenditure of another blood point, but it will last throughout the day’s rest. Those with Auspex can still attempt to detect you, but mortals will be unaware of your sanctuary. This can be a useful trick for Kindred who like to travel.",
            "reference": "Lore of the Clans; PG 160",
            "clan": "Nosferatu",
        },
        {
            "name": "Tough Hide",
            "rating": [2],
            "description": "Your skin is much tougher than usual, possibly like that of a rhino or a lizard. This hide protects you against most normal damage, granting you an extra die when making a soak roll. However, this bonus does not apply against fire and sunlight.",
            "reference": "Lore of the Clans; PG 160",
            "clan": "Nosferatu",
        },
        {
            "name": "False Reflection",
            "rating": [3],
            "description": "Even when using their Obfuscate abilities, Nosferatu still show up in their true form when noticed by machines, such as cameras or video surveillance. With this ability, the Nosferatu can extend their power to recorded images and media. However, as with Mask of the Thousand Faces, the original image isn’t actually changed; it is just that people see it the way the Nosferatu wants it seen. Unfortunately, computers are not so easily fooled: if the image is used for facial recognition software (for instance), the computer will see the Nosferatu’s real face and fail to find a match. The Nosferatu has best take care how this power is used, as it may wear off in time. Some archived photos have given librarians a nasty surprise, years after going into storage.",
            "reference": "Lore of the Clans; PG 160",
            "clan": "Nosferatu",
        },
        {
            "name": "Patagia",
            "rating": [4],
            "description": "Your arms and legs have leathery flaps of skin between them, similar to that of a flying squirrel. While they make finding clothes a nightmare, they also allow you to glide for short distances, given enough height and a decent wind. The Storyteller might require an Athletics roll when it comes to landing.",
            "reference": "Lore of the Clans; PG 160",
            "clan": "Nosferatu",
        },
        {
            "name": "Rugged Bad Looks",
            "rating": [5],
            "description": "While you are still hideous, you are not quite as monstrous as most Nosferatu. You still have an appearance of 0, but you might pass for human in the right light. It is a still a good idea to cover up and stay in the shadows, but the sight of you (or even the smell of you) is not an instant breach of the Masquerade. Having said that, you are still ugly enough to unnerve the crap out of most people.",
            "reference": "Lore of the Clans; PG 160",
            "clan": "Nosferatu",
        },
        {
            "name": "Antitoxin Blood",
            "rating": [1],
            "description": "Although vampires are typically immune to mortal drugs and poisons, there are supernatural venoms that can affect Kindred physiology. A Ravnos with this Merit is immune to all forms of drugs and poisons, including the venoms and toxins of supernatural creatures or those created by supernatural powers.",
            "reference": "Lore of the Clans; PG 181",
            "clan": "Ravnos",
        },
        {
            "name": "Brahmin",
            "rating": [1],
            "description": "As a member of the Brahmin jati, you are a priest, artist, teacher, or other pillar of society. Perhaps you keep the lore of the Clan, or perhaps you act as an advisor to other Ravnos in need of wisdom. Once per session, if you fail an Academics or Expression roll, you may immediately reroll it. You do not have to purchase this Merit to be a member of the Brahmin jati, but only members of the Brahmin jati may have this Merit.",
            "reference": "Lore of the Clans; PG 182",
            "clan": "Ravnos",
        },
        {
            "name": "Kshatriya",
            "rating": [1],
            "description": "You are a member of the Kshatriya jati; perhaps you are a warrior, a descendant of rulers, or a member of the military. Your role is to protect the Ravnos in war, and govern in peace. Once per session, you regain a Willpower when you successfully use a combat maneuver (see V20, pp. 274-278). You do not have to purchase this Merit to be a member of the Kshatriya jati, but only members of the Kshatriya jati may have this Merit.",
            "reference": "Lore of the Clans; PG 182",
            "clan": "Ravnos",
        },
        {
            "name": "Legerdemain",
            "rating": [1],
            "description": "You’re extremely good at sleight of hand and other physical tricks. Difficulties when using Subterfuge for physical trickery, shell games, card tricks, and so forth, are decreased by two.",
            "reference": "Lore of the Clans; PG 182",
            "clan": "Ravnos",
        },
        {
            "name": "Mute Devotion",
            "rating": [1],
            "description": "Your Animalism carries an unusual side effect: it lingers in the minds of the beasts you speak with or control, lending them a certain resistance to others. When someone else attempts to command a creature you have previously controlled with Animalism, their difficulty levels are at +2.",
            "reference": "Lore of the Clans; PG 182",
            "clan": "Ravnos",
        },
        {
            "name": "Vaishya",
            "rating": [1],
            "description": "The Vaishya jati are tasked with utilizing influence, maintaining the human herds, and keeping finances. They are often seen as traders and merchants, but to the Ravnos, they are also a critical part of maintaining the Masquerade that hides vampires from mortal hunters. Once per session, you may call on of your Backgrounds as if you had an extra dot in that Background (up to the normal maximum of 5). You do not have to purchase this Merit to be a member of the Vaishya jati, but only members of the Vaishya jati may have this Merit.",
            "reference": "Lore of the Clans; PG 182",
            "clan": "Ravnos",
        },
        {
            "name": "Critters",
            "rating": [2],
            "description": "You’re excellent with animals — so much so that they constantly seek to befriend you. Wherever you go, the animals are happy to see you, and more often than not, happy to help you when you ask for their aid. You receive a bonus die on Social rolls to affect small animals. Further, animal companions who have had continual interaction with you see you as something of a pet, and occasionally bring you small useful things. Once per game session, animals will bring you a useful piece of information or a small item relevant to events. This item might occasionally play into the individual Ravnos’ particular vice, as the animals quickly pick up on what pleases their friend.",
            "reference": "Lore of the Clans; PG 182",
            "clan": "Ravnos",
        },
        {
            "name": "Heart of Needles",
            "rating": [3],
            "description": "Your natural abilities with illusions have rendered you particularly jaded and unimpressible. How can anything be as perfect as your own imagination? Because of this, your heart is harder than most, and you have a significant resistance to emotion control. All powers and Social challenges that attempt to manipulate you emotionally are made at a +2 difficulty.",
            "reference": "Lore of the Clans; PG 182",
            "clan": "Ravnos",
        },
        {
            "name": "Indelible",
            "rating": [1, 2],
            "description": "Whereas other vampires’ bodies return to the state they were in at the Embrace each evening, any body modifications you get after the Embrace remain as they are until you actively spend a Willpower point to return your body to its tabula rasa state. This Merit applies to changes as simple as dying or cutting your hair to modifications as complicated as tattoos, piercings, or even small implants. If the Merit only allows for cosmetic alterations, it is worth 1 point. If it allows for more utilitarian alterations, such as RFID implants that activate certain electronic devices, then it is worth 2 points.",
            "reference": "Lore of the Clans; PG 200",
            "clan": "Toreador",
        },
        {
            "name": "Impressive Restraint",
            "rating": [2],
            "description": "When you haven’t eaten, it can be torturous to be near mortals. The pounding thrum of blood through their veins does not leave you nearly as tempted as it might other Kindred. When opportunity presents itself, the difficulty of all Self-Control rolls to resist hunger are made against a -2 difficulty. Characters on Paths of Enlightenment that require Instinct cannot take this Merit.",
            "reference": "Lore of the Clans; PG 200",
            "clan": "Toreador",
        },
        {
            "name": "Master of the Masquerade",
            "rating": [2],
            "description": "There are many small tics, nervous habits, and autonomous bodily functions (like breathing) that Kindred simply forget to do. They can be unnervingly still or forget to breathe, particularly when they think they’re alone. You never let down your guard. The act of breathing remains unconscious habit to you, and you never lapse into that eerie statue-like stillness, even when transfixed or concentrating. Consequently, the difficulties of all Social rolls are lowered by one when interacting with mortals. This Merit does not allow you to eat food or benefit from the blush of health (V20, p. 480) — those Merits are still required to be a true master of the Masquerade.",
            "reference": "Lore of the Clans; PG 200",
            "clan": "Toreador",
        },
        {
            "name": "Slowed Degeneration",
            "rating": [5],
            "description": "Your Humanity is strong and can more easily withstand the Beast’s assaults. You gain two additional dice on any Conscience roll. This degree of moral resilience allows a well-behaved vampire to lose Humanity at a much slower rate than would otherwise be possible. Only vampires following Humanity may take this Merit, and the Merit is lost forever in the event that the vampire takes up another Path of Enlightenment.",
            "reference": "Lore of the Clans; PG 200",
            "clan": "Toreador",
        },
        {
            "name": "Embraced without the Cup",
            "rating": [1],
            "description": "For some reason you did not drink the blood of the elders when you were inducted into Clan Tremere. More dangerously, it may have had no effect on you. As a result, you are not bound to the Clan the way most Tremere are. Should it be discovered, it will usually be corrected, but one might almost believe there was some purpose to this lapse, as the Tremere don’t make mistakes. Perhaps the Clan has a special task in mind for you, one where you might be forced to act against the Clan to maintain a cover....",
            "reference": "Lore of the Clans; PG 218",
            "clan": "Tremere",
        },
        {
            "name": "Secret Society Member",
            "rating": [1],
            "description": "You have found and joined one of the many secret societies in Clan Tremere. Your character must be suitable to join, such as having Necromancy to join the Covenant. You might pick one of the societies listed here or create one of your own. In most cases, your society membership should be kept secret, but your allegiance to it is not considered a crime. While your society expects you to uphold its tenets and agenda, they can also be counted upon to back you up and help you increase your power within the pyramid.",
            "reference": "Lore of the Clans; PG 218",
            "clan": "Tremere",
        },
        {
            "name": "Keys to the Library",
            "rating": [1, 2, 3, 4, 5],
            "description": "You have one of the most sought after positions in the chantry: a librarian. It is one of your duties to catalogue and maintain the magical lore kept in your chantry. This means you have complete access to it, and get to decide who can see it and who can’t. A vast array of rituals and Thaumaturgical knowledge resides here, making it simple to learn many of the secrets of magic. No matter how restrictive your chantry, you have complete access to the library for research. The cost of this merit is the same as the chantry’s Library rating (see pp. 221-222).",
            "reference": "Lore of the Clans; PG 218",
            "clan": "Tremere",
        },
        {
            "name": "Outside Haven",
            "rating": [2],
            "description": "You maintain your own private haven outside the chantry and Tremere control. Most Tremere are expected to rest in the chantry, where the Clan can keep an eye on them. However, you have been trusted with a little more privacy. This might be because you have already proved your loyalty, or perhaps because they are testing it.",
            "reference": "Lore of the Clans; PG 218",
            "clan": "Tremere",
        },
        {
            "name": "Unmarked Antitribu",
            "rating": [2, 5],
            "description": "While you are part of the Sabbat and a traitor to House and Clan Tremere, somehow you remain unmarked by the antitribu curse. You are not easily recognized as a renegade Tremere, and the magic that burned so many of your brethren cannot target you. Further, other Sabbat members cannot judge you at a glance. Those of the Telyavelic bloodline can purchase this Merit at 2 points, while other Tremere pay 5 points.",
            "reference": "Lore of the Clans; PG 218",
            "clan": "Tremere",
        },
        {
            "name": "Quartermaster",
            "rating": [3],
            "description": "You are one of the Kindred responsible for maintaining and organizing the chantry’s mundane supplies. You may take anything from the chantry’s stores as defined by the chantry’s Stores rating. While you will have to return or replace anything you borrow, you have access the whole range of equipment appropriate to the size of the chantry. This might range from assault weapons and explosives to advanced medical and scientific equipment.",
            "reference": "Lore of the Clans; PG 218",
            "clan": "Tremere",
        },
        {
            "name": "Bioluminescence",
            "rating": [1],
            "description": "Perhaps through biological expertise, or perhaps by unlocking something primordial within, you have accessed the secrets of bioluminescence. Using the Vicissitude, you may grant yourself (through Malleable Visage) or others (via Fleshcraft — both as per V20, p. 241) the ability to emit a soft glow. With muscle control and practice, you can control the color and pattern of the illumination. This can light a soft glow in the dark, create beautiful displays, or even act as a primal form of communication. Some Fiends grant their ghouls or childer bioluminescence, developing an eerily nuanced and wordless language with their thralls and broods. Only characters with at least one dot of Vicissitude may purchase this Merit.",
            "reference": "Lore of the Clans; PG 238",
            "clan": "Tzmimisce",
        },
        {
            "name": "Pain Tolerance",
            "rating": [2],
            "description": "Maybe you are a badass or shut off your nerves through Vicissitude. Maybe your sire put you through so many intricate hells that it would be tough for anyone else to compete. Maybe it just turns you on. Regardless, at Hurt or Injured, you suffer no wound penalties, though you still suffer full penalties at Wounded and below. You must have a Conviction or Courage rating of 3 or more to take this Merit.",
            "reference": "Lore of the Clans; PG 238",
            "clan": "Tzmimisce",
        },
        {
            "name": "Dracon's Temperament",
            "rating": [3],
            "description": "You emulate the ideal of Azi Dahaka within and without, to levels visceral and abstract. Your psyche flows with the permutable nature of change. Like the protean Dracon, you are a whirlwind of temperaments. This is not multiple personalities. You are one identity shown through the prism of ever-shifting Natures. No anchor fetters your sense of self. You can be any you. At the start of each story, you may choose one Personality Archetype to function as your Nature, spending the rest of the story perceiving the world through that perspective. You also regain Willpower according to your new Nature and may be affected by other effects or Discipline powers as per your new Nature as well.",
            "reference": "Lore of the Clans; PG 238",
            "clan": "Tzmimisce",
        },
        {
            "name": "Haven Affinity",
            "rating": [3],
            "description": "You are the land. The land is you. The home soil calls to you. You give to it, and it gives to you. Your connection to the earth of your prime haven grants you an extra die to all dice pools when operating there. It also acts as a mystic beacon, allowing you to home in on its location with a standard Perception + Survival roll (difficulty 6), +1 difficulty when a state or country separates you; +2 if you’re halfway across the globe. This applies only to your primary haven.",
            "reference": "Lore of the Clans; PG 238",
            "clan": "Tzmimisce",
        },
        {
            "name": "Revenant Disciplines",
            "rating": [3],
            "description": "The blood of your revenant family runs deep, deeper than the Embrace. The Disciplines that were innate to you as a ghoul have remained so as a Cainite. At character creation, select the ghoul family from which you hail (V20, pp. 503-506). Instead of the Tzimisce’s standard complement of Animalism, Auspex, and Vicissitude, you draw from your three family Disciplines for your starting allocation (though you may buy other Disciplines with freebies, as normal). You trade in the entire set of Tzimisce Clan Disciplines for the set of revenant family Disciplines, for the purposes of in-Clan Experience cost.",
            "reference": "Lore of the Clans; PG 238",
            "clan": "Tzmimisce",
        },
        {
            "name": "Promethean Clay",
            "rating": [5],
            "description": "Your flesh ripples and molds itself to your preternatural will, almost before you consciously invoke the change. The difficulty to use any Vicissitude power on yourself is two less than normal, and you may activate Vicissitude powers reflexively at your full dice pool while taking other actions. Powers that require multiple turns to activate still require the usual duration. The change simply occurs without conscious direction. As a final benefit, you need no physical sculpting to use the first three levels of Vicissitude on yourself, as your flesh undulates and extrudes to its desired shape. Only characters with at least one dot of Vicissitude may purchase this Merit.",
            "reference": "Lore of the Clans; PG 238",
            "clan": "Tzmimisce",
        },
        {
            "name": "Connoisseur",
            "rating": [2],
            "description": "Your study of the Auspex Discipline, combined with your rarified tastes, allows you powerful insights into the character of any whose blood you taste. The character tastes another’s blood (potentially risking blood bond), and player rolls Perception + Empathy (difficulty 6 for mortals or 8 for Kindred). If the blood came from a mortal, each success allows him to learn one of the following: the mortal’s Nature, her Demeanor, any Derangements she may possess, whether she is blood bonded, and whether she carries any blood-borne diseases. If the vitae came from a vampire, he can learn all of the previous information, plus anything discoverable with the first level of the Path of Blood (see V20, p. 213). The Ventrue may taste the blood of a mortal who does not fit within his feeding restriction long enough to use this ability, but he must immediately spit it out afterwards. Vampires that do not have Auspex•• cannot take this Merit.",
            "reference": "Lore of the Clans; PG 261",
            "clan": "Ventrue",
        },
        {
            "name": "Blessed by St. Gustav",
            "rating": [4],
            "description": "Many Ventrue antitribu replace their traditional affinity for Presence with an aptitude for Auspex by means of the ignobilis ritus known as the Prayer to St. Gustav (see sidebar). For your piety and devotion to the Sabbat cause, you have been especially blessed and have an affinity for both Disciplines. Prayer to St. Gustav: To the Ventrue antitribu, the Presence discipline (while useful) is often viewed as decadent and unworthy of the martial heritage they imagine for themselves. In contrast, the Auspex discipline is prized for its power to grant insights and to see through deceptions. This ignobilis ritus allows a Ventrue antitribu to replace Presence with Auspex as a Clan Discipline. The ritus requires a group consisting solely of Ventrue antitribu to participate in a Vaulderie while wearing ceremonial armor and singing the praises of St. Gustav Mallenhaus, the founder of the Sabbat Inquisition. The player of any crusader present who has not yet acquired any dots in Presence may roll Intelligence + Occult (difficulty 7), and if the roll succeeds, she may replace Presence with Auspex as a Clan Discipline. With five or more successes, the Storyteller may decide to award the Blessed by St. Gustav Merit. A character who has already started learning Presence may attempt this ritus, but may not swap out his Presence for Auspex — instead his Presence immediately becomes out-of-Clan, and the player must pay the difference in experience points between what the Presence cost before and what it costs now. This Merit is identical to Additional Discipline Merit found on V20, p. 494, except that it can only be used to add Auspex as a fourth in-Clan discipline. Only Ventrue antitribu can take this Merit.",
            "reference": "Lore of the Clans; PG 261",
            "clan": "Ventrue",
        },
        {
            "name": "Personal Masquerade",
            "rating": [3],
            "description": "Thorough charm, manipulation, or just plain luck, you have managed to convince other vampires that you are a member of one of the Clans. Any social interactions with vampires ignorant of your true nature ignore your usual penalty for being Caitiff. However, you must constantly be vigilant of your ruse. Should anyone come to realize you have been playing them for fools, their vengeance will be swift. The higher you climb in Kindred politics, the more likely this becomes. The Clan Weakness Flaw can actually prove to be a boon in supporting your Masquerade. Others, however, must be that much more careful.",
            "reference": "Lore of the Clans; PG 269",
            "clan": "Caitiff",
        },
        {
            "name": "The High Price",
            "rating": [3],
            "description": "The burden of acquiring truth or power always comes at a high price. None know that more than these Baali, who sacrifice a part of their own soul in aspiration of greatness. Their physical body is wracked with weakness and pain, capping any Physical Attributes at four dots and costing 1 Willpower point every evening when they rise. In exchange for this tribute, the Baali receive +2 dice to any Discipline-related checks.",
            "reference": "Lore of the Bloodlines; PG 16",
            "clan": "Baali",
        },
        {
            "name": "Simply Waiting",
            "rating": [4],
            "description": "The Baali knows their place within the order of the universe, and where they stand against other vampires or those of their own bloodline. They also know the end of the world is coming, sooner rather than later. They appear apathetic to the world around them, but in truth, they are simply resigned to their fate and remain unmoved if others try to get them to stray from their path. All Social rolls against them are increased by +2 difficulty, as the Baali knows the true end of it all.",
            "reference": "Lore of the Bloodlines; PG 16",
            "clan": "Baali",
        },
        {
            "name": "Chorus Trained",
            "rating": [3, 5],
            "description": "The character has learned how to use the Fugue to tune in to her sisters and work together with far more efficiency. For 3 points, this Merit grants the character 2 extra dice to any Melpominee dice pool when using the power with another character with this Merit. For 5 points, the bonus 2 dice can be added for any action being performed by a partner with this Merit, such as making art or even fighting together.",
            "reference": "Lore of the Bloodlines; PG 26",
            "clan": "Daughters of Cacophony",
        },
        {
            "name": "Fugue Instinct",
            "rating": [3],
            "description": "You can hear warnings and gain insight by listening to the Fugue more deeply. You must forego one of your actions to listen properly to the Fugue within. During this time, you may defend yourself but take no active actions. If you do, then you gain an insight for your next action that grants you +2 dice to whatever dice pool you use.",
            "reference": "Lore of the Bloodlines; PG 26",
            "clan": "Daughters of Cacophony",
        },
        {
            "name": "Stillness of Death",
            "rating": [2],
            "description": "Gargoyles often hide themselves as statuary. The difficulty for any searches to find you are increased by 2 when you stay perfectly still.",
            "reference": "Lore of the Bloodlines; PG 37",
            "clan": "Gargoyels",
        },
        {
            "name": "Heavy Hands",
            "rating": [3],
            "description": "One of the effects of becoming a vampire is strange changes happening to your body. The obvious alterations to your hands have made them tougher, harder, and more impervious to pain. All difficulties for damage rolls using unarmed attacks go down by 1.",
            "reference": "Lore of the Bloodlines; PG 37",
            "clan": "Gargoyels",
        },
        {
            "name": "Disciple of Lazarus / Japheth",
            "rating": [2],
            "description": "You speak for the powers-that-be within your bloodline, and bear the clean, white death mask of a respected Harbinger lost to one of the historic purges suffered by your people. Most Harbingers of Skulls will listen to what you say, and take your words at face value. This Merit adds two dice to any Social roll when you invoke the name of Lazarus or Japheth.",
            "reference": "Lore of the Bloodlines; PG 48",
            "clan": "Harbinger of Skulls",
        },
        {
            "name": "Styx Baptism",
            "rating": [3],
            "description": "You pledged fealty to the Harbingers of Skulls and swore to work against the machinations of Ashur, despite not being Embraced into the bloodline. You were escorted to the Shadowlands, where you were baptized head-first in the churning waters of the Styx. The flesh upon your head sloughed off with contact over the coming month, leaving just rotten patches or bare bone, reducing your Appearance Rating to 0 permanently. You’re now held in esteem by Lazarenes, gaining any one of the bloodline’s Disciplines as a Clan Discipline in place of one of your own.",
            "reference": "Lore of the Bloodlines; PG 48",
            "clan": "Harbinger of Skulls",
        },
        {
            "name": "Half-Life",
            "rating": [6],
            "description": "You’re more than just a vampire; you’re a wraith in vampire form. Your awareness of the realities of death enables you to spend half the regular experience points cost for increasing Necromancy Paths after the first point, and permits you to move between Shadowlands and Skinlands through the expenditure of a Willpower point. You cannot be controlled as a normal spirit through use of Necromancy, but should other vampires discover what you are, you can expect to be hunted mercilessly. You suffer the same weaknesses and have the same strengths as a vampire, but if viewed with a power such as Aura Perception (V20, p. 135) the aura appears as a double-exposure, with a wavering, translucent humanoid shape merging in and out of yours.",
            "reference": "Lore of the Bloodlines; PG 48",
            "clan": "Harbinger of Skulls",
        },
        {
            "name": "Prized Collection",
            "rating": [1, 2],
            "description": "Kiasyd have appreciation for compilations of books, records, vintages of blood, and other collectable items among Cainites. You possess a collection that may not be worth much (1pt.) or could be worth a lot to the right buyer (2pt.). Importantly, it’s a point of interest for any visiting Kiasyd or expert in the field, and they’re likely to treat you well just to get access to it.",
            "reference": "Lore of the Bloodlines; PG 59",
            "clan": "Kyasid",
        },
        {
            "name": "Alien Perfection",
            "rating": [2],
            "description": "You possess beauty unsettling in its perfection. People stand in awe of your flawless form, while inexplicable nausea subconsciously creeps up. The difficulty of any Appearance roll is reduced by three. A Stamina roll is required by anyone in your presence for longer than one scene, if this is the first time they’ve encountered you. Failure drives them away from you with a sickness wracking their body.",
            "reference": "Lore of the Bloodlines; PG 59",
            "clan": "Kyasid",
        },
        {
            "name": "Paranormal Link",
            "rating": [2],
            "description": "You’re linked to another weird species of the world, and unconsciously find yourself able to understand their parlance, codes, and rituals. Difficulties to decipher the hidden rites and languages of one society (selected when this Merit is purchased) are reduced by three.",
            "reference": "Lore of the Bloodlines; PG 60",
            "clan": "Kyasid",
        },
        {
            "name": "Skin of Porcelain",
            "rating": [4],
            "description": "Through concoctions imbibed or by a fluke of your Embrace, you possess a ceramic-like coating to your skin. In order for this to have any effect beyond looking strange, a Stamina roll is required (difficulty 8). Success allows you to convert up to three points of aggravated damage from a fire source to lethal damage before attempts to soak. The hardening dissipates for the remainder of the current story.",
            "reference": "Lore of the Bloodlines; PG 60",
            "clan": "Kyasid",
        },
        {
            "name": "Vitae Mutation",
            "rating": [5],
            "description": "You’ve drank the liquid essence of entities both strange and powerful. Whether the vitae of Methuselahs, the boiling blood of lupines, or bottled dreams of fae, the volume and combination of the brews you’ve consumed have forever altered you. Each night a Willpower roll is required (difficulty 7) for you to manifest a single point of Auspex, Chimerstry, or Dementation. This point can be added to an existing rating in the Discipline, but disappears the following night.",
            "reference": "Lore of the Bloodlines; PG 60",
            "clan": "Kyasid",
        },
        {
            "name": "Extra Sharp",
            "rating": [2],
            "description": "All Nagaraja already have sharpened fangs for the purposes of cutting into flesh with ease. A character with this Merit, however, has additional rows of fangs, similar to a shark, each one poised to inflict the most pain possible. Instead of dealing 1 unsoakable lethal damage per bite, they deal 2 lethal instead. Some Nagaraja like this gift since it makes their victims stop squirming much quicker. Others fear it creates a connection to the painful bite of the Giovanni, and may see Nagaraja with this Merit almost as outsiders.",
            "reference": "Lore of the Bloodlines; PG 70",
            "clan": "Nagaraja",
        },
        {
            "name": "Speed Eater",
            "rating": [2, 4],
            "description": "The vampire’s jaws have been strengthened to allow for faster devouring of one’s prey. For 2 points, he can devour 2 blood points worth of flesh per minute, or he may devour 3 blood points worth for 4 points. Must have at least Stamina 3 in order to gain this Merit. Otherwise, his undead form cannot support the influx of blood and viscera at such a fast pace.",
            "reference": "Lore of the Bloodlines; PG 70",
            "clan": "Nagaraja",
        },
        {
            "name": "Wolverine's Palate",
            "rating": [3],
            "description": "Though many do not know this, the dreaded wolverine is one of only a few creatures in the world that can eat their prey entirely, whether larger or smaller. The Nagaraja with this Merit has the ability to eat bone just as easily as flesh, sapping even more spiritual essence from her victim and converting it to blood points. With one bite, she can cut through flesh and bone and swallow it all at once with no ill effect. This also means she may gain up to 5 additional blood points from a body by consuming the bones.",
            "reference": "Lore of the Bloodlines; PG 70",
            "clan": "Nagaraja",
        },
        {
            "name": "Scent of the Other",
            "rating": [1],
            "description": "“You don’t seem like a soul-sucker…” For whatever reason, your third eye shuts tightly when you choose to hide it, and your blood and aura don’t give away your Clan. You might be regarded as a Caitiff, or as a member of another Clan. In any case, Tremere or other Salubri hunters are thrown off your trail, unless you do something to reveal yourself again.",
            "reference": "Lore of the Bloodlines; PG 80",
            "clan": "Salubri",
        },
        {
            "name": "Sight Beyond Sight",
            "rating": [3],
            "description": "Your third eye occasionally experiences visions and pierces illusions. When your eye is open (via use of Auspex or Obeah), you occasionally pierce Obfuscate or Chimerstry. Some past Salubri have seen through faerie miens or glimpsed the dead lands of ghosts. You have no control over what your eye sees, though it’ll sometimes open involuntarily in response to the above phenomena.",
            "reference": "Lore of the Bloodlines; PG 80",
            "clan": "Salubri",
        },
        {
            "name": "Warrior's Heart",
            "rating": [3],
            "description": "Steel sits in the placid heart of the Salubri bloodline, and Adonai’s resurrection has caused your own heart to flutter ever so slightly. Like the Healers of old, you may learn the Valeren powers of the antitribu at a cost of current rating x6; if you know the first two dots of Obeah and Valeren, you gain a 2-die bonus to using the first two Discipline dots. However, your warrior’s heart suffers from the Precept of Samiel, the well-defined wanderlust that affects many Salubri — for every week you spend in the same location, you lose a point of Willpower, as your soul agitates without action. The antitribu might have a similar Merit allowing them to learn Obeah at a cost of always helping someone in need, at the Storyteller’s discretion.",
            "reference": "Lore of the Bloodlines; PG 80",
            "clan": "Salubri",
        },
        {
            "name": "Death Grip",
            "rating": [3],
            "description": "Thanks to your connection with death, you have a keen insight few other Kindred possess. When in contact with a dead body, you make a Wits + Alertness roll (difficulty 7). On a success, you intuitively know how the body died. On a failure, you suffer an illusory version of the wound that saps a point of Willpower. On a botch, your body mirrors the wound and hurts itself in the same manner, causing lethal damage equal to the final blow.",
            "reference": "Lore of the Bloodlines; PG 91",
            "clan": "Samedi",
        },
        {
            "name": "Stitcher",
            "rating": [3],
            "description": "Getting blown apart isn’t a big deal. When parts of your body are cut off or otherwise removed due to damage, you may make a Dexterity + Medicine (difficulty 7) to sew the part back in place properly. If successful, the cost of healing the wound is reduced by one blood point.",
            "reference": "Lore of the Bloodlines; PG 91",
            "clan": "Samedi",
        },
        {
            "name": "Advanced Tech",
            "rating": [1, 5],
            "description": "You have a device (or possibly a few) of an advanced design. While the True Brujah are not especially good at innovation, they are good at making improvements. So this device has no special functions unavailable to its contemporaries, but it does work a lot better. It reduces the chance of a mechanical fault (such as a jam) by half and all uses of the device are made with a -1 to the difficulty. The Storyteller should decide on the cost of the Merit, depending on how many items the character has, and how powerful they are.",
            "reference": "Lore of the Bloodlines; PG 99",
            "clan": "True Brujah",
        },
        {
            "name": "Fatalist",
            "rating": [3],
            "description": "The character’s study of time has led them to believe that what is done is simply done. Destiny is a fixed path and therefore we are all the slaves of our own futures. As such, nothing can truly be our fault, for nothing is entirely under our control. It therefore becomes a lot easier to excuse themselves from their worst excesses. The character subtracts 2 from the difficulty of all degeneration rolls against losses of Humanity or Path of Enlightenment.",
            "reference": "Lore of the Bloodlines; PG 99",
            "clan": "True Brujah",
        },
        {
            "name": "True Celerity",
            "rating": [5],
            "description": "The True Brujah have an odd relationship with Celerity. It often comes easily to them, but a few refuse to learn it, as it has become a symbol of the traitor Brujah. However, many find it a useful skill for masquerading as Brujah within the Camarilla or Sabbat, and so a few True Brujah have developed a slightly different form of the Discipline. A character with this Merit has the ability to learn True Celerity. While it works exactly the same as Celerity, it feels very different. Instead of the character moving quickly, they slow time down all around them. This Merit confers no Discipline points for the character, but does allow it to be bought with experience as if Celerity was a Clan discipline. While this power functions the same as Celerity, it cannot be taught to anyone who does not have any levels of the Temporis Discipline.",
            "reference": "Lore of the Bloodlines; PG 99",
            "clan": "True Brujah",
        },
        {
            "name": "Peacemaker",
            "rating": [2],
            "description": "You have a reputation for having a good head on your shoulders and the honor to keep your word no matter what. As a result, your allies and sectmates ask you to mediate their disputes, even with other sects. This Merit allows your character to use her reputation as leverage to keep the peace during tense situations. Reduce the difficulty of all social rolls to keep the peace or to mediate honestly between factions (even other sects) by 2.",
            "reference": "Anarchs Unbound; PG 102",
            "clan": None,
        },
        {
            "name": "Prized Patch",
            "rating": [2],
            "description": "You belong to an Anarch gang with a violent, effective, or otherwise impressive reputation. The history of the gang might extend a hundred years before you were born, but so long as you hold membership and wear the colors of your crew, other Anarchs naturally tend to respect you. Some may even occasionally perform minor tasks for you to try to curry favor with the others. When your membership is known, reduce the difficulty of all Manipulation rolls with other Anarchs by 2 unless a given Anarch has a historical animosity with your gang.",
            "reference": "Anarchs Unbound; PG 102",
            "clan": None,
        },
        {
            "name": "Soapbox",
            "rating": [3],
            "description": "You have some sort of special forum (a zine, a secure blog, a well-known podcast, or a social media account with a lot of followers) that allows your Anarch to express an opinion and have said opinion spread widely. The Soapbox Merit represents a social delivery mechanism that can influence Kindred outside of your character’s normal social circle or class. Reduce the difficulty of Expression and Subterfuge rolls by 2 difficulty when dealing with vampires who read the Soapbox.",
            "reference": "Anarchs Unbound; PG 102",
            "clan": None,
        },
        {
            "name": "Sugar Daddy",
            "rating": [3],
            "description": "You have a personal relationship with a high-ranking member of a different sect. You may invoke your Sugar Daddy’s name to lower the difficulty of Manipulation rolls by 2 against members of that sect when attempting to smooth out problems or acquire minor favors. Of course, the Sugar Daddy may expect similar treatment in kind, and is unlikely to look favorably on any behavior that impugns whatever status he may have.",
            "reference": "Anarchs Unbound; PG 102",
            "clan": None,
        },
        {
            "name": "Berserker",
            "rating": [3],
            "description": "You possess the ability to willingly enter a berserker state for a scene. While berserking, you ignore wound penalties and reduce the difficulty of all combat rolls except for dodges by -3. You also can take no complex actions other than combat, dodging, or running.",
            "reference": "The Black Hand: A Guide to The Tal'Mahe'Ra; PG 177",
            "clan": None,
        },
    ]

    for m in merit_data:
        existing = V20_Advantage.query.filter_by(name=m["name"]).first()
        if existing:
            continue

        merit = V20_Advantage(
            name=m.get("name"),
            rating=m.get("rating"),
            description=m.get("description"),
            reference=m.get("reference"),
            clan=m.get("clan"),
            category="Merit",
        )

        db.session.add(merit)


def seed_v20_flaws():
    flaw_data = []
    pass


def seed_v20():
    seed_v20_disciplines()
    seed_v20_clan()
    seed_v20_sorcery()
    seed_v20_nature()
    seed_v20_backgrounds()
    seed_v20_merits()
    db.session.commit()
