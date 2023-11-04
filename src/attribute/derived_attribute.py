#!/usr/bin/python3

from typing import List
from attribute.attribute import *

class DerivedAttribute(Attribute):
    component_attributes: List

    def __init__(self, name: str, value: int) -> None:
        super().__init__(name, value)
        self.component_attributes = []

    def add_attribute(self, attr: Attribute) -> None:
        self.component_attributes.append(attr)

    def remove_attribute(self, attr: Attribute) -> None:
        if self.component_attributes.index(attr) >= 0:
            self.component_attributes.remove(self.component_attributes.index(attr))