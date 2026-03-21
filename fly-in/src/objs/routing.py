import sys
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
            # drone.last_moved = True
            drone.waiting_turns = 0


def start_simulation(
        drones: Dict[str, Dron],
        connections:Dict[Tuple [str, str], Hub],
        hubs: Dict[str, Hub]
        ) -> None:

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

            # check the next hub index
            intended_next_hub_idx = drone.hub_index + 1
            if intended_next_hub_idx >= len(drone.path):
                continue # Drone in goal or in the right position
            # getting the next hub to move in
            next_hub = drone.path[intended_next_hub_idx]

            # getting the next connection from current hub
            for key, connection in connections.items():
                from_, to_ = key
                if drone.where.name == from_ and next_hub.name == to_:
                    next_connection = connection
                    break

            if next_connection is None:
                raise ValueError(
                    f"Error: No connection found between {drone.where.name} and {next_hub.name} for drone {drone.id}")
                # continue

            # checking whether the next hub is crossable
            can_enter_next_hub = next_hub.is_crossable
            # checking whether next connection is crossable TODO crear metodo en connection similar a hub
            can_use_connection = int(next_connection.curr_drones) < int(next_connection.max_link_cap)

            if next_hub.zone == "restricted":
                if drone.waiting_turns == 0: # Drone first turn
                    # if can_enter_next_hub and can_use_connection:
                    if can_use_connection:
                        next_connection.curr_drones += 1
                        drone.waiting_turns = 1
                        to_print += f"{drone.id}-{drone.where.name}-{next_hub.name} (In connection)  "
                        drone.where.curr_drones -= 1
                        continue # TODO Añadido despues de buen funcionamiento

                elif drone.waiting_turns == 1: # Drone second turn
                    if can_enter_next_hub:
                        next_connection.curr_drones -= 1

                        drone.where.curr_drones -= 1
                        drone.where = next_hub
                        drone.where.curr_drones += 1
                        drone.hub_index = intended_next_hub_idx # Actualizar el índice ahora que se movió

                        hub_color = drone.where.color.upper()
                        color_code = Colors.__members__.get(hub_color, Colors.WHITE).value
                        to_print += f"{drone.id}-{color_code}{drone.where.name}{Colors.RESET.value}  "
                        drone.last_moved = True
                        drone.waiting_turns = 0 # Restart turns
            else:
                if can_enter_next_hub and can_use_connection:
                    next_connection.curr_drones += 1
                    drone.where.curr_drones -= 1
                    drone.where = next_hub
                    drone.where.curr_drones += 1
                    drone.hub_index = intended_next_hub_idx
                    next_connection.curr_drones -= 1

                    hub_color = drone.where.color.upper()
                    color_code = Colors.__members__.get(hub_color, Colors.WHITE).value
                    to_print += f"{drone.id}-{color_code}{drone.where.name}{Colors.RESET.value}  "
                    drone.waiting_turns = 0

            if drone.where.name == goal_hub.name:
                drone.where.curr_drones = 0
                drone.in_goal = True
        print(to_print)
        print()
        to_print=""
        turns += 1
