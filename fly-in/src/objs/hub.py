from typing import List, Dict, Any
from src.objs.connection import Connection
from icecream import ic


class Hub:

    def __init__(self, name: str, x: int, y: int,
                 color: str, zone: str, max_drones: int) -> None:
        self.name = name
        # self.x = x
        # self.y = y
        self.coord = (x, y)
        self.color = color
        self.zone = zone
        self.cross = True
        self.max_drones = max_drones
        self.curr_drones = 0
        self.neighbors: Dict[str, int] = {}
        self.g_cost = self.traversal_cost
        self.h_cost = 0
        self.f_cost = self.calc_f_cost()
        self.father = ""

    @property
    def traversal_cost(self) -> int:
        if self.zone == "restricted":
            return 2
        return 1

    @property
    def is_blocked(self) -> bool:
        return self.zone == "blocked"

    @property
    def is_crossable(self) -> bool:
        return self.curr_drones < self.max_drones and not self.is_blocked

    def add_neighbors(self, map_validators: Dict[str, Any]) -> None:
        for conn in map_validators.get("conns").map_connects:
            origin, dest = conn.get("conn", "")
            if origin == self.name:
                self.neighbors[dest] = 0

    def define_neighbor_cost(self, hubs_dict: Dict[str, Any]) -> None:
        for neighbor in self.neighbors:
            if neighbor in hubs_dict:
                neighbor_hub = hubs_dict[neighbor]
                self.neighbors[neighbor] = neighbor_hub.traversal_cost

    def calc_f_cost(self) -> int:
        return self.g_cost + self.h_cost

