from typing import Dict, Any, List
from src.objs.hub import Hub


class Dron:

    def __init__(self, id: str, where: Hub) -> None:
        self.id = id
        self.where = where  # Hub where dron is
        self.in_goal = False
        self.next_restricted = False
        self.hub_index = 0
        self.waiting_turns = 0
        self.path: List[Hub] = []


def create_drones(drones: int, hubs: Dict[str, Any]) -> Dict[str, Dron]:
    drones_dict = {}
    for hub in hubs.values():
        if hub.is_start:
            start_hub = hub
    for id in range(1, drones + 1):
        new_dron = Dron(
            "ID" + str(id),
            start_hub
        )
        drones_dict[new_dron.id] = new_dron
    return drones_dict
