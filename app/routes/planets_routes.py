from flask import Blueprint, abort, make_response
from app.models.planet import planets

planets_bp = Blueprint("planets_bp", __name__, url_prefix="/planets")

@planets_bp.get("")
def get_planets():
    response_planets = []
    for planet in planets:
        response_planets.append(dict(
            id=planet.id,
            name=planet.name,
            description=planet.description,
            distance_from_sun_mm_km=planet.distance_from_sun_mm_km
        ))
    return response_planets

@planets_bp.get("/<id>")
def get_one_planet(id):
    planet = validate_planet_id(id)
    return dict(
        id=planet.id,
        name=planet.name,
        description=planet.description,
        distance_from_sun_mm_km=planet.distance_from_sun_mm_km
    )

def validate_planet_id(id):
    try:
        id = int(id)
    except:
        response = {"message": f"This ID {id} is invalid"}
        abort(make_response(response, 400))

    for planet in planets:
        if planet.id == id:
            return planet
    
    response = {"message": f"Planet with ID {id} is not found"}
    abort(make_response(response, 404))
