import sys
import random
from typing import Any
from pydantic import ValidationError
from src.config.enums import Colors, PrintMode
from src.parser.config_model import ConfigModel


def config_adapter(maze_config: dict[str, Any]) -> dict[str, Any]:
    """
    Adapt raw config keys to ConfigModel field names and coerce types.

    Args:
        maze_config (dict): Raw key/value pairs read from the config file.

    Returns:
        dict: The adapted dictionary ready for ConfigModel instantiation.

    Raises:
        SystemExit: Exits with code 1 if a value cannot be converted to the
        expected type, is of the wrong type, or a required key is missing
        during processing.
    """
    try:
        if "WIDTH" in maze_config:
            maze_config["maze_width"] = int(maze_config.get("WIDTH", 9))
            maze_config.pop("WIDTH")
        if "HEIGHT" in maze_config:
            maze_config["maze_height"] = int(maze_config.get("HEIGHT", 7))
            maze_config.pop("HEIGHT")
        if "ENTRY" in maze_config:
            maze_config["maze_entry"] = tuple(
                map(int, maze_config.get("ENTRY", (0, 0)).split(","))
            )
            maze_config.pop("ENTRY")
        if "EXIT" in maze_config:
            def_exit = (maze_config["maze_width"], maze_config["maze_height"])
            maze_config["maze_exit"] = tuple(
                map(int, maze_config.get("EXIT", def_exit).split(","))
            )
            maze_config.pop("EXIT")
        if "PERFECT" in maze_config:
            maze_config["maze_perfect"] = maze_config.get("PERFECT", True)
            maze_config.pop("PERFECT")
        if "OUTPUT_FILE" in maze_config:
            maze_config["maze_output"] = maze_config.get(
                "OUTPUT_FILE", "config.txt")
            maze_config.pop("OUTPUT_FILE")
        if "PRINT_MODE" in maze_config:
            maze_config["maze_print_mode"] = maze_config.get(
                "PRINT_MODE", PrintMode.MLX.value).upper()
            maze_config.pop("PRINT_MODE")
        if "SEED" in maze_config:
            maze_config["maze_seed"] = maze_config.get("SEED", "")
            maze_config.pop("SEED")
        if "maze_seed" not in maze_config:
            maze_config["maze_seed"] = ""
        if "SEED_CODE" in maze_config:
            if not maze_config.get("SEED_CODE"):
                maze_config["maze_seed_code"] = random.randint(1, 50000)
            else:
                maze_config["maze_seed_code"] = int(
                    maze_config.get("SEED_CODE", "")
                )
            maze_config.pop("SEED_CODE")
    except (ValueError, TypeError, KeyError) as v_e:
        print(
            f"{Colors.RED.value}[ERROR] Some entry of configuration file is "
            f"not correct. Please check it.{Colors.RESET.value}"
        )
        print(f"{Colors.RED.value}{v_e}{Colors.RESET.value}")
        sys.exit(1)

    return maze_config


def ft_parsing_config(config_file: str) -> ConfigModel:
    """
    Parse and validate a maze configuration file.

    Reads a configuration file in key=value format, transforms the keys to
    match the ConfigModel schema, and validates the data using Pydantic.

    Args:
        config_file (str): Path to the configuration file. Defaults to
        "config.txt"
                          if not provided or empty string.

    Returns:
        ConfigModel: A validated configuration model instance containing maze
        settings.

    Raises:
        SystemExit: Exits with code 1 if:
            - Configuration file cannot be found or read
            - Configuration values cannot be parsed to expected types
            - Parsed values fail Pydantic validation

    Configuration Keys Supported:
        - WIDTH: Integer maze width (default: 9)
        - HEIGHT: Integer maze height (default: 7)
        - ENTRY: Tuple of coordinates as "x,y" string (default: (0, 0))
        - EXIT: Tuple of coordinates as "x,y" string (default: (WIDTH, HEIGHT))
        - PERFECT: Boolean for perfect maze generation (default: True)
        - OUTPUT_FILE: Output file path (default: "config.txt")
        - PRINT_MODE: Rendering mode, converted to uppercase (default: MLX)

    Prints:
        Error messages with color formatting to stdout on failure.
    """

    # Opening config file and loading information in a dictionary
    if not config_file:
        config_file = "config.txt"
    maze_config: dict[str, Any] = {}
    try:
        with open(config_file, mode="r") as fd:
            lines = fd.readlines()
        for line in lines:
            if "=" in line:
                entry = line.split("=")
                maze_config[entry[0].strip()] = entry[1].strip()
    except (FileNotFoundError, AttributeError, PermissionError, IOError) as e:
        print(f"{Colors.RED.value}[ERROR] - {config_file}. "
              f"{e}{Colors.RESET.value}")
        sys.exit(1)

    maze_config = config_adapter(maze_config)

    # Data validation with pydantic in config_model.py
    try:
        maze_model = ConfigModel(**maze_config)
    except ValidationError as v_e:
        for error in v_e.errors():
            print(
                f"{Colors.RED.value}"
                f"{error.get('msg')} {error.get('loc', None)}"
                f"{Colors.RESET.value}"
            )
        sys.exit(1)
    return maze_model
