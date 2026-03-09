import sys
from typing import List, Dict
from src.conf.enums import Colors
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

def get_map_info(map_lines: List[str]) -> Dict[str: List | int]:
    map_info = {}
    hubs = []
    conections = []

    for line in map_lines:
        if line == '\n':
            continue
        if "nb_drones" in line:
            map_info["nb_drones"] = int(line.split(":")[1].strip())
        elif "hub:" in line:
            hub_data = line.split(": ")[1:]
            hub_dict = {}
            for item in hub_data:
                obj = item.split(" ")
                hub_dict["name"] = obj[0]
                hub_dict["x"] = int(obj[1])
                hub_dict["y"] = int(obj[2])
                if obj[3]:
                    hub_dict["meta"] = obj[3]
                hubs.append(hub_dict)
        elif "connection: " in line:
            con = line.split(": ")[1:]
            for item in con:
                con_2 = tuple(item.split("-"))
                conections.append(con_2)
        else:
            continue

    map_info["hubs"] = hubs
    map_info["connect"] = conections
    ic(map_info)
    return map_info

def parse_map(map: str) -> None:
    map_lines = read_map(map)
    map_info = get_map_info(map_lines)


