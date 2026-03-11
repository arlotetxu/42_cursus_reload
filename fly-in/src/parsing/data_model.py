from typing import List, Dict, Any, Self, Tuple
from pydantic import BaseModel, Field, model_validator, ValidationError
from src.conf.enums import Colors
from icecream import ic

'''
The zones coordinates will always be positive integers, and there
will always be a unique start and a unique end zone.


'''

class ConnexValidator(BaseModel):

    map_connects: List[Tuple[str, str]] = Field(...)

    @model_validator(mode='after')
    def check_connections(self) -> Self:
        for con in self.map_connects:
            if con[0] is con[1]:
                raise ValidationError(
                    f"{Colors.RED.value}[Error] - Same hubs in connection!"
                    f"{Colors.RESET.value}"
                )
        return self


class HubsValidator(BaseModel):

    map_hubs: List[Dict[str, Any]] = Field(...)

    @model_validator(mode='after')
    def check_positive_coord(self) -> Self:
        for hub in self.map_hubs:
            if hub.get("x") < 0 or hub.get("y") < 0:
                raise ValidationError(
                    f"{Colors.RED.value}[ERROR] - hub coordinates cannot be "
                    f"negative. Please, check it in map file and try again."
                    f"{Colors.RESET.value}"
                )
        return self

    @model_validator(mode='after')
    def check_start_goal_coord(self) -> Self:
        for hub in self.map_hubs:
            if hub.get("name") == 'start':
                start_x = hub.get("x")
                start_y = hub.get("y")
                start = (start_x, start_y)
            elif hub.get("name") == 'goal':
                goal_x = hub.get("x")
                goal_y = hub.get("y")
                goal = (goal_x, goal_y)
        if start == goal:
            raise ValidationError(
                f"{Colors.RED.value}[ERROR] - Start and Goal coordinates "
                f"cannot be the same. Please, check it in the map file."
                f"{Colors.RESET.value}"
            )
        return self

    @model_validator(mode='after')
    def check_unique_start_goal(self) -> Self:
        starts = sum(1 for hub in self.map_hubs if hub.get("name") == 'start')
        goals = sum(1 for hub in self.map_hubs if hub.get("name") == 'goal')
        if starts > 1 or goals > 1:
            raise ValidationError(
                f"{Colors.RED.value}[ERROR] - There are more than one start/"
                f"goal point in the map's hubs definition. Please, check it "
                f"in the map file.{Colors.RESET.value}"
            )
        return self


class DroneValidator(BaseModel):

    map_drones: int = Field(..., gt=0)

