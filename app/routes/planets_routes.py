from flask import Blueprint, abort, make_response, request, Response
from app.models.planet import Planet
from ..db import db

planets_bp = Blueprint("planets_bp", __name__, url_prefix="/planets")

@planets_bp.post("")
def create_planet():
    request_body = request.get_json()
    name = request_body["name"]
    description = request_body["description"]
    distance_from_sun_mm_km = request_body["distance_from_sun_mm_km"]

    new_planet = Planet(name=name, description=description, distance_from_sun_mm_km=distance_from_sun_mm_km)
    db.session.add(new_planet)
    db.session.commit()

    response = {
        "id": new_planet.id,
        "name": new_planet.name,
        "description": new_planet.description,
        "distance_from_sun_mm_km": new_planet.distance_from_sun_mm_km
    }

    return response, 201


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

@planets_bp.put("/<id>")
def update_one_planet(id):
    planet = validate_planet_id(id)
    request_body = request.get_json()
    
    planet.name = request_body["name"]
    planet.description = request_body["description"]
    planet.distance_from_sun_mm_km = request_body["distance_from_sun_mm_km"]

    db.session.commit()

    return Response(status=204, mimetype="application/json")

@planets_bp.delete("/<id>")
def delete_one_planet(id):
    planet = validate_planet_id(id)

    db.session.delete(planet)
    db.session.commit()

    return Response(status=204, mimetype="application/json")

def validate_planet_id(id):
    try:
        id = int(id)
    except:
        response = {"message": f"This ID {id} is invalid"}
        abort(make_response(response, 400))
    
    query = db.select(Planet).where(Planet.id == id)
    planet = db.session.scalar(query)   

    if not planet:
        response = {"message": f"Planet with ID {id} is not found"}
        abort(make_response(response, 404))

    return planet
