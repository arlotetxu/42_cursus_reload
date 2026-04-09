import sys
from typing import List
from src.model.seed import Seed
from src.model.maze import Maze
from src.config.enums import Colors, PrintMode
from src.parser.config_model import ConfigModel
from src.parser.ft_parser_config import ft_parsing_config
from src.visual.print_minilib import MazePainter_mlx
from src.visual.print_ascii import MazePainter_ascii
from src.core.maze_generator import MazeGenerator
from src.core.solve_maze import SolveMaze
from src.core.seed_file import SeedFile


def export_maze_to_file(maze: Maze,
                        string_directions: str,
                        maze_config: ConfigModel) -> None:
    """
    Export a maze to a file with the given configuration.
    Args:
        maze (Maze): The maze object to export.
        string_directions (str): A string representing the directions for the
        maze path.
        maze_config (ConfigModel): Configuration model containing settings for
        maze export.
    Returns:
        None
    """
    my_maze_seed: List[List[str]] = SeedFile(maze).generate_seed()
    SeedFile(maze).export_seed(my_maze_seed, string_directions, maze_config)


def ft_make_maze() -> None:
    """
    Build, solve, and visualize a maze based on configuration parameters.
    Reads maze configuration from a file specified in command-line arguments,
    generates a perfect maze, solves it, exports the result to a file, and
    displays the maze using the specified visualization mode (ASCII or MLX).
    Raises:
        IndexError: If no config file path is provided in command-line
        arguments.
        FileNotFoundError: If the specified config file does not exist.
        ValueError: If the config file format is invalid.
    """
    try:
        config_file = sys.argv[1]
        maze_config: ConfigModel = ft_parsing_config(config_file)
        string_directions: str = ""
        if maze_config.maze_seed:
            seed = Seed(maze_config)
            seed.create_grid_from_seed()
        else:
            maze: Maze = Maze(maze_config)
            MazeGenerator(maze).perfect_maze(
                maze_config.maze_entry,
                maze_config.maze_exit,
                maze_config.maze_perfect
            )
            string_directions = SolveMaze(maze).solve_maze(
                maze_config.maze_entry,
                maze_config.maze_exit
            )
            export_maze_to_file(maze, string_directions, maze_config)
            if maze_config.maze_print_mode == PrintMode.ASCII.value:
                maze_painter_ascii = MazePainter_ascii(maze, maze_config)
                maze_painter_ascii.start_visual()
            elif maze_config.maze_print_mode == PrintMode.MLX.value:
                maze_painter_mlx = MazePainter_mlx(maze, maze_config)
                maze_painter_mlx.start_visual()

    except Exception as e:
        print(f"{Colors.RED.value}[ERROR]:{e}{Colors.RESET.value}")
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"{Colors.RED.value}[ERROR] config file not specified "
              f"in the arguments!!{Colors.RESET.value}")
        sys.exit(1)

    ft_make_maze()
