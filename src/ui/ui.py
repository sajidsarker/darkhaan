#!/usr/bin/python3

import pygame

from typing import Tuple

pygame.font.init()

FONT = pygame.font.Font('../assets/fonts/Ac437_Acer_VGA_8x8.ttf')

BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)
GREEN = (  0, 255,   0)
BLUE  = (  0,   0, 255)

def draw_text(position: Tuple[float, float], text: str, colour: Tuple, screen) -> None:
    screen.blit(FONT.render(text, True, colour), position)

def draw_sprite(position: Tuple[float, float], sprite_index: str, screen) -> None:
    sprite = pygame.image.load(sprite_index).convert_alpha()
    screen.blit(sprite, position)