import sys
from typing import Dict, Any
from src.conf.enums import Colors
from src.parsing.map_parsing import parse_map
from src.objs.connection import create_connections
from src.objs.grapth import Graph
from src.objs.drone import create_drones
from src.objs.simulation import Simulation


def main(map: str) -> None:
    """
    Main entry point for the fly-in simulation.

    Args:
        map (str): Path to the map file to be parsed and simulated.

    Returns:
        None
    """
    print("Hello from main fly-in")
    try:
        map_validators: Dict[str, Any] = parse_map(map)
        # Creating grapth with hubs in it
        my_graph = Graph(map_validators)
        my_graph.create_graph()
        my_graph.set_h_cost()
        hubs_dict = my_graph.hubs
        # Creating connections
        connections_dict = create_connections(map_validators, hubs_dict)

    # Creating drones
        drone_validator = map_validators.get("drones")
        if drone_validator is not None:
            drones_nb = drone_validator.map_drones
        else:
            print(f"{Colors.RED.value}[ERROR#2] - "
                  f"The number of drones couldn't be found in the map file."
                  f" Please, check it and try again.{Colors.RESET.value}")
            sys.exit(1)
        drones_dict = create_drones(drones_nb, hubs_dict)

    # Starting the simulation
        my_simulation = Simulation()
        my_simulation.start_simulation(
            drones_dict, connections_dict, hubs_dict)
    except (ValueError) as ve:
        print(ve)
        sys.exit(1)


if __name__ == "__main__":

    if len(sys.argv) != 2:
        print(f"{Colors.RED.value}[ERROR#1] - Invalid number of arguments!"
              f"{Colors.RESET.value}")
        sys.exit(1)
    main(map=sys.argv[1])
