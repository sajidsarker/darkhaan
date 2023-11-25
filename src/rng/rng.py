#!/usr/bin/python3

import random

def roll_d(sides: int, num: int) -> int:
    value: int = random.choice(range(1, (sides + 1) * num))
    return value

def roll_d4(num: int) -> int:
    return roll_d(4, num)

def roll_d6(num: int) -> int:
    return roll_d(6, num)

def roll_d8(num: int) -> int:
    return roll_d(8, num)

def roll_d10(num: int) -> int:
    return roll_d(10, num)

def roll_d12(num: int) -> int:
    return roll_d(12, num)

def roll_d20(num: int) -> int:
    return roll_d(20, num)