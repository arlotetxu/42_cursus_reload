from enum import Enum


class Colors(Enum):
    """
    This enum provides standard ANSI escape sequences for coloring and styling
    text in terminal/console applications.
    Attributes:
        RESET: Resets all formatting to default.
        BLACK: Black text color.
        ...
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
    PURPLE = "\033[38;5;128m"
    BROWN = "\033[38;5;130m"
    ORANGE = "\033[38;5;208m"
    MAROON = "\033[38;5;52m"
    GOLD = "\033[38;5;220m"
    DARKRED = "\033[38;5;88m"
    CRIMSON = "\033[38;5;197m"
    VIOLET = "\033[38;5;93m"
    RAINBOW = "\033[1m""\033[32m"
