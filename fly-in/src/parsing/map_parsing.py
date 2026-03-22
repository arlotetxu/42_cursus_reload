import sys
from typing import List, Dict, Any
from pydantic import ValidationError
from src.conf.enums import Colors
from src.parsing.data_model import ConnexValidator, HubsValidator, \
    DroneValidator
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


def get_metadata(meta: str) -> Dict:
    meta_data_dict = {}
    for part in meta.split():
        if "=" in part:
            key, value = part.split("=", 1)
            meta_data_dict[key] = value
    return meta_data_dict


def get_hubs_data(map_lines: List[str]) -> List[Dict[str, Any]]:
    hubs_data: List[Dict[str, Any]] = []
    num_hubs = 0
    for line in map_lines:
        if "hub:" in line and not line.startswith("#"):
            hub_dict: Dict[str, Any] = {}
            hub_prefix = line.split(": ")[0]
            hub_data = line.split(": ")[1:]
            if hub_prefix == "start_hub":
                hub_dict["is_start"] = True
            if hub_prefix == "end_hub":
                hub_dict["is_goal"] = True
            for item in hub_data:
                # Adding metadata to the hub information dict
                start_meta = item.find('[')
                stop_meta = item.find(']')
                if start_meta != -1 and stop_meta != -1:
                    meta_data = item[start_meta + 1: stop_meta]
                    meta_data_dict = get_metadata(meta_data)
                    for k, v in meta_data_dict.items():
                        hub_dict[k] = v
                # Adding the rest hub information
                obj = item.strip().split()
                hub_dict["name"] = obj[0]
                hub_dict["x"] = int(obj[1])
                hub_dict["y"] = int(obj[2])
                num_hubs += 1
                hubs_data.append(hub_dict)
    if num_hubs < 2:
        print(f"{Colors.RED.value}[ERROR] - "
              f"There are not enought hubs in the map file. "
              f"Please, check it. {Colors.RESET.value}")
        sys.exit(1)
    return hubs_data


def get_conection_data(map_lines: List[str]) -> List[Dict[str, Any]]:
    connections: List[Dict[str, Any]] = []
    num_connections: int = 0
    for line in map_lines:
        if "connection: " in line and not line.startswith("#"):
            conn_data = line.split(": ")
            conn_dict: Dict[str, Any] = {}
            for item in conn_data[1:]:
                # Adding metadata to the hub information dict
                start_meta = item.find('[')
                stop_meta = item.find(']')
                if start_meta != -1 and stop_meta != -1:
                    meta_data = item[start_meta + 1: stop_meta]
                    conn_data_dict = get_metadata(meta_data)
                    for k, v in conn_data_dict.items():
                        conn_dict[k] = v
                conn_names = item.split('[')[0].strip()
                conn_tuple = tuple(
                    name.strip() for name in conn_names.split("-"))
                conn_dict["conn"] = conn_tuple
                num_connections += 1
            connections.append(conn_dict)
    if num_connections < 1:
        print(f"{Colors.RED.value}[ERROR] - "
              f"There are not rigth connection number in the map file. "
              f"Please, check it. {Colors.RESET.value}")
        sys.exit(1)
    return connections


def get_map_info(map_lines: List[str]) -> Dict[str, Any]:
    map_info: Dict[str, Any] = {}

    for line in map_lines:
        if line == '\n' or line.startswith("#"):
            continue
        if "nb_drones" in line:
            map_info["nb_drones"] = int(line.split(":")[1].strip())
        else:
            continue

    map_info["hubs"] = get_hubs_data(map_lines)
    map_info["connects"] = get_conection_data(map_lines)

    return map_info


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
    return map_data


def parse_map(map: str) -> Dict[str, Any]:
    return data_validation(map)
