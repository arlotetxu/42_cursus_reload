from typing import List, Dict, Tuple, Any
from src.objs.hub import Hub

from icecream import ic

class Connection:

    def __init__(self, father: str, son: str, max_link_cap: int) -> None:
        self.father = father
        self.son = son
        self.max_link_cap = max_link_cap


def create_connections(map_validators: Dict[str, Any], hubs: Dict[str, Hub]) -> Dict[Tuple [str, str], Hub]:
    from src.objs.hub import Hub
    connects_dict = {}
    connections = map_validators.get("conns").map_connects

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
        connects_dict[(father.name, son.name)] = new_con

    return connects_dict

