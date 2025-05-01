from flask import Blueprint, abort, make_response, request, Response
from app.models.planet import Planet
from app.routes.routes_utilities import validate_model
from ..db import db

planets_bp = Blueprint("planets_bp", __name__, url_prefix="/planets")

@planets_bp.post("")
def create_planet():
    request_body = request.get_json()
    new_planet = Planet.from_dict(request_body)

    db.session.add(new_planet)
    db.session.commit()

    return new_planet.to_dict(), 201


@planets_bp.get("")
def get_planets():
    query = db.select(Planet)

    name_param = request.args.get("name")
    if name_param:
        query = query.where(Planet.name.ilike(f"%{name_param}%"))

    description_param = request.args.get("description")
    if description_param:
        query = query.where(Planet.description.ilike(f"%{description_param}%"))
    
    distance_param = request.args.get("distance_from_sun_mm_km")
    if distance_param:
        query = query.where(Planet.distance_from_sun_mm_km.ilike(f"%{distance_param}%"))

    query = query.order_by(Planet.id)
    planets = db.session.scalars(query)

    response_planets = []
    for planet in planets:
        response_planets.append(planet.to_dict())
        
    return response_planets

@planets_bp.get("/<id>")
def get_one_planet(id):
    planet = validate_model(Planet, id)

    return planet.to_dict()

@planets_bp.put("/<id>")
def update_one_planet(id):
    planet = validate_model(Planet, id)
    request_body = request.get_json()
    
    planet.name = request_body["name"]
    planet.description = request_body["description"]
    planet.distance_from_sun_mm_km = request_body["distance_from_sun_mm_km"]

    db.session.commit()

    return Response(status=204, mimetype="application/json")

@planets_bp.delete("/<id>")
def delete_one_planet(id):
    planet = validate_model(Planet, id)

    db.session.delete(planet)
    db.session.commit()

    return Response(status=204, mimetype="application/json")
