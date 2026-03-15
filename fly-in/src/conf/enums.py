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
    BLACK = "\033[30m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"
    WHITE = "\033[37m"
    BOLD = "\033[1m"
