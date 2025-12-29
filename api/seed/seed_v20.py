from app import db
from models import V20_Clans, V20_Backgrounds, V20_Nature

def seed_v20_clan():
    clans_data = [
        {
            "name": "Brujah",
            "weakness": "The Brujah are unable to spend willpower points to temporarily gain control during a frenzy",
            "information": "Rebels and punks, passionate and quick to anger"
        }
    ]

    for c in clans_data:
        existing = V20_Clans.query.filter_by(name=c["name"]).first()
        if existing:
            continue

        clan = V20_Clans(
            name=c["name"],
            weakness=c["weakness"],
            information=c["information"],
        )
        db.session.add(clan)

def seed_v20_nature():
    natures_data = [
        {"name": "Architect", "description": "You build something of lasting value."},
        {"name": "Autocrat", "description": "You need control."},
        {"name": "Bon Vivant", "description": "Unlife is for pleasure."},
        {"name": "Bravo", "description": "Might makes right."},
        {"name": "Capitalist", "description": "Why give it away for free when you can sell it?"},
        {"name": "Caregiver", "description": "Everyone needs nurturing."},
        {"name": "Celebrant", "description": "Your cause brings you joy."},
        {"name": "Chameleon", "description": "You manage to blend into any situation."},
        {"name": "Child", "description": "Won’t somebody be there for you?"},
        {"name": "Competitor", "description": "You must be the best."},
        {"name": "Conformist", "description": "You follow and assist."},
        {"name": "Conniver", "description": "Others exist for your benefit."},
        {"name": "Creep Show", "description": "Disgusting the straights makes you smile."},
        {"name": "Curmudgeon", "description": "Everything has its flaws."},
        {"name": "Dabbler", "description": "It's always about the next big thing."},
        {"name": "Deviant", "description": "The status quo is for sheep."},
        {"name": "Director", "description": "You oversee what must be done."},
        {"name": "Enigma", "description": "Just when people think they've figured you out, you change the game."},
        {"name": "Eye of the Storm", "description": "Chaos and havoc follow you, but it never gets to you."},
        {"name": "Fanatic", "description": "The cause is all that matters."},
        {"name": "Gallant", "description": "You're not the showstopper: you're the show!"},
        {"name": "Guru", "description": "People find you spiritually compelling."},
        {"name": "Idealist", "description": "You believe in something greater."},
        {"name": "Judge", "description": "Your judgment will improve things."},
        {"name": "Loner", "description": "You make your own way."},
        {"name": "Martyr", "description": "You suffer for the greater good."},
        {"name": "Masochist", "description": "Pain reminds you that you still exist."},
        {"name": "Monster", "description": "You're Damned, so act like it!"},
        {"name": "Pedagogue", "description": "You save others through knowledge."},
        {"name": "Penitent", "description": "Unlife is a curse, and you must atone for it."},
        {"name": "Perfectionist", "description": "You strive for an unattainable goal."},
        {"name": "Rebel", "description": "You follow no one's rules."},
        {"name": "Rogue", "description": "It's all about you."},
        {"name": "Sadist", "description": "You live to cause pain."},
        {"name": "Scientist", "description": "Everything is a puzzle to solve."},
        {"name": "Sociopath", "description": "The inferior must be destroyed."},
        {"name": "Soldier", "description": "You follow orders, but in your own way."},
        {"name": "Survivor", "description": "Nothing can keep you down."},
        {"name": "Thrill-Seeker", "description": "The rush is all that matters."},
        {"name": "Traditionalist", "description": "As it has always been, so it must be."},
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


def seed_v20():
    seed_v20_clan()
    seed_v20_nature()
    db.session.commit()