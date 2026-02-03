from datetime import datetime
from enum import Enum
from typing import List
from pydantic import BaseModel, Field, model_validator, ValidationError


class Rank(Enum):
    """
    Enumeration of space crew ranks.
    """
    CADET = "cadet"
    OFFICER = "officer"
    LIEUTENANT = "lieutenant"
    CAPTAIN = "captain"
    COMMANDER = "commander"


class CrewMember(BaseModel):
    """
    Represents a member of the space crew with personal and professional
    details.
    """
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = True


class SpaceMission(BaseModel):
    """
    Represents a space mission including its crew and validation requirements.
    """
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(ge=1, le=3650)
    crew: List[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = Field(default="planned")
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode='after')
    def check_id(self):
        """
        Validates that the mission_id starts with the prefix 'M'.
        """
        if not self.mission_id.startswith('M'):
            raise ValueError("Mission ID must start with 'M'.")
        return self

    @model_validator(mode='after')
    def check_rank(self):
        """
        Ensures the mission has at least one high-ranking officer (Captain
        or Commander).
        """
        has_proper_rank: bool = False
        for member in self.crew:
            if member.rank.value in ["captain", "commander"]:
                has_proper_rank = True
        if not has_proper_rank:
            raise ValueError(
                "Mission must have at least one Commander or Captain.")
        return self

    @model_validator(mode='after')
    def check_long_mission(self):
        """
        Validates that long missions have a sufficient ratio of experienced
        crew members.
        """
        mission_years: int = self.duration_days / 365
        crew_experienced: int = sum(
            1 for member in self.crew if member.years_experience > 5
            )
        if mission_years > 1 and (crew_experienced / len(self.crew)) < 0.5:
            raise ValueError(
                "Long missions (>365 days) need 50% experience "
                "crew (5+ years).")
        return self

    @model_validator(mode='after')
    def check_crew_status(self):
        """
        Verifies that all assigned crew members are currently active.
        """
        all_crew_active: bool = True
        for member in self.crew:
            if not member.is_active:
                all_crew_active = False
        if not all_crew_active:
            raise ValueError("All crew members must be active.")
        return self


def ft_printing_mission(mission: SpaceMission) -> None:
    """
    Prints the details of a SpaceMission in a formatted manner.
    """
    if not mission:
        print("[ERROR] No mission data available.")
        return
    print(f"Mission: {mission.mission_name}")
    print(f"ID: {mission.mission_id}")
    print(f"Destination: {mission.destination}")
    print(f"Duration: {mission.duration_days} days")
    print(f"Budget: ${mission.budget_millions:.1f}M")
    print(f"Crew size: {len(mission.crew)}")
    print("Crew members:")
    for member in mission.crew:
        print(
            f"- {member.name} ({member.rank.value}) - {member.specialization}"
            )


def main() -> None:
    """
    Main entry point to demonstrate SpaceMission validation with various
    scenarios.
    """
    print("Space Mission Crew Validation")
    print("="*42)
    print("Valid mission created:")
    crew_mission_1: list = [
        CrewMember(
            member_id="CM001",
            name="Sarah Williams",
            rank="captain",
            age=43,
            specialization="Mission Command",
            years_experience=19,
            is_active=True
            ),
        CrewMember(
            member_id="CM002",
            name="James Hernandez",
            rank="captain",
            age=43,
            specialization="Pilot",
            years_experience=30,
            is_active=True
            ),
        CrewMember(
            member_id="CM003",
            name="Anna Jones",
            rank="cadet",
            age=35,
            specialization="Communications",
            years_experience=15,
            is_active=True
            ),
        CrewMember(
            member_id="CM004",
            name="David Smith",
            rank="commander",
            age=27,
            specialization="Security",
            years_experience=15,
            is_active=True
            ),
        CrewMember(
            member_id="CM005",
            name="Maria Jones",
            rank="cadet",
            age=55,
            specialization="Research",
            years_experience=30,
            is_active=True
            ),
    ]
    mission_1_data: dict = {
        "mission_id": "M2024_TITAN",
        "mission_name": "Solar Observatory Research Mission",
        "destination": "Solar Observatory",
        "launch_date": "2024-03-30T00:00:00",
        "duration_days": 451,
        "crew": crew_mission_1,
        "mission_status": "planned",
        "budget_millions": 2208.1
    }

    try:
        mission_1: SpaceMission = SpaceMission(**mission_1_data)
        ft_printing_mission(mission_1)
    except (ValidationError) as v_e:
        for error in v_e.errors():
            print(error.get("msg"))

    print("")
    print("="*42)
    print("Expected validation error:")
    crew_mission_2: list = [
        CrewMember(
            member_id="CM001",
            name="Sarah Williams",
            rank="cadet",
            age=43,
            specialization="Mission Command",
            years_experience=1,
            is_active=True
            ),
        CrewMember(
            member_id="CM002",
            name="James Hernandez",
            rank="cadet",
            age=43,
            specialization="Pilot",
            years_experience=3,
            is_active=True
            ),
        CrewMember(
            member_id="CM003",
            name="Anna Jones",
            rank="cadet",
            age=35,
            specialization="Communications",
            years_experience=15,
            is_active=True
            ),
        CrewMember(
            member_id="CM004",
            name="David Smith",
            rank="cadet",
            age=27,
            specialization="Security",
            years_experience=15,
            is_active=True
            ),
        CrewMember(
            member_id="CM005",
            name="Maria Jones",
            rank="cadet",
            age=55,
            specialization="Research",
            years_experience=30,
            is_active=True
            ),
    ]
    mission_2_data: dict = {
        "mission_id": "M2024_EUROPA",
        "mission_name": "Saturn Rings Research Mission",
        "destination": "Saturn Rings",
        "launch_date": "2024-09-18T00:00:00",
        "duration_days": 602,
        "crew": crew_mission_2,
        "mission_status": "planned",
        "budget_millions": 1092.6
    }
    try:
        mission_2: SpaceMission = SpaceMission(**mission_2_data)
        ft_printing_mission(mission_2)
    except (ValidationError) as v_e:
        for error in v_e.errors():
            print(error.get("msg"))


if __name__ == "__main__":
    main()
