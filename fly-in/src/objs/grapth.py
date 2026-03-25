from typing import Dict, Any, List, Tuple
from src.objs.hub import Hub
from heapq import heappop, heappush


class Graph:
    """
    Represents a graph structure containing hubs and manages
    pathfinding operations using A* algorithm.
    """

    def __init__(self, map_validators: Dict[str, Any]) -> None:
        """
        Initializes a Graph instance with map data.

        Args:
            map_validators (Dict[str, Any]): Parsed map data
                containing hub and connection information.

        Returns:
            None
        """
        self.map_validators = map_validators

    def create_graph(self) -> None:
        """
        Initializes all hubs from map data and establishes
        parent-child relationships between them.

        Returns:
            None
        """
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
                hub.get("is_start", False),
                hub.get("is_goal", False),
            )
            # Setting the hub neighbors
            new_hub.add_neighbors(self.map_validators)
            hubs_dict[new_hub.name] = new_hub

        self.hubs = hubs_dict
        # Setting the hub fathers:
        self.set_hubs_father(self.hubs)
        # Setting max_drones in start/end hubs
        self.start_end_max_drones()

    def get_hub(self, name: str) -> Hub | None:
        """
        Retrieves a hub by its name.

        Args:
            name (str): The name identifier of the hub.

        Returns:
            Hub | None: The Hub object if found, None otherwise.
        """
        return self.hubs.get(name, None)

    def set_hubs_father(self, hubs_dict: Dict[str, Hub]) -> None:
        """
        Establishes parent-child relationships between hubs based
        on their neighbor connections.

        Args:
            hubs_dict (Dict[str, Hub]): Dictionary of all hubs.

        Returns:
            None
        """
        for son in hubs_dict.values():
            for father_ in hubs_dict.values():
                if son.name in father_.neighbors:
                    son.father.append(father_)

    def set_h_cost(self) -> None:
        """
        Calculates heuristic costs (h_cost) for all hubs using
        a reverse Dijkstra from the goal hub.

        Returns:
            None
        """
        for hub in self.hubs.values():
            if hub.is_goal:
                goal_hub = hub
        if not goal_hub:
            return
        # Setting all hubs h_cost to infinite
        for hub in self.hubs.values():
            hub.h_cost = float(('inf'))
        goal_hub.h_cost = 0

        pq: List[Tuple[int | float, str]] = [(0, goal_hub.name)]
        while pq:
            current_dist, current_name = heappop(pq)
            current_hub = self.get_hub(current_name)

            if current_hub and current_dist > current_hub.h_cost:
                continue

            if current_hub:
                for father_ in current_hub.father:
                    # the h_cost is the father_ cost + current hub cost
                    new_dist = current_dist + current_hub.traversal_cost
                    if new_dist < father_.h_cost:
                        father_.h_cost = new_dist
                        heappush(pq, (new_dist, father_.name))

    def start_end_max_drones(self) -> None:
        """
        Sets unlimited drone capacity for start and goal hubs.

        Returns:
            None
        """
        for hub in self.hubs.values():
            if hub.is_start or hub.is_goal:
                hub.max_drones = float('inf')

    # def restart_costs(self) -> None:
    #     for _, hub in self.hubs.items():
    #         hub.g_cost = 0
    #         hub.h_cost = 0
    #         hub.father = []
