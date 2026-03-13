import sys
from typing import Dict, Any
from src.conf.enums import Colors
from src.parsing.map_parsing import parse_map
from src.hub.hub import Hub
from src.hub.hub import add_hubs
from icecream import ic

def main(map: str):
    print("Hello from main fly-in")
    map_validators: Dict[str, Any] = parse_map(map)
    # Creating hubs
    hubs_dict = add_hubs(map_validators.get("hubs", "").map_hubs)
    # ic(hubs_dict.get("waypoint1", "").x,
    #    hubs_dict.get("waypoint1", "").y,
    #    hubs_dict.get("waypoint1", "").zone,
    #    hubs_dict.get("waypoint1", "").neighbors)
    # Creating connections
    # TODO crear clase Connections y añadir funcion para crearlas similar a hubs
    # TODO añadir instancias de las conexiones a los hubs segun corresponda
    # Adding hub connections - bidirectional
    for conn in map_validators.get("conns").map_connects:
        origin, dest = conn.get("conn", "")
        hubs_dict.get(origin).neighbors[dest] = 1
        hubs_dict.get(dest).neighbors[origin] = 1


if __name__ == "__main__":

    if len(sys.argv) != 2:
        print(f"{Colors.RED.value}[ERROR] - Invalid number of arguments!"
              f"{Colors.RESET.value}")
    main(map=sys.argv[1])


