import sys
from typing import List, Dict, Any
from pydantic import ValidationError
from src.conf.enums import Colors
from src.parsing.data_model import ConnexValidator, HubsValidator, \
    DroneValidator
from src.parsing.data_load import get_hubs_data, get_conection_data
from icecream import ic

ic.configureOutput(contextAbsPath=True)


def read_map(map: str) -> List[str]:
    if map:
        try:
            with open(map, mode='r') as fd:
                lines = fd.readlines()
        except (FileNotFoundError, PermissionError, AttributeError) as e:
            print(f"{Colors.RED.value}{e}{Colors.RESET.value}")
            sys.exit(1)
    return lines


def get_map_info(map_lines: List[str]) -> Dict[str, Any]:
    map_info: Dict[str, Any] = {}

    for line in map_lines:
        if line == '\n' or line.startswith("#"):
            continue
        if "nb_drones" in line:
            try:
                map_info["nb_drones"] = int(line.split(":")[1].strip())
            except ValueError:
                raise ValueError(
                    f"{Colors.RED.value}[ERROR] - "
                    f"Drones must be integers. Please, check the"
                    f" map file and try again."
                    f"\n{line}{Colors.RESET.value}"
                )
        else:
            continue

    map_info["hubs"] = get_hubs_data(map_lines)
    map_info["connects"] = get_conection_data(map_lines)

    return map_info


def check_conn_hubs(map_data: Dict[str, Any]) -> None:
    hubs_data = map_data.get("hubs", "").map_hubs
    if not hubs_data:
        raise ValueError(
            f"{Colors.RED.value}[ERROR] - "
            f"Hubs information couldn't be retrieved"
            f"{Colors.RESET.value}"
        )
    hubs_name_list = []
    for hub in hubs_data:
        hub_name = hub.get("name", None)
        hubs_name_list.append(hub_name)

    conn_data = map_data.get("conns", "").map_connects
    if not conn_data:
        raise ValueError(
            f"{Colors.RED.value}[ERROR] - "
            f"Connections information couldn't be retrieved"
            f"{Colors.RESET.value}"
        )
    for item in conn_data:
        hub1, hub2 = item.get("conn", None)
        if hub1 not in hubs_name_list or hub2 not in hubs_name_list:
            raise ValueError(
                f"{Colors.RED.value}[ERROR] - "
                f"There are hubs ({hub1}-{hub2}) not defined in connections. "
                f"Please, check the map file and try again."
                f"{Colors.RESET.value}"
            )


def data_validation(map: str) -> Dict[str, Any]:
    map_data: Dict[str, Any] = {}
    map_lines = read_map(map)
    map_info = get_map_info(map_lines)
    try:
        connects_data = ConnexValidator(
            map_connects=map_info.get("connects", [])
            )
        map_data["conns"] = connects_data

        hubs_data = HubsValidator(map_hubs=map_info.get("hubs", {}))
        map_data["hubs"] = hubs_data

        drone_data = DroneValidator(map_drones=map_info.get("nb_drones", 0))
        map_data["drones"] = drone_data
    except ValidationError as e:
        for error in e.errors():
            print(error['msg'])
        sys.exit(1)
    except ValueError as e:
        print(e)
        sys.exit(1)
    check_conn_hubs(map_data)
    return map_data


def parse_map(map: str) -> Dict[str, Any]:

    return data_validation(map)
