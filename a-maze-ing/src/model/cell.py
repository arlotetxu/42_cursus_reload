from src.config.enums import Walls


class Cell:
    """
    A cell representation for a maze grid.

    Attributes:
        x (int): The x-coordinate of the cell in the maze grid.
        y (int): The y-coordinate of the cell in the maze grid.
        visited (bool): Flag indicating whether this cell has been visited
        during maze generation.
        is_FORTY_TWO (bool): Flag indicating whether this cell is a special
        '42' marker cell.
        is_exit (bool): Flag indicating whether this cell is the exit point of
        the maze.
        is_start (bool): Flag indicating whether this cell is the starting
        point of the maze.
        walls (dict): A dictionary mapping wall directions (N, S, E, W) to
        boolean values, where True indicates the wall exists and False
        indicates it has been removed.
    """
    def __init__(self, x: int, y: int) -> None:
        """
        Initialize a Cell object representing a single cell in a maze.

        Args:
            x (int): The x-coordinate of the cell in the maze grid.
            y (int): The y-coordinate of the cell in the maze grid.

        Attributes:
            x (int): The x-coordinate of the cell.
            y (int): The y-coordinate of the cell.
            visited (bool): Flag indicating whether the cell has been visited
            during maze generation. Defaults to False.

            is_FORTY_TWO (bool): Flag indicating whether the cell is a special
            "42" cell. Defaults to False.

            is_exit (bool): Flag indicating whether the cell is the exit point
            of the maze. Defaults to False.

            is_start (bool): Flag indicating whether the cell is the starting
            point of the maze. Defaults to False.
            walls (dict): Dictionary tracking the state of walls in four
            directions (North, South, East, West).
            Each wall is initially set to True (wall exists). Keys are wall
            direction values, values are boolean states.
        """
        self.x: int = x
        self.y: int = y
        self.visited: bool = False
        self.is_FORTY_TWO: bool = False
        self.is_exit: bool = False
        self.is_start: bool = False
        self.walls: dict[str, bool] = {
            Walls.N.value: True,
            Walls.S.value: True,
            Walls.E.value: True,
            Walls.W.value: True,
                      }
