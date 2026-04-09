import random
import sys
from typing import List
from src.config.enums import MazeAlgorithm, Walls
from src.model.cell import Cell
from src.model.maze import Maze
from src.utils.utils_maze import UtilsMaze


class MazeGenerator:
    """Generate maze layouts using configurable algorithms.

    This class encapsulates the maze construction workflow and applies either
    DFS or Prim generation to a provided maze instance. It also supports
    optional non-perfect generation by opening extra walls after the base
    structure is created.

    Args:
        maze (Maze): Maze instance that will be modified in place.

    Returns:
        None
    """

    def __init__(self, maze: Maze) -> None:
        """Initialize the maze generator context.

        Args:
            maze (Maze): Maze instance used for generation operations.

        Returns:
            None
        """
        self.maze: Maze = maze
        self.util_mz: UtilsMaze = UtilsMaze(maze)

    def perfect_maze(self,
                     start: tuple[int, int],
                     exit: tuple[int, int],
                     is_perfect: bool = True,
                     algorithm: str = MazeAlgorithm.DFS.value,
                     ) -> None:
        """
        Generate a maze from a starting point to an exit point using the
        specified algorithm.

        This method creates either a perfect maze (no loops, all cells are
        connected) or a non-perfect maze (with additional wall openings)
        by employing depth-first search (DFS) or Prim's algorithm. The
        maze is initialized if not already done, and walls are removed
        based on the perfection setting.

        Args:
            start (tuple[int, int]): The (x, y) coordinates of the maze
            starting point.
            exit (tuple[int, int]): The (x, y) coordinates of the maze
            exit point.
            is_perfect (bool, optional): If True, generates a perfect maze
            with no loops.
                If False, removes approximately 15% of walls to create a
                non-perfect maze.
                Defaults to True.
            algorithm (str, optional): The maze generation algorithm to
            use.
                Options are Maze_Algorithm.DFS.value or Maze_Algorithm.
                PRIM.value.
                Defaults to Maze_Algorithm.DFS.value.

        Returns:
            None

        Raises:
            SystemExit: If the starting and exit positions are not valid.

        Side Effects:
            - Initializes the maze grid if not already initialized.
            - Marks the start and exit cells.
            - Sets the maze watermark.
            - Modifies cell walls based on the selected algorithm.
            - Opens additional areas in the maze.
        """
        if not self.maze.grid_maze:
            self.maze.initial_matrix()

        random.seed(self.maze.seed_code)

        def non_perfect_maze(walls_to_open: int = 20) -> None:
            """
            Creates a non-perfect maze by randomly removing walls between
            cells.
            A non-perfect maze contains loops and multiple paths to the
            destination, as opposed to a perfect maze which has exactly
            one path between any two points.
            This method randomly selects cells in the maze and opens walls
            between them
            and their neighbors, creating circular paths and alternative
            routes.
            Args:
                walls_to_open (int, optional): The number of walls to
                remove from the maze.
                    Defaults to 20.
            Returns:
                None
            Note:
                - Walls are only removed between valid cells within maze
                bounds.
                - Walls are not removed if either cell has the FORTY_TWO
                property set.
                - When a wall is removed between two cells, the opposite
                wall in the
                    neighbor cell is also removed to maintain consistency.
            """
            for _ in range(walls_to_open):
                x: int = random.randint(1, self.maze.width - 2)
                y: int = random.randint(1, self.maze.height - 2)
                cell: Cell | None = self.util_mz.get_cell(x, y)

                if cell and cell.walls:
                    w_rm: str = random.choice(list(cell.walls.keys()))

                    # Opening opposite wall of the neighbor
                    offset_x, offset_y = 0, 0
                    if w_rm == Walls.N.value:
                        offset_y = -1
                    elif w_rm == Walls.S.value:
                        offset_y = 1
                    elif w_rm == Walls.E.value:
                        offset_x = 1
                    elif w_rm == Walls.W.value:
                        offset_x = -1

                    neighbor: Cell | None = self.util_mz.get_cell(
                        x + offset_x, y + offset_y
                    )
                    if (neighbor
                       and not neighbor.is_FORTY_TWO
                       and not cell.is_FORTY_TWO):
                        cell.walls[w_rm] = False
                        w: str = self.util_mz.opposite_wall(w_rm)
                        neighbor.walls[w] = False

        def dfs(cell: Cell) -> None:
            """
            Perform depth-first search to generate maze using recursive
            backtracking.
            Marks the given cell as visited and recursively visits
            unvisited neighbors,
            removing walls between connected cells. Neighbors are shuffled
            to create randomized maze paths. Walls are only removed for
            cells that are not marked as FORTY_TWO (special cells that may
            have fixed walls).
            Args:
                cell (Cell): The current cell to process in the maze
                generation algorithm.
            Returns:
                None
            """
            cell.visited = True

            # shuffle the neighbors
            neighbors: List[tuple[Cell, str]] = (self.util_mz
                                                 .get_neighbors(cell))
            random.shuffle(neighbors)

            for next_cell, wall in neighbors:
                if not next_cell.visited:
                    if not cell.is_FORTY_TWO:
                        # break the wall
                        cell.walls[wall] = False
                        if not next_cell.is_FORTY_TWO:
                            op_w: str = self.util_mz.opposite_wall(wall)
                            next_cell.walls[op_w] = False

                    # recursive call
                    dfs(next_cell)

        def prim(cell: Cell) -> None:
            """
            Generate a maze using Prim's algorithm starting from the given
            cell.

            This iterative implementation of Prim's algorithm marks cells
            as visited and creates passages by removing walls between the
            current cell and unvisited neighboring cells. It uses a
            frontier list to randomly select the next cell
            to visit, ensuring a randomized maze generation.

            Args:
                cell (Cell): The starting cell from which to begin maze
                generation.

            Returns:
                None

            Note:
                - Modifies the visited state and walls of cells in the maze
                - Skips cells that are already visited or marked as
                FORTY_TWO
                - Uses random selection of frontier cells for varied maze
                patterns
            """
            cell.visited = True

            frontier: List[tuple[Cell, Cell, str]] = []
            for neigh, wall in self.util_mz.get_neighbors(cell):
                frontier.append((neigh, cell, wall))

            while frontier:
                idx: int = random.randrange(len(frontier))
                candidate, origin, wall = frontier.pop(idx)

                if candidate.visited or candidate.is_FORTY_TWO:
                    continue

                candidate.visited = True
                origin.walls[wall] = False
                candidate.walls[self.util_mz.opposite_wall(wall)] = False

                for neigh, wall in self.util_mz.get_neighbors(candidate):
                    if not neigh.visited:
                        frontier.append((neigh, candidate, wall))

        starting_cell_maze: Cell | None = self.util_mz.get_cell(*start)
        if starting_cell_maze:
            starting_cell_maze.is_start = True

        exit_cell_maze: Cell | None = self.util_mz.get_cell(*exit)
        if exit_cell_maze:
            exit_cell_maze.is_exit = True
        if starting_cell_maze:
            self.util_mz.watermark()
            if not self.util_mz.check_valid_position(start, exit):
                sys.exit(1)
            if algorithm == MazeAlgorithm.DFS.value:
                dfs(starting_cell_maze)
            else:
                prim(starting_cell_maze)

        if not is_perfect:
            # removing a 20% walls according to width * height
            walls_to_remove: int = int(self.maze.width *
                                       self.maze.height * 0.2)
            non_perfect_maze(walls_to_remove)
        self.util_mz.open_areas()
