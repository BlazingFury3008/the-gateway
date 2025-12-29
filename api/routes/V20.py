from flask import Blueprint, jsonify
from models import V20_Nature

v20_bp = Blueprint("V20", __name__, url_prefix="/v20")


# ---------------------------------------------------------
# Clans
# ---------------------------------------------------------
@v20_bp.route("/clans", methods=["GET"])
def get_clans():
    return jsonify([
        {"id": 1, "name": "Brujah", "bane": "Rageful", "disciplines": ["Celerity", "Potence", "Presence"]},
        {"id": 2, "name": "Toreador", "bane": "Obsession", "disciplines": ["Auspex", "Celerity", "Presence"]},
        {"id": 3, "name": "Tremere", "bane": "Blood Bond to Clan", "disciplines": ["Auspex", "Dominate", "Thaumaturgy"]},
    ])


# ---------------------------------------------------------
# Disciplines
# ---------------------------------------------------------
@v20_bp.route("/disciplines", methods=["GET"])
def get_disciplines():
    return jsonify([
        {"id": 1, "name": "Auspex", "description": "Supernatural senses"},
        {"id": 2, "name": "Celerity", "description": "Supernatural speed"},
        {"id": 3, "name": "Potence", "description": "Supernatural strength"},
        {"id": 4, "name": "Presence", "description": "Supernatural charisma"},
    ])


# ---------------------------------------------------------
# Merits
# ---------------------------------------------------------
@v20_bp.route("/merits", methods=["GET"])
def get_merits():
    return jsonify([
        {"id": 1, "name": "True Love", "cost": 1, "type": "Supernatural"},
        {"id": 2, "name": "Acute Sense", "cost": 2, "type": "Physical"},
        {"id": 3, "name": "Iron Will", "cost": 3, "type": "Mental"},
    ])


# ---------------------------------------------------------
# Flaws
# ---------------------------------------------------------
@v20_bp.route("/flaws", methods=["GET"])
def get_flaws():
    return jsonify([
        {"id": 1, "name": "Nightmares", "severity": 1, "type": "Mental"},
        {"id": 2, "name": "Short Fuse", "severity": 2, "type": "Personality"},
        {"id": 3, "name": "Prey Exclusion", "severity": 1, "type": "Behavioral"},
    ])


# ---------------------------------------------------------
# Backgrounds
# ---------------------------------------------------------
@v20_bp.route("/backgrounds", methods=["GET"])
def get_backgrounds():
    return jsonify([
        {"id": 1, "name": "Allies", "description": "Mortal helpers"},
        {"id": 2, "name": "Contacts", "description": "Information network"},
        {"id": 3, "name": "Resources", "description": "Wealth"},
    ])


# ---------------------------------------------------------
# Archetypes (Nature / Demeanor)
# ---------------------------------------------------------
@v20_bp.route("/nature", methods=["GET"])
def get_archetypes():
    data = V20_Nature.query.all()
    payload = [n.to_dict() for n in data]
    return jsonify(payload)