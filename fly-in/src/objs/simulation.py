from typing import Dict, Tuple
from src.conf.enums import Colors
from src.objs.a_star import AStar
from src.objs.dron import Dron
from src.objs.hub import Hub
from src.objs.connection import Connection
from icecream import ic

ic.configureOutput(contextAbsPath=True)


class Simulation:

    def set_simulation_drone_attr(
        self,
        drones: Dict[str, Dron],
        hubs: Dict[str, Hub]
            ) -> None:

        for drone in drones.values():
            drone.hub_index = 0
            drone.where.curr_drones += 1
            drone.waiting_turns = 0

    def get_drone_path(
        self,
        drones: Dict[str, Dron],
        hubs: Dict[str, Hub]
            ) -> None:

        my_astar = AStar(hubs)
        for drone in drones.values():
            drone.path = my_astar.init_a_star()

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
            if can_enter_next_hub:
                next_connection.curr_drones -= 1
                drone.where.curr_drones -= 1
                drone.where = next_hub
                drone.where.curr_drones += 1
                # drone.hub_index = intended_next_hub_idx
                drone.hub_index += 1

                hub_color = drone.where.color.upper()
                color_code = Colors.__members__.get(
                    hub_color, Colors.WHITE
                    ).value
                to_print += f"{drone.id}-{color_code}" + \
                    f"{drone.where.name}{Colors.RESET.value}  "
                # drone.last_moved = True
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
            # drone.hub_index = intended_next_hub_idx
            drone.hub_index += 1
            next_connection.curr_drones -= 1

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
        self.get_drone_path(drones, hubs)

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
                    continue  # Drone in goal or in the right position
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
                        f"[ERROR] - "
                        f"No connection found between {drone.where.name} "
                        f"and {next_hub.name} for drone {drone.id}")

                # checking whether the next hub is crossable
                # can_enter_next_hub = next_hub.is_crossable
                # checking whether next connection is crossable
                # can_use_connection = next_connection.is_crossable

                if next_hub.zone == "restricted":
                    # if drone.waiting_turns == 0: # Drone first turn
                    #     # if can_enter_next_hub and can_use_connection:
                    #     if can_use_connection:
                    #         next_connection.curr_drones += 1
                    #         drone.waiting_turns = 1
                    #         to_print += f"{drone.id}-{drone.where.name}-" + \
                    #             f"{next_hub.name} (In connection)  "
                    #         drone.where.curr_drones -= 1
                    #         continue
                    # # TODO Añadido despues de buen funcionamiento

                    # elif drone.waiting_turns == 1: # Drone second turn
                    #     if can_enter_next_hub:
                    #         next_connection.curr_drones -= 1

                    #         drone.where.curr_drones -= 1
                    #         drone.where = next_hub
                    #         drone.where.curr_drones += 1
                    #         drone.hub_index = intended_next_hub_idx

                    #         hub_color = drone.where.color.upper()
                    #         color_code = Colors.__members__.get(
                    #             hub_color, Colors.WHITE
                    #             ).value
                    #         to_print += f"{drone.id}-{color_code}" + \
                    #             f"{drone.where.name}{Colors.RESET.value}  "
                    #         drone.last_moved = True
                    #         drone.waiting_turns = 0 # Restart turns

                    to_print += self.in_restricted(
                        drone, next_connection, next_hub)
                else:
                    # if can_enter_next_hub and can_use_connection:
                    #     next_connection.curr_drones += 1
                    #     drone.where.curr_drones -= 1
                    #     drone.where = next_hub
                    #     drone.where.curr_drones += 1
                    #     drone.hub_index = intended_next_hub_idx
                    #     next_connection.curr_drones -= 1

                    #     hub_color = drone.where.color.upper()
                    #     color_code = Colors.__members__.get(
                    #         hub_color, Colors.WHITE
                    #         ).value
                    #     to_print += f"{drone.id}-{color_code}" + \
                    #         f"{drone.where.name}{Colors.RESET.value}  "
                    #     drone.waiting_turns = 0
                    to_print += self.not_in_restricted(
                        drone, next_connection, next_hub)

                if drone.where.name == goal_hub.name:
                    drone.where.curr_drones = 0
                    drone.in_goal = True
            print(to_print)
            print()
            to_print = ""
            turns += 1
