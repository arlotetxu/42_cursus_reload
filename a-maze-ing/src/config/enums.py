from enum import Enum


class Colors(Enum):
    """
    ANSI color and text formatting codes for terminal output.
    This enum provides standard ANSI escape sequences for coloring and styling
    text in terminal/console applications.
    Attributes:
        RESET: Resets all formatting to default.
        BLACK: Black text color.
        RED: Red text color.
        GREEN: Green text color.
        YELLOW: Yellow text color.
        BLUE: Blue text color.
        MAGENTA: Magenta text color.
        CYAN: Cyan text color.
        WHITE: White text color.
        BOLD: Bold/bright text formatting.
    Example:
        >>> print(f"{Colors.RED.value}Error occurred{Colors.RESET.value}")
        Error occurred (displayed in red)
    """
    RESET = "\033[0m"
    # BLACK = "\033[30m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"
    WHITE = "\033[37m"
    # BOLD = "\033[1m"


class ColorsHex(Enum):
    """
    An enumeration of hexadecimal color values.
    This enum defines a collection of common colors represented as 32-bit
    hexadecimal values,  where the format is 0xAARRGGBB (Alpha, Red, Green,
    Blue).

    Attributes:
        WHITE (int): Pure white color (0xFFFFFFFF)
        BLACK (int): Pure black color (0xFF000000)
        RED (int): Pure red color (0xFFFF0000)
        GREEN (int): Pure green color (0xFF00FF00)
        BLUE (int): Pure blue color (0xFF0000FF)
        YELLOW (int): Pure yellow color (0xFFFFFF00)
        CYAN (int): Pure cyan color (0xFF00FFFF)
        MAGENTA (int): Pure magenta color (0xFFFF00FF)
        GRAY (int): Medium gray color (0xFF808080)
        ORANGE (int): Orange color (0xFFFFA500)
        PURPLE (int): Purple color (0xFF800080)
        BROWN (int): Brown color (0xFFA52A2A)
        PINK (int): Light pink color (0xFFFFC0CB)
        LIME (int): Lime green color (0xFF32CD32)
    """
    WHITE = 0xFFFFFFFF
    BLACK = 0xFF000000
    RED = 0xFFFF0000
    GREEN = 0xFF00FF00
    BLUE = 0xFF0000FF
    YELLOW = 0xFFFFFF00
    CYAN = 0xFF00FFFF
    MAGENTA = 0xFFFF00FF
    GRAY = 0xFF808080
    ORANGE = 0xFFFFA500
    PURPLE = 0xFF800080
    BROWN = 0xFFA52A2A
    PINK = 0xFFFFC0CB
    LIME = 0xFF32CD32


class Walls(Enum):
    """
    Enum representing the four cardinal directions as maze wall positions.

    Attributes:
        N (str): North wall direction.
        S (str): South wall direction.
        E (str): East wall direction.
        W (str): West wall direction.
    """
    N = "N"
    S = "S"
    E = "E"
    W = "W"


class PrintMode(Enum):
    """
    Enum class defining the available print/display modes for the maze
    application.

    Attributes:
        MLX (str): Graphics mode using the MLX library for graphical rendering.
        ASCII (str): Text-based mode using ASCII characters for terminal
        display.
    """
    MLX = "MLX"
    ASCII = "ASCII"


class MazeAlgorithm(Enum):
    """
    Enum class for maze generation algorithms.

    Attributes:
        DFS (str): Depth-first search algorithm for maze generation.
        PRIM (str): Prim's algorithm for maze generation.
    """
    DFS = "DFS"  # Depth-first search
    PRIM = "PRIM"
