from flask import Blueprint, abort, make_response, request, Response
from app.models.planet import Planet
from app.models.moon import Moon
from app.routes.routes_utilities import validate_model
from ..db import db

bp = Blueprint("moons_bp", __name__, url_prefix="/moons")

@bp.post("planets/<planet_id>/moons")
def create_moon_to_planet():
    planet = validate_model(Planet, planet_id)
    moon_data = request.get_json()
    moon_data["planet_id"] = planet.id
    
    return make_response(create_model(Moon, moon_data))



