import sys
from typing import Optional, Any, List
from src.parser.config_model import ConfigModel
from src.model.cell import Cell
from src.config.enums import Walls, Colors


class Seed:
    """
    Seed

    A class responsible for loading, validating, and reconstructing a maze
    from a seed file. It parses hexadecimal wall encodings and metadata
    (dimensions, entry, exit, and solution path) to build a grid of Cell
    objects for visualization.

    Attributes:
        maze_config (ConfigModel): Configuration model containing the path
            to the seed file and other global settings.
        seed_config (dict): Dictionary storing metadata extracted from the
            seed file, such as width, height, entry/exit points, and the
            solution string.
        grid_seed (list[list[Cell]]): 2D grid of Cell objects reconstructed
            from the seed data.

    Methods:
        get_cell(x, y) -> Optional[Cell]:
            Retrieves a cell at the specified coordinates from the seed grid.
        get_seed_info() -> None:
            Reads the seed file, extracts hex maze data and metadata, and
            initializes the grid structure.
        create_grid_from_seed() -> None:
            Populates the grid with wall states, start/exit markers, and
            triggers the ASCII visualization.
        get_solution_coord() -> set[tuple]:
            Converts the solution direction string into a set of coordinates.
        validate_solution() -> bool:
            Ensures the hexadecimal wall encodings are consistent between
            adjacent cells.
    """

    def __init__(self, maze_config: ConfigModel) -> None:
        """
        Initialize the Seed object.

        Args:
            maze_config (ConfigModel): The configuration model containing
                global settings, including the path to the maze seed file.
        Returns:
            None
        """
        self.maze_config = maze_config
        self.seed_config: dict[str, Any] = {}
        self.grid_seed: list[list[Cell]] = []

    def get_cell(self, x: int, y: int) -> Optional[Cell]:
        """
        Retrieve a specific cell from the reconstructed seed grid.

        Args:
            x (int): The horizontal coordinate (column) of the cell.
            y (int): The vertical coordinate (row) of the cell.

        Returns:
            Optional[Cell]: The Cell object if coordinates are within bounds,
            else None.
        """
        height = int(self.seed_config.get("seed_height", 0))
        width = int(self.seed_config.get("seed_width", 0))
        if 0 <= y < height and 0 <= x < width:
            return self.grid_seed[y][x]
        return None

    def get_seed_info(self) -> None:
        """
        Read and parse the maze seed file to extract grid data and metadata.

        This method performs the following steps:
        1. Validates the seed file's wall consistency.
        2. Reads the hexadecimal maze structure.
        3. Extracts metadata including the entry point, exit point, and
            solution path.
        4. Initializes the `grid_seed` with empty Cell objects based on the
           parsed dimensions.

        Returns:
            None

        Side Effects:
            Exits the program if the seed file is invalid, missing metadata,
                or unreadable.
        """
        if not self.maze_config.maze_seed:
            return None
        self.seed_config = {}
        hex_seed: list[str] = []
        try:
            if not self.validate_solution():
                print(f"{Colors.RED.value}[ERROR] The seed file is not valid. "
                      f"Please, check it!{Colors.RESET.value}")
                sys.exit(1)
            with open(self.maze_config.maze_seed, mode='r') as fd:
                for line in fd:
                    if line.strip() == "":
                        break
                    hex_seed.append(line.rstrip("\n"))
                self.seed_config["hex_seed"] = hex_seed
                lines = [line.rstrip("\n") for line in fd.readlines()]
                if len(lines) < 3:
                    print(f"{Colors.RED.value}[ERROR] The seed file is "
                          f"missing required metadata (entry, exit, "
                          f"solution).{Colors.RESET.value}")
                    return
                self.seed_config["solution"] = lines[-1]
                self.seed_config["entry"] = tuple(lines[-3].split(","))
                self.seed_config["exit"] = tuple(lines[-2].split(","))
        except (FileNotFoundError, PermissionError, AttributeError) as e:
            print(f"{Colors.RED.value} The seed file cannot be read. "
                  f"Please, check it!...")
            print(f"{e}{Colors.RESET.value}")
            return

        if not hex_seed:
            print(f"{Colors.RED.value}[ERROR] The seed file contains no "
                  f"maze data.{Colors.RESET.value}")
            return

        self.seed_config["seed_width"] = len(hex_seed[0])
        self.seed_config["seed_height"] = len(hex_seed)
        self.grid_seed = [
            [Cell(x, y) for x in range(self.seed_config.get("seed_width", 0))]
            for y in range(self.seed_config.get("seed_height", 0))
        ]

    def create_grid_from_seed(self) -> None:
        """
        Reconstruct the maze grid from the parsed seed data and trigger
        visualization.

        This method performs the following operations:
        1. Calls `get_seed_info()` to parse the seed file.
        2. Validates and sets the entry and exit flags on the corresponding
           Cell objects.
        3. Iterates through the hexadecimal wall data to configure the wall
           states for every cell in the grid.
        4. Identifies "FORTY_TWO" pattern cells (cells with all walls closed).
        5. Initializes and starts the ASCII-based visualization.

        Side Effects:
            Exits the program if coordinates are out of bounds or if the
            hexadecimal data is malformed.
        """

        self.get_seed_info()

        # Guard: if get_seed_info() did not build a grid, exit early
        if not self.grid_seed:
            print(f"{Colors.RED.value}[ERROR] Seed grid could not be "
                  f"initialised. Aborting.{Colors.RESET.value}")
            sys.exit(1)

        seed_width = int(self.seed_config.get("seed_width", 0))
        seed_height = int(self.seed_config.get("seed_height", 0))

        # Adding entry and exit values to the corresponding cells
        entry = self.seed_config.get("entry")
        if entry:
            try:
                start_x, start_y = int(entry[0]), int(entry[1])
            except (ValueError, IndexError):
                print(f"{Colors.RED.value}[ERROR] Seed file has malformed "
                      f"entry coordinates: {entry}.{Colors.RESET.value}")
                sys.exit(1)
            if 0 <= start_x < seed_width and 0 <= start_y < seed_height:
                self.grid_seed[start_y][start_x].is_start = True
            else:
                print(f"{Colors.RED.value}[ERROR] Entry coordinates "
                      f"({start_x},{start_y}) are out of bounds for seed "
                      f"dimensions {seed_width}x{seed_height}."
                      f"{Colors.RESET.value}")
                sys.exit(1)

        exit_data = self.seed_config.get("exit")
        if exit_data:
            try:
                exit_x, exit_y = int(exit_data[0]), int(exit_data[1])
            except (ValueError, IndexError):
                print(f"{Colors.RED.value}[ERROR] Seed file has malformed "
                      f"exit coordinates: {exit_data}.{Colors.RESET.value}")
                sys.exit(1)
            if 0 <= exit_x < seed_width and 0 <= exit_y < seed_height:
                self.grid_seed[exit_y][exit_x].is_exit = True
            else:
                print(f"{Colors.RED.value}[ERROR] Exit coordinates "
                      f"({exit_x},{exit_y}) are out of bounds for seed "
                      f"dimensions {seed_width}x{seed_height}."
                      f"{Colors.RESET.value}")
                sys.exit(1)

        # Opening the cell walls according to its hex value
        for y, line in enumerate(self.seed_config.get("hex_seed", [])):
            if len(line) != seed_width:
                print(f"{Colors.RED.value}[ERROR] Seed row {y} has length "
                      f"{len(line)}, expected {seed_width}."
                      f"{Colors.RESET.value}")
                sys.exit(1)
            for x, cell in enumerate(line):
                try:
                    cell_bin = bin(int(cell, base=16)).split("b")[-1]
                except ValueError:
                    print(f"{Colors.RED.value}[ERROR] Invalid hex character "
                          f"'{cell}' at row {y}, col {x} in seed file."
                          f"{Colors.RESET.value}")
                    sys.exit(1)
                if len(cell_bin) < 4:
                    cell_bin = "0" * (4 - len(cell_bin)) + cell_bin
                maze_cell = self.grid_seed[y][x]
                if int(cell_bin[-1]) != 1:
                    maze_cell.walls[Walls.N.value] = False
                if int(cell_bin[-2]) != 1:
                    maze_cell.walls[Walls.E.value] = False
                if int(cell_bin[-3]) != 1:
                    maze_cell.walls[Walls.S.value] = False
                if int(cell_bin[-4]) != 1:
                    maze_cell.walls[Walls.W.value] = False
                if all(maze_cell.walls.values()):
                    maze_cell.is_FORTY_TWO = True

        from src.visual.print_seed_ascii import SeedPainter_ascii
        seed_ascii_painter = SeedPainter_ascii(self, self.seed_config)
        seed_ascii_painter.start_visual()

    def get_solution_coord(self) -> set[tuple[int, int]]:
        """
        Generate a set of coordinates representing the solution path through
        the maze.

        Retrieves the solution string from the seed metadata and converts
        directional characters (N, S, E, W) into coordinate tuples. Starting
        from the maze entry point, each direction character is translated
        into an offset that updates the current position. The entry and exit
        coordinates are excluded from the final result.

        Returns:
            set[tuple]: A set of (x, y) coordinate tuples representing the
            maze solution path, excluding the starting and ending positions.
            Returns an empty set if entry metadata is missing or malformed.

        Raises:
            SystemExit: If an invalid character (not N, S, E, or W) is found
            in the solution string.
        """
        solution_str = self.seed_config.get("solution", "")
        entry = self.seed_config.get("entry")

        if not entry or len(entry) < 2:
            return set()

        coord: List[tuple[int, int]] = []
        try:
            coord.append((int(entry[0]), int(entry[1])))
        except (ValueError, IndexError):
            return set()

        if solution_str:
            for c in solution_str:
                offset_y = 0
                offset_x = 0
                if c == "N":
                    offset_y = -1
                elif c == "S":
                    offset_y = 1
                elif c == "E":
                    offset_x = 1
                elif c == "W":
                    offset_x = -1
                else:
                    print(f"{Colors.RED.value}[ERROR] - character {c} found "
                          f"in solution path. {Colors.RESET.value}")
                    sys.exit(1)

                last_coord_x, last_coord_y = coord[-1]
                new_coord = (
                    last_coord_x + offset_x, last_coord_y + offset_y
                    )
                coord.append(new_coord)
            if coord:
                del coord[-1]
            if coord:
                del coord[0]

        coord_set: set[tuple[int, int]] = set(coord)
        return coord_set

    def validate_solution(self) -> bool:
        """Validates the maze solution by checking the consistency of wall
        encodings.

        Reads a maze seed file where each cell is encoded as a hexadecimal
        value
        representing wall configurations. Verifies that adjacent cells have
        consistent wall states (i.e., if one cell has a wall facing another,
        that adjacent cell must have a corresponding wall facing back).

        The hexadecimal encoding uses bits for walls in each direction:
            - Bit 0: North wall
            - Bit 1: East wall
            - Bit 2: South wall
            - Bit 3: West wall

        Returns:
            bool: True if the maze seed file is valid and all wall encodings
                  are consistent between adjacent cells. False if the file
                  cannot be read or a validation error occurs.

        Raises:
            ValueError: If inconsistent wall encoding is detected between
                adjacent cells.
                The error message includes the coordinates (c, r) of the
                problematic cell.

        Side Effects:
            Prints error messages to stdout if the seed file cannot be read
            (FileNotFoundError, PermissionError, AttributeError).
        """
        g = []
        is_valid: bool = False
        try:
            with open(self.maze_config.maze_seed, mode='r') as file:
                for line in file:
                    if line.strip() == '':
                        break
                    g.append([int(c, 16) for c in line.strip(' \t\n\r')])

                for r in range(len(g)):
                    for c in range(len(g[0])):
                        v = g[r][c]
                        if not all([(r < 1 or v & 1 == (g[r-1][c] >> 2) & 1),
                                    (c >= len(g[0])-1 or (v >> 1)
                                     & 1 == (g[r][c+1] >> 3) & 1),
                                    (r >= len(g)-1 or (v >> 2)
                                     & 1 == g[r+1][c] & 1),
                                    (c < 1 or (v >> 3) & 1 == (g[r][c-1] >> 1)
                                     & 1)]):
                            raise ValueError(f'Wrong encoding for ({c},{r})')
                is_valid = True
        except (FileNotFoundError, PermissionError, AttributeError) as e:
            print(f"{Colors.RED.value} The seed file cannot be read. "
                  f"Please, check it!...")
            print(f"{e}{Colors.RESET.value}")
            sys.exit(1)
        except ValueError as ve:
            print(f"{Colors.RED.value}[ERROR] The seed file is not valid. "
                  f"Please, check it!{Colors.RESET.value}")
            print(f"{Colors.RED.value} Validation error: "
                  f"{ve}{Colors.RESET.value}")
            sys.exit(1)
        return is_valid
