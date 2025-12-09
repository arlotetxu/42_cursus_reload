#!/usr/bin/env python3

class GardenError(Exception):
    def __init__(self, msg: str):
        self.msg = msg


