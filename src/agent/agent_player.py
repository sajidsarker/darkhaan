#!/usr/bin/python3

import math

from agent.agent import *

class AgentPlayer(Agent):
    def __init__(self, x: float, y: float, z: float = 0.0) -> None:
        super().__init__(x, y, z, '../assets/sprites/agent_player.png',
                         image_index=0.0,
                         image_speed=0.0,
                         image_width = 32.0,
                         image_height = 32.0)

    def update(self, delta_time: float) -> None:
        _h: int = 0
        _v: int = 0

        if self.instancer.key_pressed['k_right'] == True and self.instancer.key_pressed['k_left'] == False:
            _h = 1

        if self.instancer.key_pressed['k_right'] == False and self.instancer.key_pressed['k_left'] == True:
            _h = -1

        if self.instancer.key_down['k_down'] == True and self.instancer.key_down['k_up'] == False:
            _v = 1

        if self.instancer.key_down['k_down'] == False and self.instancer.key_down['k_up'] == True:
            _v = -1

        if self.position[0] % 16.0 == 0 and self.position[1] % 16.0 == 0 and self.position[2] % 90.0 == 0:
            self.set_velocity(0.0, 0.0, 0.0)

            if abs(_h) > 0:
                self.set_velocity(0.0, 0.0, _h * 5.0)
                _v = 0

            if abs(_v) > 0:
                _x: float = 3.0 * math.cos(self.position[2] * _v * math.pi / -180.0)
                _y: float = 3.0 * math.sin(self.position[2] * _v * math.pi / -180.0)
                self.set_velocity(_x, _y, 0.0)

        for i in range(len(self.position)):
            self.position[i] += self.velocity[i]

        if self.position[2] < 0.0:
            self.position[2] += 360.0

        if self.position[2] >= 360.0:
            self.position[2] -= 360.0

        self.sprite.rect.center = (self.position[0], self.position[1])