from typing import Dict, Tuple, Set
from src.conf.enums import Colors
from src.objs.a_star import AStar
from src.objs.dron import Dron
from src.objs.hub import Hub
from src.objs.connection import Connection
from icecream import ic

ic.configureOutput(contextAbsPath=True)


class Simulation:

    def __init__(self) -> None:
        self.connections_to_release: Set[Connection] = set()

    def set_simulation_drone_attr(
        self,
        drones: Dict[str, Dron],
        hubs: Dict[str, Hub]
            ) -> None:

        for drone in drones.values():
            drone.hub_index = 1
            drone.where.curr_drones += 1
            drone.waiting_turns = 0

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
            if can_use_connection:
                next_connection.curr_drones += 1
                drone.waiting_turns = 1
                to_print += f"{drone.id}-{drone.where.name}-" + \
                    f"{next_hub.name} (In connection)  "
                drone.where.curr_drones -= 1

        elif drone.waiting_turns == 1:  # Drone second turn
            if can_enter_next_hub:
                next_connection.curr_drones -= 1
                drone.where.curr_drones -= 1
                drone.where = next_hub
                drone.where.curr_drones += 1

                hub_color = drone.where.color.upper()
                color_code = Colors.__members__.get(
                    hub_color, Colors.WHITE
                    ).value
                to_print += f"{drone.id}-{color_code}" + \
                    f"{drone.where.name}{Colors.RESET.value}  "
                drone.waiting_turns = 0  # Restart turns
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
        if can_enter_next_hub and can_use_connection:
            next_connection.curr_drones += 1
            drone.where.curr_drones -= 1
            drone.where = next_hub
            drone.where.curr_drones += 1
            # Drone is using the connection so it is added to be unblocked at
            # the end of turn
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
                if not drone.path:
                    raise ValueError(
                        f"{Colors.RED.value}[ERROR] - "
                        f"The drone {drone.id} couldn't find a path "
                        f"to the goal{Colors.RESET.value}"
                    )

                if drone.in_goal:
                    continue

                # getting the next hub to move in
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

            # Freeing the connections comming from not restricted hubs
            # at the end of each turn
            for connection_to_release in self.connections_to_release:
                connection_to_release.curr_drones -= 1
            self.connections_to_release.clear()
            print(to_print)
            print()
            turns += 1
            # if turns > 150:
            #     break
