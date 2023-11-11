#!/usr/bin/python3

from typing import Tuple
from camera.raycast import *

RESOLUTION: Tuple[float] = (640.0, 480.0)
HALF_WIDTH: float = RESOLUTION[0] * 0.5
HALF_HEIGHT: float = RESOLUTION[1] * 0.5
FIELD_OF_VIEW: float = 66.0
HALF_FIELD_OF_VIEW: float = FIELD_OF_VIEW * 0.5
RENDER_DELAY: float = 30.0
DELTA_ANGLE: float = FIELD_OF_VIEW / RESOLUTION[0]
PRECISION: float = 64.0
NUM_RAYS: int = FIELD_OF_VIEW

class Camera:
    ray: Raycast

    def __init__(self, position: List[float], direction: float = 0.0) -> None:
        self.ray = Raycast(position, direction)

    def update(self, direction: float) -> None:
        self.ray.cast(direction, FIELD_OF_VIEW, HALF_FIELD_OF_VIEW, NUM_RAYS, DELTA_ANGLE)

    def render(self, screen) -> None:
        pass