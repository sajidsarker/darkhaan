#!/usr/bin/python3

from typing import List

DIMENSION: float = 64.0
MAXIMUM_DEPTH: float = 30.0 * DIMENSION

class Raycast:
    direction: float

    def __init__(self, direction: float):
        self.direction = direction