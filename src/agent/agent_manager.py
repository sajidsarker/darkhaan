#!/usr/bin/python3

import pygame

from typing import List
from agent.agent import *
from agent.agent_player import *

class AgentManager:
    instancer = None
    entities: List[Agent]
    sprites = pygame.sprite.Group()

    def __init__(self):
        self.entities = []

    def spawn(self, instance: Agent, x: float, y: float, z: float) -> Agent:
        self.entities.append(instance(x, y, z))
        self.entities[len(self.entities)-1].instancer = self.instancer
        self.sprites.add(self.entities[len(self.entities)-1].sprite)
        return self.entities[len(self.entities)-1]

    def despawn(self, instance: Agent) -> None:
        pass

    def update(self, delta_time) -> None:
        for entity in self.entities:
            entity.update(delta_time)

    def render(self, screen) -> None:
        #self.sprites.draw(screen)
        pass