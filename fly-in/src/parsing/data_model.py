from typing import List, Dict, Any, Self
from pydantic import BaseModel, Field, model_validator
from src.conf.enums import Colors
from icecream import ic

ic.configureOutput(contextAbsPath=True)


class ConnexValidator(BaseModel):

    map_connects: List[Dict[str, Any]] = Field(...)

    @model_validator(mode='after')
    def check_connections(self) -> Self:
        for item in self.map_connects:
            conn = item.get("conn", ())
            if len(conn) == 2 and conn[0] == conn[1]:
                raise ValueError(
                    f"{Colors.RED.value}[Error] - "
                    f"Same hubs in a connection!"
                    f"{Colors.RESET.value}"
                )
        return self


class HubsValidator(BaseModel):

    map_hubs: List[Dict[str, Any]] = Field(...)

    @model_validator(mode='after')
    def check_start_goal(self) -> Self:
        count_start = 0
        count_goal = 0
        for hub in self.map_hubs:
            if hub.get("is_start", False):
                count_start += 1
            if hub.get("is_goal", False):
                count_goal += 1
        if count_start > 1 or count_goal > 1:
            raise ValueError(
                f"{Colors.RED.value}[ERROR] - There are more than one "
                f"start_hub/end_hub. "
                f"Please, check the map file.{Colors.RESET.value}"
            )
        elif count_start < 1 or count_goal < 1:
            raise ValueError(
                f"{Colors.RED.value}[ERROR] - There are not start_hub/end_hub"
                f" Please, check the map file.{Colors.RESET.value}"
            )
        return self

    @model_validator(mode='after')
    def check_positive_coord(self) -> Self:
        for hub in self.map_hubs:
            if hub.get("x", -1) < 0 or hub.get("y", -1) < 0:
                raise ValueError(
                    f"{Colors.RED.value}[ERROR] - hub coordinates cannot be "
                    f"negative. Please, check it in map file and try again."
                    f"{Colors.RESET.value}"
                )
        return self

    @model_validator(mode='after')
    def check_start_goal_coord(self) -> Self:
        start = None
        goal = None
        for hub in self.map_hubs:
            if hub.get("is_start"):
                start_x = hub.get("x")
                start_y = hub.get("y")
                start = (start_x, start_y)
            if hub.get("is_goal"):
                goal_x = hub.get("x")
                goal_y = hub.get("y")
                goal = (goal_x, goal_y)
        if start is not None and goal is not None and start == goal:
            raise ValueError(
                f"{Colors.RED.value}[ERROR] - Start and Goal coordinates "
                f"cannot be the same. Please, check it in the map file."
                f"{Colors.RESET.value}"
            )
        return self

    @model_validator(mode='after')
    def check_zones(self) -> Self:
        valid_zones = ['normal', 'blocked', 'restricted', 'priority']
        for hub in self.map_hubs:
            if hub.get("zone", "normal") not in valid_zones:
                raise ValueError(
                    f"{Colors.RED.value}[ERROR] - "
                    f"Hub zone definition is not valid."
                    f" Please, check it in the map file."
                    f"{Colors.RESET.value}"
                    )
        return self


class DroneValidator(BaseModel):

    map_drones: int = Field(..., gt=0)
