#!/usr/bin/python3

from typing import List, Dict, Tuple

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
            for i in range(self.width):
                self.data['fog'][i].append(False)

        self.reveal(self.spawn_position)

        _file.close()

    def generate(self) -> None:
        pass

    def reveal(self, position: Tuple[int]) -> None:
        self.data['fog'][position[1]][position[0]] = True
        self.data['fog'][max(position[1]-1, 0)][position[0]] = True
        self.data['fog'][min(position[1]+1, self.width-1)][position[0]] = True
        self.data['fog'][position[1]][max(position[0]-1, 0)] = True
        self.data['fog'][position[1]][min(position[0]+1, self.height-1)] = True