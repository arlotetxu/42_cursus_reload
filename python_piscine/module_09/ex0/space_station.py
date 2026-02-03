from pydantic import BaseModel, Field, ValidationError
from datetime import datetime
from typing import Optional


class SpaceStation(BaseModel):
    """
    Represents a space station with its operational parameters.
    """
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(gt=0, le=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)
    last_maintenance: datetime
    is_operational: bool = True
    notes: Optional[str] = Field(default=None, max_length=200)


def main() -> None:
    """
    Main function to validate and display space station data.
    Attempts to create SpaceStation objects with provided data,
    prints their details if valid, and handles validation errors.
    """

    print("Space Station Data Validation")
    print("========================================")

    ss1_data: dict = {
        "station_id": "LGW125",
        "name": "Titan Mining Outpost",
        "crew_size": 6,
        "power_level": 85.5,
        "oxygen_level": 92.3,
        "last_maintenance": "2025-01-31 13:00",
        "is_operational": True,
    }

    try:
        ss1: SpaceStation = SpaceStation(**ss1_data)
    except ValidationError as v_e:
        print(v_e)
        return

    print("Valid station created:")
    print(f"ID: {ss1.station_id}")
    print(f"Name: {ss1.name}")
    print(f"Crew: {ss1.crew_size} people")
    print(f"Power: {ss1.power_level}%")
    print(f"Oxygen: {ss1.oxygen_level}%")
    status = "✅ Operational" if ss1.is_operational else "⚠️ Maintenance"
    print(f"Status: {status}")
    print()
    print("========================================")

    ss2_data: dict = {
        "station_id": "QCH189",
        "name": "Deep Space Observatory",
        "crew_size": 21,
        "power_level": 85.5,
        "oxygen_level": 92.3,
        "last_maintenance": "2025-01-31 13:00",
        "is_operational": True,
    }

    try:
        print("Expected validation error:")
        ss2: SpaceStation = SpaceStation(**ss2_data)
        print(ss2)
    except ValidationError as v_e:
        for error in v_e.errors():
            print(error.get("msg"))


if __name__ == "__main__":
    main()
