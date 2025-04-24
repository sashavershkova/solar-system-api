from sqlalchemy.orm import Mapped, mapped_column
from ..db import db

class Planet(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str]
    description: Mapped[str]
    distance_from_sun_mm_km: Mapped[float]


# planets = [
#     Planet(1, "Mercury", "The smallest planet in our solar system and closest to the Sun.", 57.9),
#     Planet(2, "Venus", "A rocky planet with a thick, toxic atmosphere and surface temperatures hot enough to melt lead.", 108.2),
#     Planet(3, "Earth", "The only planet known to support life, with vast oceans and diverse ecosystems.", 149.6),
#     Planet(4, "Mars", "The Red Planet, known for its iron oxide surface and potential for past water.", 227.9),
#     Planet(5, "Jupiter", "The largest planet in the solar system, a gas giant with a massive storm called the Great Red Spot.", 778.3)
# ]