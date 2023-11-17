#!/usr/bin/python3

from typing import List, Dict, Tuple
from ui.ui import *

DIMENSION: float = 64.0

class Map:
    id: int
    width: int
    height: int
    spawn_position: Tuple[int]
    data: Dict[str, List[List[int]]]

    def __init__(self, file_name: str) -> None:
        self.data = {
            'collisions': [],
            'fog': [],
            'tiles': [],
            'items': [],
            'agents': []
        }
        self.load(file_name)

    def load(self, file_name: str) -> None:
        _file = open(file_name, 'r')

        self.id = int(_file.readline())
        self.width = int(_file.readline())
        self.height = int(_file.readline())
        self.spawn_position = (int(_file.readline()), int(_file.readline()))

        for i in range(self.height):
            self.data['collisions'].append(_file.readline().split(','))

        for i in range(self.height):
            self.data['tiles'].append(_file.readline().split(','))

        for row in range(self.height):
            for col in range(self.width):
                self.data['collisions'][row][col] = int(self.data['collisions'][row][col])
                self.data['tiles'][row][col] = int(self.data['tiles'][row][col])

        for i in range(self.height):
            self.data['fog'].append([])
            self.data['items'].append([])
            self.data['agents'].append([])
            for j in range(self.width):
                self.data['fog'][i].append(False)
                self.data['items'][i].append(None)
                self.data['agents'][i].append(None)

        self.reveal([self.spawn_position[0], self.spawn_position[1]])

        _file.close()

    def generate(self) -> None:
        pass

    def reveal(self, position: List[int]) -> None:
        _x: int = int(position[0] / DIMENSION)
        _y: int = int(position[1] / DIMENSION)
        self.data['fog'][_y][_x] = True
        self.data['fog'][max(_y - 1, 0)][_x] = True
        self.data['fog'][min(_y + 1, self.height - 1)][_x] = True
        self.data['fog'][_y][max(_x - 1, 0)] = True
        self.data['fog'][_y][min(_x + 1, self.width - 1)] = True

    def update(self, position: List[int]) -> None:
        self.reveal(position)

    def render(self, position: List[int], screen) -> None:
        _w: int = 6
        _h: int = 4
        _x: int = int(position[0] / DIMENSION)
        _y: int = int(position[1] / DIMENSION)
        _offset: Tuple[float] = (16.0, 16.0)

        i, j = 0, 0
        for row in range(_y - _h, _y + _h, 1):
            i = 0
            for col in range(_x - _w, _x + _w, 1):
                if row >= 0 and row <= self.height - 1 and col >= 0 and col <= self.width - 1:
                    if i == _w and j == _h:
                        draw_sprite((_offset[0] + 8.0 * i, _offset[1] + 8.0 * j), '../assets/sprites/minimap_cell_centre.png', screen)
                    elif self.data['collisions'][row][col] == 1:
                        draw_sprite((_offset[0] + 8.0 * i, _offset[1] + 8.0 * j), '../assets/sprites/minimap_cell_full.png', screen)
                    else:
                        draw_sprite((_offset[0] + 8.0 * i, _offset[1] + 8.0 * j), '../assets/sprites/minimap_cell_empty.png', screen)
                i += 1
            j += 1