#!/usr/bin/python3

from typing import List
from camera.raycast import *

FIELD_OF_VIEW: float = 66.0

class Camera:
    rays: List[Raycast] = []

    def __init__(self, direction: float, num_rays: int):
        _delta_angle: float = FIELD_OF_VIEW / num_rays
        for i in range(num_rays):
            self.rays.append(Raycast(direction - FIELD_OF_VIEW * 0.5 + i * _delta_angle))

    def update(self, direction: float):
        _delta_angle: float = FIELD_OF_VIEW / len(self.rays)
        for i in range(len(self.rays)):
            self.rays[i].direction = direction - FIELD_OF_VIEW * 0.5 + i * _delta_angle

    def render(self, screen):
        pass