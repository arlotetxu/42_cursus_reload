import random
from typing import Any, List, Optional
from src.config.enums import Walls
from src.model.cell import Cell
from src.model.maze import Maze


class UtilsMaze:
    """
    Utils_Maze class for managing and manipulating maze structures.

    A comprehensive maze utility class that handles maze validation,
    navigation, generation using different algorithms (DFS, Prim's),
    solving, and special features like watermarking and open area
    management.

    Attributes:
        maze (Maze): The maze object containing grid and dimension
        information.

    Methods:
        is_within_bounds(x, y) -> bool:
            Validates if coordinates are within maze boundaries.

        get_cell(x, y) -> Optional[Cell]:
            Retrieves a cell at given coordinates, returns None if out of
            bounds.

        get_directions() -> list[tuple[str, int, int]]:
            Returns cardinal directions (N, E, S, W) with their offset
            values.

        opposite_wall(wall) -> str:
            Returns the opposite wall direction for a given wall.

        get_neighbors(cell) -> List[tuple[Cell, str]]:
            Gets unvisited neighboring cells with their connecting walls.

        find_direction_by_wall(wall) -> tuple[str, int, int]:
            Finds direction tuple matching the given wall identifier.

        has_necessary_dimensions() -> bool:
            Checks if maze meets minimum dimensions (9x7).

        calculate_init_position() -> Optional[tuple[int, int]]:
            Calculates center position for watermark placement.

        watermark() -> bool:
            Marks cells in a "42" pattern at maze center, marks them as
            visited.

        check_valid_position(start, exit) -> bool:
            Validates that start and exit coordinates are valid and not on
            watermark.

        open_areas(max_passes) -> None:
            Prevents large open spaces by adding walls to 2x3 or 3x2 areas.

        perfect_maze(start, exit, is_perfect, algorithm) -> None:
            Generates a maze using DFS or Prim's algorithm, optionally
            adds cycles.

        find_cells_without_walls(cell) -> list[str]:
            Returns list of wall directions that are open for a cell.

        get_cells_solve_maze(start, exit) -> Optional[List[Cell]]:
            Solves maze using BFS, returns ordered list of cells from
            start to exit.

        path_to_directions(path) -> str:
            Converts cell path into directional string (N/S/E/W sequence).

        solve_maze(start, exit) -> str:
            Main solver method, returns directional string or empty if no
            solution.
    """

    def __init__(self, maze: Any) -> None:
        """
        Initialize the utilis maze object handler.

         Args:
            maze (Maze): Maze instance used for generation operations.

        Returns:
            None
        """
        self.maze: Maze = maze

    def is_within_bounds(self, x: int, y: int) -> bool:
        """
        Check if the given coordinates are within the maze boundaries.

        Args:
            x (int): The x-coordinate to check.
            y (int): The y-coordinate to check.

        Returns:
            bool: True if the coordinates (x, y) are within the maze bounds
                    (0 <= x < width and 0 <= y < height), False otherwise.
        """
        if 0 <= x < self.maze.width and 0 <= y < self.maze.height:
            return True
        return False

    def get_cell(self, x: int, y: int) -> Optional[Cell]:
        """
        Retrieve a cell from the maze grid at the specified coordinates.

        Args:
            x (int): The x-coordinate (column) of the cell.
            y (int): The y-coordinate (row) of the cell.

        Returns:
            Optional[Cell]: The Cell object at the specified coordinates
            if the coordinates
                            are within the maze bounds, otherwise None.
        """
        if self.is_within_bounds(x, y):
            return self.maze.grid_maze[y][x]
        return None

    @staticmethod
    def get_directions() -> list[tuple[str, int, int]]:
        """
        Generate a list of cardinal directions with their corresponding
        offsets.

        Returns:
            list[tuple[str, int, int]]: A list of tuples containing:
                - direction name (N, E, S, W as string values)
                - x-axis offset (column delta)
                - y-axis offset (row delta)
        """
        return [
            (Walls.N.value, 0, -1),
            (Walls.E.value, 1, 0),
            (Walls.S.value, 0, 1),
            (Walls.W.value, -1, 0),
        ]

    @staticmethod
    def opposite_wall(wall: str) -> str:
        """
        Return the opposite wall direction for a given wall.

        Args:
            wall (str): A wall direction string (N, S, E, or W).

        Returns:
            str: The opposite wall direction.
                    - N returns S (North returns South)
                    - S returns N (South returns North)
                    - E returns W (East returns West)
                    - W returns E (West returns East)

        Raises:
            KeyError: If wall is not a valid direction (N, S, E, W).
        """
        opposites = {
            Walls.N.value: Walls.S.value,
            Walls.S.value: Walls.N.value,
            Walls.E.value: Walls.W.value,
            Walls.W.value: Walls.E.value,
        }
        return opposites[wall]

    def get_neighbors(self, cell: Cell) -> List[tuple[Cell, str]]:
        """
        Retrieves unvisited neighboring cells of a given cell.

        Args:
            cell (Cell): The cell for which to find neighbors.

        Returns:
            List[tuple[Cell, str]]: A list of tuples containing unvisited
            neighbor cells
                and the wall direction connecting to them. Each tuple
                consists of:
                - Cell: The neighboring cell object
                - str: The wall identifier/direction string

        Example:
            neighbors = maze.get_neighbors(current_cell)
            for neighbor_cell, wall_direction in neighbors:
                # Process neighbor
        """
        directions: List[tuple[str, int, int]] = self.get_directions()
        neighbors: List[tuple[Cell, str]] = []
        for wall, dir_x, dir_y in directions:
            node_x = cell.x + dir_x
            node_y = cell.y + dir_y
            neighbor: Cell | None = self.get_cell(node_x, node_y)
            if neighbor and not neighbor.visited:
                neighbors.append((neighbor, wall))
        return neighbors

    def find_direction_by_wall(self, wall: str) -> tuple[str, int, int]:
        """
        Find the direction tuple associated with a given wall identifier.

        Args:
            wall (str): The wall identifier to search for (e.g., 'N', 'S',
            'E', 'W').

        Returns:
            tuple[str, int, int]: A tuple containing the wall identifier,
                                    x-offset (dx), and y-offset (dy) for the
                                    matching direction.

        Raises:
            StopIteration: If no direction with the given wall identifier
            is found.
        """
        return next(((w, dx, dy)
                     for w, dx, dy in self.get_directions()
                     if w == wall))

    def has_necessary_dimensions(self) -> bool:
        """
        Check if the maze has the minimum required dimensions.

        Returns:
            bool: True if the maze width is at least 9 and height is at
            least 7,
                    False otherwise.
        """
        return self.maze.width >= 9 and self.maze.height >= 7

    def calculate_init_position(self) -> Optional[tuple[int, int]]:
        """
        Calculate the initial position at the center of the maze.

        Computes the center coordinates of the maze by dividing its width
        and height by 2.
        If the dimensions are not integers, they are truncated to integers.

        Returns:
            Optional[tuple[int, int]]: A tuple of (x, y) coordinates
            representing the center position, or None if the maze does not
            have the necessary dimensions.
        """
        if not self.has_necessary_dimensions():
            return None
        x: float = self.maze.width / 2
        y: float = self.maze.height / 2

        x = x if x.is_integer() else int(x)
        y = y if y.is_integer() else int(y)

        return (int(x), int(y))

    def watermark(self) -> bool:
        """
        Mark cells in the maze to create a '42' watermark pattern.

        This method identifies and marks specific cells in the maze grid
        that form the visual representation of the numbers '4' and '2',
        creating a watermark.
        The watermark is positioned relative to the calculated initial
        position.

        Returns:
            bool: True if the watermark was successfully applied, False if
            the maze dimensions are insufficient to display the watermark.

        Note:
            - Requires the maze to have sufficient dimensions (checked via
                has_necessary_dimensions())
            - Marks cells by setting their `is_FORTY_TWO` and `visited`
            attributes
                to True
            - The watermark pattern is defined by two grids: one for the
            digit '4'
                and one for the digit '2'
        """
        if not self.has_necessary_dimensions():
            print("The maze dimensions are not sufficient to print"
                  "the watermark")
            return False
        # Identify position for number four
        grid_four: set[tuple[int, int]] = {
            (-3, -2),
            (-1, -2),
            (-3, -1),
            (-1, -1),
            (-3, 0),
            (-2, 0),
            (-1, 0),
            (-1, 1),
            (-1, 2),
        }
        # Identify position for number two
        grid_two: set[tuple[int, int]] = {
            (1, -2),
            (2, -2),
            (3, -2),
            (3, -1),
            (1, 0),
            (2, 0),
            (3, 0),
            (1, 1),
            (1, 2),
            (2, 2),
            (3, 2),
        }
        grid_all: set[tuple[int, int]] = grid_four | grid_two
        start_pos: tuple[int, int] | None = self.calculate_init_position()
        start_pos_x: int = 0
        start_pos_y: int = 0
        if start_pos:
            start_pos_x, start_pos_y = start_pos

        for row in self.maze.grid_maze:
            for cell in row:
                _x: int = cell.x - start_pos_x
                _y: int = cell.y - start_pos_y
                if (_x, _y) in grid_all:
                    cell.is_FORTY_TWO = True
                    cell.visited = True
        return True

    def check_valid_position(
        self, start: tuple[int, int], exit: tuple[int, int]
    ) -> bool:
        """
        Validate that the start and exit positions are valid for maze
        traversal.

        Checks that both start and exit coordinates exist within the maze
        and
        that neither position contains a cell marked with the '42' pattern.

        Args:
            start: A tuple of (row, col) coordinates for the maze start
            position.
            exit: A tuple of (row, col) coordinates for the maze exit
            position.

        Returns:
            bool: True if both positions are valid, False otherwise.

        Prints:
            - "The start or end coordinates are incorrect." if either
            coordinate
                is out of bounds or doesn't correspond to a valid cell.
            - "The coordinates cannot match the pattern '42'" if either
            position
                contains a cell marked with the '42' pattern.
        """
        result: bool = True
        _start: Cell | None = self.get_cell(*start)
        _end: Cell | None = self.get_cell(*exit)

        if not _start or not _end:
            print("The start or end coordinates are incorrect.")
            result = False
        if ((_start and _start.is_FORTY_TWO) or
           (_end and _end.is_FORTY_TWO)):
            print("The coordinates cannot match the pattern '42'")
            result = False
        return result

    def open_areas(self, max_passes: int = 10) -> None:
        """
        Reduce large open areas in the maze by strategically placing walls.
        This method iteratively scans the maze for rectangular open areas
        (2x3 or 3x2 cells with no internal walls) and subdivides them by
        adding walls with random gaps.
        The process continues for multiple passes until no more open areas
        are found or the maximum number of passes is reached.
        Args:
            max_passes (int, optional): Maximum number of iterations to
            scan and modify the maze. Defaults to 10. The method may
            terminate early if a complete pass finds no open areas to
            modify.
        Returns:
            None: Modifies the maze in-place by closing walls between
            cells.
        Note:
            - Operates on 2x3 (width x height) and 3x2 rectangular areas
            - Each identified open area gets one wall placement with a
            randomized gap
            - Process repeats until convergence or max_passes limit is
            reached
        """

        def is_open_between(wall: str, x: int, y: int) -> bool:
            """
            Check if there is an open passage between the current cell and
            an adjacent cell.
            Determines whether a wall between the cell at (x, y) and its
            neighbor in the
            direction specified by 'wall' is open (passable).
            Args:
                wall (str): The wall identifier indicating the direction
                to check
                            (e.g., 'north', 'south', 'east', 'west').
                x (int): The x-coordinate of the current cell.
                y (int): The y-coordinate of the current cell.
            Returns:
                bool: True if the passage between the current cell and the
                adjacent cell
                        is open (both walls are False), False otherwise.
                        Returns False if either cell does not exist or if
                        either wall is closed.
            """
            cell: Cell | None = self.get_cell(x, y)
            if cell and cell.walls[wall]:
                return False

            _, dx, dy = self.find_direction_by_wall(wall)
            next_x, next_y = x + dx, y + dy
            next_cell: Cell | None = self.get_cell(next_x, next_y)
            if next_cell:
                return next_cell.walls[self.opposite_wall(wall)] is False
            return False

        def close_between(wall: str, x: int, y: int) -> None:
            """
            Close the wall between two adjacent cells.

            Given a wall direction and coordinates, this function closes
            the wall
            on both sides - setting the wall as closed for the current
            cell and
            closing the opposite wall for the adjacent cell in the
            specified direction.

            Args:
                wall (str): The direction of the wall to close (e.g.,
                'north', 'south', 'east', 'west').
                x (int): The x-coordinate of the first cell.
                y (int): The y-coordinate of the first cell.
            """
            _, dx, dy = self.find_direction_by_wall(wall)
            next_x, next_y = x + dx, y + dy

            c1: Cell | None = self.get_cell(x, y)
            c2: Cell | None = self.get_cell(next_x, next_y)
            if c1:
                c1.walls[wall] = True
            if c2:
                c2.walls[self.opposite_wall(wall)] = True

        def is_open_2x3(x: int, y: int) -> bool:
            """
            Check if a 2x3 rectangular area is completely open (no walls
            blocking passage).
            Verifies that a region starting at coordinates (x, y) with
            width 2 and height 3
            has no internal walls. Checks all vertical walls between
            columns and all
            horizontal walls between rows within the specified region.
            Args:
                x (int): The x-coordinate of the top-left corner of the
                region.
                y (int): The y-coordinate of the top-left corner of the
                region.
            Returns:
                bool: True if the 2x3 region is completely open with no
                blocking walls, False if any walls are present or if the
                region extends beyond maze bounds.
            """
            if x + 1 >= self.maze.width or y + 2 >= self.maze.height:
                return False

            # Check vertical walls
            for cx in (x, x + 1):
                if not is_open_between(Walls.S.value, cx, y):
                    return False
                if not is_open_between(Walls.S.value, cx, y + 1):
                    return False

            # Check horizontal walls
            for cy in (y, y + 1, y + 2):
                if not is_open_between(Walls.E.value, x, cy):
                    return False

            return True

        def is_open_3x2(x: int, y: int) -> bool:
            """
            Check if a 3x2 rectangular area is open (traversable) in the
            maze.

            Verifies that all walls within a 3-column by 2-row region are
            open,
            allowing movement through the area. Checks:
            - East walls for columns x and x+1 across rows y and y+1
            - South walls for columns x, x+1, and x+2 at row y

            Args:
                x: The x-coordinate (column) of the top-left corner of the
                area.
                y: The y-coordinate (row) of the top-left corner of the
                area.

            Returns:
                True if all walls in the 3x2 area are open, False
                otherwise.
                Also returns False if the area extends beyond maze
                boundaries.
            """
            if x + 2 >= self.maze.width or y + 1 >= self.maze.height:
                return False

            # Check horizontal walls
            for cy in (y, y + 1):
                if not is_open_between(Walls.E.value, x, cy):
                    return False
                if not is_open_between(Walls.E.value, x + 1, cy):
                    return False

            # Check vertical walls
            for cx in (x, x + 1, x + 2):
                if not is_open_between(Walls.S.value, cx, y):
                    return False

            return True

        def build_wall_2x3(x: int, y: int) -> None:
            """
            Build a 2x3 wall structure with a random gap.
            Creates a vertical wall spanning 3 rows at the specified
            x-coordinate, with a randomly positioned gap in one of the
            three rows. The gap is created
            by skipping the wall closure for that row.
            Args:
                x (int): The x-coordinate where the wall structure will be
                built.
                y (int): The starting y-coordinate of the wall structure
                (covers y, y+1, y+2).
            Returns:
                None
            """
            gap_row = random.choice([y, y + 1, y + 2])
            for cy in (y, y + 1, y + 2):
                if cy == gap_row:
                    continue
                close_between(Walls.E.value, x, cy)

        def build_wall_3x2(x: int, y: int) -> None:
            """
            Build a horizontal wall of 3 cells with a random gap.

            Creates a wall segment spanning 3 columns (x, x+1, x+2) at row
            y, with a randomly selected column left open (no wall). This
            function is typically used in maze generation to create wall
            structures with controlled passages.

            Args:
                x (int): The starting x-coordinate (leftmost column) of
                the wall segment.
                y (int): The y-coordinate (row) where the wall will be
                built.

            Returns:
                None
            """
            gap_col = random.choice([x, x + 1, x + 2])
            for cx in (x, x + 1, x + 2):
                if cx == gap_col:
                    continue
                close_between(Walls.S.value, cx, y)

        """ Look for open areas of 2x3 or 3x2 cells to avoid large open
        spaces in the maze."""
        for _ in range(max_passes):
            changed: bool = False

            for y in range(self.maze.height):
                for x in range(self.maze.width):
                    if is_open_2x3(x, y):
                        build_wall_2x3(x, y)
                        changed = True

                    if is_open_3x2(x, y):
                        build_wall_3x2(x, y)
                        changed = True

            if not changed:
                break

    def find_cells_without_walls(self, cell: Cell) -> list[str]:
        """
        Find all directions of the cell that don't have walls.

        Args:
            cell: The Cell object to inspect for open directions.

        Returns:
            A list of direction strings (keys) from the cell's walls
            dictionary where the corresponding wall value is False (i.e.,
            no wall exists).

        Example:
            >>> cell = Cell()
            >>> cell.walls = {'north': True, 'south': False,
                'east': False, 'west': True}
            >>> find_cells_without_walls(cell)
            ['south', 'east']
        """

        return [l for (l, b) in cell.walls.items() if not b]
