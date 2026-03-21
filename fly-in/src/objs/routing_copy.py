from typing import Dict, Tuple
from src.conf.enums import Colors
from src.objs.a_star import AStar
from src.objs.dron import Dron
from src.objs.hub import Hub
from icecream import ic

def get_drone_path(drones, hubs) -> None:
    my_astar = AStar(hubs)
    for drone in drones.values():
            drone.path = my_astar.init_a_star()
            drone.hub_index = 0
            drone.where.curr_drones += 1
            drone.last_moved = True
            drone.turns = 0


def start_simulation(
        drones: Dict[str, Dron],
        connections:Dict[Tuple [str, str], Hub],
        hubs: Dict[str, Hub]
        ) -> None:

    # my_astar = AStar(hubs)
    goal_hub = next((hub for hub in hubs.values() if hub.is_goal), None)
    get_drone_path(drones, hubs)

    turns = 1
    to_print = ""

    while not all(drone.in_goal for drone in drones.values()):
        print(f"TURN: {turns}")
        for drone in drones.values():
            next_connection = None
            next_hub = None

            if drone.in_goal:
                continue

            if not drone.last_moved:
                drone.hub_index -= 1
            if drone.hub_index + 1 < len(drone.path):
                drone.hub_index += 1
                next_hub = drone.path[drone.hub_index]


            # TODO buscar la conexion correspondiente y chequear que hay capacidad
            # for key, connection in connections.items():
            #     from_, to_ = key
            #     if drone.where.name == from_ and next_hub.name == to_:
            #         next_connection = connection
            #         break

            # if next_hub.zone == "restricted" and drone.turns != 1 and next_connection.curr_drones <= next_connection.max_link_cap:
            #     drone.turns += 1
            #     drone.last_moved = False
            #     to_print += f"{drone.id}-{next_connection.father.name}-{next_connection.son.name}  "
            #     next_connection.curr_drones += 1
            #     continue

            if next_hub.is_crossable:
                drone.where.curr_drones -= 1
                drone.where = next_hub
                drone.where.curr_drones += 1

                hub_color = drone.where.color.upper()
                color_code = Colors.__members__.get(hub_color, Colors.WHITE).value

                # print(f"{drone.id}-"
                #     f"{color_code}{drone.where.name}"
                #     f"{Colors.RESET.value}")
                # print()
                to_print += f"{drone.id}-{color_code}{drone.where.name}{Colors.RESET.value}  "
                drone.last_moved = True
                drone.turns = 0
                # if next_connection.curr_drones > 0:
                #     next_connection.curr_drones -= 1
            else:
                drone.last_moved = False

            if drone.where.name == goal_hub.name:
                drone.where.curr_drones = 0
                drone.in_goal = True

        print(f"{to_print}")
        print()
        to_print = ""
        turns += 1