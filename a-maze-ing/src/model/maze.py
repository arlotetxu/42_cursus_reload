from typing import List
from src.model.cell import Cell
from src.parser.config_model import ConfigModel


class Maze:
    """
    Maze class for generating and solving maze puzzles.

    This class provides functionality to create, manipulate, and solve mazes
    using various algorithms. It includes features for maze generation, wall
    management, pathfinding, and maze validation.

    Attributes:
        width (int): The width of the maze in cells.
        height (int): The height of the maze in cells.
        grid_maze (List[List[Cell]]): 2D grid representing the maze structure.

    Methods:
        initial_matrix() -> List[List[Cell]]:
            Initializes the maze grid with Cell objects.

    """

    def __init__(self, maze_config: ConfigModel) -> None:
        """
        Initialize a Maze object.

        Args:
            maze_config (ConfigModel): The validated configuration model
            containing maze settings (dimensions, entry/exit points, etc.).

        Attributes:
            width (int): The width of the maze grid.
            height (int): The height of the maze grid.
            grid_maze (List[List[Cell]]): A 2D list representing the maze
            grid, where each element is a Cell object.
            build (Built_Maze): An instance of the Built_Maze helper class for
            maze construction operations.
        """
        self.width: int = maze_config.maze_width
        self.height: int = maze_config.maze_height
        self.grid_maze: List[List[Cell]] = []
        self.solve_maze_seed: str = ""
        self.seed_code = maze_config.maze_seed_code

    def initial_matrix(self) -> List[List[Cell]]:
        """
        Initialize and create the maze grid matrix.

        Creates a 2D grid of Cell objects with dimensions based on the maze's
        width and height. Each cell is instantiated with its corresponding
        (x, y) coordinates.

        Returns:
            List[List[Cell]]: A 2D list representing the maze grid, where each
                             element is a Cell object positioned at coordinates
                             (x, y) within the specified width and height
                             bounds.
        """
        self.grid_maze = [
            [Cell(x, y) for x in range(self.width)] for y in range(self.height)
        ]
        return self.grid_maze
