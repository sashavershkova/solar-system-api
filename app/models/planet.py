from sqlalchemy.orm import Mapped, mapped_column, relationship
from ..db import db

class Planet(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str]
    description: Mapped[str]
    distance_from_sun_mm_km: Mapped[float]
    moons: Mapped[list["Moon"]] = relationship(back_populates="planet")

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "distance_from_sun_mm_km": self.distance_from_sun_mm_km,
            "moons": [moon.to_dict() for moon in self.moons] if self.moons else []
        }

    @classmethod
    def from_dict(cls, planet_data):
        planet = cls(name=planet_data["name"], description=planet_data["description"], distance_from_sun_mm_km=planet_data["distance_from_sun_mm_km"])

        return planet

