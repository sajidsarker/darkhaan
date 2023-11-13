#!/usr/bin/python3

from typing import List, Dict

import os
import pygame

class TextureCache:
    data: Dict[str, Dict]

    def __init__(self, file_path: str):
        self.data = {}
        self.load(file_path)

    def load(self, file_path: str) -> None:
        _tex: List = [os.path.join(directory_path, file) for (directory_path, directory_name, file_name) in os.walk(file_path) for file in file_name]

        for i in range(len(_tex)):
            _fragment: List[str] = _tex[i].split('_')
            if _fragment[1].rfind('.png') > -1:
                _index: List[str] = _fragment[0].split('/')
                if _index[len(_index) - 1] in self.data.keys():
                    self.data[_index[len(_index) - 1]].update({int(_fragment[1].split('.')[0]): pygame.image.load(_tex[i])})
                else:
                    self.data[_index[len(_index) - 1]] = {
                        int(_fragment[1].split('.')[0]),
                        pygame.image.load(_tex[i])
                    }

        print('[!] Texture Cache Initialised: {}'.format(self.data))