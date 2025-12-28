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
    nature_data = [
        {
            "name": "Architect",
            "description": "You need to build something of lasting value",
        },
        {
            "name": "Autocrat",
            "description": "You need control",
        },
        {
            "name": "Bon Vivant",
            "description": "Your unlife is for pleasure",
        },{
            "name": "Bravo",
            "description": "Might makes right",
        },

    ]


def seed_v20():
    seed_v20_clan()
    seed_v20_nature()
    db.session.commit()