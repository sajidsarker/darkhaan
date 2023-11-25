#!/usr/bin/python3

import math

from typing import List, Dict
from attribute.attribute import *
from attribute.derived_attribute import *

class AttributeManager:
    '''
    attributes: Dict[str, Attribute]
    '''
    #strength, vigour, endurance et cetera
    '''
    consumable_attributes: Dict[int]
    '''
    #health, magic, experience
    '''
    derived_attributes: Dict[str, DerivedAttribute]
    '''
    #health, magic

    #level: int = 1
    #max_experience: List = [math.log(x + 1) for x in range(25)]

    def __init__(self) -> None:
    #def __init__(self, attribute_names: List[str], attribute_points: List[int]) -> None:
        '''
        for i in range(len(attribute_points)):
            self.attributes[attribute_points[i]] = Attribute(attribute_names[i], attribute_points[i])
        '''
        pass

    def upgrade_level(self, attribute_points: List[int]) -> None:
        '''
        for i in range(len(attribute_points)):
            self.level += attribute_points[i]

        for attribute in self.attributes:
            self.attributes[attribute.get_name()].base_value += attribute_points

        for derived_attribute in self.derived_attributes:
            self.derived_attributes[derived_attribute.get_name()].calculate_value()
        '''
        pass

    def update(self):
        pass