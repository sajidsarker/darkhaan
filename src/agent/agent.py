#!/usr/bin/python3

from typing import List
from sprite.sprite import *

DIMENSION: float = 64.0

class Agent:
    instancer = None
    position: List[float]
    velocity: List[float]
    sprite: Sprite

    def __init__(self, x: float, y: float, z: float,
                 sprite_index: str,
                 image_index: float = 0.0,
                 image_speed: float = 1.0,
                 image_width: float = DIMENSION,
                 image_height: float = DIMENSION) -> None:
        self.position = [x, y, z]
        self.velocity = [0.0, 0.0, 0.0]
        self.sprite = Sprite(sprite_index, image_index, image_speed, image_width, image_height)
        self.sprite.rect.center = (x + self.sprite.image_width * 0.5, y + self.sprite.image_height * 0.5)

    def get_position(self) -> List[float]:
        return self.position

    def set_position(self, x: float, y: float, z: float) -> None:
        self.position[0] = x
        self.position[1] = y
        self.position[2] = z

    def get_velocity(self) -> List[float]:
        return self.velocity

    def set_velocity(self, vx: float, vy: float, vz: float) -> None:
        self.velocity[0] = vx
        self.velocity[1] = vy
        self.velocity[2] = vz

    def update(self, delta_time: float) -> None:
        for i in range(len(self.position)):
            self.position[i] += self.velocity[i]

        self.sprite.rect.center = (self.position[0] + self.sprite.image_width * 0.5, self.position[1] + self.sprite.image_height * 0.5)