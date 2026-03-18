from typing import Dict, Any
from src.objs.hub import Hub

class Dron:

    def __init__(self, id: str, where) -> None:
        self.id = id
        self.where: Hub = where  # Hub name wher dron is
        self.in_goal = False
        self.in_restricted = False


def create_drones(drones: int, hubs: Dict[str, Any]) -> Dict[str, Dron]:
    drones_dict = {}
    for hub in hubs.values():
        if hub.is_start:
            start_hub = hub
    for id in range(1, drones + 1):
        new_dron = Dron(
            "ID-" + str(id),
            start_hub
        )
        drones_dict[new_dron.id] = new_dron
    return drones_dict


