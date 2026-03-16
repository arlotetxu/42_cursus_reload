from typing import Dict, Any
from src.objs.grid import Grid
from heapq import heappop, heappush
from icecream import ic

class AStar:

    def __init__(self, hubs: Dict[str, Any]) -> None:
        self.hubs = hubs
        self.open = []
        self.close = []

    def init_astar(self):
        start_hub = self.hubs.get("start", None)
        ic(start_hub.g_cost)
        heappush(self.open, (start_hub.g_cost, start_hub))
        ic(self.open)

