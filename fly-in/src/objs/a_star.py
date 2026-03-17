from typing import Dict, Any
from src.objs.grid import Grid
from heapq import heappop, heappush
from icecream import ic

ic.configureOutput(includeContext=True)

class AStar:

    def __init__(self, hubs: Dict[str, Any]) -> List:
        self.hubs = hubs
        self.open = []
        self.close = []

    def init_astar(self):
        for hub in self.hubs.values():
            hub.g_cost = float('inf')

        start_hub = self.hubs.get("start", None)
        if not start_hub:
            return []
        start_hub.g_cost = 0
        heappush(self.open, (start_hub.f_cost, start_hub.name))
        parent_map = {}

        while self.open:
            _, current_hub_name = heappop(self.open)
            current_hub_obj = self.hubs.get(current_hub_name, None)

            if current_hub_obj.name == 'goal':
                path = []
                curr = current_hub_obj
                while curr.name in parent_map:
                    path.append(curr)
                    curr = parent_map[curr.name]
                path.append(curr)
                return path[::-1]

            if current_hub_name in self.close:
                continue
            self.close.append(current_hub_name)

            for neighbor_name in current_hub_obj.neighbors:
                neighbor_obj = self.hubs.get(neighbor_name, None)

                if not neighbor_obj.is_crossable or neighbor_obj in self.close:
                    continue

                tentative_g_cost = current_hub_obj.g_cost + neighbor_obj.traversal_cost
                if tentative_g_cost < neighbor_obj.g_cost:
                    neighbor_obj.g_cost = tentative_g_cost
                    parent_map[neighbor_name] = current_hub_obj
                    heappush(self.open, (neighbor_obj.f_cost, neighbor_obj.name))
        return []
