#!/usr/bin/python3

from typing import List

import math

class Raycast:
    direction: float

    def __init__(self, position: List[float], direction: float = 0.0):
        self.position = position
        self.direction = direction

    def cast(self, field_of_view: float, half_field_of_view: float, num_rays: int, delta_angle: float) -> None:
        pass