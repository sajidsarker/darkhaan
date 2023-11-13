#!/usr/bin/python3

from typing import List, Tuple

import math
import pygame

RENDER_DELAY: float = 30.0
RESOLUTION: Tuple[int, int] = (640, 480)
HALF_WIDTH: float = RESOLUTION[0] * 0.5
HALF_HEIGHT: float = RESOLUTION[1] * 0.5
FIELD_OF_VIEW: float = 60.0
HALF_FIELD_OF_VIEW: float = FIELD_OF_VIEW * 0.5
NUM_RAYS: int = 160
#NUM_RAYS: int = RESOLUTION[0]
DELTA_ANGLE: float = FIELD_OF_VIEW / RESOLUTION[0]
PRECISION: float = 64.0

BLACK = (  0,   0,   0)
GREY  = (125, 125, 125)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)
GREEN = (  0, 255,   0)
BLUE  = (  0,   0, 255)

class Camera:
    position: List[float]

    def __init__(self, position: List[float]) -> None:
        self.position = position

    def update(self, position: List[float]) -> None:
        self.position = position

    def render(self, screen) -> None:
        pygame.draw.rect(screen, GREY, pygame.Rect((0.0, HALF_HEIGHT), (RESOLUTION[0], HALF_HEIGHT)))

        _angle: float = self.position[2] - HALF_FIELD_OF_VIEW + 180

        for i in range(NUM_RAYS):
            _x: float = self.position[0] / PRECISION
            _y: float = self.position[1] / PRECISION
            _cos: float = math.cos(math.radians(_angle)) / PRECISION
            _sin: float = math.sin(math.radians(_angle)) / PRECISION
            _wall: int = 0

            while _wall == 0:
                _x += _cos
                _y += _sin
                _wall = self.instancer.map.data['collisions'][int(math.floor(_y))][int(math.floor(_x))]

            _distance: float = math.sqrt(math.pow(self.position[0] - _x, 2) + math.pow(self.position[1] - _y, 2))

            # Fish-eye effect correction
            _distance = _distance * math.cos(math.radians(_angle - self.position[2] + 180))

            _wall_height: float = math.floor(HALF_HEIGHT / _distance) * 64.0

            #drawLine(rayCount, 0, rayCount, data.screen.halfHeight - wallHeight, "cyan");
            #drawLine(rayCount, data.screen.halfHeight - wallHeight, rayCount, data.screen.halfHeight + wallHeight, "red");
            #drawLine(rayCount, data.screen.halfHeight + wallHeight, rayCount, data.screen.height, "green");
            #pygame.draw.line(screen, WHITE, (i * 2, HALF_HEIGHT - _wall_height), (i * 2, HALF_HEIGHT + _wall_height), 2)

            _angle += DELTA_ANGLE