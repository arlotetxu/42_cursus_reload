import sys
from src.conf.enums import Colors
from icecream import ic

class Hub:

    def __init__(self, name: str, x: int, y: int,
                 color: str, zone: str, max_drones: int):
        self.name = name
        self.x = x
        self.y = y
        self.color = color
        self.zone = zone
        self.max_drones = max_drones
        self.neighbors: Dict[str, int] = {}

    @property
    def traversal_cost(self) -> int:
        if self.zone == "restricted":
            return 2
        return 1

    @property
    def is_blocked(self) -> bool:
        return self.zone == "blocked"



def add_hubs(hub_data: list):
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
        hubs_dict[new_hub.name] = new_hub
    # ic(hubs_dict)
    return hubs_dict
