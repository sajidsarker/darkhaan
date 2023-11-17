#!/usr/bin/python3

import math

from agent.agent import *

DIMENSION: float = 64.0

class AgentNPC(Agent):
    conversation: str

    def __init__(self, x: float, y: float, z: float = 0.0) -> None:
        super().__init__(x, y, z, '../assets/sprites/agent_player.png',
                         image_index = 0.0,
                         image_speed = 0.0,
                         image_width = DIMENSION,
                         image_height = DIMENSION)
        self.sprite.rect.center = (self.position[0] + self.sprite.image_width * 0.5, self.position[1] + self.sprite.image_height * 0.5)

    def assign_conversation(self, conversation: str) -> None:
        self.conversation = conversation

    def interact(self) -> None:
        print('[?] Interacted.')
        self.instancer.conversation_manager.play(self.conversation)

    def update(self, delta_time: float) -> None:
        super().update(delta_time)