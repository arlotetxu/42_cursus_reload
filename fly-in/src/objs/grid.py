from typing import Dict, Any
from src.objs.hub import Hub
from icecream import ic

class Grid:

    def __init__(self, map_validators: Dict[str, Any]) -> None:
        self.map_validators = map_validators

    def create_grid(self):
        hubs_dict = {}
        hub_data = self.map_validators.get("hubs", "").map_hubs
        for hub in hub_data:
            new_hub = Hub(
                hub.get("name", ""),
                hub.get("x", -1),
                hub.get("y", -1),
                hub.get("color"),
                hub.get("zone", "normal"),
                hub.get("max_drones", 1),
            )
            new_hub.add_neighbors(self.map_validators)
            
            hubs_dict[new_hub.name] = new_hub
        for hub in hubs_dict.values():
            hub.define_neighbor_cost(hubs_dict)
        # ic(hubs_dict)
        self.hubs = hubs_dict

    def get_hub(self, name: str) -> Hub:
        return self.hubs.get(name, None)

    def restart_costs(self) -> None:
        for _, hub in self.hubs.items():
            hub.g_cost = 0
            hub.h_cost = 0
            hub.f_cost = hub.calc_f_cost()
            hub.father = ""
