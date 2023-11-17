#!/usr/bin/python3

from typing import List, Tuple

import math
import pygame

RESOLUTION: Tuple[int, int] = (640, 480)
HALF_WIDTH: float = RESOLUTION[0] * 0.5
HALF_HEIGHT: float = RESOLUTION[1] * 0.5
FIELD_OF_VIEW: float = 60.0
HALF_FIELD_OF_VIEW: float = FIELD_OF_VIEW / 2
SCALE_FACTOR: int = 2
PRECISION: float = 64.0
DIMENSION: float = 64.0
NUM_RAYS: int = RESOLUTION[0] // SCALE_FACTOR
DELTA_ANGLE: float = FIELD_OF_VIEW / NUM_RAYS

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

        _angle: float = self.position[2] - HALF_FIELD_OF_VIEW

        for i in range(NUM_RAYS):
            _x: float = (self.position[0] + DIMENSION / 2) / PRECISION
            _y: float = (self.position[1] + DIMENSION / 2) / PRECISION
    
            _cos: float = math.cos(math.radians(_angle)) / PRECISION
            _sin: float = math.sin(math.radians(_angle)) / PRECISION

            _hit: int = 0
            _tex: int = 0
            _npc: int = None

            while _hit == 0:
                _x += _cos
                _y += _sin
                _hit = self.instancer.map.data['collisions'][int(math.floor(_y))][int(math.floor(_x))]

            _tex = self.instancer.map.data['tiles'][int(math.floor(_y))][int(math.floor(_x))]
            _npc = self.instancer.map.data['agents'][int(math.floor(_y))][int(math.floor(_x))]

            if _hit == 1:
                _distance: float = math.sqrt(math.pow((self.position[0] + DIMENSION / 2.0) - _x * DIMENSION, 2) + math.pow((self.position[1] + DIMENSION / 2.0) - _y * DIMENSION, 2))

                # Fish-eye effect correction
                _distance = _distance * math.cos(math.radians(_angle - self.position[2]))

                _wall_height: float = HALF_HEIGHT / _distance * DIMENSION * 2.0

                #_texel = self.instancer.texture_cache.data['texture0'][_tex].subsurface((i % DIMENSION, 0.0), (1.0, DIMENSION))
                _texel = self.instancer.texture_cache.data['texture0'][0].subsurface((i % DIMENSION, 0.0), (1.0, DIMENSION))
                _texel = pygame.transform.scale(_texel, (SCALE_FACTOR, _wall_height))
                screen.blit(_texel, (i * SCALE_FACTOR, HALF_HEIGHT - _wall_height / 2))

            _angle += DELTA_ANGLE