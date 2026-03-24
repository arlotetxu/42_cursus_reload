from typing import Dict, Tuple, Any
from src.objs.hub import Hub
from src.conf.enums import Colors
from icecream import ic

ic.configureOutput(contextAbsPath=True)


class Connection:

    def __init__(self, father: str, son: str, max_link_cap: int = 1) -> None:
        self.father = father
        self.son = son
        self.max_link_cap = int(max_link_cap)
        self.curr_drones = 0

    @property
    def is_crossable(self) -> bool:
        return self.curr_drones < self.max_link_cap


def create_connections(
        map_validators: Dict[str, Any],
        hubs: Dict[str, Hub]
        ) -> Dict[Tuple[str, str], Connection]:

    connects_dict = {}
    connections = map_validators.get("conns", "").map_connects

    for connection in connections:
        father, son = connection.get("conn", "")
        for hub in hubs.values():
            if hub.name == father:
                father = hub
            elif hub.name == son:
                son = hub
        max_link_cap = connection.get("max_link_capacity", 1)
        new_con = Connection(
            father, son, max_link_cap
        )
        try:
            connects_dict[(father.name, son.name)] = new_con
        except Exception:
            raise ValueError(
                f"{Colors.RED.value}[ERROR] - There is an issue with "
                f"connections. Please, check the map file and try again."
                f"{Colors.RESET.value}")

    return connects_dict
