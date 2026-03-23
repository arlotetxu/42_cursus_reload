from typing import Dict, Tuple
from src.conf.enums import Colors
from src.objs.a_star import AStar
from src.objs.dron import Dron
from src.objs.hub import Hub
from src.objs.connection import Connection
from icecream import ic

ic.configureOutput(contextAbsPath=True)


class Simulation:

    def __init__(self):
        self.connections_to_release = set()

    def set_simulation_drone_attr(
        self,
        drones: Dict[str, Dron],
        hubs: Dict[str, Hub]
            ) -> None:

        for drone in drones.values():
            drone.hub_index = 1
            drone.where.curr_drones += 1
            drone.waiting_turns = 0

    # def get_drone_path(
    #     self,
    #     drones: Dict[str, Dron],
    #     hubs: Dict[str, Hub],
    #         ) -> None:

    #     my_astar = AStar(hubs)
    #     for drone in drones.values():
    #         drone.path = my_astar.init_a_star()

    def in_restricted(
        self,
        drone: Dron,
        next_connection: Connection,
        next_hub: Hub
            ) -> str:

        to_print = ""
        # checking whether the next hub is crossable
        can_enter_next_hub = next_hub.is_crossable
        # checking whether next connection is crossable
        can_use_connection = next_connection.is_crossable
        if drone.waiting_turns == 0:  # Drone first turn
            # if can_enter_next_hub and can_use_connection:
            if can_use_connection:
                next_connection.curr_drones += 1
                drone.waiting_turns = 1
                to_print += f"{drone.id}-{drone.where.name}-" + \
                    f"{next_hub.name} (In connection)  "
                drone.where.curr_drones -= 1

        elif drone.waiting_turns == 1:  # Drone second turn
            # if can_enter_next_hub and can_use_connection:
            if can_enter_next_hub:
                next_connection.curr_drones -= 1
                drone.where.curr_drones -= 1
                drone.where = next_hub
                drone.where.curr_drones += 1
                # drone.hub_index = intended_next_hub_idx
                # drone.hub_index += 1

                hub_color = drone.where.color.upper()
                color_code = Colors.__members__.get(
                    hub_color, Colors.WHITE
                    ).value
                to_print += f"{drone.id}-{color_code}" + \
                    f"{drone.where.name}{Colors.RESET.value}  "
                drone.waiting_turns = 0  # Restart turns
                # self.connections_to_release.add(next_connection)
        return to_print

    def not_in_restricted(
        self,
        drone: Dron,
        next_connection: Connection,
        next_hub: Hub
            ) -> str:

        to_print = ""
        # checking whether the next hub is crossable
        can_enter_next_hub = next_hub.is_crossable
        # checking whether next connection is crossable
        can_use_connection = next_connection.is_crossable
        # ic("not restricted")
        # ic(can_enter_next_hub, can_use_connection)
        if can_enter_next_hub and can_use_connection:
            next_connection.curr_drones += 1
            drone.where.curr_drones -= 1
            drone.where = next_hub
            drone.where.curr_drones += 1
            # drone.hub_index += 1
            # El dron ha pasado por la conexión, la marcamos para liberarla al final del turno
            self.connections_to_release.add(next_connection)

            hub_color = drone.where.color.upper()
            color_code = Colors.__members__.get(
                hub_color, Colors.WHITE
                ).value
            to_print += f"{drone.id}-{color_code}" + \
                f"{drone.where.name}{Colors.RESET.value}  "
            drone.waiting_turns = 0
        return to_print

    def start_simulation(
        self,
        drones: Dict[str, Dron],
        connections: Dict[Tuple[str, str], Connection],
        hubs: Dict[str, Hub]
            ) -> None:

        goal_hub = next((hub for hub in hubs.values() if hub.is_goal), None)
        if not goal_hub:
            raise ValueError(
                f"{Colors.RED.value}[ERROR] - "
                f"Goal hub couldn't be found. Please, check the map file."
                f"{Colors.RESET.value}"
            )
        self.set_simulation_drone_attr(drones, hubs)
        turns = 1
        my_astar = AStar(hubs)

        while not all(drone.in_goal for drone in drones.values()):

            print(f"TURN: {turns}")
            to_print = ""
            for drone in drones.values():
                next_connection = None
                next_hub = None
                drone.path = my_astar.init_a_star(drone.where)

                if drone.in_goal:
                    continue

                #getting the next hub to move in
                # drone.hub_index += 1
                # if drone.hub_index >= len(drone.path):
                #     continue
                next_hub = drone.path[drone.hub_index]

                # getting the next connection from current hub
                for key, connection in connections.items():
                    from_, to_ = key
                    if drone.where.name == from_ and next_hub.name == to_:
                        next_connection = connection
                        break

                if next_connection is None:
                    raise ValueError(
                        f"[ERROR] - "
                        f"No connection found between {drone.where.name} "
                        f"and {next_hub.name} for drone {drone.id}")

                if next_hub.zone == "restricted":
                    to_print += self.in_restricted(
                        drone, next_connection, next_hub)
                else:
                    to_print += self.not_in_restricted(
                        drone, next_connection, next_hub)

                if drone.where.name == goal_hub.name:
                    drone.where.curr_drones = 0
                    drone.in_goal = True

            # Al final del turno, liberamos las conexiones que fueron usadas por movimientos no restringidos
            # Esto asegura que las conexiones se mantengan ocupadas durante todo el turno, respetando max_link_cap.
            for connection_to_release in self.connections_to_release:
                connection_to_release.curr_drones -= 1
            self.connections_to_release.clear() # Limpiamos el conjunto para el siguiente turno

            print(to_print)
            print()
            turns += 1
            # if turns > 150:
            #     break
