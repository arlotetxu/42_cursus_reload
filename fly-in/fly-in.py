import sys
from typing import Dict, Any
from src.conf.enums import Colors
from src.parsing.map_parsing import parse_map
# from src.hub.hub import add_hubs
from src.objs.connection import Connection
from src.objs.grid import Grid
from src.objs.a_star import AStar
from icecream import ic


def main(map: str):
    print("Hello from main fly-in")
    map_validators: Dict[str, Any] = parse_map(map)
    # Creating grid and hubs whithin it
    my_grid = Grid(map_validators)
    my_grid.create_grid()
    my_astar = AStar(my_grid.hubs)
    my_astar.init_astar()
    # my_connecion = Connection(map_validators)
    # my_grid.restart_costs()
    # ic(map_validators.get("conns").map_connects)
    # ic(my_grid.hubs.get("waypoint1", "").coord,
    #    my_grid.hubs.get("waypoint1", "").zone,
    #    my_grid.hubs.get("waypoint1", "").neighbors,
    #    my_grid.hubs.get("waypoint1", "").g_cost,
    #    my_grid.hubs.get("waypoint1", "").f_cost,)
    # ic(map_validators.get("conns", None).map_connects)


if __name__ == "__main__":

    if len(sys.argv) != 2:
        print(f"{Colors.RED.value}[ERROR] - Invalid number of arguments!"
              f"{Colors.RESET.value}")
        sys.exit(1)
    main(map=sys.argv[1])
