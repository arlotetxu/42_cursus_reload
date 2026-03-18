import sys
from typing import Dict, Any
from src.conf.enums import Colors
from src.parsing.map_parsing import parse_map
from src.objs.connection import Connection
from src.objs.grid import Graph
from src.objs.dron import create_drones
from src.objs.a_star import AStar
from icecream import ic

ic.configureOutput(includeContext=True)


def main(map: str):
    print("Hello from main fly-in")
    map_validators: Dict[str, Any] = parse_map(map)
    # Creating grid and hubs whithin it
    my_grid = Graph(map_validators)
    my_grid.create_graph()
    my_grid.set_h_cost()

    my_astar = AStar(my_grid.hubs)
    path = my_astar.init_a_star()
    for r in path:
        ic(r.name)
    drones_nb = map_validators.get("drones").map_drones
    drones_dict = create_drones(drones_nb, my_grid.hubs)
    for dron in drones_dict.values():
        ic(dron.id)
        ic(dron.where.name)


    # ic(map_validators.get("conns").map_connects)
    # ic(map_validators.get("conns", None).map_connects)
    # ic(my_grid.hubs.get("waypoint2", "").coord,
    # my_grid.hubs.get("waypoint2", "").zone,
    # my_grid.hubs.get("waypoint2", "").neighbors,
    # my_grid.hubs.get("waypoint2", "").g_cost,
    # my_grid.hubs.get("waypoint2", "").h_cost,
    # my_grid.hubs.get("waypoint2", "").f_cost,
    # my_grid.hubs.get("waypoint2", "").father),
    # )


if __name__ == "__main__":

    if len(sys.argv) != 2:
        print(f"{Colors.RED.value}[ERROR] - Invalid number of arguments!"
              f"{Colors.RESET.value}")
        sys.exit(1)
    main(map=sys.argv[1])
