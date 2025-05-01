import pytest
from app import create_app
from app.db import db
from flask.signals import request_finished
from dotenv import load_dotenv
from app.models.planet import Planet
import os

load_dotenv()

@pytest.fixture
def app():
    test_config = {
        "TESTING": True,
        "SQLALCHEMY_DATABASE_URI": os.environ.get('SQLALCHEMY_TEST_DATABASE_URI')
    }
    app = create_app(test_config)

    @request_finished.connect_via(app)
    def expire_session(sender, response, **extra):
        db.session.remove()

    with app.app_context():
        db.create_all()
        yield app

    with app.app_context():
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def two_saved_planets(app):
    pluto = Planet(name="Pluto", description="A dwarf planet in the Kuiper Belt, formerly classified as the ninth planet. It has a rocky and icy surface with a thin atmosphere of nitrogen, methane, and carbon monoxide.",
                    distance_from_sun_mm_km=5906)
    saturn = Planet(name="Saturn", description="A gas giant, the sixth planet from the Sun. Known for its spectacular ring system, composed mostly of ice particles, rocky debris, and dust.", 
                    distance_from_sun_mm_km=1429)
    db.session.add_all([pluto, saturn])
    db.session.commit()