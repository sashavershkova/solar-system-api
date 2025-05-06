# external
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
from typing import Optional
from ..db import db

class Moon(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str]
    description: Mapped[str]
    size: Mapped[int]
    planet_id: Mapped[Optional[int]] = mapped_column(ForeignKey("planet.id"))
    planet: Mapped[Optional["Planet"]] = relationship(back_populates="moons")

    

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "size": self.size
        }

    @classmethod
    def from_dict(cls, moon_data):
        planet_id = moon_data.get("planet_id")

        new_moon = cls(
            name=moon_data["name"],
            description=moon_data["description"],
            size=moon_data["size"],
            planet_id=planet_id
        )

        return new_moon