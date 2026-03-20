import sys
from typing import Dict, Any
from src.conf.enums import Colors
from src.parsing.map_parsing import parse_map
from src.objs.connection import create_connections
from src.objs.grapth import Graph
from src.objs.dron import create_drones
from src.objs.a_star import AStar
from src.objs.routing import start_simulation
from icecream import ic

ic.configureOutput(includeContext=True)


def main(map: str):
    print("Hello from main fly-in")
    map_validators: Dict[str, Any] = parse_map(map)
    # Creating grapth with hubs in it
    my_graph = Graph(map_validators)
    my_graph.create_graph()
    my_graph.set_h_cost()
    hubs_dict = my_graph.hubs
    # Creating connections
    connections_dict = create_connections(map_validators, hubs_dict)
    # Creating drones
    drones_nb = map_validators.get("drones").map_drones
    drones_dict = create_drones(drones_nb, hubs_dict)
    # for dron in drones_dict.values():
    #     ic(dron.id)
    #     ic(dron.where.name)

    # Calculating the optimal path
    # my_astar = AStar(hubs_dict)
    # path = my_astar.init_a_star()
    # for r in path:
    #     ic(r.name)
    start_simulation(drones_dict, connections_dict, hubs_dict)

    # ic(map_validators.get("conns", None).map_connects)
    # ic(hubs_dict.get("waypoint2", "").x,
    #    hubs_dict.get("waypoint2", "").y,
    #    hubs_dict.get("waypoint2", "").zone,
    #    hubs_dict.get("waypoint2", "").is_start,
    #    hubs_dict.get("waypoint2", "").is_goal,
    #    hubs_dict.get("waypoint2", "").neighbors,
    #    hubs_dict.get("waypoint2", "").g_cost,
    #    hubs_dict.get("waypoint2", "").h_cost,
    #    hubs_dict.get("waypoint2", "").f_cost,
    #    hubs_dict.get("waypoint2", "").father,
    #    )


if __name__ == "__main__":

    if len(sys.argv) != 2:
        print(f"{Colors.RED.value}[ERROR] - Invalid number of arguments!"
              f"{Colors.RESET.value}")
        sys.exit(1)
    main(map=sys.argv[1])
