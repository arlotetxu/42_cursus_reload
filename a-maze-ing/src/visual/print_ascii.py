import random
import sys
import os
import time
from typing import List
from random import choice
from src.model.maze import Maze
from src.model.cell import Cell
from src.config.enums import Colors, Walls, MazeAlgorithm
from src.parser.config_model import ConfigModel
from src.utils.utils_maze import UtilsMaze
from src.core.solve_maze import SolveMaze
from src.core.maze_generator import MazeGenerator
from src.core.seed_file import SeedFile


class MazePainter_ascii:
    """
    MazePainter_ascii

    A class responsible for rendering and displaying ASCII art representations
    of mazes.
    Provides functionality to visualize maze structures, solutions, and
    interactive parameter control through a command-line interface.

    Attributes:
        maze (Maze): The maze object containing the maze structure and build
        operations.
        maze_config (ConfigModel): Configuration model containing maze
        parameters (dimensions, entry/exit points, algorithm type, etc.).
        maze_color (str): ANSI color code for maze walls and borders.
        pattern_color (str): ANSI color code for the 42 pattern cells.
        show_solution (bool): Flag to toggle visualization of the solution
        path.

    Methods:
        get_solution_coord() -> set[tuple]:
            Solves the maze and returns a set of (x, y) coordinates
            representing
            the path from entry to exit point. Parses directional characters
            (N/S/E/W)
            from the solution string and computes absolute positions.

        print_maze_ascii() -> None:
            Renders the maze as ASCII art using box-drawing characters.
            Displays
            maze walls, cells, solution path (if enabled), start point, and
            exit point
            with appropriate color coding.

        clear_screen() -> None:
            Clears the terminal/console screen. Handles both Windows (cls) and
            Unix-based systems (clear).

        put_parameters() -> None:
            Displays an interactive menu allowing users to:
            - Regenerate mazes
            - Toggle solution visualization
            - Rotate maze and pattern colors
            - Change maze generation algorithms
            - Exit the application

        start_visual() -> None:
            Main entry point that initializes the visual display by computing
            solution coordinates, clearing the screen, rendering the maze,
            and activating the interactive parameter menu.
    """
    def __init__(self, maze: Maze, maze_config: ConfigModel) -> None:
        """
        Initialize the ASCII maze printer.

        Args:
            maze (Maze): The maze object to be printed.
            maze_config (ConfigModel): Configuration model for maze settings.

        Attributes:
            maze (Maze): The maze object to be printed.
            maze_config (ConfigModel): Configuration model for maze settings.
            maze_color (str): Color for maze elements (default: WHITE).
            pattern_color (str): Color for pattern elements (default: WHITE).
            show_solution (bool): Flag to display the maze solution (default:
            False).
        """
        self.maze: Maze = maze
        self.maze_config: ConfigModel = maze_config
        self.maze_color = Colors.WHITE.value
        self.pattern_color = Colors.WHITE.value
        self.show_solution: bool = False
        self.util_mz: UtilsMaze = UtilsMaze(maze)
        self.solve: SolveMaze = SolveMaze(maze)

    def get_solution_coord(self) -> set[tuple[int, int]]:
        """
        Generate a set of coordinates representing the solution path through
        the maze.

        Retrieves the solution string from the maze solver and converts
        directional characters (N, S, E, W) into coordinate tuples. Starting
        from the maze entry point, each direction character is translated into
        an offset that updates
        the current position. The entry and exit coordinates are excluded from
        the final result.

        Returns:
            set[tuple]: A set of (x, y) coordinate tuples representing the
            maze solution path, excluding the starting and ending positions.

        Raises:
            SystemExit: If an invalid character (not N, S, E, or W) is found
            in the solution string.
        """
        solution_str: str = self.solve.solve_maze(
                self.maze_config.maze_entry,
                self.maze_config.maze_exit)

        start_x, start_y = self.maze_config.maze_entry

        coord: List[tuple[int, int]] = []
        if start_x is not None and start_y is not None:
            coord.append((start_x, start_y))

        if solution_str and solution_str is not None:
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
                new_coord = (last_coord_x + offset_x, last_coord_y + offset_y)
                coord.append(new_coord)
            if coord[-1]:
                del coord[-1]
            if coord[0]:
                del coord[0]

        coord_set: set[tuple[int, int]] = set(coord)
        return coord_set

    def print_maze_ascii(self) -> None:
        """
        Print a visual ASCII representation of the maze to the console.

        Renders the maze using box-drawing characters with the following
        features:
        - Displays the maze grid with walls represented by lines
        - Highlights the solution path in blue (if show_solution is enabled)
        - Marks the start cell in cyan and exit cell in yellow
        - Uses pattern color to fill cells marked as FORTY_TWO
        - Applies maze color to all structural elements (walls and borders)

        The output includes:
        - Top border with corner and junction characters
        - Cell content rows with vertical wall separators
        - Horizontal wall lines between rows
        - Bottom border completing the maze frame

        Returns:
            None
        """
        w, h = self.maze_config.maze_width, self.maze_config.maze_height
        solution: set[tuple[int, int]] = self.get_solution_coord()
        maze_color: str = self.maze_color
        pattern_color: str = self.pattern_color

        # Top line
        sup: str = "┌" + "───┬" * (w - 1) + "───┐"
        print(f"{maze_color}{sup} {Colors.RESET.value}")

        for y in range(h):
            # Cell lines (content + vertical walls)
            line: str = "│"
            for x in range(w):
                cell: Cell | None = self.util_mz.get_cell(x, y)
                if cell and not cell.is_FORTY_TWO:
                    content: str = "   "
                    if self.show_solution:
                        if (x, y) in solution:
                            content = f"{Colors.BLUE.value} ፨ "\
                                    f"{Colors.RESET.value}"
                    if cell.is_start:
                        content = f"{Colors.GREEN.value}░░░\033[0m"
                    elif cell.is_exit:
                        content = f"{Colors.RED.value}░░░\033[0m"

                    line += content
                    line += f"{maze_color}│{Colors.RESET.value}" \
                            if cell.walls[Walls.E.value] else " "
                elif cell and cell.is_FORTY_TWO:
                    line += f"{pattern_color}███{maze_color}│"\
                            f"{Colors.RESET.value}"
            print(f"{maze_color}{line} {Colors.RESET.value}")

            # Bottom line
            if y < h - 1:
                line = "├"
                for x in range(w):
                    cell = self.util_mz.get_cell(x, y)
                    if cell:
                        line += "───" if cell.walls["S"] else "   "
                        line += "┼" if x < w - 1 else "┤"
                print(f"{maze_color}{line} {Colors.RESET.value}")
            else:
                # Bottom border
                last = "└" + "───┴" * (w - 1) + "───┘"
                print(f"{maze_color}{last} {Colors.RESET.value}")

    def clear_screen(self) -> None:
        """
        Clear the terminal screen.

        Clears the console output by calling the appropriate system command
        based on the operating system:
        - 'cls' for Windows
        - 'clear' for macOS and Linux

        Returns:
            None
        """
        # For Windows
        if os.name == 'nt':
            os.system('cls')
        # For macOS and Linux
        else:
            os.system('clear')

    def get_display_colors(self) -> List[Colors]:
        """
        Return the list of colors used for maze rendering.

        Excludes ANSI control values such as RESET and BOLD so color changes
        are always visible in the terminal.

        Returns:
            List[Colors]: Available colors for maze and pattern rendering.
        """
        return [
            Colors.RED,
            Colors.GREEN,
            Colors.YELLOW,
            Colors.BLUE,
            Colors.MAGENTA,
            Colors.CYAN,
            Colors.WHITE,
        ]

    def render_visual(self) -> None:
        """
        Render the current maze state without reopening the menu.

        Returns:
            None
        """
        self.get_solution_coord()
        self.clear_screen()
        self.print_maze_ascii()
        self.util_mz.watermark()

    def draw_maze_by_op(self, maze_color: str,
                        pattern_color: str,
                        algorithm: str = MazeAlgorithm.DFS.value) -> None:
        """
        Generate and display a maze using the specified algorithm and colors.
        This method initializes a maze, generates it using the provided
        algorithm, solves it, exports the seed and solution, and renders the
        visual representation with the specified color scheme.
        Args:
            maze_color: The color to use for rendering the maze walls.
            pattern_color: The color to use for rendering the maze pattern
                or path.
            algorithm: The maze generation algorithm to use. Defaults to DFS
                algorithm.
        Returns:
            None
        """

        self.maze.initial_matrix()
        self.maze.seed_code = random.randint(1, 50000)
        MazeGenerator(self.maze).perfect_maze(
                self.maze_config.maze_entry,
                self.maze_config.maze_exit,
                self.maze_config.maze_perfect,
                algorithm)
        seed = SeedFile(self.maze).generate_seed()
        solution = self.solve.solve_maze(
                self.maze_config.maze_entry,
                self.maze_config.maze_exit,
                True
                )
        SeedFile(self.maze).export_seed(
                seed,
                solution,
                self.maze_config
                )
        self.show_solution = False
        self.maze_color = maze_color
        self.pattern_color = pattern_color
        self.render_visual()

    def animate_colored_mazes(self, delay: float = 0.005) -> None:
        """
        Generate and render several mazes with different colors.

        Args:
            delay (float): Seconds to wait between each rendered maze.

        Returns:
            None
        """
        colors = self.get_display_colors()

        for maze_color in colors:
            pattern_choices = [color for color in colors
                               if color != maze_color]
            pattern_color = choice(pattern_choices)
            self.draw_maze_by_op(maze_color.value, pattern_color.value)
            time.sleep(max(delay, 0.5))

    def print_menu(self) -> None:
        """
        Print the interactive menu.

        Returns:
            None
        """
        print("\n" * 3)
        print("=== A-Maze_Ing ===")
        print("1. Re-generate new maze with DFS Algorithm")
        print("2. Show/Hide path from entry to exit")
        print("3. Rotate maze colors")
        print("4. Rotate 42 pattern colors")
        print("5. Re-generate new maze with PRIM Algorithm")
        print("6. Animate several colored mazes")
        print("7. Quit")
        print("(R/G/B). Specific 42 pattern color")
        print(f"Seed_Code: {self.maze.seed_code}")

    def put_parameters(self) -> None:
        """
        Display an interactive menu for maze generation and visualization
        control.

        Presents a menu with the following options:
        1. Re-generate new maze - Creates a new maze, solves it, and resets
        visualization
        2. Show/Hide path from entry to exit - Toggles the solution path
        visibility
        3. Rotate maze colors - Randomly changes the maze display color
        4. Rotate 42 pattern colors - Randomly changes the pattern display
        color
        5. Change algorithm for the maze - Generates new maze using DFS or
        PRIM algorithm
        6. Quit - Exits the application

        Continuously prompts user for input until a valid selection (1-6) is
        made.
        Handles invalid input gracefully with error messaging.

        Raises:
            SystemExit: When user selects option 6 (Quit).
        """
        while True:
            self.print_menu()
            try:
                select: str = input("Choice? (1 - 7 | R/G/B): ")
                if select not in ["1", "2", "3", "4", "5", "6", "7",
                                  "r", "g", "b", "R", "G", "B"]:
                    raise ValueError()
            except (ValueError, UnboundLocalError):
                print(f"{Colors.RED.value}[ERROR] - Invalid selection. "
                      f"Try again...\n {Colors.RESET.value}")
                continue

            if select == "7":  # key 6/ESC
                sys.exit(0)
            elif select == "1":  # key 1: Re-generate new maze
                self.draw_maze_by_op(Colors.WHITE.value, Colors.WHITE.value)
            elif select == "2":  # key 2: Show/Hide path
                self.show_solution = not self.show_solution
                self.render_visual()
            elif select == "3":  # key 3: Rotate maze colors
                self.maze_color = choice(self.get_display_colors()).value
                self.render_visual()
            elif select == "4":  # key 4: Rotate 42 pattern colors
                self.pattern_color = choice(self.get_display_colors()).value
                self.render_visual()
            elif select == "5":  # key 5: Change algorithm for the maze
                self.draw_maze_by_op(Colors.WHITE.value, Colors.WHITE.value,
                                     MazeAlgorithm.PRIM.value)
            elif select == "6":  # key 6: Animate several mazes
                self.animate_colored_mazes()
            elif select == "r" or select == "R":  # key r/R Pattern in Red
                self.pattern_color = Colors.RED.value
                self.render_visual()
            elif select == "g" or select == "G":  # key g/G Pattern in Green
                self.pattern_color = Colors.GREEN.value
                self.render_visual()
            elif select == "b" or select == "B":  # key b/B Pattern in Blue
                self.pattern_color = Colors.BLUE.value
                self.render_visual()
            else:
                print(f"{Colors.RED.value}[ERROR] - Invalid selection. "
                      f"Try again...\n {Colors.RESET.value}")

    def start_visual(self) -> None:
        """
        Initialize and display the visual representation of the maze.

        This method orchestrates the complete visual setup process by:
        1. Retrieving the solution coordinates
        2. Clearing the screen for a fresh display
        3. Printing the maze in ASCII format
        4. Displaying the maze parameters

        Returns:
            None
        """
        self.render_visual()
        self.put_parameters()
