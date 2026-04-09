import sys
from typing import List
from pathlib import Path
from src.config.enums import Colors
from src.model.maze import Maze
from src.parser.config_model import ConfigModel


class SeedFile:
    """Handle maze seed serialization and export operations.

    This class converts maze wall data to hexadecimal seed rows and writes
    them to disk with entry, exit, and solution metadata so the maze can be
    reproduced later.

    Args:
        maze (Maze): Maze instance used as the source for seed generation.

    Returns:
        None
    """

    def __init__(self, maze: Maze) -> None:
        """
        Initialize the seed file object handler.

         Args:
            maze (Maze): Maze instance used for generation operations.

        Returns:
            None
        """
        self.maze: Maze = maze

    def generate_seed(self) -> List[List[str]]:
        """
        Generate a maze seed by encoding wall configurations of each cell.

        Converts the maze grid into a 2D list where each cell is represented
        as a hexadecimal
        digit encoding its wall states. Each wall direction is mapped to a bit:
        - North (N): 1
        - East (E): 2
        - South (S): 4
        - West (W): 8

        Returns:
            list[list]: A 2D list of hexadecimal strings representing the maze
            seed, where each element corresponds to a cell's wall
            configuration.
        """
        maze_seed: List[list[str]] = []
        i: int = 0
        for row in self.maze.grid_maze:
            maze_seed.append([])
            for cell in row:
                cell_walls: int = 0
                if cell.walls.get("N"):
                    cell_walls += 1
                if cell.walls.get("E"):
                    cell_walls += 2
                if cell.walls.get("S"):
                    cell_walls += 4
                if cell.walls.get("W"):
                    cell_walls += 8
                # Saving in Hexadecimal format
                maze_seed[i].append(f"{cell_walls:X}")
            i += 1
        return maze_seed

    def export_seed(
        self,
        maze_seed: List[List[str]],
        solve_directions: str,
        maze_config: ConfigModel,
    ) -> None:
        """
        Export maze data to a file.

        This method writes the maze structure, entry point, exit point, and
        solution directions to a file specified in the maze configuration.

        Args:
            maze_seed (list[list]): A 2D list representing the maze structure
            where each inner list represents a row of the maze.
            solve_directions (str): A string containing the directions to
            solve the maze (e.g., "SWSES" for South, West, South, East,
            South).
            maze_config (ConfigModel): Configuration object containing maze
            output file path and entry/exit coordinates.

        Returns:
            None

        Raises:
            IOError: If the output file cannot be written.
            ValueError: If maze_config.maze_output path is invalid.
        """
        # .resolve() converts relative paths to absolute paths avoiding ./..
        base_dir = Path("./output").resolve()
        file_path = Path(base_dir / maze_config.maze_output).resolve()

        try:
            if not file_path.is_relative_to(base_dir):
                raise PermissionError("Not authorized access!")
            # Creating the output folder if it does not exist:
            file_path.parent.mkdir(parents=True, exist_ok=True)
            with open(file_path, mode="w") as fd:
                for row in maze_seed:
                    fd.writelines(row)
                    fd.write("\n")
                fd.write("\n")
                x, y = maze_config.maze_entry
                fd.write(f"{x},{y}\n")
                x, y = maze_config.maze_exit
                fd.write(f"{x},{y}\n")
                fd.write(f"{solve_directions}")
        except (
                FileNotFoundError,
                AttributeError,
                PermissionError) as e:
            print(f"{Colors.RED.value}[ERROR] - {maze_config.maze_output}. "
                  f"{e}{Colors.RESET.value}")
            sys.exit(1)
