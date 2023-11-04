#!/usr/bin/python3

import pygame

from typing import List
from agent.agent import *
from agent.agent_player import *

class AgentSpawner:
    instancer = None
    entities: List[Agent]
    sprites = pygame.sprite.Group()

    def __init__(self):
        self.entities = []

    def spawn(self, instance: Agent, x: float, y: float) -> Agent:
        self.entities.append(instance(x, y))
        self.entities[len(self.entities)-1].instancer = self.instancer
        self.sprites.add(self.entities[len(self.entities)-1].sprite)
        return self.entities[len(self.entities)-1]