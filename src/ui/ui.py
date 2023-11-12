#!/usr/bin/python3

import pygame

from typing import List, Tuple

pygame.font.init()

FONT = pygame.font.Font('../assets/fonts/Ac437_Acer_VGA_8x8.ttf')

BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)
GREEN = (  0, 255,   0)
BLUE  = (  0,   0, 255)

def draw_text(position: Tuple[float, float], text: str, colour: Tuple[float], screen) -> None:
    screen.blit(FONT.render(text, True, colour), position)

def draw_sprite(position: Tuple[float, float], sprite_index: str, screen) -> None:
    sprite = pygame.image.load(sprite_index).convert_alpha()
    screen.blit(sprite, position)

def draw_window(position: Tuple[float, float], size: Tuple[float], text: List[str], colour: Tuple[float], screen) -> None:
    pygame.draw.rect(screen, colour, pygame.Rect(position, size))

    i: int = 0
    for line in text:
        screen.blit(FONT.render(line, True, WHITE), (position[0] + 16, position[1] + 16 + i * 16))
        i += 1