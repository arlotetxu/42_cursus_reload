import sys
from typing import List, Dict
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

def get_map_info(map_lines: List[str]) -> Dict[str: List | int]:
    map_info = {}
    hubs = []
    conections = []

    for line in map_lines:
        if line == '\n' or line.startswith("#"):
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
    map_info["connects"] = conections
    # ic(map_info)
    return map_info

def data_validation(map: str) -> Dict[str,Any]:
    map_data = {}
    map_lines = read_map(map)
    map_info = get_map_info(map_lines)
    try:
        connects_data = ConnexValidator(map_connects=map_info.get("connects", []))
        map_data["conn"] = connects_data
        hubs_data = HubsValidator(map_hubs=map_info.get("hubs", {}))
        map_data["hubs"] = hubs_data
        drone_data = DroneValidator(map_drones=map_info.get("nb_drones", 0))
    except ValueError as e:
        print(f"{Colors.RED.value}[ERROR '{e.errors()[0].get("loc", "")[0]}']"
              f" {e.errors()[0].get("msg", "")}"
              f"{Colors.RESET.value}")
        print()

        # print(f"{Colors.RED.value}[ERROR in {e.errors().get("loc", "")}] -"
        #         f"{e.errors().get("msg", "")}{Colors.RESET.value}")
        sys.exit(1)
    return map_data


def parse_map(map: str) -> None:
    map_data = data_validation(map)
