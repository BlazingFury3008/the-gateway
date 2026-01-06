from flask import Blueprint, jsonify
from models import (
    V20_Nature,
    V20_Clans,
    V20_Backgrounds,
    V20_Disciplines,
    V20_Sorcery_Paths,
    V20_Magic_Types,
    V20_Advantage,
)
from sqlalchemy.orm import selectinload

v20_bp = Blueprint("V20", __name__, url_prefix="/v20")


# ---------------------------------------------------------
# Clans
# ---------------------------------------------------------
@v20_bp.route("/clan", methods=["GET"])
def get_clans():
    """
    Get all V20 clans (with discipline objects)
    ---
    tags:
      - v20
    security:
      - ApiKeyAuth: []
    responses:
      200:
        description: List of clans
        schema:
          type: array
          items:
            $ref: '#/definitions/V20_Clan'
    """
    clans = (
        V20_Clans.query.options(
            selectinload(V20_Clans.discipline1),
            selectinload(V20_Clans.discipline2),
            selectinload(V20_Clans.discipline3),
            selectinload(V20_Clans.discipline4),
        ).all()
    )

    payload = []
    for c in clans:
        payload.append(
            {
                "id": c.id,
                "name": c.name,
                "weakness": c.weakness,
                "information": c.information,
                "reference": c.reference,
                "discipline_1": c.discipline1.to_dict() if c.discipline1 else None,
                "discipline_2": c.discipline2.to_dict() if c.discipline2 else None,
                "discipline_3": c.discipline3.to_dict() if c.discipline3 else None,
                "discipline_4": c.discipline4.to_dict() if c.discipline4 else None,
            }
        )

    return jsonify(payload)


# ---------------------------------------------------------
# Disciplines
# ---------------------------------------------------------
@v20_bp.route("/discipline", methods=["GET"])
def get_disciplines():
    """
    Get all V20 disciplines
    ---
    tags:
      - v20
    security:
      - ApiKeyAuth: []
    responses:
      200:
        description: List of disciplines
        schema:
          type: array
          items:
            $ref: '#/definitions/V20_Discipline'
    """
    t = V20_Disciplines.query.all()
    payload = [x.to_dict() for x in t]
    return jsonify(payload)


# ---------------------------------------------------------
# Merits
# ---------------------------------------------------------
@v20_bp.route("/merit", methods=["GET"])
def get_merits():
    """
    Get all V20 merits
    ---
    tags:
      - v20
    security:
      - ApiKeyAuth: []
    responses:
      200:
        description: List of merits
        schema:
          type: array
          items:
            $ref: '#/definitions/V20_Advantage'
    """
    t = V20_Advantage.query.filter_by(category="Merit").all()
    payload = [x.to_dict() for x in t]
    return jsonify(payload)


# ---------------------------------------------------------
# Flaws
# ---------------------------------------------------------
@v20_bp.route("/flaw", methods=["GET"])
def get_flaws():
    """
    Get all V20 flaws
    ---
    tags:
      - v20
    security:
      - ApiKeyAuth: []
    responses:
      200:
        description: List of flaws
        schema:
          type: array
          items:
            $ref: '#/definitions/V20_Advantage'
    """
    t = V20_Advantage.query.filter_by(category="Flaw").all()
    payload = [x.to_dict() for x in t]
    return jsonify(payload)


# ---------------------------------------------------------
# Advantages (all)
# ---------------------------------------------------------
@v20_bp.route("/advantage", methods=["GET"])
def get_adv():
    """
    Get all V20 advantages
    ---
    tags:
      - v20
    security:
      - ApiKeyAuth: []
    responses:
      200:
        description: List of advantages
        schema:
          type: array
          items:
            $ref: '#/definitions/V20_Advantage'
    """
    t = V20_Advantage.query.all()
    payload = [x.to_dict() for x in t]
    return jsonify(payload)


# ---------------------------------------------------------
# Backgrounds
# ---------------------------------------------------------
@v20_bp.route("/backgrounds", methods=["GET"])
def get_backgrounds():
    """
    Get all V20 backgrounds
    ---
    tags:
      - v20
    security:
      - ApiKeyAuth: []
    responses:
      200:
        description: List of backgrounds
        schema:
          type: array
          items:
            $ref: '#/definitions/V20_Background'
    """
    data = V20_Backgrounds.query.all()
    payload = [n.to_dict() for n in data]
    return jsonify(payload)


# ---------------------------------------------------------
# Archetypes (Nature / Demeanor)
# ---------------------------------------------------------
@v20_bp.route("/nature", methods=["GET"])
def get_archetypes():
    """
    Get all V20 natures
    ---
    tags:
      - v20
    security:
      - ApiKeyAuth: []
    responses:
      200:
        description: List of natures
        schema:
          type: array
          items:
            $ref: '#/definitions/V20_Nature'
    """
    data = V20_Nature.query.all()
    payload = [n.to_dict() for n in data]
    return jsonify(payload)


# ---------------------------------------------------------
# Sorcery
# ---------------------------------------------------------
@v20_bp.route("/sorcery", methods=["GET"])
def get_sorcery():
    """
    Get all V20 magic paths
    ---
    tags:
      - v20
    security:
      - ApiKeyAuth: []
    responses:
      200:
        description: List of sorcery paths
        schema:
          type: array
          items:
            $ref: '#/definitions/V20_Sorcery_Path'
    """
    data = V20_Sorcery_Paths.query.all()
    payload = [n.to_dict() for n in data]
    return jsonify(payload)


# ---------------------------------------------------------
# Magic Types
# ---------------------------------------------------------
@v20_bp.route("/m_type", methods=["GET"])
def get_magic_type():
    """
    Get all V20 magic types
    ---
    tags:
      - v20
    security:
      - ApiKeyAuth: []
    responses:
      200:
        description: List of magic types/disciplines
        schema:
          type: array
          items:
            type: object
            properties:
              id:
                type: integer
              name:
                type: string
    """
    data = V20_Magic_Types.query.all()
    payload = [n.to_dict() for n in data]
    return jsonify(payload)
