#!/usr/bin/python3

from typing import List
from sprite.sprite import *

class Agent:
    instancer = None
    position: List[float]
    velocity: List[float]
    sprite: Sprite

    def __init__(self, x: float, y: float, z: float,
                 sprite_index: str,
                 image_index: float = 0.0,
                 image_speed: float = 1.0,
                 image_width: float = 32.0,
                 image_height: float = 32.0) -> None:
        self.position = [x, y, z]
        self.velocity = [0.0, 0.0, 0.0]
        self.sprite = Sprite(sprite_index, image_index, image_speed, image_width, image_height)
        self.sprite.rect.center = (x, y)

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

    def update(self) -> None:
        for i in range(len(self.position)):
            self.position[i] += self.velocity[i]

        self.sprite.rect.center = (self.position[0], self.position[1])