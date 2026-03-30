from typing import List, Dict, Any
from typing_extensions import Self
from pydantic import BaseModel, Field, model_validator
from src.conf.enums import Colors


class ConnexValidator(BaseModel):
    """
    Validator for map connections data.

    Attributes:
        map_connects (List[Dict[str, Any]]): List of connection data.
    """

    map_connects: List[Dict[str, Any]] = Field(...)

    @model_validator(mode='after')
    def check_connections(self) -> Self:
        """
        Verify that a connection does not link a hub to itself.

        Returns:
            Self: The validated instance.
        """
        for item in self.map_connects:
            conn = item.get("conn", ())
            if len(conn) == 2 and conn[0] == conn[1]:
                raise ValueError(
                    f"{Colors.RED.value}[Error#13] - "
                    f"Same hubs in a connection!"
                    f"{Colors.RESET.value}"
                )
        return self

    @model_validator(mode='after')
    def check_connections_dupli(self) -> Self:
        """
        Check for duplicated connections in the map data.

        Returns:
            Self: The validated instance.
        """
        con_1 = None
        con_2 = None
        for item in self.map_connects:
            con_1, con_2 = item.get("conn", ())
            con_3, con_4 = None, None
            for item in self.map_connects:
                con_3, con_4 = item.get("conn", ())
                if con_1 == con_4 and con_3 == con_2:
                    raise ValueError(
                        f"{Colors.RED.value}[Error#14] - "
                        f"Duplicated Connection ({con_1}-{con_2}). "
                        f"Please, check the map file.{Colors.RESET.value}"
                    )
        return self


class HubsValidator(BaseModel):
    """
    Validator for map hubs data.

    Attributes:
        map_hubs (List[Dict[str, Any]]): List of hub dictionaries.
    """

    map_hubs: List[Dict[str, Any]] = Field(...)

    @model_validator(mode='after')
    def check_start_goal(self) -> Self:
        """
        Ensure exactly one start hub and one end hub are defined.

        Returns:
            Self: The validated instance.
        """
        count_start = 0
        count_goal = 0
        for hub in self.map_hubs:
            if hub.get("is_start", False):
                count_start += 1
            if hub.get("is_goal", False):
                count_goal += 1
        if count_start > 1 or count_goal > 1:
            raise ValueError(
                f"{Colors.RED.value}[ERROR#15] - There are more than one "
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
        """
        Verify that all hub coordinates are non-negative.

        Returns:
            Self: The validated instance.
        """
        for hub in self.map_hubs:
            if hub.get("x", -1) < 0 or hub.get("y", -1) < 0:
                raise ValueError(
                    f"{Colors.RED.value}[ERROR#16] - hub coordinates cannot be"
                    f" negative. Please, check it in map file and try again."
                    f"({hub.get('x', -1)} {hub.get('y', -1)})"
                    f"{Colors.RESET.value}"
                )
        return self

    @model_validator(mode='after')
    def check_start_goal_coord(self) -> Self:
        """
        Ensure start and goal hubs do not share the same coordinates.

        Returns:
            Self: The validated instance.
        """
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
                f"{Colors.RED.value}[ERROR#17] - Start and Goal coordinates "
                f"cannot be the same. Please, check it in the map file."
                f"{Colors.RESET.value}"
            )
        return self

    @model_validator(mode='after')
    def check_zones(self) -> Self:
        """
        Validate that hub zones belong to the allowed set of types.

        Returns:
            Self: The validated instance.
        """
        valid_zones = ['normal', 'blocked', 'restricted', 'priority']
        for hub in self.map_hubs:
            if hub.get("zone", "normal") not in valid_zones:
                raise ValueError(
                    f"{Colors.RED.value}[ERROR#18] - "
                    f"Hub zone definition ({hub.get('zone')}) is not valid."
                    f" Please, check it in the map file."
                    f"{Colors.RESET.value}"
                    )
        return self

    @model_validator(mode='after')
    def check_hub_names(self) -> Self:
        """
        Check for unique hub names and forbidden characters.

        Returns:
            Self: The validated instance.
        """
        hub_names = []
        for hub in self.map_hubs:
            hub_name = hub.get("name", "")
            if hub_name in hub_names:
                raise ValueError(
                    f"{Colors.RED.value}[ERROR#19] - "
                    f"There are duplicated hub names ({hub_name}). "
                    f"Please, check the map file and try again."
                    f"{Colors.RESET.value}"
                )
            hub_names.append(hub_name)
            if "-" in hub_name:
                raise ValueError(
                    f"{Colors.RED.value}[ERROR#20] - "
                    f"There are not allowed chars in hub names ({hub_name})."
                    f" Please, check the map file and try again."
                    f"{Colors.RESET.value}"
                )
        return self


class DroneValidator(BaseModel):
    """
    Validator for the number of drones.

    Attributes:
        map_drones (int): Number of drones, must be greater than zero.
    """

    map_drones: int = Field(..., gt=0)
