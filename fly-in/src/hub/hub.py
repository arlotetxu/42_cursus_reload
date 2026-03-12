import sys
from src.conf.enums import Colors
from icecream import ic

class Hub:

    def __init__(self, name: str, x: int, y: int, color: str, zone: str):
        self.name = name
        self.x = x
        self.y = y
        self.color = color
        self.zone = zone
        self.cross: bool = True
        self.conn: list = []

    