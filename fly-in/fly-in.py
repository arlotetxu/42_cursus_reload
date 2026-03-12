import sys
from typing import Dict, Any
from src.conf.enums import Colors
from src.parsing.map_parsing import parse_map
from icecream import ic

def main(map: str):
    print("Hello from main fly-in")
    map_data: Dict[str, Any] = parse_map(map)
    ic(map_data.get("hubs").map_hubs)



if __name__ == "__main__":

    if len(sys.argv) != 2:
        print(f"{Colors.RED.value}[ERROR] - Invalid number of arguments!"
              f"{Colors.RESET.value}")
    main(map=sys.argv[1])


