#!/usr/bin/python3

from attribute.base_attribute import *

class RawBonus(BaseAttribute):
    def __init__(self, name: str, value: int = 0, multiplier: float = 0.0) -> None:
        super().__init__(name, value, multiplier)