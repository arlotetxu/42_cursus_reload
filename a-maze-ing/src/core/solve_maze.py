from typing import List, Optional
from src.config.enums import Colors, Walls
from src.model.cell import Cell
from src.model.maze import Maze
from src.utils.utils_maze import UtilsMaze


class SolveMaze:
    """Solve maze paths using breadth-first search (BFS).

    This class provides pathfinding utilities for a maze instance and
    converts computed paths into directional strings that can be exported or
    rendered by visualization modules.

    Args:
        maze (Maze): Maze instance used to compute and cache solutions.

    Returns:
        None
    """

    def __init__(self, maze: Maze) -> None:
        """
        Initialize the solve maze object handler.

         Args:
            maze (Maze): Maze instance used for generation operations.

        Returns:
            None
        """
        self.maze: Maze = maze
        self.util_mz: UtilsMaze = UtilsMaze(maze)

    def get_cells_solve_maze(self,
                             start: Cell,
                             exit: Cell) -> Optional[List[Cell]]:
        """
        Solve the maze using breadth-first search (BFS) algorithm.
        Finds a path from the start cell to the exit cell by exploring the
        maze and tracking parent cells to reconstruct the solution path.
        Args:
            start (Cell): The starting cell for the maze solution.
            exit (Cell): The target/exit cell to reach.
        Returns:
            Optional[List[Cell]]: A list of cells representing the path
            from start to exit,
                                    or None if no path exists.
        Note:
            - Resets the visited state of all cells (except FORTY_TWO
            cells) before solving.
            - Uses BFS to guarantee the shortest path in an unweighted
            maze.
            - Only traverses through cells that have no walls between them.
        """
        # reset visited
        for row in self.maze.grid_maze:
            for col in row:
                if not col.is_FORTY_TWO:
                    col.visited = False

        list_cells: List[Cell] = [start]
        i: int = 0
        start.visited = True

        parent: dict[Cell, Cell] = {}

        while i < len(list_cells):
            cell = list_cells[i]
            i += 1

            if cell is exit:
                path: list[Cell] = [cell]
                while cell in parent:
                    cell = parent[cell]
                    path.append(cell)
                path.reverse()
                return path

            cell_wall: list[str] = self.util_mz.find_cells_without_walls(cell)
            for cw in cell_wall:
                _, x, y = self.util_mz.find_direction_by_wall(cw)
                next_x, next_y = cell.x + x, cell.y + y
                next_cell: Cell | None = self.util_mz.get_cell(next_x, next_y)

                if (
                    next_cell
                    and (not next_cell.visited)
                    and (not next_cell.is_FORTY_TWO)
                ):
                    next_cell.visited = True
                    parent[next_cell] = cell
                    list_cells.append(next_cell)

        return None

    def path_to_directions(self, path: List[Cell]) -> str:
        """
        Convert a list of cells representing a path into a string of
        directional characters.
        Each movement from one cell to the next is translated into a
        cardinal direction
        character (N, S, E, W) based on the coordinate differences.
        Args:
            path: A list of Cell objects representing consecutive
            positions in a path.
        Returns:
            A string of direction characters where:
            - 'N' represents movement up (dy = -1)
            - 'S' represents movement down (dy = 1)
            - 'E' represents movement right (dx = 1)
            - 'W' represents movement left (dx = -1)
            Returns an empty string if the path contains fewer than 2
            cells.
        Example:
            >>> path = [Cell(0, 0), Cell(0, 1), Cell(1, 1)]
            >>> path_to_directions(path)
            'SE'
        """

        if len(path) < 2:
            return ""

        directions_str: str = ""

        for i in range(len(path) - 1):
            current_cell: Cell = path[i]
            next_cell: Cell = path[i + 1]

            dx: int = next_cell.x - current_cell.x
            dy: int = next_cell.y - current_cell.y

            if dy == -1:  # Move up
                directions_str += Walls.N.value
            elif dy == 1:  # Move down
                directions_str += Walls.S.value
            elif dx == 1:  # Move right
                directions_str += Walls.E.value
            elif dx == -1:  # Move left
                directions_str += Walls.W.value

        return directions_str

    def solve_maze(self,
                   start: tuple[int, int],
                   exit: tuple[int, int],
                   reg_solve: bool = True) -> str:
        """
        Finds a path through the maze from start to exit and returns
        directions.
        Args:
            start: A tuple of (row, col) coordinates for the maze start
            position.
            exit: A tuple of (row, col) coordinates for the maze exit
            position.
        Returns:
            A string containing directional commands representing the path
            from start to exit.
            Returns an empty string if no path is found or if start/exit
            positions are invalid.
        Raises:
            None. Prints an error message to console if no path exists
            between start and exit.
        """
        string_directions: str = ""
        if ((not self.maze.solve_maze_seed and
            len(self.maze.solve_maze_seed) == 0)
           or reg_solve):
            _start: Cell | None = self.util_mz.get_cell(*start)
            _end: Cell | None = self.util_mz.get_cell(*exit)
            if _start is not None and _end is not None:
                list_solve = self.get_cells_solve_maze(_start, _end)
                if list_solve is not None:
                    string_directions = (self.
                                         path_to_directions(list_solve))
                else:
                    print(
                        f"{Colors.RED.value}"
                        "No path found from start to exit."
                        f"{Colors.RESET.value}"
                    )
        else:
            string_directions = self.maze.solve_maze_seed

        return string_directions
