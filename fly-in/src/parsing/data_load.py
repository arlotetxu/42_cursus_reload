import sys
from src.conf.enums import Colors
from typing import Dict, List, Any
from icecream import ic

ic.configureOutput(contextAbsPath=True)


def get_metadata(meta: str) -> Dict[str, int | str]:
    meta_data_dict: dict[str, int | str] = {}
    valid_values = ['zone', 'color', 'max_drones', 'max_link_capacity']
    for part in meta.split():
        if "=" in part:
            key, value = part.split("=", 1)
            if key not in valid_values or not value:
                raise ValueError(
                    f"{Colors.RED.value}[ERROR] - "
                    f"Invalid metadata ({part}). Please, check the"
                    f" map file and try again.\n"
                    f"{Colors.RESET.value}"
                )
            if key == "max_drones" or key == "max_link_capacity":
                try:
                    if int(value) <= 0:
                        raise ValueError
                except ValueError:
                    raise ValueError(
                        f"{Colors.RED.value}[ERROR] - "
                        f"Invalid metadata ({key}={value}). Please, check the"
                        f" map file and try again.\n"
                        f"{Colors.RESET.value}"
                    )
                meta_data_dict[key.strip()] = int(value)
            else:
                meta_data_dict[key.strip()] = value
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
                try:
                    hub_dict["x"] = int(obj[1])
                    hub_dict["y"] = int(obj[2])
                except ValueError:
                    raise ValueError(
                        f"{Colors.RED.value}[ERROR] - "
                        f"Coordinates must be integers. Please, check the"
                        f" map file and try again.\n"
                        f"{line}{Colors.RESET.value}"
                    )
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
    try:
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
    except Exception as e:
        raise ValueError(
            f"{Colors.RED.value}[ERROR] - in line {line}"
            f"{e}{Colors.RESET.value}"
        )
    if num_connections < 1:
        print(f"{Colors.RED.value}[ERROR] - "
              f"There are not right connection number in the map file. "
              f"Please, check it. {Colors.RESET.value}")
        sys.exit(1)
    return connections
