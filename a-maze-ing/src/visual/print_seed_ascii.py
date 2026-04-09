import os
from src.model.cell import Cell
from src.config.enums import Colors, Walls
from src.model.seed import Seed
from typing import Any


class SeedPainter_ascii:
    """
    SeedPainter_ascii

    A class responsible for rendering and displaying ASCII art representations
    of mazes loaded from a seed file.
    Provides functionality to visualize maze structures and solutions through
    a command-line interface.

    Attributes:
        seed (Seed): The seed object containing the maze structure and
        configuration.
        seed_config (dict): Configuration dictionary with seed metadata
        (dimensions, entry/exit points, solution string, etc.).
        seed_color (str): ANSI color code for maze walls and borders.
        pattern_color (str): ANSI color code for the 42 pattern cells.
        show_solution (bool): Flag to toggle visualization of the solution
        path.

    Methods:
        get_solution_coord() -> set[tuple]:
            Parses the solution string from seed metadata and returns a set
            of (x, y) coordinates representing the path from entry to exit.

        print_maze_ascii() -> None:
            Renders the maze as ASCII art using box-drawing characters.

        clear_screen() -> None:
            Clears the terminal/console screen.

        start_visual() -> None:
            Main entry point that clears the screen and renders the maze.
    """
    def __init__(self, seed: Seed, seed_config: dict[str, Any]) -> None:
        """
        Initialize the ASCII seed painter.

        Args:
            seed (Seed): The seed object to be printed.
            seed_config (dict): Configuration dictionary for seed settings.

        Attributes:
            seed (Seed): The seed object to be printed.
            seed_config (dict): Configuration dictionary for seed settings.
            seed_color (str): Color for maze elements (default: WHITE).
            pattern_color (str): Color for pattern elements (default: WHITE).
            show_solution (bool): Flag to display the maze solution (default:
            True).
        """
        self.seed: Seed = seed
        self.seed_config: dict[str, Any] = seed_config
        self.seed_color = Colors.WHITE.value
        self.pattern_color = Colors.WHITE.value
        self.show_solution: bool = True

    def print_maze_ascii(self) -> None:
        """
        Print a visual ASCII representation of the maze to the console.

        Renders the maze using box-drawing characters with the following
        features:
        - Displays the maze grid with walls represented by lines
        - Highlights the solution path in blue (if show_solution is enabled)
        - Marks the start cell in green and exit cell in red
        - Uses pattern color to fill cells marked as FORTY_TWO
        - Applies maze color to all structural elements (walls and borders)

        Returns:
            None
        """
        w, h = self.seed_config.get("seed_width", 0), \
            self.seed_config.get("seed_height", 0)
        solution: set[tuple[int, int]] = self.seed.get_solution_coord()
        seed_color: str = self.seed_color
        pattern_color: str = self.pattern_color

        # Top line
        sup: str = "┌" + "───┬" * (w - 1) + "───┐"
        print(f"{seed_color}{sup} {Colors.RESET.value}")

        for y in range(h):
            # Cell lines (content + vertical walls)
            line: str = "│"
            for x in range(w):
                cell: Cell | None = self.seed.get_cell(x, y)
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
                    line += f"{seed_color}│{Colors.RESET.value}" \
                            if cell.walls[Walls.E.value] else " "
                elif cell and cell.is_FORTY_TWO:
                    line += f"{pattern_color}███{seed_color}│"\
                            f"{Colors.RESET.value}"
            print(f"{seed_color}{line} {Colors.RESET.value}")

            # Bottom line
            if y < h - 1:
                line = "├"
                for x in range(w):
                    cell = self.seed.get_cell(x, y)
                    if cell:
                        line += "───" if cell.walls["S"] else "   "
                        line += "┼" if x < w - 1 else "┤"
                print(f"{seed_color}{line} {Colors.RESET.value}")
            else:
                # Bottom border
                last = "└" + "───┴" * (w - 1) + "───┘"
                print(f"{seed_color}{last} {Colors.RESET.value}")

        print(f"\n{Colors.GREEN.value}MAZE SEED REPRESENTATION "
              f"IN ASCII OUTPUT.\n{Colors.RESET.value}")

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

    # Note: An earlier interactive `put_parameters` menu implementation was
    # present here as a large commented-out block of code. It has been
    # removed to avoid keeping stale, dead code in the module. Reintroduce
    # the interactive menu logic here if/when it is needed again.

    def start_visual(self) -> None:
        """
        Initialize and display the visual representation of the seed maze.

        This method orchestrates the complete visual setup process by:
        1. Clearing the screen for a fresh display
        2. Printing the maze in ASCII format

        Returns:
            None
        """
        self.clear_screen()
        self.print_maze_ascii()
