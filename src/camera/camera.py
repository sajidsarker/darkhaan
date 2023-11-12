#!/usr/bin/python3

from typing import List, Tuple
from camera.raycast import *

RENDER_DELAY: float = 30.0
RESOLUTION: Tuple[int, int] = (640, 480)
HALF_WIDTH: float = RESOLUTION[0] * 0.5
HALF_HEIGHT: float = RESOLUTION[1] * 0.5
FIELD_OF_VIEW: float = 66.0
HALF_FIELD_OF_VIEW: float = FIELD_OF_VIEW * 0.5
NUM_RAYS: int = RESOLUTION[0]
DELTA_ANGLE: float = FIELD_OF_VIEW / RESOLUTION[0]
PRECISION: float = 64.0

class Camera:
    ray: Raycast

    def __init__(self, position: List[float]) -> None:
        self.ray = Raycast(position)
        self.ray.instancer = self

    def update(self, position: List[float]) -> None:
        self.ray.update(position)
        #self.ray.cast(HALF_FIELD_OF_VIEW, HALF_HEIGHT, NUM_RAYS, DELTA_ANGLE, PRECISION)

    def render(self, screen) -> None:
        pass