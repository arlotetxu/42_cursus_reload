from typing import List, Dict, Any
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
        # self.coord = (x, y)
        self.color = color
        self.zone = zone
        self.max_drones = int(max_drones)
        # self.cross = True
        self.curr_drones = 0
        self.neighbors: Dict[str, int] = {}
        self.g_cost = 0
        self.h_cost = 0
        self.father = []

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
        for conn in map_validators.get("conns").map_connects:
            origin, dest = conn.get("conn", "")
            if origin == self.name:
                self.neighbors[dest] = 0

    # def define_neighbor_cost(self, hubs_dict: Dict[str, Any]) -> None:
    #     for neighbor in self.neighbors:
    #         if neighbor in hubs_dict:
    #             neighbor_hub = hubs_dict[neighbor]
    #             self.neighbors[neighbor] = neighbor_hub.traversal_cost

    def set_hubs_father(self, hubs_dict: Dict[str, Hub]) -> None:
        for son in hubs_dict.values():
            for father_ in hubs_dict.values():
                if son.name in father_.neighbors:
                    son.father.append(father_)


