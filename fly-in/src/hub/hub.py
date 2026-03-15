from typing import List, Dict, Any
from icecream import ic


class Hub:

    def __init__(self, name: str, x: int, y: int,
                 color: str, zone: str, max_drones: int) -> None:
        self.name = name
        self.x = x
        self.y = y
        self.color = color
        self.zone = zone
        self.cross = True
        self.max_drones = max_drones
        self.curr_drones = 0
        self.neighbors: Dict[str, int] = {}
        self.g_cost = 0
        self.h_cost = 0
        # self.from

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
        return self.curr_drones < self.max_drones

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

    def f_cost(self) -> int:
        return self.g_cost + self.h_cost


def add_hubs(
        hub_data: List[str, str | int],
        map_validators: Dict[str, Any]) -> Dict[str, Any]:
    hubs_dict = {}
    for hub in hub_data:
        new_hub = Hub(
            hub.get("name", ""),
            hub.get("x", -1),
            hub.get("y", -1),
            hub.get("color"),
            hub.get("zone", "normal"),
            hub.get("max_drones", 1),
        )
        new_hub.add_neighbors(map_validators)
        hubs_dict[new_hub.name] = new_hub
    for hub in hubs_dict.values():
        hub.define_neighbor_cost(hubs_dict)
    # ic(hubs_dict)
    return hubs_dict
