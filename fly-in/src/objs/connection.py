from typing import Dict, Tuple, Any
from src.objs.hub import Hub
from src.conf.enums import Colors


class Connection:
    """
    Represents a link between two hubs in the graph with capacity
    constraints for drone traversal.
    """

    def __init__(self, father: str, son: str, max_link_cap: int = 1
                 ) -> None:
        """
        Initializes a Connection instance.

        Args:
            father (str): Name or Hub object of the source hub.
            son (str): Name or Hub object of the destination hub.
            max_link_cap (int): Maximum drones allowed on this
                link simultaneously. Defaults to 1.

        Returns:
            None
        """
        self.father = father
        self.son = son
        self.max_link_cap = int(max_link_cap)
        self.curr_drones = 0

    @property
    def is_crossable(self) -> bool:
        """
        Checks if a drone can traverse this connection.

        Returns:
            bool: True if current drone count is below maximum
                capacity.
        """
        return self.curr_drones < self.max_link_cap


def create_connections(
        map_validators: Dict[str, Any],
        hubs: Dict[str, Hub]
        ) -> Dict[Tuple[str, str], Connection]:
    """
    Creates Connection objects from parsed map data and hub
    references.

    Args:
        map_validators (Dict[str, Any]): Parsed map data
            containing connection specifications.
        hubs (Dict[str, Hub]): Dictionary of Hub objects indexed
            by name.

    Returns:
        Dict[Tuple[str, str], Connection]: Dictionary mapping
            (father_name, son_name) tuples to Connection objects.

    Raises:
        ValueError: If a connection references a non-existent hub
            or has invalid data.
    """
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
                f"{Colors.RED.value}[ERROR#21] - There is an issue with "
                f"connections. Please, check the map file and try again."
                f"{Colors.RESET.value}")

    return connects_dict
