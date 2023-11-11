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
        '''
        start_angle = player_angle - HALF_FOV
        for ray in range(CASTED_RAYS):
            for depth in range(MAX_DEPTH):
                target_x = player_x - math.sin(start_angle) * depth
                target_y = player_y + math.cos(start_angle) * depth
                col = int(target_x / TILE_SIZE)
                row = int(target_y / TILE_SIZE)
                square = row * MAP_SIZE + col
                (target_y / TILE_SIZE) * MAP_SIZE + target_x / TILE_SIZE 
                if MAP[square] == '#':
                    pygame.draw.rect(win,(0,255,0),(col * TILE_SIZE,
                                                    row * TILE_SIZE,
                                                    TILE_SIZE - 2,
                                                    TILE_SIZE - 2))
                    pygame.draw.line(win, (255,255,0),(player_x,player_y),(target_x,target_y))
                    color = 50 / (1 + depth * depth * 0.0001)
                    
                    depth *= math.cos(player_angle - start_angle)
                        
                    wall_height = 21000 / (depth + 0.0001)
                    
                    if wall_height > SCREEN_HEIGHT: wall_height == SCREEN_HEIGHT
                    pygame.draw.rect(win,(color,color,color), (SCREEN_HEIGHT + ray * SCALE,(SCREEN_HEIGHT / 2) - wall_height / 2,SCALE,wall_height))
                    break
            start_angle += STEP_ANGLE
            '''
        pass