from datetime import datetime
from enum import Enum
from typing import List

from pydantic import BaseModel, Field, model_validator


class Rank(Enum):
    CADET = "cadet"
    OFFICER = "officer"
    LIEUTENANT = "lieutenant"
    CAPTAIN = "captain"
    COMMANDER = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = True


class SpaceMission(BaseModel):
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
       if not self.mission_id.startswith('M'):
          raise ValueError("Mission ID must start with 'M'")
       return self

    @model_validator(mode='after')
    def check_rank(self):
        has_proper_rank = False
        for member in self.crew:
            if member.value in ["captain", "commander"]:
                has_proper_rank = True
        if not has_proper_rank:
            raise ValueError("There is needed a Captain or Commander whithin the crew")
        return self

