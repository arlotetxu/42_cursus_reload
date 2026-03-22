from typing import Dict, Any, List
from icecream import ic

ic.configureOutput(includeContext=True)


class Hub:

    def __init__(self, name: str, x: int, y: int, color: str,
                 zone: str, max_drones: int, is_start: bool = True,
                 is_goal: bool = True) -> None:
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
        if self.zone == "restricted":
            return 2
        elif self.zone == "priority":
            return 0.8
        elif self.zone == "blocked":
            return (float('inf'))
        return 1

    @property
    def is_blocked(self) -> bool:
        return self.zone == "blocked"

    @property
    def is_crossable(self) -> bool:
        return (self.curr_drones < self.max_drones) and \
            not self.zone == "blocked"

    @property
    def f_cost(self) -> int | float:
        return self.g_cost + self.h_cost

    def add_neighbors(self, map_validators: Dict[str, Any]) -> None:
        for conn in map_validators.get("conns", "").map_connects:
            origin, dest = conn.get("conn", "")
            if origin == self.name:
                self.neighbors[dest] = 0
