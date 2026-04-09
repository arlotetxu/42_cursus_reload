from src.config.enums import Colors, PrintMode
from typing import Any
from pydantic import BaseModel, Field, model_validator


class ConfigModel(BaseModel):
    """
    Configuration model for maze generation and rendering.

    This model validates and stores configuration parameters for maze creation,
    including dimensions, entry/exit points, output settings, and rendering
    mode.

    Attributes:
        maze_width (int): Width of the maze. Must be at least 7.
        maze_height (int): Height of the maze. Must be at least 7.
        maze_entry (tuple[int, int]): Entry point coordinates (x, y) for the
        maze.
        maze_exit (tuple[int, int]): Exit point coordinates (x, y) for the
        maze.
        maze_output (str): Output file path. Minimum length of 5 characters.
        maze_perfect (bool): Flag indicating if the maze should be perfect (no
        loops).
        maze_print_mode (str): Rendering mode for maze output. Must be 'MLX'
        or 'ASCII'.

    Validators:
        check_entry: Validates that entry coordinates are within maze
        boundaries.
        check_exit: Validates that exit coordinates are within maze boundaries
            and are different from entry coordinates.
        check_print_mode: Validates that the print mode is one of the
        supported options.

    Raises:
        ValueError: If any validation rule is violated with descriptive error
        messages.
    """
    maze_width: int = Field(..., ge=3)
    maze_height: int = Field(..., ge=3)
    maze_entry: tuple[int, int]
    maze_exit: tuple[int, int]
    maze_output: str = Field(..., min_length=5)
    maze_perfect: bool
    maze_print_mode: str = Field(..., min_length=3)
    maze_seed: str = Field(default="",
                           description="Path to seed file for loading "
                           "pre-generated mazes")
    maze_seed_code: int | None = Field(default=None)

    @model_validator(mode='after')
    def check_recursion_limit(self) -> Any:
        """
        Validate that the maze dimensions do not exceed the recursion limit.

        This validator ensures that the total number of cells (width * height)
        is less than 1000. This restriction is in place to prevent
        RecursionError during maze generation or solving algorithms that
        rely on deep recursive calls.

        Returns:
            Self: Returns the instance itself to allow method chaining.

        Raises:
            ValueError: If the product of width and height is 1000 or greater.
        """
        if self.maze_height * self.maze_width >= 1000:
            raise ValueError(
                f"{Colors.RED.value}[ERROR] maze WIDTH * maze HEIGHT must be "
                "less than 1000 to avoid recursion issues. Current cell count "
                f"is {self.maze_width * self.maze_height}. Please check the "
                "maze_width and maze_height values in the config file."
                f"{Colors.RESET.value}")
        return self

    @model_validator(mode='after')
    def check_entry(self) -> Any:
        """
        Validate that the maze entry point coordinates are within valid bounds.

        Checks that the entry point (x, y) coordinates fall within the maze
        dimensions.
        The x coordinate must be between 0 and maze_width - 1 (inclusive), and
        the y
        coordinate must be between 0 and maze_height - 1 (inclusive).

        Returns:
            Self: Returns the instance itself to allow method chaining.

        Raises:
            ValueError: If either the x or y coordinate is outside the valid
            range.
            The error message includes the valid range for each coordinate.
        """
        x, y = self.maze_entry

        if x < 0 or x >= self.maze_width or y < 0 or y >= self.maze_height:
            raise ValueError(
                f"{Colors.RED.value}[ERROR] Entry values are incorrect!!\n"
                f"- For x coord, min: 0 max: {self.maze_width - 1}\n"
                f"- For y coord, min: 0 max: {self.maze_height - 1}"
                f"{Colors.RESET.value}")
        return self

    @model_validator(mode='after')
    def check_exit(self) -> Any:
        """
        Validate that the maze exit coordinates are within bounds and
        different from the entry point.

        Checks that:
        - Exit x coordinate is within [0, maze_width)
        - Exit y coordinate is within [0, maze_height)
        - Exit coordinates are not identical to entry coordinates

        Returns:
            Self: Returns self for method chaining.

        Raises:
            ValueError: If exit coordinates are out of bounds or match entry
            coordinates.
        """
        x, y = self.maze_exit
        w, z = self.maze_entry

        if x < 0 or x >= self.maze_width or y < 0 or y >= self.maze_height:
            raise ValueError(
                f"{Colors.RED.value}[ERROR] Exit values are incorrect!!"
                f"- For x coord, min: 0 max: {self.maze_width - 1}\n"
                f"- For y coord, min: 0 max: {self.maze_height - 1}"
                f"{Colors.RESET.value}")

        if x == w and y == z:
            raise ValueError(
                f"{Colors.RED.value}"
                f"[ERROR] Exit values cannot be the same than Entry!!"
                f"{Colors.RESET.value}")

        return self

    @model_validator(mode='after')
    def check_print_mode(self) -> Any:
        """
        Validates that the maze print mode is one of the supported options.

        This method checks if the configured `maze_print_mode` is a valid
        print mode.
        Currently supported modes are 'MLX' and 'ASCII'. The check is
        case-insensitive.

        Returns:
            Self: Returns the instance itself to allow method chaining.

        Raises:
            ValueError: If `maze_print_mode` is not one of the valid options
            ('MLX' or 'ASCII'). The error message will be displayed in red
            color (if supported).
        """
        if self.maze_print_mode.upper() not in [PrintMode.MLX.value,
                                                PrintMode.ASCII.value]:
            raise ValueError(
                f"{Colors.RED.value}[ERROR] PRINT_MODE value is incorrect!!"
                f"\nValid options: 'MLX' / 'ASCII'{Colors.RESET.value}")

        return self
