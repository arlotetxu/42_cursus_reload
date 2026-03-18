from typing import Dict, Any, List
from src.objs.grid import Graph
from src.objs.hub import Hub
from heapq import heappop, heappush
from icecream import ic

ic.configureOutput(includeContext=True)

class AStar:

    def __init__(self, hubs: Dict[str, Any]) -> None:
        self.hubs = hubs

    # def init_a_star(self, goal_name: str = "goal") -> List[Hub]:
    def init_a_star(self) -> List[Hub]:
        self.open = []
        self.close = []
        # Setting all hub's g_cost to inf
        for hub in self.hubs.values():
            hub.g_cost = float('inf')

        start_hub = None
        goal_name = ""
        # Selecting the starting hub
        for hub in self.hubs.values():
            if hub.is_start:
                start_hub = hub
            if hub.is_goal:
                goal_name = hub.name
        # start_hub = self.hubs.get("start", None)
        if not start_hub:
            return []
        start_hub.g_cost = 0
        heappush(self.open, (start_hub.f_cost, start_hub.name))
        parent_map = {}

        while self.open:
            _, current_hub_name = heappop(self.open)
            current_hub_obj = self.hubs.get(current_hub_name, None)

            if current_hub_name == goal_name:
                path = []
                curr = current_hub_obj
                # Building the path from the goal hub
                while curr.name in parent_map:
                    path.append(curr)
                    curr = parent_map[curr.name]
                path.append(curr)  # Adding the starting hub
                return path[::-1]

            if current_hub_name in self.close:
                continue
            self.close.append(current_hub_name)

            for neighbor_name in current_hub_obj.neighbors:
                neighbor_obj = self.hubs.get(neighbor_name, None)

                if neighbor_obj is None or not neighbor_obj.is_crossable or neighbor_name in self.close:
                    continue

                tentative_g_cost = current_hub_obj.g_cost + neighbor_obj.traversal_cost
                if tentative_g_cost < neighbor_obj.g_cost:
                    neighbor_obj.g_cost = tentative_g_cost
                    parent_map[neighbor_name] = current_hub_obj
                    heappush(self.open, (neighbor_obj.f_cost, neighbor_obj.name))
        return []
