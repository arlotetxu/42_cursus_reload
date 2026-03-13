import sys
from typing import List, Dict, Any
from pydantic import ValidationError
from src.conf.enums import Colors
from src.parsing.data_model import ConnexValidator, HubsValidator, \
    DroneValidator
from icecream import ic

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
    meta_data = meta.split(" ")
    for meta in meta_data:
        meta_key_value = meta.split("=")
        meta_data_dict[meta_key_value[0]] = meta_key_value[1]
    return meta_data_dict


def get_hubs_data(map_lines: List[str]) -> List[str, str | int]:
    hubs_data = []
    for line in map_lines:
        if "hub:" in line:
            hub_data = line.split(": ")[1:]
            hub_dict = {}
            for item in hub_data:
                # Adding metadata to the hub information dict
                start_meta = item.find('[')
                stop_meta = item.find(']')
                if start_meta != -1 and stop_meta != -1:
                    meta_data = item[start_meta + 1 : stop_meta]
                    meta_data_dict = get_metadata(meta_data)
                    for k, v in meta_data_dict.items():
                        hub_dict[k] = v
                # Adding the rest hub information
                obj = item.split(" ")
                hub_dict["name"] = obj[0]
                hub_dict["x"] = int(obj[1])
                hub_dict["y"] = int(obj[2])
                hubs_data.append(hub_dict)
    return hubs_data


def get_conection_data(map_lines: List[str]) -> List:
    connections = []
    for line in map_lines:
        if "connection: " in line:
                conn_data = line.split(": ")
                conn_dict = {}
                for item in conn_data[1:]:
                    # Adding metadata to the hub information dict
                    start_meta = item.find('[')
                    stop_meta = item.find(']')
                    if start_meta != -1 and stop_meta != -1:
                        meta_data = item[start_meta + 1 : stop_meta]
                        conn_data_dict = get_metadata(meta_data)
                        for k, v in conn_data_dict.items():
                            conn_dict[k] = v
                    stop = conn_data[1].find(" ")
                    conn_tuple = tuple(conn_data[1][:stop].split("-"))
                    conn_dict["conn"] = conn_tuple
                connections.append(conn_dict)
    return connections


def get_map_info(map_lines: List[str]) -> Dict[str: List | int]:
    map_info = {}

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

def data_validation(map: str) -> Dict[str,Any]:
    map_data = {}
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


def parse_map(map: str) -> None:
    return data_validation(map)
