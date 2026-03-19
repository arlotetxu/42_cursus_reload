from src.conf.enums import Colors
from src.objs.a_star import AStar
from icecream import ic

def get_drone_path(drones, hubs) -> None:
    my_astar = AStar(hubs)
    for drone in drones.values():
            drone.path = my_astar.init_a_star()
            drone.hub_index = -1

def start_simulation(drones, connections, hubs) -> None:

    # my_astar = AStar(hubs)
    goal_hub = next((hub for hub in hubs.values() if hub.is_goal), None)

    # for drone in drones.values():
    #         drone.path = my_astar.init_a_star()
    #         drone.hub_index = -1
    get_drone_path(drones, hubs)

    turns = 0
    while not all(drone.in_goal for drone in drones.values()):

        for drone in drones.values():
            if drone.in_goal:
                continue

            if drone.hub_index + 1 < len(drone.path):
                drone.hub_index += 1
                next_hub = drone.path[drone.hub_index]
                # TODO buscar la conexion correspondiente y chequear que hay capacidad
                # next_conection = ??

            if next_hub.is_crossable :
                drone.where = next_hub

            hub_color = drone.where.color.upper()
            color_code = Colors.__members__.get(hub_color, Colors.WHITE).value
            print(f"TURN: {turns}")
            print(f"{drone.id} - "
                  f"{color_code}{drone.where.name}"
                  f"{Colors.RESET.value}")
            print()

            # for r in drone.path:
            #     ic(r.name)

            if drone.where.name == goal_hub.name:
                drone.in_goal = True


        turns += 1