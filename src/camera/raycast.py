#!/usr/bin/python3

from typing import List

import math

class Raycast:
    position: List[float]
    direction: float

    def __init__(self, position: List[float]):
        self.position = position
        self.direction = position[2]

    def cast(self, half_field_of_view: float,
                    half_height: float,
                    num_rays: int,
                    delta_angle: float,
                    precision: float) -> None:
        _angle: float = self.direction - half_field_of_view

        for i in range(num_rays):
            _x: float = self.position[0]
            _y: float = self.position[1]
            _cos: float = math.cos(math.radians(_angle)) / precision
            _sin: float = math.sin(math.radians(_angle)) / precision
            _wall: int = 0

            while _wall == 0:
                _x += _cos
                _y += _sin
                _wall = self.instancer.instancer.map.data['collisions'][int(math.floor(_y))][int(math.floor(_x))]

            _distance: float = math.sqrt(math.pow(self.position[0] - _x, 2) + math.pow(self.position[1] - _y, 2))

            # Fish-eye effect correction
            _distance = _distance * math.cos(math.radians(_angle - self.direction))

            _wall_height: float = math.floor(half_height / _distance)

            '''
            render
            '''

            _angle += delta_angle

    def update(self, position: List[float]) -> None:
        self.position = position
        self.direction = position[2]