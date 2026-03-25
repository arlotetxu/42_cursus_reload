from typing import Dict, Any, List
from src.objs.hub import Hub


class Drone:
    """
    Represents a drone moving through hubs in the simulation.
    """

    def __init__(self, id: str, where: Hub) -> None:
        """
        Initializes a Dron instance.

        Args:
            id (str): Unique drone identifier.
            where (Hub): Current hub where the drone is located.

        Returns:
            None
        """
        self.id = id
        self.where = where  # Hub where dron is
        self.in_goal = False
        self.next_restricted = False
        self.hub_index = 0
        self.waiting_turns = 0
        self.path: List[Hub] = []


def create_drones(drones: int, hubs: Dict[str, Any]) -> Dict[str, Drone]:
    """
    Creates drones and places them at the start hub.

    Args:
        drones (int): Number of drones to create.
        hubs (Dict[str, Any]): Dictionary containing hub objects.

    Returns:
        Dict[str, Dron]: Dictionary of created drones keyed by ID.
    """
    drones_dict = {}
    for hub in hubs.values():
        if hub.is_start:
            start_hub = hub
    for id in range(1, drones + 1):
        new_dron = Drone(
            "D" + str(id),
            start_hub
        )
        drones_dict[new_dron.id] = new_dron
    return drones_dict
