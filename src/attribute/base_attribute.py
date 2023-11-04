#!/usr/bin/python3

class BaseAttribute:
    name: str
    base_value: int
    base_multiplier: float

    def __init__(self, name: str, value: int = 0, multiplier: float = 0.0) -> None:
        self.name = name
        self.base_value = value
        self.base_multiplier = multiplier

    def get_name(self) -> str:
        return self.name

    def get_base_value(self) -> int:
        return self.base_value

    def set_base_value(self, value: int = 0) -> None:
        self.base_value = max(0, value)

    def get_base_multiplier(self) -> float:
        return self.base_multiplier

    def set_base_multiplier(self, value: float = 0.0) -> None:
        self.base_multiplier = max(0.0, value)

    name = property(get_name)
    base_value = property(get_base_value, set_base_value)
    base_multiplier = property(get_base_multiplier, set_base_multiplier)