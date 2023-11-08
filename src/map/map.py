#!/usr/bin/python3

from typing import List

class Map:
    width: int
    height: int
    data: List[List[int]]

    def __init__(self, filename: str):
        self.width = 0
        self.height = 0
        self.data = None

    def load(self, filename: str):
        pass

    def generate(self):
        pass