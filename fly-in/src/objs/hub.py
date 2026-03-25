from typing import Dict, Any, List


class Hub:
    """
    Represents a node in the simulation graph where drones can cross.
    """

    def __init__(self, name: str, x: int, y: int, color: str,
                 zone: str, max_drones: int, is_start: bool = True,
                 is_goal: bool = True) -> None:
        """
        Initializes a Hub instance.

        Args:
            name (str): Unique identifier for the hub.
            x (int): X-coordinate on the map.
            y (int): Y-coordinate on the map.
            color (str): Color associated with the hub for display.
            zone (str): Type of zone (normal, restricted, priority, etc).
            max_drones (int): Maximum capacity of drones.
            is_start (bool): True if it's a starting point.
            is_goal (bool): True if it's a destination point.

        Returns:
            None
        """
        self.name = name
        self.is_start = is_start
        self.is_goal = is_goal
        self.x = x
        self.y = y
        self.color = color
        self.zone = zone
        self.max_drones: int | float = int(max_drones)
        self.curr_drones = 0
        self.neighbors: Dict[str, int] = {}
        self.g_cost = 0
        self.h_cost: int | float = 0
        self.father: List[Hub] = []

    @property
    def traversal_cost(self) -> int | float:
        """
        Calculates the cost to traverse this hub based on its zone type.

        Returns:
            int | float: The weight used for pathfinding algorithms.
        """
        if self.zone == "restricted":
            return 2
        elif self.zone == "priority":
            return 0.8
        elif self.zone == "blocked":
            return (float('inf'))
        return 1

    @property
    def is_blocked(self) -> bool:
        """
        Checks if the hub is currently inaccessible.

        Returns:
            bool: True if the zone is 'blocked'.
        """
        return self.zone == "blocked"

    @property
    def is_crossable(self) -> bool:
        """
        Determines if a drone can enter the hub.

        Returns:
            bool: True if capacity is not reached and not blocked.
        """
        return (self.curr_drones < self.max_drones) and \
            not self.zone == "blocked"

    @property
    def f_cost(self) -> int | float:
        """
        Calculates the total A* cost (g + h).

        Returns:
            int | float: The combined cost for pathfinding.
        """
        return self.g_cost + self.h_cost

    def add_neighbors(self, map_validators: Dict[str, Any]) -> None:
        """
        Populates the neighbors dictionary based on map connections.

        Args:
            map_validators (Dict[str, Any]): Parsed map data containing
                connection information.
        """
        for conn in map_validators.get("conns", "").map_connects:
            origin, dest = conn.get("conn", "")
            if origin == self.name:
                self.neighbors[dest] = 0
