#!/usr/bin/python3

import pygame

DIMENSION: float = 64.0

class Sprite(pygame.sprite.Sprite):
    image_index: float
    image_speed: float
    image_width: float
    image_height: float

    def __init__(self, sprite_index: str, image_index: float = 0.0, image_speed: float = 1.0, image_width: float = DIMENSION, image_height: float = DIMENSION) -> None:
        super().__init__()
        self.image = pygame.image.load(sprite_index).convert_alpha()
        self.image_index = image_index
        self.image_speed = image_speed
        self.image_width = image_width
        self.image_height = image_height
        self.rect = self.image.get_rect()
