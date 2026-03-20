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

        #     if not drone.last_moved:
        #         drone.hub_index -= 1
        #     if drone.hub_index + 1 < len(drone.path):
        #         drone.hub_index += 1
        #         next_hub = drone.path[drone.hub_index]


        #     # TODO buscar la conexion correspondiente y chequear que hay capacidad
        #     for key, connection in connections.items():
        #         from_, to_ = key
        #         if drone.where.name == from_ and next_hub.name == to_:
        #             next_connection = connection
        #             break

        #     if next_hub.zone == "restricted" and drone.turns != 1 and next_connection.curr_drones <= next_connection.max_link_cap:
        #         drone.turns += 1
        #         drone.last_moved = False
        #         to_print += f"{drone.id}-{next_connection.father.name}-{next_connection.son.name}  "
        #         next_connection.curr_drones += 1
        #         continue

        #     if next_hub.is_crossable:
        #         drone.where.curr_drones -= 1
        #         drone.where = next_hub
        #         drone.where.curr_drones += 1

        #         hub_color = drone.where.color.upper()
        #         color_code = Colors.__members__.get(hub_color, Colors.WHITE).value

        #         # print(f"{drone.id}-"
        #         #     f"{color_code}{drone.where.name}"
        #         #     f"{Colors.RESET.value}")
        #         # print()
        #         to_print += f"{drone.id}-{color_code}{drone.where.name}{Colors.RESET.value}  "
        #         drone.last_moved = True
        #         drone.turns = 0
        #         if next_connection.curr_drones > 0:
        #             next_connection.curr_drones -= 1
        #     else:
        #         drone.last_moved = False

        #     if drone.where.name == goal_hub.name:
        #         drone.where.curr_drones = 0
        #         drone.in_goal = True

        # print(f"{to_print}")
        # print()
        # to_print = ""
        # turns += 1



            # Determinar el índice del próximo hub al que el dron intenta moverse en este turno.
            # Si el dron no se movió en el turno anterior, significa que estaba bloqueado o en un estado de varios turnos.
            # Debe intentar alcanzar el mismo 'next_hub' al que apuntaba.
            # Si se movió en el turno anterior, avanzó con éxito, por lo que debe avanzar al siguiente hub en su ruta.
            intended_next_hub_idx = drone.hub_index
            if drone.last_moved: # Solo avanza si se movió con éxito en el turno anterior
                intended_next_hub_idx += 1

            if intended_next_hub_idx >= len(drone.path):
                continue # El dron ha llegado al final de su ruta o ya está en el objetivo
            next_hub = drone.path[intended_next_hub_idx]

            # TODO buscar la conexion correspondiente y chequear que hay capacidad
            for key, connection in connections.items():
                from_, to_ = key
                if drone.where.name == from_ and next_hub.name == to_:
                    next_connection = connection
                    break
            ic(drone.id, next_connection.father.name, next_connection.son.name)

            if next_connection is None:
                ic(f"Error: No connection found between {drone.where.name} and {next_hub.name} for drone {drone.id}")
                drone.last_moved = False
                continue

            # Verificar si el próximo hub es transitable (tiene capacidad)
            can_enter_next_hub = next_hub.is_crossable
            # Verificar si la conexión tiene capacidad
            can_use_connection = next_connection.curr_drones < next_connection.max_link_cap

            if next_hub.zone == "restricted":
                if drone.turns == 0: # Primer turno intentando entrar en zona restringida
                    if can_enter_next_hub and can_use_connection:
                        next_connection.curr_drones += 1 # Ocupar la conexión
                        drone.turns = 1 # Marcar como inicio de travesía restringida
                        drone.last_moved = False # El dron no se mueve al next_hub todavía
                        to_print += f"{drone.id}-{drone.where.name}-{next_hub.name} (restricted start)  "
                        # drone.hub_index permanece igual, ya que aún no se ha movido
                    else:
                        drone.last_moved = False # Bloqueado por capacidad del hub o de la conexión
                elif drone.turns == 1: # Segundo turno en zona restringida, ahora se mueve
                    # En el segundo turno, la conexión ya está ocupada.
                    # Solo necesitamos verificar si el hub de destino sigue siendo transitable.
                    if can_enter_next_hub:
                        next_connection.curr_drones -= 1 # Liberar capacidad de la conexión

                        drone.where.curr_drones -= 1
                        drone.where = next_hub
                        drone.where.curr_drones += 1
                        drone.hub_index = intended_next_hub_idx # Actualizar el índice ahora que se movió

                        hub_color = drone.where.color.upper()
                        color_code = Colors.__members__.get(hub_color, Colors.WHITE).value
                        to_print += f"{drone.id}-{color_code}{drone.where.name}{Colors.RESET.value}  "
                        drone.last_moved = True
                        drone.turns = 0 # Reiniciar turnos
                    else:
                        drone.last_moved = False # Bloqueado por capacidad del hub de destino
                        # Si se bloquea aquí, la conexión permanece ocupada hasta que pueda moverse.
            else: # Zona normal o prioritaria (travesía de 1 turno)
                if can_enter_next_hub and can_use_connection:
                    # Ocupar la conexión (brevemente)
                    next_connection.curr_drones += 1

                    drone.where.curr_drones -= 1
                    drone.where = next_hub
                    drone.where.curr_drones += 1
                    drone.hub_index = intended_next_hub_idx # Actualizar el índice

                    # Liberar la conexión inmediatamente para travesías de 1 turno
                    next_connection.curr_drones -= 1

                    hub_color = drone.where.color.upper()
                    color_code = Colors.__members__.get(hub_color, Colors.WHITE).value
                    to_print += f"{drone.id}-{color_code}{drone.where.name}{Colors.RESET.value}  "
                    drone.last_moved = True
                    drone.turns = 0 # Reiniciar turnos
                else:
                    drone.last_moved = False # Bloqueado por capacidad del hub o de la conexión

            # if drone.where.name == goal_hub.name:
            #     drone.where.curr_drones = 0
            #     drone.in_goal = True
