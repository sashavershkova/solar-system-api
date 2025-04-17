from flask import Blueprint
from app.models.planets import planets

planets_bp = Blueprint("planets_bp", __name__, url_prefix="/planets")

@planets_bp.get("")
def get_planets():
    response_planets = []
    for planet in planets:
        response_planets.append(dict(
            id = planet.id,
            name = planet.name,
            description = planet.description,
            distance_from_sun = planet.distance_from_sun
        ))
    return response_planets