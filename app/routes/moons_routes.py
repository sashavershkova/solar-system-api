from flask import Blueprint, abort, make_response, request, Response
from app.models.planet import Planet
from app.models.moon import Moon
from app.routes.routes_utilities import validate_model
from ..db import db

bp = Blueprint("moons_bp", __name__, url_prefix="/moons")


