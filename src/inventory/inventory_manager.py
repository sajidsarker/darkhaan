#!/usr/bin/python3

from typing import Dict
from inventory.item import *

class InventoryManager:
    inventory: Dict[str, Dict[int, int]]

    def __init__(self) -> None:
        self.inventory = {
            'key_item': {},
            'consumable': {},
            'weapon': {},
            'armour': {},
            'accessory': {}
        }

    def add(self, inventory: str, item_id: int, amount: int) -> None:
        assert amount > 0, 'Amount {} must be non-negative.'.format(amount)

        if self.find(inventory, item_id):
            self.inventory[inventory][item_id] = min(999, self.inventory[inventory][item_id] + amount)

        else:
            self.inventory[inventory] = {
                item_id: amount
            }

    def remove(self, inventory: str, item_id: int, amount: int) -> None:
        assert amount > 0, 'Amount {} must be non-negative.'.format(amount)

        if self.find(inventory, item_id):
            self.inventory[inventory][item_id] = max(0, self.inventory[inventory][item_id] - amount)

            if self.inventory[inventory][item_id] == 0:
                del self.inventory[inventory][item_id]

    def find(self, inventory: str, item_id: int) -> bool:
        return True if item_id in self.inventory[inventory].keys() else False