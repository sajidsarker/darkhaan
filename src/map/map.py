#!/usr/bin/python3

from typing import List, Dict, Tuple
from ui.ui_helper import *

class Map:
    id: int
    width: int
    height: int
    spawn_position: Tuple[int]
    data: Dict[str, List[List[int]]]

    def __init__(self, filename: str) -> None:
        self.data = {
            'collisions': [],
            'fog': [],
            'tiles': [],
            'items': [],
            'agents': []
        }
        self.load(filename)

    def load(self, filename: str) -> None:
        _file = open(filename, 'r')

        self.id = int(_file.readline())
        self.width = int(_file.readline())
        self.height = int(_file.readline())
        self.spawn_position = (int(_file.readline()), int(_file.readline()))

        for i in range(self.height):
            self.data['collisions'].append(_file.readline().split(','))

        for i in range(self.height):
            self.data['tiles'].append(_file.readline().split(','))

        for i in range(self.height):
            self.data['fog'].append([])
            for j in range(self.width):
                self.data['fog'][i].append(False)

        self.reveal([self.spawn_position[0], self.spawn_position[1]])

        _file.close()

    def generate(self) -> None:
        pass

    def reveal(self, position: List[int]) -> None:
        _x: int = int(position[0] / 32.0)
        _y: int = int(position[1] / 32.0)
        self.data['fog'][_y][_x] = True
        self.data['fog'][max(_y-1, 0)][_x] = True
        self.data['fog'][min(_y+1, self.height-1)][_x] = True
        self.data['fog'][_y][max(_x-1, 0)] = True
        self.data['fog'][_y][min(_x+1, self.width-1)] = True

    def update(self, position: List[int]) -> None:
        self.reveal(position)

    def render(self, position: List[int], screen) -> None:
        '''
        for row in range(0, self.height, 1):
            for col in range(0, self.width, 1):
                if self.data['fog'][row][col] == False:
                    draw_sprite((col * 32.0, row * 32.0), '../assets/sprites/agent_player.png', screen)
        '''

        _w: int = 4
        _h: int = 4
        _x: int = int(position[0] / 32.0)
        _y: int = int(position[1] / 32.0)
        _offset: Tuple[float] = (16.0, 16.0)
        i, j = 0, 0
        for row in range(_y - _h, _y + _h, 1):
            i = 0
            for col in range(_x - _w, _x + _w, 1):
                if row >= 0 and row <= self.height - 1 and col >= 0 and col <= self.width - 1:
                    if self.data['fog'][row][col] == True:
                        draw_sprite((_offset[0] + 8.0 * i, _offset[1] + 8.0 * j), '../assets/sprites/minimap_cell_empty.png', screen)
                    else:
                        draw_sprite((_offset[0] + 8.0 * i, _offset[1] + 8.0 * j), '../assets/sprites/minimap_cell_full.png', screen)
                i += 1
            j += 1