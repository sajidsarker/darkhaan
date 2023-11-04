#!/usr/bin/python3

from typing import List
from attribute.base_attribute import *
from attribute.raw_bonus import *
from attribute.final_bonus import *

class Attribute(BaseAttribute):
    raw_bonuses: List
    final_bonuses: List
    final_value: int

    def __init__(self, name: str, value: int = 0) -> None:
        super().__init__(name, value)
        self.raw_bonuses = []
        self.final_bonuses = []
        self.final_value = self.base_value

    def add_raw_bonus(self, bonus: RawBonus) -> None:
        self.raw_bonuses.append(bonus)

    def add_final_bonus(self, bonus: FinalBonus) -> None:
        self.final_bonuses.append(bonus)

    def remove_raw_bonus(self, bonus: RawBonus) -> None:
        if self.raw_bonuses.index(bonus) >= 0:
            self.raw_bonuses.remove(self.raw_bonuses.index(bonus))

    def remove_final_bonus(self, bonus: FinalBonus) -> None:
        if self.final_bonuses.index(bonus) >= 0:
            self.final_bonuses.remove(self.final_bonuses.index(bonus))

    def apply_raw_bonuses(self) -> None:
        raw_bonus_value: float = 0.0
        raw_bonus_multiplier: float = 0.0

        for bonus in self.raw_bonuses:
            raw_bonus_value += bonus.base_value
            raw_bonus_multiplier += bonus.base_multiplier
        
        self.final_value += raw_bonus_value
        self.final_value *= (1 + raw_bonus_multiplier)

    def apply_final_bonuses(self) -> None:
        final_bonus_value: float = 0.0
        final_bonus_multiplier: float = 0.0

        for bonus in self.final_bonuses:
            final_bonus_value += bonus.base_value
            final_bonus_multiplier += bonus.base_multiplier
        
        self.final_value += final_bonus_value
        self.final_value *= (1 + final_bonus_multiplier)

    def calculate_value(self) -> int:
        self.final_value = self.base_value
        self.apply_raw_bonuses()
        self.apply_final_bonuses()
        return self.final_value

    def get_final_value(self) -> int:
        return self.calculate_value()

    final_value = property(get_final_value)